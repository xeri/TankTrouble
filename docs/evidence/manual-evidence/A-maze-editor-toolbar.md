# Visual evidence — mazeCreator toolbar, tool icons and title typography

> Analysis of 11 evidence files under `manualevidence/`.
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)

---

## Scope and provenance

This document covers the **page-side control row under the 688×400 SWF stage**
(`userpanelMazeCreatorControls-`, `userpanelMazeTitle-`, the three tool `<img>`s,
`userpanelCancelMaze-`, `userpanelSaveMaze-`, `userpanelAcceptMaze-`) and the
**two pieces of in-stage typography** (the centred grey heading and the
`version 0.3` watermark). It does not cover maze geometry, floor tones, cell
highlights or spawn-icon artwork inside the maze except where those were needed
to derive a scale.

### The frames are three different sessions, three different accounts

The centred heading differs between frames and never matches the maze-name field:

| Session | Centred heading | Maze-name field | Frames |
|---|---|---|---|
| A | `revengexx1` | `One Path to Destruction` | `A-toolbar-confirm-click-midfade.png` |
| B | `mr_enderman` | `Kill The Player` | `A-editor-panel-primary-source-hq.png`, `A-editor-panel-kill-the-player.png`, `A-toolbar-three-tool-icons-visible.png`, `A-editor-panel-highlight-outside-maze.png` (+3 maze-only crops) |
| C | `cam12win` | `Epic Twister` | `A-editor-howto-step6-or-just-click.png`, `A-editor-preview-mode-lone-tick.png` |
| D | *(not in frame)* | `Run Around The WORLD` | `A-toolbar-row-crop-run-around-the-world.png` |

`[MEASURED]` The three sessions render the same control row at three different
widths for the title input (156.0 / 176.4 / 182.3 CSS px — see the geometry
table) while the tool icons stay 42–46 CSS px in all of them. Different browsers
sizing the same `size=` attribute against different default fonts is the obvious
reading; **do not merge these into one session.**

`[OBSERVED]` `A-editor-howto-step6-or-just-click.png` carries, at capture (983,501)–(1022,544), a
40×44 px light-grey rounded square containing a white "rectangle with an arrow
pointing into a smaller rectangle" glyph — a **picture-in-picture toggle**.
`[INFERRED]` this is a modern browser's `<video>` overlay (Firefox shipped that
control in v71, Dec 2019), i.e. **direct proof that this frame is a screen grab
of era footage played back in a modern browser**, exactly as the repo owner
states. It dates *Ethan's capture*, not the footage. Falsified if the same glyph
turns up inside an era page's own markup.

### Capture order (file mtimes = when Ethan cropped, 2026-08-04)

Used **only** as an ordering signal, per the brief:

```
17:03:26  A-toolbar-row-crop-run-around-the-world.png  626×296    session D, focused title field
17:04:59  A-toolbar-confirm-click-midfade.png       session A, ✓ just clicked, row mid-fade
17:29:57  A-editor-panel-primary-source-hq.png          session B  ← primary measurement source
17:30:14  A-editor-panel-kill-the-player.png              session B
17:30:25  A-maze-crop-4x4-hollow-centre.png  395×358     session B, maze-only crop
17:30:31  A-maze-crop-cell-highlight-on-spawn.png  413×363     session B, maze-only crop
17:30:46  A-toolbar-three-tool-icons-visible.png              session B  ← first frame with the 3rd icon
17:30:50  A-maze-crop-wall-highlight-vertical.png  375×392     session B, maze-only crop
17:31:12  A-editor-panel-highlight-outside-maze.png              session B
17:38:37  A-editor-howto-step6-or-just-click.png         session C
17:39:57  A-editor-preview-mode-lone-tick.png 1421×923     session C, PREVIEW state
```

`[OBSERVED]` Ethan worked session B as a block (17:29–17:31), then moved to
session C. Within session B the two frames **without** a tank icon
(`A-editor-panel-primary-source-hq`, `A-editor-panel-kill-the-player.png`) were cropped before the two **with** one
(`A-toolbar-three-tool-icons-visible.png`, `A-editor-panel-highlight-outside-maze.png`).

### `A-editor-panel-primary-source-hq.png` is the primary measurement source — and why  *(was `mazeditorhq.png`)*

`[OBSERVED]` The repo owner's filename claims it is his highest-quality editor
capture. `[MEASURED]` **Corroborated, on colour fidelity rather than pixel
count.** Sampling the maze's outer wall (known `#444444` from
[mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)) gives
`#454545` (darkest 20 px mean 69.3/255 vs the true 68) — essentially lossless.
The same sample in `A-toolbar-confirm-click-midfade.png` reads `#676a67` (103.6), i.e. that frame
has ~35 levels of lifted black and cannot be trusted for colour. `A-editor-preview-mode-lone-tick.png`
is physically larger (1421×923) but is a *zoomed, cropped* view with no panel
edges, so it cannot be scale-calibrated on its own. **Every colour and geometry
constant below is quoted from `A-editor-panel-primary-source-hq.png` unless stated otherwise.**

---

## Method — scale derivation, and the thing it forced into the open

Everything below is quoted in **CSS/stage px**, so the scale factor has to be
earned. Here is the derivation, in full, because it turned up a result that
overturns a pinned constant.

### Step 1 — the panel border marks the SWF stage edges

`[MEASURED]` In `A-editor-panel-primary-source-hq.png` the rounded panel's 1-px border renders as a
2–3 px light-grey line whose darkest columns/rows are: left `x=10–11`
(`#cecece`,`#d1d1d1`), right `x=980–981` (`#d2d2d2`,`#cfcfcf`), top `y=11`
(`#cccccb`), bottom `y≈659.5`. Border centres: **left 10.5, right 980.5, top 11.**

Span = 970.0 capture px. The SWF is embedded at **688×400**
(`srv/index.php:3617`), so if the border box coincides with the stage:

```
s = 970.0 / 688 = 1.40988 capture px per stage px
```

### Step 2 — three independent checks that s = 1.40988 and origin = (10.5, 11)

1. `[MEASURED]` Title ink `mr_enderman` spans x 410–579 → centre 494.5 →
   `(494.5 − 10.5)/1.40988 = 343.3` stage px. Stage centre is **344**. ✔ (0.7 px)
2. `[MEASURED]` Watermark ink right edge x 977 → `(977 − 10.5)/1.40988 = 685.5`
   stage px, i.e. right-flush to the stage. ✔
3. `[MEASURED]` Watermark ink bottom y 579.5 → `(579.5 − 11)/1.40988 = 403.2`
   stage px, i.e. baseline flush with the 400-px stage bottom (±3 px, the
   thickness of the border used as origin). ✔

A fourth, independent of the border entirely: the maze's wall centres sit at
capture y 158.5 and 458.0; their midpoint 308.25 maps to stage y 210 — the
centre of the `LATTICE_Y=50 … 370` box — only if the y-origin is 12.2. So the
**y-origin is 11 ± 3 capture px** and every vertical stage figure below carries
that ±2 stage px.

### Step 3 — the cell pitch does not come out at 32

`[MEASURED]` In `A-editor-panel-primary-source-hq.png` the maze is **4 cells × 4 cells** (wall runs at
x 343–351, 419–426, 568–575, 643–651 and y 155–162, 229–237, 380–387, 454–462;
the middle 2×2 is `#ffffff`, i.e. not floor). Outer wall centres 347→647 = 300.0
capture px over 4 cells = **75.00 capture px/cell horizontally and 74.88
vertically (158.5→458.0) = 53.19 / 53.11 stage px** — square to 0.2 %.

That is not 32. Repeating the exercise on every frame that shows a whole maze
and a calibratable panel:

| Frame | maze (w×h) | pitch, capture px | s | **cell, stage px** | `min(576/(w+2), 320/(h+2))` |
|---|---|---|---|---|---|
| `A-editor-panel-primary-source-hq.png` | 4 × 4 | 75.0 | 1.4099 | **53.19** | 53.33 |
| `A-toolbar-confirm-click-midfade.png` | 13 × 10 | 42.46 | 1.5959 | **26.61** | 26.67 |
| `A-editor-howto-step6-or-just-click.png` | 18 × 10 | 39.89 | 1.5138 | **26.35** | 26.67 |
| *(spec's `Making a maze.png`)* | 13 × 8 | 38.69 | 1.2093 | **31.99** | 32.00 |

`[MEASURED]` Four mazes, three distinct heights, four hits within 1.2 %:

> **the editor scales the maze so that the maze *plus a one-cell margin ring*
> fills the 576×320 lattice box** — `cell = min(576/(w+2), 320/(h+2))`.

`[UNCERTAIN]` Only the **height** term binds in all four samples, so what I can
defend hard is `cell = 320/(h+2)`; the width term is required to exist (a wide
short maze must be clamped somewhere) and `576` is consistent with every sample
(`A-editor-howto-step6-or-just-click` needs `Bw ≥ 533`), but no frame binds on it.

`[OBSERVED]` The one-cell margin ring is *real and clickable*: in
`A-editor-panel-highlight-outside-maze.png` the blue hover/selection rounded-rect sits **entirely outside the
maze's left boundary wall**, exactly one cell to its left. In `A-editor-preview-mode-lone-tick.png` the
recorder's click-highlight ring sits one cell to the right of an already-18-wide
maze. That is what the extra ring is for — it is how you grow the maze.

`[MEASURED]` The maze stays centred on the lattice box in both axes:
`A-editor-panel-primary-source-hq` maze bbox centre = stage (345.1, 210.8); `A-toolbar-confirm-click-midfade`
= (344.0, 210.4). Lattice box centre = (344, 210). ✔ `LATTICE_X=56`,
`LATTICE_Y=50` and the 576×320 box survive; **`CELL=32` as a constant does not.**

This is out of my assigned lane, but it is the derivation the brief demanded,
and it is load-bearing for every stage-px number in this document. Flagging it
loudly for whoever owns maze geometry.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| 1 | The centred grey heading above the stage is **not** the maze name — it is a username-shaped string differing from the title field in all 3 sessions | `[OBSERVED]` ×3 sessions + `[INFERRED]` for "username" | VE 7, S38, S39 | **Yes** — `Editor.as:338 titleTf.text = title` |
| 2 | Cell size is **dynamic**: `cell = min(576/(w+2), 320/(h+2))`; a one-cell editable margin ring surrounds the maze | `[MEASURED]` 4 mazes, ≤1.2 % error | VE 6, spec `CELL` | **Yes** — `MazeRenderer.CELL=32`, `originFor()`, `Editor.onClick` hit test |
| 3 | Tool strip is **exactly three** icons, never four; art described + palettes measured | `[MEASURED]` | **VE 1** | Adds 3 states as visual evidence |
| 4 | Deselect state is **exactly greyscale** (max R−B delta = **1** over the whole sprite); Select is full colour | `[MEASURED]` | **VE 1** | New constraint |
| 5 | The third (tank) icon is **wholly absent** — pure `#ffffff` — in the two earliest session-B frames and present in the two later ones, everything else pixel-identical | `[MEASURED]` diff | VE 1, S39 | Cautions against reading a build difference |
| 6 | Title ink is `#666666` (stem plateau **103**), ≈19 px, centred at stage x 343.3 | `[MEASURED]` | VE 7, spec title row | Confirms spec |
| 7 | Face is a **Helvetica/Arial-class grotesque — not Verdana, not Tahoma** (digit `1` has no foot bar in two sessions) | `[OBSERVED]` + `[MEASURED]` metrics | **VE 7**, S108 | Supports the rebuild's `_sans` |
| 8 | Watermark ≈12 px, letter-spacing **1.88 stage px**, ink right edge stage x **685.5**, ink bottom stage y **403** | `[MEASURED]` | VE 7, spec watermark row | Corrects `x≈682` → ≈685 |
| 9 | Watermark string carries **two spaces**: `version␣␣0.3` | `[MEASURED]` gap 13.5 stage px vs 8.4 predicted for one | VE 7 | **Yes** — `Editor.as:319` |
| 10 | Preview state = **lone ✓, no ✗, no input, no icons**; ✓ occupies the identical slot as the edit-state ✓ | `[OBSERVED]` + `[MEASURED]` position | VE 3, VE 4, S39 | Confirms `index.php:3737-3753` |
| 11 | `A-toolbar-confirm-click-midfade.png` catches the 200 ms fade in flight: ✗/input/icons at α≈0.17–0.20, accept ✓ already at α=1 | `[MEASURED]` | **VE 3** | Confirms `index.php:3742-3752` ordering |
| 12 | Error panel: **`[NOT VISIBLE]` in all 11 frames** | `[NOT VISIBLE]` | **VE 2** | Nothing — stays WANTED |
| 13 | Full control-row geometry in CSS px (input 11.7→167.0, icons at 47.5 px pitch, ✗/✓ right-aligned) | `[MEASURED]` | **S39** | S39 WANTED → PARTIAL/FETCHED |

---

## The control row — consolidated geometry

All figures are **CSS px measured from the panel's border-box top-left corner**,
which coincides with the SWF stage origin (see Method). Ink extents, not element
boxes: these are `<img>`s and an `<input>` on white, so the sprite files may be
slightly larger than their visible ink.

### Session B (`A-editor-panel-primary-source-hq` + 3 siblings, s = 1.4099) — the reference layout

| Element | x (CSS px) | width | y | height |
|---|---|---|---|---|
| title `<input>` border box | 11.7 → 167.0 | **156.0** | 424.1 → 443.3 | **19.9** |
| construct tool icon | 177.0 → 220.2 | 44.0 | 414.9 → 456.1 | 41.8 |
| crate spawn tool icon | 225.2 → 266.3 | 41.8 | 414.9 → 453.2 | 39.0 |
| tank spawn tool icon | 272.0 → 317.4 | 46.1 | 414.9 → 453.2 | 39.0 |
| ✗ `userpanelCancelMaze-` | 608.2 → 642.3 | 34.8 | 415.6 → 447.6 | 32.6 |
| ✓ `userpanelSaveMaze-` | 650.1 → 679.8 | 30.5 | 414.9 → 449.7 | 35.5 |

### Cross-session comparison

| Quantity | B (`A-editor-panel-primary-source-hq`) | C (`A-editor-howto-step6-or-just-click`) | A (`A-toolbar-confirm-click-midfade`) |
|---|---|---|---|
| left padding to input | 11.7 | 11.2 | 10.7 |
| input width | 156.0 | 176.4 | 182.3 |
| gap input → 1st icon | 10.0 | 10.6 | 7.5 |
| icon 1 → icon 2 pitch | 48.2 | 47.6 | 48.9 |
| icon 2 → icon 3 pitch | 46.8 | 46.2 | *(icons merged by fade)* |
| icon ink widths | 44.0 / 41.8 / 46.1 | 42.9 / 41.6 / 46.2 | 44.5 / merged |
| ✗ left edge | 608.2 | 602.5 | 607.8 |
| ✓ right edge | 679.8 | 674.5 | 683.6 |
| strip top edge | 414.9 | 407.6 | 417.9 |

`[MEASURED]` Reading of the above:

* The row is **left-flushed at ≈11 CSS px** and the ✗/✓ pair is **right-flushed,
  the ✓'s right edge landing 4–14 px short of the 688-px stage edge** (688 minus
  683.6 / 679.8 / 674.5); that 10 px spread across sessions is residual scale
  error plus video blur on the sprite's soft drop shadow, not a layout
  difference. `[UNCERTAIN]` I cannot narrow the right padding below "≈4–14 px"
  without a native-resolution frame.
* `[INFERRED]` The icons **flow inline immediately after the input**: session C's
  input is 20.4 px wider than session B's, and session C's first icon starts
  20.5 px further right. Same for the gap (≈10 px in both). That one-to-one
  correspondence is what an inline `<input><img><img><img>` row does, and it
  falsifies any absolute-positioned model. Falsified if a frame turns up with a
  wide input and icons still at x≈177.
* `[MEASURED]` **Icon pitch is 46–49 CSS px and constant across sessions**, so
  the JPGs are the same size everywhere; only the input's rendered width varies.
* `[MEASURED]` The strip's ink starts **8–18 CSS px below the SWF's 400-px
  bottom edge** and the panel's bottom border sits at 460.0 CSS px.
  `[UNCERTAIN]` That 460 does not obviously equal `userpanelContent` 385 or
  `userpanelswrapper` 500 from `srv/index.php:3619-3620`; I can measure the
  rendered panel but cannot map it onto those two animated heights without the
  server-side markup, which is unarchived (S24).

---

## The title/name input

`[MEASURED]` **Field:** a plain rectangle, `156.0 × 19.9` CSS px in session B.
The border is a single thin light-grey line — darkest pixels `#d3d3d3`
(left, x=30), `#d4d4d4` (top, y=610), `#d7d7d6` (bottom, y=635) — rendered
2 capture px wide, so **≈1 CSS px, colour ≤ `#d3d3d3`**. No inset/outset 3-D
bevel: the four sides sample the same tone, so this is *not* the Win-classic
default `<input>` border.

`[MEASURED]` **Text is left-aligned** with a **≈3.2 CSS px left inset**: field
inner edge at capture x 31.5, first ink (`K` of `Kill`) at x 36. `Kill The Player`
occupies capture x 36–137 of a field running to x 246 — under half the width.

`[MEASURED]` **Text colour is black.** Darkest ink `[24,19,22]` = `#181316`;
5th-percentile 66. This is the **typed state**, matching
`srv/index.php:3668-3669` (`value = title; style.color = "#000000"`).

`[MEASURED]` **Text size ≈11.5 px.** Per-glyph advances in `Kill The Player`
(capture px, ÷1.4099 for CSS): `h`→`e` 9 px = 6.4 CSS; `a`→`y` 9 px = 6.4 CSS;
`P`→`l` 11 px = 7.8 CSS. Against Arial advances (`h`,`a` = 0.556 em;
`P` = 0.667 em) those give 11.5 / 11.5 / 11.7 px. Cap-top to descender-bottom is
15 capture px = 10.6 CSS px, consistent with the same size.

### Transcriptions — verbatim, including casing

