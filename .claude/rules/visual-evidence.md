---
paths:
  - "src/mazecreator/**"
  - "oracle/**"
  - "docs/*visual*"
  - "docs/UI-*"
  - "docs/evidence/**"
---

# Building pixels from image evidence

This is where invention is easiest and hardest to detect: a screenshot always
looks like proof. Full procedure in `docs/standards/UI-RECONSTRUCTION.md`; these are the
rules that hold for any file that renders something.

## Ceiling and citation

Image-derived work is **`M2` at best, never `O`** — a frame is *of* the site, not
its bytes. Guide §6.5 requires the LEDGER row to carry the source URL, uploader,
upload date and timestamp. **If you cannot cite the source, you cannot place the
asset**; the finding stays in `docs/standards/VISUAL-EVIDENCE-WANTED.md` until the citation
exists.

## Confidence tags are load-bearing

`[OBSERVED]` (point at it) · `[MEASURED]` (a number a script printed) ·
`[INFERRED]` (a reasoned step, **with its falsifier**) · `[UNCERTAIN]` (deniable
at this resolution) · `[NOT VISIBLE]` (absent — which keeps the want-list honest).

Never promote a tag when quoting a finding. An `[INFERRED]` claim carried into
code as if measured is how a wrong constant becomes a foundation.

## Before measuring

* **Derive the scale and show the derivation.** Assumed scale factors produced
  the bogus per-axis 1.209/1.390 numbers in guide §6.5; the real capture scale is
  uniform, provable because cell pitch matches on both axes.
* **Date the frame, twice.** The available corpus spans ~2013 to post-classic
  HTML5. Independent dating signals: footer copyright year, monotonic Scrapyard
  and Visits counters, nav tab count, in-stage `version` watermark.
* **Page chrome and stage content date separately.** A 2013 page can carry the
  era `TankTrouble_v4.0.swf` inside its stage; in-stage measurements from that
  frame are admissible, the chrome around them is not. State which layer a
  finding came from.
* **Exclude what the video author drew.** Comic bubbles, caption tracks, title
  cards, recorder click-halos, player chrome, PiP toggles. Record them only where
  they *occlude*, because that bounds what can be read. The converse trap is
  real: TankTrouble's own UI is hand-drawn and skewed, so "it looks like an
  annotation" is not a test. The tests that work: does it recur across unrelated
  sessions; does page content read *through* it; does it carry live state (a
  caret, a server-composed prefix); does its type ramp match the page's chrome.

## Turning measurements into code

* Measured constants live in **one** module, consumed verbatim — `MazeRenderer`'s
  statics come from `docs/standards/MAZECREATOR-VISUAL-SPEC.md` and nowhere else. Two
  copies of a constant guarantee an eventual disagreement.
* Anything not forced by the evidence is an **invention with a seam**: a named
  function or constant that can be replaced whole. Record it in
  `docs/FOUNDATIONS.md` with its falsifier and its dependents, and in
  `DECISIONS.md` as a choice.
* Where the original's rule is unknowable but something must be chosen, prefer a
  **deterministic** stand-in over randomness so the pixel oracle stays stable
  (the floor-tone hash is the worked example), and log it as a divergence.

## When new evidence arrives

THE OVERHAUL RULE: rewrite the affected piece **fully** against the evidence. Do
not patch the invention to be "close enough" — it has zero authority and exists
only so the site runs end to end. Archive the evidence first, add the LEDGER row
with full citation, overhaul, then record the supersession in `DECISIONS.md`
(what the invention was, what the evidence showed, what changed). Byte-level
gates — round-trip, replay, contract — stay green throughout: evidence changes
pixels and behaviour, never the wire format.
