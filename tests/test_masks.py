"""Gate F, offline half — the masks themselves are evidence (guide 7.4a).

Three claims, each of which must hold BEFORE any route PHP is trusted:
  1. every dynamic region carries a valid, non-blocking annotation;
  2. regeneration is annotation-stable (region_sha keying works — a
     re-classified archive re-attaches every annotation byte-identically);
  3. the annotated masks HOLD against the archive: for every era capture of
     every route, gated reference lines survive byte-identical, masked
     regions absorb all differences, echo regexes match every projected
     line. A wrong template-edit window or a missed dynamic cause fails
     here, with no docker stack involved.
"""

import filecmp
import shutil

import pytest

import maskcheck
from conftest import DASH, REPO

import annotate_regions as ann     # via maskcheck's sys.path
import classify_regions as cls

CLASSIFICATION = REPO / "archive-cleaned" / "classification"
ROUTES = [r for r in cls.ROUTES if r != "statistics"]   # 0 era captures


def test_all_dynamic_regions_annotated():
    bad = []
    for route in ROUTES:
        mask = maskcheck.load_mask(route)
        bad += ["%s %s" % (route, rid)
                for rid in maskcheck.blocking_regions(mask)]
        bad += ["%s %s: static row annotation must be %s" % (route, rid, DASH)
                for rid, _, _, status, cell in mask
                if status == "static" and cell != DASH]
    assert not bad, "gate-blocking or malformed mask rows:\n" + "\n".join(bad)


def test_regen_is_annotation_stable(tmp_path, archive_root, monkeypatch):
    work = tmp_path / "classification"
    shutil.copytree(CLASSIFICATION, work)
    monkeypatch.setattr(ann, "OUT", str(work))
    monkeypatch.setattr(cls, "OUT", str(work))
    ann.cmd_regen()
    for f in sorted(CLASSIFICATION.iterdir()):
        assert filecmp.cmp(f, work / f.name, shallow=False), (
            "%s not byte-stable across regeneration" % f.name)


@pytest.mark.parametrize("route", ROUTES)
def test_masks_hold_against_archive(route, archive_root):
    caps, bodies = maskcheck.era_route_bodies(archive_root, route)
    mask = maskcheck.load_mask(route)
    assert not maskcheck.blocking_regions(mask)
    ref = bodies[-1]
    assert mask[-1][2] == len(ref), (
        "mask line count != reference capture — regenerate the TSVs")
    removed = maskcheck.load_removed(route)
    div = []
    for cap, body in zip(caps, bodies):
        modes, regexes = maskcheck.line_modes(
            mask, side="capture", ts8=cap["ts"][:8])
        div += maskcheck.check_side(
            ref, body, modes, regexes,
            "%s@%s" % (route, cap["ts"]),
            removed=removed, ts8=cap["ts"][:8])
    assert not div, ("mask does not hold against the archive "
                     "(%d divergence(s)):\n" % len(div) +
                     "\n".join(div[:12]))
