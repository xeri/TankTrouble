# How to think here

The original server is gone. Nothing in `srv/` may rest on "it probably worked
like this." This file is the reasoning toolkit; `DEDUCE.md` is the full record of
how each existing claim was reached.

## Evidence grades

| Grade | Means |
|---|---|
| **A** | Directly observed — a 200 response, a decompiled function, an archived payload |
| **B** | Observed indirectly but unambiguously — a 403 proves a path existed and was protected |
| **C** | The **name** or **shape** is proven, the content is not — a 404, a call site with no response body |
| **D** | Wrong era or wrong site — says nothing about the target |
| **X** | Artefact. Looks like evidence, is not |

Grades map onto tiers: A → `O`/`M1`, B/C → `M2`, nothing → `M3`.

## Seven techniques that produced almost everything here

1. **Find the counterpart of the lost thing.** The writer is gone; its reader
   survives and fully specifies what the writer emitted.
2. **Corpus statistics reveal enforced limits.** What thousands of users never
   did is what the tool forbade.
3. **Machine-generated output inverts exactly.** Library-emitted stubs and
   bundle names enumerate their own inputs; run them backwards.
4. **Diff across time separates constant from variable.** Bytes identical across
   captures spanning a decade are literal text; bytes that vary are echoed.
5. **First and last appearance date a feature**, often to the exact day, and two
   independent sources landing on the same day is strong corroboration.
6. **Error messages leak schema.** Validation errors report expected parameter
   counts and types.
7. **Siblings predict the lost thing.** A held artefact sharing author, era and
   embed convention bounds the design space of the missing one.

## Rules that stop deduction becoming invention

**Absence of evidence needs a mechanism.** Until you can say *why* something is
absent, absence means nothing. A file that appears nowhere in CDX — not even a
404 — can still be provably real if nothing ever linked it.

**A refusal is not a negative.** A CDX prefix quirk, a rate-limit 403 and an
empty large-domain scan all look exactly like zero results. Always record "asked
and got nothing" separately from "never successfully asked."

**Corroboration must be independent.** Two sources derived from the same capture
are one source. Someone who says they never read the code is not a second source
on the code.

**sha256 of the decoded payload is the only identity.** CDX `digest` over-splits
(same payload, different gzip); CDX `length` is record size, not payload size.

**Size is never integrity.** A ~151 KB HTML error page passes any "bigger than
N" check. Validate magic bytes. This bug landed three separate times.

**A stub that returns plausible data is the most dangerous thing in this
project.** Reject rather than fake.

## What each source can and cannot tell you

| Source | Strong for | Blind to |
|---|---|---|
| Wayback CDX index | which paths existed, when, with what status | anything never linked |
| Wayback content | logged-out HTML, CSS, JS, binaries | anything behind login |
| Common Crawl | the same, plus unrewritten bodies and other hosts | the same login gap |
| Decompiled SWFs | client logic, wire formats, constants, endpoint names | server internals |
| Archived API responses | exact response bytes | handling of bad input |
| SAJAX stubs in HTML | the server's exported RPC surface, with dates | function bodies |
| Wikis | screenshots of logged-in UI | accuracy — user-written |
| Video | logged-in UI *in motion*, i.e. state transitions | exact pixels — lossy, rescaled |
| Distribution zips | client bundles as shipped | server code — all four were client-only |

**Nothing above can ever yield server-side PHP source.** A web server emits
output, never source. That is a property of HTTP, not a gap in coverage.

## Symptom → first suspect

| Symptom | Look here first |
|---|---|
| Gate A or C1 fails on every row | the `archive/` junction is missing, or `TT_ARCHIVE_ROOT` is unset |
| Gate B or F fails immediately, everything else green | the stack is down, or serving a stale volume — `docker compose down -v && up -d` |
| Row counts wrong after a seed change | stale MySQL volume; the seed did not re-run |
| Page renders unstyled with broken images | gate E — run `tools/refgraph.py`. Do not copy a plausible file into place |
| An asset 404s in the container but works locally | case sensitivity: Windows folds case, `php:5.6` does not |
| A reference "does not resolve" but the path was live | you resolved it script-relative; browsers resolve against the **document** |
| Gate F fails on one capture out of many | a `template-edit` window, or an unannotated region — check the mask before the PHP |
| Gate F passes only after the mask grew | the reconstruction is drifting. That is a defect, not a fix |
| A promotion looks obvious | check the digest is **in-era** and the match is not just a basename |
| Numbers on screen never change | may be correct — several regions are deliberately frozen; check `docs/standards/DIVERGENCES-SERVED.md` before "fixing" |

## Escalate — stop and ask a human

* changing a wire format, or any schema key of a seeded table
* anything touching authentication
* deleting a `LEDGER.tsv` row, rather than superseding it
* publishing evidence outside the repo
* overturning a `docs/FOUNDATIONS.md` row that still has dependents
* accepting an out-of-era digest match to close a gap

## Evidence standards for your own claims

"Should work now" is not a result. State the named test, the log line, or the
reproduction that proves it — and run it in the session where you claim it, not
from memory. Silence is not success: a gate that did not run has not passed.
