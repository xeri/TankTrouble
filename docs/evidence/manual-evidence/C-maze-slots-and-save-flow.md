# Visual evidence — maze preview slots, editor open/close transitions and save flow

> Analysis of 10 evidence files under `manualevidence/`.
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)

---

## Scope and provenance

Ten captures, all of the logged-in `?garage` route. They fall into **two
different sessions, on two different accounts, in two different years**, and
they must not be merged:

**Session A — account `revengexx1` (9 files, `C-garage-before-maze-panel` → `afterrfadein…`).**
A second userpanel for account `creed` sits beside it. Left column reads
`Visits … 17858418 / Today: 9805 / Online: 283 / Tank owners: 518873 /
Logged in: 95`; the Scrapyard flip-counter reads 665 70x xxx. Nine frames,
in the order given in the assignment.

**Session B — account `cam12win` (1 file, `C-empty-slot-maze3-cam12win.png`).**
One userpanel. `Visits … 16133602 / Today: 8434 / Online: 568 / Tank owners:
404381 / Logged in: 167`; Scrapyard 59 178 251.

Both are **video frames, not screenshots**:

- `[OBSERVED]` `C-garage-before-maze-panel.png` carries a burned-in title card in the top-left
  reading `…rouble Mazez` (white, semi-transparent, over the page) —
  a video title, almost certainly "…Tank Trouble Mazez".
- `[OBSERVED]` `C-empty-slot-maze3-cam12win.png` carries `…ake A Tank Trouble
  Maze!` in the same position, mid-fade — a tutorial title card.
- `[OBSERVED]` `C-maze-icon-clicked.png` carries a centred caption strip at the
  very bottom reading `You're a manager` — a subtitle/caption track, not page
  content.
- `[OBSERVED]` A bright-yellow ring follows the cursor in
  `C-open-transition-height-phase`, `C-preview-boot-state`, `C-slot-hover-green-glow`,
  `C-editor-opened-on-slot1`, `afterclickingonconfirm…`, `afterrfadein…` and
  `C-empty-slot-maze3-cam12win` — a screen-recorder click highlight, brightest
  right after a click and fading over the following frames. It is a recording
  artifact and is masked out of every measurement below.

**Both sessions predate the 2017–2018 target era, probably by years.**
`DIVERGENCES-SERVED.md` §5 pins the latest archived scrapyard total at
`scraps=1785664230` from `includes-tree/20160126_getScrapyard.php`. Session A
shows **665 708 045** and session B **59 178 251** — both far below the
2016-01-26 value of a monotonically accumulating counter.
`srv/index.php:1069,2654,…` freeze the 2018-12 visit box at
`68374157 … Tank owners: 1675298`; session A shows 17 858 418 / 518 873 and
session B 16 133 602 / 404 381. `[INFERRED]` Session A is pre-2016-01;
session B is earlier still (roughly a 1.7 M-visit gap ≈ 6 months at the
~9 000/day rate its own box reports). **Falsifier:** any evidence that the
scrapyard total was ever reset. Consequence: everything below describes
`mazeCreator_v0.3.swf` as it behaved *before* the era window, and the
possibility of a later change (in particular to the slot count) is not
excluded by these frames. `DEDUCE.md:366` notes the binary was "frozen for
7½ years", which makes a change unlikely but not impossible.

### Capture order is corroborated by an in-frame clock

The assignment gives the owner's crop-save order. That is not evidence of
frame order, so it was checked against the Scrapyard flip-counter, which
only ever climbs:

| # | file | Scrapyard reading | `[MEASURED]` |
|---|---|---|---|
| 1 | `C-garage-before-maze-panel.png` | 665707985 | last plate mid-flip |
| 2 | `C-maze-icon-clicked.png` | 665708045 | last plate mid-flip |
| 3 | `C-open-transition-width-phase.png` | 665708045–046 | |
| 4 | `C-open-transition-height-phase.png` | 665708046–047 | |
| 5 | `C-preview-boot-state.png` | 665708055 | plates settled |
| 6 | `C-slot-hover-green-glow.png` | 665708063–064 | |
| 7 | `C-editor-opened-on-slot1.png` | 665708066–068 | |
| 8 | `afterclickingonconfirm….png` | 665708204 | plates settled |
| 9 | `C-after-confirm-preview-returned.png` | 665708208 | last plate mid-flip |

`[MEASURED]` Strictly monotonic. **The owner did not step backwards inside
this set**; the filename order is the temporal order. (Frame 10,
`C-empty-slot-maze3-cam12win.png`, is a different video and sits outside this
sequence.)

`[INFERRED]` Relative spacing: frames 2→4 span **1–3 ticks** while 1→2 spans
60 and 7→8 spans ~137. Whatever the tick rate, the open animation occupies
under 1/40 of the interval the editing session occupies — consistent with the
1.7 s scripted sequence at `srv/index.php:3613-3622` and a ~2 min edit at
≈1 tick/s. The rate itself is not pinned (the only archived velocity,
`0.0071382502652744`, is a 2015 sample and `DIVERGENCES-SERVED.md` §5 reads it
as one scrap per ~140 s, which these frames plainly contradict) so **no timing
claim below rests on the counter**; the timings come from the panel geometry.

### Scale derivation (used throughout)

The page is fixed-width: `srv/index.php:3479-3482` gives a 1312 px content
div containing a 1002 px float with `#centerColumn` at **692 px**, and
`openMazeCreator` (`srv/index.php:3613`) tweens `userpanel-<user>` from
**224 px to 692 px** while `closeMazeCreator` (`:3633`) returns it to 224.
Card border centres were located to sub-pixel precision by ink-weighted
centroid of the border dip.

| frame | card left | card right | width (capture px) | card top | card bottom | height (capture px) |
|---|---|---|---|---|---|---|
| `C-garage-before-maze-panel` panel 1 | 447.95 | 801.94 | **353.99** | 118.98 | 399.15 | **280.17** |
| `C-garage-before-maze-panel` panel 2 | 820.45 | 1174.02 | 353.57 | 118.98 | 399.15 | 280.17 |
| `C-maze-icon-clicked` | 450.13 | 803.48 | **353.35** | 118.98 | 399.29 | 280.31 |
| `firstanimation…` | 265.84 | 1364.26 | **1098.42** | 118.98 | 404.32 | **285.34** |
| `secondanimation…` | 278.87 | 1377.27 | 1098.40 | 118.98 | 853.44 | **734.46** |
| `C-preview-boot-state` | 247.88 | 1346.32 | 1098.44 | 118.97 | 853.32 | 734.35 |
| `C-slot-hover-green-glow` | 249.88 | 1348.32 | 1098.44 | 116.97 | 851.31 | 734.34 |
| `C-editor-opened-on-slot1` | 251.90 | 1350.32 | 1098.42 | 117.95 | 852.37 | 734.42 |
| `afterclickingonconfirm…` | 248.72 | 1347.51 | 1098.79 | 118.97 | 853.41 | 734.44 |
| `afterrfadein…` | 247.72 | 1346.51 | 1098.79 | 118.97 | 853.41 | 734.44 |
| `emptymaze…,maze3` (session B) | 268.98 | 1702.18 | **1433.20** | 5.74 | 963.23 | **957.49** |

`[MEASURED]` **Session A scale s = 1098.44 / 692 = 1.5873 capture px per CSS
px.** Cross-check, non-circular: the *collapsed* card then measures
353.99 / 1.5873 = **223.0 CSS px** against the specified 224 (border centres,
so 223 is the expected reading). Second cross-check: the width delta
744.43 / 468 = 1.5907 and the height delta 454.29 / 286 = 1.5885 — two
independent O-specified deltas agreeing to **0.14 %**.
`[MEASURED]` **Session B scale s = 1433.20 / 692 = 2.0711.** Cross-check: the
maze-slot pitch ratio between sessions is 415.5/318.5 = 1.30455 against a card
ratio of 1.30474 — 0.015 % apart, so the two captures differ by a pure uniform
scale with no anamorphic stretch.

