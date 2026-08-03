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
DEDUCE.md         how every claim was deduced; evidence grades
srv/              the reconstructed document root
docker/           PHP 5.6 + MySQL 5.5, validated; seeds in docker/mysql/init/
seed/             importers: archive → deterministic init SQL
tools/            era resolution, skeleton build, capture cleaning, region classify
tests/            gates A (assets), D (structural), S (seeds), C1 (cleaned captures)
oracle/           Ruffle spike harness + DIVERGENCES.md (gate C groundwork)
archive/          junction to the read-only archive (not committed)
archive-cleaned/  sha256-locked capture manifest + classification drafts
```

Run the stack: `cd docker`, put `MYSQL_ROOT_PASSWORD=<anything>` in `.env`,
`docker compose up -d` → http://127.0.0.1:8056 (stubs 501 by design).

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

1. ~~Skeleton + LEDGER + gates A/D~~ (`skeleton-complete`)
2. ~~Ruffle spike on `SetVariable`~~ — bridge works, SetVariable ABSENT;
   consequences in `oracle/DIVERGENCES.md`. Projector half still open.
3. ~~Clean captures~~ (`archive-cleaned/`; classic captures are PageSpeed-free)
4. ~~Seed DB from archive~~ (`seed-complete`; live-imported and verified)
5. `loadMaze.php` → gate B, 843/843 ← **milestone 3 starts here**
6. De-render the 6 routes → gate F byte-diff. Harness spec ready
   (`tests/GATE_F_SPEC.md`); masks drafted
   (`archive-cleaned/classification/`); **annotate every dynamic region
   before writing route PHP** (§7.4a).
