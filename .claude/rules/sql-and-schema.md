---
paths:
  - "docker/**"
  - "seed/**"
  - "**/*.sql"
---

# Schema, seeds and the stack

The database is reconstructed from wire evidence, not from a dump. Nothing here
was ever archived directly, so every column is an inference with a grade.

## Tier the parts separately

A table is not one claim. Grade them apart, the way `DECISIONS.md` already does:

* **Column set** — usually `M1`: the client's queries and response grammars name
  the fields.
* **Keys** — usually `M2`: deduced from what the client looks a row up by.
* **Types, engine, collation** — `M3`: period-plausible, never observed. MyISAM
  and utf8mb3/`utf8_general_ci` were chosen for the site's 2008 birth era and a
  corpus scan showing 44,739 BMP non-ASCII characters and zero astral ones.

Record which is which in `docs/FOUNDATIONS.md`. A schema is the most expensive
thing to change late, so it gets a falsifier like everything else.

## Comparison semantics are evidence too

`mazes.author` is `VARBINARY(16)`, not `VARCHAR`: MySQL `VARCHAR` primary keys
compare PAD-SPACE, and `utf8_general_ci` compares case-insensitively, so 12
byte-distinct authors in the corpus collapse into 6. Merging them would invent
identity and silently drop observed states. **When a storage choice can erase an
observation, the storage choice is wrong.** Check for collisions before picking a
key type.

## Seeds

* Importers under `seed/` turn archive corpora into deterministic init SQL. Same
  inputs, same bytes out.
* Losing data must be loud. When an assumption breaks — an unexpected character,
  a duplicate key, a field that was supposed to be raw — **fail**, do not
  normalise. A silent `unquote_plus` is how an encoding question disappears.
* Arbitrary values (a frozen counter, a synthetic user) are labelled `ARBITRARY`
  in the SQL with the archived source they came from.
* Superseded captures survive as trailer comments (`-- superseded:`,
  `-- witness:`), so the row's provenance is readable from the SQL alone.
* **Synthetic users only** (`testuser01…`). Real usernames from the maze and
  forum corpora are display metadata, never login accounts. No real credential
  ever enters this repo.

## After any schema or seed change

```bash
cd docker && docker compose down -v && docker compose up -d
```

Then re-assert the row counts in `tests/test_seed.py`. A stale volume serving
old rows is the single most common cause of a confusing gate failure — the
`stack` fixture checks a known hash on startup precisely to catch it.

## The stack

`127.0.0.1` only, no published MySQL port, credentials reach PHP through
`TT_DB_*` container environment from an uncommitted `docker/.env`. Do not change
any of those (`SECURITY.md`). The dev filler overlay is opt-in, lives outside
`srv/`, and gate F must be run against the default stack.
