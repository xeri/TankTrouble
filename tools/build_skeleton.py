#!/usr/bin/env python3
"""Milestone-1 skeleton builder. Copies O bytes (never moves), verifies
sha256 on arrival, writes loud 501 stubs, and regenerates LEDGER.tsv.

Stages (idempotent; run all three, in order, or one via --stage):
  copy   O/O? files: archive -> srv/, sha256(source)==sha256(dest) asserted
  stubs  M* PHP stubs from the template below
  rows   known-lost / pending rows (no files)

LEDGER.tsv is fully regenerated (sorted by path) on each run. Append-only
discipline begins at the skeleton-complete tag (DECISIONS.md).

The ledger's `source` column uses archive/<relpath> with forward slashes.
Era-group sources come from tools/era_choices.tsv (resolve_era.py output,
human-reviewed); this script refuses to run `copy` without it.
"""

import argparse
import hashlib
import os
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRV = REPO / "srv"
LEDGER = REPO / "LEDGER.tsv"
ERA_CHOICES = REPO / "tools" / "era_choices.tsv"
WRITTEN = "2026-08-02"
DASH = "—"  # em dash: honest empty

HEADER = ["path", "tier", "sha256", "source", "evidence", "verified_by", "notes"]

# ---------------------------------------------------------------- O sources
# Fixed-source O/O? files: srv path -> (tier, archive relpath, evidence, notes)
FIXED_O = {
    "srv/robots.txt": ("O", "commoncrawl/warc-bodies/20180317214202_200_www.tanktrouble.com_robots.txt.txt",
        "CC capture 2018-03-17 status 200, apex www; in-era",
        "47 b, Mediapartners-Google body"),
    "srv/infirmary/index.html": ("O", "commoncrawl/warc-bodies/20180722_tanktrouble.com_infirmary_.txt",
        "CC body 2018-07-22, raw, no PageSpeed/Wayback artifacts; in-era",
        "filename convention-inferred; leaked TEMPORARY WARP author comment retained verbatim "
        "(evidence for sendRequest/changePassword); may be superseded by de-rendered index.php "
        "per guide 6.1a - row then demoted to archive-cleaned reference, never edited"),
    # includes/ single-capture originals
    "srv/includes/embed.js": ("O", "includes-tree/20120912_embed.js",
        "Wayback capture 2012-09-12", ""),
    "srv/includes/TankTrouble_v3.6c.swf": ("O", "includes-tree/20120615_TankTrouble_v3.6c.swf",
        "Wayback capture 2012-06-15", ""),
    "srv/includes/scrapyard06.swf": ("O", "includes-tree/20120615_scrapyard06.swf",
        "Wayback capture 2012-06-15", ""),
    "srv/includes/scrapyard10.swf": ("O", "includes-tree/20150106_scrapyard10.swf",
        "Wayback capture 2015-01-06", ""),
    "srv/includes/scrapyard11.swf": ("O", "includes-tree/20150928_scrapyard11.swf",
        "Wayback capture 2015-09-28", ""),
    "srv/includes/signUpTankDesign04StandardColours.swf": ("O",
        "includes-tree/20120601_signUpTankDesign04StandardColours.swf",
        "Wayback capture 2012-06-01 status 200; guide 2.2 never-captured listing is stale "
        "(HUNT-LOG 35/37.4: earlier failures were throttling)", ""),
    "srv/includes/signUpTankDesign13StandardColours.swf": ("O",
        "includes-tree/20130409_signUpTankDesign13StandardColours.swf",
        "Wayback capture 2013-04-09", ""),
    "srv/includes/signUpTankDesign16StandardColours.swf": ("O",
        "includes-tree/20150514_signUpTankDesign16StandardColours.swf",
        "Wayback capture 2015-05-14", ""),
    "srv/includes/signUpTankDesign17StandardColours.swf": ("O",
        "includes-tree/20161002_signUpTankDesign17StandardColours.swf",
        "Wayback capture 2016-10-02", ""),
    "srv/includes/ima3_preloader_1.5.swf": ("O", "includes-tree/20161122_ima3_preloader_1.5.swf",
        "Wayback capture 2016-11-22", ""),
    "srv/includes/loggedInTank06.swf": ("O", "includes-tree/20191004_loggedInTank06.swf",
        "Wayback capture 2019-10-04", ""),
    "srv/includes/TankTrouble_v3.5.zip": ("O", "includes-tree/20110520_TankTrouble_v3.5.zip",
        "Wayback capture 2011-05-20; distribution kit, http-observed includes path (HUNT-LOG 46)", ""),
    "srv/includes/TankTrouble_v3.6.zip": ("O", "includes-tree/20111011_TankTrouble_v3.6.zip",
        "Wayback capture 2011-10-11; distribution kit", ""),
    "srv/includes/TankTrouble_v3.6e.zip": ("O", "includes-tree/20121003_TankTrouble_v3.6e.zip",
        "Wayback capture 2012-10-03; distribution kit", ""),
    "srv/includes/TankTrouble_v3.8c.zip": ("O", "includes-tree/20130818_TankTrouble_v3.8c.zip",
        "Wayback capture 2013-08-18; distribution kit", ""),
    "srv/includes/TankTrouble_v3.6e.swf": ("O?",
        "zip-extracted/20121003_TankTrouble_v3.6e/TankTrouble_v3.6e.swf",
        "authentic bytes extracted from O zip (includes-tree/20121003_TankTrouble_v3.6e.zip); "
        "served-path bytes never directly captured",
        "O? by placement, not by bytes"),
}

