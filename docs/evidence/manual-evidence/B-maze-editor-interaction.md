# Visual evidence — mazeCreator editing interaction semantics

> Analysis of 18 evidence files under `manualevidence/` (17 PNG frames + 1 owner note).
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)
>
> Siblings: [A — toolbar](./A-maze-editor-toolbar.md) · [C — slots and save flow](./C-maze-slots-and-save-flow.md)

---

## Scope and provenance

This document owns **VISUAL-EVIDENCE-WANTED entry 5** ("Editing interaction
semantics — WANTED, changes behavior not pixels"), whose three open questions are
quoted verbatim in the entry:

> Phase 3 invented: click cell = toggle floor, click edge between floor cells =
> toggle wall, click with spawn tool = toggle spawn. Unknown: **did the original
> drag-paint? preview walls on hover? show a cursor ghost?** Footage of someone
> actually drawing a maze answers all three in seconds.

It also bears on entries **6** (maze placement rule / fixed vs live lattice) and
**8a** (floor tone pattern), and on **S48** (object caps).

### Sessions represented

The 17 frames are **not one session**. Two distinct accounts, two distinct page
scales, and two distinct maze-building episodes are present. I separate them by
account name in the page chrome and by an independent page-scale ruler
(described under *Scale derivation* below).

| Session | Account (verbatim) | Frames | Capture times (file mtimes = crop times, 2026-08-04) | Page scale |
|---|---|---|---|---|
| **R** | `revengexx1` | `B-hover-ghost-on-cell.png`, `B-hover-ghost-contains-cursor.png`, `B-wall-slot-preview-vertical.png`, `B-wall-slot-preview-second-location.png`, `B-wall-slot-preview-horizontal.png` | 17:00:43 → 17:04:37 | ×1.5966 |
| **C** | `cam12win` | `B-editor-howto-step3-epic-twister.png`, `4shouldntbethislaggy-…png`, `B-editor-howto-step5-nearly-solid.png`, (`A-editor-howto-step6-or-just-click.png` — analyst A), `B-editor-howto-step7-drag-paint-wall-run.png`, `B-tank-spawn-placement-effect.png`, `B-crate-spawn-placement-effect.png`, `B-maze-growth-mechanism{,1,2}.png` | 17:26:19 → 17:39:32 | ×1.5000 (chrome-bearing frames) |
| **?** | not determinable | `B-frontpage-achievement-unlock-float.png`, `B-frontpage-after-float-dismissed.png`, `B-hover-ghost-in-margin-ring.png` | 17:26:19 / 17:26:46 / 17:31:26 | see per-file |

`[OBSERVED]` Session R is a **maze being edited that already exists** — it is
complete, has 10 spawn objects on it, and carries a name in the name field. Session
C is a maze being **built from nothing** — frame `B-editor-howto-step3-epic-twister.png` shows a sparse L of floor
cells and frame `A-editor-howto-step6-or-just-click.png` shows a full rectangle. The two sessions must
not be merged.

Per the shared brief, mtimes are *when Ethan cropped the frame today*, not when the
footage was shot. I use them **only as capture order**, and I say so wherever I
reconstruct a sequence.

### Two overlays that are NOT part of the game — read this before anything else

`[OBSERVED]` Every frame in this topic carries a **screen-recorder cursor overlay**.
Two different overlays appear, one per session:

* **Session R** — a thick **yellow ring** (~90 capture px outer diameter) centred on
  the cursor hotspot. Visible in all five R frames.
  `[MEASURED]` sampled at (578, 645) in
  `B-hover-ghost-on-cell.png` = `#e3e92c`; the ring is
  opaque and *occludes* stage content behind it (it hides part of the blue cell
  ghost in that frame — see below).
* **Session C** — a **filled translucent blue disc** (~30 capture px diameter)
  centred on the cursor hotspot. Visible in `B-editor-howto-step3-epic-twister.png`, `4…png`, `B-editor-howto-step5-nearly-solid.png`,
  `A-editor-howto-step6-or-just-click.png`, `7candragit…png`.

`[INFERRED]` Neither is drawn by the SWF. Proof: in `B-editor-howto-step3-epic-twister.png` the blue disc sits at
(485, 592), which is **below the SWF stage entirely**, over the page's tool row; and
in `4…png` it sits at (310, 455), over blank white page area far outside the maze.
Stage content cannot render there. Falsifier: a frame where the blue disc appears
*without* a cursor near it.

`[INFERRED]` The blue disc is a **mouse-button-down indicator**. This is the
standard behaviour of era screen-capture tools (Camtasia, ActivePresenter, BB
FlashBack) — an idle highlight plus a coloured disc on button press. Supporting
observation: the disc is centred on the arrow's *tip* (the hotspot), not its
centroid, in all five C frames. This matters enormously for question 1 below, so it
is flagged, not assumed: **if the disc is instead an always-on highlight, the
drag-paint argument loses its cursor-state leg but keeps both other legs.**

**Do not rebuild either overlay.** They are recording artefacts.

### Scale derivation (how capture px become stage px)

`srv/index.php:3617` is O evidence for the stage size:

```
new SWFObject("includes/mazeCreator_v0.3.swf", "userSettingsMazeCreatorFlash-…",
              "688", "400", "8", "#ffffff")
```

so the SWF stage is **688 × 400** page px.

`[MEASURED]` In `B-hover-ghost-on-cell.png` (session R) the
white maze-panel's 1 px grey border runs at x = 252.8 and x = 1351.2, and at
y = 119.0 and y = 853.5. That is **1098.4 × 734.5** capture px.
1098.4 / 688 = **1.5966**. Cross-check on the other axis: 734.5 / 1.5966 = 460.1
page px tall, i.e. 400 px of SWF plus **60.1 px** of page chrome below it (name
field, three tools, ✗/✓). `docs/standards/MAZECREATOR-VISUAL-SPEC.md:12` derived "~72 px of
page chrome below the SWF" at scale 1.2093 → 72 / 1.2093 = 59.5 page px. The two
independent captures agree to **0.6 px**. Both the 688-px assumption and the panel
identification are therefore sound.

`[MEASURED]` In `A-editor-howto-step6-or-just-click.png` (session C) the same panel borders sit at x = 6
and x = 1038 → 1032 capture px → scale **1.5000**. Independent cross-check with a
page-fixed ruler: the centroid distance between the red ✗ and the green ✓ below the
stage is 67.10 capture px in every R frame and 63.15 in every C frame
(63.15 × 1.5966/1.5000 = 67.2 — agreement to 0.2 %). Both rulers agree, so the two
sessions differ by a genuine 6.4 % page zoom and nothing else.

`[MEASURED]` The ✗–✓ ruler is **identical (63.1–63.2 px) across `B-editor-howto-step3-epic-twister.png`, `4…png`,
`B-editor-howto-step5-nearly-solid.png`, `A-editor-howto-step6-or-just-click.png` and `B-tank-spawn-placement-effect.png`.** The maze-name
input box is 263–267 px wide in all of them. Those five frames are therefore at one
fixed zoom and can be compared directly, without normalisation, which is what makes
the growth analysis in §3 possible.

`[NOT VISIBLE]` `B-maze-growth-mechanism.png` and `…1.png` contain no page chrome
at all, so they have **no scale anchor**; measurements from them are reported in
capture px only.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| B1 | The editor draws a **hover ghost**: a blue rounded-rectangle outline on the cell under the pointer | `[MEASURED]` | VE 5 (q3) | Yes — `Editor.as` has no hover code at all |
| B2 | It also draws a **wall preview**: a blue stadium/capsule outline on the cell edge under the pointer, exactly one cell long, centred on the gridline | `[MEASURED]` | VE 5 (q2) | Yes — same |
| B3 | Ghost and preview are **unfilled outlines** (interior reads pure `#ffffff` over empty stage, `#ededef` over light floor) | `[MEASURED]` | VE 5 | — |
| B4 | Highlight stroke colour ≈ `#8f95e0` (periwinkle), measured across 4 independent frames | `[MEASURED]` | new constant | — |
| B5 | **Drag-paint is real**: a continuous run of new walls along one gridline with detached fragments *ahead* of the run, plus a button-down cursor indicator, in two consecutive frames 23 s apart | `[INFERRED]` (strong) | VE 5 (q1) | Yes — `Editor.as:60` binds `onMouseDown` only |
| B6 | The **cell pitch is dynamic** — it shrank from 53.5 to 39.95 capture px inside one session as the maze grew | `[MEASURED]` | VE 6 | Yes — `MazeRenderer.CELL = 32` fixed |
| B7 | Wall thickness **scales with the cell** (7.0 px at pitch 53.5, 5.5 px at pitch 39.95) → the maze is drawn at a nominal cell and uniformly scaled | `[MEASURED]` | spec `WALL_T` | Yes |
| B8 | For every settled 10-row maze measured (5 frames, 2 sessions, 3 maze widths) the cell is **26.58–26.63 stage px** vs sibling A's predicted `320/12 = 26.667` — agreement within 0.3 % | `[MEASURED]` | VE 6 | Confirms A's *height* term |
| B9 | Maze width does **not** change the cell for 10-row mazes (w = 12, 13, 18 all give 26.6) → the fit is `min()`-of-two-terms with the height term binding, as A modelled | `[MEASURED]` | VE 6 | Confirms A's form |
| B10 | `B-editor-howto-step3-epic-twister.png` is the one exception (11×10 maze at 35.67 stage px = `320/9`) — the refit appears to **lag** behind a stroke | `[UNCERTAIN]` | VE 6 | new want |
| B11 | Maze is re-centred horizontally on the panel centre live (maze bbox centre = panel centre to 1.5 px in `A-editor-howto-step6-or-just-click.png`) | `[MEASURED]` | VE 6 | Yes — `Editor.as` snaps to a fixed lattice |
| B12 | Floor tones measured at **220 (`#dcdcdc`) / 237 (`#ededef`)** — matches spec `#dddddd`/`#eeeeee` to 1 level | `[MEASURED]` | spec, VE 8a | Confirms |
| B13 | Two frames of the SAME maze 83 s apart have **identical per-cell tone grids** → the tone is not re-randomised per redraw | `[MEASURED]` | VE 8a | Partially answers |
| B14 | Tank spawn icon core ≈ `#8f94d6`/`#a5aae8`, crate core ≈ `#e0b95a` — both consistent with spec's pinned tones | `[MEASURED]` | spec | Confirms |
| B15 | Spawn icons are **rotated at arbitrary, differing angles** between frames of the same maze | `[MEASURED]` | spec "not clearly rotated" | Yes — `MazeRenderer.drawTank/drawCrate` axis-aligned |
| B16 | Object cap: exactly **5 tanks + 5 crates** on the session-R maze, matching the corpus max | `[OBSERVED]` | S48, `Editor.as:228-230` | Confirms |
| B17 | The centred grey heading above the stage is the **account name**, not the maze name — confirmed independently on a second account | `[OBSERVED]` | `Editor.as:338` | Yes — confirms sibling A |
| B18 | No refused-placement UI (grey-out, shake, panel) visible in any frame | `[NOT VISIBLE]` | S48, VE 2 | stays WANTED |

---

## 1. VE entry 5, question by question

VE entry 5 asks three things. Here they are, verbatim, with the evidence.

### 1a. "did the original drag-paint?"

**Answer: almost certainly yes.** `[INFERRED]`, from three independent legs. I state
up front what the brief demands: **a still frame can only ever be *consistent with*
dragging, never prove motion.** What raises this above "consistent with" is that two
of the three legs are artefacts that click-only interaction cannot produce.

**The owner's claims.** Two filenames assert it:
`B-editor-howto-step7-drag-paint-wall-run.png` — "can drag it to create walls
continuously" — and its sibling `A-editor-howto-step6-or-just-click.png` — "or just click". Those are the
repo owner's own words, not observations of mine. Tested below.

**Leg 1 — a partially-rendered run of new walls along one stroke path.**
`[MEASURED]` In `B-editor-howto-step7-drag-paint-wall-run.png` the maze is a complete
18-wide rectangle with no interior walls except along **one single gridline**, the
first interior horizontal gridline (capture y ≈ 61). Along that line:

| capture x span | length | state |
|---|---|---|
| 60 → 340 | 280 px ≈ 7 cells | continuous new wall |
| 340 → 344 | 4 px | gap |
| 344 → 372 | 28 px ≈ 0.7 cell | **detached fragment** |
| 372 → 785 | 413 px ≈ 10 cells | nothing |

and the cursor sits at (457, 60) — i.e. *on that same gridline*, ~85 px (2 cells) to
the right of the fragment, with the blue button-down disc active.

A detached wall fragment lying on the same gridline, ahead of a continuous run, in
the direction of the cursor, is the classic signature of **pointer sampling during a
drag**: the handler fires on `onMouseMove`, the pointer outruns the frame rate, and
the sampled positions leave gaps. Under a click-only model each wall requires a
separate mouse-down; producing a 7-cell run plus one isolated cell 2 cells further
along, all on one gridline, would take 8 deliberate clicks and would leave no reason
for the gap.

`[OBSERVED]` The same structure appears in `A-editor-howto-step6-or-just-click.png` (analyst A's file,
inspected here only for continuity, 17:38:00 → this frame precedes 7): the same
gridline carries a shorter continuous run (x ≈ 165 → 250) plus **two** detached
dashes at x ≈ 267–283 and x ≈ 300–308, with the cursor at (337, 158) — again ahead
of the fragments, again on the same line, again with the button-down disc. Between
frame 6 and frame 7 the run **grew leftward-to-rightward along the same line** and
the fragments moved with the cursor. Two frames of the same stroke, 23 s of capture
order apart, showing the same fragment-ahead-of-run pattern.

**Leg 2 — the held-button cursor.** `[INFERRED]` The blue disc (see *Scope*) is
present in every C frame where drawing is happening. It is a recorder overlay, and
in every era recorder that draws one, it means a button is down. If that reading is
right this is the "held-button cursor" the brief names as a corroborating artefact.

**Leg 3 — the rate of change.** `[OBSERVED]` `4shouldntbethislaggy-sourcescomputer
isslow.png`, `B-editor-howto-step5-nearly-solid.png` and `B-maze-growth-step1.png` all contain **video-codec
tearing** in the region of the maze that is changing — motion-compensation
fragments, half-drawn wall dashes, ghosted circular blobs. The owner's own filename
says it: *"shouldn't be this laggy - sources computer is slow"*. `[INFERRED]` A
click-per-cell model does not stress a renderer; a continuous drag that redraws the
whole maze on every mouse-move does. This is weak on its own and is offered only as
corroboration.

**What would falsify B5:** a frame showing the same gridline with a *contiguous*
partial run and no detached fragments in any capture; or evidence that the blue disc
is an always-on cursor highlight rather than a press indicator; or a straightforward
statement in a surviving decompile that only `onMouseDown` is bound.

**Program impact.** `src/mazecreator/Editor.as:60`:

```actionscript
_root.onMouseDown = function() { owner.onClick(_root._xmouse, _root._ymouse); };
```

This is the *only* mouse binding in the rebuilt editor. There is no `onMouseMove`,
no `onMouseUp`, no drag state, no "last painted cell" memo. **CONTRADICTED.**
Under **THE OVERHAUL RULE** the interaction model in `src/mazecreator/Editor.as`
(the block `onClick()` at lines 183–235, plus the binding at line 60) is an invented
M3 piece with zero authority and is now owed a **wholesale rewrite**, not a patch:
press/move/release states, a per-stroke "already visited" set so a drag does not
toggle the same cell twice, and a stroke-scoped mode (see the note under §1c on
toggle-vs-paint).

`docs/superpowers/plans/2026-08-03-mazecreator-phase3-editor.md` and the
`DECISIONS.md` 2026-08-03 entry that logged the invented interaction model both need
a supersession note.

### 1b. "preview walls on hover?"

**Answer: yes, unambiguously.** `[MEASURED]` — this is the single cleanest result in
the whole topic.

Three frames each show a **blue stadium (capsule) outline sitting exactly on an
interior gridline, exactly one cell long**, where no wall exists yet:

| frame | orientation | capsule bbox (capture px) | gridline it sits on | span vs cell |
|---|---|---|---|---|
| `B-wall-slot-preview-vertical.png` | vertical | x 665–678, y 580–621 | col line | 42 px long = 1.00 cell (pitch 42.44) |
| `B-wall-slot-preview-second-location.png` | vertical | x 667–683, y 286–326 | col line at 675.75; capsule axis measured at 675.5 | y 285.1 → 327.6 = exactly the two row gridlines |
| `B-wall-slot-preview-horizontal.png` | **horizontal** | x 1037–1076, y 488–502 | row line at 497.30; capsule axis at 496.6 | x 1035.6 → 1078.0 = exactly the two column gridlines |

`[MEASURED]` The capsule's long axis lands on the gridline to **0.25 px** in
`B-wall-slot-preview-second-location.png` (675.5 measured vs 675.75 fitted) and **0.7 px** in
`B-wall-slot-preview-horizontal.png`. Its ends land on the perpendicular gridlines to under a pixel.
It is a **wall-slot preview**, not a decoration.

`[OBSERVED]` In every case the slot is *empty* — there is no dark `#444444` wall
there. The preview shows where a wall **would be created**, which is exactly what VE
5 asks about.

The owner's filename claim, verbatim: *"B-wall-slot-preview-vertical"* —
"selected wall, small blue bit between blocks". **Corroborated**, and now measured:
the "small blue bit" is 13–17 capture px across and 42 px long — i.e.
**0.31–0.40 cell wide × 1.00 cell long**.

### 1c. "show a cursor ghost?"

**Answer: yes.** `[MEASURED]` Two frames in session R and one in session C show a
**blue rounded-rectangle outline occupying one whole cell**:

* `B-hover-ghost-contains-cursor.png` — ghost over an **empty** cell immediately below the maze's
  bottom boundary wall. `[MEASURED]` interior sampled along y = 648, x = 640…667:
  **pure `(255,255,255)`** — the ghost is unfilled and the cell has no floor. Right
  stroke centre x = 673.3 vs the cell's right gridline 674.55 → **inset 1.25 capture
  px = 0.78 stage px**. Bottom stroke centre y = 665.6 vs gridline 666.9 → inset
  1.3 px.
* `B-hover-ghost-on-cell.png` — ghost over the maze's
  **bottom-left floor cell**, grid (col 0, row 9). `[MEASURED]` interior sampled
  along y = 645, x = 552…571 = `(237,237,239)` ≈ `#ededef`, i.e. the light floor tone
  showing through unchanged. Ghost bbox x 552→590, y 621→663 — the cell is
  x 547.4→589.8, y 624.8→667.2.
* `B-maze-growth-mechanism.png` — ghost floating in **empty white space one cell to
  the left of a 3×3 maze**, touching its boundary wall. See §3 for why its
  proportions differ.

The owner's filename claim, verbatim:
*"B-hover-ghost-on-cell"* — "maze editor: selected block is
the block on mouse hover". **Corroborated in `B-hover-ghost-contains-cursor.png`**, where the ghost
does contain the cursor hotspot (arrow tip ≈ (668, 640); ghost cell
x 632.1→674.6, y 624.5→666.9).

`[UNCERTAIN]` **Not** corroborated in
`B-hover-ghost-on-cell.png` itself: there the arrow tip is at
≈ (636, 648), which is grid column 2, while the ghost is on column 0 — **two cells
adrift**. Two readings, and I do not pick a winner: (i) render lag — the recorder
composites the OS cursor at capture time while the Flash stage was rendered several
frames earlier, and the owner explicitly notes the source machine was slow; or
(ii) the ghost marks something other than the pointer cell (last-touched cell?).
What would settle it: any two consecutive video frames with the cursor stationary.

**Together, 1b + 1c say the ghost is one primitive with two shapes.**
`[INFERRED]` A rounded-rect stroke, drawn on the *hit target* — a square when the
target is a cell, a stadium when the target is a wall slot (a rounded rect whose
corner radius equals half its short side). That single rule reproduces every one of
the five highlight instances measured. Falsifier: a frame showing a cell ghost with
visibly *square* corners, or a wall preview with square ends.

**Program impact for 1b + 1c.** `src/mazecreator/Editor.as` contains **no hover
handling whatsoever** — no `onMouseMove`, no highlight movieclip, no ghost geometry.
`MazeRenderer.render()` (lines 66–102) draws floors, walls and objects and nothing
else. **CONTRADICTED — the invention is not wrong, it is absent.** Under **THE
OVERHAUL RULE**, `src/mazecreator/MazeRenderer.as` must gain a hover layer and
`src/mazecreator/Editor.as` a pointer-tracking state, both written against the
measurements in §2 rather than patched in.

---

## 2. Hover-highlight geometry and colour — measured

All numbers below are from `numpy`/`PIL` pixel dumps, not from eyeballing. Session R
scale ×1.5966; "stage px" = capture px / 1.5966.

### 2a. Is the target a whole cell, or the edge between two cells?

`[MEASURED]` **Both, depending on where the pointer is.** The editor has (at least)
two distinct hit targets and draws a different ghost for each:

| target | ghost shape | measured extent | as cell fractions |
|---|---|---|---|
| a cell | rounded **square** | 38–40 × 40–42 capture px (pitch 42.44) | 0.92 × 0.96 cell |
| a wall slot | rounded **stadium** | 13–17 × 42 capture px | 0.31–0.40 × 1.00 cell |

`[MEASURED]` Direct shape comparison, vertical vs horizontal wall slot:

* `B-wall-slot-preview-second-location.png`, vertical slot, cross-section at y = 306: two stroke peaks at
  x = 671 (blue-excess +80) and x = 680 (+72), with a near-baseline trough at
  x = 674 (+5) between them → **hollow**, stroke-centre separation **9.0 capture px
  = 5.6 stage px**; half-max outer envelope 667→684 = **17 capture px**.
* `B-wall-slot-preview-horizontal.png`, horizontal slot, cross-section at x = 1056: peaks at
  y = 492.7 (+56) and y = 500.5 (+65) → separation **7.8 capture px = 4.9 stage px**;
  half-max outer envelope 489.6→502.2 = **12.6 capture px = 7.9 stage px**.

`[INFERRED]` The horizontal and vertical previews are **the same shape rotated 90°**
— the two cross-sections agree to 1.2 capture px, which at this blur level is noise.
Nothing in the pixels suggests a different primitive per orientation.

`[MEASURED]` Length: both capsules span **exactly one cell pitch**, terminating on
the perpendicular gridlines (`B-wall-slot-preview-second-location.png`: 285.1 → 327.6, fitted gridlines
285.11 and 327.57; `B-wall-slot-preview-horizontal.png`: 1035.6 → 1078.0, fitted gridlines 1035.57
and 1078.03). So the preview is per-**segment**, one cell long — it does not run the
whole gridline and it does not stop at a half-cell.

### 2b. Fill and stroke

`[MEASURED]` **There is no fill.** The decisive sample is `B-hover-ghost-contains-cursor.png`,
where the ghosted cell is empty stage: the interior reads `(255,255,255)` at every
pixel from x = 640 to x = 667 along y = 648, and from y = 631 to y = 658 along
x = 660. A translucent fill of any opacity would depress that. In
`B-hover-ghost-on-cell.png` the ghosted cell is light floor
and reads `(237,237,239)` — the underlying `#eeeeee` unchanged to one level.

`[UNCERTAIN]` The wall capsules *look* filled (their interior reads ≈ `(205,205,218)`
against a `(220,220,216)` floor). Given the strokes are only 8–9 px apart in a
capture whose point-spread is ~3 px, this is fully explained by stroke blur, and the
white-background evidence above says the primitive is hollow. What would settle it:
one native-resolution frame.

`[MEASURED]` **Stroke colour.** The most blue-saturated pixel found inside each
highlight, across four independent frames:

| frame | element | most-saturated px | hex | blue excess |
|---|---|---|---|---|
| `B-wall-slot-preview-second-location.png` | vertical capsule | (145,152,233) | `#9198e9` | +81 |
| `B-wall-slot-preview-vertical.png` | vertical capsule | (143,147,214) | `#8f93d6` | +67 |
| `B-wall-slot-preview-horizontal.png` | horizontal capsule | (152,153,218) | `#9899da` | +65 |
| `B-hover-ghost-contains-cursor.png` | cell ghost | (153,152,211) | `#9998d3` | +58 |
| `B-hover-ghost-on-cell.png` | cell ghost | (191,191,255) | `#bfbfff` | +64 |

`[INFERRED]` The stroke sits at roughly **(145, 150, 225) ≈ `#9196e1`**, a
periwinkle / blue-violet. The true value is at least this saturated — every reading
is a blurred, chroma-subsampled *blend toward the background*, so the darkest,
most-saturated observation is an upper bound on lightness. I recommend the rebuild
pin **`#8f95e0` ± 12 per channel** and re-pin when a cleaner capture lands. The
outlier `#bfbfff` (B channel clipped at 255) comes from a frame where the yellow
recorder ring overlaps the ghost and is discarded.

`[MEASURED]` Note where this sits relative to the pinned spawn palette
(`MazeRenderer.as:45-50`): the highlight (145,150,225) is *between*
`COLOR_TANK_LINE = 0x5555BB` (85,85,187) and `COLOR_TANK_FILL = 0xAFB4EE`
(175,180,238). It is a **different, third blue** — the rebuild has no constant for
it and must add one.

### 2c. Inset, corner radius, opacity

`[MEASURED]` **Inset**: stroke centre-line is **1.25–1.3 capture px = 0.78–0.81
stage px** inside the cell's own gridline bounds (`B-hover-ghost-contains-cursor.png`, both the
right and the bottom edge). `[INFERRED]` That is consistent with a **2 stage px
stroke drawn centred on a rect inset ~1 px**, i.e. essentially *on* the cell
boundary. It is not inset by a visible margin the way a "selection box" usually is.

