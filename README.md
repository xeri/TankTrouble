# TankTrouble classic — reconstruction

Rebuild of the classic tanktrouble.com PHP/Flash site, governed by
`archive/REBUILD-GUIDE.md`. **Target era: 2017–2018.**

> A reconstruction that cannot be told apart from the original is a forgery,
> not a preservation.

Every file in `srv/` carries a provenance tier in `LEDGER.tsv`
(`O` / `O?` / `M1` / `M2` / `M3`; `known-lost` and `pending` rows have no file).
Original bytes are never edited. Made files announce themselves. Judgement
calls live in `DECISIONS.md` (append-only).

## Layout

```
LEDGER.tsv        one row per srv/ path — the spine
DECISIONS.md      append-only log of judgement calls
srv/              the reconstructed document root
docker/           PHP 5.6 + MySQL 5.5 skeleton (UNVALIDATED — no docker here yet)
tools/            resolve_era.py (era choice), build_skeleton.py (copy/verify/stub)
tests/            CI gates A (asset integrity) + D (structural)
archive/          junction to the read-only archive (not committed)
archive-cleaned/  created at order-of-work step 3, not yet — cleaned O captures
```

## Setup

The archive junction (needs no admin):

```powershell
New-Item -ItemType Junction -Path "C:\Users\eth\websites\TankTrouble\archive" -Target "C:\Users\eth\websites\_NOT-PART-OF-MAIN-ARCHIVE_swf-recovered-2026-08-02"
```

Alternative: set `TT_ARCHIVE_ROOT` to the archive path. Tests fail (never
skip) if neither resolves.

## Gates

```
python -m pytest tests/ -q
```

* **Gate A** (`tests/test_assets.py`) — every `O`/`O?` row: sha256 recomputed
  from `srv/` AND from the archive source; three-way match or red.
* **Gate D** (`tests/test_no_unlabelled.py`) — every `srv/` file has a ledger
  row; every `M*` text file has a parseable `@provenance` header; no
  unverified stub returns 200; credential-shaped-string scan.

## Provenance conventions

* `O` files: no header injected (that would edit original bytes) — provenance
  lives in the ledger row only.
* `M*` text files: machine-parseable header (`@provenance`, `@evidence`,
  `@verified`, `@written`, `@caveat`, optional `@contains`).
* `M*` binaries (none yet): sidecar `<name>.provenance`.
* Mixed files (from de-rendering, guide §6.1a): file tier = authorship tier;
  verbatim-original regions are fenced in-file:

  ```php
  /* @O-begin source=archive-cleaned/<capture> */ ?>
  ...verbatim HTML...
  <?php /* @O-end */
  ```

  and declared in the header's `@contains` line. The step-6 harness verifies
  each fenced region byte-matches its named source span.

## What comes next (guide §9)

1. ~~Skeleton + LEDGER + gates A/D~~ ← this milestone
2. **Ruffle vs projector spike on `SetVariable`** — do EARLY, can change design
3. Clean captures + un-do PageSpeed (§6.1a steps 1–2) → `archive-cleaned/` as O
4. Seed DB from archive
5. `loadMaze.php` → gate B, 843/843
6. De-render the 6 routes → gate F byte-diff. **Build the Gate F harness
   before writing any route PHP** (§7.4a).