| Frame | Field content | Note |
|---|---|---|
| `A-toolbar-row-crop-run-around-the-world.png` | `Run Around The WORLD` | all-caps `WORLD`; whole string **selected** |
| `A-toolbar-confirm-click-midfade.png` | `One Path to Destruction` | lowercase `to`; caret visible at position 0 |
| `A-editor-panel-primary-source-hq.png`, `A-editor-panel-kill-the-player.png`, `A-toolbar-three-tool-icons-visible.png`, `A-editor-panel-highlight-outside-maze.png` | `Kill The Player` | no caret |
| `A-editor-howto-step6-or-just-click.png` | `Epic Twister` | caret visible at position 0 |

`[NOT VISIBLE]` **No frame shows the `Maze name` placeholder state.** All four
sessions show a typed, black, non-empty name. So the `#666666` half of the
`#666→#000` flip at `srv/index.php:3673-3674` remains **unverified against
pixels** — only the `#000000` half is now corroborated.

### The focused state — `A-toolbar-row-crop-run-around-the-world.png` only

`[MEASURED]` The whole string is highlighted: selection band ≈`#2292ff` /
`#278fe3` (most-saturated 60 px mean `#1d92fc`), with the glyphs rendered in a
**light** tone on top of it. `[OBSERVED]` Around the field runs a warm
cream/tan ring, tones `#fff9e4` → `#e1d4aa` → `#cbbc99` → `#f2ecd3`, roughly
2–3 CSS px thick, present on all four sides and extending horizontally past the
end of the blue band to the field's right edge.

`[UNCERTAIN]` I will not call this a focus ring outright. Two readings survive:
(a) a genuine `:focus` treatment or browser focus halo — supported by the ring
extending beyond the selection band and by its clean rectangular shape; (b) H.264
chroma overshoot, which produces exactly this complementary-yellow halo around a
saturated blue block, and this is the smallest, most compressed frame in the set
(626×296). **What would settle it:** the same field focused in a frame where the
text is *not* selected — no blue block, no possible chroma artefact. No CSS is
available to check against: `srv/includes/` is not in the staged tree.

`[INFERRED]` The placeholder mechanism is almost certainly the era's
`textFocus`/`textBlur` pair — every other era input uses
`onfocus="textFocus(this,'<placeholder>','rgb(102, 102, 102)','#666666')"`
(`srv/index.php:576-577, 4175, 4199`) and `showMazeCreatorToolsAndTitle` sets the
identical `value` + `#666666` pair by hand at `srv/index.php:3673-3674`. The
maze-title input's own markup is server-generated and unarchived, so this is an
inference from siblings, not a reading.

---

## The tool icons

### How many, and what each depicts

`[MEASURED]` **Three. Never four.** In every frame where the strip is legible
(`A-toolbar-row-crop-run-around-the-world.png`, `A-toolbar-three-tool-icons-visible.png`, `A-editor-panel-highlight-outside-maze.png`, `A-editor-howto-step6-or-just-click.png`) there are
exactly three sprites, at a constant 46–49 CSS px pitch, matching the three
`src` assignments at `srv/index.php:3732-3734` one-for-one. The brief's
"3-icon vs 4-icon" worry resolves the other way: **two frames show only *two*
icons** (below), and no frame anywhere shows four.

**Icon 1 — `mazeConstructToolSelect.jpg` (coloured).**
`[OBSERVED]` An open box/tray drawn in heavy black outline at a three-quarter
angle. Its rear-left panel is a saturated blue-violet rectangle carrying a
**dashed lighter-blue edge** (reads as a blueprint sheet or a selection
marquee); a white sheet lies in the tray's floor; the right-hand walls are mid
grey. Laid diagonally across the top-right is a **hammer** — ochre/gold handle
running lower-left to upper-right, grey-silver head at the top-right corner.
`[MEASURED]` Blue: most-saturated 60 px mean **`#5959df`**, single most
saturated `#5960e4`, blue-class darkest `#1d2069`, lightest `#9392b2`, n=558.
Gold: n=108 pixels with R−B>50, mean `#755f25`, ranging `#3b2701`→`#756b3a`.
Outline black: `#3e3e3e`–`#414141` (1.6 % of the tile). Ink 44.0 × 41.8 CSS px.

**Icon 2 — `crateSpawnToolDeselect.jpg` (greyscale).**
`[OBSERVED]` An isometric cube, three visible faces, sitting in front of an
**eight-pointed starburst**. `[MEASURED]` Cube faces: top `#d9d9d9`,
left `#bbbbbb`, right `#9e9e9e`; outline `#9e9e9e`/`#9f9f9f` (8.4 % of the
tile); starburst `#e4e4e4`–`#e5e5e5`. Ink 41.8 × 39.0 CSS px.

**Icon 3 — `tankSpawnToolDeselect.jpg` (greyscale).**
`[OBSERVED]` A three-quarter view of a tank facing right: tracked lower hull
with a visible row of road-wheel/tread marks, a hull body above it, and a long
barrel angled up to the right — in front of the **same eight-pointed
starburst**. `[MEASURED]` Hull `#cbcbcb`, barrel `#e7e7e7`, outline
`#9e9e9e`/`#a1a1a1`, starburst `#e5e5e5`–`#e6e6e6`. Ink 46.1 × 39.0 CSS px.

### The Select/Deselect distinction — measured

`[MEASURED]` **Deselect is exactly greyscale.** Over the *entire* crate tile
(60×55 capture px) and the *entire* tank tile (65×55), the maximum of
`max(R,G,B) − min(R,G,B)` is **1**. Over the construct tile it is **139**.
Same numbers in all four session-B frames and in `A-editor-howto-step6-or-just-click.png`
(1 / 1 / 138).

`[INFERRED]` Therefore the pair differs by **desaturation, not by a raised /
pressed border, not by a brightness step, and not by a positional offset**:
there is no border, bevel, frame or shadow around any of the three tiles to
measure (the sprites sit directly on the panel's white background — the icon
bounding boxes contain white right up to the artwork), and the three tiles sit
on a common top edge within 0.7 CSS px of each other in every frame. What
would falsify this: a frame where a selected icon is displaced or gains a frame.

`[INFERRED]` **Which state each frame holds.** `showMazeCreatorToolsAndTitle`
ends with `selectMazeCreatorTool(user, "construct")` (`srv/index.php:3664`), so
on entering edit mode the construct tool is always the selected one. Every frame
in this set is in edit state with a coloured construct icon and greyscale
crate/tank icons. So these frames hold:

* `mazeConstructToolSelect.jpg` — **new**, the archive shot holds the Deselect
* `crateSpawnToolDeselect.jpg` — **new**, the archive shot holds the Select
* `tankSpawnToolDeselect.jpg` — already held by the archive shot

`[NOT VISIBLE]` **`tankSpawnToolSelect.jpg` is still unseen** — no frame in this
set shows the tank tool active. Nor is `mazeConstructToolDeselect` /
`crateSpawnToolSelect` newly seen here (the archive shot has them).

### The vanishing third icon

`[MEASURED]` Aligning frames on the panel border and differencing the strip
(255×68 capture px) against `A-toolbar-three-tool-icons-visible.png`:

```
A-editor-panel-primary-source-hq.png    dx=-2 dy=0   construct: mean|Δ| 2.14 max 14   crate: 0.75 max 6   tank: 32.15 max 126, 1557 px >40
A-editor-panel-kill-the-player.png        dx= 0 dy=-5  construct: mean|Δ| 2.02 max 14   crate: 0.66 max 5   tank: 32.15 max 126, 1557 px >40
A-editor-panel-highlight-outside-maze.png        dx=-1 dy=-4  construct: mean|Δ| 1.42 max  9   crate: 0.65 max 4   tank:  0.67 max   5
```

`[MEASURED]` In `A-editor-panel-primary-source-hq.png` and `A-editor-panel-kill-the-player.png` the third slot (capture
x 390–470, y 590–656 and the 90 px beyond it) is **`#ffffff` to `#fefefe`, zero
pixels below 250** — not a faint icon, not a broken-image placeholder box, not a
greyed variant. Nothing at all. The construct and crate tiles in those same
frames are pixel-identical to the later frames.

`[INFERRED]` **This is a transient, most likely the third JPEG not yet
loaded/decoded**, not a build difference: `srv/index.php:3732-3734` sets all
three `src` attributes in one statement, the browser fetches them in parallel,
and the last can land a frame or two late — and the two icon-less frames are the
*earlier* two in Ethan's crop order. **Do not record a two-tool build.**
Falsified by: a frame showing a broken-image glyph in slot 3, a frame where the
tank icon disappears *after* being present, or a frame with a different tool
selected and still only two icons.

---

## The ✗ / ✓ buttons