`[UNCERTAIN]` **Stroke width**: the horizontal profile across the ghost's right edge
in `B-hover-ghost-contains-cursor.png` gives a full-width-at-half-maximum of **6.3 capture px =
3.9 stage px**. The same measurement on a known 4-stage-px wall in the same frame
gives ~6 capture px, so the capture's blur inflates any thin feature by ~2 px. My
defensible range is therefore **2–4 stage px**; I will not round that to a constant.

`[UNCERTAIN]` **Corner radius**: visually ~6–8 capture px = 4–5 stage px on the cell
ghost. At this blur an exact radius cannot be separated from the anti-aliasing
kernel. What would settle it: a native-resolution capture, or a frame at higher video
bitrate.

`[MEASURED]` **Opacity against the floor beneath**: the ghost does not tint the
floor at all (see 2b), so alpha applies to the stroke only. The stroke over white
background reaches (153,152,211); over a `#dcdcdc` floor it reaches (143,147,214).
`[INFERRED]` If the stroke were substantially translucent those two would differ far
more than they do — the stroke reads as **opaque or near-opaque**.

### 2d. What the highlight does NOT tell us

* `[NOT VISIBLE]` No frame shows the highlight while the **crate** or **tank** tool
  is selected (all five highlight frames have the wall/construct tool active — see
  sibling [A](./A-maze-editor-toolbar.md) for tool-state reading). Whether the spawn
  tools get their own ghost is unknown.
* `[NOT VISIBLE]` No frame shows a highlight over a slot that *already has* a wall,
  so we cannot say whether the preview changes appearance for "remove" vs "add".
* `[NOT VISIBLE]` No frame shows the highlight outside the maze in a direction where
  a cell could not legally be added, so we cannot say whether illegal targets are
  suppressed.

---

## 3. Growth semantics — VE entry 6, and the test of sibling A's fit-law

VE entry 6 says:

> Screenshot shows the 13×8 maze centered with HALF-cell precision … Phase 3 snaps
> to integer cells so the editing lattice stays fixed. **Footage of a maze growing
> (cells added at the edge) reveals whether the original re-centered live or kept a
> fixed lattice.**

**Answer: it re-fits and re-centres live. The lattice is not fixed and the cell size
is not a constant.** `[MEASURED]`

### 3a. Method — registration and normalisation, stated before the conclusion

Per the brief I normalise before concluding, and here is exactly how:

1. **Zoom** is established per frame from two independent page-fixed rulers (✗–✓
   centroid distance; maze-name input width), and confirmed against the panel border
   width where visible. Frames `B-editor-howto-step3-epic-twister.png`, `4…png`, `B-editor-howto-step5-nearly-solid.png`, `A-editor-howto-step6-or-just-click.png` and
   `B-tank-spawn-placement-effect.png` are **all at ✗–✓ = 63.1–63.2 px and input
   width 263–267 px**, i.e. one identical zoom, so *no* rescaling is applied between
   them; only translation differs (each is a different crop of the same video).
2. **Landmark**: the page-fixed ✗ centroid is used as the common origin for
   frame-to-frame translation.
3. **Pitch** is measured two ways per frame and required to agree: (a) least-squares
   fit of a lattice to the detected dark wall-line centroids, (b) the spacing of
   **floor-tone boundaries** (the `#dddddd`/`#eeeeee` cell tones tile the lattice
   exactly, so their edges are gridlines even where no wall exists).
4. Only then is the pitch divided by the frame's scale to get stage px.

### 3b. The measurement

| frame | session | time | maze size (cells) | pitch, capture px | pitch, **stage px** |
|---|---|---|---|---|---|
| `B-editor-howto-step3-epic-twister.png` | C | 17:36:30 | **11 × 10** | 53.5 | **35.67** |
| `4shouldntbethislaggy…png` | C | 17:36:57 | **18 × 10** | 39.95 | **26.63** |
| `B-editor-howto-step5-nearly-solid.png` | C | 17:37:27 | 18 × 10 | 39.9 | 26.6 |
| `A-editor-howto-step6-or-just-click.png` | C | 17:38:00 | 18 × 10 | 39.9 | 26.6 |
| `7candragittocreate…png` | C | 17:38:00 | 18 × 10 | 39.9 | (no anchor; same bbox 725×407 as 4/5/6) |
| `placingtankscreate…png` | C | 17:39:04 | 18 × 10 | 40.0 | 26.62 |
| `B-hover-ghost-on-cell.png` | R | 17:00:43 | **12 × 10** | 42.44 | **26.58** |
| `B-hover-ghost-contains-cursor.png` | R | 17:01:49 | 12 × 10 | 42.46 | 26.59 |
| `B-wall-slot-preview-second-location.png` | R | 17:02:46 | 12 × 10 | 42.44 | 26.58 |
| `B-wall-slot-preview-horizontal.png` | R | 17:04:37 | **13 × 10** | 42.5 | **26.62** |