IMAGES_DIR = "classic-ui-images"  # archive dir mirrored 1:1 to srv/images/

# ---------------------------------------------------------------- stubs
STUB_TEMPLATE = """<?php
/* @provenance {tier}
 * @evidence   {evidence}
 * @verified   none
 * @written    {written}
 * @caveat     Milestone-1 skeleton stub. Behaviour not reconstructed. Must
 *             never return 200 or plausible data.{extra_caveat}
 */
header('HTTP/1.1 501 Not Implemented');
die("STUB {relpath} [{tier}] - behaviour not yet reconstructed\\n");
"""

INDEX_EXTRA = """
 *             Promotion path: de-render per guide 6.1a; verify via Gate F
 *             (tests/test_render_diff.py); a passing route is M1."""

AUTH_EXTRA = """
 *             DELIBERATE DIVERGENCE. The original used SAJAX over GET, which
 *             is why real credentials are still in the public Wayback CDX
 *             index. This file does NOT reconstruct that. POST + TLS +
 *             password_hash."""

# srv path -> (tier, evidence, extra caveat)
STUBS = {
    "srv/index.php": ("M2",
        "obs 2008->; SAJAX front controller; 6 routes ?game ?garage ?news ?lab ?forum ?shop; "
        "36 exported functions (HUNT-LOG 54)", INDEX_EXTRA),
    "srv/embed.php": ("M2", "obs in CDX; embed target", ""),
    "srv/content.php": ("M2", "obs in CDX", ""),
    "srv/getimage.php": ("M2",
        "obs in CDX x99; ?id=N ?at2x; images content-addressed by integer (HUNT-LOG 46 n.3)", ""),
    "srv/uploadimage.php": ("M2", "obs in CDX (2021 capture, post-era); admin news upload", ""),
    "srv/sendRequest.php": ("M2",
        "inf; named in infirmary page author comment (srv/infirmary/index.html)", ""),
    "srv/changePassword.php": ("M2",
        "inf; named in infirmary page author comment (srv/infirmary/index.html)", ""),
    "srv/feedback.php": ("M2",
        "http-observed (HUNT-LOG 46); referenced in 2018 bodies", ""),
    "srv/includes/loadMaze.php": ("M1",
        "17,411 CDX rows; 843 decoded responses in archive/maze-corpus/raw/; "
        "reader source archive/decompiled/.../MazeDataFetcher.as", ""),
    "srv/includes/updateGameStatistics.php": ("M2",
        "2,305 CDX rows; client call sites in decompiled AS2; no response body captured", ""),
    "srv/includes/achievement.php": ("M2",
        "6 client call sites in decompiled AS2; achievementId/achievementIds/achievementProgress; "
        "no response body captured", ""),
    "srv/includes/getScrapyard.php": ("M2",
        "CDX params ?scraps &velocity; 2 captured response bodies "
        "(archive/includes-tree/20150928_getScrapyard.php, 20160126_getScrapyard.php)", ""),
    "srv/includes/getUserAuthentication.php": ("M3",
        "5 client call sites in decompiled AS2; behaviour unknown", AUTH_EXTRA),
    "srv/includes/db.php": ("M3", "none - name invented", ""),
    "srv/tankRanks/index.php": ("M2",
        "dir /tankRanks/ 86x200 CDX 2010-2015; era ?lab pages open it via "
        "window.open('tankRanks',...) (DEDUCE.md 2.2); index filename convention-inferred", ""),
}
for d in ("faq", "shop", "privacy", "like", "statistics", "spreadTheWord",
          "tellAFriendMail", "ios", "theLabReport"):
    STUBS[f"srv/{d}/index.php"] = ("M2",
        f"directory /{d}/ observed in CDX; index filename convention-inferred", "")

