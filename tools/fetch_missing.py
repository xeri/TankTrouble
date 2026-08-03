#!/usr/bin/env python3
"""Refetch era assets that CDX proves were served but the archive never held.

resolve_assets.py leaves two recoverable verdicts:

  wrong-era-bytes  we hold a copy, it hashes to another era
  cdx-observed     the era window captured the path, we hold nothing

Both name the era digest, so a download is VERIFIABLE: Wayback's id_ raw
endpoint returns the original payload, and base32(SHA1(payload)) must equal
the digest the CDX row recorded. A mismatch is rejected and nothing is
written — that is the whole point of fetching by digest rather than by date.

New bytes land in a fresh archive directory (evidence arrives under archive/,
existing archive files are never touched). Re-run resolve_assets.py and
place_assets.py afterwards to promote them.

    python tools/fetch_missing.py --dry-run
    python tools/fetch_missing.py
"""

import argparse
import base64
import collections
import hashlib
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CHOICES = REPO / "tools" / "asset_choices.tsv"
DEST_DIRNAME = "wayback-images-2026-08-03"
ERA_START, ERA_END = "20170101000000", "20181231235959"
RECOVERABLE = ("wrong-era-bytes", "cdx-observed")
CDX_FILES = [
    "wayback-inventory/cdx-tanktrouble.com.txt",
    "wayback-inventory/cdx-classic.tanktrouble.com.txt",
]
UA = "TankTrouble-reconstruction/1.0 (preservation; contact via repo)"
PAUSE = 1.5          # polite gap between Wayback hits
RETRIES = 3


def archive_root():
    root = os.environ.get("TT_ARCHIVE_ROOT") or str(REPO / "archive")
    p = Path(root)
    if not (p / "includes-tree").is_dir():
        sys.exit("archive root not found: set TT_ARCHIVE_ROOT or create the "
                 "archive junction (see README.md)")
    return p


def load_cdx_rows(root):
    """{served path: [(ts, status, digest, original url)]} sorted by ts."""
    rows = collections.defaultdict(list)
    for rel in CDX_FILES:
        f = root / rel
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            parts = line.split()
            if len(parts) != 6:
                continue
            url, ts, status, _mime, _length, digest = parts
            hostpath = url.split("://", 1)[-1]
            path = "/" + hostpath.split("/", 1)[1] if "/" in hostpath else "/"
            rows[path.split("?", 1)[0]].append((ts, status, digest, url))
    for v in rows.values():
        v.sort()
    return rows


def pick_capture(rows):
    """The era capture to fetch: a status-200 row carrying the digest that
    dominates the era window (revisit rows point at the same payload but have
    no body of their own)."""
    era = [r for r in rows if ERA_START <= r[0] <= ERA_END
           and r[1] in ("200", "-")]
    if not era:
        return None
    counts = collections.Counter(r[2] for r in era)
    want = counts.most_common(1)[0][0]
    for ts, status, digest, url in era:
        if digest == want and status == "200":
            return ts, digest, url, len(era), len(counts)
    # only revisit rows in-era: the payload was first seen outside the window
    for ts, status, digest, url in rows:
        if digest == want and status == "200":
            return ts, digest, url, len(era), len(counts)
    return None


def b32sha1(data):
    return base64.b32encode(hashlib.sha1(data).digest()).decode()


def fetch(ts, url):
    """Wayback raw payload — id_ suppresses the rewriting toolbar."""
    target = f"https://web.archive.org/web/{ts}id_/{url}"
    req = urllib.request.Request(target, headers={"User-Agent": UA})
    last = None
    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            last = e
            time.sleep(PAUSE * (attempt + 2))
    raise RuntimeError(f"{target}: {last}")


def read_judgements():
    """tools/asset_judgements.tsv — hand-made era arguments for paths the
    window never captured. Each names the exact capture and the digest its
    payload must have."""
    f = REPO / "tools" / "asset_judgements.tsv"
    if not f.is_file():
        return []
    lines = f.read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t")
    return [dict(zip(header, l.split("\t"))) for l in lines[1:]
            if l.strip() and not l.lstrip().startswith("#")]


def work_list():
    lines = CHOICES.read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t")
    return [dict(zip(header, l.split("\t"))) for l in lines[1:]
            if l.strip() and l.split("\t")[1] in RECOVERABLE]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    root = archive_root()
    cdx = load_cdx_rows(root)
    dest = root / DEST_DIRNAME
    todo = work_list()
    if args.limit:
        todo = todo[:args.limit]

    print(f"{len(todo)} assets with an era digest to verify against\n")
    got, rejected, nocapture, failed = [], [], [], []

    judged = {j["target"]: j for j in read_judgements()}
    todo = todo + [{"target": t} for t in judged
                   if not (REPO / "srv" / t).is_file()
                   and t not in {c["target"] for c in todo}]

    for c in todo:
        target = c["target"]
        if target in judged:
            j = judged[target]
            pick = (j["capture_ts"], j["expected_digest"], j["capture_url"],
                    0, 1)
        else:
            pick = pick_capture(cdx.get("/" + target, []))
        if not pick:
            nocapture.append(target)
            continue
        ts, digest, url, era_rows, n_digests = pick
        out = dest / f"{ts}_{os.path.basename(target)}"
        if out.is_file() and b32sha1(out.read_bytes()) == digest:
            got.append((target, out, ts, digest, era_rows, n_digests))
            continue
        if args.dry_run:
            print(f"  would fetch {ts} {url}  (era rows {era_rows}, "
                  f"digests in window {n_digests})")
            continue
        try:
            data = fetch(ts, url)
        except RuntimeError as e:
            failed.append((target, str(e)))
            print(f"  FAIL   {target}: {e}")
            continue
        actual = b32sha1(data)
        if actual != digest:
            rejected.append((target, digest, actual))
            print(f"  REJECT {target}: payload {actual} != CDX {digest}")
            continue
        dest.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        got.append((target, out, ts, digest, era_rows, n_digests))
        print(f"  ok     {target} <- {ts} ({len(data)} b, {digest})")
        time.sleep(PAUSE)

    print(f"\nverified {len(got)}   rejected {len(rejected)}   "
          f"no era capture {len(nocapture)}   network failures {len(failed)}")
    if nocapture:
        print("no era capture:", ", ".join(sorted(nocapture)[:12]))
    if not args.dry_run and got:
        print(f"\nbytes in {dest}\n"
              f"next: python tools/resolve_assets.py && "
              f"python tools/place_assets.py")


if __name__ == "__main__":
    main()
