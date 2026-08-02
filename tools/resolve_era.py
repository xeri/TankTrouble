#!/usr/bin/env python3
"""Resolve which held capture of each multi-capture asset was live 2017-2018.

Method (DECISIONS.md "era method"):
  1. identical            all candidates share one sha256 -> earliest capture
  2. sha1-digest-match    a CDX row inside the era window carries the
                          base32(SHA1) of a candidate -> that candidate, tier O
  3. digest-run-continuity the digest observed at the candidate's own capture
                          time has an unbroken CDX run spanning into the era
                          window -> that candidate, tier O
  4. nearest-capture      nothing provable -> candidate temporally nearest the
                          window, tier O?

CDX dump row format: <url> <ts> <status> <mime> <length> <digest>
digest = base32(SHA1(payload)); warc/revisit rows (status "-") count for
continuity. Digests of gzip-served text bodies may hash the gzip stream, so
method 2 can fail where method 3 succeeds — that is expected.

Writes tools/era_choices.tsv for human review. build_skeleton.py refuses to
copy era-group files until that file exists and covers every group.
"""

import base64
import hashlib
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ERA_START, ERA_END = "20170101000000", "20181231235959"

CDX_FILES = [
    "wayback-inventory/cdx-tanktrouble.com.txt",
    "wayback-inventory/cdx-classic.tanktrouble.com.txt",
]

