---
name: adopt-visual-evidence
description: Use when a screenshot, video frame, wiki image or community capture is about to inform the rebuild — measuring UI geometry, redrawing an asset, changing an interaction model, or acting on anything in docs/evidence/manual-evidence or VISUAL-EVIDENCE-WANTED.
---

# Adopt visual evidence

A screenshot always looks like proof. This procedure is what separates a
measurement from a guess, and it is what makes THE OVERHAUL RULE affordable.

## 1. Admissibility — before measuring anything

- [ ] **Citation exists.** Source URL, uploader, upload date, timestamp within
      the video (guide §6.5). No citation → the finding stays in
      `docs/standards/VISUAL-EVIDENCE-WANTED.md`; it does not become a LEDGER row.
- [ ] **Archive the source first**, read-only, then cite the archived copy.
- [ ] **Date the frame from inside the frame.** File mtimes are save times, not
      frame times. Use footer copyright year, monotonic Scrapyard / Visits
      counters, nav tab count, in-stage `version` watermark — and corroborate
      with a second signal.
- [ ] **Reject out-of-era generations**, and say so. Post-classic HTML5 material
      must be actively kept out; pre-era material is admissible only as *change*
      evidence, never as era look.
- [ ] **Separate the layers.** Page chrome and stage content date independently.
      In-stage measurements from an out-of-era page can still be admissible.
      State which layer the finding came from.
- [ ] **Identify the video author's own drawings** — comic bubbles, captions,
      title cards, recorder click-halos, player chrome, PiP toggles — and exclude
      them. Record them only where they occlude, because that bounds what is
      readable. Do not use "it looks hand-drawn" as the test: the site's real UI
      is hand-drawn too. Use recurrence across unrelated sessions, whether page
      content reads *through* it, live state (a caret, a server-composed prefix),
      and whether the type ramp matches the page's chrome.

## 2. Measure

- [ ] **Derive the scale and show the derivation.** Never assume it. Cross-check
      on both axes — matching pitch proves uniformity; a mismatch usually means
      page chrome was included in the denominator.
- [ ] Prefer the frame with the best **colour fidelity**, not the biggest one. A
      known constant sampled off by 35 levels means that frame cannot be trusted
      for colour even if it is larger.
- [ ] Tag every claim: `[OBSERVED]` `[MEASURED]` `[INFERRED]` `[UNCERTAIN]`
      `[NOT VISIBLE]`. Every `[INFERRED]` carries its falsifier. Never promote a
      tag when quoting.
- [ ] Record `[NOT VISIBLE]` explicitly — it is what keeps the want-list honest.

## 3. Compare against what is already pinned

- [ ] Diff the findings against `docs/FOUNDATIONS.md` and any pinned constants
      (`docs/standards/MAZECREATOR-VISUAL-SPEC.md` and friends).
- [ ] **Agreement** → strengthen the row: raise the grade, cite the new source.
- [ ] **Contradiction** → open an OVERHAUL item in `docs/PROGRESS.md` naming the
      falsified row and its blast radius. Do not start editing yet.

## 4. Overhaul, do not patch

When evidence overturns an invention, replace the affected piece **wholesale**.
The invented version has zero authority; it existed only so the site ran end to
end. This applies to whole files, not just constants — an `M2` SWF whose real
appearance surfaces gets rebuilt against the footage, not tweaked.

- [ ] Update the single seam that owns the constant, and let its consumers
      follow. If the value is written in two places, fix that first.
- [ ] Re-pin the tests to the evidence.
- [ ] Byte-level gates — round-trip, replay, contract — must stay green
      throughout. Evidence changes pixels and behaviour, never the wire format.
      If a wire gate goes red, stop: you have changed the wrong layer.
- [ ] Re-run the pixel oracle (gate C) and record the new baseline.

## 5. Land it

- [ ] `LEDGER.tsv` row with the full citation; tier `M2` at best, never `O`.
- [ ] `DECISIONS.md` supersession: what the invention was, what the evidence
      showed, what changed.
- [ ] `docs/FOUNDATIONS.md` row updated — new grade, new falsifier, dependents
      re-checked.
- [ ] `docs/standards/VISUAL-EVIDENCE-WANTED.md` entry moved to `DONE`, or narrowed to
      what is still missing.
- [ ] Anything still chosen rather than observed → `docs/standards/DIVERGENCES-SERVED.md`
      or `oracle/DIVERGENCES.md`.

## Current backlog

`docs/evidence/manual-evidence/` holds 13 published analyses that are **not yet
adopted**, several of which falsify pinned constants. Their blocking issue is
step 1: the source video URLs have never been supplied. Start there.
