# Visual evidence — in-game rendering, HUD and chat

> Analysis of 14 evidence files under `manualevidence/`.
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)

---

## Scope and provenance

My 14 frames cover the game stage as it looks in a live round: the maze as the
*game* draws it (not the editor), tanks, weapon crates, the scoreboard strip
under the maze, and an in-stage **chat system that appears nowhere in the
project's held bytes or want-list**.

### Two corrections to my own task brief, up front

1. **`Game/F-video-card-beginner-league-caption.png` is not a login sidebar.** My assignment said it "appears
   to show a login sidebar next to the stage with Exp figures and an 'Access
   Online BETA / Beta access required / Shop Open / Get BETA access here'
   panel". It does not. `F-video-card-beginner-league-caption.png` (1266×650) is a four-panel **rank card**
   ("Dog Food / Lab Rat / Intern / Scavenger") with a blue *"The beginner
   league"* caption — a video-graphics frame, not site UI. The **Access Online
   BETA sidebar is in `Game/F-gameplay-2015-page-beta-sidebar.png`**, and it carries no "Exp" figures; it
   carries a Visits box. I analyse both files below as they actually are.
2. **There is no `mt-0-Malls.com`-style clone watermark in any of my frames.**
   The bottom-left text in `F-gameplay-2013-page-round-countdown.png` and `F-gameplay-2013-page-four-tanks.png` that reads as a
   watermark is `…ast-O-Matic.com` — the free-tier watermark of
   **Screencast-O-Matic**, the screen recorder. `[MEASURED]` cropped and
   upscaled at `(0,735)-(240,767)`; the glyphs read `ast-O-Matic.com` with the
   leading `Screenc` cut by the crop. That is a recorder artefact, not a
   rehost. If a clone watermark exists in the corpus it is on some other
   topic's files.

### The generation question — and why it turns out to be two questions

The task framed these frames as possibly "a different build or a different site
generation than the classic 2017-2018 target". The measurements split that into
**two independent datings**, and the answer differs between them:

| Layer | What dates it | Verdict |
|---|---|---|
| **The page around the stage** (sidebars, footer, nav) | footer copyright year, sidebar box set, credits line | **Pre-era.** 2013 and 2015 generations, plus one post-classic HTML5 generation. None is the 2017-2018 target page. |
| **The game inside the stage** (maze, tanks, crates, HUD, chat) | the `version 4.0` watermark drawn bottom-right *inside the stage* | **In-era.** `LEDGER.tsv` row 163 serves `srv/includes/TankTrouble_v4.0.swf` (tier `O`, sourced from `archive/includes-tree/20130313_TankTrouble_v4.0.swf`) and `srv/index.php:404` embeds exactly that filename at `712×490`. The game these frames show **is the game the reconstruction serves**. |

That is the single most consequential thing in this document. The page chrome is
two to five years early, but the SWF is byte-identical to the era one, because
the era page (2018) still names `TankTrouble_v4.0.swf` and the filename carries
the version (`srv/index.php:403` — `//REMEMBER TO CHANGE THE VERSION IN
logIn.php AND embed.php AS WELL!!!`). So everything I measure *inside the stage
in a v4.0 frame* is admissible evidence about the era build, even though the
page around it is not.

The lone exception is `Game/F-html5-generation-contrast-case.png`, which is a genuinely later generation
(no `version` watermark, HTML5-era boxes) and is useful only as a contrast case.

### Capture-order sessions

mtimes are when the repo owner saved the crop today (2026-08-04); I use them
only as **capture order**, and I reconstruct sessions from pixel content.

| Order | File | Session | Generation |
|---|---|---|---|
| 16:22:54 | `Game/F-gameplay-three-guests-maze-crop.png` | **A** — 3 guest tanks, maze "hvere are you by bulla" | v4.0 game / 2015 page (same frame as next) |
| 16:23:14 | `Game/F-gameplay-2015-page-beta-sidebar.png` | **A** (same video frame, wider crop) | v4.0 game / **2015** page (footer `2007 – 2015`) |
| 16:24:50 | `Game/F-gameplay-maze-61-crates.png` | **B** — 2 guest tanks, 61 crates | v4.0 game; page not visible |
| 16:34:05 | `Game/F-video-card-beginner-league.png` | **C** — rank card | video graphic, undatable |
| 16:34:19 | `Game/F-video-card-beginner-league-caption.png` | **C** — same card + caption | video graphic |
| 16:36:14 | `Game/F-video-card-scientist-league.png` | **C** — scientist rank card | video graphic |
| 16:36:31 | `Game/F-video-card-scientist-league-caption.png` | **C** — same card + caption | video graphic |
| 16:37:38 | `Game/F-html5-generation-contrast-case.png` | **D** — 5 named tanks, accessories | **post-classic HTML5** |
| 16:55:20 | `UI/F-chat-message-stack-in-stage.png` | **E** — chat stack, 3 named tanks | v4.0 game, 2013-style HUD |
| 16:55:44 | `UI/F-gameplay-2013-page-round-countdown.png` | **F** — chat, round countdown | v4.0 game / **2013** page |
| 16:56:05 | `UI/F-gameplay-2013-page-four-tanks.png` | **F** — 4 named tanks | v4.0 game / **2013** page |
| 17:08:46 | `UI/F-chat-bar-crop-1.png` | **G** — chat bar crop | v4.0 game |
| 17:08:54 | `UI/F-chat-bar-crop-2.png` | **G** — chat bar crop | v4.0 game |
| 17:09:01 | `UI/F-chat-bar-crop-3.png` | **G** — chat bar crop | v4.0 game |

The owner was clearly stepping through: gameplay → ranks → HTML5 build →
chat-in-context → chat close-ups. Sessions E/G are near-identical in style but
have different players and different capture zoom (cell pitch 80.2 vs 77.6
capture px), so I do **not** merge them.

### A note on tooling and scale

Everything numeric below came from Python/PIL/numpy on the staged files
(scratch scripts under `scratch/F/`). No held asset bytes other than
`srv/index.php` and the three `src/mazecreator/*.as` files were staged for me,
so I could not measure any held image; where that matters I say so.

I could **not** pin an absolute capture→stage scale factor for any frame with
the rigour `docs/standards/MAZECREATOR-VISUAL-SPEC.md` achieved for the editor
screenshot, because none of these captures spans a known-size object
edge-to-edge. `[UNCERTAIN]` Everything geometric below is therefore reported as
**capture pixels plus scale-free ratios** (wall/cell, tank/cell, crate/cell),
which are the numbers a rebuild can actually act on. My best bounded scale
estimate and its derivation are in the `F-gameplay-2015-page-beta-sidebar.png` section, flagged as such.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| F1 | In-game floor is a **single flat tone** `#e5e5e5`/`#e6e6e6`, not a two-tone per-cell mix. 98 floor-cell centres in `F-gameplay-three-guests-maze-crop.png` measure mean R **229.01, σ 0.10**; 192 cells in `F-gameplay-maze-61-crates.png` measure mean **230.2, σ 0.72** | `[MEASURED]` | VE **8a**, mazecreator-visual-spec "Floor tones" | No — different renderer. But 8a's framing needs a correction (see below) |
| F2 | Fully-enclosed cells render **`#ffffff`** (stage background), i.e. the game uses the same floor / non-floor cell model as the editor | `[MEASURED]` | `MazeData.as` floor model | Confirms |
| F3 | In-game wall tone **`#4c4c4c`** (dominant), trough minimum luminance 72-76; editor pins `#444444` | `[MEASURED]` | mazecreator-visual-spec "Wall color" | Challenges (different SWF) |
| F4 | Wall thickness / cell pitch = **0.099–0.121** across five frames (mean 0.109); editor pins 4/32 = **0.125** | `[MEASURED]` | mazecreator-visual-spec "Wall thickness" | Broadly consistent |
| F5 | **Cell size is not a constant in play.** Same session, two rounds: 6×3 maze at pitch 112.1 capture px, 4×8 maze at pitch 56.4. The maze is scaled to fit a fixed stage viewport (≈672×451 capture px in that session) | `[MEASURED]` | VE **6** (maze placement), new want | New |
| F6 | Weapon crate in play = **grey** rounded square, random rotation, dark `?`-like glyph, **no glow**. Side ≈ **0.47 cell**, bbox ≈ 0.58 cell. Zero non-grey pixels in a 37×37 crop | `[MEASURED]` | mazecreator-visual-spec "Crate spawn icon" | Distinguishes spawn marker (amber+glow) from live crate (grey, no glow) |
| F7 | In-game tank ≈ **0.41–0.45 cell** by √area, **0.52–0.61 cell** by bbox, and **scales with the maze** (proved by two rounds in one session) | `[MEASURED]` | new want | New |
| F8 | Stage carries a **`version  4.0`** watermark bottom-right, letter-spaced, very light grey — same treatment as the editor's `version 0.3` | `[MEASURED]` | VE **7**, **S110** | Gives S110 a build-fingerprint method |
| F9 | Stage carries a **maze name + author caption** (`hvere are you` / `by bulla`), right-aligned above the watermark | `[OBSERVED]` | new want, `saveMaze.php` wire format | New |
| F10 | **A chat system exists in the classic game stage** — an input bar and a stack of `<name> says '<text>'` strips — and `srv/index.php` contains **zero** chat markup, ids, strings or JS | `[MEASURED]` + clean grep miss | **New want (major)** | New |
| F11 | Chat input bar fill **`#8ddc97`**, opaque, thick black border, drawn as a **trapezoid** (right end 22–25% taller than left) at a **tilt that changes between frames** (+0.64°, −0.84°, −1.70°) — verified not a video rotation | `[MEASURED]` | new want | New |
| F12 | Chat message strips are **translucent** (α ≈ 0.76 solved against two backgrounds), 34 px tall at 50 px pitch, newest at top fading in | `[MEASURED]` / `[INFERRED]` | new want | New |
| F13 | HUD = optional gear + speaker at far left; per-player tank thumbnail + score; **username under the tank only when logged in**; version watermark right | `[OBSERVED]` | **S113**, new want | New |
| F14 | 2015 HUD **mirrors** the outermost-right entry (tank faces the stage centre, score on the barrel side); 2013 HUD does not | `[MEASURED]` | new want | New |
| F15 | Left icon changed generation: **door** (2013) → **gear** (2015) above the speaker | `[MEASURED]` | new want | New |
| F16 | 2015 Visits box format is **byte-for-byte the same label set and order** as the held 2018 bytes (`srv/index.php:1067-1069`), with 2015 values | `[MEASURED]` | **S105** | Confirms format stability 2015→2018 |
| F17 | `F-html5-generation-contrast-case.png` (post-classic) floor **is** two-tone `#e8e8e8`/`#dadada`, σ 7.44 across 77 cells, no parity rule — the opposite of the classic build | `[MEASURED]` | VE **8a** | New constraint |
| F18 | `F-html5-generation-contrast-case.png` right column replaces "Got Feedback?" with **"Message the laboratory"**; adds a **WALL of FAME** box; left column adds **"Battle mode: Classic"** and **"Tank Rank has been Deployed"**. All four absent from `srv/index.php` | `[OBSERVED]` + clean grep miss | S11, S96, S114 | Records the successor copy |
| F19 | S102 (era game-SWF audio) — nothing hearable in a still | `[NOT VISIBLE]` | **S102** | Stays WANTED |