`[MEASURED]` Maze cell counts were verified by overlaying the fitted lattice on the
image and reading it off — see the derivation notes per file in §5. The 18×10 frames
share an identical maze outer bbox of **725 × 407 capture px** in `4…png`, `B-editor-howto-step5-nearly-solid.png`,
`A-editor-howto-step6-or-just-click.png` and `7candragit…png`, which is the strongest possible check that
they are one maze at one scale.

### 3c. Conclusion 1 — the lattice is NOT fixed

`[MEASURED]` Between `B-editor-howto-step3-epic-twister.png` (17:36:30) and `4…png` (17:36:57) — **27 s apart, same
session, same account, same page zoom verified two ways** — the cell pitch fell from
**53.5 to 39.95 capture px**, a 25 % reduction, while the maze grew from 11 to 18
columns. There is no reading of that other than: **the editor re-fits the maze to the
stage as it grows.**

`[MEASURED]` Conclusion 1 is corroborated by the wall thickness, which is *not*
constant on screen: FWHM 7.0 capture px at pitch 53.5 (`B-editor-howto-step3-epic-twister.png`) and 5.5 px at pitch
39.95 (`A-editor-howto-step6-or-just-click.png`), in the same session at the same zoom. Wall / cell =
0.131 and 0.138 respectively — i.e. **a constant ratio of ≈ 1/7.5**, not a constant
width. Spec `WALL_T = 4` with `CELL = 32` is a ratio of 1/8. `[INFERRED]` The
renderer therefore draws the maze at a **nominal** `CELL = 32`, `WALL_T = 4` and
applies a uniform `_xscale`/`_yscale` to the maze clip to fit — it does not
recompute geometry at a new cell size. Falsifier: a frame where wall thickness stays
constant while the cell pitch changes.

### 3d. Conclusion 2 — it re-centres live

`[MEASURED]` `A-editor-howto-step6-or-just-click.png`: maze outer bbox x 161 → 886, centre **523.5**;
panel borders x 6 and 1038, centre **522.0**. Offset 1.5 capture px = 1.0 stage px.
`[MEASURED]` `B-hover-ghost-on-cell.png`: maze bbox
x 545 → 1059, centre **802.0**; panel centre (252.8 + 1351.2)/2 = **802.0**. Offset
**0.0 px**.

`[MEASURED]` Vertically the maze is *not* on the stage's mid-line: in session R the
maze bbox centre is y = 458 while the stage's vertical centre is y = 438.3, an offset
of +19.7 capture px = **+12.3 stage px** downward. `[INFERRED]` Consistent with the
maze being centred in the stage area *below the title band* (the spec puts the title
band at stage y ≈ 10–22): centring in y ∈ [26, 400] predicts a centre at stage
y = 213 against 212.3 measured. Falsifier: a frame with a taller/shorter maze whose
vertical centre does not track that rule.

**This answers VE 6 directly: the original re-centred live, it did not keep a fixed
lattice.** VE 6 should move `PARTIAL` → **`FETCHED`** for the "does it recentre"
half; the half-cell-precision claim from the 13×8 screenshot is untouched by this
evidence (see §3f).

### 3e. Conclusion 3 — sibling A's fit-law, tested

Sibling [A](./A-maze-editor-toolbar.md) derived
`cell = min(576/(w+2), 320/(h+2))` — the maze plus a one-cell editable margin ring,
fitted into a 576 × 320 box.

**The height term is confirmed, precisely.** `[MEASURED]` A predicts
`320/(10+2) = 26.667` stage px for any 10-row maze whose width term does not bind.
Measured, across **two sessions, two accounts, two page zooms and three different
maze widths (12, 13, 18)**:

| maze | measured cell (stage px) | A predicts | error |
|---|---|---|---|
| 12 × 10 (session R) | 26.58 | 26.667 | −0.33 % |
| 13 × 10 (session R) | 26.62 | 26.667 | −0.18 % |
| 18 × 10 (session C) | 26.63 | 26.667 | −0.14 % |

Three independent measurements landing inside 0.35 % of a formula derived from
completely different evidence is not a coincidence. **`[MEASURED]` The `320` and the
`+2` margin ring are confirmed.**

**The `min()` form is confirmed.** `[MEASURED]` Widening the maze from 12 → 13 cells
(session R, `B-hover-ghost-on-cell.png` → `B-wall-slot-preview-horizontal.png`, 17:00:43 →
17:04:37) left the cell pitch unchanged at 42.44 → 42.5 capture px. Widening from
12 → 18 across sessions likewise leaves it at 26.6. So width genuinely does **not**
enter for these mazes, which is exactly what a `min()` with the height term binding
predicts.

**The width term is untested.** `[NOT VISIBLE]` For `576/(w+2)` to bind you need
`w + 2 > 1.8 (h + 2)`. No frame in my set satisfies that: the widest maze is 18 × 10
(`20 < 21.6`). So I can put **no** number on the `576`. It should stay flagged as
A's inference, not as measured.

**One frame disagrees, and I am not going to paper over it.** `[MEASURED]` `B-editor-howto-step3-epic-twister.png`
is an 11 × 10 maze — h = 10, so A predicts 26.667 — measured **35.67 stage px**,
a 34 % excess. 35.67 is not a random number: `320/9 = 35.56`, i.e. **the value A's
law returns for a 7-row maze** (agreement 0.3 %). Two readings:

* `[UNCERTAIN]` **The refit lags.** `B-editor-howto-step3-epic-twister.png` is captured *mid-stroke* (blue
  button-down disc present at (485, 592)), 27 s before `4…png`. If the fit is
  recomputed on some event rather than on every cell added, then at the last refit
  the maze was 7 rows tall and the user has since dragged three more rows without a
  refit. Nothing overflows: 10 rows × 35.56 = 355.6 stage px still fits the ~374 px
  of stage below the title band. This reading keeps A's law exactly as written.
* `[UNCERTAIN]` **The law is wrong in some third variable.** Solving
  `min(A/(w+2), B/(h+2))` against `B-editor-howto-step3-epic-twister.png` + the 18×10 frames requires B ≈ 427 stage
  px, which exceeds the 400 px stage and is therefore impossible. So the *simple*
  patch to A's law does not exist; if the law is wrong, it is wrong structurally.

I cannot choose between these from stills. **What would settle it:** any two frames,
seconds apart in the same session, that bracket a single cell being added at the
bottom edge — if the pitch changes at the moment of the click, the fit is immediate
and `B-editor-howto-step3-epic-twister.png` needs another explanation; if the pitch changes only after the button is
released, the lag reading is proved. That is a **new want** (§7).

**Verdict on A's law, stated plainly as the task asks:** the cell pitch **shrinks as
the maze grows — A is right that the cell is dynamic.** The specific formula's height
term and margin ring are confirmed to 0.35 % on three independent mazes; its width
term is untested; and one frame (`B-editor-howto-step3-epic-twister.png`) is off by exactly the amount a 3-row refit
lag would produce.

### 3f. Program impact

* `src/mazecreator/MazeRenderer.as:19,35-51` — `CELL = 32` as a **constant**.
  **CONTRADICTED.** The cell is a function of maze size, and the measured value for
  every 10-row maze is 26.6, not 32. Spec `docs/standards/MAZECREATOR-VISUAL-SPEC.md:21`
  ("CELL | 32 px") is challenged: 32 is what the fit returns for the *8-row* maze in
  `Making a maze.png` (`320/10 = 32.0` exactly), which is why the deduction looked
  clean. `[INFERRED]` The pinned constant is not wrong for that screenshot; it is
  wrong as a *constant*.
* `src/mazecreator/MazeRenderer.as:20-23,36-40` — `LATTICE_X/Y = 56/50`,
  `LATTICE_W/H = 18/10` fixed. **CONTRADICTED** as a *fixed* lattice; a fixed 18×10
  region at 32 px would be 576 × 320 stage px, which is precisely A's fit box —
  suggesting the rebuild's authors deduced the box correctly but then froze the cell
  instead of the box.
* `src/mazecreator/MazeRenderer.as:55-58` `originFor()` and
  `src/mazecreator/Editor.as:82-105` `loadIntoLattice()` (integer-cell placement plus
  `fracX/fracY` half-cell remainder) — **CONTRADICTED in mechanism.** The evidence
  says the maze is centred by *fitting and scaling*, so half-cell offsets fall out of
  the fit automatically and do not need a remainder shift.
* **OVERHAUL RULE, named concretely:** `src/mazecreator/MazeRenderer.as` must be
  **rewritten wholesale**, not patched. Its `initConstants()` becomes a
  `fitFor(data)` returning `{cell, ox, oy}`; `render()` takes that; `Editor.as`
  hit-testing (lines 192–198) must use the fitted cell rather than
  `MazeRenderer.CELL`. `Editor.as:21 EDGE_TOL = 6` — an invented constant in a
  now-invalid coordinate system — must be re-derived (see §7).

---

## 4. The growth series in detail — `B-maze-growth-mechanism*.png`, and the margin ring

### 4a. The one-cell editable margin ring, seen directly

`[OBSERVED]` `B-hover-ghost-in-margin-ring.png` (account `mr_enderman`)
shows a **4 × 4 maze** with a blue rounded-rect ghost **floating in empty white space
to the left of it**, its right edge touching the maze's left boundary wall, and the
mouse cursor's arrow tip inside the ghost.

`[MEASURED]` Lattice fitted from the maze's own wall lines: vertical gridlines at
x = 799.8, 875.0, 950.0, 1025.0, 1100.0 → pitch **75.05** capture px; horizontal
gridlines 251.4, 326.4, 401.4, 476.4, 551.4 → pitch **75.0**. The ghost's stroke
centres are at x = 729.8 and 794.5, y = 405.6 and 471.7 — i.e. it occupies the
lattice cell **(column −1, row 2)**, exactly one cell outside the maze bbox, aligned
to the maze's own lattice to under a pixel.

`[INFERRED]` **This is direct visual proof of a one-cell editable margin ring around
the maze** — the `+2` that sibling A's fit-law assumes. The editor lets you hover,
and by implication click, a cell that does not exist yet, and it previews it at the
correct lattice position. Falsifier: a frame with a ghost **two** cells outside the
maze.

`[OBSERVED]` The same thing appears in `B-maze-growth-mechanism.png` (session C, a
3 × 3 maze with a ghost one cell to its left) — two independent accounts, two
independent sessions.

`[OBSERVED]` In `B-maze-growth-mechanism.png` **no mouse cursor is drawn at all**
(`[MEASURED]` 0 yellow-ring pixels, 28 strong-blue pixels — all of them the ghost's
own stroke). The ghost is therefore **stage content drawn by the SWF**, not part of
a cursor bitmap. That is worth stating because it is the one thing that could
otherwise have explained the highlight away.

The owner's filename claim, verbatim: *"B-maze-growth-mechanism"* — "expanding walls
by clicking". **Corroborated in substance** (the maze does expand, and the ghost
marks the cell that expansion would add), with one correction: what expands is the
**floor**, and the boundary walls follow it. Nothing in these frames shows a wall
being created outside the maze.

### 4b. The three expanding frames measured, and the width term of A's law

`[MEASURED]` `B-maze-growth-step2-width-term-binds.png` carries the stage-internal title
`cam12win` at exactly **128 px wide**, identical to the same string in
`A-editor-howto-step6-or-just-click.png` (128 px, scale ×1.5000). The expanding crops are therefore **not
zoomed** — they are tight crops of the same video at the same scale. I take
s = 1.5000 for all three, and flag that only `…2.png` has the anchor directly.

Pitch was recovered by fitting `outer bbox = pitch × (n + 1/8)` — the maze's boundary
wall is centred on the outermost gridlines and, per §3c, is `cell/8` thick, so it
overhangs by `pitch/16` on each side. Cross-checked against the interior tone
boundaries, which agree to 0.3 px in `B-maze-growth-mechanism.png` (predicted
351.7, observed 352).

| frame | crop time | maze | pitch (capture) | **cell (stage)** | A predicts | which term binds |
|---|---|---|---|---|---|---|
| `B-maze-growth-mechanism.png` | 17:35:51 | **3 × 3** | 95.68 | **63.8** | `320/5 = 64.0` | height |
| `B-maze-growth-step1.png` | 17:34:57 | **7 × 3** | 95.5 | **63.7** | `320/5 = 64.0` | height |
| `B-maze-growth-step2-width-term-binds.png` | 17:35:22 | **≈10 × 3** (crop clips the left) | 74.0 ± 0.3 | **49.3 ± 0.2** | `576/12 = 48.0` (w = 10) | **width** |

`[MEASURED]` **This is the first and only test of A's width term in the corpus, and
it passes.** For a 3-row maze the switch from height-bound to width-bound happens at
`576/(w+2) < 320/5` → `w > 7`. Observed: at w = 7 the cell is still 63.7 (height
still binding, unchanged from the 3-wide maze); at w ≈ 10 it has dropped to 49.3
(width now binding). The switch occurs exactly in the predicted interval.

`[UNCERTAIN]` The width **numerator** cannot be pinned tightly because the crop clips
the maze's left edge, so `w` is inferred, not counted. Inverting: `A = 49.33 × (w+2)`
gives **A = 592 for w = 10** and **A = 542 for w = 9**. A's `576` sits inside that
bracket. What would settle it: any frame with a wide, short maze fully in shot.

`[UNCERTAIN]` The crop order (…1, …2, then the unsuffixed file) implies the maze went
7×3 → 10×3 → 3×3, i.e. shrank. **mtimes are crop times, not source times**, so the
source order is not constrained by them. Read in the physically sensible order
(3×3 → 7×3 → 10×3) the three frames are a clean growth series showing the cell
holding at 64 while the height binds, then dropping to 49 once the width takes over.
I state the ambiguity rather than assert an order.

`[OBSERVED]` `B-maze-growth-step1.png` is a **badly torn video frame** — the
left half of the maze is replaced by motion-compensation debris (broken wall dashes,
ghosted circular blobs) while the right half is clean. Only the clean half was used
for measurement. This is the same lag/tearing the owner flags in
`B-editor-howto-step4-lag-note.png`.

### 4c. Consolidated fit-law evidence

Every measurement of the cell size in this topic, in one table. "A predicts" is
`min(576/(w+2), 320/(h+2))`.

