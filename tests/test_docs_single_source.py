"""Single-source gate — a watched constant has exactly one home.

Two copies of a number guarantee an eventual disagreement, and the copy that
goes stale is indistinguishable from the copy that is right.
docs/reference/ARCHITECTURE.md owns every constant; the always-on instruction files cite them
by name and never restate the value.

Scope is deliberately narrow: CLAUDE.md and .claude/**. Registers and reference
documents (FOUNDATIONS, PROGRESS, ASSET-DISCIPLINE, DECISIONS, the analyses)
legitimately quote evidence figures — that is what they are for.
"""

import re

from conftest import REPO

OWNER = REPO / "docs" / "reference" / "ARCHITECTURE.md"

# name -> the literal string as it appears in the owner.
# Only values distinctive enough that an occurrence is certainly a restatement.
# Small round numbers (32, 13, 5) are deliberately absent: they collide with
# ordinary prose (`base32`, "13 analyses") and a gate that cries wolf gets
# switched off.
WATCHED = {
    "LEDGER_ROWS": "430",
    "SRV_FILES": "326",
    "STACK_PORT": "8056",
    "CDX_ROWS": "74,165",
    "CLEANED_CAPTURES": "411",
    "DYNAMIC_REGIONS": "217",
    "MAZE_PAYLOADS": "843",
    "MAZE_DISTINCT_BODIES": "744",
    "MAZE_STATES": "672",
    "SUBRESOURCES_REFERENCED": "219",
    "SUBRESOURCES_RESOLVED": "156",
    "SUBRESOURCES_KNOWN_LOST": "63",
    "ASSETS_PLACED": "134",
    "ROUNDTRIP_GRIDS": "670",
    "FORUM_REPLIES": "228,316",
}


def guarded_docs():
    """The always-on surface, which must cite constants rather than restate."""
    paths = [REPO / "CLAUDE.md", REPO / "AGENTS.md"]
    paths += sorted((REPO / ".claude" / "rules").glob("*.md"))
    paths += sorted((REPO / ".claude" / "skills").glob("*/SKILL.md"))
    return [p for p in paths if p.is_file()]


def test_owner_holds_every_watched_constant():
    """If the owner loses a value, the registry is describing a fiction."""
    assert OWNER.is_file(), "docs/reference/ARCHITECTURE.md missing"
    text = OWNER.read_text(encoding="utf-8")
    missing = [f"{name} ({value})" for name, value in WATCHED.items()
               if value not in text]
    assert not missing, (
        "docs/reference/ARCHITECTURE.md no longer contains: " + ", ".join(missing) +
        "\nUpdate the value there and update WATCHED to match.")


def test_always_on_docs_do_not_restate_constants():
    bad = []
    for doc in guarded_docs():
        rel = doc.relative_to(REPO).as_posix()
        for lineno, line in enumerate(
                doc.read_text(encoding="utf-8").splitlines(), start=1):
            for name, value in WATCHED.items():
                # bounded on both sides so 430 does not fire inside 4300 or
                # base430, and 156 does not fire inside a sha256 digest
                if re.search(r"(?<![\w,.])" + re.escape(value) + r"(?![\w,.])",
                             line):
                    bad.append(f"{rel}:{lineno}: restates {name} = {value}")
    assert not bad, "\n".join(bad) + (
        "\nCite the constant by name and let docs/reference/ARCHITECTURE.md own "
        "the value.")
