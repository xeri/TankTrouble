"""Shared gate-F comparator (guide 7.4a; GATE_F_SPEC + DECISIONS 2026-08-03).

Line-mode with difflib projection: era captures of one route differ in line
COUNT, so mask ranges (defined on the reference capture) are projected onto
the other side via SequenceMatcher opcodes instead of positional dropping.

Modes per reference line, derived from the annotation column:
  G (gated)  — must survive byte-identical on the other side
  M (masked) — may differ / be absent; extra other-side lines may attach
plus regex regions (echo:$x re=...) where every projected line must
fullmatch the pattern — the static remainder of the line stays gated.

template-edit:<from>[..<to>] is side-dependent: on the CAPTURE side the
region is gated only when the capture ts falls inside the window (the ref
bytes were live then); on the RENDER side it is always gated — the
reconstruction must emit the era-final reference text.

REMOVED BLOCKS: template content deleted before the era-final reference has
no reference lines, so no region can mask it. Those blocks live in
classification/<route>-removed.tsv: (ref position, validity window, max
observed lines, name). A capture-side insert is legal iff it touches a
masked region OR matches a removed-block row (position + window + size cap).
The RENDER side never gets this allowance — the reconstruction must not
emit removed content.
"""

import difflib
import re
import sys

from conftest import REPO

sys.path.insert(0, str(REPO / "tools"))
import annotate_regions as ann          # noqa: E402  (path set above)
import classify_regions as cls          # noqa: E402


def load_mask(route):
    """[(rid, a, b, status, annotation-cell)] with 0-based end-exclusive
    line ranges, straight from the committed TSV."""
    out = []
    _, rows = ann.read_tsv(route)
    for r in rows:
        lo, hi = r["ref_lines"].split("-")
        out.append((r["region_id"], int(lo) - 1, int(hi), r["status"],
                    r["annotation"]))
    return out


def load_removed(route):
    """[(removed_id, ref_pos_1based, lo, hi, max_lines, name)] from the
    optional <route>-removed.tsv sidecar."""
    p = REPO / "archive-cleaned" / "classification" / ("%s-removed.tsv" % route)
    if not p.is_file():
        return []
    out = []
    lines = p.read_text(encoding="utf-8").splitlines()
    assert lines[0].split("\t") == ["removed_id", "ref_pos", "window",
                                    "max_lines", "name", "sample"], (
        "%s: bad header" % p.name)
    for l in lines[1:]:
        if not l.strip():
            continue
        rid, pos, window, mx, name, _sample = l.split("\t")
        lo, _, hi = window.partition("..")
        assert re.match(r"\A\d{8}\Z", lo) and re.match(r"\A\d{8}\Z", hi), (
            "%s %s: window must be YYYYMMDD..YYYYMMDD" % (p.name, rid))
        out.append((rid, int(pos), lo, hi, int(mx), name))
    return out


def blocking_regions(mask):
    return [rid for rid, _, _, status, cell in mask
            if status == "dynamic" and ann.blocks_gate(cell)]


def line_modes(mask, side, ts8=None):
    """(modes list of 'G'/'M' per ref line, [(rid, a, b, compiled-regex)])"""
    n = mask[-1][2] if mask else 0
    modes = ["G"] * n
    regexes = []
    for rid, a, b, status, cell in mask:
        if status != "dynamic":
            continue
        parsed = ann.parse_annotation_cell(cell)
        kinds = [k for k, _ in parsed]
        if kinds == ["echo"] and parsed[0][1][1]:
            regexes.append((rid, a, b, re.compile(parsed[0][1][1])))
            for i in range(a, b):
                modes[i] = "M"      # regex pass handles it separately
        elif all(k == "template-edit" for k in kinds):
            gated = side == "render" or (
                ts8 is not None and any(lo <= ts8 <= hi
                                        for _, (lo, hi) in parsed))
            if not gated:
                for i in range(a, b):
                    modes[i] = "M"
        else:
            for i in range(a, b):
                modes[i] = "M"
    return modes, regexes


def opcodes(ref, other):
    return difflib.SequenceMatcher(
        a=ref, b=other, autojunk=False).get_opcodes()


def check_side(ref, other, modes, regexes, label, removed=(), ts8=None):
    """Divergence strings ([] = pass). ref/other are line lists. `removed`
    (capture side only) carries the removed-block allowances."""
    div = []
    ops = opcodes(ref, other)
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            continue
        if tag in ("delete", "replace"):
            bad = [i for i in range(i1, i2) if modes[i] == "G"]
            if bad:
                i = bad[0]
                got = other[j1:j2][:2]
                div.append(
                    "%s: gated ref line %d not matched\n  ref  |%s\n  got  %s"
                    % (label, i + 1, ref[i][:160],
                       " / ".join(repr(g[:160]) for g in got) or "(absent)"))
        elif tag == "insert":
            touches_masked = ((i1 < len(modes) and modes[i1] == "M") or
                              (i1 > 0 and modes[i1 - 1] == "M"))
            allowed_removed = any(
                pos == i1 + 1 and lo <= (ts8 or "") <= hi
                and j2 - j1 <= mx
                for _rid, pos, lo, hi, mx, _n in removed)
            if not touches_masked and not allowed_removed:
                div.append(
                    "%s: %d unexplained extra line(s) at ref position %d, "
                    "first: %r" % (label, j2 - j1, i1 + 1, other[j1][:160]))
    for rid, a, b, pat in regexes:
        lines = ann.project(ops, other, a, b)
        if len(lines) != b - a:
            div.append("%s: echo region %s projected %d lines, expected %d"
                       % (label, rid, len(lines), b - a))
            continue
        for line in lines:
            if not pat.match(line):
                div.append("%s: echo region %s line fails its regex: %r"
                           % (label, rid, line[:160]))
    return div


def era_route_bodies(archive_root, route):
    """(caps, bodies) for the era window, archive order, ref = bodies[-1]."""
    rows = cls.manifest_rows()
    caps = cls.era_captures(rows, route)
    bodies = []
    for r in caps:
        src = archive_root / r["source"].replace("archive/", "", 1)
        bodies.append(src.read_text(encoding="utf-8",
                                    errors="replace").splitlines())
    return caps, bodies
