# Glossary

## Provenance tiers (`LEDGER.tsv`)

| Tier | Means |
|---|---|
| `O` | original bytes, era-verified. Never edited; no injected header |
| `O?` | authentic bytes, era service inferred rather than digest-proven |
| `M1` | written, and gated byte-for-byte against real captures |
| `M2` | written from constrained evidence — a decompiled reader, a measurement |
| `M3` | invented. The name, shape or behaviour has no evidence |
| `known-lost` | referenced but unrecoverable, with the evidence that it is lost. No file |
| `pending` | path evidenced, rebuild scheduled. No file |

## Asset verdicts (`tools/asset_choices.tsv`)

`era-digest-match` → `O` · `judged` → `O?` · `held-no-era-cdx` → `O?` ·
`wrong-era-bytes`, `cdx-observed`, `weak-candidate-only`, `unobserved` →
`known-lost`. Definitions: `docs/standards/ASSET-DISCIPLINE.md`.

## Gates

| | Name | Proves |
|---|---|---|
| A | asset integrity | `O` bytes match ledger **and** archive source |
| B | replay | the endpoint reproduces every invariant the corpus pins |
| C | the Flash oracle | projector and Ruffle render identically |
| C1 | cleaned captures | the capture set is exactly the sha256-locked manifest |
| D | structural | everything labelled, announced, and no stub returning 200 |
| E | subresource resolution | every reference resolves or is a recorded loss |
| F | render byte-diff | served HTML byte-matches captures outside the masks |
| S | seeds | seeded row counts match the corpora |

**Naming collision:** guide §7.5 calls gate E "visual regression". In this repo
gate E is subresource resolution; visual regression is gate C. The guide's
published copy carries this in its superseded table.

## Vocabulary

**Era partition** — one hostname, two different sites. CLASSIC is PHP + Flash
with `?query` routes; MODERN is an SPA that answers 200 for *any* path, so a
modern-era 200 is worthless as filesystem evidence.

**`@O` fence** — `/* @O-begin source=… */ … /* @O-end */`, marking verbatim
original bytes inside a written file. Declared in the header's `@contains` and
byte-verified by `tests/test_fenced_regions.py`.

**De-rendering** — inverting captured HTML back into PHP source, using diffs
across captures to separate literal text from echoed values.

**Mask / annotation** — the per-route classification of which lines are dynamic,
plus the annotation naming what produces each one. An unannotated region blocks
gate F for that route.

**CODE12** — the 12-character prefix in a `loadMaze` corpus filename. It is the
Wayback sha1-base32 digest of the response body, i.e. a **capture identity**,
not a user code.

**Pair message** — the wire envelope: `q=`/`r=` plus base64 of shuffled `k=v&…`
pairs. The shuffle is per request; the order carries no meaning.

**THE OVERHAUL RULE** — every `M2`/`M3` visual, animation, interaction or copy
text is a placeholder pending evidence. When evidence arrives, the piece is
rewritten wholesale, never patched to be "close enough".

**Seam** — the single module that owns an invented value, so an overhaul is a
one-file change.

**Falsifier** — the observation that would overturn a claim. Required on every
`docs/FOUNDATIONS.md` row; a claim without one is a preference, not a deduction.

**Divergence** — any way the reconstruction's user-visible output differs from
what the original served. Logged before it ships, and made visibly non-original
on screen so no screenshot can be mistaken for evidence.

**Confidence tags** (image evidence) — `[OBSERVED]` `[MEASURED]` `[INFERRED]`
`[UNCERTAIN]` `[NOT VISIBLE]`. Never promoted when quoted.