---

## File-by-file analysis

### `Game/F-gameplay-three-guests-maze-crop.png` (1319×621, captured 16:22:54)  *(was `{C276DC91-7517-42D5-8AC9-59CD05FC525A}.png`)*

`./Game/F-gameplay-three-guests-maze-crop.png`

**Filename claim (repo owner):** none — GUID filename, no claim to test.

**What is drawn**

- A maze occupying most of the frame: thin dark-grey walls on a light-grey
  floor, with a heavier boundary. `[OBSERVED]`
- Six cells inside the maze are drawn **white** and are each fully enclosed by
  wall on all four sides. `[OBSERVED]`
- Two coloured objects sit inside the maze — a **blue** one at ≈(330,238) and a
  **green** one at ≈(537,228). Both are small rotated rounded rectangles with a
  dark outline; the blue one shows a barrel stub protruding top-left.
  `[OBSERVED]` They are tanks, not crates — see Measurements. `[INFERRED]`
- A grey **smoke puff** with a black dot at ≈(338,347). `[OBSERVED]` Reading it
  as the wreck of the red player is `[INFERRED]` — the HUD lists a red player
  but no red pixel exists anywhere inside the maze (`[MEASURED]`, 0 pixels with
  R>G+40 and R>B+40 in the maze bbox).
- Four small black dots scattered on the floor at ≈(211,35), (708,53),
  (418,173), (335,357). `[OBSERVED]` Bullets in flight is the natural reading
  but I cannot prove it from a still. `[UNCERTAIN]`
- A dark-grey **cross `+`** at ≈(211,78) and a dark-grey **ring `○`** at
  ≈(272,160), both drawn flat on the floor. `[OBSERVED]` I do not know what
  either is. They are not maze geometry (they sit mid-cell), not tanks (no
  colour), not crates (wrong shape, wrong tone). Candidates: a mine/booby-trap
  marker, an aiming reticle, an expanding blast ring. `[UNCERTAIN]` — a
  *sequence* of frames a few hundred ms apart would settle it instantly and is
  worth adding to the want-list.
- Below the maze, a HUD strip: a **gear** icon above a **speaker** icon at far
  left; then three tank thumbnails with score numbers. `[OBSERVED]`
- At the right, two light-grey right-aligned lines `hvere are you` / `by bulla`
  and, lower, a letter-spaced `version  4.0`. `[OBSERVED]`

**Transcriptions (verbatim, including the typo)**

```
hvere are you
by bulla

version  4.0
```

Scores, left to right: `28` `29` `21`. No usernames anywhere. `[OBSERVED]`

**Measurements**

*Lattice.* Dark-pixel column/row profiles give full-height boundary bands at
x = 169–176 and x = 1159–1166, and interior gridlines that fit a lattice of
**pitch 66.0 capture px** with residuals ≤ 2 px at every line. Maze width
1159 − 169 = 990 = 15 × 66.0 → **15 columns**. `[MEASURED]`
Row pitch from bands at y = 131, 198, 330, 395, 462.5 → **66.4**, i.e. square
cells. The bottom boundary is at y ≈ 462.5. The top boundary is **above the
crop**: at y = 0–2 only 45% of the maze width is dark, and at x = 400/600/1000
y = 0 reads `#e5e5e5` (floor). So the maze is **≥ 8 rows**; I can see 7 complete
ones. `[MEASURED]`

*Floor.* Sampling a 21×21 patch at every cell centre on that lattice and taking
the modal tone gives, over the **98 non-white, non-tank cells**:
mean R = **229.01, σ = 0.10, min 229, max 230** — i.e. every floor cell is
`#e5e5e5`. `[MEASURED]` There is **no** two-tone mix. For comparison, the same
statistic on the post-classic frame `F-html5-generation-contrast-case.png` is σ = 7.44 with a 28-level
range.

The six white cells sample exactly `#ffffff`. `[MEASURED]`

*Walls.* Averaging the horizontal luminance profile across rows 210–319 through
the isolated vertical wall at x ≈ 830: floor 229.0, trough minimum 72.0,
**half-maximum width 6.53 capture px** → wall/cell = **0.099**. `[MEASURED]`
Four further interior walls on row 240 measure 6.52, 6.53, 6.55, 6.65.
The maze boundary band is 8 px wide against the interior 6.5 → the boundary is
drawn ≈ 1.2× thicker. `[MEASURED]`
Wall interior tone, sampled in a 12×100 box at (826,215)-(838,315):
`#4c4c4c` dominant (182 px), i.e. **rgb(76,76,76)**. `[MEASURED]`

*Level-shift control.* Pure `#000000` (126 px) and pure `#ffffff` (339 842 px)
both occur in this frame, so the capture pipeline has not applied a
studio-swing/full-range levels shift that would move `#444444` to `#4c4c4c`.
`[MEASURED]` The floor and wall tones above can be taken at face value to
within compression noise.

*Tanks.* Saturated-colour masks (`G>R+40 & G>B+40`, and the blue equivalent)
give: green object bbox 32×33, 572 mask px; blue object bbox 34×33, 670 mask px.
Uniform dark-blob measurement (`luma<200`) gives 39×39/892 px and 38×40/846 px.
So **tank bbox ≈ 39 px in a 66 px cell = 0.59 cell**; √area/cell = 0.45.
`[MEASURED]`

*HUD.* All three tank thumbnails measure exactly **126×72** capture px.
`[MEASURED]` Positions: entry 1 tank x 270–395 with score `28` at x 406–441;
entry 2 tank x 570–695; entry 3 **score `21` at x 890–923 with the tank at
x 934–1059**. Digit height 23 px. The third thumbnail is the **mirror** of the
others (same 126×72 footprint, barrel pointing left).
`[MEASURED]` HUD group centre (270+1059)/2 = 664.5 against maze centre
(172.5+1162.5)/2 = 667.5 — the HUD is centred under the maze to within 3 px.
`[MEASURED]`

Icons: gear bbox 28×29 at (89,506); speaker bbox 27×25 at (90,548); both ink
modal `#666666`, darkest pixel luminance 98. `[MEASURED]`

Score ink: modal `#5d5d5d`, darkest pixel luminance 56 — mid-to-dark grey, but
the digits are too small for a fully-covered pixel, so the true ink is ≤ that.
`[UNCERTAIN]` I would not pin a hex.

Tank thumbnail body colours, sampled inside the hull: red `#990000` with shade
`#4d0000`; green `#009900` / `#004e00`; blue `#000099` / `#00004e`.
`[MEASURED]` A clean pure-channel ramp — 0x99 body, 0x4d/0x4e shade.

*Right-hand text.* `hvere are you` bbox 1133–1248 × 474–493 (116×20);
`by bulla` bbox 1184–1248 × 499–518 (65×20) — both flush right at x = 1248.
`version  4.0` bbox 1113–1247 × 553–569 (135×17), also flush right, with
visibly wide letter-spacing. Darkest pixel luminance: 199 for the maze name,
**194** for the watermark. `[MEASURED]` That is consistent with the editor
spec's `≈#bbbbbb` watermark rendered small (antialiasing lightens the darkest
pixel). `[INFERRED]`

Note the watermark's right edge (1247) is **84.5 capture px to the right of the
maze's right boundary** (1162.5) — so the watermark is anchored to the *stage*,
not the maze. `[MEASURED]`

**Links to the program**

- `srv/index.php:404` — `new SWFObject("includes/TankTrouble_v4.0.swf",
  "TankTroubleGame", "712", "490", "8", "#ffffff")`. The `#ffffff` stage
  background is exactly the tone the enclosed cells render (F2), which is
  consistent with those cells simply having **no floor drawn**. `[INFERRED]`
- `LEDGER.tsv` row 163: `srv/includes/TankTrouble_v4.0.swf  O  …
  archive/includes-tree/20130313_TankTrouble_v4.0.swf`. The on-screen
  `version 4.0` watermark identifies the running SWF as that file. `[INFERRED]`
- `docs/standards/MAZECREATOR-VISUAL-SPEC.md` "Wall color `#444444`", "Floor tones
  `#dddddd`/`#eeeeee`", "Wall thickness 4 px": this frame gives `#4c4c4c`, flat
  `#e5e5e5`, and 0.099 cell. **These are the game SWF's constants, not the
  editor's** — different SWF, so the spec is not contradicted, but the two
  renderers are now known to differ and that fact belongs in the spec.
- Grep results: `hvere` → 0 hits, `bulla` → 0 hits, `version 4.0` → 0 hits in
  `srv/index.php`. All three strings are SWF-side. `[MEASURED]` (clean misses)

**What this does NOT show**

No crates (there are none in this round). No chat. No usernames — these are
guest players, so it cannot speak to the logged-in HUD. No stage edges, so no
absolute scale. The maze top is cropped, so the row count is unknown.

---

### `Game/F-gameplay-2015-page-beta-sidebar.png` (1242×500, captured 16:23:14)  *(was `{B77B6A43-B2D1-4D46-9BDD-880073BB9C63}.png`)*

`./Game/F-gameplay-2015-page-beta-sidebar.png`

**Filename claim:** none.

**This is the same video frame as `F-gameplay-three-guests-maze-crop.png`, at a wider crop / lower zoom.**
`[MEASURED]` — proof: building the cell-tone grid on each frame's own lattice
(15 columns × 7 visible rows) produces **identical** patterns:

```
...............        ...............
...............        ...............
.....W..W.W....        .....W..W.W....
....W?.........        ....W?.........
........W......        ........W......
..........W....        ..........W....
...............        ...............
     F-gameplay-three-guests-maze-crop.png             F-gameplay-2015-page-beta-sidebar.png
```

(`.` = floor `#e5e5e5`, `W` = `#ffffff` enclosed cell, `?` = tank.) Tank and
smoke positions match too. Scale ratio 66.0 / 44.97 = **1.468**.

**What is drawn (beyond the shared frame)**

The full page around the stage:

- **Left sidebar** (cut at x = 0, right edge at x = 125.5):
  - a `Log in` button beside a `Sign up` link;
  - a rounded grey box reading **`Access` / `Online BETA`** (bold) then
    **`Beta access` / `required`**, over a faint greyscale illustration of a
    tank with radiating sunburst rays. `[OBSERVED]`
  - a box with a **green header** reading **`Shop Open`** in white bold, body
    **`Get BETA access here!`** in grey on white. Header green measures
    `#2bdd72` (21.6% of the header box). `[MEASURED]`
  - a `Visits` box (header tone `#d3d3d3`).
- **Footer**, centred: `Copyright www.purup.com 2007 – 2015`. `[OBSERVED]`

**Transcriptions (verbatim)**

```
Log in   Sign up

Access
Online BETA
Beta access
required

Shop Open
Get BETA
access here!

Visits
Since 2007-12-16
42315370
Today: 21657
Online: 833
Tank owners:
1534911
Logged in: 245

Copyright www.purup.com 2007 – 2015
```

HUD, unchanged from `F-gameplay-three-guests-maze-crop.png`: gear + speaker, red `28`, green `29`, `21`
blue (mirrored), `hvere are you` / `by bulla`, `version  4.0`.

**Measurements**

- Maze pitch **44.97** capture px, 15 columns (border centres 386 and 1060.5,
  674.5 / 15 = 44.97). Interior wall half-max widths on row 200: 4.43–4.67 →
  **wall/cell = 0.100**, matching `F-gameplay-three-guests-maze-crop.png`'s 0.099 as it must. `[MEASURED]`
- Floor luminance 229 at every sampled point; y = 0 at x = 400 and x = 1000 is
  floor, confirming the maze top is cropped here too. `[MEASURED]`
- Copyright glyph rows 486–497; `version 4.0` watermark glyph rows 374–383;
  sidebar box right edge (background 211 → page white 255) at x = 125.5.
  `[MEASURED]`

**Scale estimate, and why I will not pin it** `[UNCERTAIN]`

The era layout gives a genuinely useful anchor: `srv/index.php:452-453` puts the
left banner at `width: 160px; float: left; margin-right: 20px`,
`srv/index.php:466` puts the box column at `width: 120px; float: left`, the
centre column at `width: 692px; float: right` inside a `width: 1002px` block
(`srv/index.php:308-311`), and `#TankTrouble` at `left: -10px`
(`srv/index.php:324`). Arithmetic: box-column right edge = container + 300;
centre column left = container + 310; SWF left = 310 − 10 = container + 300.
**The SWF's left edge coincides exactly with the box column's right edge.**

