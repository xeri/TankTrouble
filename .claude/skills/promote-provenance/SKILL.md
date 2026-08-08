---
name: promote-provenance
description: Use when raising a file's provenance tier — known-lost to O? or O, M2 to M1, lifting a 501 stub, or deciding whether newly found bytes justify a promotion. Also use when tempted to promote and unsure.
---

# Promote a provenance tier

A promotion is a claim that a file is *more real* than it was. It needs a
citation, not a feeling. Demotion needs the same care and is far rarer than it
should be.

## The ladder

| From → to | Requires |
|---|---|
| `known-lost` → `O?` | authentic bytes located; era service inferred but not digest-proven. `place_assets.py --promote` rewrites the row |
| `known-lost` → `O` | payload's `base32(SHA1)` equals a digest on an **era** CDX row for that **exact served path** |
| `O?` → `O` | an in-era capture appears. A later-era digest match is not enough |
| `M3` → `M2` | evidence now constrains the shape (a decompiled reader, a measured capture) — the name or format is no longer free |
| `M2` → `M1` | a byte-level gate passes against real captures: gate F for every era capture of the route, gate B replay, or an equivalent |
| stub → implemented | `verified_by` names a test that exists, in the same commit |

## Citation format

Every promotion records **which gate proved it and against what**. For gate F,
that is the capture list. For an asset, the digest and the CDX rows. Put it in
the ledger `evidence` column and in the `DECISIONS.md` entry.

## Refuse to promote when

- [ ] The match is a **basename**. Different case or an unrelated tree is
      `weak-candidate-only`, and a human decides.
- [ ] The digest match is **out of era**. Authentic bytes from the wrong window
      are `wrong-era-bytes`, and the ceiling is `known-lost`.
- [ ] The proof is a **contract test you wrote**. Pinning an invention stops it
      drifting; it is not evidence. `saveMaze.php` stays `M3` and says
      `DO NOT PROMOTE`.
- [ ] The proof is **out-of-era replay**. Replaying a pre-era archived body
      proves the pre-era shape, not the era one. Flag it and ask.
- [ ] Only the **easiest** capture passes. A route is `M1` when every era capture
      passes, not the first one.
- [ ] The file is **image-derived**. Ceiling is `M2`, always.

## Order of operations

1. Confirm the gate is green *now*, on a clean run, not from memory.
2. Update `LEDGER.tsv`: tier, `evidence`, `verified_by`, `notes`.
3. `DECISIONS.md` entry naming the citation and what was rejected.
4. If the promotion closes a `known-lost` row, check `test_known_lost_rows_have_no_file`
   passes — a `known-lost` row that gained a file is an unrecorded promotion.
5. If the file is a foundation, update its `docs/FOUNDATIONS.md` grade.

## Demotion

If a promotion turns out to be unjustified, demote by **superseding** — new
`DECISIONS.md` entry, ledger row updated, old entry untouched. Never quietly
rewrite history to make the tree look cleaner than the evidence.