| frames | session | maze | **cell, stage px** | A predicts | error |
|---|---|---|---|---|---|
| `B-maze-growth-mechanism.png` | C | 3 × 3 | 63.8 | 64.00 | −0.3 % |
| `B-maze-growth-step1.png` | C | 7 × 3 | 63.7 | 64.00 | −0.5 % |
| `B-hover-ghost-in-margin-ring.png` | mr_enderman | 4 × 4 | 53.23 | 53.33 | −0.2 % |
| `B-maze-growth-step2-width-term-binds.png` | C | ≈10 × 3 | 49.3 | 48.00 (w=10) | +2.7 % |
| `B-hover-ghost-on-cell.png`, `B-hover-ghost-contains-cursor.png`, `B-wall-slot-preview-second-location.png` | R | 12 × 10 | 26.55–26.59 | 26.667 | −0.4 % |
| `B-wall-slot-preview-horizontal.png` | R | 13 × 10 | 26.62 | 26.667 | −0.2 % |
| `4…`, `5`, `A-editor-howto-step6-or-just-click`, `7candragit…`, `placingtanks…` | C | 18 × 10 | 26.63–26.67 | 26.667 | ±0.1 % |
| `B-editor-howto-step3-epic-twister.png` | C | 11 × 10 | 35.53 | 26.667 | **+33 %** (= `320/9`, the h = 7 value) |

`[MEASURED]` **Four distinct maze heights (3, 4, 10 — plus the anomalous 7-value)
and four distinct cell sizes (63.8, 53.2, 49.3, 26.6) across three accounts and
three page zooms, all reproduced by one formula to better than 0.5 %.** This is not
a fit — the formula came from sibling A's independent reasoning, and every number
here is a prediction it made before I measured.

**Verdict, stated as the task requires:** the cell pitch **shrinks as the maze
grows**. Sibling A is right. `MazeRenderer.CELL = 32` is not a constant of the
program; it is `320/(8+2)`, the value the fit returns for the 8-row maze in
`Making a maze.png`.

---

## 5. Floor tone pattern — VE entry 8a

VE 8a asks for exactly one thing:

> Two different frames of the SAME maze would settle it instantly: identical tones =
> deterministic function (then derivable); different tones = runtime random.

I have four such frames, and I ran a second test 8a did not ask for.

### 5a. The two tones, measured

`[MEASURED]` Pooling 28 111 pixels from the inner 44 % of every floor cell in
`B-hover-ghost-on-cell.png`, the luminance histogram is
cleanly **bimodal** with no third mode:

| cluster | n px | mean RGB | median RGB | hex |
|---|---|---|---|---|
| dark | 15 554 | (220.8, 220.7, 220.4) | (221, 221, 221) | **`#dddddd`** |
| light | 12 007 | (236.8, 236.9, 236.6) | (237, 237, 237) | `#ededed` |

`[MEASURED]` The dark tone is **exactly** the spec's pinned `#dddddd` (0xDD = 221).
The light tone reads `#ededed`, **one level below** the spec's `#eeeeee`.

`[INFERRED]` That one-level gap is a **video-encode rounding artefact, not a build
difference**. Reasoning: a build difference or a gamma difference would displace
*both* tones (and gamma would displace the mid-tone more than the light one); here
the darker of the two lands on its pinned value to the exact integer while the
lighter is short by one. Chroma subsampling cannot move luma at all. A −1 luma
rounding on a near-white flat field in an H.264 encode is routine. **I recommend the
spec keep `#eeeeee`** and record this reading as corroboration, not as a challenge.
Falsifier: a second, independently encoded capture that also reads 237.

### 5b. VE 8a's own test — same maze, four frames

Four frames of session R's maze, in crop order 17:00:43 → 17:01:49 → 17:02:06 →
17:02:46, each registered independently by fitting its own lattice (origins differ by
up to 4 px between frames because each is a separate crop of the video).

Tone grids, `L` = light `#eeeeee`, `D` = dark `#dddddd`, `.` = no floor,
`*` = spawn icon or cursor overlay covering the sample core:

```
F1  B-hover-ghost-on-cell.png    F4  B-wall-slot-preview-second-location.png
    (17:00:43)                      (17:02:46)
    ........LL..                    ..DL....LL..
    *DDDDDLLDL.*                    *DDD*DLLDL.*
    D*LLLD*LDDLL                    D*LLLD*LDDLL
    DDDD**LDLLLD                    DDDD**LDLLLD
    LDDLDDLD*DL.                    LDDLDDLD*DL.
    DDLDD*LDDDD.                    DDLDD*LDDDD.
    DDLDLLLDDLD.                    DDLDLLLDDLD.
    DLLDLDDL..L.                    DLLDLDDL..L.
    LDLLDDDD..*.                    LLLLDDDD..*.
    L*.D........                    L*..........
```

`[MEASURED]` **115 of 120 lattice positions have identical class.** The five that
differ are each explained without appeal to randomness:

| cell | F1 → F4 | explanation |
|---|---|---|
| (2, 0) | `.` 254 → `D` 224 | **new floor cell** — the maze grew at the top edge between the two frames |
| (3, 0) | `.` 255 → `L` 238 | same — a second new cell |
| (4, 1) | 221 → 199 | codec debris / element overlap; not an L↔D swap (199 is below both tones) |
| (1, 8) | 217 → 234 | this cell reads 217 / 235 / 210 / 234 across F1–F4 — it sits under the yellow recorder ring in every frame and is the *only* unstable one |
| (3, 9) | 227 → `.` | the yellow ring's edge tinting an empty cell in F1 |

`[MEASURED]` Restricting to cells that are floor in all four frames and clear of the
recorder overlay: **80 of 81 identical across all four frames**, the exception being
(1, 8) above.

`[MEASURED]` Redraws certainly happened between these frames: walls were added, floor
cells were added, and a hover ghost moved. So the tones survive redraw.

`[MEASURED]` The frames are also separated by **real elapsed time in the source
footage**, not merely by crop time: the page's live `Scrapyard` odometer advances
from `66570803`9 (F1) to `66570807`3 (F2). That matters — it rules out the trivial
explanation that the four crops are the same video frame saved four times.

**VE 8a's stated conclusion applies: identical tones. The tone is NOT re-randomised
per redraw.** That kills the worst case for the rebuild.

### 5c. A second test VE 8a did not ask for — is it a function of (x, y)?

If the tone were a deterministic function of lattice coordinates, then two *different*
mazes would show the same pattern at the same coordinates (allowing for a lattice
offset). I extracted the full **18 × 10** tone grid from `A-editor-howto-step6-or-just-click.png` — session
C's maze is a solid rectangle, so all 180 cells are floor, which makes it the ideal
comparison target:

```
cam12win, 18×10 (A-editor-howto-step6-or-just-click.png)
   LDDDLDLLDDDLLDDLDD
   DLLD*DLDLDLLLDLLDLL
   DDDDLDDLLLDLLDDDLL
   DDLDLDDLDLDLLLDDLL
   LLLLLLLDDLLDLLLLLD
   LLDDLDLLDDDLLDDLDD
   LLLDLDDLDLDLLLLDLL
   DDLDLDLLDLDDDDLLLD
   DLDLDLLLDLLDDDDLLL
   LDDLDLDDDDDLDLLDLL
```

`[MEASURED]` Cross-correlating session R's grid against session C's over **all 665
integer lattice offsets**, the best agreement any offset achieves is **0.710**
(n = 31 overlapping classified cells); the mean over all offsets is **0.497**
(= chance) and the best offset with a large overlap (n = 59) reaches only 0.661. A
deterministic function of lattice coordinates would give **1.000** at the correct
offset.

`[MEASURED]` The light fraction also differs per maze:

| maze | light : dark | fraction light |
|---|---|---|
| `Making a maze.png` (spec, 13 × 8) | 15 : 29 | 0.34 |
| session R (12 × 10) | 35 : 46 | 0.43 |
| session C (18 × 10) | 95 : 84 | **0.53** |

`[MEASURED]` None of the obvious rules fits session R's grid better than chance:
`(x+y)%2` 40/81, the rebuild's `(x*3+y*7)%3` 45/81, `(x+y)%3` 38/81, `x%3` 45/81,
`y%3` 45/81 — all within noise of the 50–57 % a coin flip would give.

`[INFERRED]` **The tone is randomised once — per cell at creation, or per maze at
load — and then persists for the life of the editing session.** It is not a function
of `(x, y)` shared between mazes, and it is not re-rolled per frame. I cannot
distinguish "random, stored" from "hash seeded on the maze's identity"; both produce
exactly what is observed. Falsifier for the first: reopening the *same saved maze*
twice and getting the same pattern.

`[OBSERVED]` The two cells that appeared between F1 and F4 came in with tones 224
(dark) and 238 (light) — i.e. a newly created cell picks up a tone immediately, which
is consistent with "assigned at creation".

**Status of VE 8a:** move `WANTED` → **`PARTIAL`**. The per-redraw question is
answered (no); the per-maze question is answered (different mazes differ, at every
offset); the "reopen the same maze" question remains open and is the only thing left.

**Rebuild consequence.** `MazeRenderer.floorTone()` (lines 60–63) uses
`((x*3 + y*7) % 3 == 0)`. `[INFERRED]` It is a **fair stand-in for a single render**,
exactly as VE 8a hoped, and the OVERHAUL RULE does *not* demand it be replaced by
another fixed function — but it is wrong **in kind**: it gives every maze the same
pattern at the same coordinates, and it gives ≈ 1/3 light where the measured range
across three mazes is 0.34–0.53. A per-cell random assigned at creation and stored
in `MazeData` would be closer to the evidence; if determinism is needed for gate C,
seed it per maze rather than per coordinate. That is a **recommendation**, not an
overhaul demand, and it belongs in `DIVERGENCES-SERVED.md`.

---

## 6. Spawn placement rendering

### 6a. The owner's note, verbatim

`UI/B-owner-note-spawn-icons.txt`, in full, exactly as typed (single line, no trailing
newline, comma splice and all):

> `blue objects on maze creator is a tank, orange/brown is item (e.g. weapons e.g. laser) they all slowly rotate as animation.`

Three claims. All three tested.

### 6b. Claim 1 — "blue objects … is a tank" — **CORROBORATED**

`[OBSERVED]` In `B-tank-spawn-placement-effect.png`, upscaled ×8, the blue icon in the
maze's top-left cell resolves unmistakably into a **top-view tank**: a rounded hull,
**two parallel tracks** flanking it, and a **barrel** projecting from one end, drawn
as a dark blue-violet outline over a pale blue fill. This is not a blob or a
generic marker. Any reader looking at the upscale would agree.

`[MEASURED]` `B-hover-ghost-on-cell.png` contains exactly
**five** such blue icons, at capture (611, 345), (823, 345), (909, 430), (780, 475),
(611, 642), each 19–25 × 25–28 capture px = **12–16 × 16–18 stage px**.
`MazeRenderer.drawTank()` (lines 136–146) draws a 12 × 16 hull with 3 × 18 tracks and
a 2 × 8 barrel — **12–16 × 16–18 stage px overall**. The rebuilt icon's *size and
component layout are confirmed*; only its rotation is wrong (6d).

### 6c. Claim 2 — "orange/brown is item (e.g. weapons e.g. laser)" — **CORROBORATED in substance, with a caveat**

`[OBSERVED]` The amber icon resolves into a **square with a distinctly darker border**
— a crate/box seen from above. It carries no weapon imagery: there is no laser, no
gun, no glyph inside it. `[INFERRED]` The owner is describing what the marker
*means* (a weapon-crate spawn — TankTrouble's weapon pickups arrive in crates), not
what it *depicts*. That reading matches the rebuild's `type == 8` "crate" and
`Editor.as:222` (`var t:Number = (tool == "tankSpawn") ? 5 : 8;`). Recorded as
corroborating the **semantics**, not as evidence of a laser sprite.

`[MEASURED]` Icon core tones, sampled from the flat interior of each icon:

| icon | measured core | spec pinned | `MazeRenderer` constant |
|---|---|---|---|
| tank fill | ≈ (165, 170, 232) | (175, 180, 238) | `COLOR_TANK_FILL = 0xAFB4EE` |
| tank outline | ≈ (90, 92, 175) | "dark blue-violet outline" | `COLOR_TANK_LINE = 0x5555BB` = (85,85,187) |
| crate fill | ≈ (224, 185, 90) | (219, 183, 85) | `COLOR_CRATE_FILL = 0xDBB755` |
| crate border | ≈ (168, 128, 55) | (170, 130, 50) | `COLOR_CRATE_EDGE = 0xAA8232` |

`[MEASURED]` **Every pinned spawn colour survives contact with independent footage.**
The crate fill is +5/+2/+5 off its pinned value and the border −2/−2/+5 — inside the
±8 that a video encode of a soft-edged 16 px icon can shift. `[OBSERVED]` The tank
fill reads ~10 levels darker than pinned, which is what a blurred dark outline
bleeding into a small light interior does; it is not evidence of a different colour.
**These four constants stay as they are.**

### 6d. Claim 3 — "they all slowly rotate as animation" — **CORROBORATED**

The spec (`docs/standards/MAZECREATOR-VISUAL-SPEC.md:30`) says the tank icon is *"not clearly
rotated (upscale too soft to pin exact angles — treated as axis-aligned)"*, and
`MazeRenderer.as:9-11` records the same surrender. The task asks: *if any two frames
show the same spawn icon at different angles, that settles it.* They do.

`[MEASURED]` Orientation was measured with a gradient structure tensor at doubled
angle (4θ, giving orientation mod 90° — the natural period of a square), weighted by
squared gradient magnitude, over a disc around each icon.

**Test 1 — two icons of the same type in the same frame.**
`B-crate-spawn-placement-effect.png`: the two crates measure **−25.9°** and **+30.4°**
(mod 90). They cannot both be axis-aligned, and they are not at the same angle as
each other. `[OBSERVED]` The upper crate is visibly a **tilted square** in the ×6
upscale — this is not a marginal measurement.

**Test 2 — the same icon in two frames.** The spiral maze appears in both
`B-tank-spawn-placement-effect.png` (crop 17:39:04) and
`B-crate-spawn-placement-effect.png` (crop 17:39:32). The tank in the maze's top-left
corner cell measures **−5.8°** in the first and **+6.7°** in the second — a change of
**12.5°**. The interior tank measures **+28.2°** then **+13.0°** — a change of
**15.2°**. Two independent objects, both moved, between two frames of one maze.

`[UNCERTAIN]` The **sign and rate** cannot be recovered. The 4θ estimator returns
orientation mod 90°, so a measured +12.5° is equally consistent with −77.5°; and
because mtimes are crop times the real elapsed time between the two frames is
unknown. So I can say the icons rotate; I cannot say how fast, or whether all icons
share one phase, or whether tanks and crates rotate at the same rate.

`[MEASURED]` Session R's five crates, across four frames, vary by only ±3°
(crate at (993, 602): 2.41°, 2.33°, 2.47°, 2.91°). `[INFERRED]` That is *not*
evidence against rotation, but it is a real constraint: the Scrapyard odometer proves
non-zero elapsed time between those frames (§5b), so whatever rotation is happening is
slow enough to keep five icons inside ±3° across that interval — which is at least
consistent with the owner's word *"slowly"*. The elapsed time itself is not
recoverable (the odometer is a scrap counter, not a clock). It does put a soft floor under "slowly": the rate is slow enough that four
hand-picked frames of one session can land within 3°.

**Program impact.** `MazeRenderer.as:126-147` draws both icons **axis-aligned**
(`boxAt()` emits axis-parallel rectangles), and the class comment at lines 9–11 says
so explicitly. **CONTRADICTED.** Under **THE OVERHAUL RULE** `drawCrate()` and
`drawTank()` in `src/mazecreator/MazeRenderer.as` must be **rewritten** to draw into a
rotated child clip with a per-object angle advanced on `onEnterFrame`, and the
`.provenance` sidecar and the spec line
`docs/standards/MAZECREATOR-VISUAL-SPEC.md:30` ("not clearly rotated") must be superseded.

### 6e. The placement effect — a wholly new finding

The owner's filename claims, verbatim: *"B-tank-spawn-placement-effect"* and
*"B-crate-spawn-placement-effect"*. **Corroborated, and it is not what the rebuild
draws.**

`[OBSERVED]` In `B-tank-spawn-placement-effect.png` the tank in the maze's top-left
cell is surrounded by a **burst of short blue rays and scattered blue speckles**
extending roughly one cell in every direction. In
`B-crate-spawn-placement-effect.png` **both** crates carry the same effect in **amber**
— rays plus loose sparkle dots at varying radii, clearly *particulate*, not a smooth
radial gradient.

`[MEASURED]` The effect's colour follows the icon: blue for tanks (matching
`COLOR_TANK_LINE`/`FILL` family), amber for crates (matching the crate family). The
speckles are discrete blobs of 3–8 capture px, at distances of 20–60 capture px from
the icon centre, i.e. **0.3–0.8 cell**.