`[MEASURED]` **Position and size** (session B, CSS px from the panel's top-left):
✗ at x 608.2–642.3 (34.8 wide) × y 415.6–447.6 (32.6 tall); ✓ at x 650.1–679.8
(30.5 wide) × y 414.9–449.7 (35.5 tall). **Gap between them: 7.8 CSS px.**
The ✓'s right edge lands 8.2 CSS px short of the 688-px stage edge — the same
order as the ≈11 px left padding on the input.

`[MEASURED]` **✗ colour.** Horizontal scan at capture y=620 across the left arm
of the cross:

```
c6a29f 903e3c e05654 ea403e f33838 f6393b fa3839 f33a38 ee4a44 c0534f 763a37
```

So a **body plateau of ≈`#f43838`**, a **dark maroon outline
≈`#8b2b2a`–`#903e3c`**, and a lighter gloss along the top-left (`#f57374` in
the vertical scan). Red-class pixels n=911, mean `#d45a5a`.

`[MEASURED]` **✓ colour.** Vertical scan down the tall right arm at capture
x=958:

```
68e021 69f123 66f219 60ed13 60ed14 5be914 56e50d 58e20c 5ed911 61c921 51a520 407c17
```

A **top-to-bottom gloss gradient from `#66f219` (bright yellow-green) to
≈`#4ab30d`**, with a very dark green
`#004d00` in the fold between the two strokes and `#319000`/`#4a8427` outlines.
Green-class pixels n=594, mean `#4da91c`.

`[OBSERVED]` Both are the classic glossy "cross"/"tick" sprites with a soft grey
drop shadow below-right. Neither ever appears greyed or disabled in any frame.

### The ✗ is absent in the preview state — and that is real

`[MEASURED]` In `A-editor-preview-mode-lone-tick.png` the only non-white content in the bottom-right
quadrant (searched x 1100–1421, y 820–923) is a single cluster at
x 1347–1410, y 832–908. Scaling that frame by the watermark's `v`→`n` span
(103 px there vs 70 px in `A-editor-panel-primary-source-hq`, ratio 1.471), a ✗ would occupy roughly
x 1260–1332 — **and that region contains no pixel below 245.**

`[MEASURED]` The lone ✓ is the *same sprite in the same slot*: its ink is
64 capture px wide (÷1.471 = 43.5, vs 43 for session B's ✓) and the offset from
the watermark's `v` to the ✓'s left edge is 90 capture px there vs 61 in
`A-editor-panel-primary-source-hq` — ratio 1.475 against the expected 1.471.

`[OBSERVED]` `A-editor-preview-mode-lone-tick.png` also has **no title input and no tool icons**. That
is exactly the state `hideMazeCreatorToolsAndTitle` leaves behind
(`srv/index.php:3737-3753`): controls hidden, `userpanelSaveMaze-` hidden,
`userpanelAcceptMaze-` shown. `[INFERRED]` **The lone ✓ is
`userpanelAcceptMaze-`, and it renders at the same place and size as
`userpanelSaveMaze-`.** This bears directly on the save-vs-cancel model: the
green tick is *two different buttons* that never coexist, and cancel only exists
while editing.

### `A-toolbar-confirm-click-midfade.png` catches the 200 ms fade in flight  *(was `clickonconfirm.png`)*

`[OBSERVED]` The mouse pointer sits on the ✓. `[MEASURED]` In that frame the
✗ is nearly white (most-saturated pixels `#ffdbdf`, `#fddcde`) while the ✓ is
fully saturated (`#00c932`, `#05cd2c`). Solving `observed = 255 − α(255 − c)`
against the full-opacity ✗ core (`#f83127`) on the green and blue channels gives
**α ≈ 0.15–0.17**; comparing peak chroma within the same frame (✗ 35 vs ✓ 201,
against 209 / 225 at full opacity) gives **α ≈ 0.19**. The input and the icon
strip in that frame are equally washed (the whole input crop spans only greys
220–255).

`[INFERRED]` This is `hideMazeCreatorToolsAndTitle` mid-run, ≈160–170 ms into
its 200 ms linear fade, and it **confirms the ordering written at
`srv/index.php:3742-3752`**: `userpanelCancelMaze-` and
`userpanelMazeCreatorControls-` fade over 200 ms while `userpanelSaveMaze-` is
switched to `display:none` and `userpanelAcceptMaze-` to `display:block`
*instantly*. That is why one tick is at full opacity in the middle of a fade.

### Error panel

`[NOT VISIBLE]` **In all 11 frames.** I searched every frame for a large solid
dark region (sliding 60×40 px window, fraction of pixels with mean < 150). The
maximum anywhere is 0.67, and in every case the window sits **on the tool-icon
strip** (e.g. `A-editor-panel-primary-source-hq` at (260,600) — the construct icon's black outline).
No frame contains a dark rounded box, a message strip, an overlay, or any text
other than the heading, the watermark and the name field.

VE 2 (`_root.errorPanel.hide`, `srv/index.php:3706, 3721`) stays **WANTED**,
untouched. `[INFERRED]` No frame here even *attempts* the trigger: every frame
has a non-empty name in the field, and the one save we can see
(`A-toolbar-confirm-click-midfade.png`) succeeded.

---

## In-stage title and the `version 0.3` watermark

### The heading is not the maze name — finding 1

`[OBSERVED]` In `A-toolbar-confirm-click-midfade.png` the heading reads `revengexx1` while the
name field, in the same frame, reads `One Path to Destruction`. In
`A-editor-howto-step6-or-just-click.png` the heading reads `cam12win` while the field reads
`Epic Twister`. In the four session-B frames the heading reads `mr_enderman`
while the field reads `Kill The Player`. **Three sessions, three disagreements,
zero agreements.**

`[INFERRED]` The heading is the **maze owner's username**. The reasoning: all
three strings are username-shaped tokens (`mr_enderman` with an underscore,
`cam12win` and `revengexx1` with trailing digits) of exactly the kind TankTrouble
accounts use, while all four field strings are sentence-cased maze names; and the
same heading `cam12win` appears over two *different* mazes of session C
(`A-editor-howto-step6-or-just-click.png` 18×10 fresh lattice, `A-editor-preview-mode-lone-tick.png` a finished spiral).
**What would falsify it:** a frame where the heading changes while the account
does not, or a frame where the heading tracks keystrokes in the field.

`[UNCERTAIN]` **Whether the heading is drawn by the SWF or by the page.** It is
inside the stage's 688×400 area and centred on stage x 344, which fits an SWF
TextField; but a page-side `<h?>` at the top of `userpanel-<user>` would land in
the same place, and `x_updateUserPanels`' markup is unarchived (S24). One useful
datum: in `A-toolbar-confirm-click-midfade.png` the heading stays at **full opacity** while the
whole control row fades, so it is definitely **not** inside
`userpanelMazeCreatorControls-`.

`[MEASURED]` Centred: heading ink centre maps to stage x **343.3**
(`A-editor-panel-primary-source-hq`) — stage centre is 344.

### Title typography

`[MEASURED]` **Colour = `#666666`.** Horizontal scanlines through the `n` and
`d` stems of `mr_enderman` (capture rows 30–41, columns 472–504) plateau at
**103–110**, e.g. row 37 reads `… 249, 201, 144, 108, 153, 213, 247 …`. The
outlying "darkest pixel" figures (82) come from stroke junctions where the video
codec rings; the *plateau* is the fill. `#676767` measured against `#666666`
specified — **the spec's pinned title colour is confirmed almost exactly.**
(Calibration check: the maze wall in the same frame measures 69 against a true
68, so this frame carries ~1 level of tonal error.)

`[MEASURED]` **Size ≈19 px (defensible range 18–20).** Baseline at capture
y 42.7, x-height top at 28.3, `d`-ascender top at 24.0. With s=1.4099:
x-height **10.2 stage px**, ascender height **13.3 stage px**. Against Arial
(x-height 0.519 em, `d` 0.716 em) that gives 19.7 px and 18.6 px respectively.
Ink width of `mr_enderman` = 170 capture px = 120.6 stage px; Arial's advance sum
for that string is 6.224 em → 19.7 px, Tahoma's 6.486 em → 18.9 px, Verdana's
7.11 em → 17.2 px. **The spec's "≈18 px" holds; 19 is the better centre.**

`[MEASURED]` **Band.** Ink runs stage y ≈ 9 → 22.5 (±2, from the y-origin
uncertainty); the x-height band is stage y 11.4 → 21.6 using the maze-centre
y-origin. The spec's "band stage y ≈ 10-22" is confirmed.

`[MEASURED]` **Weight is regular, not bold.** The `n` left stem has a
full-width-half-maximum of ≈2.2 capture px = 1.56 CSS px, which is a regular
18–19 px Arial stem. A bold stem would be ≈2.5 CSS px.

### Typeface — what can and cannot be said

`[OBSERVED]` **It is not Verdana and it is not Tahoma.** The decisive glyph is
the digit `1`, which appears in two independent sessions:

* `A-editor-preview-mode-lone-tick.png` `cam12win`: the `1` is ink 5 capture px wide inside a ~15 px
  advance — a bare stem with a small angled flag, **no horizontal foot bar**.
* `A-toolbar-confirm-click-midfade.png` `revengexx1`: same — the upscaled crop shows a plain stem
  and flag with no base serif.

Verdana and Tahoma both draw `1` with a full-width horizontal foot; Arial and
Helvetica do not. `[MEASURED]` The metric evidence agrees but is weaker: for
`revengexx1` the `r`/`n` advance ratio is 10/17 = **0.588** (Arial 0.60,
Tahoma 0.674, Verdana 0.690); for `mr_enderman` it is 10/15 = 0.667, i.e.
±1 px quantisation on a 15 px advance is enough to swing it, so I would not
convict on metrics alone.

`[INFERRED]` **A Helvetica/Arial-class grotesque, which is exactly what Flash's
`_sans` device font resolves to** (Arial on Windows, Helvetica on Mac). The
rebuild's choice at `src/mazecreator/Editor.as:309, 315, 330` is therefore
*supported*, not merely unfalsified. `[NOT VISIBLE]` Arial vs Helvetica is
**not resolvable at this resolution** — the discriminators (the angled vs
horizontal cut on `e`, `s`, `t` terminals) are 1–2 px features here.

`[UNCERTAIN]` One weak hint that the heading is device text rather than an
embedded font: `A-editor-panel-primary-source-hq`'s darkest heading pixels carry a slight channel
split (`[82,78,80]`, `[81,78,75]`) where the watermark is pure neutral
(`[192,192,192]`), which is what an OS subpixel rasteriser does. This is well
inside video-chroma noise; I would not build on it. It is, however, exactly the
question S108 asks.

### Watermark

`[MEASURED]` **Content:** `version 0.3`, all lowercase `version`, digits `0.3`.
Nine glyph column-runs in `A-editor-panel-primary-source-hq` at capture x
`866-873 (v), 877-884 (e), 888-894 (r), 898-905 (s), 909-912 (i), 916-923 (o),
927-935 (n), 954-966 (0.), 968-977 (3)`.

`[MEASURED]` **Position:** ink x 866→977 = stage **606.8 → 685.5**; ink y
567→579.5 = stage **394.4 → 403.2** (±2, origin uncertainty). So it is
right-flushed and bottom-flushed to the stage corner. The spec's pinned
"right-aligned to x ≈ 682" is **≈3 stage px short**; the ink's true right edge
(discounting one AA column) is **≈684–685**. The spec's "bottom edge ≈ 400
(flush corner)" is confirmed.

`[MEASURED]` **Size ≈12 px.** Digit/cap height = 402.9 − 394.4 = 8.5 stage px;
Arial cap height is 0.716 em → **11.9 px**. The spec's "≈12 px" is confirmed.

`[MEASURED]` **Letter-spacing = 1.88 stage px.** From `v` ink start to `n` ink
start is 61 capture px = 43.3 stage px, covering the advances of
`v,e,r,s,i,o` (0.500+0.556+0.333+0.500+0.222+0.556 = 2.667 em = 32.0 px at 12 px)
plus 6 letter-space increments → `(43.3 − 32.0)/6 = 1.88`. **`Editor.as:316`
`vf.letterSpacing = 2` is confirmed.**

`[MEASURED]` **The string carries two spaces, not one.** The whitespace between
the `n` ink end (x 935) and the `0` ink start (x 954) is 19 capture px =
**13.5 stage px**. One space predicts `rsb(n) + LS + 3.34 + LS + lsb(0)` ≈
**8.4** stage px; two spaces predict **13.6**. Cross-checked start-to-start:
`n`→`0` is 19.15 stage px in `A-editor-panel-primary-source-hq` and 19.4 in `A-toolbar-confirm-click-midfade`, against
`8.55 + 5.22k` → **k = 1.98**. So the watermark text is **`version␣␣0.3`**.

`[MEASURED]` **Colour ≈`#bbbbbb`–`#c0c0c0`.** Darkest ink pixel is **192**
(`#c0c0c0`) in `A-editor-panel-primary-source-hq`, and 192 / 192 / 193 / 194 in the three other
calibratable frames. At 12 px the strokes are ~1 CSS px, so no pixel reaches
full coverage and the true fill is **darker than or equal to `#c0c0c0`**; the
spec's `#bbbbbb` (187) sits right at the edge of that bound and is consistent.
It cannot be as dark as `#999999`. `[UNCERTAIN]` I cannot pin it exactly without
a native-resolution frame.

`[OBSERVED]` In `A-editor-howto-step6-or-just-click.png` and `A-toolbar-confirm-click-midfade.png` the final `3` is
**clipped by the panel's right border** — further evidence the mark is flushed
hard into the corner.

---

## File-by-file analysis

### `UI/A-toolbar-row-crop-run-around-the-world.png` (626×296, captured 17:03:26)  *(was `{7EB8BFD4-E208-4674-A24A-B5879F8FEBC5}.png`)*
[image](./UI/A-toolbar-row-crop-run-around-the-world.png)

**Filename claim (repo owner):** none — GUID name.

**What is drawn.** `[OBSERVED]` A tight crop of the control row only; the SWF
stage is above the top edge and is not in frame. Left to right: the title
`<input>` containing **`Run Around The WORLD`** with the entire string
selected; the coloured construct icon; the greyscale crate icon; the greyscale
tank icon. `[MEASURED]` A solid black block occupies capture x 0–13,
y 71–132 at the far left (an adjacent page column; not identifiable from this
crop).
`[OBSERVED]` Bottom-right carries the era page copy `Sign up anoth…` in the
site's heading style — the visible fragment of **`Sign up another tank`**
(`srv/index.php:702`), i.e. the login sidebar is still on the page around the
garage panel. `[NOT VISIBLE]` heading, watermark, ✗, ✓, maze, error panel.

**Measurements.** `[MEASURED]` No panel border is in frame, so scale is derived
from the icon ink widths against session B: construct 74 capture px here vs 62
there (1.194), crate 69 vs 59 (1.169), tank 76 vs 65 (1.169) → **s ≈ 1.65
± 0.04**, the loosest calibration in this set. Icon strip at capture
x 345–418 / 424–492 / 500–575 (pitch 79, 76 capture px = **48, 46 CSS px** —
matching every other session). Input outer ink x 48–333 = 286 capture px =
**≈173 CSS px**, i.e. this session's field is wider than session B's 156.
Selection band `#2292ff`/`#278fe3`; ring tones `#fff9e4`→`#cbbc99` (see
"the focused state" above, marked `[UNCERTAIN]`).

**Links to the program.** Confirms the three-icon strip of
`srv/index.php:3732-3734` and the Select/Deselect colour/greyscale split. The
only frame in this set holding the input **focused**, which is where
`srv/index.php:3673-3674`'s `#666→#000` flip and `mazeTitleLegalCharacters`
(`:3678-3701`) live — but the field already holds a typed name, so neither is
directly exercised. Bears on **S39**.

**What this does NOT show.** The placeholder state, the heading, the watermark,
the buttons, any tool other than construct in Select.

---

### `UI/A-toolbar-confirm-click-midfade.png` (1112×767, captured 17:04:59)  *(was `clickonconfirm.png`)*
[image](./UI/A-toolbar-confirm-click-midfade.png)

**Filename claim (repo owner):** *"click on confirm"* — **corroborated.**
`[OBSERVED]` The mouse pointer sits directly on the green ✓, and the entire
control row is caught mid-fade while the ✓ is at full strength. That is
precisely the instant after a confirm click.

**What is drawn.** `[OBSERVED]` The full panel. Heading **`revengexx1`**
centred at the top at full opacity. A large irregular maze. Bottom-right
`version 0.3` (the `3` clipped by the panel border). Along the bottom, faded
almost to white: the title input reading **`One Path to Destruction`** with a
caret at position 0, the three tool icons, and the ✗. At full opacity: the ✓,
with the cursor on it.

**Measurements.** `[MEASURED]` s = 1.5959 (panel border centres x 1.0 and
1099.0). Control row in CSS px: input 10.7→192.4 (**182.3** wide), icon 1
199.9→243.7, icons 2+3 merged by the fade at 248.8→342.1, ✗ 607.8→644.8,
✓ 647.9→683.6. `[MEASURED]` Fade α of the ✗ ≈ **0.15–0.20** (two independent
estimates, above); input crop spans only greys 220–255. `[MEASURED]` Maze
13 × 10 cells, wall pitch 42.46 capture px = **26.61 stage px**, bbox centred at
stage (344.0, 210.4). `[MEASURED]` Watermark `v`→`n` 68 capture px = 42.6 stage
px; `n`→`0` 31 capture px = 19.4 stage px (the two-space evidence).
`[MEASURED]` **Colour warning:** the maze wall reads `#676a67` (103.6) against a
true `#444444` — this frame has ~35 levels of lifted black and **must not be
used for colour constants**.

**Links to the program.** The strongest single confirmation of
`srv/index.php:3737-3753` in this set: the 200 ms linear fades on
`userpanelCancelMaze-` (`:3742-3743`) and `userpanelMazeCreatorControls-`
(`:3745-3746`) running while `userpanelSaveMaze-`/`userpanelAcceptMaze-` swap
instantly (`:3748-3752`). Moves **VE 3** off zero. Second independent proof that
the heading ≠ the maze name (finding 1).

**What this does NOT show.** What happens *after* the fade completes — the frame
stops mid-transition. No error panel, no spinner, no confirmation flash is
present at this instant, but 160 ms is not enough to rule one out later.

---

### `UI/A-editor-panel-primary-source-hq.png` (990×672, captured 17:29:57) — PRIMARY SOURCE  *(was `mazeditorhq.png`)*
[image](./UI/A-editor-panel-primary-source-hq.png)

**Filename claim (repo owner):** *"maze editor hq"* — **corroborated on
fidelity, not on size.** `[MEASURED]` Its maze wall samples `#454545` against a
true `#444444`; it is the most colour-accurate frame in the set even though
`A-editor-preview-mode-lone-tick.png` has more pixels.

**What is drawn.** `[OBSERVED]` The whole garage panel: a white rounded box with
a 1 px light-grey border; heading **`mr_enderman`** centred at the top; a small
4×4 maze with a hollow 2×2 centre, two tank spawns in the bottom-left, and a
thin blue horizontal wall-highlight at the left with the mouse arrow beside it;
`version 0.3` bottom-right; and the control row — input **`Kill The Player`**,
construct icon (coloured), crate icon (greyscale), **an empty third slot**,
then ✗ and ✓ at the right.

**Measurements.** `[MEASURED]` Panel border centres left 10.5, right 980.5,
top 11.0, bottom 659.5 → **s = 1.40988**, panel height 460.0 CSS px.
Full control-row geometry in the table above. Title ink x 410–579, y 24–47;
stem plateau **103**; x-height 10.2 stage px; ascender 13.3 stage px.
Watermark ink x 866–977, y 567–579; darkest 192; letter advances
11,11,10,11,7,11 capture px. Maze wall centres x 347/422.5/571.5/647,
y 158.5/233/383.5/458 → pitch **75.0 capture = 53.19 stage px**. Floor tones per
cell: `#d8d8d8` / `#ececec`, inner 2×2 `#ffffff` (not floor). Third icon slot
(x 390–470): **zero pixels below 250**.

**Links to the program.** Everything in the "consolidated geometry",
"title/name input", "tool icons", "✗/✓" and "typography" sections above is
anchored here. Bears on **VE 1**, **VE 7**, **S39**, the spec's title and
watermark rows, and (via the pitch) the spec's `CELL` row.

**What this does NOT show.** The tank icon; the placeholder state; any tool
other than construct selected; the error panel; the preview state.

---

### `UI/A-editor-panel-kill-the-player.png` (992×665, captured 17:30:14)  *(was `{C2BC325C-D127-4F7B-A66F-D188E2B42ABA}.png`)*
[image](./UI/A-editor-panel-kill-the-player.png)

**Filename claim (repo owner):** none.

**What is drawn.** `[OBSERVED]` The same session-B panel, one interaction later:
identical heading, maze, watermark and control row, except the maze highlight is
now a **cell-sized** blue rounded square inside the maze's left column instead
of the thin wall sliver of `A-editor-panel-primary-source-hq`. `[OBSERVED]` The third icon slot is
still empty.

**Measurements.** `[MEASURED]` s = 1.40988 (border centres 12.5 / 982.5, top
6.0). Control row in CSS px identical to `A-editor-panel-primary-source-hq` to within 0.1 px on every
element (see table). `[MEASURED]` Differencing the icon strip against
`A-toolbar-three-tool-icons-visible.png` after alignment: construct mean |Δ| **2.02**, max 14; crate mean
|Δ| **0.66**, max 5 — pixel-identical sprites. Third slot: zero pixels below
250 over an 80×65 capture-px window.

**Links to the program.** Second instance of the missing tank icon, 17 s later
in crop order. Together with `A-editor-panel-primary-source-hq` it establishes that the absence
persists across at least two frames — which is why I call it a load transient
rather than a dropped frame, but also why it deserves the explicit
falsification list above.

**What this does NOT show.** Same list as `A-editor-panel-primary-source-hq`.

---

### `UI/A-maze-crop-4x4-hollow-centre.png` (395×358, captured 17:30:25)  *(was `{4CEE81F1-5F4D-4B08-9AEC-CF6BE2CA6820}.png`)*
[image](./UI/A-maze-crop-4x4-hollow-centre.png)

**Filename claim (repo owner):** none.

**What is drawn.** `[OBSERVED]` A crop containing **only** the session-B maze:
the 4×4 grid, hollow 2×2 centre, two tank spawns bottom-left, a thin blue
horizontal wall-highlight on the left edge with the mouse arrow on it.

**Measurements.** `[MEASURED]` Wall-run centres x 34 / 109.5 / 258.5 / 334 and
y 22.5 / 97 / 247.5 / 322 → pitch **75.00 horizontal, 74.88 vertical capture
px**, identical to `A-editor-panel-primary-source-hq`'s 75.00 / 74.88 — the same session at the same
zoom.
`[MEASURED]` Non-white content spans rows 17–328 and nothing else: the crop
contains no page chrome at all.

**Links to the program.** Nothing in my topic. Useful only as corroboration that
the three small crops belong to session B.

**What this does NOT show.** `[NOT VISIBLE]` toolbar, tool icons, title input,
✗, ✓, heading, watermark, error panel — **all of them.** Recording that
explicitly: this file contributes nothing to VE 1, VE 2, VE 7 or S39.

---

### `UI/A-maze-crop-cell-highlight-on-spawn.png` (413×363, captured 17:30:31)  *(was `{48554A6F-E546-42A0-B785-2824B4B4D7E3}.png`)*
[image](./UI/A-maze-crop-cell-highlight-on-spawn.png)

**Filename claim (repo owner):** none.

**What is drawn.** `[OBSERVED]` The same session-B maze, cropped, with the blue
**cell** highlight now on the bottom-left cell (the one holding a tank spawn),
cursor inside it.

**Measurements.** `[MEASURED]` Wall centres x 73 / 148.5 / 297.5 / 373,
y 36.5 / 111 / 261.5 / 336 → pitch **75.00 / 74.88 capture px**. Same session,
same zoom.

**Links to the program.** Nothing in my topic.

**What this does NOT show.** `[NOT VISIBLE]` toolbar, icons, input, ✗/✓,
heading, watermark, error panel.

---

### `UI/A-toolbar-three-tool-icons-visible.png` (997×676, captured 17:30:46)  *(was `{145AE34F-9EA7-4B2A-BF15-DFF015A87A17}.png`)*
[image](./UI/A-toolbar-three-tool-icons-visible.png)

**Filename claim (repo owner):** none.

**What is drawn.** `[OBSERVED]` The session-B panel with **all three tool icons
present** — the first frame in crop order to have the tank icon. Heading
`mr_enderman`, input `Kill The Player`, ✗ and ✓. The maze highlight is a thin
blue **vertical** wall sliver on the maze's top interior edge.

**Measurements.** `[MEASURED]` s = 1.40988 (borders 12.5 / 982.5, top 11.0).
This is the reference frame for the icon palettes quoted above: construct
max chroma **139**, crate **1**, tank **1**; cube faces `#d9d9d9`/`#bbbbbb`/
`#9e9e9e`; tank hull `#cbcbcb`, barrel `#e7e7e7`; starbursts `#e4e4e4`–`#e6e6e6`;
construct blue most-saturated mean `#5959df`, gold class mean `#755f25`,
outline `#3e3e3e`–`#414141`. ✗ body plateau `#f43838`, outline `#8b2b2a`;
✓ gloss `#66f219` → `#4ab30d`, fold `#004d00`. Tank icon ink **46.1 × 39.0 CSS
px** at x 272.0→317.4.

**Links to the program.** The best single frame for **VE 1**: it holds
`mazeConstructToolSelect`, `crateSpawnToolDeselect` and `tankSpawnToolDeselect`
simultaneously at ~44 CSS px, with the Select/Deselect rule measurable
(chroma 139 vs 1 vs 1). Confirms the third `src` line at `srv/index.php:3734`
actually resolved to an image on the live site — all six JPGs are `known-lost`
in [LEDGER.tsv](../../../LEDGER.tsv) rows 305, 306, 327, 328, 414, 415.

**What this does NOT show.** `tankSpawnToolSelect` / `crateSpawnToolSelect` /
`mazeConstructToolDeselect`; the placeholder state; the error panel.

---

### `UI/A-maze-crop-wall-highlight-vertical.png` (375×392, captured 17:30:50)  *(was `{BFBF9223-3000-4A0B-AF02-70983B4C0C3E}.png`)*
[image](./UI/A-maze-crop-wall-highlight-vertical.png)

**Filename claim (repo owner):** none.

**What is drawn.** `[OBSERVED]` The session-B maze again, cropped, with a thin
blue **vertical** wall highlight at the maze's top interior edge and the cursor
beside it — the same interaction as `A-toolbar-three-tool-icons-visible.png` but with the page chrome
cropped away.

**Measurements.** `[MEASURED]` Wall centres x 36 / 111.5 / 260.5 / 336,
y 42.5 / 117 / 267 / 342 → pitch **75.00 / 74.88 capture px**. Same session,
same zoom.

**Links to the program.** Nothing in my topic.

**What this does NOT show.** `[NOT VISIBLE]` toolbar, icons, input, ✗/✓,
heading, watermark, error panel.

---

### `UI/A-editor-panel-highlight-outside-maze.png` (988×667, captured 17:31:12)  *(was `{851E5C49-BBC4-4CE1-B061-D5A37CC9651D}.png`)*
[image](./UI/A-editor-panel-highlight-outside-maze.png)

**Filename claim (repo owner):** none.

**What is drawn.** `[OBSERVED]` The session-B panel, three icons present.
Notably the blue cell highlight now sits **entirely outside the maze**, one cell
to the left of its boundary wall, on plain white background — the clearest
single view of the editable margin ring.

**Measurements.** `[MEASURED]` s = 1.40988 (borders 11.5 / 981.5, top 7.0).
Aligned diff against `A-toolbar-three-tool-icons-visible.png` over the whole icon strip: **zero pixels
differ by more than 30**, per-icon mean |Δ| 1.42 / 0.65 / 0.67. So the tool
state is unchanged between those two frames. Control-row geometry identical to
the table.

**Links to the program.** Confirms the tool strip is static between frames
(i.e. no hover state on the icons was captured — see "New wants"). Its highlight
position is the geometric evidence for the one-cell margin ring in the Method
section.

**What this does NOT show.** A second tool state; the placeholder; the error
panel.

---

### `UI/A-editor-howto-step6-or-just-click.png` (1051×699, captured 17:38:37)  *(was `6orjustclick.png`)*
[image](./UI/A-editor-howto-step6-or-just-click.png)

**Filename claim (repo owner):** *"6 or just click"* — **unsettled by this
topic.** `[OBSERVED]` The `6` reads as a step number in a numbered how-to
sequence, and "or just click" is a claim about *interaction* (drag-paint vs
click), which is VE 5 territory, not mine. Nothing in the toolbar, icons or
typography can confirm or refute it. `[OBSERVED]` What the frame does show is a
maze in a state consistent with "just started": a full 18×10 floor with a single
short wall segment drawn in the top-left corner and a blue blob under the cursor.

**What is drawn.** `[OBSERVED]` Session C's panel: heading **`cam12win`**,
an 18×10 all-floor lattice bounded by a dark rectangle, `version 0.3`
bottom-right with the `3` clipped, and the control row — input
**`Epic Twister`** with a caret at position 0, three tool icons (construct
coloured, crate and tank greyscale), ✗ and ✓. `[OBSERVED]` A picture-in-picture
toggle overlay at capture (983,501)–(1022,544) (provenance note, above).

**Measurements.** `[MEASURED]` s = 1.5138 (panel border centres 6.0 / 1047.5).
Control row in CSS px: input 11.2→186.9 (**176.4** wide), icons
197.5→239.8 / 245.1→286.0 / 291.3→336.9 (pitch **47.6 / 46.2**), ✗
602.5→636.1, ✓ 644.1→674.5. Icon chroma: construct **138**, crate **1**,
tank **1**. `[MEASURED]` Maze boundary spans capture x 165→883 (718 px) and
y 116→515 (399 px) = 18 × 10 cells at **39.89 capture px = 26.35 stage px**.
Watermark `v`→`n` 74 capture px.

**Links to the program.** Second session confirming the three-icon strip, the
Select/Deselect chroma rule and the inline flow of the row after the input.
Its 18×10 maze is one of the four data points behind the dynamic-cell finding.
Bears on **VE 1**, **VE 7**, **S39**, and (via the maze) VE 6 / the spec's
`CELL` row.

**What this does NOT show.** A second tool state; the placeholder; the error
panel; the preview state.

---

### `UI/A-editor-preview-mode-lone-tick.png` (1421×923, captured 17:39:57)  *(was `{5243A3F8-38F5-4DB2-8589-17C8F75A505A}.png`)*
[image](./UI/A-editor-preview-mode-lone-tick.png)

**Filename claim (repo owner):** none.

**What is drawn.** `[OBSERVED]` A zoomed, cropped view of session C's panel
showing a **finished concentric-spiral maze** (18 × 10) with faint per-cell
gridlines and a dark dot at each grid intersection, three tank spawns and four
crate spawns. Heading **`cam12win`** at the top (its glyph tops clipped by the
crop). `version 0.3` bottom-right with the `3` at the image edge. Bottom-right:
**a single green ✓, and nothing else** — no ✗, no title input, no tool icons.
`[OBSERVED]` A yellow ring around the cursor, one cell to the right of the
maze's right boundary — a screen-recorder click indicator, not site UI.

**Measurements.** `[MEASURED]` Non-white content in the whole bottom-right
quadrant (x 1100–1421, y 820–923) is confined to x 1347–1410, y 832–908 — the
✓ alone. A ✗ would fall near x 1260–1332, where **no pixel is below 245**.
`[MEASURED]` ✓ ink 64 capture px wide; ÷1.471 (scale ratio from the watermark
`v`→`n` span, 103 vs 70 px) = **43.5**, against session B's ✓ ink of 43 capture
px — the same sprite. Offset from the watermark `v` to the ✓ left edge: 90 px
here vs 61 px in session B, ratio **1.475** vs the expected 1.471 — the same
slot. `[MEASURED]` Watermark glyph runs `1257-1268 (v) … 1348-1359 (n),
1386-1405 (0.), 1408-1420 (3)`; heading glyph runs `620-635 (c) … 780-797 (n)`
with the `1` of `cam12win` **5 px of ink inside a 15 px advance — no foot bar**
(the typeface evidence).

**Links to the program.** The only **preview-state** frame in this set. It
matches `hideMazeCreatorToolsAndTitle` (`srv/index.php:3737-3753`) exactly:
controls gone, `userpanelSaveMaze-` gone, `userpanelAcceptMaze-` present. Gives
**VE 4** its first datum — the boot/preview screen is *the maze itself, drawn
full-size, with a single accept tick* — and is the second frame proving the
heading is not the maze name (it persists with no input on screen).

**What this does NOT show.** Whether the preview offers multiple slots or a
"create new maze" affordance (only one maze is on screen and the crop cuts the
left/bottom of the panel); the transition into edit state; the error panel.

---

## Consequences for the rebuild

### Confirmed

* `[MEASURED]` **Title colour `#666666`** — spec row "Title text" holds
  (stem plateau 103 in a frame whose wall reference is accurate to 1 level).
* `[MEASURED]` **Title band stage y ≈ 10–22** — spec row holds.
* `[MEASURED]` **Title centred on the stage** (ink centre → stage x 343.3) —
  `Editor.as:309` `align="center"` over a stage-wide field holds.
* `[MEASURED]` **Title ≈18 px** — spec holds; 19 is a slightly better centre,
  the defensible range is 18–20. `Editor.as:309` `tfm.size = 18` needs no change.
* `[MEASURED]` **Watermark ≈12 px** and **bottom edge flush at stage y ≈400** —
  spec rows hold; `Editor.as:315` `vf.size = 12` holds.
* `[MEASURED]` **Watermark letter-spacing ≈1.88 px** — `Editor.as:316`
  `letterSpacing = 2` holds.
* `[MEASURED]` **Watermark colour ≤ `#c0c0c0`** — spec's `#bbbbbb` is inside the
  bound; `Editor.as:315` `0xBBBBBB` holds.
* `[INFERRED]` **Device sans (`_sans`) is the right family choice** — the digit
  `1` has no foot bar in two independent sessions, ruling out Verdana and
  Tahoma and leaving the Arial/Helvetica class that `_sans` resolves to.
* `[MEASURED]` **Lattice box origin (56, 50) and size 576×320** — both maze
  bboxes centre on (344, 210) to within 1.1 stage px.
* `[OBSERVED]` **`hideMazeCreatorToolsAndTitle` behaviour** (`srv/index.php:
  3737-3753`): 200 ms fade on cancel + controls, instant swap of save→accept.
* `[MEASURED]` **Typed-state input colour `#000000`** —
  `srv/index.php:3668-3669`.
* `[MEASURED]` **Three tool buttons, defaulting to construct=Select** —
  `srv/index.php:3664, 3732-3734`.

### Contradicted — overhaul owed

1. **`src/mazecreator/Editor.as:338` — `titleTf.text = title;`**
   The in-stage heading is **not** the maze name. Three sessions show a
   username-shaped heading alongside a different, maze-shaped name in the input.
   *What the invention was:* the rebuild renders the maze name centred over the
   stage. *What the evidence shows:* it renders the owner's username (or at
   least something that is not the field's content and does not track it).
   *Owed:* rewrite the title source in `Editor.as` (`redraw()` and the
   `mazeName` branch of `onSetVariable`, `:165`) so the heading is driven by the
   identity field of `initCode`, not by `_root.mazeName`. Under **THE OVERHAUL
   RULE** this is a rewrite of the display path, not a string tweak — and it
   also re-opens **S38**, because the SWF must be *given* a username, which is
   positive evidence for an `n`-like field in `userSettingsMazeCreatorInitCode-`.
   `[UNCERTAIN]` If the heading turns out to be page-side markup, the fix moves
   to the (unarchived) userpanel template instead and `titleTf` should be deleted
   outright. Settle this before rewriting: a frame where the SWF is mid-fade
   (`fadeOut`) tells you instantly whether the heading fades with it.

2. **`src/mazecreator/MazeRenderer.as:36` — `CELL = 32` as a constant**, and
   everything built on it: `originFor()` (`:56-59`), `Editor.loadIntoLattice`'s
   `fracX/fracY` half-cell remainder (`:82-105`), and `Editor.onClick`'s hit
   test (`:192-214`, which divides by `MazeRenderer.CELL` and uses a fixed
   `EDGE_TOL = 6`).
   *What the invention was:* a fixed 32-px cell on a fixed 18×10 lattice, with
   the maze centred at integer cell offsets and a half-cell render shift.
   *What the evidence shows:* `cell = min(576/(w+2), 320/(h+2))` — 53.19 px for a
   4×4 maze, 26.6 px for 13×10 and 18×10, and 32 px for the spec's own 13×8
   sample, all within 1.2 %. 32 is not a constant; it is what the formula returns
   for `h = 8`. The maze is centred in the 576×320 box, surrounded by exactly one
   editable cell of margin.
   *Owed:* a wholesale rewrite of the renderer's geometry and the editor's hit
   test against the formula, plus a re-pin of the visual-spec `CELL` row and the
   `Making a maze.png`-derived gauntlet. `EDGE_TOL` must scale with the cell too.
   This lands outside my assigned topic but fell straight out of the mandated
   scale derivation; it needs an owner.

3. **`src/mazecreator/Editor.as:319` — `_root.versionTf.text = "version 0.3";`**
   *What the evidence shows:* the gap between `n` and `0` is 13.5 stage px, and
   one space predicts 8.4. The string is **`version␣␣0.3`** (two spaces).
   *Owed:* one-character change, but it is a rendered-pixel difference, so it
   should be logged as a supersession like any other.

4. **`docs/standards/MAZECREATOR-VISUAL-SPEC.md`, watermark row — "right-aligned to
   x ≈ 682".**
   *What the evidence shows:* the ink's right edge lands at stage x **685.5**
   (AA-inclusive), i.e. ≈684–685 true. `Editor.as:313`'s field
   (`x=482, width=200` → right edge 682) is ~3 px short. Minor, but it is a
   pinned constant and it is wrong.

### Still unknown / stays on the want-list

* **VE 2 — editor error panel.** `[NOT VISIBLE]` in all 11 frames, verified by
  a sliding-window search for dark blocks. **Stays WANTED, unchanged.** The
  M3 invention at `Editor.as:322-332` (dark rounded box, `#444444` at 90 %,
  400×80 at stage (144,160)) and the copy at `:283-285` still have zero
  authority.
* **VE 1 — `tankSpawnToolSelect.jpg`.** Still unseen. Also unseen *in this set*:
  `mazeConstructToolDeselect` and `crateSpawnToolSelect` (the archive shot has
  those two). **Between the archive shot and these frames, 5 of 6 states are now
  visually held.**
* **The `Maze name` placeholder state** (`srv/index.php:3673-3674`). All four
  sessions show a typed name. The `#666666` half of the colour flip is
  unverified against any pixel.
* **Arial vs Helvetica** (S108). Not resolvable at 1.4–2.1× upscale of video.
* **Whether the heading is SWF-drawn or page-drawn.** See contradiction 1.
* **The width term of the cell formula.** Only the height term binds in all four
  samples.
* **The `userpanel` height mapping.** The rendered panel is 460 CSS px tall;
  `srv/index.php:3619-3620` animates `userpanelContent` to 385 and
  `userpanelswrapper` to 500. Without the server-side markup (S24) I cannot
  reconcile those.

### New wants to add

* **N1 — a frame with the crate or tank tool *selected*.** The whole set is
  construct-selected because `showMazeCreatorToolsAndTitle` forces it
  (`srv/index.php:3664`) and nobody in these clips clicked a spawn tool with the
  toolbar in view. *Trigger:* any editing footage where the user places a tank or
  a crate — the strip is on screen throughout; two adjacent frames give
  `tankSpawnToolSelect` and `mazeConstructToolDeselect` together.
* **N2 — a hover state on the tool icons.** `A-toolbar-three-tool-icons-visible.png` and `A-editor-panel-highlight-outside-maze.png` are
  pixel-identical across the strip, so no hover treatment was captured; the page
  JS sets only `src`, so if a hover exists it is CSS. *Trigger:* cursor resting
  on a tool icon.
* **N3 — the title input *focused but not selected*.** Settles the
  `[UNCERTAIN]` cream/tan ring in `A-toolbar-row-crop-run-around-the-world.png` (focus style vs chroma artefact)
  and would also catch the placeholder if the user tabs into an empty field.
* **N4 — a frame of the editor mid-fade (`fadeOut`).** Settles whether the
  centred heading belongs to the SWF or to the page — the single cheapest
  experiment for contradiction 1.
* **N5 — a maze whose width binds the cell formula** (very wide, very short,
  e.g. 18 × 2 or 18 × 3). Pins the `576` term that all four current samples
  leave free.

---

## Recommended edits to existing docs (not applied)

**`docs/standards/VISUAL-EVIDENCE-WANTED.md`**

* Entry **1 (Tool icon states)** — keep status `PARTIAL` but rewrite the body:
  > The screenshot `archive/ia-items/extracted/images/Making a maze.png` holds
  > 3 of 6 states: wall=Deselect, crate=**Select**, tank=Deselect.
  > `manualevidence/UI/A-toolbar-three-tool-icons-visible.png`, `A-editor-panel-highlight-outside-maze.png`, `A-editor-howto-step6-or-just-click.png`
  > and `A-toolbar-row-crop-run-around-the-world.png` hold the complementary set —
  > wall=**Select**, crate=Deselect, tank=Deselect — at ≈44 CSS px, in three
  > independent sessions. **5 of 6 states are now visually held; only
  > `tankSpawnToolSelect.jpg` has never been seen.** Deselect is *exactly*
  > greyscale (max R−B delta = 1 over the whole tile); Select is full colour.
  > Needed: one frame with a spawn tool active.
* Entry **2 (Error panel)** — add: *"Checked against 11 frames of editor footage
  (2026-08-04 sweep, topic A): absent from all of them. Still WANTED."*
* Entry **3 (Save flow after ✓)** — `WANTED` → **`PARTIAL`**:
  `manualevidence/UI/A-toolbar-confirm-click-midfade.png` catches the row ≈165 ms into the 200 ms
  fade with the accept ✓ already at full opacity, and
  `A-editor-preview-mode-lone-tick.png` shows the resting post-save state. Still needed: the frames
  *between* them, and whether anything else flashes.
* Entry **4 (Maze preview / garage mode)** — `WANTED` → **`PARTIAL`**:
  `A-editor-preview-mode-lone-tick.png` shows the preview state — the saved maze drawn full-size
  with the owner's name above it and a single accept ✓ bottom-right, no input,
  no tools, no cancel. Still unknown: slots, thumbnails, a "create new" affordance.
* Entry **6 (Maze placement rule)** — needs rewriting around the dynamic-cell
  finding rather than the half-cell one; add the four-sample table.
* Entry **7 (Title + watermark typography)** — `PARTIAL` → **`PARTIAL` with the
  face narrowed**: add *"Verdana and Tahoma are excluded — the digit `1` has no
  foot bar in `A-editor-preview-mode-lone-tick.png` and `A-toolbar-confirm-click-midfade.png`. The face is an
  Arial/Helvetica-class grotesque, i.e. `_sans` is a defensible rendering.
  Arial vs Helvetica remains unresolvable. Also: the watermark carries two
  spaces (`version␣␣0.3`) and its ink right edge is at stage x ≈685, not 682."*
  And a new sub-line: *"the centred heading is NOT the maze name."*
* **S39 (Maze-creator toolbar row)** — `MED` recoverability, currently "chrome/
  spacing unconfirmed" → **essentially FETCHED**: full CSS-px geometry now
  measured in three sessions (see this document's geometry table). Remaining gap:
  the placeholder state and the focus treatment.
* **S79 (Tick/cross sprites)** — add: *"the maze-creator ✗/✓ pair is now
  measured (`#f43838` body / `#8b2b2a` outline; `#66f219`→`#4ab30d` gloss).
  `srv/images/v.jpg` and `x.jpg` are held **O** (LEDGER 133-134) — **compare
  them against `manualevidence/UI/A-toolbar-three-tool-icons-visible.png` at 34.8×32.6 and 30.5×35.5
  CSS px; if they match, S79's 'usage sites unconfirmed' closes for these two
  files.**"* I could not run that comparison here: `srv/images/` is not in the
  staged tree.
* **S108 (Editor title font: device vs embedded)** — add the `1`-without-a-foot
  observation and the weak subpixel-fringing hint; keep `LOW`.
* Add **N1–N5** above as new entries.

**`docs/standards/MAZECREATOR-VISUAL-SPEC.md`**

* `CELL` row: replace `32 px` with the formula and the four-sample table; note
  that 32 is the value the formula returns for the spec's own 13×8 sample.
* `Maze placement` row: add the one-cell editable margin ring.
* `Title text` row: keep `#666666`; change "≈18 px" to "18–20 px (best estimate
  19)"; **add that the string is the owner's username, not the maze name.**
* `Watermark` row: change `x ≈ 682` to `x ≈ 685`; add `letter-spacing ≈1.88 px`
  and `two spaces between "version" and "0.3"`.
* `Known unknowns`: strike "exact font faces" down to "Arial vs Helvetica within
  the `_sans` class".

**`DECISIONS.md`** — a new dated entry recording the supersessions: the title
source, the dynamic cell size, the watermark string, and the watermark
right-align target, each with what the invention was and what the pixels showed
(per THE OVERHAUL RULE step 3).

**`LEDGER.tsv`** — rows for the 11 files as M2 with the source-video URL,
uploader, date and timestamp once Ethan supplies them. All six tool JPGs stay
`known-lost`: these frames are *pictures of* the sprites, not their bytes, and
nothing here may be promoted above M2 (guide §6.5).
