# Visual evidence wanted

Standing request log. Rule: when a rebuild visual cannot be deduced with
enough accuracy from held evidence, or it is a vital user-facing interface,
an entry lands here with (a) what is needed, broadly, (b) specific
details/references to hunt for, (c) what it would replace or confirm.
Sources that work: YouTube footage from the active years (2010-2018 —
frame-step, crop; provenance **M2 at best, never O**), old screenshots,
community archives. Record video URL, uploader, upload date, and timestamp
in LEDGER.tsv for every asset derived this way (guide §6.5).

Status values: `WANTED` / `PARTIAL` (some states held) / `FETCHED` (evidence
in archive, redraw pending) / `DONE`.

---

## mazeCreator (phase 3 rebuild shipped from deduction — every entry below would upgrade it)

### 1. Tool icon states — PARTIAL, high value
Page-side JPGs, never captured: `images/mazeConstructTool{S,Des}elect.jpg`,
`images/crateSpawnTool{S,Des}elect.jpg`, `images/tankSpawnTool{S,Des}elect.jpg`
(srv/index.php:3732-3734). The screenshot
`archive/ia-items/extracted/images/Making a maze.png` holds 3 of 6 states:
wall=Deselect, crate=**Select**, tank=Deselect. Needed: the opposite three.
Video of someone CLICKING a tool gives the same icon in both states in
adjacent frames — ideal shot: any maze-editing footage where the toolbar is
visible while tools change.

### 2. Editor error panel — WANTED, vital user-facing
Known ONLY from `_root.errorPanel.hide` (srv/index.php:3706,3721). No
capture, no screenshot, no copy text. Phase 3 invented a dark rounded box +
copy ("Please give your maze a name." etc — DECISIONS 2026-08-03). Needed:
any frame showing the panel — likely triggers in footage: user hits the
green ✓ with an empty/duplicate name, or server rejects. Also wanted: the
exact wording, font, position, whether it animates.

### 3. Save flow / dialogue after ✓ — WANTED
What the SWF showed between "✓ clicked" and "tools hidden" (page evidence:
SWF calls `hideMazeCreatorToolsAndTitle` only on success). Spinner?
Instant? Confirmation flash? Any footage of a successful maze save.

### 4. Maze preview / garage mode — WANTED, vital user-facing
The SWF's boot state before editing (`previewLoaded` SetVariable, page
comment "display maze previews"). Phase 3 renders the saved maze +
click-anywhere-to-edit as a minimal stand-in. Needed: what the preview
actually looked like — multiple slots? thumbnails? "create new maze"
affordance? Any logged-in garage footage showing the maze panel BEFORE the
user starts editing.

### 5. Editing interaction semantics — WANTED, changes behavior not pixels
Phase 3 invented: click cell = toggle floor, click edge between floor
cells = toggle wall, click with spawn tool = toggle spawn. Unknown: did the
original drag-paint? preview walls on hover? show a cursor ghost? Footage
of someone actually drawing a maze answers all three in seconds.

### 6. Maze placement rule — PARTIAL
Screenshot shows the 13×8 maze centered with HALF-cell precision
(bbox left 137.2 stage px = lattice 56 + 2.5 cells). Phase 3 snaps to
integer cells so the editing lattice stays fixed. Footage of a maze
growing (cells added at the edge) reveals whether the original re-centered
live or kept a fixed lattice.

### 7. Title + watermark typography — PARTIAL
"Gauntlet" title (#666666, ~18px) and "version 0.3" watermark measured
from one upscaled screenshot; face unknown (rebuild uses `_sans`).
A cleaner capture or any frame at native scale would pin the actual font
(era site chrome used Verdana/Arial family).

### 8. Fade transitions — PARTIAL
15 frames @ 25fps is O evidence (srv/index.php:3637 comment). Unknown:
linear alpha vs eased. Any open/close footage of the maze creator panel.

## Older / other routes

### 9. Tank paint editor icon states — WANTED (same JPG family, phase 4+)
`images/userpanel*Paint*.jpg` states referenced by the paint flow; same
video-frame technique applies when that milestone opens.

---

*Add new entries at the bottom of the relevant section. When evidence
arrives: archive it under `archive/` (read-only discipline), add the
LEDGER row (M2, with URL/uploader/date/timestamp), flip the status here,
and note the superseded invention in DECISIONS.md.*