If the maze were horizontally centred in the SWF, that forces scale = 1.679 —
but that scale puts the copyright line 940 capture px below the stage top, i.e.
the stage bottom at y = 366, *above* the HUD and the watermark. Contradiction.
If instead I assume the `version 4.0` watermark is flush to the stage bottom
(as `docs/standards/MAZECREATOR-VISUAL-SPEC.md` measured for `version 0.3` — "bottom edge
≈ 400 (flush corner)"), the copyright's 70 CSS px offset gives scale ≈ **1.39**,
and then the maze is not centred in the stage.

Both readings cannot be right. The most likely resolution is that **this is a
2015 page and the 2018 layout constants I grepped do not apply to it** — the
2015 sidebar (Access Online BETA / Shop Open) is demonstrably a different box
set. I therefore report **capture pixels only** and state the scale as
**1.4 ± 0.3**, which is too loose to derive a stage constant from. A frame of
the *2017-2018* page with the game running would collapse this immediately.

**Links to the program**

- `srv/index.php:328-329` — `<div class="text small gray" id="gameCopyright" …
  top: 550px;"> Copyright <a href="http://www.purup.com" …>www.purup.com</a>
  2007 &ndash; 2018`. This frame reads **2015**. The held bytes' year is 2018.
  That is the cleanest single dating datum in my whole set. `[MEASURED]`
- `srv/index.php:1067-1069` — the held Visits box:
  `<div class="header text normal gray">Visits</div> … Since 2007-12-16<br/>
  <div … class="text normal">68466319</div>Today: 19254<br/>Online: 184<br/>
  Tank owners: 1699890<br/>Logged in: 184<br/>`.
  **The label set, order, punctuation and the `Since 2007-12-16` anchor are
  identical to this 2015 frame**; only the numbers differ (42 315 370 vs
  68 466 319; 1 534 911 vs 1 699 890 tank owners). This is direct support for
  `docs/standards/DIVERGENCES-SERVED.md` §3 / **S105** — the format did not change between
  2015 and 2018. `[MEASURED]`
- Greps against `srv/index.php` — clean misses, all zero hits:
  `Beta access required`, `Get BETA access here`, `Access Online` (the phrase),
  and `Shop Open` as a box header (the four hits are all news-item text at
  `:7328`, `:7338`, `:7476`, `:7488`, `Kickstarter Latecomers' Shop Open…`).
  `Log in` and `Sign up` **do** appear, at `srv/index.php:579-580`. `[MEASURED]`
  So: the login row survived to 2018; the two promo boxes did not.
- The "Access Online BETA" box's faint sunburst-tank background is a `.box`
  *variant with a background image* — the family **S16** flags
  (`.box.christmas/.halloween/.glitch/.kickstarter` in `boxStyles.css`, "used by
  zero captured page"). This is the first rendered instance of any such variant
  I have seen. `[INFERRED]` — I cannot name which class it is without the CSS
  staged.

**What this does NOT show**

The right column is entirely off-frame. No ad slots visible (S23 untouched). The
stage edges are still invisible. Nothing about 2017-2018 chrome.

---

### `Game/F-gameplay-maze-61-crates.png` (1031×770, captured 16:24:50)  *(was `{60BCFBE2-EF13-4549-A040-8BAA1119828E}.png`)*

`./Game/F-gameplay-maze-61-crates.png`

**Filename claim:** none.

**What is drawn**

A complete maze, boundary visible on all four sides, containing **61 small grey
rotated squares** distributed across the floor, one per cell in the cells that
have them. `[OBSERVED]` Two tanks: green at ≈(572,204), red at ≈(917,623).
One black dot at ≈(588,300). Below: a speaker icon at far left (partly cut by
the frame edge), a red tank thumbnail with `1`, then `0` with a **mirrored**
green tank thumbnail, and `versio…` cut off at the right edge. `[OBSERVED]`

**Transcriptions**

Scores: `1` (red), `0` (green). No usernames. Watermark cut to `versio`.

**Measurements**

- Maze boundary: x 129 → 953 (824 px), y 38 → 656 (618 px). A lattice of
  **pitch 51.5** at those origins overlays every wall in the frame (verified by
  rendering a red 16×12 grid over the image and inspecting). → **16 columns ×
  12 rows**. `[MEASURED]`
- Floor: modal tone at all **192** cell centres — 153 cells `#e6e6e6`, 19
  `#e8e8e8`, 12 `#e7e7e7`, 7 `#e5e5e5`, 1 `#eaeae9`; **mean R 230.2, σ 0.72,
  full range 229–234**. `[MEASURED]` A 5-level spread is compression noise; the
  editor's two tones are 17 levels apart. **Single flat floor tone, confirmed on
  a second, much larger sample.**
- **Crates.** Connected-component analysis of `luma<205` blobs in the 20–40 px
  size band yields **61 objects**: bbox mean **29.9 × 29.7** (min 24, max 33),
  filled area mean **592 px²** (min 566, max 736). √592 = 24.3 px.
  Against pitch 51.5 → **side ≈ 0.47 cell, bbox ≈ 0.58 cell**. `[MEASURED]`
- Crate colour: in a 37×37 crop centred on one crate, **zero pixels** have
  (max channel − min channel) > 6 — the sprite is **pure greyscale**.
  `[MEASURED]` A horizontal cut through a crate reads
  floor 230 → border ≈ 142 → body 90–160 with a gradient → glyph **57–59** →
  body → border → floor 230, over 30 px. The floor immediately adjacent is
  `#e6e6e6`, unchanged — **there is no glow**. `[MEASURED]`
- Crate glyph: a contact sheet of eight crates at 4× shows the *same* dark
  glyph in every one, rotated with its crate; it reads as a **`?`** (and as an
  `S`/`2` when rotated ~120–180°). `[OBSERVED]`/`[UNCERTAIN]` on the exact
  character.
- Crate placement: each crate sits at a cell centre; rotations vary
  continuously. `[OBSERVED]`
- Tanks: dark-blob bbox 45×40 (green, area 1182 — likely merged with an adjacent
  crate) and 43×36 (red, area 986). Against pitch 51.5 that is bbox 0.70–0.87
  cell, higher than the 0.52–0.61 seen elsewhere; I treat the green figure as a
  merged blob and do **not** use this frame for the tank/cell ratio.
  `[UNCERTAIN]`
- Icons: scanning the whole region y 660–770, x 0–120 for `luma<200` finds dark
  pixels **only** at y 739–760, x 0–23 — the speaker. **There is no gear or door
  icon above it in this frame.** `[MEASURED]`

**Links to the program**

- **`LEDGER.tsv` row 2: `srv/Assets/Crate.swf` is held `O`** (sha256
  `19c320ea…`, from `archive/classic.tanktrouble.com/Assets/Crate.swf`, era
  method "identical+era-confirmed"). So the crate artwork is *already in the
  repo as original bytes* — this frame is not a source for it, it is an
  **oracle to validate a render against**. Rows 3 and 5
  (`srv/Assets/GameTank.swf`, `srv/Assets/Tank.swf`) give the same standing to
  the tank art.
- `docs/standards/MAZECREATOR-VISUAL-SPEC.md`, "Crate spawn icon": *"axis-aligned amber
  square ≈16×16 with darker border + soft yellow glow; core ≈ (219,183,85),
  border darker ≈ (170,130,50)"*. The live crate is **grey, randomly rotated,
  and unglowed**, at side ≈ 0.47 cell against the marker's 16/32 = 0.50 cell.
  **The footprint matches; nothing else does.** These are two different objects
  and the spec is right to call one a *spawn icon*. My recommendation below is
  to say so explicitly in the spec so nobody later "fixes" the editor marker to
  look like the crate. `[MEASURED]`

**What this does NOT show**

No page chrome at all, so this frame cannot be dated. No chat. No usernames.
Whether 61 crates is normal accumulation or an unusual state is unknowable from
one still. `[UNCERTAIN]`

---

### `Game/F-video-card-beginner-league.png` (1275×690, captured 16:34:05)  *(was `{47111A69-3425-4628-BA3A-F77E1D02E573}.png`)*

`./Game/F-video-card-beginner-league.png`

**Filename claim:** none.

**What is drawn.** A 2×2 grid of pale-blue panels separated by thick black
rules, inside a thick lavender border. Each panel holds a gold chevron insignia
above a rank name in a heavy white cartoon face with a black outline and drop
shadow. `[OBSERVED]` A very faint blue caption is ghosted across the middle
rule — it is legible in `F-video-card-beginner-league-caption.png` as `The beginner league`, and in this frame
it is mid-fade. `[OBSERVED]`

**Transcription (verbatim)**

```
Dog Food        Lab Rat
Intern          Scavenger
```

Insignia, reading with the same layout: **Dog Food** = 1 chevron, no star;
**Lab Rat** = 1 chevron + 1 star; **Intern** = 1 chevron + 2 stars;
**Scavenger** = 1 chevron + 3 stars. `[OBSERVED]`

**Measurements.** Panel fill `#e8f3f9` (49.35% of the frame); border/rule
lavender `#a178af` (5.34%). `[MEASURED]` A 4× crop of the Dog Food chevron shows
gold/amber fill with a black outline and a **lavender halo** — the halo colour
matches the card border, and in the red-themed cards (`F-video-card-scientist-league.png`,
`F-video-card-scientist-league-caption.png`) the halo is red instead. `[MEASURED]` **The halo is the video
author's styling, not game art.** `[INFERRED]`

**Links to the program.** This is a rank card, which is topic **H (ranks)**'s
subject; I record it because it was assigned to me. `srv/index.php:9181` and
`:13845-13848` are the only rank surfaces in the held bytes ("What's Your Tank
Rank?" → `<a href='' id='tankRanks'>Tank Rank by Experience</a>`), i.e. the
`/tankRanks/` popup of **S83**. None of these four rank names appears in
`srv/index.php` (grep: `Dog Food`, `Lab Rat`, `Scavenger` → 0 hits;
`Intern` appears only in news prose at `:7160`/`:7167`). `[MEASURED]` — clean
miss, as expected for a SWF/popup-side feature.

**What this does NOT show.** No game stage, no HUD, no chat. Nothing datable —
no site chrome, no version watermark. It cannot be assigned to a generation.
`[NOT VISIBLE]`

---

### `Game/F-video-card-beginner-league-caption.png` (1266×650, captured 16:34:19)  *(was `{9DF5F575-CCBE-4C44-A576-EAC0B1AF8251}.png`)*

`./Game/F-video-card-beginner-league-caption.png`

**Filename claim:** none. **My task brief's description of this file is wrong**
— see the correction at the top of this document.

**What is drawn.** The same four-panel rank card as `F-video-card-beginner-league.png`, 14 seconds
later in capture order, now with the caption fully faded in: a bright light-blue
cartoon-face line `The beginner league` straddling the horizontal rule.
`[OBSERVED]` The two frames are otherwise the same graphic at a slightly
different crop (1266×650 vs 1275×690).

**Transcription (verbatim)**

```
Dog Food        Lab Rat
     The beginner league
Intern          Scavenger
```

**Measurements.** Panel fill `#e8f3f9` (48.36%), border `#a178af` (4.24%) —
same palette as `F-video-card-beginner-league.png` to within compression noise. `[MEASURED]`
The pair `F-video-card-beginner-league.png` → `F-video-card-beginner-league-caption.png` is a **caption fade-in**, captured before
and after; that is the only motion evidence these two frames carry.
`[INFERRED]`

**Links to the program.** As `F-video-card-beginner-league.png`. Bears on **S83** (`/tankRanks/`
popup) only as a name list, and on topic H.

**What this does NOT show.** No login sidebar, no Exp figures, no Access Online
BETA panel, no game stage, no chrome, no version watermark. `[NOT VISIBLE]`

---

### `Game/F-video-card-scientist-league.png` (1281×698, captured 16:36:14)  *(was `{46F00358-FE88-40FF-9150-6A21DBA00B38}.png`)*

`./Game/F-video-card-scientist-league.png`

**Filename claim:** none.

**What is drawn.** The same card format, second league: mint-green panels, thick
red-orange border and rules. Four gold chevron insignia with rank names.
`[OBSERVED]` The bottom-right name is rendered in **red-orange with a white
outline** while the other three are white with a black outline — the theme
colour marks the top rank of the league. `[OBSERVED]`

**Transcription (verbatim)**

```
Jr. Scientist       Scientist
Lead                Mad
Scientist           Scientist
```

Insignia: **Jr. Scientist** = 3 chevrons, no star; **Scientist** = 3 chevrons +
1 star; **Lead Scientist** = 3 chevrons + 2 stars; **Mad Scientist** =
3 chevrons + 3 stars. `[OBSERVED]` Cross-reading against `F-video-card-beginner-league.png`
(1 chevron + 0..3 stars) the scheme is *chevron count = league, star count =
rank within league*. `[INFERRED]` — falsifiable by any league with a
non-matching chevron count.

**Measurements.** Panel fill `#a3dbcc` (42.83%); border `#e84d35` (5.51%).
`[MEASURED]` At the extreme right edge, x ≈ 1230–1260, y ≈ 455–490, there is a
faint translucent glyph — a rounded square containing a diagonal arrow pointing
down-right into a tray. `[OBSERVED]` It sits half on the mint panel and half on
the red border, and it is semi-transparent. That is the signature of a
**video-player or capture-tool overlay control**, not site or game art.
`[UNCERTAIN]` I would not read anything into it.

**Links to the program.** As above — topic H / **S83**. Zero hits in
`srv/index.php` for `Scientist` as a rank (the only `Scientist`/`scientists`
hits are news prose). `[MEASURED]`

**What this does NOT show.** Nothing about the site. `[NOT VISIBLE]`

---

### `Game/F-video-card-scientist-league-caption.png` (1283×718, captured 16:36:31)  *(was `{91B492F8-C25F-440A-A1CF-5F3105D1AEAA}.png`)*

`./Game/F-video-card-scientist-league-caption.png`

**Filename claim:** none.

**What is drawn.** `F-video-card-scientist-league.png` 17 seconds later, with the league caption faded
in: `The Scientist League` in red-orange cartoon face across the middle rule.
`[OBSERVED]`

**Transcription (verbatim)**

```
Jr. Scientist        Scientist
     The Scientist League
Lead                 Mad
Scientist            Scientist
```

Note the capitalisation differs between the two league captions: lower-case
`league` in `The beginner league` versus capital `League` in
`The Scientist League`. `[OBSERVED]` — transcribed as seen; that inconsistency
is the video author's, not the game's.

**Measurements.** Panel fill `#a3dbcc` (38.84%), border `#e94e36` (1.93% — lower
than `F-video-card-scientist-league.png`'s 5.51% because this crop includes less border).
`[MEASURED]`

**Links to the program.** As above.

**What this does NOT show.** Nothing about the site. `[NOT VISIBLE]`

---

### `Game/F-html5-generation-contrast-case.png` (1286×725, captured 16:37:38)  *(was `{F11210C7-8FE2-441F-938C-962FE5591AD3}.png`)*

`./Game/F-html5-generation-contrast-case.png`

`[This frame is a different, later generation — the contrast case.]`

**Filename claim:** none.

**What is drawn**

A full page with the TankTrouble logo and a nav strip of four grey folder tabs
(`OPEN` placard, a radio/megaphone, a `?!` speech bubble, and one blank), a game
stage with a red **✗ close button** at its top right, a left sidebar, a right
sidebar, and a Google-ad creative on each flank. `[OBSERVED]`

Left sidebar, top to bottom:

```
Scrapyard
2453183314

[3-chevron + 3-star insignia]
Tank Rank
has been
Deployed
Read more

Battle mode:
Classic
Never-ending
destruction!
Next battle mode
starts in
1 minute.
Read more
```

Right sidebar:

```
Download on the
App Store

GET IT ON
Google play

WALLoFAME
COMMEMORATING
BACKERS AND FRIENDS

Message the
laboratory
Got ideas, found
a bug, need help or
just love trouble?
Let the scientists
know!
```

(`a bug` is a blue hyperlink. `WALLoFAME` is set as `WALL` + small-caps `of` +
`FAME` on one line.) `[OBSERVED]`

In the maze: a khaki tank beside a **blue** rotated square with a pale ring, a
red tank, a grey smoke plume, several small yellow shrapnel shapes, and two
black dots. `[OBSERVED]`

HUD, five entries, each = accessorised tank thumbnail, username below it in
white with a black outline, a small chevron after the name, and a
`kills • deaths` pair below that:

```
Happyhour888 ^      6•2      (a small skull glyph left of the score)
moscles25 ^         0•0
carlosr117 ^       15•8
yungkidd12 ^      25•10      (a small crown glyph right of the score)
Vireaux ^           6•5
```

A sixth, unnamed white/grey tank with a blue medical cross sits at the far
right. `[OBSERVED]` `[UNCERTAIN]` what it represents.

**Measurements**

- Maze lattice: boundary bands at x 301.5 / 1052.5 and y 68.5 / 506.5; interior
  gridlines at 426.5, 802.5 and 318.5, 381.5. Common pitch **62.58**;
  751/62.58 = 12.0 columns, 438/62.58 = 7.0 rows → **12 × 7**. Wall band width
  **4 px** → wall/cell = 0.064, distinctly thinner than the classic build's
  0.099–0.121. `[MEASURED]`
- **Floor is two-tone.** Modal tone at each of the 84 cell centres: `#e8e8e8`
  ×27, `#dadada` ×29, `#ffffff` ×7 (enclosed), plus compression-shifted
  neighbours around the explosion. Excluding white cells, **mean R 224.2,
  σ 7.44, range 28** — bimodal, against the classic build's σ 0.10 / 0.72.
  `[MEASURED]`
- The two tones do **not** follow a parity rule. Row 6 reads
  `D L D L D L D L L D L D` (nearly alternating) but row 0 reads
  `D D L L L D D D D D D D` and row 1 `L L L L L L D L W L L D`. No
  row/column/checkerboard rule fits. `[MEASURED]`
- Light/dark split is roughly **1 : 1** (27 : 29), against the editor
  screenshot's ≈ 1 : 2 (15 light : 29 dark).
- Whole-frame dominant tones: `#ffffff` 26.8%, `#e8e8e8` 7.4%, `#dadada` 6.8%.
  `[MEASURED]`

**Links to the program — this is where it stops being the target build**

Greps against `srv/index.php`, all **zero hits**: `Battle mode`, `Deployed`,
`Message the laboratory`, `Never-ending`, `Google play`, `WALL`. `[MEASURED]`

What the held bytes have instead:

- `srv/index.php:1163-1165` — the App Store and Google Play boxes exist, but as
  `images/availableOnTheAppStore120.jpg` and `images/getItOnGooglePlay.png`
  inside plain `<div class="box">`s.
- `srv/index.php:1183-1196` — the feedback box is
  `<div class="box mobile"><div class="header text normal">Got Feedback?</div>
  … Got ideas?<br/>Found Bugs?<br/>Urge to praise us to the skies?<br/>Then give
  us your feedback <img src="images/envelope.jpg" …>`.
  The frame's `Message the laboratory / Got ideas, found a bug, need help or
  just love trouble? Let the scientists know!` is a **rewrite of that box**.
  `[OBSERVED]`
- `srv/index.php:7297` — `<li>Wall of Fame</li>` appears **only** inside a news
  item describing new **Online BETA** features, alongside
  `<li>Chat bubble appear in game when tanks chat</li>` (`:7293`) and
  `<li>Press Enter from the lobby to start chatting</li>` (`:7296`). So the WALL
  of FAME box is a post-classic, Online-BETA-era feature. `[INFERRED]`
- `srv/index.php:467` / `:488-490` — the era Scrapyard is a Phaser widget in a
  `box special`; the frame's Scrapyard is a similar flip counter, value
  `2453183314`.

**Generation verdict:** `[INFERRED]` — **post-classic (Online BETA / HTML5
lineage)**. Reasons, in strength order: (a) four of its sidebar strings are
absent from the era bytes and one of them ("Wall of Fame") is announced as an
Online BETA feature in the era news; (b) no `version N.N` watermark on the stage
at all; (c) the maze floor is two-tone where the classic v4.0 floor is
provably flat; (d) the wall/cell ratio is 0.064 against the classic 0.10–0.12;
(e) the HUD shows `kills • deaths`, rank chevrons and accessories, none of which
the classic HUD has. `DEDUCE.md:288` and `:374-396` already treat the HTML5
client as a separate tree.

**What this does NOT show.** Nothing about the 2017-2018 Flash page. Its only
value to the rebuild is as a *negative control* — it shows what the successor
looks like, so future evidence can be sorted correctly.

---

### `UI/F-chat-message-stack-in-stage.png` (980×776, captured 16:55:20)  *(was `{5234E61B-0B7D-47D5-8E71-3CA300A31A82}.png`)*

`./UI/F-chat-message-stack-in-stage.png`

**Filename claim:** none.

**What is drawn**

The game stage with **five stacked green chat message strips** across the top,
a **green chat input bar** lying diagonally across the upper-middle of the
maze, three tanks with **coloured name labels** floating beside them, and a
three-entry HUD with usernames. A sliver of the page's left sidebar is visible
at x < 20. `[OBSERVED]`

**Transcriptions (verbatim, top strip first)**

```
revengexx1 says 'I wont tell you'                              (faded, partly occluded)
revengexx1 says 'And i will show you, how i go through walls :)'
Blaze4330 says 'whut?'
revengexx1 says 'Tanktrouble gaming here'
revengexx1 says 'Ello'
```

The top strip is `[UNCERTAIN]` — it is both alpha-faded and overlapped by the
strip below it; after a contrast stretch the readable fragments are
`reveng…` `…says 'I wont tell you'`. The capital/lower-case of `I` is not
resolvable.

Input bar: `Chat:` (label) followed by an empty field — the bar is open with no
text. `[OBSERVED]`

In-maze name labels, each in its player's colour: `revengexx1` (dark red, top
right), `Blaze4330` (blue-violet, partly hidden behind the bar),
`rushabh4084` (red). `[OBSERVED]`

HUD: `Blaze4330` `0` · `revengexx1` `3` · `rushabh4084` `3`, with a **door**
icon above a **speaker** icon at far left and `version` (cut) at the right.
`[OBSERVED]`

**Measurements**

- Maze pitch **80.2** capture px (gridlines at 200.5, 360.5, 520.5, 680.3,
  842.6 — deltas 160, 160, 160, 162 read on a row that happened to catch
  alternate lines; overlaying an 80.2 lattice aligns every wall in the frame).
  Interior wall half-max width 8.45–8.54 → **wall/cell = 0.106**. `[MEASURED]`
- Floor luminance 229 throughout (`#e5e5e5`). `[MEASURED]`
- **Message strips**: green vertical runs at x = 700 are y 61–94, 111–144,
  161–194, 211–244 → **height 34 px, pitch 50 px, gap 16 px**. `[MEASURED]`
- **Widths**: strips span x 124–928 (**805 px**); the input bar spans x 165–874
  (**710 px**); the maze spans x 195–847 (**652 px**). So the chat furniture is
  sized to the *stage*, not the maze, and both overhang the maze on both sides.
  `[MEASURED]`
- **Strip fill**: `#95cc9b` at mid-height, with a vertical gradient darkening to
  `#78b07d` near the bottom edge. The gaps between strips read `#a8aba8` — a
  neutral grey, i.e. a shadow, not floor. `[MEASURED]`
- **Faded top strip**: fill `#d9eddd` against the others' `#95cc9b`.
  `[MEASURED]`
- **Input bar fill**: `#90da99` in this frame (`#8ddc97` in the dedicated
  crops). `[MEASURED]`
- Tank blob: 49×40, area 1266 at pitch 80.2 → bbox 0.61 cell, √area/cell 0.44.
  `[MEASURED]`
- Icons: door bbox at ≈(33,630)-(48,655); speaker below it at ≈(33,668).
  `[OBSERVED]`

**Message ordering** `[INFERRED]`

Reading the five strips **bottom to top** gives a coherent conversation:
`Ello` → `Tanktrouble gaming here` → `whut?` → `And i will show you, how i go
through walls :)` → `I wont tell you`. Combined with the fact that the *topmost*
strip is the semi-transparent one, the model is: **a new message fades in at the
top of the stack and pushes older ones down; the oldest drop off the bottom.**
`F-gameplay-2013-page-round-countdown.png` independently supports it (`i cant seee the screen` at the bottom,
`now i can` at the top). This would be falsified by any frame where a
*bottom* strip is the faded one.

**Links to the program**

- **`srv/index.php` contains no chat feature.** Full grep results:
  - `Chat:` → 0 hits.
  - ` says '` → 0 hits (`says` appears 3 times, all news prose: `:7160`,
    `:7167`, `:10112`).
  - `chat` (case-insensitive) → 10 hits, **every one inside a news item's body
    or `description:` string**: `:6634`, `:6643`, `:7047`, `:7059`, `:7293`,
    `:7295`, `:7296`, `:7305`. No element id, no CSS class, no handler.
  - `Chat` (capitalised) → 2 hits, both the same news item (`:7293`, `:7305`).
  `[MEASURED]` — a clean, total miss.
- **Conclusion on generation:** the chat is **not** evidence of a different
  build. The stage in this session carries the `version` watermark and the same
  flat `#e5e5e5` floor, `≈0.10` wall ratio and half-cell tanks as the
  demonstrably-v4.0 frames. The chat therefore lives **inside
  `srv/includes/TankTrouble_v4.0.swf`** — which is held `O` (`LEDGER.tsv` row
  163) and which `srv/index.php:404` embeds on the era page. The page has no
  chat because the page never had one; the game did. `[INFERRED]`
  The decisive confirmation is cheap and I recommend it below: **scan the held
  `TankTrouble_v4.0.swf` for the literal strings `Chat:` and `says '`.**
- Caveat I cannot close: the news items at `:7293-7296` describe an
  *Online BETA* chat ("Chat bubble appear in game when tanks chat", "Press
  Enter from the lobby to start chatting"). That is a **different** chat — this
  one has no bubbles and no lobby. `[OBSERVED]` I have not excluded the
  possibility that these frames come from a third-party multiplayer rehost of
  the v4.0 SWF; `revengexx1 says 'TTG Multiplayer!!!…111'` in `F-gameplay-2013-page-round-countdown.png` is
  faintly suggestive of one. `[UNCERTAIN]` The string scan settles it.

**What this does NOT show.** Only a sliver of page chrome, so this frame alone
cannot be dated; I date it by style association with `F-gameplay-2013-page-round-countdown.png`/`F-gameplay-2013-page-four-tanks.png`
(same door+speaker icons, same username-under-tank HUD, same players
`revengexx1`/`rushabh4084`). `[INFERRED]`

---

### `UI/F-gameplay-2013-page-round-countdown.png` (1191×767, captured 16:55:44)  *(was `{DE1A72E2-BEDF-4001-9ABE-C5BB117CED10}.png`)*

`./UI/F-gameplay-2013-page-round-countdown.png`

**Filename claim:** none.

**What is drawn**

A whole page: a `TANKTROUBLE.com` wordmark and **four** grey folder tabs (a
`NEWS` placard, a wrench, a speech bubble, a flask) — not the six-tab era strip.
Below, the stage with three chat strips at the top, a 6×3 maze, two tanks, a
large white **round-countdown card showing `3`** drawn tilted, a yellow ring
around the mouse cursor, a four-entry… no — a **three-entry HUD**, and the
footer. `[OBSERVED]`

**Transcriptions (verbatim)**

Chat strips, top to bottom:

```
j-dog78 says 'now i can'
revengexx1 says 'TTG Multiplayer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111'
j-dog78 says 'i cant seee the screen'
```

The exclamation-mark count is `[UNCERTAIN]`: stroke analysis on the glyph row
finds **31 separable strokes at 4.43 px pitch** between the merged word blob and
the `111`, but the leading marks merge with `Multiplayer` below the resolution
limit, so **≥ 31** is the defensible statement.

HUD: `j-dog78` `2` · `revengexx1` `14` · `rushabh4084` `7`, plus `version  4.0`
at the right, and a door icon above a speaker icon at far left. `[OBSERVED]`

Footer, two centred lines:

```
Copyright www.purup.com 2007 – 2013
Design: Mads Purup, Programming: Brian Bunch Christensen, Server: Søren Boll Overgaard
```

Bottom-left, the recorder watermark: `…ast-O-Matic.com`.

An in-maze name label `revengexx…` in dark red at the right edge of the strip
stack. `[OBSERVED]`

**Measurements**

- Maze: boundaries at x 261 / 929 and y 197.5 / 534; interior gridlines fit
  **pitch 112.1**, and an overlaid 6×3 red lattice lands on every wall in the
  frame (verified visually). → **6 columns × 3 rows**. `[MEASURED]`
- Interior wall half-max width **13.6** → wall/cell = **0.121**. `[MEASURED]`
- Floor luminance 228–229 (`#e4e4e4`/`#e5e5e5`). `[MEASURED]`
- **Strip translucency, measured properly.** At y = 175 the strip fill is
  `#93cc9b` at x = 650 and `#6fa877` across x = 699–712. There is **no wall** at
  x = 700–721 at y = 250 (plain floor `#e4e4e4`), so the dark band is not the
  maze below — but x = 709 *is* a maze gridline, so it is a wall in the maze's
  top row, which the strips cover. Solving the two-background alpha equation on
  the green channel (over floor 229 → 204; over wall 76 → 167):
  `1 − α = (204 − 167)/(229 − 76) = 0.242` → **α ≈ 0.758**, intrinsic strip
  colour **≈ rgb(121, 196, 134) = `#79c486`**. Back-substituting predicts
  R = 110, B = 120 over the wall; measured 111 and 119–121. `[MEASURED]`
- Strip geometry: green runs at x = 900 are y 75–103, 116–143, 156–183 →
  height 28–29, pitch 40.5. At x = 300 the same strips are 24, 9+11, 22 tall —
  i.e. **shorter on the left than the right**, the same right-taper as the input
  bar. `[MEASURED]`
- Tank blobs: 58×64 (area 2162) and 54×65 (area 2147) at pitch 112.1 →
  bbox 0.52–0.58 cell, √area/cell **0.41**. `[MEASURED]`

**Links to the program**

- `srv/index.php:329` reads `2007 &ndash; 2018`; this frame reads **2013**.
  `[MEASURED]`
- The credits line `Design: Mads Purup, Programming: Brian Bunch Christensen,
  Server: Søren Boll Overgaard` returns **zero hits** for `Mads Purup`,
  `Brian Bunch` and `Overgaard` in `srv/index.php`. `[MEASURED]` The credits
  line was **removed** between 2013 and the era bytes. That is a new, dateable
  divergence between the 2013 and 2018 footers, and it belongs in `DEDUCE.md`.
- The four-tab nav is not the era six-tab strip (`srv/index.php:302`:
  `menuStartSelect.jpg`, `tab1Select.jpg`, … `tab6Deselect.jpg`,
  `menuEndDeselect.jpg` inside `<td style="width: 708px;">`). Bears on **S2**
  and **S10** only as "the strip had a different generation in 2013".
  `[OBSERVED]`
- `version  4.0` on the stage ⇒ the SWF is `TankTrouble_v4.0.swf`, whose ledger
  source is a **2013-03-13** capture. A 2013 page running the 2013 SWF is
  exactly consistent. `[INFERRED]`

**What this does NOT show.** No sidebars (the frame is cropped to the centre
column plus grey page margin). No stage edges. No settings gear.

---

### `UI/F-gameplay-2013-page-four-tanks.png` (1195×769, captured 16:56:05)  *(was `{FFAE5568-B5FA-478F-B166-4CA448E1C6C3}.png`)*

`./UI/F-gameplay-2013-page-four-tanks.png`

**Filename claim:** none.

**What is drawn**

Same page and same session as `F-gameplay-2013-page-round-countdown.png`, 21 s later in capture order: same
wordmark and four tabs, same footer, same recorder watermark. One chat strip
remains. The maze is now a **tall narrow** one. Two tanks are adjacent near the
bottom. The HUD has **four** entries. `[OBSERVED]`

**Transcriptions (verbatim)**

```
revengexx1 says '4 more minutes of Destruction'
```

HUD, left to right — thumbnail, score, then username centred underneath:

```
[khaki tank with a red bow]                 2     j-dog78
[red tank, pumpkin head, black crane-ball,
 white skull, gold star]                   24     revengexx1
[red tank, white flag with a crossed-out
 paw, pirate hat with skull, gold mace]    11     rushabh4084
[blue tank with a red bird/cockscomb]       4     stdorfner

version  4.0
```

Footer as `F-gameplay-2013-page-round-countdown.png`: `Copyright www.purup.com 2007 – 2013` /
`Design: Mads Purup, Programming: Brian Bunch Christensen, Server: Søren Boll Overgaard`.

**Measurements**

- Maze: full-height boundaries at x 484.5 and 710.5 (**226 px**); interior
  verticals at 541.25 and 653.75 → **pitch 56.4**, 226/56.4 = **4.0 columns**.
  Vertical extent ≈ y 105 → 540 (435 px) → **≈ 7.7 rows**, best read as 8 rows
  at pitch 54.4 or 7.7 at 56.4; I cannot separate the two because the top and
  bottom bands are soft. `[UNCERTAIN]` — **4 columns is solid; the row count is
  7 or 8.**
- Interior wall half-max width **6.68** → wall/cell = **0.118**. `[MEASURED]`
- Floor luminance 229. `[MEASURED]`
- Tank blobs: 34×28 (area 634) and 31×21 (area 578) at pitch 56.4 →
  bbox 0.55–0.60 cell, √area/cell **0.43**. `[MEASURED]`
- Left icons: a **door** above a **speaker**, same as `F-chat-message-stack-in-stage.png`.
  `[OBSERVED]`
- All four HUD entries are drawn the same way round (tank left, score right,
  name below). **No mirroring.** `[OBSERVED]`

**The scale-invariance experiment** `[MEASURED]` — the most load-bearing
measurement in this document after the floor tone

`F-gameplay-2013-page-round-countdown.png` and `F-gameplay-2013-page-four-tanks.png` are the **same session at the same capture zoom**
(same page, same window, 21 s apart). They show two different rounds:

| | maze | cell pitch (capture px) | maze extent (capture px) | tank √area | tank/cell |
|---|---|---|---|---|---|
| `F-gameplay-2013-page-round-countdown.png` | 6 × 3 | **112.1** | 672.6 × 336.3 | 46.4 | 0.41 |
| `F-gameplay-2013-page-four-tanks.png` | 4 × ~8 | **56.4** | 225.6 × ~451 | 24.5 | 0.43 |

Three conclusions follow directly:

1. **The in-game cell size is not a constant.** It differs by a factor of 1.99
   between two consecutive rounds on the same screen.
2. **The maze is scaled to fit a fixed stage viewport.** The 6-wide maze is
   width-limited at 672.6 px; the 8-tall maze is height-limited at ≈451 px.
   Viewport ≈ **672 × 451 capture px**, aspect **1.49** — close to the
   712 × 490 stage's 1.453 (`srv/index.php:404`). `[INFERRED]`
3. **The tank scales with the maze.** Tank linear size ratio
   √(2150/600) = 1.89 against a cell ratio of 1.99; tank/cell is 0.41 vs 0.43.
   The tank is a fixed fraction of a cell, not a fixed number of stage pixels.

Combined with all five v4.0 frames, the tank is **0.41–0.45 cell by √area** and
**0.52–0.61 cell by bounding box** (bbox varies with the tank's rotation).

**Links to the program**

- Same footer/credits/nav findings as `F-gameplay-2013-page-round-countdown.png`.
- **S113 ("Any page rendered logged-in — project boundary")**: this frame and
  `F-chat-message-stack-in-stage.png` are logged-in renderings of the **game** tab — four named
  accounts with custom painted tanks and accessories in the HUD. That is not the
  garage, but it is the first logged-in page rendering in this evidence set.
  `[OBSERVED]`
- **S30/S31 (era accessory catalogue, badge picker)**: these eight accessorised
  tank thumbnails are 2013 accessories, not 2017-18 ones, so they do not settle
  S30 — but they do prove the accessory system's *HUD presentation* (accessories
  render on the thumbnail, not just in the garage). `[OBSERVED]`

**What this does NOT show.** No sidebars. No gear icon. No crates. Nothing from
the target era.

---

### `UI/F-chat-bar-crop-1.png` (873×191, captured 17:08:46)  *(was `{099B8E88-41F9-46DC-B4BD-552ABD22B5F4}.png`)*

`./UI/F-chat-bar-crop-1.png`

**Filename claim:** none.

**What is drawn.** A tight crop of the chat input bar over the maze: a green bar
with a heavy black outline and a soft grey drop shadow beneath it, running
nearly the full crop width, tilted slightly and visibly **taller at the right
end than the left**. Its left end is cut on a slant (a parallelogram edge, not a
vertical one). Inside, in bold black: `Chat:` then two spaces then the typed
text and a caret. `[OBSERVED]`

**Transcription (verbatim)**

```
Chat:  im rec
```

`[MEASURED]` The last glyph looks like a `d` at first sight. It is not: at
x = 206–207 the vertical stroke spans y 60/61–80/81 (**21 px**) while the letter
bowls span y 67–77 (x-height 11 px, baseline ≈ 77–78). The stroke therefore
extends ~6 px above x-height **and 3–4 px below the baseline**. A `d` ascender
does not descend. It is a **text caret**, and the letter under it is `c`. The
next two crops (`im recording`, `im recording if you dont`) confirm the word.

**Measurements**

- **Fill colour `#8ddc97`** — dominant tone inside the green mask (4773 px of
  `#8ddc97` plus 2419 `#8ddb99`, 1433 `#8ddc98`, …). `[MEASURED]`
- **Opaque.** A maze wall occupies x = 299–309 continuously from y = 0 to
  y = 184 in this crop. At y = 75 (inside the bar) the fill reads `#8edb95` at
  every x from 292 to 319 — the wall does **not** show through. `[MEASURED]`
  This distinguishes the input bar (opaque) from the message strips
  (translucent, α ≈ 0.76 — see `F-gameplay-2013-page-round-countdown.png`).
- **Border**: black runs above/below the green at x = 500 are 5 px (top) and
  7 px (bottom); at x = 700, 4 px and 7 px. The extra thickness below is the
  drop shadow merging with the border. `[MEASURED]`
- **Green interior height**: 46 px at x = 300, 50 at x = 500, 52 at x = 700.
  Averaged over the bar, **left end 44.0 px, right end 55.2 px** — the right end
  is **1.25×** taller. `[MEASURED]`
- **Skew**: fitting straight lines to the green mask's top and bottom edges over
  the middle 80% of the bar gives top slope **+0.0112 (+0.64°)**, residual σ
  0.70 px; bottom slope **+0.0261 (+1.49°)**, residual σ 0.42 px. `[MEASURED]`
  The two edges are **not parallel** — the bar is a trapezoid, not a rotated
  rectangle.
- **The skew is real, not a rotated video.** In the same crop the maze wall at
  x = 299–309 sits at exactly the same x at y = 0, 4, 8, …, 184 — **zero drift
  over 184 rows**. Three other walls (378–386, 532–541, 609–618) behave the same
  way. The maze is perfectly axis-aligned; only the chat bar is tilted.
  `[MEASURED]` This is the answer to the task's "verify the skew is real": **it
  is.**
- Cell pitch in this crop: gridlines at 304, 382, 459.5, 536.5, 613.5 →
  **77.6**. Wall band 9–11 px at the `luma<160` threshold. `[MEASURED]`

**Links to the program.** `Chat:` → **0 hits** in `srv/index.php`. See the
`F-chat-message-stack-in-stage.png` section for the full grep and the generation conclusion.

**What this does NOT show.** No HUD, no page, no other player. The bar's
absolute position on the stage is not recoverable from this crop.

---

### `UI/F-chat-bar-crop-2.png` (898×177, captured 17:08:54)  *(was `{6AA2EF0E-D4C6-434A-AD4D-89676F01B1A1}.png`)*

`./UI/F-chat-bar-crop-2.png`

**Filename claim:** none.

**What is drawn.** The same chat bar 8 seconds later in capture order, with more
text typed. Behind it, above the bar, a purple/violet player-name label is
partly occluded by the bar; below the bar, a **purple rotated square with a
yellow-gold circle** — a tank. `[OBSERVED]`

**Transcription (verbatim)**

```
Chat:  im recording
```

Player-name label: `HYPERSTORM…` in purple, cut by the bar's top edge —
`[UNCERTAIN]`, the tail (possibly `S`, possibly digits) is not readable.

**Measurements**

- Fill `#8ddc97` (3181 px) — identical to `F-chat-bar-crop-1.png`. `[MEASURED]`
- Green mask spans x 68–853; green interior height **left 43.4, right 52.6**
  (ratio 1.21). `[MEASURED]`
- Top-edge slope **−0.0147 (−0.84°)**, bottom-edge slope **−0.0003 (−0.02°)`**;
  top-minus-bottom = −0.82°. `[MEASURED]`
- Black border 5–7 px top, 6 px bottom. `[MEASURED]`

**The bar's tilt changes between frames.** Across the three crops the *overall*
tilt is +0.64°, −0.84°, −1.70° — but the *difference* between the top and bottom
edge slopes is −0.85°, −0.82°, −0.85°, i.e. constant. `[MEASURED]`
`[INFERRED]`: the bar is a fixed trapezoid (right end ~22–25% taller) that is
**animated — it rocks slowly about its own axis** while keeping its shape. A
rebuild that draws it statically at one angle will be wrong. Falsifiable by any
sequence of consecutive frames showing a constant angle.

**Links to the program.** As `F-chat-bar-crop-1.png`.

**What this does NOT show.** Nothing of the HUD, page or scoreboard.

---

### `UI/F-chat-bar-crop-3.png` (880×164, captured 17:09:01)  *(was `{CB3725C2-5442-4122-8096-E15264753533}.png`)*

`./UI/F-chat-bar-crop-3.png`

**Filename claim:** none.

**What is drawn.** The same chat bar 7 seconds later again, with the message
extended. Above the bar, a white-filled maze cell (enclosed) and a magenta
fragment of a name label; below, the same purple tank with a gold circle.
`[OBSERVED]`

**Transcription (verbatim)**

```
Chat:  im recording if you dont
```

The message is unfinished — the caret follows `dont` with no closing text.

**Measurements**

- Fill `#8ddc97` (3916 px). Green mask spans x 44–823. `[MEASURED]`
- Green interior height **left 43.2, right 54.4** (ratio 1.26). `[MEASURED]`
- Top-edge slope **−0.0296 (−1.70°)**, bottom **−0.0148 (−0.85°)**.
  `[MEASURED]`
- Black border 6 px top, 6–7 px bottom. `[MEASURED]`

**The three-crop typing sequence.** `F-chat-bar-crop-1.png` (17:08:46) → `F-chat-bar-crop-2.png`
(17:08:54) → `F-chat-bar-crop-3.png` (17:09:01) is one message being typed:
`im rec` → `im recording` → `im recording if you dont`. `[INFERRED]` from the
capture order plus the text being a strict prefix chain. This also confirms the
caret reading in `F-chat-bar-crop-1.png`.

**Links to the program.** As `F-chat-bar-crop-1.png`.

**What this does NOT show.** What happens on Enter — no frame in my set shows a
message being committed, so I cannot say whether the bar clears, closes, or
animates. That is a want.

---

## Consequences for the rebuild

### Confirmed

- **The floor/non-floor cell model.** In-game, cells that are part of the maze
  get a floor tone and cells enclosed on all four sides get the stage's
  `#ffffff` (`srv/index.php:404` sets `bgcolor #ffffff`). That is the same model
  `src/mazecreator/MazeData.as` encodes. `[MEASURED]`
- **Square cells, uniform pitch, walls centred on gridlines.** Every frame's
  lattice fits with residuals ≤ 2 capture px, in both axes, in seven independent
  mazes. `[MEASURED]`
- **The `version N.N` watermark convention.** The game stage carries
  `version  4.0` bottom-right, letter-spaced, in a very light grey (darkest
  pixel luminance 194), right-aligned, exactly the treatment
  `docs/standards/MAZECREATOR-VISUAL-SPEC.md` records for the editor's `version 0.3`
  (`≈#bbbbbb`, wide letter-spacing, right-aligned, flush corner). The editor
  spec's watermark styling is now corroborated by a **sibling SWF**, not just by
  one screenshot. `[MEASURED]`
- **Wall thickness is roughly an eighth of a cell.** Five independent frames
  give 0.099, 0.100, 0.106, 0.118, 0.121 (mean 0.109) against the editor's
  pinned 4/32 = 0.125. The editor constant is at the top of the observed range
  but not out of family. `[MEASURED]`
- **S105 — frozen live regions.** The 2015 Visits box in `F-gameplay-2015-page-beta-sidebar.png` uses the
  identical label set, order and `Since 2007-12-16` anchor as the held 2018
  bytes at `srv/index.php:1067-1069`. Format stability across three years is now
  observed, not assumed. `[MEASURED]`
- **The game SWF served by the rebuild is the one in this footage.** The
  `version 4.0` watermark plus `LEDGER.tsv` row 163 plus
  `srv/index.php:404` close that loop. `[INFERRED]`

### Contradicted — overhaul owed

Nothing in `srv/` is contradicted, because **nothing in `srv/` renders the game
stage** — the game is a held-`O` SWF and the HUD/chat/maze pixels are its
output, not the rebuild's. There is no M2/M3 invention here to supersede. The
overhaul rule does not fire.

Two *documentation* corrections are owed, though, and they are real:

1. **`docs/standards/MAZECREATOR-VISUAL-SPEC.md` presents its constants without saying
   which renderer they describe.** They describe `mazeCreator_v0.3.swf`. The
   game SWF's equivalents are measurably different — floor `#e5e5e5` flat vs
   `#dddddd`/`#eeeeee` mixed; wall `#4c4c4c` vs `#444444`; wall/cell 0.10–0.12
   vs 0.125; crate marker amber-with-glow vs live crate grey-no-glow; cell size
   fixed at 32 vs scaled-to-fit. Anyone reading the spec today could reasonably
   assume it describes "the TankTrouble maze look". It does not.
2. **`VISUAL-EVIDENCE-WANTED.md` entry 8a is written as though the floor tone
   pattern is a property of the game.** It is a property of the **editor**. My
   evidence shows the classic game has no such pattern at all, and the
   post-classic HTML5 client has a *different* one. 8a's "two different frames
   of the SAME maze would settle it" test is still exactly right — but it has to
   be two frames of the same maze **in the editor**, and no amount of gameplay
   footage will help.

### Still unknown / stays on the want-list

- **VE 8a — editor floor tone pattern.** Stays **WANTED**, unchanged, with the
  scope correction above. My frames add one useful sidelight: the HTML5 client's
  in-game floor *is* a per-cell two-tone mix with no parity rule (σ 7.44 over 77
  cells, ≈1:1 light:dark), so "per-cell mix, no deterministic rule visible" is a
  recurring house pattern across TankTrouble renderers — which makes the
  editor's fixed-hash stand-in a defensible choice, but does not derive it.
- **S102 — era game-SWF audio set.** `[NOT VISIBLE]`. A still cannot carry
  audio. Stays **WANTED**. Worth recording explicitly: **sessions A, B, E, F and
  G are all screen recordings** (session F carries a Screencast-O-Matic
  watermark, which only appears on recorded video), so the **source videos
  almost certainly have the game audio track on them**. Recovering the videos
  behind these crops is therefore the single cheapest route to S102, and to S41
  (editor sound effects) if any of the same uploaders recorded the garage.
- **S13 — game stage slide-up transition.** `[NOT VISIBLE]`; every frame is
  mid-round, none is pre-start.
- **S14 — scrapyard counter in motion.** `F-html5-generation-contrast-case.png` shows one (value
  `2453183314`) but in the post-classic generation. Stays **WANTED** for the
  classic widget.
- **S19, S23, S5, S3, S4, S6, S7, S8, S9** — `[NOT VISIBLE]` in every frame.
- **The absolute stage scale** of any of these captures. Stays open; a frame
  showing the game running on the *2017-2018* page would fix it via the layout
  arithmetic at `srv/index.php:308-311, 324, 452-453, 466`.
- **What the `+` and `○` marks on the floor in `F-gameplay-three-guests-maze-crop.png` are.**

### New wants to add

These are the entries I would add. None of them currently exists in
`docs/standards/VISUAL-EVIDENCE-WANTED.md` — I checked entries 1–10 and S1–S114.

**N1. In-game chat system (major, previously unrecorded).** `WANTED`.
The classic game stage carries a chat: an opaque green input bar
(`#8ddc97`, heavy black border, trapezoid, animated tilt) labelled `Chat:` with
a text caret, and a stack of up to 5 translucent green message strips
(fill-over-floor `#95cc9b`, α ≈ 0.76, 34 px tall at 50 px pitch) in the format
`<name> says '<text>'`, newest fading in at the top. `srv/index.php` has zero
chat markup. What is still needed: how it opens (a key? Enter?), what happens on
send, the message lifetime, the max stack depth, whether messages are local-only
or networked, and the exact fonts. **First action is not footage at all**: scan
the held `srv/includes/TankTrouble_v4.0.swf` for the literals `Chat:` and
`says '`. If they are there, the feature is in-era and in-hand.

**N2. In-game maze render constants.** `PARTIAL` (this document).
Floor `#e5e5e5` flat, enclosed cells `#ffffff`, wall `#4c4c4c` at 0.10–0.12
cell, boundary ≈1.2× interior. Needed to upgrade: a native-resolution capture
(these are all video re-scales), and the actual stage-pixel values, which come
free from a Ruffle/projector render of the held SWF.

**N3. Maze-to-stage fit rule.** `PARTIAL`.
Cell size is not constant: measured 112.1 (6×3) and 56.4 (4×8) capture px in one
session. Viewport ≈672×451 capture px, aspect 1.49. Needed: the exact viewport
rectangle in stage px, and whether the maze is centred in it. Bears on VE **6**
(maze placement) — the *editor* snaps to a fixed lattice, the *game* does not,
so entry 6's question is editor-only.

**N4. HUD / scoreboard strip.** `WANTED`.
Layout differs by generation and by login state — see the table below. Needed:
the strip's stage-px geometry, the entry pitch rule, what happens at 1 and at
the maximum player count, and the exact fonts/tones.

| | 2013 (`F-gameplay-2013-page-four-tanks.png`, `F-chat-message-stack-in-stage.png`) | 2015 (`F-gameplay-three-guests-maze-crop.png`, `F-gameplay-maze-61-crates.png`) |
|---|---|---|
| far-left icons | **door** over speaker | **gear** over speaker (or speaker alone) |
| entry | tank ▸ score ▸ **username below** | tank ▸ score, **no username** (guests) |
| outermost-right entry | not mirrored | **mirrored**, score on the barrel side |
| thumbnails | accessorised, per-account paint | plain red / green / blue |

**N5. Maze name + author caption.** `WANTED`.
`hvere are you` / `by bulla` right-aligned above the version watermark. This is
a user-generated maze being played, captioned with its title and its author's
username. It ties the mazeCreator directly to gameplay and it is the only
evidence I have seen that a saved maze's *name* is surfaced anywhere. Bears on
**S38** (`userSettingsMazeCreatorInitCode-` fields) and **S43** (multiple maze
slots): a name and an author are carried through to the game, so the wire format
must include both. Needed: how a maze is selected for play, and whether the
caption appears for every round or only for community mazes.

**N6. In-maze player name labels.** `WANTED`.
Names float beside each tank in the player's own colour (`revengexx1` dark red,
`Blaze4330` blue-violet, `rushabh4084` red, `HYPERSTORM…` purple). Note
`srv/index.php:7292` announces "Tank names appear at battle start so you know
who's who" as an **Online BETA** feature — but the classic v4.0 build already
had them, so that news item is about the HTML5 client, not about this. Needed:
whether the label is permanent or only shown at round start, its font, and its
outline treatment.

**N7. Round-countdown card.** `WANTED`.
`F-gameplay-2013-page-round-countdown.png` shows a large white card with a black `3`, drawn tilted, with a
heavy outline and drop shadow, centred over the maze. Needed: the full 3-2-1
sequence, the animation, and whether `GO`/`FIGHT` follows.

**N8. Weapon crate as rendered in play.** `FETCHED` — evidence in hand *and*
bytes in hand.
Grey rounded square, random rotation, dark `?`-like glyph, side ≈0.47 cell, no
glow. `srv/Assets/Crate.swf` is held `O` (`LEDGER.tsv` row 2), so this frame's
value is as a **gate-C oracle**: a Ruffle render of `Crate.swf` that does not
look like `F-gameplay-maze-61-crates.png`'s crates is wrong.

**N9. In-game tank sizing.** `PARTIAL` (this document).
0.41–0.45 cell by √area, 0.52–0.61 by bbox, scales with the maze. Thumbnail
palette: `#990000`/`#4d0000`, `#009900`/`#004e00`, `#000099`/`#00004e`.
`srv/Assets/Tank.swf` and `srv/Assets/GameTank.swf` are held `O` (rows 5, 3) —
same oracle argument as N8.

**N10. The `+` and `○` floor marks.** `WANTED`.
Two dark-grey glyphs drawn flat on the floor in `F-gameplay-three-guests-maze-crop.png`, matching no
object I can identify. Any consecutive-frame sequence would resolve them.

**N11. 2015 sidebar promo boxes.** `WANTED` (dating aid, not era art).
`Access` / `Online BETA` / `Beta access required` on a sunburst-tank background
(a `.box` background-image variant — the family **S16** flags), and a
green-header (`#2bdd72`) `Shop Open` / `Get BETA access here!` box. Zero hits in
`srv/index.php`. Useful for dating other frames and for S16/S106.

**N12. Post-classic sidebar copy (negative control).** `WANTED`.
`Battle mode: / Classic / Never-ending destruction!`, `Tank Rank has been
Deployed`, `WALLoFAME / COMMEMORATING / BACKERS AND FRIENDS`, `Message the
laboratory / Got ideas, found a bug, need help or just love trouble? Let the
scientists know!`. All absent from held bytes. Recording them lets future
analysts *reject* HTML5-era frames quickly instead of re-deriving it.

---

## Recommended edits to existing docs (not applied)

**1. `docs/standards/MAZECREATOR-VISUAL-SPEC.md` — add a scope line at the top.**

> Add after the "Source:" line:
> `**Scope: these constants describe mazeCreator_v0.3.swf only.** The game SWF
> (TankTrouble_v4.0.swf) renders the same maze data with different constants —
> flat #e5e5e5 floor (no two-tone mix), #4c4c4c walls, wall/cell ≈ 0.10-0.12,
> and a cell size scaled to fit the stage rather than fixed at 32 px. Measured
> in manualevidence/F-gameplay-hud-and-chat.md.`

**2. `docs/standards/MAZECREATOR-VISUAL-SPEC.md` — annotate the "Crate spawn icon" row.**

> Append to the Evidence cell:
> `The live weapon crate in play is a DIFFERENT object: grey, randomly rotated,
> no glow, side ≈0.47 cell (measured, 61 crates, manualevidence/
> F-gameplay-hud-and-chat.md). The amber+glow marker is editor-only — do not
> "correct" it toward the crate art.`

**3. `docs/standards/VISUAL-EVIDENCE-WANTED.md` entry 8a — narrow the scope, keep the
status.**

> Change the opening of 8a from `Editor floor is a per-cell mix of
> #dddddd/#eeeeee…` to `**Editor-only.** The game SWF's in-play floor is a
> single flat tone (#e5e5e5; 98 cells σ 0.10 and 192 cells σ 0.72 measured), so
> no amount of gameplay footage bears on this. Editor floor is a per-cell mix
> of #dddddd/#eeeeee…`
> and append to the "Any footage showing one maze twice" line:
> `— it must be the EDITOR showing one maze twice, not the game.`
> **Status stays `WANTED`.**

**4. `docs/standards/VISUAL-EVIDENCE-WANTED.md` S105 — `HIGH`/open → `PARTIAL`.**

> Reason: the 2015 Visits box (`Game/F-gameplay-2015-page-beta-sidebar.png`) uses the identical label set,
> order and `Since 2007-12-16` anchor as `srv/index.php:1067-1069`, with 2015
> values (42 315 370 visits; Today 21 657; Online 833; Tank owners 1 534 911;
> Logged in 245). Format stability 2015→2018 is observed. Remaining unknown:
> the Top-10 and forum-latest-posters regions.

**5. `docs/standards/VISUAL-EVIDENCE-WANTED.md` S110 — add the fingerprint method.**

> Append to the "What exists / what's missing" cell:
> `Fingerprint: the classic game stage draws a right-aligned, wide-letter-spaced
> "version N.N" watermark in ≈#bbbbbb at the bottom-right of the 712x490 stage.
> Reading it off a frame identifies the build directly, without inferring from
> UI. Confirmed on v4.0 in four frames (manualevidence/
> F-gameplay-hud-and-chat.md).`

**6. `docs/standards/VISUAL-EVIDENCE-WANTED.md` S113 — open → `PARTIAL`.**

> Reason: `UI/F-gameplay-2013-page-four-tanks.png` and `UI/F-chat-message-stack-in-stage.png` are logged-in renderings of the
> **game** tab — four and three named accounts with per-account painted tanks
> and accessories in the HUD, usernames under each thumbnail. 2013 generation,
> so it does not settle the era look, but the boundary is no longer absolute.
> The garage, news, shop, forum and lab tabs remain unseen logged-in.

**7. `docs/standards/VISUAL-EVIDENCE-WANTED.md` S102 — keep `WANTED`, add the lead.**

> Append to the FOOTAGE TRIGGER cell:
> `The frames in manualevidence/F-gameplay-hud-and-chat.md are crops from
> screen recordings (one carries a Screencast-O-Matic watermark), so the source
> videos carry the game audio. Recovering those videos is the cheapest route to
> S102 — and to S41 if the same uploaders recorded the garage.`

**8. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — add a new section for the game stage.**

> The twelve entries N1–N12 above. N1 (the chat system) is the most valuable:
> it is a whole user-facing feature the project has never recorded, and unlike
> most wants it has a **zero-cost first step** — a string scan of a file the
> repo already holds.

**9. `DEDUCE.md` — record two new dating handles.**

> (a) The footer credits line `Design: Mads Purup, Programming: Brian Bunch
> Christensen, Server: Søren Boll Overgaard` is present under the copyright in
> 2013 (`UI/F-gameplay-2013-page-round-countdown.png`, `UI/F-gameplay-2013-page-four-tanks.png`) and **absent** from the era bytes
> (`Mads Purup`, `Brian Bunch`, `Overgaard` → 0 hits in `srv/index.php`). It was
> dropped somewhere between 2013 and 2018 — a second footer datum alongside the
> copyright year.
> (b) The nav strip had a **four-tab** generation in 2013 (`NEWS` placard,
> wrench, speech bubble, flask, with the wordmark acting as the game tab)
> against the era six-tab strip at `srv/index.php:302`.

**10. `DECISIONS.md` — log the generation split, so it is not re-litigated.**

> Suggested entry: *"manualevidence gameplay frames: page chrome is 2013/2015
> (footer years 2007–2013 / 2007–2015; credits line present; 4-tab nav; Access
> Online BETA sidebar) and one post-classic HTML5 frame. The **game** in the
> 2013/2015 frames is `version 4.0` = `TankTrouble_v4.0.swf`, held O
> (LEDGER row 163) and embedded by the era page at `srv/index.php:404`.
> Therefore in-stage measurements from those frames are admissible as era
> evidence; page-chrome measurements from them are not. The `F-html5-generation-contrast-case.png` frame
> is post-classic throughout and is admissible for neither."*

---

### One-line summary of what this topic proved

The classic game's maze — the one `TankTrouble_v4.0.swf` actually draws in a
live round — has a **single flat `#e5e5e5` floor** (98 cells at σ 0.10, 192
cells at σ 0.72), **not** the two-tone per-cell mix the editor uses; and the
same stage carries a **complete chat system that appears in no held byte, no
ledger row and no want-list entry**, whose first recovery step costs nothing
because the SWF that contains it is already in the repo.