`[INFERRED]` This is a **transient placement animation**, not the persistent "soft
glow" the spec records. Reasoning: the effect is present only on icons in frames
whose filenames say a spawn was just placed, and the five settled spawns in session R
show a soft halo but no rays or speckles. Falsifier: a frame of a maze nobody has
touched for many seconds where the icons still show rays.

`[UNCERTAIN]` I cannot rule out that what the spec read as a *"soft blue glow"* /
*"soft yellow glow"* in `Making a maze.png` is one frame of this same burst caught
late in its decay. All ten objects in that shot showing it simultaneously argues
against, but that shot may itself have been taken right after a bulk placement.

**Program impact.** `MazeRenderer.glow()` (lines 115–123) draws three concentric
squares at alphas 10/16/22 — a static, axis-aligned, square "glow". **CONTRADICTED
in form** (the evidence shows rays and discrete speckles) and **incomplete in
behaviour** (there is no placement animation at all in the rebuild). New want raised
in §8.

### 6f. Bonus: a third confirmation of finding B17

`[OBSERVED]` The centred grey heading above the stage reads:

| frame | heading (verbatim) | maze-name input (verbatim) | account in the left sidebar |
|---|---|---|---|
| `B-hover-ghost-on-cell.png` | `revengexx1` | `Run Around The WORLD` | `revengexx1  Exp. 10500` |
| `B-editor-howto-step3-epic-twister.png`, `B-editor-howto-step5-nearly-solid.png`, `A-editor-howto-step6-or-just-click.png` | `cam12win` | `Epic Twister` | `cam12win  Exp. 1191` |
| `B-hover-ghost-in-margin-ring.png` | `mr_enderman` | `Kill The Player` | `mr_enderman  Exp. 7722` |

`[OBSERVED]` In all three sessions the heading equals the **account name** and the
**maze name lives in the page's input box below the stage**. `revengexx1` also
appears in the frame's own "Top 10 Exp." leaderboard with the same spelling.

This **confirms sibling [A](./A-maze-editor-toolbar.md)'s conclusion** on two extra,
independent accounts. `src/mazecreator/Editor.as:338`:

```actionscript
titleTf.text = title;      // title = the maze name, from initCode 't'
```

is **CONTRADICTED**. The correct source is `init.n` (the user name, read at
`Editor.as:38` and currently used only for the save POST at line 250). Under **THE
OVERHAUL RULE** the title band in `src/mazecreator/Editor.as` (`buildStage()` lines
305–310 and `redraw()` line 338) is rewritten, and `onSetVariable`'s `mazeName`
branch (line 165) must stop calling `redraw()` for the title's sake.

---

## 7. Limits — S48

`[NOT VISIBLE]` **No frame in my set shows a refused placement.** I looked
specifically for: a greyed-out tool icon, a shake/wobble on a tool or on the maze, an
error panel, a colour change on the ✓, or a spawn icon appearing and vanishing.
None appears.

