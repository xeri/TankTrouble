---
paths:
  - "LEDGER.tsv"
  - "srv/**"
  - "**/*.provenance"
---

# Provenance and the ledger

`LEDGER.tsv` is the spine: one row per `srv/` path, and the only place an `O`
file's provenance lives. Losing a row loses the evidence that a byte is real.

## Row grammar

Seven tab-separated columns, header exactly:

```
path  tier  sha256  source  evidence  verified_by  notes
```

* `—` (em dash) is the honest-empty cell. Never blank, never `n/a`, never `-`.
* Paths are repo-relative POSIX. Rows are sorted by path.
* `known-lost` and `pending` rows have **no file**; every other tier has one.
  `tests/test_assets.py` enforces set equality in both directions.

## Tiers

| Tier | Means | Gets a header? |
|---|---|---|
| `O` | original bytes, era-verified | **no** — injecting one would edit the original |
| `O?` | authentic bytes, era service inferred | no |
| `M1` | written, but gated byte-for-byte against captures | yes |
| `M2` | written from constrained evidence (logic, measurements) | yes |
| `M3` | invented — name, shape or behaviour has no evidence | yes |
| `known-lost` | referenced, unrecoverable, with the evidence that it is lost | no file |
| `pending` | path evidenced, rebuild scheduled | no file |

A red gate is a to-do list. A fabricated file is a forgery. When something
cannot be recovered, write the `known-lost` row **with the evidence that it is
lost** — never a plausible substitute.

## Headers on made files

Every `M*` text file carries a machine-parseable header, checked by
`tests/test_no_unlabelled.py`:

```php
/* @provenance M3
 * @evidence   NONE for the name, method, or wire format - ALL INVENTED.
 *             <deduction chain, or the capture that constrains it>
 * @verified   tests/test_savemaze.py (pins the INVENTED contract only)
 * @written    2026-08-03
 * @caveat     DO NOT PROMOTE. <what is unobservable, what was chosen, why>
 * @contains   <fenced verbatim regions, if any>
 */
```

* `@provenance` must equal the ledger tier. Disagreement is a gate failure.
* `@caveat` is required on `M2`/`M3`: name every choice the evidence does not
  force. An uncaveated invention is the failure mode this project exists to
  prevent.
* `M*` binaries get a `<name>.provenance` sidecar instead. `O` binaries
  deliberately get none.

## Mixed files

A de-rendered page is verbatim original HTML inside written PHP. File tier =
**authorship** tier; the original spans are fenced and declared:

```php
/* @O-begin source=archive-cleaned/<capture> */ ?>
...verbatim HTML...
<?php /* @O-end */
```

`tests/test_fenced_regions.py` byte-matches each fenced region against its named
source span and checks it is listed in `@contains`. Editing inside a fence is
editing an original.

## Changing rows

* Append and supersede; never delete a row to make a check pass.
* A tier promotion needs a **citation**: the gate that proves it plus the
  capture list. `known-lost` → `O?` → `O`, `M2` → `M1`. Use the
  `promote-provenance` skill.
* A row change and the file it describes belong in the same commit.
* Never add a new path under `srv/` without its row — a new fetchable path is a
  claim that the original server had that path, and needs the same evidence as
  any other claim.
