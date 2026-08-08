# Reconstructing UI from images

Most of what a 2018 visitor saw was behind a login, and almost none of it was
archived. The evidence that remains is screenshots, wiki images and YouTube
footage — material that **looks** like proof and is the easiest thing in this
project to over-trust.

This is the pipeline from a frame to a shipped pixel. The step-by-step checklist
is the `adopt-visual-evidence` skill; this file is why each step exists.

## The bottleneck is the frontend, not the backend

Backend contracts are in good shape: endpoint names, wire formats, response
grammars, a schema by inference. What is thin is **pages**. A handful of archived
renderings, all logged out. The garage — the page that matters most — was never
captured with a session.

So the risk profile inverts. On the backend the danger is a quiet invention
nobody can see. On the frontend the danger is a *confident* invention everybody
can see, built on a frame that was measured wrong, dated wrong, or drawn on by a
video author.

## 1. Provenance ceiling: `M2`, never `O`

A frame is *of* the site, not its bytes. Guide §6.5 requires the LEDGER row to
carry the source URL, uploader, upload date and timestamp within the video.

**No citation, no placement.** The finding stays in
`docs/standards/VISUAL-EVIDENCE-WANTED.md` until the source can be named. This is the
current blocker on the whole `docs/evidence/manual-evidence/` set: the analyses
are rigorous, and their sources have never been supplied.

## 2. Date the frame from inside the frame

File modification times are save times, not frame times. Independent in-frame
signals: footer copyright year, the monotonic Scrapyard and Visits counters, nav
tab count, ad creative, the in-stage `version` watermark. Use at least two.

The available corpus spans roughly 2013 to post-classic HTML5, and **most of it
is outside the target window**:

| Generation | Admissible? |
|---|---|
| Pre-era (older nav, older version watermark) | only as *change* evidence — never as era look |
| The target window | yes |
| Post-classic HTML5 / "Online BETA" | **no — actively keep it out** |

**Page chrome and stage content date separately.** A pre-era page can carry the
era SWF inside its stage, so in-stage measurements from that frame are admissible
even when the chrome around them is not. Always state which layer a finding came
from.

## 3. Separate the site's UI from the video author's drawings

Known overlays: comic speech bubbles, caption and subtitle tracks, burned-in
title cards, recorder click-halos, player chrome and timecodes, browser toasts,
picture-in-picture toggles, thumbnail art. None of it carries evidential weight.
Record an overlay only where it **occludes** something, because that bounds what
can be read.

The converse trap is just as real: TankTrouble's own UI is drawn in a hand-made,
slightly skewed paper style that looks exactly like an annotation. "It looks
hand-drawn" is not a test. The tests that work:

* does it appear in more than one unrelated session?
* does page content read *through* it?
* does it carry live state — a text caret, a server-composed prefix?
* does its type ramp match the page's own chrome?

## 4. Derive the scale, and show the derivation

Never assume a scale factor. Cross-check both axes: matching pitch proves the
scale is uniform. A mismatch usually means page chrome was included in the
denominator — that is exactly how guide §6.5's bogus per-axis factors arose.

Prefer the frame with the best **colour fidelity**, not the largest one. Sample a
constant you already know: if it reads tens of levels off, that frame cannot be
trusted for colour no matter how many pixels it has.

## 5. Tag every claim

`[OBSERVED]` — point at it · `[MEASURED]` — a number a script printed ·
`[INFERRED]` — a reasoned step, **with its falsifier** · `[UNCERTAIN]` — deniable
at this resolution · `[NOT VISIBLE]` — absent, which is what keeps the want-list
honest.

**Never promote a tag when quoting.** An `[INFERRED]` claim carried into code as
if measured is precisely how a wrong constant becomes a foundation nobody
questions.

## 6. Turning measurements into code

* Every measured constant lives in **one** module and is consumed verbatim.
* Anything the evidence does not force is an invention behind a **seam** — a
  named function or constant replaceable whole.
* Register the structure in `docs/FOUNDATIONS.md`: grade, falsifier, dependents,
  blast radius, seam. If the falsifier is cheap to test, **test it before
  building on the guess.**
* Where the original's rule is unknowable but something must be chosen, prefer a
  deterministic stand-in over randomness so the pixel oracle stays stable, and
  log it as a divergence.
* Gate C is the proof: projector and Ruffle must render identically.

## 7. When better evidence arrives

THE OVERHAUL RULE. Rewrite the affected piece **fully** against the evidence —
whole files, not just constants. The invention has zero authority; it existed
only so the site ran end to end. Archive the evidence, add the cited LEDGER row,
overhaul, then record the supersession in `DECISIONS.md`.

Byte-level gates stay green throughout. Evidence changes pixels and behaviour,
never the wire format — **if a wire gate goes red during an overhaul, stop: you
have changed the wrong layer.**

## Gather evidence before you build

The want-list exists because gathering evidence *before* a rebuild starts beats
overhauling after. When a visual cannot be deduced with enough accuracy from held
evidence — or it is a vital user-facing interface — it gets an entry with what is
needed, what to hunt for, and what it would replace.

Footage answers questions that no amount of reasoning can: whether a tool
drag-paints, whether a lattice re-centres, whether a floor pattern is
deterministic. Two of those have already overturned shipped work (F-08, F-09).
That is the cost of building first.
