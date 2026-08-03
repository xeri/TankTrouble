"""Gate E — subresource resolution. Every asset the served pages ask the
browser for either exists under srv/ or is declared lost in the ledger.

Gates A and D walk srv/ -> LEDGER (does this file have a row, do its bytes
match). Gate F byte-diffs HTML against the captures. None of them walks the
other way, page -> subresource, so a byte-perfect page that serves zero images
passed all three green. It did: milestone-3 review found 193 referenced-and-
absent assets, none with a ledger row. See docs/ASSET-DISCIPLINE.md.

Offline gate. Runs on every commit alongside A and D.
"""

import http.client
import sys

import pytest

from conftest import REPO, parse_ledger

sys.path.insert(0, str(REPO / "tools"))
import refgraph  # noqa: E402

DYNAMIC_DECL = REPO / "tests" / "gate_e_dynamic.tsv"
DYNAMIC_HEADER = ["referrer", "family", "target", "evidence"]


def read_dynamic_decl():
    """Runtime-assembled names, enumerated by hand because no static reader
    can expand 'images/x' + tool + 'Select.jpg'. One row per concrete name."""
    assert DYNAMIC_DECL.is_file(), f"{DYNAMIC_DECL} missing"
    lines = DYNAMIC_DECL.read_text(encoding="utf-8").splitlines()
    assert lines[0].split("\t") == DYNAMIC_HEADER, "gate_e_dynamic.tsv header"
    rows = []
    for i, line in enumerate(lines[1:], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cells = line.split("\t")
        assert len(cells) == len(DYNAMIC_HEADER), \
            f"gate_e_dynamic.tsv line {i}: {len(cells)} cols"
        rows.append(dict(zip(DYNAMIC_HEADER, cells)))
    return rows


def known_lost_paths():
    return {r["path"] for r in parse_ledger() if r["tier"] == "known-lost"}


def all_targets():
    """Every concrete subresource the site asks for: statically extracted
    references plus the hand-enumerated runtime-assembled names."""
    refs, dynamic, _unreachable = refgraph.build()
    targets = {r.target for r in refs}
    decl = read_dynamic_decl()
    targets |= {d["target"] for d in decl}
    return targets, refs, dynamic, decl


def test_every_referenced_subresource_resolves():
    """The gate. Absent AND unlabelled is the defect; absent WITH a
    known-lost row is honest bookkeeping."""
    targets, _refs, _dyn, _decl = all_targets()
    lost = known_lost_paths()
    unexplained = sorted(t for t in targets
                         if not (REPO / "srv" / t).is_file()
                         and f"srv/{t}" not in lost)
    assert not unexplained, (
        f"{len(unexplained)} referenced subresources are neither present nor "
        f"declared known-lost in LEDGER.tsv:\n  " + "\n  ".join(unexplained))


def test_dynamic_families_declared():
    """Every 'a' + expr + 'b.jpg' shape found in the source has at least one
    enumerated concrete target. Otherwise the names vanish from the gate."""
    _targets, _refs, dynamic, decl = all_targets()
    declared = {(d["referrer"], d["family"]) for d in decl}
    missing = []
    for referrer, families in dynamic.items():
        for fam in families:
            if (referrer, fam) not in declared:
                missing.append(f"{referrer}: {fam}")
    assert not missing, (
        "runtime-assembled asset names with no gate_e_dynamic.tsv row "
        "(enumerate every concrete name they can produce):\n  "
        + "\n  ".join(sorted(missing)))


def test_dynamic_decl_rows_are_live():
    """A declared family that no longer appears in the source is stale —
    delete the row rather than let it rot."""
    _targets, _refs, dynamic, decl = all_targets()
    live = {(referrer, fam)
            for referrer, families in dynamic.items() for fam in families}
    stale = [f"{d['referrer']}: {d['family']}" for d in decl
             if (d["referrer"], d["family"]) not in live]
    assert not stale, ("gate_e_dynamic.tsv rows whose family is gone from the "
                       "source:\n  " + "\n  ".join(sorted(set(stale))))


def test_known_lost_rows_have_no_file():
    """A known-lost row that acquired a file is a promotion nobody recorded."""
    bad = [p for p in known_lost_paths() if (REPO / p).is_file()]
    assert not bad, f"known-lost rows with a file present: {sorted(bad)}"


@pytest.mark.live
def test_subresources_serve_as_labelled(stack):
    """The offline half trusts the developer's filesystem. Windows matches
    paths case-insensitively and the php:5.6 container does not, so a file
    stored as DimitrisEmporium.png satisfies a request for
    dimitrisEmporium.png here and 404s in the container. Ask the stack."""
    host, port = stack
    targets, _refs, _dyn, _decl = all_targets()
    lost = known_lost_paths()
    conn = http.client.HTTPConnection(host, port, timeout=15)
    wrong = []
    for t in sorted(targets):
        want = 404 if f"srv/{t}" in lost else 200
        try:
            conn.request("GET", "/" + t)
            resp = conn.getresponse()
            resp.read()
            got = resp.status
        except OSError as e:                       # keep-alive dropped
            conn.close()
            conn = http.client.HTTPConnection(host, port, timeout=15)
            got = f"error {e}"
        if got != want:
            wrong.append(f"/{t}: got {got}, ledger says {want}")
    conn.close()
    assert not wrong, ("stack disagrees with the ledger on "
                       f"{len(wrong)} subresources:\n  " + "\n  ".join(wrong))