Every "CSS px" figure below means *CSS pixels of the page*, which is also
*pixels of the 688 × 400 box the SWF is embedded into* (`srv/index.php:3617`).
Where that box maps onto the SWF's internal stage coordinates is discussed
under Finding 8 — it is not as certain as `mazecreator-visual-spec.md`
assumes.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| 1 | The maze preview is a **row of exactly three slots**, centred, 200.6 px pitch, 125.3 px square box each, captions beneath. Two sessions, two accounts, two eras agree. | `[MEASURED]` | VE **4**, **S43**, S38 | Yes — `Editor.as` preview is a single click-anywhere maze; rewrite owed |
| 2 | An **empty slot renders as a flat grey square (#d1d1d1) with a 1 px darker border and the words "Maze 3" centred inside**, and **no caption underneath**. There is no separate "create new" affordance. | `[OBSERVED]`+`[MEASURED]` | VE **4**, **S43** | Yes — nothing in the rebuild draws an empty slot |
| 3 | Slot captions are the **maze names**, rendered by the SWF in a fixed-width (~145 px) centred field that **hard-clips** overlong titles. Verbatim transcriptions below. | `[MEASURED]` | VE **4**, S38 | Yes — `_root.mazeName` currently drives a stage title; it drives the caption |
| 4 | Thumbnails are **true miniature renders of the real maze geometry** — walls, floor, tank and crate spawns — scaled to fit the slot box, so **each thumbnail has a different cell size**. Verified by overlaying thumbnail 2 on the same maze open in the editor. | `[MEASURED]` | VE **4** | Yes — no preview renderer exists |
| 5 | Save flow after the green ✓: **no spinner, no dialogue, no flash.** Tools/title/✗ vanish, the accept ✓ appears in the same corner, the preview returns — and **the slot that was just saved is blank for seconds while the other two are already drawn**. | `[MEASURED]` | VE **3**, S43 | Yes — `Editor.as:267-271` re-renders synchronously |
| 6 | The open transition is **two distinct, sequential, non-overlapping axes** — width first, then height — not a diagonal tween. In `firstanimation…` the width tween is 100 % done and the height tween 1.1 % done. | `[MEASURED]` | **S37**, VE **8** | Confirms `srv/index.php:3613/3619/3620` |
| 7 | Card geometry confirms the **maze-flow** numbers (content 99→**385**, wrapper 214→**500**, Δ = 286) and rules out the paint-flow numbers (Δ = 146). Width Δ = 468 confirmed; the panel moves **116.3 px left and 351.7 px right**. | `[MEASURED]` | **S37**, S24, S29 | Confirms; corrects the brief's premise |
| 8 | The editor **does not use a fixed 32 px cell**. Cell size = `min(576/(w+2), 320/(h+2))` CSS px — four mazes across three captures fit to ≤0.26 %. | `[INFERRED]` (strong) | VE **6**, spec `CELL`, `LATTICE` | Yes — `MazeRenderer.CELL`, `LATTICE_W/H`, `loadIntoLattice` |
| 9 | The grey centred name at the top of the maze panel is the **page's userpanel username label**, not an SWF title: identical pixel row in the collapsed garage panel, visible while the SWF is at α≈0, and it shows the *username* while a different maze name sits in the input field. | `[MEASURED]` | VE **7**, spec "Title text" | Yes — `Editor.as:305-310,338` |
| 10 | Rollover on a slot draws a **bright green glow tracing the maze silhouette** (not a rectangle) and turns the caption green; cursor is a pointing hand. | `[MEASURED]` | VE **4**, S42 | Yes — no hover state exists |
| 11 | Clicking the maze icon fades out **the entire sibling userpanel**, not just the clicked panel's icons — behaviour absent from the archived JS. | `[MEASURED]` | S24, S25, S37, S40 | New requirement for phase-4 markup |
| 12 | The classic `userpanelMaze-` icon is **visible**: a greyscale isometric tray with raised maze walls, 3rd of 4 icons. | `[OBSERVED]` | **S46**, S25 | Fills a hole |
| 13 | Preview thumbnails use a **flat single-tone floor**, not the editor's two-tone mix. | `[MEASURED]` | VE **8a** | Narrows 8a to the editor only |
| 14 | No error panel in any of the ten frames. | `[NOT VISIBLE]` | VE **2** | Stays WANTED |
| 15 | No delete/clear affordance and no unsaved-changes warning observable. | `[NOT VISIBLE]` | **S44**, **S45** | Stay open; absence recorded |

---

## File-by-file analysis

### `UI/C-garage-before-maze-panel.png` (1616 × 1055, captured 16:57:18) — [image](./UI/C-garage-before-maze-panel.png)  *(was `garage1.png`)*

**Filename claim (repo owner):** none beyond "garage" — nothing to corroborate.

**What is drawn**

- `[OBSERVED]` The `?garage` route, logged in, with the wrench tab raised in
  the six-tab nav strip.
- `[OBSERVED]` **Two userpanels side by side** in `#centerColumn`. Left panel
  = `revengexx1`, right panel = `creed`. Each is a white card with a thin
  light-grey border, rounded corners.
- `[OBSERVED]` Each panel contains, top to bottom: a centred grey **username
  label**; a rendered **tank** (revengexx1's is a Halloween skin — pumpkin
  turret, skull accessory, gold star badge, red tracks; creed's is a plain
  brown/tan tank with a white accessory); and a **strip of four icons** along
  the bottom.
- `[OBSERVED]` The four icons, left to right: (1) a spanner/wrench with a
  small tag reading `beta`; (2) a silver trophy; (3) **a greyscale isometric
  tray whose raised interior walls form a maze** — the maze-creator icon;
  (4) a sheet of paper with a yellow warning triangle overlaid.
- `[OBSERVED]` `srv/index.php:3501-3534` names five icons
  (`userpanelPaint- / Maze- / SherifStar- / Form- / Stats-`) but guards
  `SherifStar` with `if (document.getElementById('userpanelSherifStar-'+user)
  != null)`. Four icons here, on both panels, is consistent with a
  non-moderator account.
- `[OBSERVED]` Below the panels: `Sign up another tank` heading, the sign-up
  form (`Name your tank` / `Something awesome!`, `Password` / `Something
  secret…`, `Password`, `Email address` / `So you can recover your password if
  you forget it`), then `Customize your tank` and two rows of spray cans
  flanking a grey tank.
- `[OBSERVED]` Left column: Scrapyard counter, Log In box, two user cards
  (`creed  Exp. 7820`, `revengexx1  Exp. 10500`), `Need Help? Check the
  F.A.Q.`, Visits box. Right column: `Top 10 Exp.` list with a
  `Weekly | Friends` tab pair below it, a Facebook Like button reading
  `8.2k`, `Tell a Friend`, an `Available on the App Store` badge, a red hoodie
  product image, and the `Got Feedback?` box. These belong to topics D/E/F and
  are not analysed here beyond noting they date the frame.

**Measurements**

| quantity | capture px | CSS px (s = 1.5873) |
|---|---|---|
| panel 1 border box | 447.95 → 801.94 | width **223.0** (spec 224) |
| panel 2 border box | 820.45 → 1174.02 | width 222.7 |
| gap between panels | 18.51 | **11.7** |
| panel `left` within `#centerColumn` | 185.07 | **116.3** |
| panel 2 `left` | 557.1 | **350.9** |
| card top → bottom | 118.98 → 399.15 | height **176.5** |
| username label ink box | x 543–699, y 134–160 | 98.3 × 16.4 |
| icon centres (panel 1) | 494.0, 570.5, 653.0, 733.0 | pitch **≈50.2** |
| maze icon (3rd) box | x 618–688, y 328–391 | **44.7 × 39.7** |

`[MEASURED]` Username label darkest sample `#545454` (blur floor; the source
is plausibly `#666666`); ink extent 27 capture px including the `g` descender
→ ≈17.0 CSS px ascender-to-descender → a ~18 px face.

**Links to the program**

- Confirms `srv/index.php:3613` / `:3633`'s 224 px collapsed width to within
  1 px, and gives the real `position` argument passed to
  `closeMazeCreator(user, position)` for a two-user row: **116.3** for the
  left panel, **350.9** for the right.
- **S46 (garage maze-icon art)** — the icon is now *seen*. It is plainly not
  the HTML5-tree `mazeCreator*.png` files: it is a greyscale 3-D tray, not a
  flat glyph. Status `WANTED` → **PARTIAL** (seen at 44.7 × 39.7 CSS px in a
  compressed video frame; the bytes are still lost).
- **S25 (userpanel icon strip)** — four of five icons captured in their
  *enabled* state. Status `WANTED` → **PARTIAL**. The fifth (sherif star) is
  absent because the account is not a moderator, which itself confirms the
  conditional at `srv/index.php:3515`.
- **S24 (the userpanel itself)** — first sight of it. Contents, ordering and
  the 224 px box are now evidenced.

**What this does NOT show**

The disabled/faded icon art (that is the next frame), the fifth icon, any
maze data, the paint facility, or the hover state of any icon.

---

### `UI/C-maze-icon-clicked.png` (1617 × 1074, captured 16:58:07) — [image](./UI/C-maze-icon-clicked.png)  *(was `clickintomaze.png`)*

**Filename claim (repo owner):** "click into maze" — **corroborated**: the
cursor sits on the maze icon and the opening sequence has visibly begun.

**What is drawn**

- `[OBSERVED]` The cursor (standard arrow, tip ≈ (658, 359)) sits inside the
  box the maze icon occupied in `C-garage-before-maze-panel` (x 618–688, y 328–391, allowing for
  this frame's +2 px crop offset). The icon itself is no longer drawn.
- `[OBSERVED]` The `revengexx1` panel is still card-shaped and unmoved, but
  **empty**: the tank is gone and all four icons are gone.
- `[OBSERVED]` The username label is drawn **with a blue text-selection
  highlight** — the click selected the label text.
- `[OBSERVED]` The **entire `creed` panel** — its border, its username label,
  its tank and all four of its icons — is faded to a ghost.

**Measurements** (ink = Σ(255 − grey) over a fixed box; a proxy for alpha)

| element | `C-garage-before-maze-panel` ink | `C-maze-icon-clicked` ink | ratio |
|---|---|---|---|
| panel 1 tank | 2 809 157 | 27 091 | **0.010** |
| panel 1 icon strip | 1 077 237 | 53 346 | **0.050** |
| panel 2 tank | 2 007 995 | 20 567 | **0.010** |
| panel 2 username label | 85 324 | 8 995 | **0.105** |
| panel 2 icon strip | 1 079 707 | 109 191 | **0.101** |
| panel 1 username label | 168 168 | 439 157 | 2.61 (selection fill) |

`[MEASURED]` Panel 1 border box = 353.35 capture px (222.6 CSS) against
353.99 (223.0) in `C-garage-before-maze-panel` — a difference of −0.4 CSS px, i.e. **the width
tween has not started**.

`[INFERRED]` Placement on the specified timeline: `openMazeCreator`
(`srv/index.php:3611`) sets `fadeOut=true` on the tank SWF at t = 0 and
`disableUserPanelIcons` (`:3615`, → `:3503-3534`, 200 ms linear) starts at
t = 0; the width tween starts at **t = 700 ms** (`:3613`). The tank is fully
gone (a 15-frame @ 25 fps fade = 600 ms, per the `:3637` comment) and the
width has not moved, so **t ≈ 600–720 ms**. Falsifier: any evidence the tank
fade is not 600 ms.

**Links to the program**

- **S40 (`userSettingsTank-` visibility juggle)** — the tank goes out by
  **fade**, not by a pop: `SetVariable("fadeOut","true")` at `:3611` and only
  then `style.visibility="hidden"` at t = 700 ms (`:3617`). At t ≈ 650 ms the
  tank is already at ~1 % ink, so the fade is complete *before* the hide.
  Status `WANTED` → **PARTIAL** (open half answered; the restore on collapse
  is still unseen).
- **S25** — gives the *faded* state of the four icons (opacity 0), the other
  half of the pair `C-garage-before-maze-panel` provides.
- **S24 / S37 — NEW, not in the archived JS.** `disableUserPanelIcons(user)`
  touches only the clicked user's icons. Nothing at `srv/index.php:3609-3624`
  fades the *other* userpanel, yet the whole `creed` panel is at ~10 %.
  `[INFERRED]` the fade must live in the SAJAX-generated `x_updateUserPanels`
  markup's `onclick` (the HTML of which is, per S24, "zero bytes archived") or
  in a helper it calls. **The phase-4 markup reconstruction owes this
  behaviour.** Falsifier: a frame showing a sibling panel staying opaque
  through an open.

**What this does NOT show**

Which of the four icons is `userpanelPaint-` versus `userpanelStats-`; the
icons' *hover* art; the sherif star; any part of the maze SWF (it is created
at t = 700 ms, after this frame).

---

### `UI/C-open-transition-width-phase.png` (1626 × 1080, captured 16:58:41) — [image](./UI/C-open-transition-width-phase.png)  *(was `firstanimationcardexpandsright.png`)*

**Filename claim (repo owner):** "first animation card expands right" —
**corroborated, with one correction**: the horizontal phase is real and is
first, but this frame catches it *finished*, not in progress, and the card
expands in both horizontal directions (mostly right).

**What is drawn**

- `[OBSERVED]` One card only, spanning the full centre column. The `creed`
  panel is gone entirely.
- `[OBSERVED]` The card is short — the same height as the collapsed panel.
- `[OBSERVED]` Its only content is the blue-selection-highlighted username
  `revengexx1`, re-centred on the new card centre, and the cursor.
- `[OBSERVED]` **No green ✓.** **No maze content, no watermark.**

**Measurements**

| quantity | capture px | CSS px |
|---|---|---|
| card width | 1098.42 | **692.0** (target reached) |
| card height | 285.34 | **179.7** |
| height vs collapsed (176.5) | +5.17 | **+3.2** |
| fraction of the 286 px height growth | — | **1.12 %** |
| ink inside the card | x 659–896, y 124–397 only | label + cursor |
| watermark zone minimum grey | 252.7 (of 255) | nothing drawn |
| green pixels in the ✓ corner | **0** | ✓ not yet shown |

`[INFERRED]` `srv/index.php:3613` runs the width tween at t = 700 ms for
500 ms (`Fx.Transitions.Quad.easeInOut`); `:3619/:3620` run the height tweens
at t = 1200 ms. Width complete ⇒ t ≥ 1200 ms. Height at 1.12 %: for
`Quad.easeInOut` the first half is `p = 2f²`, so f = 0.075 ⇒ 37 ms in ⇒
**t ≈ 1237 ms (± ~20 ms)**. Falsifier: a different easing than the one the
source states.

**Links to the program**

- **S37** — first direct confirmation that the two tweens do **not** overlap.
  At t ≈ 1237 ms one axis is at 100 % and the other at 1 %. A single diagonal
  tween is impossible.
- **VE 8 (fade transitions)** — confirms that the SWF is created (t = 700 ms,
  `:3617`) but contributes **zero ink** at t ≈ 1237 ms, i.e. it boots hidden.
  That matches `Editor.as:56` (`if (ExternalInterface.available) _root._alpha
  = 0`) exactly.

**What this does NOT show**

Any intermediate width value (the frame is past the width tween), the easing
curve itself, or any SWF pixel.

---

### `UI/C-open-transition-height-phase.png` (1638 × 1062, captured 16:58:58) — [image](./UI/C-open-transition-height-phase.png)  *(was `secondanimationcardexpandsdown.png`)*

**Filename claim (repo owner):** "second animation card expands down" —
**corroborated**, again caught at the end of the phase.

**What is drawn**

- `[OBSERVED]` The card is now full width **and** full height — a large empty
  white rectangle.
- `[OBSERVED]` The **green ✓ is present**, bottom-right inside the card.
- `[OBSERVED]` Still no maze, no thumbnails, no watermark, no title text other
  than the selection-highlighted username.
- `[OBSERVED]` The cursor sits low-left with a bright recorder ring.

**Measurements**

| quantity | capture px | CSS px |
|---|---|---|
| card width | 1098.40 | 692.0 |
| card height | 734.46 | **462.7** |
| height growth from collapsed | 454.29 | **286.2** |
| ✓ bounding box | x 1319–1361, y 780–833 | **26.5 × 34.0** |
| ✓ darkest-green core (mean of 150 px) | `(0.6, 191.0, 6.1)` | — |
| same core in `C-preview-boot-state` | `(0.5, 192.8, 4.9)` | identical within noise |
| card interior minimum grey (x 400–1200, y 200–700) | **251.0** | no SWF ink |
| watermark zone minimum grey | 249.7 | no watermark |

`[INFERRED]` `srv/index.php:3622` fades `userpanelAcceptMaze-` in at
t = 1700 ms over 200 ms. The ✓ is at full opacity ⇒ **t ≳ 1900 ms**.
`srv/index.php:3619`'s `onComplete` sets the SWF's `fadeOut` to `'false'` at
t = 1700 ms and `:3637`'s comment gives the fade as 15 frames @ 25 fps
(600 ms), so at t = 1900 ms the SWF ought to be ~33 % opaque. The preview
floor tone is ≈ `#d1d1d1`; at 33 % over white that would read ≈ 240, and the
card interior minimum is 251. `[MEASURED]` **The SWF is at ≤ ~10 % alpha.**
`[INFERRED]` therefore the SWF's own fade starts *later* than the 1700 ms
`onComplete` — most simply because the SWF written at t = 700 ms
(`srv/index.php:3617`) has not finished loading and initialising when the
`SetVariable` fires. Falsifier: a frame at t ≈ 1900 ms with the SWF at ~1/3
opacity.

**Links to the program**

- **S28 (accept "✓" buttons)** — the `userpanelAcceptMaze-` art is now seen:
  a hand-drawn bright-green tick with a black outline and a lighter green
  highlight along the upstroke, ≈**26.5 × 34.0 CSS px**, its right edge
  ≈10.2 CSS px inside the card's right border and its bottom ≈12.8 CSS px
  above the card's bottom border. Session B measures the same tick at
  27.0 × 34.3 CSS px — cross-session agreement. Status `WANTED` →
  **PARTIAL** (one of four variants, at video resolution).
- **S37 / VE 8** — pins the ✓ fade-in to the specified 1700 ms slot and
  proves the SWF fade lags it.

**What this does NOT show**

The SWF fade curve (linear vs eased) — two blank frames cannot distinguish
them. VE 8 stays `PARTIAL`.

---

### `UI/C-preview-boot-state.png` (1599 × 1053, captured 16:59:13) — [image](./UI/C-preview-boot-state.png)  *(was `fadeintothispage.png`)*

**Filename claim (repo owner):** "fade into this page" — **corroborated**:
this is the state the SWF fades up into, and it is the boot/preview state
that VE entry 4 asks for.

**This is the single most valuable frame in the set.**

**What is drawn**

- `[OBSERVED]` The full-size card, with, top to bottom:
  1. the centred grey username `revengexx1` (selection highlight now cleared);
  2. **a horizontal row of three maze thumbnails**, evenly spaced;
  3. **a caption under each thumbnail**, on one shared baseline;
  4. the pale `version 0.3` watermark, bottom-right;
  5. the green accept ✓, bottom-right below the watermark.
- `[OBSERVED]` **Nothing else.** An exhaustive ink map of the card interior
  returns exactly five row bands — y 123–161 (username), 332–501
  (thumbnails), 547–564 (captions), 749–763 (watermark), 779–847 (✓) — and
  nothing between or beside them. **No toolbar, no title input, no ✗, no
  scroll arrows, no paging, no "new maze" button, no delete control, no
  error panel.**
- `[OBSERVED]` Each thumbnail is a small maze: light-grey floor cells, darker
  grey wall lines, small blue-violet squares (tank spawns) and small amber
  squares (crate spawns). The three silhouettes are different and
  non-rectangular.

**Measurements — the slot row**

Slot art bounding boxes (capture px), and the wall-gridline pitch measured by
ink-weighted peak finding along both axes:

| slot | art box x | art box y | w × h (capture) | pitch (capture) | cells | pitch (CSS) |
|---|---|---|---|---|---|---|
| 1 | 377–580 | 332–501 | 204 × 170 | 16.50 | **12 × 10** | 10.40 |
| 2 | 696–898 | 338–497 | 203 × 160 | 15.11 | **13 × 10** | 9.52 |
| 3 | 1014–1217 | 347–483 | 204 × 137 | 13.10 | **15 × 10** | 8.25 |

| derived quantity | capture px | CSS px |
|---|---|---|
| slot centres (x) | 478.5, 797.0, 1115.5 | 145.0, 345.2, 545.5 from the card's left border |
| **slot pitch** | 318.5, 318.5 | **200.7** |
| middle slot centre vs card centre (797.10) | −0.10 | dead centre |
| slot vertical centres | 416.5, 417.5, 415.0 | all on one line, **187.3 below the card top** |
| left margin (card border → slot-1 box edge) | 130.9 | **82.5** |
| right margin (slot-3 box edge → card border) | 131.1 | **82.6** |
| caption ink band | y 549/550–563 | ascender top **271.2 below the card top** |
| watermark ink `version 0.3` | x 1216–1341, y 749–763 | digits 8.8 px cap → **≈12 px face** |

`[MEASURED]` The three boxes plus gaps close on the panel width:
82.5 + 125.3 + 74.9 + 125.3 + 74.9 + 125.3 + 82.6 = **690.8** against 692.
There is no room for a fourth slot and no evidence of one.

**Measurements — the captions (verbatim)**

| slot | caption, transcribed verbatim | width (capture px) | note |
|---|---|---|---|
| 1 | `Run Around The WORLD` | 202 | complete |
| 2 | `One Path to Destruction` | 201 | complete |
| 3 | `Battlefield of Awesomness 2` | 230 | **clipped** — see below |

`[MEASURED]` Caption 3's final glyph is cut by a hard vertical edge at
x ≈ 1231: at x = 1230 the glyph is still at ink 191–250, at x = 1231 it is
238–255 and at x = 1232 the row is clean white. The cut is 115.5 capture px
right of the slot centre; caption 3 also starts 114.5 px left of it. So the
caption sits in a **centred text field ≈231 capture px = 145.5 CSS px wide
that clips rather than ellipsises**. Captions 1 and 2 (202 and 201 px) fit
inside it and are unclipped.
`[UNCERTAIN]` The clipped glyph reads as a `2` (its upper curve and a lower
stroke are present) but only its left ~40 % renders, so it could be another
character and the title could continue past it. `[OBSERVED]` The spelling
`Awesomness` — one `e` short of "Awesomeness" — is the user's own, and is
reproduced here as drawn.

`[MEASURED]` Caption ink is darkest at `#707070`/`#787878` (blur floor, source
plausibly `#666666`), cap height 14 capture px → 8.8 CSS px → a **≈12 px**
face. The captions sit on **one shared baseline regardless of how tall the
thumbnail above them is** (art bottoms 501, 497, 483; caption tops 550, 550,
549) — so they are anchored to the *slot box*, not to the art.

**Measurements — the thumbnail render**

`[MEASURED]` Floor fill: the dominant tones inside slot 1 are 208–214 grey,
a smooth unimodal spread with **no bimodal light/dark split**. Repeated on
session B's 18 × 10 "Epic Twister" at 14.4 px/cell, per-cell means over
174 floor cells give **209.6 ± 1.8** with the only outliers being cells whose
sample window clipped a wall. `[MEASURED]` **The preview floor is a flat
single tone; it does not reproduce the editor's `#dddddd`/`#eeeeee` mix.**

`[MEASURED]` Wall lines run 2–4 capture px wide with a core near `#8f8f8f`;
at 0.4 × editor scale a 4 px wall is sub-2 px, so the source colour cannot be
recovered — `[UNCERTAIN]`, consistent with a scaled `#444444` but not proof of
it.

`[MEASURED]` Spawn icons: blue-violet mean `(177, 178, 209)`, amber mean
`(221, 201, 148)` (session B slot 1). Compare the pinned spec values — tank
core ≈ `(175, 180, 238)`, crate core ≈ `(219, 183, 85)`. Corroborated as far
as a 6–8 px sprite in a video frame can corroborate anything.

**Links to the program**

- **VE entry 4 (Maze preview / garage mode — WANTED, vital).** Answered
  directly and in full for the states shown. Status `WANTED` → **FETCHED**
  (evidence in hand, redraw pending). The verbatim want was: *"what the
  preview actually looked like — multiple slots? thumbnails? 'create new
  maze' affordance?"* → **multiple slots: yes, exactly three; thumbnails:
  yes, real scaled renders with captions; 'create new' affordance: no separate
  control — see the next file.**
- **S43 (Multiple maze slots).** Status `WANTED` → **FETCHED**. See the
  dedicated discussion below.
- **VE entry 7 / spec "Title text"** — see Finding 9 under
  `C-editor-opened-on-slot1.png`; the top-centre text here is the *username*.
- `srv/index.php:3737-3753` (`hideMazeCreatorToolsAndTitle`) — the state this
  frame shows is exactly the post-`previewLoaded` state that function
  produces: cancel hidden, controls hidden, save hidden, **accept visible**.
- **spec `Watermark` row** — confirmed: `version 0.3`, wide letter-spacing,
  very light grey, right-aligned, ≈12 px, bottom-right. Independent
  corroboration from a second capture.

**What this does NOT show**

Whether an empty slot exists for this account (all three are full); what
happens on clicking an empty slot; whether the slot count is fixed or grows;
any hover state (that is the next frame); the SWF's fade curve.

---

### `UI/C-slot-hover-green-glow.png` (1596 × 1058, captured 16:59:42) — [image](./UI/C-slot-hover-green-glow.png)  *(was `selectmaze.png`)*

**Filename claim (repo owner):** "select maze" — **corroborated**: slot 1 is
in a highlighted state with a pointing-hand cursor on it.

**What is drawn**

- `[OBSERVED]` Identical to `C-preview-boot-state.png` except that **slot 1 is
  wrapped in a bright green glow that traces the maze's silhouette** — it
  follows every notch and protrusion of the outer floor boundary, and is not
  a rectangle, not a box, not a border on the slot.
- `[OBSERVED]` **The caption `Run Around The WORLD` is drawn in green too.**
- `[OBSERVED]` The cursor is a **pointing hand**, and its hotspot is on the
  *caption*, not on the maze art — so the clickable region includes the
  caption row.
- `[OBSERVED]` Slots 2 and 3 are unchanged and un-highlighted.

**Measurements**

`[MEASURED]` `ImageChops`-style difference against `C-preview-boot-state.png`
after registering the +2 x / −2 y crop offset: 28 463 pixels differ by more
than 45/255, and they fall in exactly three column bands — 190–222 (the
Scrapyard digits), **318–610 (slot 1 and its caption)** and a bottom band
(cursor/ads). **Slots 2 and 3 change by nothing.**

| quantity | value |
|---|---|
| glow core colour (mean of 200 greenest px) | `(60, 210, 65)` ≈ `#3CD241` |
| glow profile, outward scan at y = 430 | 255 → 250 → 232 → 204 → 177 → 153 → 136 → 112 → **67** at the silhouette edge, then into the floor tone |
| glow band width outside the silhouette | ≈9–10 capture px = **≈6 CSS px** |
| highlighted caption ink, mean | `(137, 200, 133)` |

`[INFERRED]` The soft outward ramp with no hard stroke edge is a **glow
filter** (blurred outward fill), not a drawn outline. Falsifier: a
native-resolution capture showing a crisp 1–2 px stroke.
`[UNCERTAIN]` The source green: `(60, 210, 65)` is a video-compressed sample
of a glow's darkest ring; the underlying colour is plausibly a pure
`#00CC00`/`#00FF00`, but this frame cannot distinguish them.

`[UNCERTAIN]` Whether this is a **rollover** state or a **selected** state.
The pointing-hand cursor is on it, which argues rollover; but nothing in the
set shows the same slot un-hovered-but-selected. The very next frame in
sequence has the editor open on this maze, so at minimum the highlight marks
the slot that is about to be entered.

**Links to the program**

- **VE entry 4** — supplies the *interaction* half of the preview: slots are
  individually hit-testable, they have a rollover state, and the hit area
  covers both the art and the caption. Nothing of this exists in the rebuild.
- **S42 (cursor over the editor stage)** — in *preview* mode the cursor over a
  slot is the **system hand**, not a custom cursor or tool ghost. Status
  `WANTED` → **PARTIAL** for the preview state only; the edit-state cursor is
  another topic's frames.
- **`Editor.as:183-191`** — the invented model is "any click anywhere enters
  edit". Contradicted: the hit target is per-slot.

**What this does NOT show**

What a hovered **empty** slot looks like; whether the glow animates in;
whether a second click toggles the highlight off.

---

### `UI/C-editor-opened-on-slot1.png` (1597 × 1051, captured 17:00:16) — [image](./UI/C-editor-opened-on-slot1.png)  *(was `fadeintomazeeditor.png`)*

**Filename claim (repo owner):** "fade into maze editor" — **corroborated**:
the editor is open on the maze that was highlighted in the previous frame.

**What is drawn**

- `[OBSERVED]` The card, same size as before, now containing a **single large
  maze** centred in the stage area, and, along the bottom, the editing
  chrome: a **text input containing `Run Around The WORLD`**, three tool
  icons, and a **red ✗** and **green ✓** at the right.
- `[OBSERVED]` The centred grey text at the top **still reads `revengexx1`** —
  the username — while the maze's own name sits in the input field.
- `[OBSERVED]` The `version 0.3` watermark is in place.
- `[OBSERVED]` The maze is drawn with a **two-tone floor** (unlike the
  thumbnails), 4 px-ish dark wall lines, tank spawn sprites and crate spawn
  sprites.

**Measurements**

| quantity | capture px | CSS px |
|---|---|---|
| maze art bbox | x 542–1061, y 238–668 | 327 × 271 |
| wall gridline pitch, horizontal (12 intervals) | **42.44** | 26.74 |
| wall gridline pitch, vertical (9 intervals) | **42.37** | 26.69 |
| maze size in cells | **12 × 10** | |
| maze centre vs card centre (x) | +0.4 | isotropic, centred |
| maze centre below the card top | 334.0 | **210.4** |
| floor tones (2 modes) | 236 and 244 | ≈ `#ececec` / `#f4f4f4` as captured |
| title input box | x 271–553 | **178** wide |
| three tool icons | x 569–638, 650–709, 721–793 | ≈44, 37, 46 wide |
| red ✗ | x 1227–1271, y 787–827 | **27.7 × 25.2** |
| green ✓ (save) | x 1290–1338, y ~780–833 | ≈30 × 33 |

`[MEASURED]` The two floor tones differ by ≈8 grey levels here and ≈12 in the
sibling `A-toolbar-confirm-click-midfade.png`; the spec's `#dddddd`/`#eeeeee` differ by 17.
Video gamma flattens the contrast but the **two-tone structure is present** —
the spec's floor-tone finding is corroborated qualitatively.

`[MEASURED]` The save ✓ (x 1290–1338) sits within ~5 capture px of where the
accept ✓ sits in preview mode (x 1287–1330). **The two green ticks occupy
essentially the same corner**, which is why the cursor does not move between
the save click and the post-save frames.

**Links to the program**

- **Finding 9 — the top-centre text is the page's username label, not an SWF
  title.** Three independent arguments, all `[MEASURED]`:
  1. In `C-garage-before-maze-panel.png`, with **no maze SWF loaded at all**, the label occupies
     capture rows **134–160**. Here it occupies rows **133–159** (this frame's
     crop is offset by −1 y). Same rows, same ~155 px width, same darkest
     sample (`#545454` here, `#545454` in `C-garage-before-maze-panel`).
  2. In `C-open-transition-height-phase.png` the label is **fully drawn while
     the SWF contributes ≤10 % alpha and no other SWF pixel exists**. An SWF
     text field cannot be visible while its own stage is transparent.
  3. Here, in **edit** mode, the maze's name (`Run Around The WORLD`) is in
     the input field and the top-centre text is the **username**. If the SWF
     drew a maze title, this is exactly the frame where it would say
     "Run Around The WORLD".
  Confirmed in a **third** capture (`A-editor-panel-primary-source-hq.png`, topic A's file): top
  centre reads `mr_enderman`, input field reads `Kill The Player`.
  `[INFERRED]` Consequence for `docs/standards/MAZECREATOR-VISUAL-SPEC.md`: its
  "Title text" row, and `DEDUCE.md:407`'s *"Gauntlet" title*, most likely
  describe the **username of the account** in `Making a maze.png`, not a maze
  name — the screenshot's crop simply included the page label above the SWF.
  **Falsifier:** show that no account named "Gauntlet" existed, or a frame
  where the top-centre text differs from the account name.
- **VE entry 7 (Title + watermark typography)** — the *watermark* half is
  corroborated (≈12 px, letter-spaced, `#bbbbbb`-ish, flush bottom-right).
  The *title* half is **reassigned to the page**, so it belongs to S24, not to
  the SWF.
- **S39 (maze-creator toolbar row)** — the row is visible and measurable
  (input 178 CSS px wide, three tools, ✗ and ✓ right-aligned). Topic A owns
  the detail; recorded here because it is the "before" state of the save diff.

**What this does NOT show**

Any tool in its selected state distinguishable at this resolution; the error
panel; the editing interaction.

---

### `UI/C-after-confirm-tools-hidden.png` (1592 × 1017, captured 17:05:15) — [image](./UI/C-after-confirm-tools-hidden.png)  *(was `afterclickingonconfirmbeforeanimationisfinished.png`)*

**Filename claim (repo owner):** "after clicking on confirm, before animation
is finished" — **corroborated**, and the "animation" turns out to be the
preview coming back, not a card tween.

**Context first.** `[OBSERVED]` The immediately preceding frame in the
owner's capture run is topic A's `A-toolbar-confirm-click-midfade.png` (17:04:59), which shows
the editor open on **`One Path to Destruction`** — the *second* slot — with
the pointing hand on the green save ✓. `[MEASURED]` That file's card measures
1098.45 × 734.37 capture px, byte-for-byte the same geometry as this session's
other frames, so it is the same session at the same scale. `[INFERRED]`
Therefore between `C-editor-opened-on-slot1` (slot 1 open) and this frame the user
left slot 1, opened **slot 2**, and saved it.

**What is drawn**

- `[OBSERVED]` The preview is back. **The tools, the title input and the red
  ✗ are gone**; the green accept ✓ is in the corner with the pointing hand
  still on it (recorder ring bright, i.e. a click happened moments before).
- `[OBSERVED]` **Slots 1 and 3 are drawn, with their captions. Slot 2 —
  the slot that was just saved — is completely blank.**
- `[OBSERVED]` No spinner, no progress indicator, no message, no flash, no
  modal, no grey placeholder box in the empty position.

**Measurements**

| test | result |
|---|---|
| red pixels anywhere inside the card | **0** (the ✗ is gone) |
| ink column bands inside the card | 253 (border), 377–582 (slot 1), 665, **719–874 (the username label only)**, 1001–1341 (slot 3 + watermark + ✓) |
| slot-2 region (x 697–898, y 339–494) minimum grey | **252.7** — pure white, not a faint ghost |
| slot-2 caption region minimum grey | **253.0** |
| slot 1 vs `afterrfadein…`, max channel difference | **40** (compression noise) |
| slot 3 vs `afterrfadein…`, max channel difference | **20** (compression noise) |

`[MEASURED]` The slot-2 area is *empty*, not partially faded: at 10 % alpha
the `#d1d1d1` floor would read 250.4, which is above this frame's 252.7 floor.
`[INFERRED]` the slot is not mid-fade — it is **not drawn at all**.

**Links to the program**

- **VE entry 3 (Save flow / dialogue after ✓ — WANTED).** Answered.
  Status `WANTED` → **FETCHED**. The verbatim want was *"Spinner? Instant?
  Confirmation flash?"* → **none of those.** What actually happens:
  1. `srv/index.php:3712` sets `_root.saveRequested = 'true'`; the page shows
     nothing at all in the meantime — no busy state is added by the page.
  2. On success the SWF calls back to `hideMazeCreatorToolsAndTitle`
     (`:3737-3753`), which sets `previewLoaded` (`:3740`), fades the ✗ and the
     controls row out over **200 ms linear** (`:3742-3746`), hard-hides the
     save button (`:3748-3749`) and hard-shows the accept ✓ (`:3751-3752`).
     Every one of those is visible in this frame as an accomplished fact.
  3. The SWF returns to preview and re-draws the slot row — **but the slot
     just written stays blank while the untouched slots are already drawn.**
- `[INFERRED]` **the just-saved slot is re-fetched from the server, and the
  other two are re-used from what the SWF already holds.** The evidence is
  specific: of three slots, exactly the one that was in the editor is missing,
  and it is missing for a measurable interval (4 Scrapyard ticks to the next
  frame). Falsifier: a frame showing a *different* slot blank, or all three
  blank, at this point in the flow. This is the strongest available answer to
  what `previewLoaded` (`srv/index.php:3740`, an empty-string `SetVariable`)
  actually triggers.
- `[OBSERVED]` **`hideMazeCreatorToolsAndTitle` is called only on success**
  (page comment, `srv/index.php:3714`) — and this frame is exactly what that
  looks like. The save succeeded.
- **`Editor.as:267-271`** — the rebuild does
  `hideError(); state="preview"; redraw(); getURL(...)` synchronously in the
  save callback, so every slot is instantly present. Contradicted; see the
  overhaul list.

**What this does NOT show**

Any *failed* save (so the error panel is still uncaptured); how long the blank
lasts in real seconds; whether the blank slot is re-fetched or merely
re-rendered late.

---

### `UI/C-after-confirm-preview-returned.png` (1592 × 1030, captured 17:05:39) — [image](./UI/C-after-confirm-preview-returned.png)  *(was `afterrfadeinanimationcomplete.png`)*

**Filename claim (repo owner):** "after re-fade-in animation complete" —
**corroborated as to the end state**; "fade" is the owner's reading and the
frame pair cannot confirm that the return is a fade rather than a pop (see
below).

**What is drawn**

`[OBSERVED]` Identical to `C-preview-boot-state.png` in every respect except the
cursor (pointing hand on the ✓, ring faded) and the live counters.

**Measurements — the frame-to-frame diff that answers VE 3**

`[MEASURED]` Difference against `afterclickingonconfirm…` after registering the
1 px x offset, threshold 40/255: **20 648 differing pixels**, falling into
exactly three column bands:

| band (x) | rows | what it is |
|---|---|---|
| 208–225 | 155–177 | Scrapyard flip plates |
| **697–897** | **339–493 and 550–563** | **slot 2's maze art and its caption appearing** |
| 1249–1371 | 742–863 | recorder ring fading + Facebook widget |

**Nothing else in the card changes.** No spinner appears or disappears, no
overlay, no message strip, no tool, no border.

`[MEASURED]` Difference against `C-preview-boot-state.png` (pixel-aligned, no
registration needed), threshold 40/255, restricted to the thumbnail band
(x 350–1250, y 300–520): **zero differing pixels**. All three thumbnails are
byte-identical to how they were drawn 6½ minutes and one full editor session
earlier.

`[INFERRED]` Two things follow.
1. **The save produced no change to the stored maze.** Overlaying
   `A-toolbar-confirm-click-midfade.png`'s editor maze on slot 2's thumbnail at matched scale
   (below) shows the same outline, the same interior walls including a
   one-cell stub in the upper right, and the same ten spawn positions. The
   user opened slot 2, made no net edit, and saved. Falsifier: an edit visible
   between topic B's editing frames and `A-toolbar-confirm-click-midfade.png`.
2. **The preview render is deterministic for a given maze.** The same maze
   renders to identical pixels twice. `[UNCERTAIN]` however: the SWF is never
   unloaded between the two frames (`closeMazeCreator`'s
   `innerHTML=''` at `srv/index.php:3633` never runs here), so the second draw
   could be a cached bitmap rather than a fresh render. This is **weaker than
   it looks** for VE 8a — and in any case the preview floor is flat, so it
   cannot settle the editor's tone pattern at all.

**Links to the program**

- **VE entry 3** — completes the answer begun in the previous frame.
- **VE entry 8a (floor tone pattern)** — narrowed, not solved: `[MEASURED]`
  the *preview* thumbnails use a **flat** floor (per-cell means 209.6 ± 1.8
  over 174 cells in session B's largest maze), so 8a is an **editor-only**
  question and no preview frame can ever settle it. Keep 8a `WANTED`,
  re-scoped.
- **`Editor.as:335-339` / `MazeRenderer`** — the rebuild renders preview and
  edit with the same routine and the same tones. Contradicted: they are
  visibly different renderers (flat vs two-tone, fit-to-box vs fit-to-lattice).

**What this does NOT show**

Whether the returning slot fades or pops (only its absent and present states
are held); a save that *changes* a maze; the close transition
(`closeMazeCreator`) — the ✓ is hovered but never seen clicked in this set.

---

### `UI/C-empty-slot-maze3-cam12win.png` (1705 × 1020, captured 17:40:06) — [image](./UI/C-empty-slot-maze3-cam12win.png)  *(was `emptymazeislikethis,maze3.png`)*

**Filename claim (repo owner):** "empty maze is like this, maze 3" —
**corroborated exactly**: slot 3 is empty and is labelled `Maze 3`.

**Different session, different account, different year.** See Scope.

**What is drawn**

- `[OBSERVED]` The same preview layout: username `cam12win` centred at the
  top, a row of three slots, `version 0.3` bottom-right, green accept ✓ below
  it.
- `[OBSERVED]` Slot 1 = a maze thumbnail, caption `epic youtube`.
- `[OBSERVED]` Slot 2 = a maze thumbnail (a rectangular spiral), caption
  `Epic Twister`.
- `[OBSERVED]` Slot 3 = **a plain grey filled square with a thin darker
  border and the words `Maze 3` centred inside it. There is no caption
  underneath it.**
- `[OBSERVED]` No `+`, no "create", no "new", no dashed outline, no plus-sign
  glyph — the empty slot is simply a labelled grey box.

**Measurements**

| quantity | capture px | CSS px (s = 2.0711) |
|---|---|---|
| slot 1 art box | x 440–705, y 303–481 | pitch 17.20 → **15 × 10** cells |
| slot 2 art box | x 855–1119, y 319–466 | pitch 14.44 → **18 × 10** cells |
| **slot 3 grey box, border centres** | x 1273–1532, y 262–522 | **125.3 × 125.6** — square |
| slot centres | 572.5, 987.0, 1403.5 | 146.6, 346.9, 547.4 from the card's left border |
| **slot pitch** | 414.5, 416.5 | **200.6** |
| middle slot centre vs card centre (985.58) | +1.4 | centred |
| slot vertical centres | 392.0, 392.5, 392.0 | one line, **186.5 below the card top** |
| grey box fill | `(209, 209, 209)` = **`#d1d1d1`** (34 298 px of one value) | |
| grey box border, darkest samples | 122 (left), 145 (right), 145 (top), 156 (bottom) | ≈1 CSS px, blurred |
| `Maze 3` ink box | x 1320–1488, y 371–409 | 81.5 × 18.8 |
| `Maze 3` glyph runs | M 1320–1362, a 1368–1391, z 1395–1416, e 1419–1443, **3** 1460–1488 | |
| `Maze 3` colour, darkest | `(106, 106, 106)` ≈ `#6a6a6a` | source plausibly `#666666` |
| `Maze 3` cap height | 39 | **18.8** → a **≈26 px** face |
| green ✓ | x 1626–1681, y 867–937 | **27.0 × 34.3** |
| captions `epic youtube`, `Epic Twister` | x 506–639 / 922–1054, y 567–591 | ascender top **271.0 below the card top** |

`[MEASURED]` The grey box's fill (`209,209,209`) and the *maze floor* fill in
the same frame (per-cell mean **209.6**) are the same tone within one level.
`[INFERRED]` the empty-slot box is drawn with the same floor fill the preview
uses for maze cells — i.e. it reads as "a slot-sized patch of empty floor",
not as a distinct UI chrome colour. Falsifier: a native-resolution capture
showing the two differing.

`[MEASURED]` Slot-3's caption row is **empty**: scanning x 1230–1600 across
y 555–605 (the band where the other two captions live) returns no pixel below
225 grey.

`[MEASURED]` **Cross-session agreement on the layout constants:**

| constant | session A (`revengexx1`) | session B (`cam12win`) | agreed |
|---|---|---|---|
| slot pitch | 200.7 | 200.6 | **200.6 ± 0.3** |
| slot box | 125.3 (derived) | 125.3–125.6 (measured directly) | **125.4 ± 0.5** |
| box centre below card top | 187.3 | 186.5 | **186.9 ± 0.5** |
| caption ascender-top below card top | 271.2 | 271.0 | **271.1 ± 0.3** |
| accept ✓ | 26.5 × 34.0 | 27.0 × 34.3 | **≈27 × 34** |
| slot count | 3 | 3 | **3** |

Two accounts, two videos, two eras, one layout.

**Links to the program**

- **VE entry 4** — this is the frame that turns "how many slots" from a count
  of one user's mazes into a **structural** answer. See below.
- **S43** — see below.
- `[NOT VISIBLE]` Whether the grey box is clickable, what it does when
  clicked, and what its hover state looks like. **New want.**

**What this does NOT show**

Any interaction with the empty slot; a slot 2 empty (so we cannot tell whether
an empty slot in the middle would compact the row or hold its position — the
evidence that it holds its position is indirect: slot 3 keeps its centre and
the row stays symmetric); this account's full editor.

---

## The questions the topic was set

### 1. VE entry 4 — the preview, answered

`[MEASURED]` **Three slots.** `[MEASURED]` **Thumbnail box 125.4 ± 0.5 CSS px
square, pitch 200.6 ± 0.3 CSS px, row centred on the panel, box centres
186.9 CSS px below the card's top border, captions with their ascender tops
271.1 CSS px below it.** `[MEASURED]` **Left and right margins 82.5 CSS px;
the three boxes and two gaps sum to 690.8 against the panel's 692.**

**Every caption, verbatim:**

| session | slot | caption |
|---|---|---|
| A `revengexx1` | 1 | `Run Around The WORLD` |
| A `revengexx1` | 2 | `One Path to Destruction` |
| A `revengexx1` | 3 | `Battlefield of Awesomness 2` — clipped at the field edge; the final glyph is cut vertically and reads as `2` `[UNCERTAIN]` |
| B `cam12win` | 1 | `epic youtube` |
| B `cam12win` | 2 | `Epic Twister` |
| B `cam12win` | 3 | *(none — empty slot, label `Maze 3` inside the box)* |

**Occupied vs empty slot:**

| | occupied | empty |
|---|---|---|
| box outline | **none drawn** — only the maze art appears | **1 px darker-grey border**, darkest sample 122 |
| fill | maze floor cells only, flat `#d1d1d1`-ish | solid `#d1d1d1` over the whole 125 px square |
| content | walls, floor, tank + crate spawns, scaled to fit | the words `Maze N` centred, `≈#6a6a6a`, ≈26 px face |
| caption below | the maze's name, ≈12 px, `≈#707070` | **none** |
| footprint | ≤ the box; a wide maze fills the width and is vertically centred | exactly the box |

`[OBSERVED]` **There is no "create new maze" affordance distinct from an empty
slot.** The card's complete ink inventory (username, three slots, captions,
watermark, ✓) contains nothing else in either session.
`[INFERRED]` the empty slot *is* the create-new affordance — it is the only
thing there to click. Falsifier: footage of the empty slot being clicked and
doing nothing.

**Are the thumbnails real renders, and at what scale?**

`[MEASURED]` **Yes.** `C-preview-boot-state.png`'s slot 2 and topic A's
`A-toolbar-confirm-click-midfade.png` show the same maze at 0.36 × and 1 × respectively; scaled
to a common size the two agree on the outer silhouette (including a notch on
the left and a step on the lower right), on every interior wall including a
single one-cell stub in the upper-right chamber, and on all ten spawn
positions (5 tank, 5 crate) — see `cmp_slot2` reproduction in the analysis
run. Slot 1 likewise matches `C-editor-opened-on-slot1.png`'s maze cell-for-cell.

`[MEASURED]` The scale is **not fixed** — each thumbnail has its own cell
size, because each maze is fitted to the box:

| maze | cells | thumb cell (CSS px) | box implied (cell × max dim) |
|---|---|---|---|
| `Run Around The WORLD` | 12 × 10 | 10.40 | 124.7 |
| `One Path to Destruction` | 13 × 10 | 9.52 | 123.8 |
| `Battlefield of Awesomness 2` | 15 × 10 | 8.25 | 123.8 |
| `epic youtube` | 15 × 10 | 8.30 | 124.6 |
| `Epic Twister` | 18 × 10 | 6.97 | 125.5 |

`[INFERRED]` **thumbnail cell = ≈124.3 / max(w, h)** — i.e. the maze itself
(with *no* padding ring) is scaled to fit the 125.4 px slot box, the ~1 px
shortfall being the wall thickness. Five mazes, spread 1.5 %. Falsifier: a
thumbnail whose cell size departs from that by more than ~3 %, or a maze
taller than it is wide (none observed) showing whether the fit is contain or
fit-to-width.

Relative to the editor render of the same maze the thumbnail is
**0.389 ×** (`Run Around The WORLD`) and **0.356 ×** (`One Path to
Destruction`) — *not a constant ratio*, because the two views use different
fit rules (Finding 8).

### 2. S43 (multiple maze slots) and S38 (`userSettingsMazeCreatorInitCode-`)

**Three slots exist. This is structural, not a coincidence of one user's
save history.** The distinction the topic asks for is exactly what session B
settles:

- `[OBSERVED]` `cam12win` has **two** saved mazes and the row still has
  **three** positions, the third occupied by a placeholder that names its own
  index: `Maze 3`. A row that grew with the number of saved mazes would show
  two slots.
- `[MEASURED]` `revengexx1` has three saved mazes and shows **three** slots —
  no fourth, no empty fourth, and no room for one: the row already fills the
  panel to within 1.2 px of 692.
- `[MEASURED]` The pitch and box size agree to 0.1 % across two accounts,
  two videos and two years — a fixed layout, not a flow.
- `[OBSERVED]` No paging control, no scroll arrow, no ellipsis, no "more".

So: **the slot count is exactly 3 in both observed sessions.** What I can
defend is that; what I cannot defend is that it was 3 in 2017–2018, because
both sessions predate 2016-01 on the scrapyard bound. `DEDUCE.md:366`'s
"frozen for 7½ years" makes a change unlikely, and `Making a maze.png`
(2016-01-30, spec source) is `version 0.3` as these are, but that is an
argument, not an observation.

**This directly contradicts the rebuild's single-slot assumption.**
`DECISIONS.md` "mazes remodel" (2026-08-03) records *"s observed only as 1
across all 842 payloads"* and models the DB as one row per `(author, slot)`
with 672 distinct states — every one of them slot 1. `saveMaze.php` invents a
`badSlot` error code with no idea what the legal range is.

`[INFERRED]` The reconciliation, stated carefully: **`s == 1` in the corpus is
a property of the archived `loadMaze.php` request shape, not proof that only
one slot existed.** `DECISIONS.md` itself records that 842 of 843 archived
bodies answered *anonymous* `c=<random>` requests — the public random-maze
read path — not per-user slot reads. If that path only ever served slot 1
(or only ever served whatever the server considered a user's "current"
maze), the corpus would look exactly as it does while three slots existed all
along. Falsifier: any archived `loadMaze` body with `s != 1`, or any archived
request carrying a slot argument.

**Consequences for the wire format**

1. `s` has a real range of at least **1..3**, and the numbers are
   user-visible: the placeholder literally reads `Maze 3`.
2. `saveMaze.php`'s invented `badSlot` code (DECISIONS 2026-08-03) now has a
   real referent; its validation should be `1 <= s <= 3` rather than an
   unbounded invention. That is still M3 until an era payload with `s != 1`
   surfaces, but it is no longer arbitrary.
3. `loadMaze.php`'s seed keyed on `(author, slot)` is **structurally right**
   and should stay; what changes is that the rebuild must be able to hold
   three rows per author, and the garage boot path must supply all three.
4. **The preview needs all three mazes.** `srv/index.php:3617` passes exactly
   one blob — `document.getElementById('userSettingsMazeCreatorInitCode-'+user)
   .innerHTML` — as `initCode`. Either that blob carries all three slots, or
   the SWF fetches the other two itself. `[INFERRED]` the frame pair
   `afterclickingonconfirm…` / `afterrfadein…` argues for **fetching**: after a
   save, exactly the saved slot goes blank for seconds while the other two
   stay drawn, which is what a per-slot refetch looks like and is not what a
   re-parse of a single static blob looks like. **S38** therefore moves from
   "rebuild invented `u,n,t,d,s`; real fields unknown" to: *the init blob must
   at minimum identify the user and the three slots; the per-slot maze data
   may or may not travel in it, and the save-time refetch says at least one
   slot is loaded over the wire.* Status `WANTED` → **PARTIAL**.

### 3. The open transition — S37 and VE entry 8

**The source.** Grepped, and the maze-creator block occurs **exactly once**
in the 16 678-line file (all other routes omit it):

```
srv/index.php:3609  function openMazeCreator(user)
srv/index.php:3611    …SetVariable("fadeOut", "true")                       // t=0
srv/index.php:3613    setTimeout(… 'width' … start(692); … 'left' … start(0), 700)
srv/index.php:3615    disableUserPanelIcons(user)                           // t=0, 200ms
srv/index.php:3617    setTimeout('… new SWFObject("includes/mazeCreator_v0.3.swf", …, "688","400", …)', 700)
srv/index.php:3619    setTimeout(… 'userpanelContent-…','height' … start(385), 1200)   // onComplete → fadeOut='false'
srv/index.php:3620    setTimeout(… 'userpanelswrapper','height' … start(500), 1200)
srv/index.php:3622    setTimeout(… 'userpanelAcceptMaze-…','opacity' … start(1), 1700)
srv/index.php:3626  function closeMazeCreator(user, position)
srv/index.php:3631    setTimeout(… content 99 … wrapper 214, 700)
srv/index.php:3633    setTimeout(… width 224 … left <position>, 1200)
srv/index.php:3637    setTimeout(… SetVariable('fadeOut','false'), 2300);   // 1700 + 15frames/25fps * 1000 = 4300
```

**Correction to the task premise.** The brief asked me to check the pixels
against "224→692 width, 99→245 content height, 214→360 wrapper". **99→245 and
214→360 are the *paint* flow** (`srv/index.php:3560-3561`,
`openPaintFacility`). The **maze** flow is **99→385 and 214→500**
(`:3619-3620`) — both a **286 px** growth against paint's 146 px.

**What the pixels say.**

| specified | measured | agreement |
|---|---|---|
| width 224 → 692 (Δ 468) | 223.0 → 692.0 (Δ 469.0) | **0.2 %** |
| height Δ 286 (content 99→385 **and** wrapper 214→500 both grow by 286) | card 176.5 → 462.7 (Δ **286.2**) | **0.07 %** |
| paint's Δ 146 | — | **excluded by a factor of 2** |
| `left` → 0 | panel `left` was 116.3; card's left border moves −116.3 and its right border +351.7, summing to 469.0 | exact |

`[MEASURED]` The card's visible height and `userpanelContent-`'s height differ
by a constant 77.1 CSS px of chrome in the collapsed state and 76.7 in the
expanded state — so the card tracks the content tween 1:1 and the Δ 286
measurement is a direct read of `99→385` (or of `214→500`; the two Δs are
equal and cannot be separated by this evidence).

**Frame-to-timeline mapping.**

| frame | measured state | inferred t |
|---|---|---|
| `C-garage-before-maze-panel` | icons opaque, tanks drawn, width 223.0 | t < 0 |
| `C-maze-icon-clicked` | tanks at 1 % ink, clicked icons at 5 %, sibling panel at 10 %, width 222.6 (unmoved) | **≈600–720 ms** |
| `C-open-transition-width-phase` | width 692.0 (done), height +3.2 CSS = **1.12 %** of Δ286, no ✓, SWF blank | **≈1237 ms** |
| `C-open-transition-height-phase` | width and height both complete, ✓ at full opacity, SWF ≤10 % alpha | **≈1900–1950 ms** |
| `C-preview-boot-state` | SWF fully drawn | **≳2300 ms** |
| `C-slot-hover-green-glow` | preview + rollover | later, user-driven |
| `C-editor-opened-on-slot1` | edit state | later, user-driven |

**Expand-right-then-down: two axes or one diagonal tween?**
**Two distinct, sequential, non-overlapping axes.** `[MEASURED]` In
`C-open-transition-width-phase` the horizontal axis is at **100 %** and the
vertical at **1.12 %**. A diagonal tween would put both at the same fraction.
`[OBSERVED]` This matches the source exactly: the width tween is scheduled at
700 ms for 500 ms and the height tweens at 1200 ms for 500 ms, so they abut
and never overlap. **The owner's reading is correct.**

What would settle the remaining question — whether the *easing* is what the
source says — is a frame taken **inside** a tween rather than at its edge:
any frame with the card width strictly between 224 and 692 would give a
`Quad.easeInOut` sample. This set has none. That, and the SWF fade's
linearity, keep **VE 8 at `PARTIAL`**; **S37** moves `WANTED` →
**PARTIAL/FETCHED for the open half** (geometry and ordering pinned; easing
and the whole *close* half — `closeMazeCreator`, the 2300 ms tank restore —
remain unseen).

`[MEASURED]` Note the O source's own arithmetic slip at `srv/index.php:3637`:
the timeout is `2300` and the comment reads `// 1700 + 15frames/25fps * 1000 =
4300`, where 1700 + 600 = 2300. The code is right, the comment's total is
wrong. Preserve both verbatim — it is O.

### 4. VE entry 3 — the save flow

Answered above under `afterclickingonconfirm…`. In one line:
**no spinner, no dialogue, no confirmation flash — a 200 ms fade-out of the
controls, a hard swap of the save ✓ for the accept ✓ in the same corner, and
a preview that comes back with the just-saved slot blank for a beat.**

`hideMazeCreatorToolsAndTitle` being called *only* on success
(`srv/index.php:3714`) is corroborated in the sense that the post-✓ frame
shows precisely its effects; it is **not** corroborated in the negative,
because no failed save is in evidence.

### 5. VE entry 2 — the editor error panel

`[NOT VISIBLE]` **in all ten frames.** This was checked programmatically, not
by eye: for every frame the card interior was scanned for any contiguous dark
region. The darkest and largest structures found are, in every case, maze wall
lines — the longest run of sub-160 grey in any card row is 352 px in
`C-preview-boot-state` (a thumbnail's wall row) and 278 px in
`C-editor-opened-on-slot1` (an editor wall row). The rebuild's invented panel
(`Editor.as:322-332`) is a 400 × 80 stage-px box at `#444444` α 90 centred at
stage (144–544, 160–240); nothing remotely like that footprint exists in any
frame.

`[OBSERVED]` No frame in this set triggers it: every save shown succeeds, no
✗ is clicked, and no empty or duplicate name is submitted. **VE 2 stays
`WANTED` and vital.** The footage trigger stated in the want-list is still
right; add to it that the *preview* state is also a candidate surface (a
failed load would presumably surface there).

### 6. S45 (unsaved-changes warning on ✗) and S44 (deleting / clearing)

**S45 — `[NOT VISIBLE]`, absence recorded.** The red ✗ is drawn in
`C-editor-opened-on-slot1.png` at x 1227–1271, y 787–827 (27.7 × 25.2 CSS px), but
no frame in this set shows it being clicked. `srv/index.php:3717-3724`
(`cancelSaveMaze`) contains the O comment `//TODO: Ask the flash to check if a
warning should be displayed` followed immediately by
`SetVariable('_root.errorPanel.hide','yes')` and an unconditional
`hideMazeCreatorToolsAndTitle(user)` — i.e. the shipped page has no warning
path. My frames neither confirm nor refute that. **Stays `WANTED`.**

**S44 — `[NOT VISIBLE]`, and the absence is informative.** The exhaustive ink
inventory of the preview card (both sessions) contains **no delete control,
no clear control, no context affordance and no per-slot secondary button**.
`[INFERRED]` If a delete path existed it was not on this surface. That is
consistent with the want-list's own note ("No delete path in page JS or wire
format. May not have existed"). It does **not** rule out overwrite-by-saving,
which is in fact what session A demonstrates: the user re-entered an occupied
slot and saved over it. **Stays `WANTED`, but narrowed**: the question is now
only whether a slot could ever be returned to the `Maze N` empty state, not
whether there was a delete button in the preview — there was not.

---

## Finding 8 in full — the editor does not use a fixed cell

This falls out of the thumbnail-scale work and matters enough to state
separately. It leans on two files outside my assignment
(`UI/A-toolbar-confirm-click-midfade.png`, topic A; `UI/A-editor-panel-primary-source-hq.png`, topic A) plus the
number `mazecreator-visual-spec.md` derives from `Making a maze.png`; those
topics should re-derive it independently.

`[MEASURED]` Editor cell pitch, all in CSS px of the 688 × 400 embed box:

| capture | maze | cells | measured cell |
|---|---|---|---|
| `Making a maze.png` (spec, via its own scale) | Gauntlet | 13 × 8 | 32.00 |
| `UI/C-editor-opened-on-slot1.png` | Run Around The WORLD | 12 × 10 | **26.71** |
| `UI/A-toolbar-confirm-click-midfade.png` | One Path to Destruction | 13 × 10 | **26.74** |
| `UI/A-editor-panel-primary-source-hq.png` | Kill The Player | 4 × 4 | **53.33** |

A single fixed `CELL = 32` cannot produce 26.7 and 53.3 in the same build.

`[INFERRED]` The rule that does, fitted on two free parameters and then tested
against a third and fourth point:

> **cell = min( 576 / (w + 2), 320 / (h + 2) )** CSS px,
> where `w × h` is the maze's own size in cells.

| maze | predicted | measured | error |
|---|---|---|---|
| 13 × 8 | 32.00 | 32.00 | +0.00 % |
| 12 × 10 | 26.67 | 26.71 | +0.17 % |
| 13 × 10 | 26.67 | 26.74 | +0.26 % |
| 4 × 4 | 53.33 | 53.33 | −0.01 % |

Solving `C/(h+k)` on the (8, 32) and (10, 26.67) pair alone gives
`k = 2.007, C = 320.2`; the independent (4, 53.33) point then predicts to
0.06 %.

`[MEASURED]` And the maze's vertical centre sits **210.4 / 210.9 / 211.7 CSS px
below the card's top border** in the three editor frames — one line, spread
1.3 px. A 320 px-tall fit box centred there spans 50.6 → 370.6 below the card
top, which is **exactly the spec's lattice band `y = 50 … 370`**
(`origin (56, 50)`, 10 × 32). Likewise 576 = 18 × 32 with the spec's
`x = 56 … 632`. So the *box* the spec measured is right; what is wrong is
treating its contents as a fixed 18 × 10 lattice of fixed 32 px cells.

`[INFERRED]` What this most likely is: the editable lattice is **the maze plus
a one-cell ring on every side**, re-fitted into the 576 × 320 stage region
after every change. That is a coherent design — it is precisely how you let a
user grow a maze at the edge without a separate resize control — and it makes
VE entry 6's open question ("did the original re-centre live or keep a fixed
lattice?") answerable: **it re-scales and re-centres.** Falsifier, and the
cheapest one available: any two frames of the *same* maze one cell apart in
size; if the cell pitch changes between them, this is settled. Topic B's
`B-maze-growth-mechanism{,1,2}.png` may contain exactly that pair.

Consequences: `docs/standards/MAZECREATOR-VISUAL-SPEC.md`'s `CELL` and `LATTICE` rows,
and VE entry 6's "half-cell precision" reading, describe **one maze at one
size**, not a constant. `MazeRenderer.CELL`, `MazeRenderer.LATTICE_W/H`,
`Editor.as:43`, `Editor.as:82-105` (`loadIntoLattice` and its `fracX/fracY`
half-cell shift) and `Editor.as:192-198` (hit-testing against a fixed lattice)
are all built on the constant and are superseded together.

---

## Consequences for the rebuild

### Confirmed

- `srv/index.php:3613` — `userpanel-<user>` 224 → 692 px. Measured 223.0 →
  692.0. **Confirmed to 0.2 %.**
- `srv/index.php:3619-3620` — the **maze** flow's 99 → 385 content / 214 → 500
  wrapper (Δ 286). Measured card Δ **286.2 CSS px**. **Confirmed to 0.07 %**,
  and the paint flow's Δ 146 is excluded outright.
- `srv/index.php:3613` vs `:3619-3620` — the two tweens are **sequential and
  non-overlapping**. Confirmed by a frame with one axis at 100 % and the other
  at 1.1 %.
- `srv/index.php:3622` — `userpanelAcceptMaze-` fades in at 1700 ms; present
  and opaque while the SWF is still blank. **Confirmed.** Art now held
  (≈27 × 34 CSS px green tick, two sessions agreeing).
- `srv/index.php:3611` + `:3617` — the tank goes out by fade *before* the
  `visibility:hidden` at 700 ms. **Confirmed** (1 % residual ink at
  t ≈ 650 ms).
- `srv/index.php:3515` — the sherif-star icon is conditional; four icons on a
  non-moderator account. **Confirmed.**
- `srv/index.php:3737-3753` — `hideMazeCreatorToolsAndTitle`'s exact effects
  (✗ gone, controls gone, save gone, accept shown) are all visible after a
  successful save. **Confirmed.**
- `Editor.as:56` — the SWF boots at α 0 under the page. **Confirmed** (two
  frames with the card open and zero SWF ink).
- `mazecreator-visual-spec.md` **Watermark** row — `version 0.3`, ≈12 px,
  letter-spaced, very light grey, flush bottom-right. **Confirmed** in a
  second, independent capture.
- `mazecreator-visual-spec.md` **Floor tones** row — the *editor* floor is
  genuinely two-tone. **Confirmed qualitatively** (Δ 8–12 grey levels through
  video compression).
- `mazecreator-visual-spec.md` **Tank/Crate spawn icon** rows — blue-violet
  and amber cores. **Confirmed** at thumbnail scale.
- `DECISIONS.md` "mazes remodel" — the `(author, slot)` **row model is
  structurally right**; three slots per author is exactly what it anticipates.

### Contradicted — overhaul owed

Under **THE OVERHAUL RULE** these are rewritten wholesale, not patched.

1. **`src/mazecreator/Editor.as` — the entire preview state.**
   `Editor.as:47` (`state = "preview"`), `:183-191` (any click → edit),
   `:335-339` (`redraw()` draws one maze). The real preview is a **three-slot
   picker**: three 125.4 px boxes on a 200.6 px pitch, box centres 186.9 px
   below the panel top, each slot independently hit-testable with a green
   silhouette glow on rollover, each captioned with its maze name on a shared
   baseline 271.1 px down, and empty slots drawn as a `#d1d1d1` square with a
   1 px darker border and `Maze N` centred in a ≈26 px `#666666` face.
   **Rewrite, do not patch.**
2. **`src/mazecreator/Editor.as:27, 40, 251` — the slot field.** `slot`
   defaults to `"1"` and is never anything else; there is no notion of a slot
   *set*. The SWF must know about three slots, must be able to render a slot
   as empty, and must address slots by a user-visible index (`Maze 3`).
3. **`src/mazecreator/Editor.as:305-310, 338` — the stage title.** The SWF
   must **not** draw the maze name at the top of the stage; the grey centred
   name there is the page's userpanel username label. `_root.mazeName`
   (`srv/index.php:3705`) drives the **slot caption**, not a stage title.
   The corresponding row of `docs/standards/MAZECREATOR-VISUAL-SPEC.md` ("Title text")
   and `DEDUCE.md:407`'s *"Gauntlet" title* need re-reading as page chrome.
4. **`src/mazecreator/MazeRenderer` `CELL` / `LATTICE_W` / `LATTICE_H`, and
   `Editor.as:43, 82-105, 192-198`.** Fixed 32 px cells on a fixed 18 × 10
   lattice with a half-cell placement remainder. Contradicted by three
   captures with cells at 26.7 and 53.3 px. Replace with the fit rule
   `cell = min(576/(w+2), 320/(h+2))` (and re-pin hit-testing to it).
5. **`src/mazecreator/Editor.as:267-271` — the save callback.** It flips to
   preview and redraws everything in one synchronous step. The evidence shows
   the just-saved slot **blank for seconds** while the others are already
   drawn. The preview reload is per-slot and asynchronous.
6. **Preview vs editor rendering share a renderer.** They must not: the
   preview floor is **flat** single-tone, the editor's is two-tone; the
   preview fits `w × h` into 125.4 px, the editor fits `(w+2) × (h+2)` into
   576 × 320.
7. **Page-side (phase 4, not yet built).** Opening a garage sub-panel fades
   out **the entire sibling userpanel**, which nothing in `srv/index.php:3609-
   3624` does. The markup reconstruction owes it. Real `left` values for a
   two-user row: **116.3** and **350.9** CSS px, panels 224 wide, 11.7 px
   apart.
8. **`saveMaze.php`'s `badSlot`** (DECISIONS 2026-08-03) — no longer a pure
   invention. Validation should be a bounded slot index (observed range 1..3),
   and `loadMaze.php`'s seed must be able to hold three rows per author.

### Still unknown / stays on the want-list

- **VE 2 — editor error panel.** `[NOT VISIBLE]` in all ten frames. Stays
  `WANTED`, vital.
- **VE 8 — fade easing.** No frame lands inside a tween; no frame shows a
  partial SWF alpha. Stays `PARTIAL`.
- **VE 8a — floor tone pattern.** Re-scoped: the preview cannot settle it
  (flat floor). Stays `WANTED`, editor-only.
- **S44 — delete/clear.** No control on the preview surface; whether a slot
  could return to empty is unknown. Stays `WANTED`, narrowed.
- **S45 — unsaved-changes warning.** The ✗ is never clicked here. Stays
  `WANTED`.
- **S37 — the *close* transition.** `closeMazeCreator`'s 700/1200/1700/2300 ms
  sequence, the tank's restore, and the panel's return to its `position` are
  entirely unseen. Stays `WANTED` for the close half.
- **S41 — editor sound.** These are silent stills. `[NOT VISIBLE]`.
- The slot count **in 2017–2018** specifically (both sessions predate
  2016-01 on the scrapyard bound).

### New wants to add

1. **Clicking an empty `Maze N` slot.** What opens, what the title field is
   pre-filled with (`showMazeCreatorToolsAndTitle`'s `title == ''` branch at
   `srv/index.php:3671-3675` sets the placeholder `Maze name` in `#666666`,
   which is exactly the empty-slot case), and whether the editor starts from a
   blank lattice or a default shape. **HIGH value, MED recoverability** — any
   tutorial video making a first maze.
2. **The empty slot's rollover state.** Does the grey box glow green too?
3. **A maze growing by one cell in the editor** — two adjacent frames settle
   the fit law of Finding 8 outright. Topic B's `B-maze-growth-mechanism*`
   frames may already hold it.
4. **A *failed* save** — the only route to VE 2.
5. **A native-resolution preview frame** — to pin the glow green, the wall
   colour at thumbnail scale, the caption face, and the empty-box border
   colour, none of which survive this compression.
6. **Any capture of `?garage` from 2017–2018** showing the slot row, to carry
   the three-slot finding into the target era.
7. **A logged-in garage where a *middle* slot is empty** — to learn whether an
   empty slot holds its position or the row compacts.
8. **Whether the wire `s` is the visible slot index.** A single archived
   `loadMaze` body with `s != 1`, or any request carrying a slot argument,
   settles the tension between "s observed only as 1 across 842 payloads" and
   three visible slots.

---

## Recommended edits to existing docs (not applied)

**`docs/standards/VISUAL-EVIDENCE-WANTED.md`**

- Entry **4 (Maze preview / garage mode)** — change status `WANTED, vital
  user-facing` → **`FETCHED`**, and replace the body with the measured layout:
  three slots, 125.4 px square boxes on a 200.6 px pitch, centred, box centres
  186.9 px below the panel top, captions 271.1 px below it in a ~145 px
  centre-clipped field, empty slots as `#d1d1d1` squares labelled `Maze N`, no
  separate create affordance, rollover = green silhouette glow + green
  caption. Cite `UI/C-preview-boot-state.png`, `UI/C-slot-hover-green-glow.png`,
  `UI/C-empty-slot-maze3-cam12win.png`.
- Entry **3 (Save flow)** — change `WANTED` → **`FETCHED`**; body: *"No
  spinner, no dialogue, no flash. Controls + ✗ fade out 200 ms, save ✓ is
  replaced by accept ✓ in the same corner, preview returns with the
  just-saved slot blank for several seconds while the other two are already
  drawn — evidence of a per-slot asynchronous reload behind `previewLoaded`.
  `UI/C-after-confirm-tools-hidden.png` +
  `UI/C-after-confirm-preview-returned.png`."*
- Entry **2 (Editor error panel)** — keep `WANTED`; append: *"Checked against
  10 garage/editor frames (topic C, 2026-08-04): `[NOT VISIBLE]` in all,
  including three preview states and one edit state. Every save in that corpus
  succeeds. Add the preview state to the list of surfaces to watch."*
- Entry **6 (Maze placement rule)** — change `PARTIAL` → **`CONTRADICTED /
  overhaul owed`**; the editor scales the maze rather than snapping it into a
  fixed lattice, `cell = min(576/(w+2), 320/(h+2))`, four mazes fitting to
  ≤0.26 %.
- Entry **7 (Title + watermark typography)** — split it. The watermark half is
  corroborated. The title half should be moved to section B (userpanel) as *"a
  page-side username label, not SWF typography"*, with the note that
  "Gauntlet" is most likely the account name in `Making a maze.png`.
- Entry **8a (Floor tone pattern)** — keep `WANTED`; append: *"the preview
  thumbnails use a flat single-tone floor (209.6 ± 1.8 over 174 cells), so
  preview frames can never settle this; editor frames only."*
- **S43 (Multiple maze slots)** — `WANTED` → **`FETCHED`**. Body: *"Three
  slots, proven structurally: `cam12win` has two saved mazes and the third
  slot renders as a grey placeholder labelled `Maze 3`. Layout identical on a
  second account in a different year. `s == 1` across 842 payloads is a
  property of the anonymous `loadMaze` read path, not proof of one slot."*
- **S38 (`userSettingsMazeCreatorInitCode-` fields)** — `WANTED` →
  **`PARTIAL`**; note that the post-save blank slot argues the SWF fetches at
  least the saved slot over the wire rather than reading everything from
  `initCode`.
- **S37 (Garage → maze-creator transition)** — `WANTED` → **`PARTIAL`**;
  the open half is pinned (geometry to 0.07–0.2 %, two sequential axes, frame
  timings), the close half and the easing are not.
- **S46 (Garage maze-icon art)** — `WANTED` → **`PARTIAL`**; the classic
  `userpanelMaze-` icon is a greyscale isometric tray with raised interior
  maze walls, ≈44.7 × 39.7 CSS px, third of four icons in the strip.
- **S24 / S25 / S28 / S40** — all `WANTED` → **`PARTIAL`**, with the
  measurements in this document.
- **S42 (Cursor)** — `WANTED` → **`PARTIAL`** for the preview state: system
  pointing hand over a slot, no custom cursor.
- **New entries** as listed under "New wants to add" above; the highest-value
  is *"a first maze being created from an empty slot"*, which would close
  entry 4 completely and probably surface entry 2 as a bonus.

**`docs/standards/MAZECREATOR-VISUAL-SPEC.md`**

- Add a banner: *"CELL and LATTICE below are a measurement of one 13 × 8 maze,
  not constants. Later evidence (topic C, 2026-08-04) shows the editor scales
  the maze to fit: `cell = min(576/(w+2), 320/(h+2))`. The 576 × 320 region at
  origin (56, 50) is confirmed; the 32 px cell is a special case of it."*
- Re-tag the **Title text** row as page chrome, not SWF content.
- Add a **Preview / slot row** block with the constants measured here.

**`DECISIONS.md`** — append a supersession entry recording: the invention
(single-slot preview, click-anywhere-to-edit, fixed 32 px cell on a fixed
18 × 10 lattice, SWF-drawn stage title, synchronous post-save redraw); what
the evidence showed; and what is being rewritten. Note explicitly that the
"`s` observed only as 1" finding is **not** contradicted — it is re-read as a
property of the archived request shape.

**`DEDUCE.md:407`** — annotate the `Making a maze.png` row: the "title
top-centre" is very likely the page's userpanel username label, so its
grade-A "layout" claim should exclude that element.

**`LEDGER.tsv`** — two new M2 rows are owed, one per source video, with URL,
uploader, upload date and timestamp, once the owner identifies them. The
burned-in titles `…rouble Mazez` (session A) and `…ake A Tank Trouble Maze!`
(session B) are the search handles.
