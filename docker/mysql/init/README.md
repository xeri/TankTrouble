# mysql/init

Executed in filename order by the mysql:5.5 entrypoint on first start.

| File | Data / schema tier | Source |
|---|---|---|
| `00-schema.sql` | schema: shape M1, names+types M3 | hand-authored; choices in DECISIONS.md |
| `10-mazes.sql` | data O | `seed/seed_mazes.py` ← archive/maze-corpus/raw/ |
| `20-forum.sql` | data O | `seed/seed_forum.py` ← archive/forum-archive/ |
| `30-news.sql` | data O (verbatim blobs) | `seed/seed_news.py` ← captured ?news bodies |
| `40-users.sql` | M3 (synthetic) | `seed/seed_users.py` |
| `50-static.sql` | M2 (debug catalogue, observed ids) | `seed/seed_static.py` |

Generated files are byte-reproducible from the archive (`tests/test_seed.py`);
regenerate with the named script, never hand-edit. No docker runtime has
executed these yet — see the milestone-2 entry in DECISIONS.md.
