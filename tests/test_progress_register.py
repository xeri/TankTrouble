"""Progress-register gate — docs/PROGRESS.md and docs/plans/ stay in step.

A plan outside the register is work nobody can find; a register row with no
evidence of completion is a claim nobody can check. The project already lost
its active plan to a scratch directory once; this stops it happening quietly.
"""

import re

from conftest import REPO

DOC = REPO / "docs" / "PROGRESS.md"
PLANS = REPO / "docs" / "plans"

KINDS = {"spec", "feature", "gate", "overhaul", "evidence"}
STATUSES = {"proposed", "active", "blocked", "done", "superseded"}
COLUMNS = ["id", "title", "kind", "status", "plan", "gate", "tag", "notes"]
DASH = "—"
CODE_RE = re.compile(r"`([^`]+)`")


def parse_rows():
    """[{column: cell}] for every P-NN row of the register table."""
    assert DOC.is_file(), "docs/PROGRESS.md missing"
    rows = []
    for line in DOC.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| P-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        assert len(cells) == len(COLUMNS), (
            f"{cells[0] if cells else line!r}: {len(cells)} columns, "
            f"expected {len(COLUMNS)}")
        rows.append(dict(zip(COLUMNS, cells)))
    assert rows, "no P-NN rows found — has the table format changed?"
    return rows


def cell_path(cell):
    """The single backticked path in a cell, or None for the honest-empty dash."""
    if cell == DASH:
        return None
    m = CODE_RE.search(cell)
    return m.group(1) if m else None


def test_ids_unique():
    ids = [r["id"] for r in parse_rows()]
    dupes = {i for i in ids if ids.count(i) > 1}
    assert not dupes, f"duplicate register ids: {sorted(dupes)}"


def test_vocabulary():
    bad = []
    for r in parse_rows():
        if r["kind"] not in KINDS:
            bad.append(f"{r['id']}: kind {r['kind']!r} not in {sorted(KINDS)}")
        if r["status"] not in STATUSES:
            bad.append(f"{r['id']}: status {r['status']!r} not in {sorted(STATUSES)}")
    assert not bad, "\n".join(bad)


def test_every_plan_file_has_a_row():
    """A plan nobody registered is a roadmap nobody can find."""
    referenced = {cell_path(r["plan"]) for r in parse_rows()}
    missing = [p.relative_to(REPO).as_posix() for p in sorted(PLANS.glob("*.md"))
               if p.relative_to(REPO).as_posix() not in referenced]
    assert not missing, (
        "plan files with no docs/PROGRESS.md row: " + ", ".join(missing))


def test_every_row_plan_exists():
    bad = [f"{r['id']}: plan {p} does not exist"
           for r in parse_rows()
           for p in [cell_path(r["plan"])] if p and not (REPO / p).is_file()]
    assert not bad, "\n".join(bad)


def test_done_rows_name_their_evidence():
    """`done` with no tag or commit is an unverifiable claim of completion."""
    bad = [f"{r['id']}: status done but tag column is empty"
           for r in parse_rows()
           if r["status"] == "done" and (not r["tag"] or r["tag"] == DASH)]
    assert not bad, "\n".join(bad)


def test_active_rows_name_a_gate():
    """Active work must say what will prove it — before it is claimed done."""
    bad = [f"{r['id']}: status active but gate column is empty"
           for r in parse_rows()
           if r["status"] == "active" and (not r["gate"] or r["gate"] == DASH)]
    assert not bad, "\n".join(bad)


def test_named_gates_exist():
    bad = [f"{r['id']}: gate {g} does not exist"
           for r in parse_rows()
           for g in [cell_path(r["gate"])] if g and not (REPO / g).exists()]
    assert not bad, "\n".join(bad)
