"""Foundations gate — docs/FOUNDATIONS.md is complete and points at real files.

A structural commitment with no falsifier is a preference, not a deduction, and
a provisional one with no seam cannot be overhauled affordably. Both failures
only hurt months later, so a gate owns them now. See CLAUDE.md invariants and
the five rules at the top of FOUNDATIONS.md.
"""

import re

from conftest import REPO

DOC = REPO / "docs" / "FOUNDATIONS.md"

HEADING_RE = re.compile(r"^### (F-\d{2}) — (.+)$")
FIELD_RE = re.compile(r"^- \*\*([A-Za-z ]+):\*\* (.+)$")
# A backticked token that looks like a repo path: has a slash, no placeholders.
PATH_RE = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_.\-]*(?:/[A-Za-z0-9_.\-*]+)+/?)`")

FIELDS = ["Layer", "Grade", "Status", "Evidence", "Falsifier", "Dependents",
          "Blast radius", "Seam"]
GRADES = {"A", "B", "C", "D", "X", "scope"}
STATUSES = {"pinned", "provisional", "falsified", "superseded"}
WEAK_GRADES = {"C", "D", "X"}
# Live only in the archive junction, which is deliberately not committed.
EXTERNAL_PREFIXES = ("archive/", "evidence/")


def parse_foundations():
    """[(id, title, {field: value})] in document order."""
    assert DOC.is_file(), "docs/FOUNDATIONS.md missing"
    rows, current = [], None
    for line in DOC.read_text(encoding="utf-8").splitlines():
        h = HEADING_RE.match(line)
        if h:
            current = (h.group(1), h.group(2), {})
            rows.append(current)
            continue
        f = FIELD_RE.match(line)
        if f and current is not None:
            current[2][f.group(1)] = f.group(2).strip()
    assert rows, "no F-NN sections found — has the format changed?"
    return rows


def test_ids_unique_and_ordered():
    ids = [r[0] for r in parse_foundations()]
    dupes = {i for i in ids if ids.count(i) > 1}
    assert not dupes, f"duplicate foundation ids: {sorted(dupes)}"
    assert ids == sorted(ids), f"F-NN sections out of order: {ids}"


def test_every_row_is_complete():
    """Every field present and non-empty. The falsifier is the point of the
    file: without it the row records a preference, not a deduction."""
    bad = []
    for fid, _title, fields in parse_foundations():
        for name in FIELDS:
            value = fields.get(name, "")
            if not value or value == "—":
                bad.append(f"{fid}: missing or empty **{name}**")
    assert not bad, "\n".join(bad)


def test_grade_and_status_vocabulary():
    bad = []
    for fid, _title, fields in parse_foundations():
        grade = fields.get("Grade", "")
        status = fields.get("Status", "")
        if grade not in GRADES:
            bad.append(f"{fid}: grade {grade!r} not in {sorted(GRADES)}")
        if status not in STATUSES:
            bad.append(f"{fid}: status {status!r} not in {sorted(STATUSES)}")
    assert not bad, "\n".join(bad)


def test_weak_grades_are_never_pinned():
    """Grade C or below is provisional: buildable only with its dependents
    listed and a single named seam (FOUNDATIONS rule 2)."""
    bad = [f"{fid}: grade {fields['Grade']} but status pinned"
           for fid, _t, fields in parse_foundations()
           if fields.get("Grade") in WEAK_GRADES
           and fields.get("Status") == "pinned"]
    assert not bad, "\n".join(bad)


def test_falsified_rows_have_an_open_overhaul():
    """A contradiction opens an overhaul row, never a patch (rule 5)."""
    progress = (REPO / "docs" / "PROGRESS.md").read_text(encoding="utf-8")
    bad = [f"{fid}: status falsified but no row in docs/PROGRESS.md names it"
           for fid, _t, fields in parse_foundations()
           if fields.get("Status") == "falsified" and fid not in progress]
    assert not bad, "\n".join(bad)


def test_cited_paths_exist():
    """A foundation naming a file that no longer exists has silently rotted."""
    bad = []
    for fid, _title, fields in parse_foundations():
        for name in ("Dependents", "Blast radius", "Seam", "Evidence",
                     "Falsifier"):
            for raw in PATH_RE.findall(fields.get(name, "")):
                if raw.startswith(EXTERNAL_PREFIXES):
                    continue
                rel = raw.rstrip("/")
                if "*" in rel:
                    parent = REPO / rel.rsplit("/", 1)[0]
                    if not any(parent.glob(rel.rsplit("/", 1)[1])):
                        bad.append(f"{fid} **{name}**: no match for {raw}")
                elif not (REPO / rel).exists():
                    bad.append(f"{fid} **{name}**: {raw} does not exist")
    assert not bad, "\n".join(bad)