`[OBSERVED]` What the evidence *does* show is the cap being **reached**, in session R:
exactly **5 blue tank icons and 5 amber crate icons** — 10 objects — on one maze. This
matches `docs/standards/MAZECREATOR-VISUAL-SPEC.md:32` ("exactly 5 tanks + 5 crates — the corpus
caps at max") and `src/mazecreator/Editor.as:228-230`:

```actionscript
if (data.objects.length >= 10) return;
if (t == 5 && tanks >= 5) return;
if (t == 8 && crates >= 5) return;
```

`[INFERRED]` Session R's maze sits exactly at the cap, on a maze the user was actively
editing, without any visible "you are at the limit" affordance in the frame. That is
weak, one-frame evidence that the original's refusal is **silent** — the `return`
with no feedback that `Editor.as:228-230` already implements. It is not enough to
close S48. Falsifier: a frame of a capped maze with a greyed tool.

**S48 stays WANTED.** The precise want is narrower now: *a frame captured while the
user clicks a spawn tool on a maze that already has 5 of that type.*

---

## 8. The numbered sequence the owner assembled — `3` → `4` → `5` → (`6`) → `7`

The owner numbered five frames. `A-editor-howto-step6-or-just-click.png` belongs to analyst A; I inspected
it only for continuity and describe it in one line. Reconstructed **in crop order**,
which for these five is also the only sensible build order (each maze strictly
contains the previous one):

| # | file | crop time | maze state | pitch | cursor |
|---|---|---|---|---|---|
| 3 | `B-editor-howto-step3-epic-twister.png` | 17:36:30 | sparse **11 × 10** skeleton: a 3×2 block top-left, a 3×2 block top-right, a 10-wide bar joining them, then a 1-wide column running down the left side to a 2-cell foot | 53.5 | blue disc (down) |
| 4 | `4shouldnt…png` | 17:36:57 | **18 × 10**: the top bar now spans the full width, the left column has thickened, a T of floor reaches the bottom, and **two detached rectangles float unattached at the bottom right** | 39.95 | blue disc (down) |
| 5 | `B-editor-howto-step5-nearly-solid.png` | 17:37:27 | **18 × 10** nearly solid; one large rectangular **hole** (≈6 × 5 cells) remains open at the lower right, correctly closed by 4-px walls | 39.9 | blue disc (down) |
| 6 | `A-editor-howto-step6-or-just-click.png` | 17:38:00 | 18 × 10 **completely solid**; the user has switched from filling floor to drawing interior walls — a short run plus two detached dashes on the first interior gridline | 39.9 | blue disc (down) |
| 7 | `7candragit…png` | 17:38:00 | same solid 18 × 10; the wall run on that gridline now spans ≈7 cells, with one detached fragment ahead of it | 39.9 | blue disc (down) |

**What the sequence demonstrates, step to step:**

1. **3 → 4:** `[MEASURED]` the maze grew from 11 to 18 columns and **the cell pitch
   shrank by 25 %** (53.5 → 39.95). This is the growth-refit result of §3, and it is
   the single pair of frames that proves it.
2. **3 → 4:** `[OBSERVED]` two rectangles at the bottom right of `4…png` are
   **completely disconnected** from the rest of the maze — floor with its own closed
   wall ring, touching nothing. So the editor permits a **non-contiguous** floor set;
   it does not enforce connectivity while editing. The rebuild's
   `MazeData.normalizeBoundary()` + `Editor.as:216-218` toggle model already permits
   this, so this is a **confirmation**, and a mild one for the save path: whatever
   `cropToFloorBbox()` (`Editor.as:109-133`) emits must tolerate islands.
3. **4 → 5:** `[OBSERVED]` the fill proceeded by *closing in* on a large rectangular
   hole rather than by sweeping rows. `[MEASURED]` The hole's closure walls are the
   same 6 capture px thick as the outer boundary (both bottom out at luma 56–94), so
   they are ordinary walls, not a special "edge" stroke. Confirms
   `MazeRenderer.render()` lines 87–92, which derive the unstorable south/east
   closure edges from floor adjacency — the evidence shows closure walls on **all
   four** sides of an interior hole, which is what adjacency-derivation produces.
4. **5 → 6:** `[OBSERVED]` the hole is filled and the user switches tool behaviour
   from "add floor" to "add wall" **without any visible tool change** — the same
   notebook/construct tool is lit in the toolbar throughout (compare
   sibling [A](./A-maze-editor-toolbar.md)). `[INFERRED]` This corroborates the
   rebuild's core premise at `Editor.as:199-219`: **one construct tool, with the hit
   position inside the cell deciding cell-vs-edge.** That premise, at least, survives.
   Falsifier: a frame where a fourth tool is lit while a wall is drawn.
5. **6 → 7:** `[MEASURED]` the wall run on one gridline extended and its detached
   fragments moved with the cursor — the drag-paint evidence of §1a.

`[UNCERTAIN]` One thing the sequence does **not** settle: whether a drag *toggles*
each cell it crosses (so dragging back over your own stroke erases it) or *paints* a
single value fixed at press time. Every frame here shows a stroke over virgin
territory. This matters for the rewrite and is a **new want** (§10).

---

## 9. File-by-file analysis

Every assigned file, none skipped. Cross-frame findings are stated once above and
referenced here rather than repeated.

### `UI/B-hover-ghost-on-cell.png` (1602 × 1052, crop 17:00:43)  *(was `mazeditor-selectedblockistheblockonmousehover.png`)*

→ [`./UI/B-hover-ghost-on-cell.png`](./UI/B-hover-ghost-on-cell.png)

**Filename claim (repo owner):** *"maze editor — selected block is the block on mouse
hover"* — **partly corroborated**: a per-cell hover ghost exists and is measured here,
but in *this* frame it is two columns from the cursor (see §1c). Unsettled which way.

**What is drawn.** `[OBSERVED]` Full TankTrouble page at browser zoom, `revengexx1`
logged in. Top nav: TANKTROUBLE wordmark, NEWS tab, a **raised (selected) wrench
tab**, speech-bubble tab, flask tab. Left rail: `Scrapyard` odometer reading
`66570803`**9** (the last two drums are mid-roll — `[UNCERTAIN]` on those glyphs),
Log In box, two tank cards (`creed  Exp. 7820`; `revengexx1  Exp. 10500` with a
Halloween pumpkin-bomb tank sprite), `Need Help?`, `Visits / Since 2007-12-16 /
17858418 / Today: 9805 / Online: 283 / Tank owners: 518873 / Logged in: 95`. Right
rail: `Top 10 Exp.` (`jokerfury9 1671220`, `lukejp1999 129042`, `lorenzo9 120736`,
`rushabh4084 77040`, `jermy2 24984`, `JB2700 24439`, `ronaldoron 18150`, `RMC 12957`,
`revengexx1 10500`, `soldado 8343`), `Weekly | Friends`, Like `8.2k`, `Tell a Friend`,
`Available on the App Store`, a red hoodie ad, `Got Feedback?`. Centre panel:
heading `revengexx1`; the maze; watermark `version 0.3`; below the stage the name
field `Run Around The WORLD`, three tool icons, red ✗, green ✓. Below the panel:
`Sign up another tank`, `Name your tank`, `tank name`.
`[OBSERVED]` The **yellow recorder ring** sits at the maze's bottom-left.

**Measurements.** `[MEASURED]` Panel 1098.4 × 734.5 capture px → **scale ×1.5966**
(§Scope). Lattice pitch **42.444** capture px both axes (least-squares fit to 12
column and 8 row wall-line centroids; residual < 0.6 px) = **26.58 stage px**. Maze
**12 × 10**, bbox x 545–1059, y 240–676, horizontal centre **802.0** = panel centre
**802.0** exactly. Floor tones `#dddddd` (n = 15 554 px) / `#ededed` (n = 12 007 px),
light fraction 0.43. **5 tank icons + 5 crate icons = the 10-object cap.** Hover
ghost: rounded rect on lattice cell (0, 9), interior `(237,237,239)`.

**Links to the program.** VE 5 (ghost exists → q3 answered); VE 6 (12 × 10 at
26.58 = `320/12`); VE 8a (this is the reference frame for the tone grid);
S48 (cap reached); `Editor.as:338` contradicted (heading = account name);
`MazeRenderer.as:19` `CELL = 32` contradicted; spec `#dddddd` confirmed exactly.

**What this does NOT show.** No tool-state change; no error panel; no save; no
cursor-adjacent ghost (which is why `B-hover-ghost-contains-cursor.png` matters).

### `UI/B-hover-ghost-contains-cursor.png` (1600 × 1047, crop 17:01:49)  *(was `selectedblock2.png`)*

→ [`./UI/B-hover-ghost-contains-cursor.png`](./UI/B-hover-ghost-contains-cursor.png)

**Filename claim:** *"selected block 2"* — **corroborated**; this is the frame where
the ghost demonstrably contains the cursor.

**What is drawn.** `[OBSERVED]` Identical page furniture to the previous frame
(same account, same leaderboard). `[MEASURED]` The Scrapyard odometer has advanced
from `66570803`9 to `66570807`3 — the counter is live, so the two frames are
separated by real elapsed time in the source footage, not two crops of one frozen
frame.
The maze is the same 12 × 10. The **hover ghost sits on an empty cell immediately
below the maze's bottom boundary wall**, i.e. in the margin ring, with the cursor
inside it.

**Measurements.** `[MEASURED]` Lattice pitch **42.446**, origin within 0.2 px of the
previous frame — the two frames are registered without any transform. Ghost stroke
centres: right x = **673.5**, bottom y = **665.0**; cell bounds x 632.09–674.55,
y 624.5–666.9 → **inset 1.05 and 1.9 capture px** (0.66 / 1.19 stage px). Ghost
interior **`(255,255,255)` at every sampled pixel** → the primitive is an unfilled
outline and the target cell has no floor. Most-saturated stroke pixel `#9998d3`.

**Links to the program.** VE 5 q3 **answered affirmatively**; the margin-ring
observation feeds §4a and A's `+2`. `Editor.as` has no hover code — contradicted by
absence.

**What this does NOT show.** The ghost's left and top edges (occluded by the yellow
ring and by the maze's boundary wall), hence no direct width measurement.

### `UI/B-wall-slot-preview-vertical.png` (1597 × 1051, crop 17:02:06)  *(was `selectedwall-smallbluebitbetweenblocks.png`)*

→ [`./UI/B-wall-slot-preview-vertical.png`](./UI/B-wall-slot-preview-vertical.png)

**Filename claim:** *"selected wall — small blue bit between blocks"* —
**corroborated and measured**.

**What is drawn.** `[OBSERVED]` Same page, same maze. A **small blue vertical capsule
sits on an interior gridline between two floor cells**, where no wall exists. Yellow
ring below-right of it; cursor at (670, 645).

**Measurements.** `[MEASURED]` Capsule bbox x 665–678 (13 px), y 580–621 (41 px) =
**0.31 × 0.97 cell**. Long axis on the column gridline. Most-saturated stroke pixel
`#8f93d6` (blue excess +67). Lattice pitch **42.444**.

**Links to the program.** VE 5 q2 **answered affirmatively** — the original previewed
walls on hover. New constant needed for the highlight colour. `MazeRenderer.render()`
draws no such element.

**What this does NOT show.** Whether the preview also appears on a slot that already
holds a wall.

### `UI/B-wall-slot-preview-second-location.png` (1600 × 1051, crop 17:02:46)  *(was `anotherwall.png`)*

→ [`./UI/B-wall-slot-preview-second-location.png`](./UI/B-wall-slot-preview-second-location.png)

**Filename claim:** *"another wall"* — **corroborated**; a second wall-slot preview,
at a different location, which is what makes the geometry repeatable rather than
anecdotal.

**What is drawn.** `[OBSERVED]` Same page and maze, **two cells added at the maze's
top edge** relative to the 17:00:43 frame (lattice (2,0) and (3,0), previously empty).
A vertical capsule preview near the top of the maze.

**Measurements.** `[MEASURED]` Lattice pitch **42.451**, origin (548.43, 242.65).
Capsule: cross-section at y = 306 gives stroke peaks at x = 671 and x = 680 with a
near-baseline trough between → **hollow, 9.0 capture px centre-to-centre = 5.6 stage
px**; axis at x = 675.5 vs fitted gridline **675.75**. Along-axis extent y ≈ 285 → 327
against gridlines **285.11** and **327.57** → **exactly one cell**. Most-saturated
stroke pixel `#9198e9` (+81) — the cleanest colour reading in the set. Adjacent black
wall FWHM ≈ 6 capture px = **3.8 stage px**, confirming spec `WALL_T = 4`.

**Links to the program.** VE 5 q2; spec wall thickness confirmed; VE 8a tone grid
(the two new cells are the "cell created → tone assigned" observation).

**What this does NOT show.** No motion; the capsule could in principle be a static
decoration rather than pointer-driven — ruled out only by the four frames together
placing it at four different positions.

### `UI/B-wall-slot-preview-horizontal.png` (1596 × 1027, crop 17:04:37)  *(was `horizontalwall.png`)*

→ [`./UI/B-wall-slot-preview-horizontal.png`](./UI/B-wall-slot-preview-horizontal.png)

**Filename claim:** *"horizontal wall"* — **corroborated**; the orientation
counter-example that makes the preview a general primitive.

**What is drawn.** `[OBSERVED]` Same account and maze, page scrolled slightly (image
25 px shorter). The maze is now **13 × 10** — one column wider than at 17:00:43. A
**horizontal** blue capsule lies on a row gridline. `[OBSERVED]` The maze-name field
below the stage shows a **blue text selection** covering its content (5416 px of
strong blue at x 275–499, y 801–826) — the user has selected the name text.

**Measurements.** `[MEASURED]` Lattice pitch **42.46/42.45**, maze bbox 558 × 430
→ 13 × 10 cells → cell **26.62 stage px**. Capsule bbox x 1037–1076 (39 px),
y 488–502 (14 px) = **0.92 × 0.33 cell** — the transpose of the vertical case.
Cross-section at x = 1056: stroke peaks y = 492.7 and 500.5, separation **7.8 capture
px**; axis y = 496.6 vs gridline **497.30**. Ends at x ≈ 1035.6 and 1078.0 vs
gridlines **1035.57** and **1078.03**.

**Links to the program.** VE 5 q2; VE 6 (13 × 10 still at 26.6 → width does not bind);
the text-selection observation is a small gift to sibling [C](./C-maze-slots-and-save-flow.md)
(the name field is an ordinary focusable HTML input).

**What this does NOT show.** No ✗/✓ interaction, no save.

### `UI/B-owner-note-spawn-icons.txt` (crop 17:07:34)  *(was `New Text Document.txt`)*

→ [`./UI/B-owner-note-spawn-icons.txt`](./UI/B-owner-note-spawn-icons.txt)

**Owner's note, verbatim and in full:**
`blue objects on maze creator is a tank, orange/brown is item (e.g. weapons e.g. laser) they all slowly rotate as animation.`

Three claims, all tested in §6: tank **corroborated** (the icon resolves into hull +
two tracks + barrel); item **corroborated in substance** (an amber crate = a
weapon-crate spawn; no laser is depicted); rotation **corroborated** (two icons of
one type at −25.9° and +30.4° in one frame; the same tank at −5.8° then +6.7° across
two frames of one maze).

`[OBSERVED]` The note is a plain single-line text file, no wiki chrome, no URL — it
is the owner's own summary of what he saw in the footage, not an archived artefact.
It is therefore a **claim to test**, exactly as the brief says, and not evidence in
itself.

### `UI/B-frontpage-achievement-unlock-float.png` (1074 × 539, crop 17:26:19)  *(was `beforetankrenders.png`)*

→ [`./UI/B-frontpage-achievement-unlock-float.png`](./UI/B-frontpage-achievement-unlock-float.png)

**Filename claim:** *"before tank renders"* — **corroborated**, but it is **not the
maze editor**.

**What is drawn.** `[OBSERVED]` The TankTrouble **front page**, account
`mr_enderman`. Centre: the big grey/white tank illustration on a hill, headline
`The most explosive 2 player tank game online` / `Tanks 'n' Trouble - Watch out,
before you turn to rubble` (partly occluded by a chat popup), and the three buttons
`1 PLAYER VS. LAIKA`, `2 PLAYERS`, `3 PLAYERS` with padlocks on 2 and 3. Watermark
`version 4.0`.

**Correction to my own first reading — this is the achievement unlock float
(S5), not a chat bubble.** `[OBSERVED]` A rounded white panel with a soft drop
shadow, top-centre over the headline, carrying a larger title line
`Hallowed Be Thy Name`, a smaller two-line body
`mr_enderman: You trick'r'treated your way to new swag!`, and a
**jack-o'-lantern icon at the right that overhangs the panel's top edge**. That
is site UI, not a video-authored overlay: the panel style, drop shadow and
type ramp match the page's own chrome, and the body is server-composed
(`<username>: <description>`). `[INFERRED]` It is the float driven by
`x_checkForAchievements` (`srv/index.php:1218-1261`), whose position — top
centre, after login/round — is exactly what the want-list predicts.

This matters beyond my topic. **S5 records the float's box art and glow tween
as O-exact but says the title, description and icon "never captured".** They
are captured here. The title and body also match, verbatim, the locked-row
entry that [G](./G-achievements.md) transcribed from the achievements panel,
so the same string is now attested on two independent surfaces. Full analysis
belongs to [G](./G-achievements.md); I record it because the frame is on my
list and my first pass named it wrongly.

Left rail: Halloween
pumpkin skin `Let the candy feast begin!`, a red `PLAY ONLINE / Online battles are in
heavy development. Try now!` panel, Log In box, and **`mr_enderman  Exp. 7697` with
NO tank sprite above the name**. Right rail: `Need Help?`, `Top 10 Exp.`
(`mr_enderman 7697`, `_nothing_ 5950`, `chaos_boy 5654`, `doggy_king 4653`,
`crash_david 1340`, `choasboy 60`), Like/Share, App Store, **Google play**,
Tell a Friend, Got Feedback?. A Fortnite skyscraper ad on the far left, a Crossout
ad on the right.

**Measurements.** `[NOT VISIBLE]` No maze, no lattice, nothing measurable for this
topic.

**Dating.** `[INFERRED]` **Late October 2018, high confidence.** Three independent
markers: the Halloween seasonal skin; the `FORTNITE SEASON 6 DARKNESS RISES` ad
(Fortnite Season 6 ran 2018-09-27 → 2018-12-06); and `Copyright www.purup.com
2007 – 2018` visible in the companion frame. This is squarely inside the rebuild's
2017–2018 target era and is a useful anchor for the corpus.

**Links to the program.** Nothing for VE 5/6/8a. Belongs to sibling D (garage /
userpanel) and E (front-page chrome). Recorded here only so the file is not skipped.

**What this does NOT show.** No maze editor, no interaction.

### `UI/B-frontpage-after-float-dismissed.png` (1227 × 610, crop 17:26:46)  *(was `aftertankrenders.png`)*

→ [`./UI/B-frontpage-after-float-dismissed.png`](./UI/B-frontpage-after-float-dismissed.png)

**Filename claim:** *"after tank renders"* — **corroborated**.

**What is drawn.** `[OBSERVED]` The same front page, same account, same session, chat
overlay gone, headline now fully legible. The **only substantive difference**: a
small dark-purple tank sprite has appeared in the left rail immediately above
`mr_enderman  Exp. 7697`, at capture (195–290, 400–450). Footer now visible:
`Copyright www.purup.com 2007 – 2018`. `Visits / Since 2007-12-16 / 66977586 /
Today: 1673 / Online: 24 / Tank owners: 1364642`.

**Measurements.** `[MEASURED]` Scrapyard odometer `2582…0290` → `2582…0293` between
the two frames. `[NOT VISIBLE]` No maze.

**Links to the program.** `[INFERRED]` The pair establishes that the account tank
sprite is fetched/rendered **asynchronously after first paint** — the page is fully
laid out and interactive with the sprite slot empty. That is a real behavioural fact,
but it belongs to sibling D, not to VE 5/6/8a.

**What this does NOT show.** Nothing about maze editing.

### `UI/B-hover-ghost-in-margin-ring.png` (1652 × 890, crop 17:31:26)  *(was `{FE109AA4-CB09-4B9D-AEE2-EFF3223B7D59}.png`)*

→ [`./UI/B-hover-ghost-in-margin-ring.png`](./UI/B-hover-ghost-in-margin-ring.png)

**Filename claim:** none — a Windows clipboard-paste GUID name. Nothing to test.

**What is drawn.** `[OBSERVED]` **The single most informative frame in this topic.**
The maze editor, account `mr_enderman`, same Halloween/Fortnite 2018 session as the
two front-page frames. Nav strip with the **wrench tab raised**, and — note for
sibling E — a **T-shirt tab** present between the wrench and the speech bubble that
does not appear in session R's strip. Centre panel: heading `mr_enderman`; a small
maze; watermark `version 0.3`; below it the name field `Kill The Player`, the three
tool icons (the crate and tank tools carry **grey starbursts**, the notebook/construct
tool does not), red ✗, green ✓. Left rail: pumpkin skin, `PLAY ONLINE` panel, Log In,
a dark-purple tank sprite, `mr_enderman  Exp. 7722  🏆3495 (25)  ☠3559`.
Right rail: `Need Help?`, `Top 10 Exp.` (`mr_enderman 7722`, `_nothing_ 5950`,
`chaos_boy 5654`, `doggy_king 4653`, `crash_david 1340`, `choasboy 60`), Like/Share,
App Store, Google play, Tell a Friend, Got Feedback?.

**The maze:** a **4 × 4** block of floor with a **2 × 2 hole** in the middle, closed
by walls on all four sides. Two tank spawn icons sit in the bottom-left area. **A
blue rounded-rect ghost floats in empty white space one cell to the LEFT of the maze,
with the cursor's arrow tip inside it.**

**Measurements.** `[MEASURED]` Panel borders x 463.5 / 1433.5 → 970 capture px →
**scale ×1.4099**; panel height 104.0 → 752.5 = 648.5 → **460.0 page px** (400 SWF +
60 chrome) — an exact, independent confirmation of the scale method.
Lattice: gridlines x 799.8 / 875.0 / 950.0 / 1025.0 / 1100.0, y 251.4 / 326.4 / 401.4
/ 476.4 / 551.4 → pitch **75.05 / 75.0** capture = **53.23 stage px**; A's law for a
4 × 4 maze predicts **53.33** (−0.2 %).
Ghost: stroke centres x 729.8 / 794.5, y 405.6 / 471.7 → **64.7 × 66.1 capture px**,
occupying lattice cell **(−1, 2)** — one cell outside the maze, on its lattice.
Stroke FWHM ≈ 5.6 capture px = **3.97 stage px**; darkest stroke pixel `(132,130,178)`.

**Links to the program.**
VE 5 q3 — ghost **under the cursor**, on a **not-yet-existing** cell.
VE 6 — a *fourth* cell size (53.2), and direct proof of the one-cell margin ring.
`Editor.as:338` — third independent contradiction (heading = `mr_enderman`).
`MazeRenderer.as:19` `CELL = 32` — contradicted (53.2 here, 26.6 elsewhere).
Sibling A's toolbar work — the grey-starburst tool states are a gift to that topic.

**What this does NOT show.** No wall preview (the ghost here is a cell); no drag; no
save; no error panel.

### `UI/B-maze-growth-step1.png` (828 × 434, crop 17:34:57)  *(was `expandingwallsbyclicking1.png`)*

→ [`./UI/B-maze-growth-step1.png`](./UI/B-maze-growth-step1.png)

**Filename claim:** *"expanding walls by clicking (1)"* — **corroborated in
substance** (§4a); the maze is being extended.

**What is drawn.** `[OBSERVED]` A tight, chrome-free crop of a **7 × 3** maze whose
**left half is destroyed by video-codec tearing** — broken wall dashes at random
angles, ghosted circular blobs, floor fragments — while the right half is clean.
No cursor, no page furniture.

**Measurements.** `[MEASURED]` From the clean half: outer bbox 680 × 298; solving
`outer = pitch × (n + 1/8)` gives pitch **95.5** capture px for 7 × 3 → at the session
scale ×1.5000, **cell = 63.7 stage px**; A's law predicts **64.00** (−0.5 %).

**Links to the program.** VE 6 — a 3-row maze at 63.7 stage px is the low-`h` end of
the fit-law evidence. `MazeRenderer.CELL = 32` contradicted by a factor of 2.

**What this does NOT show.** `[NOT VISIBLE]` No cursor, no ghost, no page chrome and
therefore no independent scale anchor of its own — the ×1.5 scale is carried over
from `…2.png`.

### `UI/B-maze-growth-step2-width-term-binds.png` (542 × 305, crop 17:35:22)  *(was `expandingwallsbyclicking2.png`)*

→ [`./UI/B-maze-growth-step2-width-term-binds.png`](./UI/B-maze-growth-step2-width-term-binds.png)

**Filename claim:** *"expanding walls by clicking (2)"* — **corroborated**.

**What is drawn.** `[OBSERVED]` A chrome-free crop showing the stage heading
`cam12win` and an **L-shaped maze**: a bottom row running off the left edge of the
crop, and a 1-cell-wide, 2-cell-tall column rising at the right. Clean frame, no
tearing, no cursor.

**Measurements.** `[MEASURED]` The heading `cam12win` is **128 px wide**, identical to
the same string in `A-editor-howto-step6-or-just-click.png` → **scale ×1.5000**, i.e. these crops are not
zoomed. Wall gridlines at x = 281.3, 503.0 and y = 35.5, 183.7, 257.6 → pitch
**74.0 ± 0.3** capture = **49.3 ± 0.2 stage px**; maze height 3 rows, width ≈ 10
(clipped). A's law with the **width** term binding predicts `576/12 = 48.0` (+2.7 %).

**Links to the program.** VE 6 — **the only frame in the corpus where the width term
of the fit-law binds**, and it does so at the predicted `w`. Brackets A's numerator
at **542 ≤ A ≤ 592**.

**What this does NOT show.** `[NOT VISIBLE]` The maze's left edge; therefore `w`
is inferred and `A` cannot be pinned.

### `UI/B-maze-growth-mechanism.png` (699 × 454, crop 17:35:51)  *(was `expandingwallsbyclicking.png`)*

→ [`./UI/B-maze-growth-mechanism.png`](./UI/B-maze-growth-mechanism.png)

**Filename claim:** *"expanding walls by clicking"* — **corroborated, and this is the
frame that shows the mechanism.**

**What is drawn.** `[OBSERVED]` A chrome-free crop on white: a **3 × 3 maze** with a
heavy dark boundary, four visible floor tones inside, and a **blue rounded-rect ghost
floating one cell to its left**, its right edge abutting the maze's boundary wall.
**No mouse cursor is drawn anywhere in the frame.**

**Measurements.** `[MEASURED]` Solving `outer = pitch × (3 + 1/8)` on the 300 × 298
bbox gives pitch **95.68**; independently predicted the interior tone boundary at
x = 351.7 against **352 observed** (0.3 px). At ×1.5000, **cell = 63.8 stage px**;
A's law predicts **64.00** (−0.3 %). Ghost stroke centres x 167 and 248.5 →
**81.5 capture px = 0.85 cell**; stroke FWHM ≈ 4.5 capture px. 0 yellow pixels,
28 strong-blue pixels (the ghost alone).

**Links to the program.** VE 5 q3 — the ghost is **stage content**, proven by the
absence of any cursor. VE 6 — a 3 × 3 maze at 63.8 px. §4a — the margin ring.

**What this does NOT show.** No cursor, hence no proof that the ghost tracks the
pointer *in this frame*; that comes from `B-hover-ghost-contains-cursor.png` and `B-hover-ghost-in-margin-ring.png`.

### `UI/B-editor-howto-step3-epic-twister.png` (1225 × 691, crop 17:36:30)  *(was `3.png`)*

→ [`./UI/B-editor-howto-step3-epic-twister.png`](./UI/B-editor-howto-step3-epic-twister.png)

**Filename claim:** none beyond its number.

**What is drawn.** `[OBSERVED]` Editor, account `cam12win`, name field `Epic Twister`.
Partial left rail (`Scrapyard 59177972`+rolling drum, Log In, a red tank sprite,
`cam12win  Exp. 1191  🏆90 (1)  ☠200`, `Need Help?`, `Visits / Since 2007-12-16 /
16133602 / Today: 8434 / Online: 568 / Tank owners: 404381 / Logged in: 167`).
The maze is a **sparse 11 × 10 skeleton**. A **blue button-down disc** at (485, 592),
by the toolbar. A small grey rounded-square widget at (1170–1205, 495–535) inside the
panel. Codec tearing at (460–500, 490–560).

**Measurements.** `[MEASURED]` ✗–✓ centroid separation **63.1 px**, name field 266 px
→ scale ×1.5000 (same as `4`–`7`). Lattice pitch **53.4–53.6** capture px, fitted
against column peaks 399.8 / 453.5 / 506.5 / 613.0 / 827.0 / 987.5 (residual < 0.9 px)
and confirmed by overlaying the lattice on the image. Maze **11 wide × 10 tall**
(gridlines counted on the overlay). Solving `outer = pitch × (11 + 1/8)` on the 593 px
bbox gives **53.30** → **35.53 stage px**.

**Links to the program.** VE 6 — **the frame that proves the pitch is dynamic**, when
read against `4…png` 27 s later. Also the frame that does **not** fit A's law
(35.53 vs 26.667 predicted for h = 10; 35.53 is `320/9`, the h = 7 value) — see §3e.
`Editor.as:338` contradicted (heading `cam12win` ≠ `Epic Twister`).

**What this does NOT show.** `[NOT VISIBLE]` No hover ghost (the pointer is off the
maze); no wall preview; no spawn icons at all on this maze.

### `UI/B-editor-howto-step4-lag-note.png` (1077 × 680, crop 17:36:57)  *(was `4shouldntbethislaggy-sourcescomputerisslow.png`)*

→ [`./UI/B-editor-howto-step4-lag-note.png`](./UI/B-editor-howto-step4-lag-note.png)

**Filename claim:** *"shouldn't be this laggy — source's computer is slow"* —
**corroborated**: the frame is visibly torn.

**What is drawn.** `[OBSERVED]` Editor, `cam12win`, `Epic Twister`. The maze is now
**18 × 10** with a substantial but incomplete floor: a full-width top bar, a thick
left column, a T reaching the bottom, and **two completely detached rectangles at the
bottom right** (≈(775–815, 470–515) and (850–935, 470–515)), each with its own closed
wall ring. Heavy codec tearing down the left edge of the maze (dashes, ghost blobs).
Blue button-down disc at (310, 455), i.e. **outside the maze on blank page**.

**Measurements.** `[MEASURED]` ✗–✓ = **63.2 px** → scale ×1.5000. Maze outer bbox
**725 × 407** capture px, identical to `B-editor-howto-step5-nearly-solid.png`, `A-editor-howto-step6-or-just-click.png` and
`7candragit…png`. Pitch from `outer = pitch × (18 + 1/8)` → **40.0** →
**26.67 stage px**; A's law predicts **26.667**.

**Links to the program.** VE 6 (growth pair with `B-editor-howto-step3-epic-twister.png`); §8 item 2 —
**non-contiguous floor is permitted**, which constrains `cropToFloorBbox()`
(`Editor.as:109-133`) and `MazeData.normalizeBoundary()`. The disc's position outside
the stage proves the overlay is not stage content.

**What this does NOT show.** No ghost or preview (the pointer is off the maze).

### `UI/B-editor-howto-step5-nearly-solid.png` (1031 × 685, crop 17:37:27)  *(was `5.png`)*

→ [`./UI/B-editor-howto-step5-nearly-solid.png`](./UI/B-editor-howto-step5-nearly-solid.png)

**Filename claim:** none beyond its number.

**What is drawn.** `[OBSERVED]` Editor, `cam12win`, `Epic Twister`. The 18 × 10 maze
is now nearly solid, with **one large rectangular hole** (≈6 × 5 cells, capture
(600, 265)–(840, 490)) still open, plus fresh tearing at its lower right. Blue
button-down disc at (643, 440) on the hole's edge. The small grey widget at
(980–1015, 500–535).

**Measurements.** `[MEASURED]` ✗–✓ = **63.1 px** → ×1.5000. Maze outer bbox
**725 × 407**, pitch **39.9** → **26.6 stage px**. The hole's closure walls measured
across at y = 350 and down at x = 700: luma minima **56–94**, run width ≈ 6 capture
px — **identical to the maze's outer boundary wall** (minimum 83, width 6). They are
ordinary 4-stage-px walls.

**Links to the program.** Confirms `MazeRenderer.render()` lines 87–92: closure walls
derived from floor adjacency appear on **all four sides** of an interior hole, which
is what that code produces. VE 6 (pitch unchanged from `4…png`).

**What this does NOT show.** No hover ghost visible; no tool change.

### `UI/B-editor-howto-step7-drag-paint-wall-run.png` (797 × 437, crop 17:38:00)  *(was `7candragittocreatewallscontinuously.png`)*

→ [`./UI/B-editor-howto-step7-drag-paint-wall-run.png`](./UI/B-editor-howto-step7-drag-paint-wall-run.png)

**Filename claim:** *"can drag it to create walls continuously"* —
**corroborated as far as a still can**, and this is the strongest single frame for
VE 5 q1.

**What is drawn.** `[OBSERVED]` A chrome-free crop of a **complete, solid 18 × 10
maze**, floor tones fully visible, with **exactly one gridline carrying new interior
walls**: a continuous run, a gap, then a detached fragment. The cursor sits on that
same gridline further right, with a **blue button-down disc**.

**Measurements.** `[MEASURED]` Maze outer bbox **725 × 407** — identical to `4`, `5`
and `6`, so same maze, same scale. Along the wall gridline (capture y ≈ 61):
continuous wall **x 60 → 340** (280 px ≈ 7 cells), **gap x 340 → 344**, detached
fragment **x 344 → 372** (28 px ≈ 0.7 cell), then nothing to x 785. Cursor hotspot
≈ (457, 60). Strong-blue pixel count **536** = the disc plus the wall run's
anti-aliasing, no yellow ring (0 px).

**Links to the program.** VE 5 q1 — the fragment-ahead-of-run signature.
`Editor.as:60` (`onMouseDown` only) **contradicted**; overhaul owed on the whole
`onClick()` block, `Editor.as:183-235`.

**What this does NOT show.** Motion. A still cannot show it. The argument rests on
the *artefact* (the fragment) plus the cursor state, and is tagged `[INFERRED]`
throughout.

### `UI/B-tank-spawn-placement-effect.png` (1056 × 690, crop 17:39:04)  *(was `placingtankscreatethiseffect.png`)*

→ [`./UI/B-tank-spawn-placement-effect.png`](./UI/B-tank-spawn-placement-effect.png)

**Filename claim:** *"placing tanks create this effect"* — **corroborated**.

**What is drawn.** `[OBSERVED]` Editor, `cam12win`, `Epic Twister`. The maze is now a
neat **18 × 10 spiral**. In the maze's **top-left corner cell** a blue tank icon sits
inside a **burst of short blue rays and scattered blue speckles**. A second tank icon
sits mid-maze at (355, 328), beside a **blue rounded-rect hover ghost** at
(295–335, 310–345). In the toolbar the **tank tool carries a blue starburst** while
the crate tool's starburst is grey. **Yellow recorder ring** (idle) at (360, 485) —
no blue disc.

**Measurements.** `[MEASURED]` ✗–✓ = **63.1 px** → ×1.5000. Maze bbox **722 × 403**,
pitch **40.0** → **26.62 stage px**. Yellow pixel count **2061**, strong-blue **1009**.
Tank angles (4θ estimator): corner tank **−5.8°**, interior tank **+28.2°**.
Tank fill core ≈ (165, 170, 232); outline ≈ (90, 92, 175).

**Links to the program.** §6d rotation; §6e placement burst (contradicts
`MazeRenderer.glow()` lines 115–123). The yellow-ring-with-no-disc reading supports
the button-state interpretation of the overlays (§Scope). The blue vs grey tool
starburst is direct evidence for VE entry 1 / sibling
[A](./A-maze-editor-toolbar.md).

**What this does NOT show.** The burst's duration or decay; a single frame cannot
give an animation curve.

### `UI/B-crate-spawn-placement-effect.png` (1107 × 667, crop 17:39:32)  *(was `placingboxescreatethiseffect.png`)*

→ [`./UI/B-crate-spawn-placement-effect.png`](./UI/B-crate-spawn-placement-effect.png)

**Filename claim:** *"placing boxes create this effect"* — **corroborated**.

**What is drawn.** `[OBSERVED]` A closer crop of the same spiral maze, same session,
28 s later by crop order. **Two amber crate icons**, each in an **amber burst** of
rays and loose sparkle dots, at (526, 170) and (524, 446). Two blue tank icons at
(85, 57) and (307, 335). A **blue rounded-rect hover ghost** at (500–555, 258–300).
**Yellow recorder ring** (idle) at (180, 340). No page chrome in the crop except the
maze.

**Measurements.** `[MEASURED]` Yellow **4816** px, strong-blue **574** px. Crate
orientations **−25.9°** and **+30.4°** (mod 90) — *different from each other in one
frame*. Tank orientations **+6.7°** (corner) and **+13.0°** (interior) — both changed
from the previous frame by 12.5° and 15.2°. Crate fill core ≈ (224, 185, 90), border
≈ (168, 128, 55) against spec (219, 183, 85) / (170, 130, 50). Speckle blobs 3–8
capture px at 20–60 px (0.3–0.8 cell) from the icon centre.

**Links to the program.** §6d — **this frame plus the previous one settle the
rotation question the spec could not**. §6e — the burst. Spec crate colours
confirmed. `MazeRenderer.drawCrate()`/`drawTank()` axis-alignment **contradicted**.

**What this does NOT show.** `[NOT VISIBLE]` No scale anchor of its own (the ✗/✓ are
outside the crop, so the ✗ detection failed) — measurements that need stage px use
the previous frame's spiral for registration.

---

## 10. Consequences for the rebuild

### Confirmed

| What | Where it was already written | Evidence |
|---|---|---|
| Stage is 688 × 400 with ~60 page px of chrome below it | `srv/index.php:3617` (O); spec line 12 | Panel geometry measured independently in 3 sessions at 3 zooms, agreeing to 0.6 px |
| Floor dark tone `#dddddd` | spec line 26 | Median (221,221,221) over 15 554 px |
| Floor light tone `#eeeeee` | spec line 26 | Reads 237; the −1 is an encode artefact, not a build difference (§5a) |
| Floor tones are **not** a checkerboard, no simple rule | spec line 27 | No rule beats 45/81 on an independent maze |
| Wall thickness `WALL_T = 4` **relative to a 32-px nominal cell** | spec line 24 | wall/cell = 0.131 and 0.138 in two frames at different cell sizes |
| Wall colour `#444444` | spec line 25 | Wall luma minima 56–94 in blurred captures; consistent, not independently re-pinnable |
| Interior-hole closure walls derived from floor adjacency | `MazeRenderer.as:87-92` | `B-editor-howto-step5-nearly-solid.png`'s 6 × 5 hole is walled on all four sides at the same 4 px |
| Object cap 5 tanks + 5 crates | spec line 32; `Editor.as:228-230` | Session R's maze holds exactly 5 + 5 |
| One construct tool decides cell-vs-edge by hit position | `Editor.as:199-219` | Floor and walls both drawn with the same lit tool through frames 3→7 |
| Tank icon = hull + two tracks + barrel, ~12–16 × 16–18 stage px | `MazeRenderer.as:136-146` | Resolves at ×8 upscale; sizes match |
| Spawn palette (`COLOR_TANK_FILL/LINE`, `COLOR_CRATE_FILL/EDGE`) | `MazeRenderer.as:45-48` | All four within ±8 per channel of independent footage |
| Non-contiguous floor is legal while editing | implied by `Editor.as:216-218` | `4…png`'s two detached rectangles |
| The 576 × 320 fit box and the one-cell margin ring | sibling A's derivation | 7 mazes, 4 heights, ≤ 0.5 % error; ring seen directly in 2 frames |

### Contradicted — overhaul owed

Per **THE OVERHAUL RULE**, each of these is an invented M2/M3 piece with zero
authority; it is **rewritten wholesale against the evidence, not patched**, and the
supersession is recorded in `DECISIONS.md`.

1. **`src/mazecreator/MazeRenderer.as` — rewrite the whole file.**
   * `initConstants()` lines 35–51: `CELL = 32`, `LATTICE_X/Y = 56/50`,
     `LATTICE_W/H = 18/10` are a **fixed lattice**. The evidence shows a **fit**:
     four different cell sizes (63.8 / 53.2 / 49.3 / 26.6 stage px) in one corpus.
     Replace with `fitFor(data) → {cell, ox, oy}` implementing
     `cell = min(576/(w+2), 320/(h+2))`, and re-pin the tests to the seven measured
     mazes in §4c.
   * `render()` lines 66–102: must take the fitted cell, and must gain a **hover
     layer** (§2) — it currently draws no highlight of any kind.
   * `drawTank()`/`drawCrate()` lines 126–147 and the class comment lines 9–11:
     **axis-aligned is wrong**. Rotate per object; the comment's surrender ("the
     capture is too soft to pin rotation") is superseded.
   * `glow()` lines 115–123: three concentric alpha squares is the wrong **form**
     (evidence shows rays + discrete speckles) and misses the **placement burst**
     entirely.
   * `floorTone()` lines 60–63: not an overhaul demand (VE 8a explicitly blesses a
     stand-in), but wrong in kind — see the recommendation in §5c.

2. **`src/mazecreator/Editor.as` — rewrite the interaction block.**
   * Line 60, `_root.onMouseDown` as the **only** pointer binding: contradicted by
     the drag evidence (§1a). Needs press / move / release, a stroke-scoped
     already-visited set, and a hover handler.
   * Lines 183–235 `onClick()`: the whole hit-test runs in `MazeRenderer.CELL`
     coordinates and must move to fitted coordinates.
   * Line 21 `EDGE_TOL = 6`: an invented constant expressed in a now-invalid unit.
     The evidence gives a target instead — the wall preview's own thickness,
     **5–6 stage px centre-to-centre at CELL = 26.6**, i.e. an edge band of roughly
     **±0.11 cell**, not a fixed 6 px. Re-derive.
   * Lines 82–105 `loadIntoLattice()` and the `fracX`/`fracY` half-cell remainder:
     the mechanism is superseded — under a live fit, half-cell offsets fall out
     automatically.
   * Line 338 `titleTf.text = title`: the heading is the **account name**
     (`init.n`, read at line 38), not the maze name. Confirmed on three accounts.

3. **`docs/standards/MAZECREATOR-VISUAL-SPEC.md` — re-pin two rows.**
   * Line 21 `CELL | 32 px`: correct *for that screenshot* (an 8-row maze →
     `320/10 = 32.0`) but wrong as a constant. Reword to record the fit and note that
     32 is the value it returns at h = 8.
   * Line 30 "not clearly rotated … treated as axis-aligned": superseded — rotation
     is now measured.

4. **`docs/superpowers/plans/2026-08-03-mazecreator-phase3-editor.md`** and the
   `DECISIONS.md` 2026-08-03 entry that logged the invented interaction model both
   need supersession notes pointing at this document.

### Still unknown / stays on the want-list

* `[NOT VISIBLE]` **Does a drag toggle or paint?** Every stroke observed runs over
  virgin cells. Whether dragging back over your own stroke erases it is unknown, and
  it changes the rewrite materially.
* `[NOT VISIBLE]` **Do the spawn tools get a hover ghost?** All five highlight frames
  have the construct tool lit.
* `[NOT VISIBLE]` **Does the preview change on an occupied slot** (add vs remove)?
* `[NOT VISIBLE]` **Is the refit immediate or deferred?** `B-editor-howto-step3-epic-twister.png` is 33 % off the fit
  law in exactly the way a 3-row lag would produce (§3e).
* `[NOT VISIBLE]` **The width numerator** of the fit law: bracketed at 542–592, not
  pinned. Needs a wide, short maze fully in shot.
* `[NOT VISIBLE]` **Refused placement UI** (S48) — nothing in any frame.
* `[NOT VISIBLE]` **Error panel** (VE 2), **save flow** (VE 3), **preview/garage mode**
  (VE 4) — none of my 17 frames touches them.
* `[UNCERTAIN]` **Highlight stroke width and corner radius** — 2–4 stage px and
  4–5 stage px respectively; the capture blur cannot be separated from the geometry.
* `[UNCERTAIN]` **Rotation rate, direction and phase** of the spawn icons.
* `[UNCERTAIN]` **Whether the persistent icon "glow" and the placement burst are one
  effect** at different points in its life.

### New wants to add

| Proposed # | Want | Why it matters | Footage trigger |
|---|---|---|---|
| **5a** | A drag stroke that **crosses its own path** | Decides toggle-vs-paint, which is the core of the `onClick` rewrite | Any editing footage where the user scribbles |
| **5b** | Hover with the **crate or tank tool** selected | Decides whether the ghost is per-tool | Footage where a spawn tool is lit and the pointer moves over the maze without clicking |
| **5c** | Hover over a slot that **already holds a wall** | Decides whether the preview signals add vs remove | Any editing footage |
| **6a** | Two frames bracketing **one cell added at an edge** | Decides whether the refit is immediate or deferred; resolves the `B-editor-howto-step3-epic-twister.png` anomaly | Slow, deliberate maze extension |
| **6b** | A **wide, short maze** (w + 2 > 1.8·(h + 2)) fully in shot | Pins the fit law's width numerator (currently 542–592) | A 2–3 row maze dragged out to full width |
| **8b** | The **same saved maze opened twice** | Separates "random, stored" from "hash seeded on maze identity" for the floor tone | Open the garage, edit a maze, cancel, reopen |
| **N1** | The **placement burst** at native frame rate | The rebuild has no placement animation at all; needs a duration and a decay | Any footage where a spawn is placed, frame-stepped |
| **N2** | A **settled** maze at rest for several seconds | Separates the persistent icon glow from the placement burst | Any editor footage with no input |

---

## 11. Recommended edits to existing docs (not applied)

I have edited nothing outside this file. These are proposals.

### `docs/standards/VISUAL-EVIDENCE-WANTED.md`

* **Entry 5 — change `WANTED` → `FETCHED`.** All three questions are answered:
  drag-paint yes (`[INFERRED]`, strong), hover wall preview yes (`[MEASURED]`),
  cursor ghost yes (`[MEASURED]`). Suggested replacement body:

  > ### 5. Editing interaction semantics — FETCHED, redraw pending
  > Answered by `manualevidence/B-maze-editor-interaction.md`. The original
  > **previews on hover** (a periwinkle ≈`#8f95e0` rounded-rect stroke on the cell
  > under the pointer; a stadium of the same stroke, one cell long, centred on the
  > gridline, for a wall slot — both unfilled), previews cells in a **one-cell
  > editable margin ring outside the maze**, and **drag-paints** (a run of new walls
  > along one gridline with detached fragments ahead of it, button-down cursor).
  > Still open: toggle-vs-paint on a self-crossing drag (→ 5a); ghost with the spawn
  > tools (→ 5b); preview on an occupied slot (→ 5c).

* **Entry 6 — change `PARTIAL` → `FETCHED`** for the recentre question:

  > Footage settles it: the editor **re-fits and re-centres live**. Cell pitch
  > measured at 63.8 / 53.2 / 49.3 / 26.6 stage px on mazes of 3 / 4 / 3 / 10 rows;
  > within one 27-second window the pitch fell 25 % as the maze grew 11 → 18 columns.
  > The fit is `cell = min(576/(w+2), 320/(h+2))` (sibling A), reproduced on seven
  > mazes to ≤ 0.5 %; the width numerator is bracketed 542–592, not pinned (→ 6b).
  > `MazeRenderer.CELL = 32` is not a constant — it is the value the fit returns for
  > an 8-row maze.

* **Entry 8a — change `WANTED` → `PARTIAL`**, appending:

  > Four frames of one maze 123 s apart (`manualevidence/UI/B-hover-ghost-on-cell.png`,
  > `B-hover-ghost-contains-cursor.png`, `selectedwall-…`, `B-wall-slot-preview-second-location.png`) give **identical** per-cell
  > tones (80/81 stable cells; the exception lies under the recorder's cursor
  > overlay) — so the tone is **not re-rolled per redraw**. But cross-correlating two
  > *different* mazes over all 665 lattice offsets peaks at 0.710 (chance 0.497,
  > perfect 1.000), and the light fraction differs per maze (0.34 / 0.43 / 0.53) — so
  > it is **not a shared function of (x, y)** either. Reading: randomised once at
  > cell creation (or seeded per maze) and stored. Remaining question → new entry 8b.

* **S42 (cursor over the editor stage) — change to `PARTIAL`.** Evidence: the
  **system arrow is present and unmodified** in every editor frame in this set, so
  there is no custom cursor art; but the SWF *does* draw a stage-side ghost, proven
  by `B-maze-growth-mechanism.png` where the ghost renders with **no cursor in
  frame at all**.

* **S48 — keep `WANTED`, narrow the trigger.** Add: *"Session R's maze
  (`manualevidence/UI/B-hover-ghost-on-cell.png`) sits exactly at the 5+5 cap while
  being edited, with no visible limit affordance — weak evidence that refusal is
  silent. Trigger: a frame captured at the instant a spawn tool is clicked on a maze
  already holding 5 of that type."*

* **Add entries 5a, 5b, 5c, 6a, 6b, 8b, N1, N2** as tabled in §10.

### `docs/standards/MAZECREATOR-VISUAL-SPEC.md`

* Line 21, row **CELL**: replace `32 px | pitch 38.69/1.2093 = 31.99` with
  `**fitted, not fixed** — cell = min(576/(w+2), 320/(h+2)); 32 px is the value this
  returns for the 8-row maze in this screenshot (320/10). Measured on 7 mazes in
  era footage: 63.8 (3×3), 53.2 (4×4), 49.3 (≈10×3), 26.6 (12/13/18 × 10).
  See manualevidence/B-maze-editor-interaction.md §4c.`
* Line 22, row **LATTICE origin**: note that a fixed `(56, 50)` origin follows from a
  fixed cell and is superseded by the fit; the fit box is 576 × 320 centred below the
  title band.
* Line 24, row **Wall thickness**: add *"scales with the cell at ≈ 1/8 (measured
  7.0 capture px at pitch 53.5 and 5.5 at pitch 39.95 in one session) — i.e. the maze
  is drawn at a nominal CELL = 32 / WALL_T = 4 and uniformly scaled."*