STUB_NOTES = {
    "srv/includes/db.php": "DO NOT PROMOTE; name invented, consider obviously-modern rename (guide 10.4)",
    "srv/theLabReport/index.php": "dir layout is FLAT (The_Lab_Report_volume_N_issue_M.pdf, CDX-verified); "
        "guide 2 vol{1..14} shape wrong; PDFs still-fetchable, deferred",
}

# ---------------------------------------------------------------- no-file rows
V_LOST = ["1.11", "1.3", "1.31", "1.4", "2.01", "2.1", "2.2", "3.02a", "3.11",
          "3.1a", "3.41", "3.42", "3.43", "3.5", "3.6", "3.6a", "3.6b", "3.7"]

NOFILE_ROWS = []
for v in V_LOST:
    note = "CDX name only, no 200 capture"
    if v in ("3.5", "3.6"):
        note += "; inner SWF exists in held zip - promotion candidate"
    NOFILE_ROWS.append((f"srv/includes/TankTrouble_v{v}.swf", "known-lost",
                        "CDX rows name the path; bytes never captured", note))
for s in ("", "01", "03", "04", "05", "07", "08"):
    NOFILE_ROWS.append((f"srv/includes/scrapyard{s}.swf", "known-lost",
                        "CDX rows name the path; bytes never captured",
                        "no scrapyard09 row - existence only inferred from gap"
                        if s == "08" else ""))
for s in ("01", "09", "11"):
    NOFILE_ROWS.append((f"srv/includes/signUpTankDesign{s}StandardColours.swf",
                        "known-lost", "CDX rows name the path; bytes never captured", ""))
for s in ("02", "04"):
    NOFILE_ROWS.append((f"srv/includes/loggedInTank{s}.swf", "known-lost",
                        "CDX rows name the path; bytes never captured", ""))
NOFILE_ROWS += [
    ("srv/includes/p2.js", "known-lost", "obs in CDX, never 200",
     "may never have existed"),
    ("srv/includes/src/p2.js", "known-lost", "obs in CDX, never 200",
     "may never have existed"),
    ("srv/includes/images/scrapyardPlates.png", "known-lost", "obs in CDX, 404 only", ""),
    ("srv/includes/mazeCreator_v0.2.swf", "known-lost",
     "single CDX sighting 2010-09-08, no 200", "pre-era"),
    ("srv/ads.txt", "known-lost", "first CDX capture 2023-06-14, outside era",
     "no body held; wayback-recoverable, out of milestone-1 scope"),
    ("srv/logIn.php", "known-lost", "http-observed 404 already in 2008",
     "name proven, file already gone pre-era"),
    ("srv/includes/mazeCreator_v0.3.swf", "pending",
     "THE LOST FILE (guide 6.5); embed params, initCode, SetVariable surface, "
     "constraints from 843 mazes all specified",
     "M2 rebuild planned - guide 6.5, order-of-work step 9"),
]

GATE_A = "tests/test_assets.py"


