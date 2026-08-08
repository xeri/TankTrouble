---
paths:
  - "srv/**/*.php"
  - "srv/**/*.html"
---

# Reconstructed PHP

The original server's source is unrecoverable — a web server emits output, never
source, confirmed by four independent negatives (`DEDUCE.md` Part 1). So PHP here
is never "written from scratch": it is **inverted from captured output**, or it
is invention that says so.

## De-render, do not author

The route order and the whole procedure live in the `derender-route` skill and
`docs/REBUILD-GUIDE.md` §6.1a. The short form:

1. Diff era captures of the route pairwise. Identical bytes are literal text;
   varying bytes are echoed values (`DEDUCE.md` §0.2 technique 4).
2. Every varying region is classified and **annotated** with the variable or
   loop that produces it. An unannotated region blocks gate F for that route —
   an unexplained region is an ununderstood region.
3. Verbatim spans go inside `@O-begin` / `@O-end` fences, not retyped.
4. Gate F byte-diffs the render against every era capture. A mask that **grows**
   to make the gate pass is the reconstruction drifting; treat it as a defect.

## Structure

* **No new files under `srv/`.** Any new path is fetchable and therefore an
  evidence claim. Shared logic lives as in-file functions in `srv/index.php`.
* Single-file `index.php` with the six `?query` routes — no per-route includes.
* Invented helpers live in `srv/includes/rebuild-db.php`, whose obviously-modern
  name is the point. There is one invented file, not several.

## Unobservable behaviour

Most of what a backend does was never archived: response headers, `Content-Type`,
trailing newlines, error bodies for malformed input, selection mechanism, case
and padding semantics. For each one:

1. Choose the **least inventive** option — mirror a convention already proven
   elsewhere in the corpus before inventing a new one.
2. Say so in `@caveat`, naming what is unobservable and what you picked.
3. Register it in `docs/standards/BACKEND-CONTRACTS.md`.

Never emit a plausible value silently. Reject rather than fake: unknown input
dies with a loud `RECONSTRUCTION:` message and a real status code, and
unimplemented SAJAX functions return the stock library error, not an invented
body.

## Stubs

An unverified endpoint returns `HTTP/1.1 501 Not Implemented`, contains `STUB`,
and dies. `tests/test_no_unlabelled.py::test_stubs_never_200` enforces it. The
501 lifts only when `verified_by` names a real replay or contract test, added in
the same commit.

## Period-correct without period-vulnerable

* PHP 5.6, `mysql_*`, no PDO — fidelity. Still escape everything: an injection
  here corrupts the seeded archive, which is the data being preserved.
* The stack is localhost-only and must never be internet-facing (`SECURITY.md`).
* **Auth is the one deliberate divergence.** The original ran SAJAX auth over
  GET, which is why real credentials sit in the public CDX index forever. This
  rebuild uses POST + `password_hash` and says so in the file header
  (guide §6.4, `tests/test_auth_divergence.py`). Never reintroduce a leaked
  credential, and never make any other endpoint "more secure" without an entry
  in `docs/standards/DIVERGENCES-SERVED.md`.

## Faults are features

Duplicated version strings across four files with no shared constant;
`infirmary/index.html` as a hand-copied simplification rather than a template.
Reproducing these is more faithful than fixing them. Tidying one is a
divergence and needs an entry before it ships.