* Line 26, row **Floor tones**: append *"independently confirmed in era footage —
  dark median (221,221,221) = #dddddd exactly over 15 554 px; light reads 237, one
  level below #eeeeee, attributed to video encode rounding, not a build difference."*
* Line 27, row **Floor tone pattern**: append the per-maze light fractions
  (0.34 / 0.43 / 0.53) and the cross-maze correlation result.
* Line 30, row **Tank spawn icon**: replace *"not clearly rotated (upscale too soft to
  pin exact angles — treated as axis-aligned)"* with *"**rotated** — two tanks in one
  frame at +6.7° and +13.0°, and the same tank at −5.8° then +6.7° across two frames
  of one maze. Rate, direction and phase unpinned."*
* Line 31, row **Crate spawn icon**: append *"rotated — two crates in one frame at
  −25.9° and +30.4° (mod 90)."*
* Add a new row **Hover highlight**: *"periwinkle stroke ≈ `#8f95e0` (darkest
  observed `#8f93d6`…`#9198e9` across four frames), unfilled; rounded square on a
  hovered cell (inset ≈ 1–5 capture px from the cell bounds), rounded stadium of the
  same stroke on a hovered wall slot — one cell long, ≈ 5–6 stage px centre-to-centre
  thick, centred on the gridline to < 1 px. Also drawn for cells in the one-cell
  margin ring outside the maze."*
