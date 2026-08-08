# Agent operating system — instructions, rules, skills, hooks, registers

> Register row: `docs/PROGRESS.md` P-09.

## Why

The repo had no agent files of any kind — no `CLAUDE.md`, no `AGENTS.md`, no
`.claude/`. Every rule that keeps this project from becoming a forgery lived in
prose an agent had to stumble across, and three of the governing documents lived
outside git entirely:

* `REBUILD-GUIDE.md` — cited by `README.md` and every milestone as "guide §N",
  but only present in the read-only archive junction, which is not always
  mounted. A clone could not read its own constitution.
* The milestone-3 plan — in a scratch directory outside the repo.
* The `manualevidence` analyses — ~1 MB of measured findings, several of which
  falsify constants the shipped editor is built on.

Two risks drove the design beyond "write a `CLAUDE.md`":

1. **Structural error found late is expensive.** It has already happened once:
   the editor shipped on an invented fixed-lattice geometry that footage now
   contradicts.
2. **The backend must be right where nobody can check it.** Most backend
   behaviour was never archived, so invention there survives longest.

## What was built

**Published into the repo** — `docs/REBUILD-GUIDE.md` (with a
"Superseded sections" table so no agent follows a `§` that later evidence
overturned), `docs/HUNT-LOG.md`, `docs/plans/2026-08-03-milestone-3.md`,
`docs/evidence/manualevidence/` (13 analyses + intake README; the 41 MB of
images stay outside git). All plans consolidated under `docs/plans/`.

**Always-on layer** — `websites/CLAUDE.md` (evidence tree is read-only) and
`TankTrouble/CLAUDE.md` (invariants, a reality-check table of what actually
exists, a routing table, maintenance rules). `AGENTS.md` points non-Claude tools
at it without being imported, so it costs no context and cannot become a second
rulebook.

**Path-scoped rules** — `.claude/rules/*.md`, loaded only when a matching file is
touched: provenance and ledger, PHP endpoints, Python tooling, visual evidence,
SQL and schema, docs and decisions.

**Skills** — `.claude/skills/`: `derender-route`, `resolve-subresources`,
`reconstruct-endpoint`, `adopt-visual-evidence`, `record-decision`,
`promote-provenance`, `track-work`.

**Enforcement, graded by severity** — hooks that *block* forgery-creating acts
(editing archive or `O`/`O?` bytes, creating a new `srv/` path with no ledger
row, deleting a ledger row, rewriting a `DECISIONS.md` entry), *auto-run* gates D
and E after `srv/` edits, and *warn* on the rest.

**New gates** — `test_citations.py` (every doc citation resolves),
`test_docs_single_source.py` (a number has one home),
`test_progress_register.py`, `test_foundations.py`; plus an `@caveat` check added
to gate D.

**Two registers** — `docs/FOUNDATIONS.md` records every structural commitment
with its evidence grade, **its falsifier**, its dependents, its blast radius and
its seam; `docs/PROGRESS.md` records work state.

## Corrections made while building

`note.txt` (untracked local scratch) claimed the four milestone-3 decisions had
no `DECISIONS.md` entry. They do — `DECISIONS.md` lines 280–349. No backfill was
needed and none was written. `note.txt` also lists finished milestones as
upcoming; it is stale and is not a source of truth. `README.md` has the same
problem in its "What comes next" section.

## Verification

* `python -m pytest tests/ -m "not live" -q` — existing gates unaffected, four
  new gates pass.
* One hook proved per severity: a blocked edit, an auto-gated edit, a warning.
* Fresh-session recall: ask *"summarise the rules in CLAUDE.md"*; anything missed
  means the file is too long or too vague.
* Line budgets: root `CLAUDE.md` under 30, project `CLAUDE.md` under 200.
