---
name: derender-route
description: Use when turning a captured page into reconstructed PHP — de-rendering a route, adding a page, annotating classification masks, or getting gate F to pass for a route. Covers guide 6.1a end to end.
---

# De-render a route

Inverting captured HTML back into PHP source. The original PHP is unrecoverable,
so the capture is the specification and gate F is the proof.

## Before you write any PHP

- [ ] **The harness exists.** `tests/test_render_diff.py` and
      `tests/test_fenced_regions.py` must be in place first (guide §7.4a). Prove
      the plumbing on `infirmary` — an `O` file with zero dynamic regions — before
      trusting it on a real route.
- [ ] **Gather the capture set.** Era-window rows from
      `archive-cleaned/MANIFEST.tsv` for this route. More captures is strictly
      better: bytes identical across captures are literal text, bytes that vary
      are echoed values.
- [ ] **Classify.** `python tools/classify_regions.py` produces the line-granular
      draft mask at `archive-cleaned/classification/<route>.tsv`.

## Annotate every dynamic region

An unannotated region **blocks the gate for that route**. An unexplained region
is an ununderstood region — that is the whole point of the rule.

Vocabulary (5th column):

| Annotation | Use for |
|---|---|
| `echo:$<name>` (+ optional `re=` with exactly one capture group) | a single echoed value |
| `loop:<name>` | variable-height block, compared in anchor mode |
| `template-edit:<from-ts>[..<to-ts>]` | literal text with a validity window |
| `per-request:<what>` | always masked; includes anything date-dependent — never fake the clock |
| `ad-block` | always masked |
| `needs-split:<why>` | blocks the gate, same as empty |

`python tools/annotate_regions.py --variants <route> [<region_id>]` prints every
distinct byte-form of a region across era captures with timestamps. Use it — the
classification becomes mechanical rather than a guess.

## Write the PHP

- [ ] Verbatim spans go inside `@O-begin source=… / @O-end` fences and are listed
      in the header's `@contains`. Do not retype original HTML.
- [ ] No new file under `srv/` — shared emitters are in-file functions.
- [ ] Every echoed value traces to a mask annotation. If you are echoing
      something no annotation named, you have invented a dynamic region.
- [ ] Unreconstructed parts stay a loud 501 from inside the dispatcher.

## Prove it

```bash
python -m pytest tests/test_render_diff.py -k <route>   # gate F, needs the stack
python tools/refgraph.py && python -m pytest tests/test_subresources.py -q
python -m pytest tests/ -q
```

- [ ] Gate F green for **every** era capture of the route, not the easiest one.
- [ ] Gate E green — a new page asks for new subresources; resolve them through
      `resolve-subresources`, never by copying a plausible file into place.
- [ ] A mask that **grew** to make the gate pass is the reconstruction drifting.
      Treat it as a defect, not a fix.

## Land it

- [ ] Flip `verified_by` in `LEDGER.tsv` to the gate that now proves the file,
      in the same commit as the code.
- [ ] Tier promotion only when the promotion criterion is met in full (for
      `index.php`: root plus all six routes passing every era capture). Use
      `promote-provenance`.
- [ ] `DECISIONS.md` entry for anything the evidence did not force.
- [ ] Any user-visible difference goes in `docs/standards/DIVERGENCES-SERVED.md` **before**
      it ships.

## Known unsolved

The DB as-of problem: captured listings reflect the DB at capture time, the
seeded DB holds the full corpus. Preference order is recorded in
`tests/GATE_F_SPEC.md` — render-time `created <= capture_ts` filtering only where
the original demonstrably ordered by time anyway, else anchor-mode gating of the
invariant scaffolding. Per-capture snapshots are rejected: they mutate seed data
per test.