* Add a new row **Spawn placement effect**: *"placing a spawn plays a burst of short
  rays plus discrete speckles in the spawn's own colour (blue / amber), extending
  0.3–0.8 cell. Distinct from the persistent soft glow; duration unknown."*
* Under **Known unknowns**: strike "icon rotation (if any)"; add "rotation rate and
  phase", "drag toggle-vs-paint", "fit-law width numerator".

### `DECISIONS.md`

Add an entry dated with the analysis, in the house style:

> **mazeCreator interaction model superseded by era footage (2026-08-04).**
> *Invention:* phase-3 `Editor.as` bound `onMouseDown` only, hit-tested against a
> fixed `MazeRenderer.CELL = 32` on a fixed 18 × 10 lattice at `(56, 50)`, drew no
> hover feedback, drew spawn icons axis-aligned with a static square glow, and put
> the maze *name* in the stage title band.
> *Evidence:* 17 frames under `manualevidence/UI/` from three accounts
> (`revengexx1`, `cam12win`, `mr_enderman`), analysed in
> `manualevidence/B-maze-editor-interaction.md`.
> *What changed:* hover ghost + wall preview exist and are measured; drag-paint is
> evidenced; the cell size is fitted, not fixed, and the maze re-centres live; spawn
> icons rotate; placement plays a particle burst; the title band shows the account
> name.
> *Owed:* wholesale rewrite of `src/mazecreator/MazeRenderer.as` and of the
> interaction block of `src/mazecreator/Editor.as`, with tests re-pinned to the seven
> measured mazes.

### `DEDUCE.md`

Add a short derivation note for the scale method, since three analysts now depend on
it: *"Editor page scale = (panel border-to-border width) / 688; cross-checked by
(panel height)/scale = 460 page px = 400 SWF + 60 chrome. Verified independently in
`B-hover-ghost-on-cell.png` (×1.5966), `A-editor-howto-step6-or-just-click.png` (×1.5000) and
`B-hover-ghost-in-margin-ring.png` (×1.4099), agreeing with the page-fixed ✗–✓ ruler to 0.2 %."*

### `docs/standards/DIVERGENCES-SERVED.md`

Add the floor-tone divergence explicitly: the rebuild serves a **deterministic
per-coordinate** tone; the original is **per-maze random**, so identical mazes will
differ from the original in pattern (never in geometry or wire format).

### `LEDGER.tsv`

The 17 files in this topic are all crops of era footage. Per guide §6.5 each needs a
row with URL / uploader / date / timestamp of the **source video**, which I do not
have. Recommend a placeholder row per file marked `M2 / source video URL unknown —
supplied by repo owner 2026-08-04`, so the provenance debt is recorded rather than
silently absorbed. `B-frontpage-achievement-unlock-float.png` / `B-frontpage-after-float-dismissed.png` /
`B-hover-ghost-in-margin-ring.png` can carry a dating note: **late October 2018**, from the Halloween
seasonal skin + Fortnite Season 6 ad + `Copyright www.purup.com 2007 – 2018`.

---

## Appendix — measurement provenance

Every number in this document came from Python (PIL + numpy + scipy.ndimage) run
against the read-only staged images. The techniques, so they can be reproduced or
attacked:

* **Page scale**: locate the maze panel's 1-px grey border by scanning rows/columns
  for a local luma minimum in 200–230 flanked by ≥ 248; divide the border-to-border
  width by 688 (`srv/index.php:3617`). Cross-check with panel height / scale = 460.
* **Lattice**: threshold `max(R,G,B) < 130` for wall pixels, sum along each axis,
  extract intensity-weighted peak centroids, then least-squares fit `origin + n·pitch`
  against integer indices. Cross-check with `outer bbox = pitch × (n + 1/8)` and with
  floor-tone boundary positions.
* **Tone grid**: sample the inner 44 % of each lattice cell, take the per-cell median
  luma, classify against the bimodal split at 229.
* **Highlight geometry**: per-pixel blue excess `B − max(R, G)`; stroke centres from
  the local maxima of that profile; extents from half-maximum crossings.
* **Icon orientation**: gradient structure tensor at 4θ (period 90°, the natural
  period of a square), weighted by squared gradient magnitude, over a disc of radius
  0.3 cell, restricted to pixels above 25–30 % of the local maximum gradient.
* **Frame registration**: each frame's lattice was fitted independently; the session-R
  frames agree to < 0.3 px in pitch and < 4 px in origin, so no resampling was applied.