def sha256_of(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def archive_root() -> Path:
    root = os.environ.get("TT_ARCHIVE_ROOT") or str(REPO / "archive")
    p = Path(root)
    if not (p / "includes-tree").is_dir():
        sys.exit("archive root not found: set TT_ARCHIVE_ROOT or create the "
                 "archive junction (see README.md)")
    return p


def load_era_choices():
    if not ERA_CHOICES.is_file():
        sys.exit("tools/era_choices.tsv missing - run resolve_era.py and "
                 "review its output first")
    rows = {}
    lines = ERA_CHOICES.read_text(encoding="utf-8").splitlines()
    head = lines[0].split("\t")
    for line in lines[1:]:
        if not line.strip():
            continue
        d = dict(zip(head, line.split("\t")))
        rows[d["srv_path"]] = d
    return rows


def copy_one(arc: Path, rel_src: str, srv_path: str) -> str:
    src = arc / rel_src
    if not src.is_file():
        sys.exit(f"source missing: {src}")
    dst = REPO / srv_path
    s_sha = sha256_of(src)
    if dst.exists():
        if sha256_of(dst) != s_sha:
            sys.exit(f"REFUSING to overwrite differing file: {dst}")
        return s_sha
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)  # copy, never move
    d_sha = sha256_of(dst)
    if d_sha != s_sha:
        sys.exit(f"sha256 mismatch after copy: {dst}")
    return s_sha


def stage_copy(rows):
    arc = archive_root()
    era = load_era_choices()
    n = 0
    for srv_path, (tier, rel_src, evidence, notes) in FIXED_O.items():
        sha = copy_one(arc, rel_src, srv_path)
        rows[srv_path] = [srv_path, tier, sha, "archive/" + rel_src,
                          evidence, GATE_A, notes or DASH]
        n += 1
    for srv_path, d in era.items():
        rel_src = d["chosen_source"].removeprefix("archive/")
        sha = copy_one(arc, rel_src, srv_path)
        note = f"era method: {d['method']}; rejected: {d['rejected']}"
        if d["tier"] == "O?":
            note += "; " + d["notes"]
        rows[srv_path] = [srv_path, d["tier"], sha, d["chosen_source"],
                          f"live 2017-2018 per {d['method']} "
                          f"(tools/era_choices.tsv; era digests {d['era_digests']})",
                          GATE_A, note]
        n += 1
    img_root = arc / IMAGES_DIR
    for f in sorted(img_root.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(img_root).as_posix()
        srv_path = f"srv/images/{rel}"
        sha = copy_one(arc, f"{IMAGES_DIR}/{rel}", srv_path)
        rows[srv_path] = [srv_path, "O", sha, f"archive/{IMAGES_DIR}/{rel}",
                          "recovered classic /images/ set, 122 files (HUNT-LOG 27)",
                          GATE_A, DASH]
        n += 1
    print(f"copy: {n} files placed/verified")


def stage_stubs(rows):
    n = 0
    for srv_path, (tier, evidence, extra) in STUBS.items():
        rel = srv_path.removeprefix("srv/")
        body = STUB_TEMPLATE.format(tier=tier, evidence=evidence,
                                    written=WRITTEN, extra_caveat=extra,
                                    relpath=rel)
        dst = REPO / srv_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(body, encoding="utf-8", newline="\n")
        rows[srv_path] = [srv_path, tier, DASH, f"written {WRITTEN}",
                          evidence, DASH,
                          STUB_NOTES.get(srv_path, "501 stub (milestone 1)")]
        n += 1
    print(f"stubs: {n} written")


def stage_rows(rows):
    for path, tier, evidence, note in NOFILE_ROWS:
        rows[path] = [path, tier, DASH, DASH, evidence, DASH, note or DASH]
    print(f"rows: {len(NOFILE_ROWS)} no-file rows")


def load_existing():
    rows = {}
    if LEDGER.is_file():
        lines = LEDGER.read_text(encoding="utf-8").splitlines()
        for line in lines[1:]:
            if line.strip():
                cells = line.split("\t")
                rows[cells[0]] = cells
    return rows


def write_ledger(rows):
    out = ["\t".join(HEADER)]
    for path in sorted(rows):
        out.append("\t".join(rows[path]))
    LEDGER.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    files = [p for p in SRV.rglob("*") if p.is_file()
             and not p.name.endswith(".provenance")]
    with_file = [r for r in rows.values() if r[1] not in ("known-lost", "pending")]
    print(f"ledger: {len(rows)} rows total, {len(with_file)} with files; "
          f"srv/ holds {len(files)} files")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["copy", "stubs", "rows", "all"],
                    default="all")
    a = ap.parse_args()
    rows = load_existing()
    if a.stage in ("copy", "all"):
        stage_copy(rows)
    if a.stage in ("stubs", "all"):
        stage_stubs(rows)
    if a.stage in ("rows", "all"):
        stage_rows(rows)
    write_ledger(rows)


if __name__ == "__main__":
    main()
