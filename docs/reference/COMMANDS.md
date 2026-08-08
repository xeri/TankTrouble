# Commands and the gate matrix

## Daily

```bash
python -m pytest tests/ -q                  # everything (needs archive + stack)
python -m pytest tests/ -m "not live" -q    # offline gates only
cd docker && docker compose up -d           # the stack (needs docker/.env)
python tools/refgraph.py                    # what does the site ask for now?
```

## Setup

The archive junction — needs no administrator rights:

```powershell
New-Item -ItemType Junction -Path "C:\Users\eth\websites\TankTrouble\archive" -Target "C:\Users\eth\websites\_NOT-PART-OF-MAIN-ARCHIVE_swf-recovered-2026-08-02"
```

Alternative: set `TT_ARCHIVE_ROOT`. Gates **fail** (never skip) if neither
resolves — a silently-skipped gate A is a green lie.

The stack needs `MYSQL_ROOT_PASSWORD` and the `TT_DB_*` variables in
`docker/.env`, which is never committed. Address and port: `STACK_ADDR` in
`architecture.md`.

## The gate matrix

| Gate | Test | Asks | Live? |
|---|---|---|---|
| A | `tests/test_assets.py` | do the `O`/`O?` bytes match the ledger **and** the archive source? | no (needs archive) |
| B | `tests/test_loadmaze_replay.py` | does `loadMaze` reproduce every invariant the corpus pins? | **yes** |
| C | `oracle/editor-visual/` | do the projector and Ruffle render the rebuilt SWF identically? | no (needs browser + projector) |
| C1 | `tests/test_cleaned.py` | are the cleaned captures exactly the sha256-locked manifest? | no (needs archive) |
| D | `tests/test_no_unlabelled.py` | is every `srv/` file labelled, every `M*` file announced, no stub returning 200, no credential-shaped string? | no |
| E | `tests/test_subresources.py` | does every subresource the pages request resolve, or carry a `known-lost` row? | partly |
| F | `tests/test_render_diff.py` | does the served HTML byte-match every era capture, outside the annotated masks? | **yes** |
| S | `tests/test_seed.py` | do the seeded row counts match the corpora? | **yes** |

Plus the instruction-surface gates added 2026-08-08: `test_citations.py`,
`test_docs_single_source.py`, `test_progress_register.py`,
`test_foundations.py` — all offline.

**A, D and F all walk `srv/` → ledger. Only E walks page → subresource.** That
asymmetry is why a byte-perfect page serving no images once passed three gates
at once.

## The gate E asset loop

```bash
python tools/refgraph.py                    # the reference graph = the work list
python tools/resolve_assets.py              # verdict + evidence per defect
python tools/fetch_missing.py               # refetch what CDX proves existed
python tools/resolve_assets.py              # re-verdict with the new bytes
python tools/place_assets.py --promote      # copy, verify, append ledger rows
python -m pytest tests/ -q
```

## De-rendering

```bash
python tools/classify_regions.py                       # draft masks
python tools/annotate_regions.py --variants <route>    # every byte-form, dated
python -m pytest tests/test_render_diff.py -k <route>  # gate F for one route
python -m pytest tests/test_fenced_regions.py -q       # verbatim spans still match
```

`infirmary` is the harness smoke test: an `O` file with zero dynamic regions.

## Database

```bash
cd docker && docker compose down -v && docker compose up -d   # full reseed
```

Required after **any** schema or seed change. Then re-check `ROW_COUNTS`
(`architecture.md`). A stale volume serving old rows is the most common cause of
a confusing gate failure; the `stack` fixture hashes a known file at startup to
catch it early.

## Eyeballing a route

```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d   # ad filler ON
docker compose up -d --force-recreate php                              # back to default
```

The dev filler labels the two blank AdSense slots so a real hole is not mistaken
for an ad. It is off by default, lives outside `srv/`, and **gate F must run
against the default stack**.

## Editor toolchain

MTASC 1.14 compiles the AS2 sources:

```bash
thirdparty/mtasc/mtasc.exe -version 8 -header 688:400:25 ...
```

Harnesses under `oracle/` drive the SWF through Ruffle (puppeteer) and the
pinned Flash projector 32.0.0.465.

## Environment notes

* The Bash tool's working directory drifts — prefix commands with
  `cd /c/Users/eth/websites/TankTrouble`.
* Never write cp1252 bytes into tracked text files. Heredocs that write files
  must set UTF-8 explicitly.
* `docker/mysql/init/20-forum.sql` is 36 MB and already in history. Under
  GitHub's limits, but worth LFS if it grows.
