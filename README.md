# TankTrouble classic — reconstruction

Byte-faithful rebuild of the classic tanktrouble.com PHP/Flash site.
**Target era: 2017–2018.**

> A reconstruction that cannot be told apart from the original is a forgery,
> not a preservation.

Every file in `srv/` carries a provenance tier in `LEDGER.tsv`
(`O` / `O?` / `M1` / `M2` / `M3`; `known-lost` and `pending` rows have no file).
Original bytes are never edited. Made files announce themselves. Judgement calls
live in `DECISIONS.md`, append-only.

## Start here

| | |
|---|---|
| Working on it | `CLAUDE.md` — the operating manual, and `docs/NOW.md` — the current target |
| The rules | `docs/REBUILD-GUIDE.md` — read its "Superseded sections" table first |
| What is committed to structurally | `docs/FOUNDATIONS.md` |
| What is done, active, blocked | `docs/PROGRESS.md` · plans in `docs/plans/` |
| Commands and the gate matrix | `docs/reference/COMMANDS.md` |

## Layout

```
LEDGER.tsv        one row per srv/ path — the spine
DECISIONS.md      append-only log of judgement calls
DEDUCE.md         how every claim was deduced; evidence grades
srv/              the reconstructed document root
docker/           PHP 5.6 + MySQL 5.5, validated; seeds in docker/mysql/init/
seed/             importers: archive → deterministic init SQL
tools/            era resolution, skeleton build, capture cleaning, region
                  classify/annotate, and the gate E asset loop
tests/            the gates
src/mazecreator/  AS2 source for the rebuilt editor SWF
oracle/           Ruffle + Flash-projector harnesses (gate C)
archive/          junction to the read-only archive — not committed
archive-cleaned/  sha256-locked capture manifest + classification masks
docs/             the guide, the registers, agent reference, published evidence
```

## Run it

```bash
cd docker && docker compose up -d      # needs MYSQL_ROOT_PASSWORD in .env
```

→ http://127.0.0.1:8056. Unreconstructed endpoints return 501 by design.

That stack serves era bytes and is the one the gates measure. For eyeballing
only, the dev overlay labels the two blank AdSense slots; it is off by default
and declared in `docs/standards/DIVERGENCES-SERVED.md`. Gate F must run against the
default stack.

## Setup

The archive junction — needs no administrator rights:

```powershell
New-Item -ItemType Junction -Path "C:\Users\eth\websites\TankTrouble\archive" -Target "C:\Users\eth\websites\_NOT-PART-OF-MAIN-ARCHIVE_swf-recovered-2026-08-02"
```

Alternative: set `TT_ARCHIVE_ROOT`. Gates fail — never skip — if neither
resolves.

## Gates

```bash
python -m pytest tests/ -q                 # everything
python -m pytest tests/ -m "not live" -q   # offline only
```

Full matrix, including which gates need the stack:
`docs/reference/COMMANDS.md`. The one asymmetry worth knowing up front: gates A, D
and F all walk `srv/` → ledger, and only gate E walks page → subresource. That
is why a byte-perfect page serving zero images once passed three gates at once
(`docs/standards/ASSET-DISCIPLINE.md`).

## Provenance conventions

* `O` files: no injected header — that would edit original bytes. Provenance
  lives in the ledger row.
* `M*` text files: machine-parseable header (`@provenance`, `@evidence`,
  `@verified`, `@written`, `@caveat`, optional `@contains`).
* `M*` binaries: sidecar `<name>.provenance`.
* Mixed files (de-rendered pages): file tier = authorship tier; verbatim
  original regions are fenced in-file and declared in `@contains`:

  ```php
  /* @O-begin source=archive-cleaned/<capture> */ ?>
  ...verbatim HTML...
  <?php /* @O-end */
  ```

  `tests/test_fenced_regions.py` byte-matches each region against its source.

## State

Milestones 1–3 are done and tagged (`skeleton-complete`, `seed-complete`,
`m3-complete`), as is the mazeCreator rebuild (`mazecreator-editor-complete`)
and the reference-derived asset pass.

Current work, blockers and the open overhaul items are in `docs/PROGRESS.md` —
this section deliberately does not restate them, because a roadmap in two places
goes stale in one.
