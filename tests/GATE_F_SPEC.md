# Gate F — render byte-diff harness (SPEC ONLY, guide §7.4a)

Written as milestone-3 prep. **No route PHP exists yet**; the guide requires
this harness to exist before any is written. This spec pins the design so
the first de-rendered route lands straight into a working gate.

## Inputs

1. **Diff corpus**: `archive-cleaned/MANIFEST.tsv` — 411 sha256-locked
   classic captures across root/game/garage/news/forum/lab/shop/embed/
   infirmary/statistics. Gate F reads the era-window subset (2017-2018) at
   first; cross-year rows join as template-history tests later.
2. **Masks**: `archive-cleaned/classification/<route>.tsv` (draft produced
   mechanically by `tools/classify_regions.py`, line-granular). Milestone 3
   upgrades each `dynamic` region with an annotation column naming the
   producing variable/loop (e.g. `deploy-tag asset prefix`, `session nonce`,
   `SAJAX login challenge`, `news loop`). **A region without an annotation
   blocks the gate for that route** — an unexplained region is an
   ununderstood region (guide 6.1a step 3).
3. **Rendering stack**: the validated docker pair (php:5.6 + seeded
   mysql:5.5) on 127.0.0.1:8056.

## Procedure (tests/test_render_diff.py, milestone 3)

For each era capture of a route with a fully-annotated mask:

1. Fetch `http://127.0.0.1:8056/?<route>` with the capture's known inputs
   (logged-out defaults; per-capture inputs recorded in the mask header when
   discovered — e.g. the DB as-of state for forum/news listings).
2. Split response and capture into lines; drop mask-dynamic line ranges from
   both.
3. Assert the remaining byte sequence is **identical**. Line-granularity is
   the floor: where a line mixes static text and one echoed value, the mask
   may carry a regex with ONE capture group per echo — anything more complex
   must be split back into classification first.

A route passing for every era capture is **M1** (promotion citation = this
gate + the capture list). Failures print the first divergent line pair.

## Mask discipline

* Masks live under version control; every change is reviewable evidence.
* The mask may only shrink or annotate; a mask that **grows** to make the
  gate pass is the reconstruction drifting (guide 7.4a corollary) — treat as
  a defect, not a fix.
* Current draft mask sizes (mechanical, pre-annotation):
  root 37 regions / game 37 / garage 32 / news 30 / forum 25 / lab 26 /
  shop 25 / embed 5 / infirmary 0.

## DB as-of problem (recorded, unsolved)

Forum/news listings on captured pages reflect the DB at capture time; the
seeded DB holds the full corpus (2026 fetch). Options for milestone 3, in
current preference order: (a) render-time `created <= capture_ts` filtering
in the reconstructed PHP's queries where the ORIGINAL demonstrably ordered/
limited by time anyway; (b) classifying the listing blocks as dynamic and
gating only their invariant scaffolding; (c) per-capture DB snapshots
(rejected: mutates seed data per test). Decide when the first affected route
(forum) is de-rendered.
