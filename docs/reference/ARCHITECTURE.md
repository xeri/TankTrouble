<!-- Single source for every constant other documents cite. If a number appears
     twice in this repo's instruction surface, this file is the one that is
     right and the other is a bug. Verified 2026-08-08 against commit e8ac581. -->

# Architecture and the numbers

## Shape

```
LEDGER.tsv        the spine — one row per srv/ path
DECISIONS.md      append-only judgement log
DEDUCE.md         how each claim was deduced, and its evidence grade
srv/              the reconstructed document root (served as-is)
docker/           PHP 5.6 + MySQL 5.5; seeds in docker/mysql/init/
seed/             importers: archive corpora → deterministic init SQL
tools/            era resolution, skeleton build, capture cleaning,
                  region classify/annotate, and the gate E asset loop
tests/            the gates
src/mazecreator/  AS2 source for the rebuilt editor SWF
oracle/           Ruffle + Flash-projector harnesses (gate C)
archive/          junction to the read-only archive — not committed
archive-cleaned/  sha256-locked capture manifest + classification masks
docs/             everything an agent needs that is not code
```

## Life of a request

A browser asks `127.0.0.1:8056` for `/?<route>`. Apache runs `srv/index.php` —
one file, no per-route includes, because any new file under `srv/` would be a
fetchable path with no CDX evidence behind it (F-03).

`index.php` handles a `rs=` SAJAX call **before** emitting any page, then
dispatches on the query string to one of six routes. Reconstructed regions are
verbatim capture bytes inside `@O-begin` / `@O-end` fences; everything that
varied between captures is echoed and has a mask annotation naming the variable
that produces it.

Endpoints under `srv/includes/` speak the pair-message wire format:
`q=` base64 of shuffled `k=v&…` in, `r=` base64 of shuffled `k=v&…` out.
`rebuild-db.php` — the one deliberately modern-named file — connects with
`mysql_*` from `TT_DB_*` environment.

The Flash stage is not reconstructed in the page. Browsers have no plugin, so
the stage shows the browser's own message; a player belongs in gate C, not in
the served bytes.

## The numbers

Cite these **by name**, never by restating the value.

### Repository

| Name | Value |
|---|---|
| `LEDGER_ROWS` | 430 |
| `SRV_FILES` | 326 (excluding `.provenance` sidecars) |
| `TIER_COUNTS` | `O` 296 · `known-lost` 104 · `M2` 20 · `O?` 4 · `M1` 3 · `M3` 3 |
| `GATE_FILES` | 13 `tests/test_*.py` |
| `STACK_ADDR` | `127.0.0.1:8056` |

### Evidence corpora

| Name | Value |
|---|---|
| `ERA_WINDOW` | 2017–2018 |
| `ERA_PARTITION` | CLASSIC … 2020-12-04 · MODERN 2020-12-22 … |
| `CDX_ROWS` | 74,165 |
| `CLEANED_CAPTURES` | 411 sha256-locked rows in `archive-cleaned/MANIFEST.tsv` |
| `DYNAMIC_REGIONS` | 217 across root/game/garage/news/forum/lab/shop/embed |
| `EVIDENCE_GRADES` | A observed · B unambiguous indirect · C name/shape only · D wrong era or site · X artefact |

### loadMaze corpus

| Name | Value |
|---|---|
| `MAZE_PAYLOADS` | 843 archived payloads (842 bodies + 1 `notFound`) |
| `MAZE_DISTINCT_BODIES` | 744 |
| `MAZE_STATES` | 672 distinct `(author, slot)` states |
| `MAZE_NOTFOUND_BODY` | `r=bm90Rm91bmQ9dHJ1ZQ==` |
| `MAZE_REPLAY_CAP` | 25,000 requests (expected ≈4,800) |

### Seeded database

| Name | Value |
|---|---|
| `DB_NAME` | `tanktrouble` |
| `ROW_COUNTS` | mazes 672 · forum threads 467 · replies 228,316 · news 224 |
| `DB_ENGINE` | MyISAM, utf8mb3, `utf8_general_ci` (F-07, provisional) |
| `AUTHOR_KEY` | `VARBINARY(16)` (F-06) |

### Subresources (gate E)

| Name | Value |
|---|---|
| `SUBRESOURCES_REFERENCED` | 219 |
| `SUBRESOURCES_RESOLVED` | 156 |
| `SUBRESOURCES_KNOWN_LOST` | 63 |
| `ASSETS_PLACED_2026_08_04` | 134 (78 era-digest-matched, 53 refetched, 3 judged) |

### mazeCreator

| Name | Value |
|---|---|
| `STAGE` | 688 × 400 at 25 fps |
| `CELL` | 32 px |
| `LATTICE_ORIGIN` | (56, 50) — F-08, falsified, pending overhaul |
| `GRID_MAX` | 18 × 10 |
| `EDITOR_LIMITS` | title ≤ 32 legal chars · author ≤ 16 · ≤ 5 tanks · ≤ 5 crates · ≤ 10 objects |
| `WALL` | 4 px, `#444444` |
| `FLOOR_TONES` | `#dddddd` / `#eeeeee`, ≈1/3 light (F-10, provisional) |
| `ROUNDTRIP_GRIDS` | 670/670 byte-identical |
| `FADE_FRAMES` | 15 @ 25 fps |

### SAJAX

| Name | Value |
|---|---|
| `SAJAX_VERSION` | Sajax 0.12, lightly modified (F-11) |
| `SAJAX_EXPORTS` | 33 wrappers after 2017-03-30 (34 with `showShop` before); infirmary emits 2 |

## Where the numbers came from

Each is traceable: repository counts are computed from the working tree;
corpus counts are recorded in `DECISIONS.md` at the entry that established them;
mazeCreator constants are measured in `docs/standards/MAZECREATOR-VISUAL-SPEC.md`;
subresource counts are the state recorded in `docs/standards/ASSET-DISCIPLINE.md`.

When a number changes, change it **here** and let the citations follow.
`tests/test_docs_single_source.py` fails if a watched constant is restated
anywhere in the instruction surface.
