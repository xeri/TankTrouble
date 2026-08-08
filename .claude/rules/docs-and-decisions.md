---
paths:
  - "*.md"
  - "docs/**/*.md"
---

# Writing documentation here

Documents in this repo are load-bearing: agents follow them literally, so a
stale one produces confident wrong work that cites the doc as justification.
Treat them like code.

## One fact, one home

| Owner | Content |
|---|---|
| `LEDGER.tsv` | per-file provenance |
| `DECISIONS.md` | judgement calls, append-only |
| `DEDUCE.md` | how a claim was deduced, and its grade |
| `docs/FOUNDATIONS.md` | structural commitments, falsifiers, blast radius |
| `docs/standards/BACKEND-CONTRACTS.md` | what the corpus proves vs what was chosen |
| `docs/reference/ARCHITECTURE.md` | every constant, by name |
| `docs/NOW.md` | the one current target |
| `docs/PROGRESS.md` | what is proposed / active / blocked / done |
| `docs/BACKLOG.md` | ideas nobody is working on yet |

Cite by name, do not restate. Two copies of a number guarantee an eventual
disagreement, and `tests/test_docs_single_source.py` will fail on the second
copy.

## DECISIONS.md is append-only

Newest at the bottom. Never edit an existing entry — supersede it, naming what
it replaces, in the format the file already uses:

```
## YYYY-MM-DD — <what was decided> [SUPERSEDES "<old entry>", <date>]
<why; what the evidence forced; what was rejected and why>
Reversible: yes/no — <how to undo>
```

Entry checklist: the decision, the evidence, the **rejected** alternatives, and
reversibility. An entry without rejected alternatives usually means the decision
was not actually made.

## Citations

* Prefer **symbols** to line numbers: `tests/test_assets.py::test_file_set_equality`,
  `refgraph.Ref.clamped`. Line numbers drift on every insertion; symbols survive
  insertions above them.
* Where a line number is unavoidable, pin it to a commit.
* `tests/test_citations.py` resolves every reference in every tracked `*.md`.
  Broken citation = failing gate, not a typo.

## Honesty rules

* Document what exists, not what is planned. Planned work goes in
  `docs/PROGRESS.md` with a status, or in a `docs/plans/` file.
* Say when something is impossible rather than pending: zero era captures and
  zero archived bodies are permanent facts, not to-do items.
* Record the failure a rule exists to prevent. Rules without reasons do not
  generalise, and the reason is what lets a later reader overturn the rule
  correctly.
* Every file in `docs/plans/` needs a `docs/PROGRESS.md` row and vice versa
  (`tests/test_progress_register.py`).
* Published copies of archive documents (`docs/REBUILD-GUIDE.md`,
  `docs/evidence/HUNT-LOG.md`) are verbatim below their header rule. Correct them by
  superseding in `DECISIONS.md` and adding a row to the header's table — never
  by editing the body.
