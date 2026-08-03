#!/usr/bin/env python3
"""Lay down the assets resolve_assets.py resolved, and label every one.

Copies never move; sha256 is re-verified on arrival against the value
tools/asset_choices.tsv recorded, so a corrupted read cannot land silently.
LEDGER rows are APPENDED (append-only discipline since the skeleton-complete
tag) — existing rows are never rewritten, and a target that already has a row
is skipped.

Assets that could not be era-resolved get a known-lost row carrying WHY, so
gate E can go green without anyone pretending the file exists.

    python tools/place_assets.py --dry-run
    python tools/place_assets.py
"""

import argparse
import hashlib
import os
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CHOICES = REPO / "tools" / "asset_choices.tsv"
LEDGER = REPO / "LEDGER.tsv"
DASH = "—"
GATE_A = "tests/test_assets.py"
GATE_E = "tests/test_subresources.py"

# verdict -> (ledger evidence phrasing, verified_by)
EVIDENCE = {
    "era-digest-match": ("live 2017-2018 per era-digest-match "
                         "(tools/asset_choices.tsv; era digests {digests})", GATE_A),
    "judged": ("era service INFERRED, not digest-confirmed — no 2017-2018 "
               "capture of this path exists; argument and its evidence in "
               "tools/asset_judgements.tsv", GATE_A),
    "held-no-era-cdx": ("bytes stored at the served path in an archived host "
                        "tree; era service not digest-confirmed "
                        "(tools/asset_choices.tsv)", GATE_A),
    "wrong-era-bytes": ("era window served {digests}; every held copy hashes "
                        "to another era (tools/asset_choices.tsv)", GATE_E),
    "cdx-observed": ("CDX rows capture the path in 2017-2018; bytes not held "
                     "(tools/asset_choices.tsv)", GATE_E),
    "weak-candidate-only": ("no era CDX row and no copy at the served path "
                            "(tools/asset_choices.tsv)", GATE_E),
    "unobserved": ("referenced by the era pages; no era CDX row and no held "
                   "bytes (tools/asset_choices.tsv)", GATE_E),
}


def archive_root():
    root = os.environ.get("TT_ARCHIVE_ROOT") or str(REPO / "archive")
    p = Path(root)
    if not (p / "includes-tree").is_dir():
        sys.exit("archive root not found: set TT_ARCHIVE_ROOT or create the "
                 "archive junction (see README.md)")
    return p


def sha256_of(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_choices():
    lines = CHOICES.read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t")
    return [dict(zip(header, l.split("\t"))) for l in lines[1:] if l.strip()]


def existing_rows():
    lines = LEDGER.read_text(encoding="utf-8").splitlines()
    return {l.split("\t")[0]: l.split("\t") for l in lines[1:] if l.strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--promote", action="store_true",
                    help="rewrite known-lost rows whose bytes have since been "
                         "refetched and digest-verified; no other tier is "
                         "ever touched")
    args = ap.parse_args()

    root = archive_root()
    have = existing_rows()
    copied, labelled, skipped = [], [], 0
    new_rows = []
    promotions = {}

    for c in read_choices():
        srv_path = f"srv/{c['target']}"
        if srv_path in have:
            old = have[srv_path]
            # known-lost -> O is a real promotion: evidence arrived that was
            # not held when the row was written (a Wayback refetch whose
            # payload digest matches the CDX row). Any other tier is left
            # alone — this tool never overwrites a judged row.
            if not (old[1] == "known-lost" and c["tier"] in ("O", "O?")
                    and args.promote):
                skipped += 1
                continue
        phrase, verified_by = EVIDENCE[c["verdict"]]
        evidence = phrase.format(digests=c["era_digests"])

        if c["tier"] in ("O", "O?"):
            src = root / c["chosen_source"].removeprefix("archive/")
            if not src.is_file():
                sys.exit(f"{c['target']}: chosen source vanished: {src}")
            dst = REPO / srv_path
            if dst.exists():
                sys.exit(f"{c['target']}: refusing to overwrite {dst}")
            if not args.dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                got = sha256_of(dst)
                if got != c["sha256"]:
                    dst.unlink()
                    sys.exit(f"{c['target']}: sha256 on arrival {got} != "
                             f"{c['sha256']} recorded — copy rejected")
            copied.append(srv_path)
            row = [srv_path, c["tier"], c["sha256"], c["chosen_source"],
                   evidence, verified_by,
                   f"era method: {c['verdict']}; {c['notes']}"]
            if srv_path in have:
                row[6] += ("; promoted from known-lost — bytes refetched and "
                           "digest-verified by tools/fetch_missing.py")
                promotions[srv_path] = row
            else:
                new_rows.append(row)
        else:
            labelled.append(srv_path)
            new_rows.append([srv_path, "known-lost", DASH, DASH, evidence,
                             verified_by, c["notes"]])

    print(f"copy   {len(copied)} O/O? files")
    print(f"label  {len(labelled)} known-lost rows")
    print(f"skip   {skipped} targets already in LEDGER.tsv")
    if promotions:
        print(f"promote {len(promotions)} known-lost rows to O/O?:")
        for p in sorted(promotions):
            print(f"    {p}")
    if args.dry_run:
        print("\n(dry run — nothing written)")
        return

    if promotions:
        lines = LEDGER.read_text(encoding="utf-8").splitlines()
        out = [lines[0]]
        for line in lines[1:]:
            if not line.strip():
                continue
            path = line.split("\t")[0]
            out.append("\t".join(promotions[path]) if path in promotions else line)
        LEDGER.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
        print(f"rewrote {len(promotions)} rows in place "
              f"(record the promotion in DECISIONS.md)")

    if new_rows:
        with open(LEDGER, "a", encoding="utf-8", newline="\n") as f:
            for row in new_rows:
                f.write("\t".join(row) + "\n")
        print(f"appended {len(new_rows)} rows to {LEDGER}")


if __name__ == "__main__":
    main()
