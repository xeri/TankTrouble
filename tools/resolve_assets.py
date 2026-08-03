#!/usr/bin/env python3
"""Era-resolve every subresource gate E reports as absent.

resolve_era.py does this for a hand-listed set of GROUPS. That hand list is
exactly how the /images/ hole happened: assets nobody thought to list were
never resolved, never laid down and never missed, because no check ran from
the page's own references. This tool takes its work list from
tools/refgraph.py instead, so the list cannot drift from what the site asks
for.

Method per asset, same evidence ladder as resolve_era.py:

  era-digest-match   a candidate's base32(SHA1) appears on a CDX row for that
                     path inside 2017-2018        -> tier O
  wrong-era-bytes    candidates held, era CDX rows exist, no digest agrees
                     -> known-lost (what we hold is a different era's file)
  held-no-era-cdx    candidates held, path has no era CDX row at all
                     -> tier O?  (authentic bytes, era service unproven)
  cdx-observed       no candidate held, but the era window captured the path
                     -> known-lost, era digests recorded as a fetch target
  unobserved         no candidate, no era CDX row -> known-lost

Candidate search prefers a copy stored at the SAME served path inside an
archived host tree (strong: proves the site served that name), then falls back
to any file of that basename anywhere in the archive (weak: name collision is
possible, so a weak candidate can only ever reach O via a digest match).

Writes tools/asset_choices.tsv. build_skeleton.py consumes it; nothing copies
bytes from here.
"""

import argparse
import base64
import hashlib
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
import refgraph  # noqa: E402

ERA_START, ERA_END = "20170101000000", "20181231235959"
OUT = REPO / "tools" / "asset_choices.tsv"
HEADER = ["target", "verdict", "tier", "chosen_source", "sha256", "sha1b32",
          "era_digests", "candidates", "notes"]

# CDX dumps for the hosts that served the classic tree. beta/cdn/m hosts are
# a different site generation whose /images/ paths would collide, so they are
# deliberately excluded — a false era match is worse than no match.
CDX_FILES = [
    "wayback-inventory/cdx-tanktrouble.com.txt",
    "wayback-inventory/cdx-classic.tanktrouble.com.txt",
]

# archive host trees, best first: a hit at the same served path is strong
HOST_TREES = [
    "flashpoint-gamezip/content/tanktrouble.com",
    "classic.tanktrouble.com",
    "flashpoint-gamezip/content/www.kongregate.com",
    "elte-mirror",
    "mirror-vseigru",
]


def archive_root():
    root = os.environ.get("TT_ARCHIVE_ROOT") or str(REPO / "archive")
    p = Path(root)
    if not (p / "includes-tree").is_dir():
        sys.exit("archive root not found: set TT_ARCHIVE_ROOT or create the "
                 "archive junction (see README.md)")
    return p


def load_cdx(root):
    """{served path: [(ts, status, digest)]} for the classic hosts."""
    rows = {}
    for rel in CDX_FILES:
        f = root / rel
        if not f.is_file():
            sys.exit(f"missing CDX dump: {f}")
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            parts = line.split()
            if len(parts) != 6:
                continue
            url, ts, status, _mime, _length, digest = parts
            hostpath = url.split("://", 1)[-1]
            path = "/" + hostpath.split("/", 1)[1] if "/" in hostpath else "/"
            rows.setdefault(path.split("?", 1)[0], []).append((ts, status, digest))
    for v in rows.values():
        v.sort()
    return rows


def index_basenames(root):
    """{lowercased basename: [absolute paths]} over the whole archive.

    Capture trees store the served name behind a timestamp prefix
    (includes-tree/20101128_styles.css, wayback-images-*/20180116170808_
    tab1Select.jpg), so each file is indexed under its stored name AND under
    the name with a leading <digits>_ stripped."""
    idx = {}
    for dirpath, _dirs, files in os.walk(root):
        for f in files:
            full = os.path.join(dirpath, f)
            idx.setdefault(f.lower(), []).append(full)
            stripped = re.sub(r"^\d{6,14}_", "", f)
            if stripped != f:
                idx.setdefault(stripped.lower(), []).append(full)
    return idx


def candidates_for(target, root, basename_index):
    """[(archive-relative path, strength)] — strong = stored at the served path."""
    out = []
    for tree in HOST_TREES:
        p = root / tree / target
        # Windows matches paths case-insensitively; the original server did
        # not. Confirm the stored name is byte-identical before calling a
        # candidate strong.
        if p.is_file() and p.name == os.path.basename(target):
            out.append((f"{tree}/{target}", "strong"))
    strong = {c for c, _ in out}
    for hit in basename_index.get(os.path.basename(target).lower(), []):
        rel = os.path.relpath(hit, root).replace("\\", "/")
        if rel not in strong:
            out.append((rel, "weak"))
    return out


def digests_of(path):
    data = Path(path).read_bytes()
    return (hashlib.sha256(data).hexdigest(),
            base64.b32encode(hashlib.sha1(data).digest()).decode())


def read_judgements():
    """Hand-made era arguments for paths the window never captured. See
    tools/asset_judgements.tsv — every row is tier O? at best and only fires
    when a held payload hashes to the digest the row names."""
    f = REPO / "tools" / "asset_judgements.tsv"
    if not f.is_file():
        return {}
    lines = f.read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t")
    return {r["target"]: r for r in
            (dict(zip(header, l.split("\t"))) for l in lines[1:]
             if l.strip() and not l.lstrip().startswith("#"))}