# name -> (served path, [candidate archive-relative paths])
GROUPS = {
    # includes/, multiple held captures
    "styles.css": ("/includes/styles.css", [
        "includes-tree/20101128_styles.css",
        "includes-tree/20201225_styles.css"]),
    "swfobject.js": ("/includes/swfobject.js", [
        "includes-tree/20101128_swfobject.js",
        "includes-tree/20201222_swfobject.js",
        "includes-tree/20201225_swfobject.js",
        "classic.tanktrouble.com/includes/swfobject.js"]),
    "mootools-release-1.11.js": ("/includes/mootools-release-1.11.js", [
        "includes-tree/20101128_mootools-release-1.11.js",
        "includes-tree/20201225_mootools-release-1.11.js"]),
    "boxStyles.css": ("/includes/boxStyles.css", [
        "includes-tree/20130313_boxStyles.css",
        "includes-tree/20201225_boxStyles.css"]),
    "forumStyles.css": ("/includes/forumStyles.css", [
        "includes-tree/20130313_forumStyles.css",
        "includes-tree/20201225_forumStyles.css"]),
    "newsStyles.css": ("/includes/newsStyles.css", [
        "includes-tree/20130313_newsStyles.css",
        "includes-tree/20201225_newsStyles.css"]),
    "shopStyles.css": ("/includes/shopStyles.css", [
        "includes-tree/20150529_shopStyles.css",
        "includes-tree/20201225_shopStyles.css"]),
    "phaser.min.js": ("/includes/phaser.min.js", [
        "includes-tree/20170221_phaser.min.js",
        "includes-tree/20201225_phaser.min.js"]),
    "scrapyard.js": ("/includes/scrapyard.js", [
        "includes-tree/20170221_scrapyard.js",
        "includes-tree/20201225_scrapyard.js"]),
    "TankTrouble_v4.0.swf": ("/includes/TankTrouble_v4.0.swf", [
        "includes-tree/20130313_TankTrouble_v4.0.swf",
        "includes-tree/20201225_TankTrouble_v4.0.swf"]),
    "c64.woff": ("/includes/c64.woff", [
        "includes-tree/20150315_c64.woff",
        "includes-tree/20201222_c64.woff",
        "includes-tree/20201225_c64.woff"]),
    "c64.eot": ("/includes/c64.eot", [
        "includes-tree/20150126_c64.eot",
        "includes-tree/20210121_c64.eot"]),
    "laika02.swf": ("/includes/laika02.swf", [
        "includes-tree/20110625_laika02.swf",
        "includes-tree/20210113_laika02.swf"]),
    "signUpTankDesign18StandardColours.swf": (
        "/includes/signUpTankDesign18StandardColours.swf", [
            "includes-tree/20190515_signUpTankDesign18StandardColours.swf",
            "includes-tree/20201225_signUpTankDesign18StandardColours.swf"]),
    "TTTradingCardsSeriesI.pdf": ("/includes/TTTradingCardsSeriesI.pdf", [
        "includes-tree/20190606_TTTradingCardsSeriesI.pdf",
        "includes-tree/20210112_TTTradingCardsSeriesI.pdf"]),
    "TTTradingCardsSeriesII.pdf": ("/includes/TTTradingCardsSeriesII.pdf", [
        "includes-tree/20190606_TTTradingCardsSeriesII.pdf",
        "includes-tree/20210112_TTTradingCardsSeriesII.pdf"]),
    "TTTradingCardsSeriesIII.pdf": ("/includes/TTTradingCardsSeriesIII.pdf", [
        "includes-tree/20190606_TTTradingCardsSeriesIII.pdf",
        "includes-tree/20210112_TTTradingCardsSeriesIII.pdf"]),
    "TTTradingCardsSpecialAnniversaryCard.pdf": (
        "/includes/TTTradingCardsSpecialAnniversaryCard.pdf", [
            "includes-tree/20190606_TTTradingCardsSpecialAnniversaryCard.pdf",
            "includes-tree/20210112_TTTradingCardsSpecialAnniversaryCard.pdf"]),
    # includes/, single held capture — era check decides O vs O?
    "c64.ttf": ("/includes/c64.ttf", [
        "includes-tree/20210121_c64.ttf"]),
    "main.css": ("/includes/main.css", [
        "includes-tree/20201222_main.css"]),
    "news.css": ("/includes/news.css", [
        "includes-tree/20201222_news.css"]),
    "TankTrouble_v4.03.swf": ("/includes/TankTrouble_v4.03.swf", [
        "includes-tree/20230908_TankTrouble_v4.03.swf",
        "classic.tanktrouble.com/includes/TankTrouble_v4.03.swf"]),
    # /Assets/ at web root, capital A (HUNT-LOG §46 note 1)
    "Tank.swf": ("/Assets/Tank.swf", [
        "classic.tanktrouble.com/Assets/Tank.swf",
        "wayback-zip-swfs/Tank__Assets_51D440C0.swf",
        "wayback-zip-swfs/Tank__Assets_8C458EF1.swf",
        "wayback-zip-swfs/Tank__Assets_B502114E.swf",
        "zip-extracted/20130818_TankTrouble_v3.8c/Assets/Tank.swf",
        "zip-extracted/20121003_TankTrouble_v3.6e/Assets/Tank.swf",
        "zip-extracted/20111011_TankTrouble_v3.6/Assets/Tank.swf",
        "zip-extracted/20110520_TankTrouble_v3.5/Assets/Tank.swf"]),
    "GameTank.swf": ("/Assets/GameTank.swf", [
        "classic.tanktrouble.com/Assets/GameTank.swf",
        "wayback-zip-swfs/GameTank__Assets_83B96231.swf",
        "wayback-zip-swfs/GameTank__Assets_D1E004D4.swf",
        "zip-extracted/20130818_TankTrouble_v3.8c/Assets/GameTank.swf",
        "zip-extracted/20111011_TankTrouble_v3.6/Assets/GameTank.swf"]),
    "Crate.swf": ("/Assets/Crate.swf", [
        "classic.tanktrouble.com/Assets/Crate.swf",
        "wayback-zip-swfs/Crate__Assets_19C320EA.swf",
        "zip-extracted/20130818_TankTrouble_v3.8c/Assets/Crate.swf",
        "zip-extracted/20111011_TankTrouble_v3.6/Assets/Crate.swf"]),
    "Laika.swf": ("/Assets/Laika.swf", [
        "classic.tanktrouble.com/Assets/Laika.swf"]),
}

# capture-timestamp anchor per candidate: leading YYYYMMDD in the stored name,
# else the live-pull date of the classic.tanktrouble.com fetch.
LIVE_PULL_TS = "20260802000000"


def archive_root():
    root = os.environ.get("TT_ARCHIVE_ROOT") or str(REPO / "archive")
    p = Path(root)
    if not (p / "includes-tree").is_dir():
        sys.exit("archive root not found: set TT_ARCHIVE_ROOT or create the "
                 "archive junction (see README.md)")
    return p


