"""Citation gate — every path this repo's instructions cite actually resolves.

Documents here are load-bearing: agents follow them literally, so a citation
that has rotted produces confident wrong work that cites the doc as its
justification. This turns the accuracy of the whole instruction surface into
something a gate owns rather than something a reader might notice.

Scope is the LIVE instruction surface only. Deliberately excluded, each for a
reason:

* DECISIONS.md, DEDUCE.md, docs/plans/* — append-only history. They legitimately
  cite files that were later renamed or removed; rewriting them to stay green
  would destroy the record. The 2026-08-08 rename map is a DECISIONS entry.
* docs/REBUILD-GUIDE.md, docs/evidence/HUNT-LOG.md — verbatim published copies of
  archive documents. Corrections go in their header tables, never in the body.
* docs/evidence/** — analyses of images that live outside the repo by design.

A backticked token counts as a citation only if it contains a slash (or is one
of the known root files) and ends in a source or document extension. Bare
filenames like `styles.css` are prose about the original site, not citations.
"""

import re

from conftest import REPO

EXTS = ("py", "php", "md", "tsv", "json", "sql", "js", "css", "as", "mjs",
        "sh", "yml", "yaml")
ROOT_FILES = {"CLAUDE.md", "AGENTS.md", "README.md", "LEDGER.tsv",
              "DECISIONS.md", "DEDUCE.md", "SECURITY.md",
              "docs/PORT-FEASIBILITY.md"}
# Not in the repo by design: the read-only archive junction and evidence dumps.
EXTERNAL_PREFIXES = ("archive/", "evidence/")

TOKEN_RE = re.compile(
    r"`([A-Za-z0-9_][A-Za-z0-9_./\-]*\.(?:" + "|".join(EXTS) + r"))"
    r"(::[A-Za-z0-9_]+|:\d+(?:-\d+)?)?`")
FENCE_RE = re.compile(r"^\s*```")


def scanned_docs():
    """The live instruction surface, repo-relative and sorted."""
    paths = [REPO / n for n in ("CLAUDE.md", "AGENTS.md", "README.md",
                                "SECURITY.md")]
    paths += sorted((REPO / ".claude" / "rules").glob("*.md"))
    paths += sorted((REPO / ".claude" / "skills").glob("*/SKILL.md"))
    paths += sorted(p for p in (REPO / "docs").glob("*.md")
                    if p.name != "REBUILD-GUIDE.md")
    paths += sorted((REPO / "docs" / "standards").glob("*.md"))
    paths += sorted((REPO / "docs" / "reference").glob("*.md"))
    return [p for p in paths if p.is_file()]


def citations(path):
    """[(raw, target, suffix, lineno)] outside fenced code blocks."""
    out, in_fence = [], False
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(),
                                  start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for target, suffix in TOKEN_RE.findall(line):
            if target.startswith(EXTERNAL_PREFIXES):
                continue
            if "/" not in target and target not in ROOT_FILES:
                continue
            out.append((target, suffix, lineno))
    return out


def test_the_surface_is_not_empty():
    """Guard against a rename silently emptying this gate."""
    docs = scanned_docs()
    assert len(docs) >= 15, f"only {len(docs)} docs scanned — path glob broken?"
    assert sum(len(citations(d)) for d in docs) >= 50, "suspiciously few citations"


def test_cited_files_exist():
    bad = []
    for doc in scanned_docs():
        rel = doc.relative_to(REPO).as_posix()
        for target, _suffix, lineno in citations(doc):
            if not (REPO / target).is_file():
                bad.append(f"{rel}:{lineno}: {target} does not exist")
    assert not bad, "\n".join(bad) + (
        "\nFix the citation, or add the path. Never delete the file to "
        "make this pass.")


def test_cited_symbols_exist():
    """`file.py::symbol` — symbols survive insertions above them, which is why
    they are preferred over line numbers."""
    bad = []
    for doc in scanned_docs():
        rel = doc.relative_to(REPO).as_posix()
        for target, suffix, lineno in citations(doc):
            if not suffix.startswith("::"):
                continue
            f = REPO / target
            if not f.is_file():
                continue
            if suffix[2:] not in f.read_text(encoding="utf-8", errors="replace"):
                bad.append(f"{rel}:{lineno}: {target} has no {suffix[2:]}")
    assert not bad, "\n".join(bad)


def test_cited_line_numbers_are_in_range():
    """Line numbers drift on every insertion. This catches the drift; it cannot
    catch a citation that still resolves but now points at the wrong thing —
    which is why the rule is to prefer symbols."""
    bad = []
    for doc in scanned_docs():
        rel = doc.relative_to(REPO).as_posix()
        for target, suffix, lineno in citations(doc):
            if not suffix.startswith(":") or suffix.startswith("::"):
                continue
            f = REPO / target
            if not f.is_file():
                continue
            last = int(suffix[1:].split("-")[-1])
            total = len(f.read_text(encoding="utf-8",
                                    errors="replace").splitlines())
            if last > total:
                bad.append(f"{rel}:{lineno}: {target}{suffix} — file has "
                           f"{total} lines")
    assert not bad, "\n".join(bad)