def resolve_one(target, root, cdx, basename_index, judgements):
    served = "/" + target
    era_rows = [r for r in cdx.get(served, [])
                if ERA_START <= r[0] <= ERA_END and r[1] in ("200", "-")]
    era_digests = sorted({r[2] for r in era_rows})
    cands = candidates_for(target, root, basename_index)

    scored = []
    for rel, strength in cands:
        sha256, sha1b32 = digests_of(root / rel)
        hits = sum(1 for r in era_rows if r[2] == sha1b32)
        scored.append((rel, strength, sha256, sha1b32, hits))

    judged = judgements.get(target)
    if judged:
        hit = [c for c in scored if c[3] == judged["expected_digest"]]
        if hit:
            rel, _strength, sha256, sha1b32, _hits = hit[0]
            return dict(
                verdict="judged", tier=judged["tier"],
                chosen_source=f"archive/{rel}", sha256=sha256, sha1b32=sha1b32,
                era_digests=era_digests, candidates=[c[0] for c in scored],
                notes=f"NOT era-digest-confirmed — no 2017-2018 capture of "
                      f"{served} exists. Placed on the argument recorded in "
                      f"tools/asset_judgements.tsv, from capture "
                      f"{judged['capture_ts']} ({sha1b32}): "
                      f"{judged['reasoning']}")

    matched = [c for c in scored if c[4] > 0]
    if matched:
        rel, strength, sha256, sha1b32, hits = max(matched, key=lambda c: c[4])
        # a digest match IS the evidence; where the bytes sit only matters for
        # describing how they got here
        if rel.startswith("wayback-images-"):
            provenance = ("refetched from Wayback by tools/fetch_missing.py "
                          "and accepted only because the payload digest "
                          "matched")
        else:
            provenance = f"bytes held at a {strength} archive location"
        return dict(
            verdict="era-digest-match", tier="O", chosen_source=f"archive/{rel}",
            sha256=sha256, sha1b32=sha1b32, era_digests=era_digests,
            candidates=[c[0] for c in scored],
            notes=f"payload sha1 {sha1b32} on {hits} CDX rows in 2017-2018 "
                  f"for {served}; {provenance}")

    if scored and era_digests:
        held = "; ".join(f"{c[0]}={c[3]}" for c in scored[:4])
        return dict(
            verdict="wrong-era-bytes", tier="known-lost", chosen_source="—",
            sha256="—", sha1b32="—", era_digests=era_digests,
            candidates=[c[0] for c in scored],
            notes=f"era window served {'/'.join(era_digests)}; held bytes are "
                  f"other eras ({held}) — era file never captured")

    strong = [c for c in scored if c[1] == "strong"]
    if strong:
        rel, _strength, sha256, sha1b32, _hits = min(strong, key=lambda c: c[0])
        return dict(
            verdict="held-no-era-cdx", tier="O?", chosen_source=f"archive/{rel}",
            sha256=sha256, sha1b32=sha1b32, era_digests=[],
            candidates=[c[0] for c in scored],
            notes=f"no CDX row for {served} in 2017-2018; bytes stored at the "
                  f"served path inside an archived host tree, era service "
                  f"unproven")

    if scored:
        # Only a basename collision links these files to the served path. Not
        # evidence (guide 6.2 rule 3: reject, never fake) — a human decides.
        near = "; ".join(c[0] for c in scored[:4])
        return dict(
            verdict="weak-candidate-only", tier="known-lost", chosen_source="—",
            sha256="—", sha1b32="—", era_digests=[],
            candidates=[c[0] for c in scored],
            notes=f"no era CDX row and no copy at the served path; basename "
                  f"matches elsewhere in the archive ({near}) are unproven — "
                  f"adjudicate by eye before any promotion")

    if era_digests:
        return dict(
            verdict="cdx-observed", tier="known-lost", chosen_source="—",
            sha256="—", sha1b32="—", era_digests=era_digests, candidates=[],
            notes=f"{len(era_rows)} CDX rows in 2017-2018 for {served}; bytes "
                  f"not held — Wayback refetch target")

    return dict(
        verdict="unobserved", tier="known-lost", chosen_source="—", sha256="—",
        sha1b32="—", era_digests=[], candidates=[],
        notes=f"referenced by the pages but no era CDX row and no held bytes "
              f"for {served}")


def work_list():
    """Gate E's own defect list: static references plus the hand-enumerated
    runtime-assembled names, minus whatever srv/ already holds."""
    refs, _dynamic, _unreachable = refgraph.build()
    targets = {r.target for r in refs}
    decl = REPO / "tests" / "gate_e_dynamic.tsv"
    for line in decl.read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip() and not line.lstrip().startswith("#"):
            targets.add(line.split("\t")[2])
    return sorted(t for t in targets if not (REPO / "srv" / t).is_file())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--print-only", action="store_true")
    args = ap.parse_args()

    root = archive_root()
    cdx = load_cdx(root)
    print("indexing archive basenames…", flush=True)
    basename_index = index_basenames(root)

    judgements = read_judgements()
    targets = work_list()
    print(f"gate E defects to resolve: {len(targets)}\n")

    lines = ["\t".join(HEADER)]
    tally = {}
    for t in targets:
        r = resolve_one(t, root, cdx, basename_index, judgements)
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
        lines.append("\t".join([
            t, r["verdict"], r["tier"], r["chosen_source"], r["sha256"],
            r["sha1b32"], ";".join(r["era_digests"]) or "—",
            ";".join(r["candidates"]) or "—", r["notes"]]))

    for verdict, n in sorted(tally.items(), key=lambda kv: -kv[1]):
        print(f"  {verdict:18s} {n:4d}")

    if args.print_only:
        return
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
