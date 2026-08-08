<!-- One target. The SessionStart hook prints the section below into every
     session, so keep it short enough to be read in full. Everything else
     belongs in PROGRESS.md (tracked work) or BACKLOG.md (ideas). -->

# Now

## Target

**P-11 — unblock the manualevidence adoption.** It gates four other rows.

Definition of done: every analysis in `docs/evidence/manual-evidence/` either
carries a citable source (URL, uploader, upload date, in-video timestamp) or is
explicitly marked uncitable, and `docs/PROGRESS.md` P-11 moves off `blocked`.

Gate: none yet — this is evidence work. Inspect `docs/evidence/manual-evidence/README.md`.

Next three steps:
1. Ask the repo owner for the source video URLs. Nothing else in P-11 can start.
2. For each supplied URL, archive it read-only and record uploader + date.
3. Re-run `adopt-visual-evidence` step 1 per document; mark the rest uncitable.

Not now: P-12, P-13 (overhauls) — they depend on this. P-15 (garage) — do not
start before this; the layout evidence exists but is uncited.

---

## How to use this file

Replace the **Target** section when the target changes; do not accumulate
history here. One target at a time, and it is always a row in
`docs/PROGRESS.md`.

The target is a commitment about *what*, not a licence to skip the invariants.
It exists so a session opens by doing the work rather than by re-deriving what
the work is.

Something that is not the target and not a two-minute fix goes in
`docs/BACKLOG.md` and the session carries on. Noticing is cheap; detouring is
not.
