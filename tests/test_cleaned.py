"""Gate C1 — archive-cleaned/ integrity. The manifest is the sha256-locked
inventory of every classic-era de-render diff target (guide 6.1a steps 1-2);
gate F will iterate it. Rows must stay reproducible from the archive and the
locked hashes must still match the archive bytes."""

import hashlib
import os
import subprocess
import sys

from conftest import REPO

CLEANED = REPO / "archive-cleaned"
MANIFEST = CLEANED / "MANIFEST.tsv"
COLS = ["route", "ts", "host", "source", "sha256_served", "depagespeed",
        "sha256_depagespeed", "jc_bundles", "single_urls", "ic_left"]


def rows():
    lines = MANIFEST.read_text(encoding="utf-8").splitlines()
    assert lines[0].split("\t") == COLS, "MANIFEST.tsv header wrong"
    return [dict(zip(COLS, l.split("\t"))) for l in lines[1:] if l.strip()]


def test_manifest_well_formed():
    rs = rows()
    assert len(rs) > 400, "expected 400+ classic captures, got %d" % len(rs)
    routes = {r["route"] for r in rs}
    assert {"root", "game", "garage", "news", "forum", "lab",
            "shop"} <= routes, "a de-render route is missing: %s" % routes
    assert all(r["ts"][:8] <= "20201204" for r in rs), "modern-era row leaked in"


def test_served_hashes_match_archive(archive_root):
    bad = []
    for r in rows():
        src = archive_root / r["source"].replace("archive/", "", 1)
        if not src.is_file():
            bad.append("%s: source missing" % r["source"])
            continue
        if hashlib.sha256(src.read_bytes()).hexdigest() != r["sha256_served"]:
            bad.append("%s: sha256 drift" % r["source"])
    assert not bad, "\n".join(bad[:10])


def test_depagespeed_files_match_manifest():
    for r in rows():
        if r["depagespeed"] == "—":
            continue
        p = CLEANED / r["depagespeed"]
        assert p.is_file(), "%s missing" % r["depagespeed"]
        assert hashlib.sha256(p.read_bytes()).hexdigest() == \
            r["sha256_depagespeed"], "%s drifted" % r["depagespeed"]


def test_cleaning_is_reproducible(tmp_path, archive_root):
    env = dict(os.environ,
               TT_CLEANED_OUT_DIR=str(tmp_path),
               TT_ARCHIVE_ROOT=str(archive_root))
    r = subprocess.run(
        [sys.executable, str(REPO / "tools" / "clean_captures.py")],
        env=env, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert (tmp_path / "MANIFEST.tsv").read_bytes() == MANIFEST.read_bytes(), \
        "regenerated manifest differs from committed one"