def anchor_ts(rel):
    name = rel.split("/")[-1]
    stem = rel.split("/")[0]
    for probe in (name[:8], rel.split("/")[1][:8] if "/" in rel else ""):
        if len(probe) == 8 and probe.isdigit():
            return probe + "000000"
    if stem == "classic.tanktrouble.com":
        return LIVE_PULL_TS
    # zip-extracted/<YYYYMMDD_...>/...
    for part in rel.split("/"):
        if len(part) > 8 and part[:8].isdigit():
            return part[:8] + "000000"
    return LIVE_PULL_TS


def load_cdx(root):
    """{exact path: [(ts, status, digest)] sorted by ts}"""
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
            path = path.split("?", 1)[0]
            rows.setdefault(path, []).append((ts, status, digest))
    for v in rows.values():
        v.sort()
    return rows


def digest_runs(rows):
    """[(digest, first_ts, last_ts)] — contiguous same-digest spans."""
    runs = []
    for ts, status, digest in rows:
        if status not in ("200", "-"):
            continue
        if runs and runs[-1][0] == digest:
            runs[-1][2] = ts
        else:
            runs.append([digest, ts, ts])
    return [tuple(r) for r in runs]


def resolve(name, served_path, cands, cdx, root):
    infos = []
    for rel in cands:
        p = root / rel
        if not p.is_file():
            sys.exit(f"{name}: candidate missing on disk: {p}")
        data = p.read_bytes()
        infos.append({
            "rel": rel,
            "sha256": hashlib.sha256(data).hexdigest(),
            "sha1b32": base64.b32encode(hashlib.sha1(data).digest()).decode(),
            "anchor": anchor_ts(rel),
        })

    if len({i["sha256"] for i in infos}) == 1:
        pick = min(infos, key=lambda i: i["anchor"])
        return pick, "identical", "O", "", "all candidates byte-identical"

    rows = cdx.get(served_path, [])
    era_rows = [r for r in rows if ERA_START <= r[0] <= ERA_END
                and r[1] in ("200", "-")]
    era_digests = sorted({r[2] for r in era_rows})
    runs = digest_runs(rows)

    # method 2 — a candidate's payload sha1 seen in the window
    hits = [i for i in infos if i["sha1b32"] in era_digests]
    if len({i["sha256"] for i in hits}) == 1 and hits:
        return (hits[0], "sha1-digest-match", "O", ";".join(era_digests),
                f"digest {hits[0]['sha1b32']} observed in era window")

    # method 3 — digest at the candidate's capture time runs into the window
    for i in infos:
        for digest, first, last in runs:
            covers_anchor = first <= i["anchor"] <= last
            overlaps_era = first <= ERA_END and last >= ERA_START
            if covers_anchor and overlaps_era:
                return (i, "digest-run-continuity", "O", ";".join(era_digests),
                        f"digest {digest} run {first}..{last} covers both "
                        f"capture ts and era window")

    # method 4 — nearest capture, O?
    def dist(i):
        a = i["anchor"]
        if a < ERA_START:
            return int(ERA_START) - int(a)
        if a > ERA_END:
            return int(a) - int(ERA_END)
        return 0
    pick = min(infos, key=dist)
    return (pick, "nearest-capture", "O?", ";".join(era_digests),
            "era-served digest not held or no era capture; nearest chosen")


def main():
    root = archive_root()
    cdx = load_cdx(root)
    out = REPO / "tools" / "era_choices.tsv"
    lines = ["name\tsrv_path\tchosen_source\tmethod\ttier\tera_digests\trejected\tnotes"]
    for name, (served_path, cands) in GROUPS.items():
        pick, method, tier, era_digests, note = resolve(
            name, served_path, cands, cdx, root)
        rejected = ";".join(c for c in cands if c != pick["rel"])
        srv_path = "srv" + served_path
        lines.append("\t".join([
            name, srv_path, "archive/" + pick["rel"], method, tier,
            era_digests or "-", rejected or "-", note]))
        print(f"{name:45s} {method:22s} {tier:2s} <- {pick['rel']}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
