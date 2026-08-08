# Manual visual evidence — published analyses, not yet adopted

Thirteen analysis documents produced 2026-08-04 from 99 screen captures and 5
text notes the repo owner collected. Published here 2026-08-08 so the findings
are readable from a clone; **nothing in them has been applied to the
reconstruction yet.**

Start at [`INDEX.md`](./INDEX.md) — it carries the era partition, the
overlay-exclusion tests and the confidence-tag vocabulary that every other
document depends on. Read it before quoting any finding.

## What is here and what is not

| | Where | In git |
|---|---|---|
| The 13 analyses (~1 MB markdown) | this directory | yes |
| The 99 PNG/WEBP captures + 5 notes (~41 MB) | `../../../../manualevidence/` (outside the repo) | no |
| `TankTrouble.ttf` | same, outside the repo | no |

Image paths quoted inside the analyses (`UI/…`, `Game/…`) are relative to that
external folder. It is read-only: evidence is cited, never corrected.

## Status: intake, not adoption

Adoption is a separate deliberate act, tracked in
[`../../PROGRESS.md`](../../PROGRESS.md). Three reasons it has not happened:

1. **Provenance is incomplete.** Every claim is `M2` at best (frames *of* the
   site, not its bytes) and guide §6.5 requires URL, uploader, upload date and
   timestamp in the `LEDGER.tsv` row. None of that is recoverable from the
   crops — the source video URLs must be supplied first. Until then these
   documents cite pixels with no citable source.
2. **The corpus is at least five eras.** Most of it sits outside the 2017–2018
   target window, and some is post-classic HTML5 that must be actively kept
   out. `INDEX.md` §1 has the partition table.
3. **Several findings falsify pinned constants**, which under THE OVERHAUL RULE
   (`../../standards/VISUAL-EVIDENCE-WANTED.md`) means a wholesale rewrite of the affected
   piece, not a tweak. Those are registered as rows in
   [`../../FOUNDATIONS.md`](../../FOUNDATIONS.md) with their blast radius.

Procedure for turning any of this into code:
[`../../standards/UI-RECONSTRUCTION.md`](../../standards/UI-RECONSTRUCTION.md), or the
`adopt-visual-evidence` skill.

## Do not

* Do not promote a confidence tag when quoting (`[INFERRED]` never becomes
  `[MEASURED]`).
* Do not treat a video author's overlay as site UI — `INDEX.md` §5 lists the
  known ones and the tests that separate them from TankTrouble's own
  hand-drawn style.
* Do not mix a finding's page-chrome era with its in-stage era. A 2013 page can
  carry the era `TankTrouble_v4.0.swf` inside the stage; in-stage measurements
  from such a frame are admissible, the chrome around them is not.
