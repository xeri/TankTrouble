---
paths:
  - "tools/**/*.py"
  - "seed/**/*.py"
  - "tests/**/*.py"
---

# Python tooling and gates

These scripts decide what counts as evidence. A bug here does not crash — it
quietly launders a guess into the ledger.

## Gates fail, they never skip

`pytest.fail`, never `pytest.skip`, never a silent pass. A skipped gate A is a
green lie. The two fixtures that model this are `archive_root` and `stack` in
`tests/conftest.py`: each fails with the exact command needed to fix it.
Deliberate offline runs must say so on the command line (`-m "not live"`).

Failure messages are part of the gate. Name the file, the expected value, the
observed value, and the command that repairs the state (`docker compose down -v`,
create the junction, re-run `place_assets.py`).

## Evidence handling

* **Verify before accepting.** A fetched payload is kept only if
  `base32(SHA1(payload))` equals the digest the CDX row named. No digest, no
  placement.
* **Size is never integrity.** Wayback returns a ~151 KB HTML error page on
  failure, which passes any "bigger than N" check. Validate magic bytes. This
  bug landed three separate times.
* **sha256 of the decoded payload is the only identity.** CDX `digest`
  over-splits (same payload, different gzip); CDX `length` is record size, not
  payload size.
* **Copy, never move.** The archive is read-only. `place_assets.py` copies and
  re-verifies sha256 on arrival.
* **Record "asked and got nothing" separately from "never successfully asked."**
  A refusal is not a negative — a CDX prefix quirk, a WAF 403 and an empty
  large-domain scan all look exactly like zero results. One Common Crawl pass
  recorded 1,148 of 1,260 jobs as zero-row results that were never actually run.

## Determinism

Tool output is committed and reviewed, so it must be reproducible: sort every
collection before writing, no wall-clock or randomness in output, one row per
subject, evidence in a `notes` column. Rerunning a tool on unchanged inputs must
produce a zero-byte diff.

`tools/refgraph.py` is the single definition of "referenced" — gate E and
`resolve_assets.py` both import it so they cannot disagree. Resolve URLs the way
a browser does, against the **document**, not the way a path looks: a
script-relative reading of one `images/…` string filed a live asset as
`known-lost` for weeks.

## Seeds

Seeds regenerate deterministically from the archive corpus into init SQL. When a
seed's assumption is violated (an unexpected character, a duplicate key), it
**fails loudly** rather than normalising — the encoding question must reopen, not
be silently mangled. Row counts are asserted in `tests/test_seed.py`; a schema or
seed change means `docker compose down -v && up -d` and re-checking them.

## Test naming

One assertion subject per test, named for the property, not the mechanism:
`test_every_referenced_subresource_resolves`, `test_known_lost_rows_have_no_file`.
Live tests carry `pytestmark = pytest.mark.live`.
