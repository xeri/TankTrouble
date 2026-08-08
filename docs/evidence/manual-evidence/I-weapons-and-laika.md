# Visual evidence — weapon icons, weapon roster, Laika and the TankTrouble typeface

> Analysis of all 11 assigned evidence files under `manualevidence/` — 10 images/text plus `TankTrouble.ttf`, inspected with `fontTools`.
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)
>
> Sibling document for in-play rendering: [F — gameplay HUD and chat](./F-gameplay-hud-and-chat.md).
> Sibling document for editor typography: [A — maze editor toolbar](./A-maze-editor-toolbar.md).

---

## Scope and provenance

Eleven files were assigned and all eleven were analysed.
`manualevidence/TankTrouble.ttf` was staged late (a staging fault, not a real
absence) and has been inspected byte-for-byte with `fontTools 4.62.1` — see
[§ `TankTrouble.ttf`](#tanktroublettf-114-092-bytes-captured-163538). Every
number in that section was re-derived here rather than taken on report.

### Capture order (the only thing the timestamps are good for)

Per the brief §"Consequences" 2, mtimes are when the repo owner saved the crop on
2026-08-04, not when the source was made. **The staged mtimes in this container are
not even that** — `[MEASURED]` the nine `.webp` files carry container mtimes
`05:53:10`–`05:53:15` in strict *alphabetical* order (`Booby_trap`, `Death_ray`,
`Frag_Bomb`, `Gatling_gun`, `Laika`, `Laser`, `Rocket`, `Weapons`, then
`RC_rocket` last because it lives in a different directory). That is the staging
copy order, not the owner's save order. The times in my assignment brief
(16:29:29 … 16:35:38) are the owner-side ones and are the only usable sequence.

Taken as a sequence they read as one continuous ~6-minute pass over a **community
wiki's weapon material**:

| # | Time | File | Reading of the step |
|---|---|---|---|
| 1 | 16:29:29 | `Game/I-weapon-toggle-panel.webp` | the settings/toggle panel — grabbed first, before the icons |
| 2 | 16:29:47 | `Game/I-laika-boss-artwork.webp` | the boss illustration |
| 3 | 16:29:56 | `Game/I-icon-gatling-gun.webp` | then the icons, one per ~5 s… |
| 4 | 16:30:01 | `Game/I-icon-booby-trap.webp` | |
| 5 | 16:30:07 | `Game/I-icon-laser.webp` | |
| 6 | 16:30:16 | `Game/I-icon-death-ray.webp` | |
| 7 | 16:30:21 | `Game/I-icon-rc-rocket.webp` | **saved to the wrong directory** — see gate-D note below |
| 8 | 16:30:25 | `Game/I-icon-rocket-homing-missile.webp` | |
| 9 | 16:30:30 | `Game/I-icon-frag-bomb.webp` | last icon — 61 s for seven icons |
| 10 | 16:31:46 | `Game/weapons.txt` | the wiki *article* the icons come from, saved ~1 min later |
| 11 | 16:35:38 | `TankTrouble.ttf` | 4 minutes later, a different hunt entirely |

`[INFERRED]` Items 3–9 are the seven infobox images of the article saved at item 10:
they are byte-for-byte uniform in canvas size, background tone and internal
geometry (measured below), they are saved 4–9 s apart with no gaps, and their
filenames are exactly the caption strings that appear under each heading in
`weapons.txt`. Falsifier: a different source with the same seven filenames and the
same 90×84 canvas.

`[INFERRED]` Item 11 is a separate errand — the 4-minute gap and the change of
file type break the run. It is not evidence *about* the weapons; it was assigned to
this topic because it is the only typography artefact in the corpus. `[MEASURED]`
Its bytes bear that out: nothing in the font references weapons, Laika or a wiki,
and its own internal dates (2013 / 2016 / 2017) sit outside any sequence the other
ten files describe. `[UNCERTAIN]` Whether the owner reached it *from* the wiki or
from somewhere else entirely cannot be told from the file — only from his browser
history, which is why the download URL keeps recurring below as the missing datum.

### Misfiling — `I-icon-rc-rocket.webp` (raised as instructed)

`[MEASURED]` `I-icon-rc-rocket.webp` sits at the **repository root**,
`websites/Game/I-icon-rc-rocket.webp`, not in `manualevidence/Game/` with its six
siblings. It is byte-compatible with them in every measured respect (90×84 WebP,
`#e6e6e6` matte, exact 2× pixel doubling, 43-px plate) — there is no doubt it
belongs with them.

`[MEASURED]` `grep -n -i "RC_rocket" LEDGER.tsv` → **no match, exit 1**. There is
no ledger row for it. There is also no row for any `.webp` file at all.

`[OBSERVED]` — and this is the part worth flagging harder than the misfiling —
**gate D as documented would not catch this.** `README.md` describes gate D
(`tests/test_no_unlabelled.py`) as *"every `srv/` file has a ledger row"*, and
`docs/standards/ASSET-DISCIPLINE.md:21` states the gate-D question verbatim as *"does every
file under `srv/` have a row?"*. `I-icon-rc-rocket.webp` is not under `srv/` — it is a
sibling of `README.md`. So the file is simultaneously (a) unledgered, (b) a binary,
(c) of foreign provenance (wiki-derived, M2 at best), and (d) **outside the walk of
the gate that exists to find exactly this**. Two separate corrections are owed:
move the file, *and* widen gate D's walk to the repo root. See
[§ Recommended edits](#recommended-edits-to-existing-docs-not-applied).

### What generation is this?

Sibling [F](./F-gameplay-hud-and-chat.md) established that at least part of this
corpus post-dates the 2017–2018 target (a complete chat system present in frames
and in no held byte). I kept that live throughout. My topic splits three ways:

* the **seven icons** and **`weapons.txt`** are wiki-derived and internally dated
  (the article says "as of 28th February 2013") — pre-target, and about the
  classic Flash game;
* **`I-weapon-toggle-panel.webp`** is the one genuinely contested item — held bytes prove a
  per-weapon settings menu existed in the classic game from **2008-12-16**, but the
  panel's *rendering* does not match classic page chrome. Verdict and reasoning in
  its section;
* **`TankTrouble.ttf`** splits the difference and is the most interesting item in
  the assignment. Its name table is **first-party Purup material** — designer
  `Mads Purup`, designerURL `www.purup.com`, the same person and domain the
  classic footer credits — so it is *authenticated*, not fan-made. But it is
  **not evidenced as a classic-era served asset**: no ledger row, no `@font-face`,
  and the only developer statement about a "custom TankTrouble font" puts it in
  **Online BETA** (2016-05-25). Its own `head.created` 2013 / `head.modified`
  2017-11-02 / copyright 2016 pull in *different directions*, and I do not resolve
  that tension below — I record it.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| I-1 | `TankTrouble.ttf` is **first-party Purup material** — name table designer `Mads Purup`, designerURL `www.purup.com`, matching the classic footer credits — but `srv/index.php:6657` (news 25-05-2016) attributes "a custom TankTrouble font" to **Online BETA**, and no held byte references it. **Authenticated, not evidenced as classic-era-served** | `[MEASURED]` | VE 7, S17, S108 | Blocks a wrong adoption; nothing to rewrite |
| I-2 | `srv/index.php:9969-9977` (news 16-12-2008) proves a **per-weapon enable/disable settings menu**, opened by a **gear during play**, existed in the classic Flash game | `[MEASURED]` | new want; `I-weapon-toggle-panel.webp` | Nothing built — pure addition |
| I-3 | All seven icons are exact **2× nearest-neighbour upscales**: native raster **45×42**, sprite plate **≈22×22 native px** | `[MEASURED]` | S102-adjacent; `Assets/Crate.swf` (LEDGER 2, O) | — |
| I-4 | All seven icons are **strictly neutral grey**: R==G==B for **7560/7560 px, 100.0000%**, in every one of the seven files | `[MEASURED]` | asset palette | — |
| I-5 | Every icon is the **same square plate at a different rotation**: side 43.0–44.2 capture px, area 1788–1860 ink px, angles 0.00° / 10.50° / 10.50° / 11.25° / 39.75° / 67.25° / 73.00° | `[MEASURED]` | S102-adjacent; crate render | — |
| I-6 | Icon matte is **`#e6e6e6`**, glyph floor **`#333333`**, plate greys span 51–230; **no alpha channel at all** (mode `RGB`) | `[MEASURED]` | asset palette | — |
| I-7 | Icon count is **7**, and the roster gap is **Shotgun only**. Homing Missile *does* have an icon — it is the file named `I-icon-rocket-homing-missile.webp` | `[MEASURED]` | roster completeness | Corrects the task's hypothesis |
| I-8 | `I-weapon-toggle-panel.webp` transcribes to 7 labels in 2 columns, column-major, pill toggles: knob `#cccccc`, track `#00ff00`-class, page `#ffffff` | `[MEASURED]` | new want | — |
| I-9 | The `I-weapon-toggle-panel.webp` title face has a **wider `W` and smaller x-height than Arial, Helvetica, Verdana and Calibri** at matched 19 px cap height — it is not stock classic page chrome | `[MEASURED]` numbers, `[UNCERTAIN]` identification | VE 7, S108, generation | — |
| I-10 | `weapons.txt` carries **wiki chrome and one clear vandalism insertion** ("gang gang scince potty train") at the head of the Death Ray body | `[OBSERVED]` | text hygiene | Quarantines a bad source |
| I-11 | `weapons.txt` dates the Laser-vs-Laika exclusivity claim to **28 Feb 2013** and marks **Shotgun as Beta-only** | `[OBSERVED]` | S103; generation | — |
| I-12 | `I-laika-boss-artwork.webp` artwork bbox is **325×416, aspect 0.781**; the `laika02.swf` embed is **140×250, aspect 0.560**. They do **not** match | `[MEASURED]` | S103 | Does **not** verify S103 |
| I-13 | The project already holds **`srv/Assets/Laika.swf` as `O`** (LEDGER 4) — a second, unremarked Laika asset that S103 does not mention | `[MEASURED]` | S103 | S103 is under-scoped |
| I-14 | LEDGER 324 already records a **`wiki-dumps/tt-game-wiki/images/LaikaSmall.jpg`** in the archive, "unproven — adjudicate by eye". That is very likely the same wiki this corpus came from | `[MEASURED]` | S103, S77 | Gives a concrete next step |
| I-15 | `TankTrouble.ttf` is a **heavy irregular display sans**, 211 glyphs, upem 1000, `fsType=0`, hinted; x/cap **0.7848**. Renders `Weapons` **17 % wider** than the captured panel title at matched cap height — so it is a **third** face, matching neither the wiki-corpus face (0.684/0.698) nor the editor title face | `[MEASURED]` | VE 7, S108 | — |
| I-16 | `I-icon-rc-rocket.webp` is unledgered **and outside gate D's documented `srv/` walk** | `[MEASURED]` | gate D | Gate-D scope fix owed |
| I-17 | The font's dates **contradict each other**: `head.created` **2013-09-28**, copyright/uniqueID **2016**, `head.modified` **2017-11-02** — the last falls *inside* the 2017–2018 target window, the first two do not | `[MEASURED]` | S116 (new) | Left unresolved on purpose |
| I-18 | Coverage carries an unusual signature: 95 ASCII + 94 Latin-1 Supplement + arrows U+2190–2193 + **box-drawing U+2500–250F** + **U+2605 BLACK STAR** — a UI-drawing set, not a text set | `[MEASURED]` | S116 (new) | Gives S116 a matchable fingerprint |

---

## File-by-file analysis

### The seven weapon pickup icons — shared properties first

All seven are analysed together where they are identical, then individually.
Files (six in `manualevidence/Game/`, one misfiled at the repo root):

| File | Canvas | Bytes | Capture |
|---|---|---|---|
| `./Game/I-icon-gatling-gun.webp` | 90×84 | 634 | 16:29:56 |
| `./Game/I-icon-booby-trap.webp` | 90×84 | 544 | 16:30:01 |
| `./Game/I-icon-laser.webp` | 90×84 | 620 | 16:30:07 |
| `./Game/I-icon-death-ray.webp` | 90×84 | 458 | 16:30:16 |
| `../../I-icon-rc-rocket.webp` **(misfiled — repo root)** | 90×84 | 658 | 16:30:21 |
| `./Game/I-icon-rocket-homing-missile.webp` | 90×84 | 672 | 16:30:25 |
| `./Game/I-icon-frag-bomb.webp` | 90×84 | 670 | 16:30:30 |

**Count confirmed: seven.** `[MEASURED]` Six under `Game/`, one at the repo root.

#### Container and transparency

`[MEASURED]` All seven decode as WebP, PIL mode **`RGB`** — there is **no alpha
channel at all**. Converting to RGBA and inspecting the alpha plane gives
`min=255, max=255, unique=[255]` for every file. So:

* there is **no transparency**;
* the background is a **flat opaque matte**, not a checkerboard, not a gradient;
* `[MEASURED]` the matte is exactly **`#e6e6e6`** (230,230,230) at all four corners
  of all seven files, and occupies 75.19 %–76.14 % of each canvas.

`[INFERRED]` The matte was baked in by whatever produced these files (a wiki
thumbnailer flattening a transparent PNG onto a page-background colour is the
usual cause). Falsifier: an original with an alpha channel and the same geometry.
Consequence for the rebuild: **do not treat `#e6e6e6` as an asset colour.** It is
a page background that got welded on. It is also, note, *not* the `#e5e5e5` that
sibling [F](./F-gameplay-hud-and-chat.md) measured for the classic in-round maze
floor — one level apart, and I would not build a bridge between them on one level.

#### Colour — the greyscale test the brief asked for, run rather than eyeballed

`[MEASURED]` For each file I tested `R==G==B` pixel by pixel over the full
90×84 = 7560-pixel canvas:

| File | pixels with R==G==B | % | distinct colours | darkest | lightest |
|---|---|---|---|---|---|
| `Gatling_gun` | 7560 / 7560 | **100.0000 %** | 108 | 51 (`#333333`) | 230 (`#e6e6e6`) |
| `Booby_trap` | 7560 / 7560 | **100.0000 %** | 106 | 51 | 230 |
| `Laser` | 7560 / 7560 | **100.0000 %** | 102 | 51 | 230 |
| `Death_ray` | 7560 / 7560 | **100.0000 %** | 107 | 51 | 230 |
| `RC_rocket` | 7560 / 7560 | **100.0000 %** | 106 | 51 | 230 |
| `Rocket` | 7560 / 7560 | **100.0000 %** | 105 | 51 | 230 |
| `Frag_Bomb` | 7560 / 7560 | **100.0000 %** | 105 | 51 | 230 |

So the answer to "are they *near*-greyscale?" is **no — they are exactly
greyscale**, with zero exceptions across 52 920 pixels. `[INFERRED]` This is
itself a provenance signal: WebP is a lossy format and lossy encoding of a
colour image essentially never returns perfectly neutral pixels (compare
`I-weapon-toggle-panel.webp` below, where only 53.47 % of pixels are neutral). Perfect
neutrality across seven independently encoded files means the encoder was given
**already-greyscale, palette-like input** and encoded it losslessly or
near-losslessly. Falsifier: a lossy-WebP round-trip of a greyscale source that
also comes back perfectly neutral — possible if the encoder used lossless mode,
which is consistent with the tiny file sizes (458–672 bytes).

`[MEASURED]` The darkest value is **exactly 51 (`#333333`)** in all seven, and the
lightest **exactly 230 (`#e6e6e6`)** in all seven. The glyph floor and the matte
are therefore shared constants, not per-file accidents.

#### Native resolution — the strongest single measurement here

`[MEASURED]` For every one of the seven files, `a[0::2] == a[1::2]` and
`a[:,0::2] == a[:,1::2]` are both **exactly true** (array equality, not
approximate). Every row is duplicated and every column is duplicated.

That means each 90×84 file is an **exact 2× nearest-neighbour upscale** of a
**45×42** raster. There is no information in the 90×84 form that is not in the
45×42 form.

`[MEASURED]` Neither `I-weapon-toggle-panel.webp` nor `I-laika-boss-artwork.webp` passes this test
(`Weapons`: 70 mismatching row-pairs, max diff 255; `Laika`: 234 mismatching
row-pairs, max diff 64), so the doubling is specific to the icon set and is not
an artefact of my reading code.

`[INFERRED]` The native sprite raster is 45×42 and something in the chain
(MediaWiki thumbnailing to a 90 px target, or the owner's crop tool) doubled it.
**Work from the 45×42 form.** Falsifier: an upstream copy at a different size
that also downsamples cleanly to 45×42.

`[UNCERTAIN]` Whether 45×42 is the *game's* native sprite size or just the wiki's
stored file size cannot be settled from these files. What argues for near-native:
the plate edges are 2-step ramps (`230 → 174 → 112`), the glyph edges are hard
`51`-to-mid-grey transitions, and the matte is a single exact value with no halo —
all signs of little or no downscaling. What would settle it: rendering
`srv/Assets/Crate.swf` (held **O**, LEDGER row 2) and measuring its stage size.

#### Geometry — every icon is the same plate at a different rotation

`[MEASURED]` Fitting a minimum-area rectangle to the non-matte mask of each icon
(rotating in 0.25° steps and minimising bounding-box area) gives:

| File | fitted angle | fitted side (capture px) | ink px | ink / fitted-rect area | axis-aligned bbox (capture px) |
|---|---|---|---|---|---|
| `Death_ray` | **0.00°** | 43.0 × 43.0 | 1860 | 1.006 | 44 × 44 |
| `Gatling_gun` | **10.50°** | 43.8 × 43.8 | 1824 | 0.950 | 50 × 48 |
| `Booby_trap` | **10.50°** | 43.8 × 43.8 | 1824 | 0.950 | 50 × 48 |
| `Laser` | **11.25°** | 43.2 × 43.2 | 1788 | 0.959 | 50 × 48 |
| `Frag_Bomb` | **39.75°** | 43.9 × 43.9 | 1824 | 0.944 | 58 × 58 |
| `Rocket` | **67.25°** | 44.0 × 44.1 | 1828 | 0.943 | 54 × 54 |
| `RC_rocket` | **73.00°** | 44.1 × 44.2 | 1836 | 0.943 | 52 × 52 |

Read this carefully, because it is the whole point:

* `[MEASURED]` The **fitted side length is 43.0–44.2 capture px in all seven** — a
  spread of 2.8 %. The **ink area is 1788–1860 px** — a spread of 4 %.
* `[MEASURED]` The **axis-aligned bounding box varies from 44×44 to 58×58** — a
  spread of 32 %.
* `[INFERRED]` Constant area + constant fitted side + wildly varying bounding box
  is the signature of **one square sprite drawn at seven different rotations**. It
  is not seven differently shaped drawings. Falsifier: any icon whose fitted rect
  is not square or whose side departs from ~43 px.
* Because a square is 90°-symmetric the fitted angle is only defined mod 90°.
  Equivalent small-angle readings: `Death_ray` 0°, `Gatling_gun`/`Booby_trap`
  +10.5°, `Laser` +11.25°, `Frag_Bomb` +39.75° (≈ −50.25°), `Rocket` +67.25°
  (≡ −22.75°), `RC_rocket` +73.00° (≡ −17.00°). Which representative is "the"
  rotation cannot be decided without knowing which plate edge is the sprite's
  "top" — and for a bevelled plate lit from one side, the bevel decides it (see
  below), so the small-angle reading is the defensible one.
* `[MEASURED]` In native (45×42) coordinates the plate spans **22×22 px** for the
  unrotated `Death_ray` (x 11..32, y 11..32). `[INFERRED]` the sprite is a
  **22×22 native-px square**.

`[INFERRED]` This is a **weapon crate**, seen face-on, drawn once and stamped at a
random rotation per pickup. That is exactly how the classic game's powerup crates
behave on the maze floor, and the project already holds the asset:
**`srv/Assets/Crate.swf`, tier `O`, LEDGER row 2**
(`sha256 19c320ea8e28095699c5b32bf70cf8a2f5d343f8e892f2fe909f7d049b035f36`).
The rotation set here (0°, 10.5°, 10.5°, 11.25°, 39.75°, 67.25°, 73.00°) is
`[INFERRED]` **not a designed constant** — it is whatever angle the wiki
contributor's screenshot happened to catch, and two icons sharing 10.50° is
consistent with chance over seven draws. Do **not** pin these angles as
constants. What they *do* establish, defensibly, is that **the crate is rendered
rotated at all**, which is a behavioural fact the rebuild can act on.

Note the contrast with `docs/standards/MAZECREATOR-VISUAL-SPEC.md`, which pins the **editor's**
crate-spawn marker as an *"axis-aligned amber square ≈16×16 with darker border +
soft yellow glow; core ≈ (219,183,85)"*. That is a different object — an editor
placement marker — and nothing here challenges it. The in-play crate measured
here is 22×22 native px, grey, glyph-bearing and rotated. Both can be true; the
spec's "(if any)" hedge under *Known unknowns → icon rotation* is about the
editor icons, and this evidence does not resolve it.

#### Shared presentation — bevel, inner frame, shading

`[OBSERVED]` Every one of the seven shares the identical construction, and I can
point at each element in the upscaled renders:

1. an outer **1-native-px dark rim** around the square;
2. a **raised outer border** ~2 native px wide;
3. an **engraved inner rectangle outline** inset from the border, visible as a
   thin darker line following the plate edge;
4. a **flat inner field** carrying the glyph;
5. the **glyph** itself in near-black.

`[MEASURED]` The plate is **shaded from the upper-left**. Mean grey inside the
plate mask, split top/bottom and left/right of the plate bbox centre:

| File | top | bottom | left | right |
|---|---|---|---|---|
| `Gatling_gun` | 132.2 | 116.8 | 130.5 | 118.3 |
| `Booby_trap` | 118.5 | 111.2 | 119.6 | 109.9 |
| `Laser` | 133.7 | 116.8 | 131.6 | 118.9 |
| `Death_ray` | 123.0 | 105.8 | 123.3 | 106.3 |
| `RC_rocket` | 124.9 | 119.3 | 130.6 | 113.8 |
| `Rocket` | 131.0 | 116.0 | 131.5 | 114.9 |
| `Frag_Bomb` | 129.5 | 110.3 | 120.4 | 119.6 |

Top is brighter than bottom in **7/7**; left is brighter than right in **6/7**
(`Frag_Bomb` is 120.4 vs 119.6, effectively flat — and it is the icon rotated
closest to 45°, where a left/right split of the bbox no longer aligns with the
sprite's own axes). `[INFERRED]` The plate is lit from the **upper-left in
screen space, not in sprite space** — i.e. the shading survives the rotation with
the same on-screen direction. Falsifier: a capture of the same crate at another
angle showing the highlight rotate with the sprite. This is a real, testable
behavioural claim and worth putting on the want-list.

`[MEASURED]` Native-resolution cut through `Death_ray` at native row y=12
(the top of the plate):
`230 230 … 230 | 174 112 121 121 120 119 118 126 132 131 129 128 126 124 130 131 129 126 124 122 106 | 198 230 …`
— i.e. matte, then a 1-px `174` ramp, a `112` dark rim, a ~20-px field in the
118–132 band, a `106` rim, a `198` trailing ramp, matte. At native row y=31 the
same field reads ~99–102. That 30-level top-to-bottom fall is the shading.

`[MEASURED]` **Drop shadow: essentially absent.** Thresholding at
`|grey − 230| > 2` instead of `> 8` adds only 16–52 extra pixels per file
(`Death_ray` +4, `Laser` +16, `Gatling_gun`/`Booby_trap` +24, `Rocket` +24,
`RC_rocket` +36, `Frag_Bomb` +52). Those pixels are the 1-px `198`/`214` ramp
immediately adjacent to the plate edge, not an offset silhouette. `[OBSERVED]`
The "second square behind" that reads as a shadow in a casual look at the
upscaled renders is the plate's own **dark bottom-right bevel**, not a cast
shadow — the bevel is inside the fitted rectangle, the ramp outside it is one
pixel wide and symmetric. So: **bevel yes, drop shadow no, and all seven share
it.**

#### Glyph-by-glyph

`[MEASURED]` Glyph extraction = native pixels at grey ≤ 60 (the glyph floor is
exactly 51 in every file, the plate field never goes below ~90):

| File | glyph px (native) | glyph bbox (native) |
|---|---|---|
| `Gatling_gun` | 27 | x 16..27, y 14..24 |
| `Booby_trap` | 86 | x 17..28, y 14..25 |
| `Laser` | 26 | x 18..24, y 16..27 |
| `Death_ray` | 69 | x 16..27, y 16..27 |
| `RC_rocket` | 35 | x 17..28, y 15..24 |
| `Rocket` | 41 | x 21..29, y 15..26 |
| `Frag_Bomb` | 46 | x 18..28, y 17..26 |

`[MEASURED]` Every glyph fits inside a ~12×12 native-px area, centred in the
22×22 plate. `[INFERRED]` the design grid is a 22 px plate with a ~12 px glyph
field and a ~5 px border on each side.

**`Gatling_gun`** — `[OBSERVED]` **six separate round dots** arranged in a ring
(two upper, two middle-outer, two lower), no connecting strokes, each dot ~2–3
native px across. `[INFERRED]` the muzzle end of a rotating barrel cluster seen
end-on. Smallest glyph-pixel count of the set (27) because it is all holes and no
mass. Plate rotated +10.5°.

**`Booby_trap`** — `[OBSERVED]` a **single solid blob**, widest across the top
with a shallow concave notch in the top edge, tapering downward to a narrower
rounded base — a bell/mine silhouette. `[MEASURED]` the heaviest glyph in the set
(86 px, and `#333333` occupies 4.29 % of the whole canvas vs 0.95 % for `Laser`).
`[UNCERTAIN]` whether this is meant as a land-mine, a satchel charge or a
proximity mine — the silhouette is too coarse at 12 px to distinguish, and
`weapons.txt` only says "land-mine". Plate rotated +10.5° — **the same angle as
`Gatling_gun` to the quarter-degree**, which is the one detail that makes me
suspect these two were captured from the same screenshot or the same crate frame.

**`Laser`** — `[OBSERVED]` a thin **S-shaped / lightning-bolt squiggle**, a single
continuous stroke ~2 px thick running from upper-right down to lower-left with two
reversals. `[MEASURED]` tallest-narrowest glyph bbox of the set (7×12).
Plate rotated +11.25°.

**`Death_ray`** — `[OBSERVED]` **three thick horizontal bars**, stacked with even
gaps, each spanning nearly the full glyph field. `[MEASURED]` the only
**unrotated** plate (fitted angle 0.00°, bbox exactly 44×44), which is why its
bars read as perfectly horizontal. `[INFERRED]` a stylised beam / energy-stack
mark. Second-heaviest glyph (69 px).

**`RC_rocket`** — `[OBSERVED]` **two concentric arcs plus a dot** at the arcs'
centre of curvature — the standard radio-emission / "wifi" mark. `[INFERRED]`
"RC" = radio control, matching `weapons.txt`'s *"you can then guide using you
standard controls"*. Plate rotated 73.00° (≡ −17.00°).

**`Rocket`** — `[OBSERVED]` a **dart/arrowhead** with a sharp apex, straight
flanks and a **concave notch cut into the base**, giving two rear fins.
`[INFERRED]` a missile seen from the side. This file is the icon for the wiki's
**Homing Missile** section (see `weapons.txt` below) — the filename `Rocket` is the
wiki's *caption*, not its heading. Plate rotated 67.25° (≡ −22.75°).

**`Frag_Bomb`** — `[OBSERVED]` a **six-pointed star / burst**, points of unequal
length, solid centre. `[INFERRED]` fragments radiating from a detonation, matching
*"sending shards everywhere"*. Plate rotated 39.75° — the closest to a 45° diamond,
which is why its axis-aligned bbox (58×58) is the largest of the set.

#### Roster gap — what the icon set does *not* cover

`weapons.txt` names **eight** weapons. There are **seven** icons.

| `weapons.txt` heading | wiki caption / filename | icon present? |
|---|---|---|
| Gatling Gun | `Gatling gun` | yes — `I-icon-gatling-gun.webp` |
| Booby Trap | `Booby trap` | yes — `I-icon-booby-trap.webp` |
| Laser | `Laser` | yes — `I-icon-laser.webp` |
| Death Ray | `Death ray` | yes — `I-icon-death-ray.webp` |
| RC Missile | `RC rocket` | yes — `I-icon-rc-rocket.webp` |
| **Homing Missile** | `Rocket` | **yes — `I-icon-rocket-homing-missile.webp`** |
| Frag Bomb | `Frag Bomb` | yes — `I-icon-frag-bomb.webp` |
| **Shotgun** | *(no caption line)* | **NO ICON** |

`[MEASURED]` The task's hypothesis was that Shotgun *and* Homing Missile might both
lack icons. **Only Shotgun does.** Homing Missile has an icon; it is filed under
the wiki's caption name `Rocket`, and the heading/caption mismatch is visible in
the article itself — every other section has a caption line matching its heading,
but the *RC Missile* section is captioned `RC rocket` and the *Homing Missile*
section is captioned `Rocket`. `[INFERRED]` the wiki's *display* names drifted from
its *internal* names; the internal names are the older/engine-side ones. Falsifier:
the wiki's file-description pages showing different original filenames.

`[OBSERVED]` **Shotgun has no icon and no caption line** in the article — its
section is heading-then-body with nothing between. `[OBSERVED]` its body says
*"This weapon can be found in the Tank Trouble Beta."* `[INFERRED]` the icon is
missing because the Shotgun was **not in the classic game** at the article's date
and therefore had no classic crate art to photograph. That is a clean, internally
consistent generation marker and it means **the classic weapon crate set is seven,
not eight**. Falsifier: a classic-era screenshot showing a shotgun crate.

#### Links to the program

* **`srv/Assets/Crate.swf`** — LEDGER row 2, tier **`O`**, held bytes. This icon
  set is a picture of what that SWF draws. Nothing in `VISUAL-EVIDENCE-WANTED.md`
  currently asks for the crate's appearance, which is an omission the evidence
  now exposes: seven glyph designs and a 22×22 plate are actionable, and the
  verification path (render `Crate.swf`, compare) is cheap.
* **S102** (*era game-SWF audio set*, HIGH) — adjacent only. This is art, not
  audio; it does not move S102. But it does confirm the weapon roster S102's
  "verify era weapon sounds match the v4.03 set" would be checked against:
  seven classic weapons, Shotgun excluded.
* **`docs/standards/MAZECREATOR-VISUAL-SPEC.md`** — the *Crate spawn icon* row (editor
  marker, 16×16 amber) is untouched and unchallenged. The *icon rotation (if any)*
  known-unknown is **not** resolved by this: these are in-play crates, not editor
  markers.
* **Gate D / `docs/standards/ASSET-DISCIPLINE.md:21`** — `I-icon-rc-rocket.webp` is an unledgered
  binary outside the `srv/` walk. See finding I-16.

#### What the icons do NOT show

* `[NOT VISIBLE]` **Colour.** The crate is drawn here in pure greyscale. Whether
  the in-play crate is grey, or tinted, or glows, cannot be told from these files —
  the greyscale may be the asset's real palette or may be a wiki-side conversion.
  Only `Crate.swf` or an in-play frame settles it.
* `[NOT VISIBLE]` **Scale on the maze floor.** No cell, no wall, no tank is in
  frame, so the 22 native px cannot be converted to stage px. `CELL = 32` from the
  visual spec is a tempting denominator; **do not use it** — the derivation is
  unsupported.
* `[NOT VISIBLE]` **Animation.** Whether the crate spins, bobs, pulses or fades in
  is invisible in a still.
* `[NOT VISIBLE]` **The pickup/collect state.** No highlighted, empty or
  just-collected crate is in the set.
* `[NOT VISIBLE]` **The Shotgun crate**, as above.
* `[NOT VISIBLE]` **Any HUD/weapon-stack representation** of these icons. Held
  bytes mention a *"weapons stack display"* as a BETA feature
  (`srv/index.php:6657`); nothing here shows one. See sibling
  [F](./F-gameplay-hud-and-chat.md) for what was found in-play.

---

### `Game/I-weapon-toggle-panel.webp` (360×148, 8736 bytes, captured 16:29:29)  *(was `Weapons.webp`)*

The contested item. Read this section before acting on it.

**Filename claim (repo owner):** the filename is just `Weapons` — no descriptive
claim is embedded, so there is nothing to corroborate or contradict. The
*capitalised* filename matches the wiki article title `Weapons` transcribed in
`weapons.txt`, and matches the sibling wiki-derived `G-achievements-panel-full.webp` /
`I-laika-boss-artwork.webp` naming. `[INFERRED]` same source family as the rest of the run.

#### What is drawn

`[OBSERVED]` A white panel with a centred title and **seven** labelled toggle
controls laid out in **two columns**. No border, no shadow, no window chrome, no
close button, no scrollbar is visible within the crop.

**Verbatim transcription** — casing exactly as rendered, no normalisation:

| Position | Label (verbatim) |
|---|---|
| title | `Weapons` |
| left col, row 1 | `Laser` |
| left col, row 2 | `Frag bomb` |
| left col, row 3 | `Death ray` |
| left col, row 4 | `RC missile` |
| right col, row 1 | `Gatling gun` |
| right col, row 2 | `Homing missile` |
| right col, row 3 | `Booby traps` |

`[OBSERVED]` Every multi-word label is **sentence case** — only the first word is
capitalised (`Frag bomb`, not `Frag Bomb`; `Death ray`, not `Death Ray`;
`Gatling gun`, `Homing missile`) — **except `RC missile`**, where `RC` is an
initialism and is fully capitalised. `[OBSERVED]` `Booby traps` is **plural**;
every other label is singular. Both of these are the kind of detail that gets
silently normalised by a careless transcriber, so they are recorded exactly.

`[OBSERVED]` The **order is column-major, not row-major**: reading down the left
column then down the right gives Laser, Frag bomb, Death ray, RC missile,
Gatling gun, Homing missile, Booby traps. Reading across rows gives
Laser/Gatling gun, Frag bomb/Homing missile, Death ray/Booby traps, RC missile/—.
The left column has **four** entries and the right **three**, with the
**bottom-right cell empty** — which is what a 7-item column-major fill produces
(`ceil(7/2) = 4` left, `3` right). `[INFERRED]` the layout algorithm is
"fill column 1 to `ceil(n/2)`, then column 2". Falsifier: a capture with a
different weapon count showing a different split.

`[UNCERTAIN]` The **order itself** does not match `weapons.txt`'s contents list
(Gatling Gun, Booby Trap, Laser, Death Ray, RC Missile, Homing Missile, Frag
Bomb), nor alphabetical, nor (as far as I can tell) release order. I cannot
derive the sort key from one frame.

#### The toggle control

`[OBSERVED]` Each control is a horizontal **pill** (stadium shape) made of two
visually distinct halves:

* a **left half**: a rounded-rectangle **knob**, filled flat grey, carrying a
  **dark outline** that traces its own rounded edge — including down its right
  side, so the knob reads as a separate object sitting *on* the track;
* a **right half**: a flat **bright green** track segment with **no outline at
  all**, its right end rounded to complete the pill.

`[MEASURED]` Sampled values:

| Element | Value | How |
|---|---|---|
| page background | `#ffffff` | 40.43 % of the canvas is exactly `#ffffff`; all four corners |
| knob fill | `#cccccc` | flat across the knob, e.g. (18,47) `#cccccc`, (18,42) `#cbcbcb`, (18,52) `#cdcdcd` |
| knob outline | ~`#686868` → darker | scan row y=47 hits `#686868` at x=6 |
| green track | `#00ff00`-class | (50,47) = `#03fe01`; modal green `#02fe03`; run of `#00ff01` across x=40..54 |
| green→knob boundary | `#004b00` at x=34 | a one-pixel dark seam where the knob's outline crosses the green |
| label text | ~`#7a7a7a` | modal `#7c797c` in the label band |
| title text | ~`#686868` | modal `(104,104,104)` = `#686868` |

`[MEASURED]` The green is **not** a subtle UI green — the modal value `#02fe03`
and the plateau `#00ff01` are within 1–3 levels of **pure `#00ff00`**. The 1–3
level wobble is lossy-WebP chroma noise, not a gradient: `[MEASURED]` only
53.47 % of this file's pixels satisfy R==G==B, against 100.0000 % for the icon
files, so this file *is* lossily encoded and small colour excursions are expected.
`[INFERRED]` the authored colour is exactly `#00ff00`. Falsifier: a
lossless capture showing a deliberate off-green.

`[MEASURED]` Geometry, in capture pixels:

* green track spans **x 31..63** (col 1) and **x 208..240** (col 2) → **33 px wide**;
* green track spans **y 40..56** at x=50 → **17 px tall**;
* knob dark outline begins at **x=6**, so the whole pill is ≈ **x 6..64, 58–59 px wide**;
  the knob is therefore ≈ **26–28 px** and the green ≈ **33 px** — roughly a
  **45 / 55** split;
* column pitch = **177 px** (green col-1 starts x=31, col-2 starts x=208);
* row pitch: green bands start at y = **39, 67, 93/94, 121** → deltas 28, 26–27, 28
  → **≈ 27.3 px**, i.e. `[MEASURED]` 27–28 px, and I will not round that to a
  constant on one sample;
* title ink bbox **x 122..232, y 9..32**; canvas centre x = 180, title centre
  x = 177 — `[MEASURED]` **centred to within 3 px**.

#### Which state is shown?

`[UNCERTAIN]` — and this matters, so it is being left open on purpose.

`[OBSERVED]` **All seven toggles are in the identical state.** `[MEASURED]` all
seven green runs are 30–31 px of green on the sampled centre row, and all seven
knobs sit at the left.

There are two self-consistent readings and this frame cannot separate them:

1. **Knob-left = OFF**, and the green is the track's "available" colour — all
   seven weapons disabled. Against this: a UI rarely paints the *off* state in
   saturated green.
2. **Green = ON**, with the knob drawn at the left of an "ON" pill — all seven
   weapons enabled, which is the sane default state a screenshotter would find.
   Against this: in the near-universal iOS-derived idiom the knob travels to the
   **right** when on.

`[INFERRED]` Reading 2 is more likely — a wiki contributor documenting a settings
panel would photograph the default, and the default for "which weapons appear" is
almost certainly all-on. But I am explicitly **not** calling it. What settles it:
a second frame of the same panel with at least one toggle in the other state, or
any frame where a weapon is known to be disabled.

#### An element continues below the crop

`[MEASURED]` At the bottom-left, pixels x 2..5, y 142..147 hold a flat grey block
at luminance **128–129** that runs to the bottom edge of the canvas and is cut off
by it. It is 4 px wide, starts 3–4 px left of where the toggle pills start (x=6),
and is a different tone from both the knob (`#cccccc` ≈ 204) and the outline.
`[OBSERVED]` So the panel **is not fully captured** — something else exists below
row 148 and slightly to the left of the toggle column. `[UNCERTAIN]` what: it is
too narrow (4 px) to be another toggle knob, and could be a scrollbar, a tab edge,
a section rule or the corner of a neighbouring control. Recording this is the
point — the crop is a fragment of a larger surface.

#### Typography — the generation test

`[MEASURED]` The title `Weapons` splits into seven clean per-letter column runs
(no touching glyphs), giving a per-letter fingerprint:

| | W | e | a | p | o | n | s |
|---|---|---|---|---|---|---|---|
| ink width (px) | **27** | 11 | 12 | 12 | 12 | 11 | 12 |
| gap to next (px) | 2 | 2 | 3 | 2 | 3 | 2 | — |
| left-edge pitch | 29 | 13 | 15 | 14 | 15 | 13 | — |

`[MEASURED]` cap height (`W`) = **19 px**; x-height (`e`) = **13 px**; total ink
width = **111 px**; ratio x-height / cap = **0.684**.

I then rendered `Weapons` in four stock faces at the point size that reproduces a
19 px `W`, and measured the same quantities:

| Face (stand-in) | size | `W` width | total width | x-height | x/cap |
|---|---|---|---|---|---|
| **capture** | — | **27** | **111** | **13** | **0.684** |
| Liberation Sans (Arial metrics) | 27 | 25 | 113 | 15 | 0.789 |
| DejaVu Sans (Verdana-class) | 26 | *(W+e merged)* | 116 | 14 | 0.737 |
| FreeSans (Helvetica clone) | 26 | 24 | 106 | 14 | 0.737 |
| Carlito (Calibri metrics) | 28 | *(W+e merged)* | 105 | 14 | 0.737 |

`[MEASURED]` The **total** width is close to Arial (111 vs 113, 1.8 %), so the
face is of normal (not condensed, not extended) width. But the **distribution** is
wrong for all four: the capture's `W` is **27 px against Arial's 25 and
Helvetica's 24** (8–12 % wider), while its x-height is **13 px against 14–15**
(7–13 % smaller). Wide caps plus a small x-height is a specific, coherent
signature and it is not Arial's, not Helvetica's, not Verdana's, not Calibri's.

`[UNCERTAIN]` on identification — at 19 px cap height a ±1 px quantisation is
5 %, so the x-height gap (1–2 px) is near the noise floor; the `W` gap (2–3 px) is
above it. I am confident enough to say **"not one of those four"** and not
confident enough to name what it is.

`[MEASURED]` Cross-check: the caption inside `I-laika-boss-artwork.webp` (§ below) is set at
cap height 43 px, x-height 30 px → **x/cap = 0.698**, within 2 % of this panel's
0.684 and well below all four stock faces. `[INFERRED]` the two files carry the
**same typeface**. Falsifier: a third sample with a different ratio.

**Why this matters:** VE entry 7 records the classic era's site chrome as the
*"Verdana/Arial family"*. Two independent samples in this corpus are measurably
outside that family in the same direction. That is a generation signal
independent of any pixel-style argument.

#### Grep results — what held bytes say, and what they fail to say

I searched `srv/index.php` (812 KB, 16 678 lines) exactly as instructed. Both
halves of the result matter.

**What is NOT there** `[MEASURED]`, counts from `grep -c -F`:

| needle | occurrences in `srv/index.php` |
|---|---|
| `toggle` | **0** |
| `checkbox` | **0** |
| `onoff` / `on/off` | **0** / **0** |
| `Shotgun` / `shotgun` | **0** / **0** |
| `rcRocket` / `RC Rocket` | **0** / **0** |
| `deathRay` | **0** |
| `@font-face` | **0** |
| `c64` / `commodore` | **0** / **0** |

So: **there is no toggle markup, no settings-panel markup, no weapon-toggle DOM
and no per-weapon control of any kind in the held page bytes.** That is a clean
negative and it is the correct starting point. The panel is **not** a page
surface.

**What IS there** `[MEASURED]`, and it changes the verdict:

* `srv/index.php:9969` — a news item headed **`Customize Your Battles`**, dated
  **`16-12-2008`**;
* `srv/index.php:9974` — its body, verbatim: *"Tired of constantly being sniped by
  your little brother who always happens to be at the right spot to pick up the
  laser? Sick of the usual, random mazes you've been playing for a year now? Well,
  now you can customize your way out of these headaches! **Through the new settings
  menu, you can select which weapons you want in your battles** and what kind of
  mazes you want to play"*;
* `srv/index.php:9976` — *"**To access the settings menu, just click the gear when
  playing the game.** It will start spinning and once the current battle is over,
  the menu will pop up."*;
* `srv/index.php:10010` — an earlier news item (`06-11-2008`) trailing it: *"we
  actually have two new weapons almost ready, a computer player just in need of
  some final tuning, plus **a settings panel which allows you to customize your
  battles**"*;
* `srv/index.php:9707` — *"(You can play other tank owner's mazes too! **Click the
  gear button during the game** to see how.)"* — a second, independent mention of
  the same gear affordance.

Weapon names also appear in prose throughout the news archive (`Gatling` ×8,
`Booby` ×14, `Death Ray` ×18, `Frag` ×5, `Homing` ×2) — narrative, not UI.

#### Verdict on generation

Putting it together, honestly, with the arguments that cut each way:

**For "real and in-era (classic Flash game)":**

* `[MEASURED]` Held bytes prove a settings menu that **selects which weapons you
  want**, reached by a **gear during play**, shipped **2008-12-16**. That is not
  an inference — it is the site's own release note, in `O`-derived page bytes.
* `[MEASURED]` The panel's roster is **exactly the seven classic weapons** with
  **no Shotgun** — matching the classic-only roster established from `weapons.txt`.
* `[MEASURED]` It lives **inside the game**, not on the page, which explains the
  zero page-markup hits perfectly. A Flash-drawn panel leaves no DOM.

**Against, i.e. for "later generation":**

* `[MEASURED]` The typeface is outside the Verdana/Arial family the classic page
  chrome used (measurements above), and matches the face in `I-laika-boss-artwork.webp`.
* `[MEASURED]` `srv/index.php:6657` (news `25-05-2016`) records **"a custom
  TankTrouble font"** as an **Online BETA** feature — so a non-Arial face in a
  TankTrouble surface is a documented BETA trait.
* `[INFERRED]` The **pill toggle** is a post-iOS UI idiom. It is not impossible in
  2008-2013 Flash, but a 2008-era settings menu would more typically use
  checkboxes or on/off buttons. Weak on its own; it points the same way as the type.
* `[MEASURED]` `srv/index.php:7418` (news `09-07-2015`) lists, under *"Not
  forgotten but postponed for now"*: *"Weapons (all weapons need to be rebuilt
  from scratch and we will do that in time — for now smooth online battles is our
  highest priority)"* and *"Laika — the beloved and infamous space dog"*. So as of
  mid-2015 the BETA had **no** weapons and **no** Laika. A BETA weapons panel
  listing all seven therefore has to post-date the weapon rebuild — i.e. **2016 or
  later**, which is *inside* or *after* the 2017–2018 target window rather than
  before it.

**My verdict** `[INFERRED]`, stated with its reasoning so it can be overturned:
this is **most likely the classic Flash game's in-game settings menu, but I cannot
date the *rendering***. The feature is certainly classic and certainly in-era —
that is held-byte fact. The specific pixels in this crop are **not** established
as 2017–2018 classic: the type measurably is not classic page chrome, and the
panel could equally be a **late-classic restyle** or the **BETA's** equivalent
panel after the 2016 weapon rebuild.

**Operationally that means:** treat the *feature* as confirmed and the *artwork*
as unconfirmed. Add a want (below). **Do not build pixels from this crop.** Under
THE OVERHAUL RULE that is not a hardship — there is nothing built to overhaul; the
settings menu is not in the rebuild at all, because it lives inside
`TankTrouble_v4.0.swf`, and this evidence's real value is that it tells the
project the surface **exists** and roughly what it contains.

#### Links to the program

* **New want** — see [§ New wants](#new-wants-to-add). Nothing in the S1–S114
  sweep covers an in-game settings/weapons panel; the closest neighbours are
  **S102** (era game-SWF contents) and **S114** (*"Any on-screen control in era
  footage that maps to nothing in this document = a find"*). By S114's own rule
  **this is a find** and should be promoted out of S114 into its own entry.
* `srv/index.php:9969-9977`, `:10010`, `:9707` — the copy above is the confirming
  evidence and did not previously appear anywhere in the want-list.
* **VE entry 7 / S108** — the typography measurement here is a second, independent
  sample outside the Verdana/Arial family; see the font section for what it does
  and does not do to those entries.

#### What this does NOT show

* `[NOT VISIBLE]` The **gear button** that opens it (`srv/index.php:9976`).
* `[NOT VISIBLE]` The rest of the settings menu — `srv/index.php:9974` says it also
  covers *"what kind of mazes you want to play"*, so there is at least one more
  section, and the truncated element at the bottom-left is consistent with that.
* `[NOT VISIBLE]` Any **panel frame, background plate, title bar or close control**.
* `[NOT VISIBLE]` The **opposite toggle state**.
* `[NOT VISIBLE]` Whether the panel is per-user-persisted, per-session or per-round.
* `[NOT VISIBLE]` Any date, watermark, browser chrome or username that would date
  the frame. **This is the single most damaging absence in my whole topic** — with
  a browser frame or a visible year this panel would be settled either way.

---

### `Game/weapons.txt` (5052 bytes, 51 lines, captured 16:31:46)

**Filename claim (repo owner):** none embedded — plain `weapons.txt`.

#### Format and provenance markers

`[MEASURED]` ASCII, **CRLF** line endings throughout (50 CRLF, 0 bare LF), no BOM,
first byte is a CRLF so the file **opens with a blank line**. 51 logical lines; the
last has no terminator. `[INFERRED]` a Windows-side copy-paste out of a rendered
web page, not a wiki API export (an export would carry markup; this carries the
*rendered* text including navigation).

`[OBSERVED]` **Wiki chrome, verbatim**, lines 2–4:

```
Weapons
Sign In to Save
View source
```

`Sign In to Save` and `View source` are Fandom/Wikia page-furniture strings.
`[INFERRED]` This is a **community wiki article**, copied from a browser. Under
guide §6.5 and the brief §"Provenance", that caps it at **M2, never O**, and it is
a *user-written secondary source* — DEDUCE.md's own verdict on wikis
(`DEDUCE.md:433`) is: *"User-written. Useful for screenshots, unreliable for
facts."* Treat every mechanical claim below as the wiki's assertion, not the
project's finding.

`[OBSERVED]` The dating line appears **twice**, lines 5 and 7, identically:
`The complete list of weapons in Tank Trouble as of 28th February 2013.`
`[INFERRED]` the duplication is a page-summary/lead pair that the copy-paste
flattened. The date is the wiki's own, and it dates the *article*, not the game.

`[OBSERVED]` Lead paragraph, line 9, verbatim (note the grocer's apostrophe in
`it's own`, retained):

> `This article tells you about the available weapons now on Tank Trouble! The term "Weapons" in Tank Trouble refers to the additional power-ups that gradually appear on the battlefield for you to equip. Each power-up has it's own unique abilities and drawbacks that can be used to the user's advantage or inevitable demise.`

#### Roster, as the article gives it

`[OBSERVED]` Contents list, lines 12–19, verbatim including the leading
four-space indent the copy-paste preserved:

```
    1 Gatling Gun
    2 Booby Trap
    3 Laser
    4 Death Ray
    5 RC Missile
    6 Homing Missile
    7 Frag Bomb
    8 Shotgun
```

`[OBSERVED]` The body then repeats a rigid three-part pattern per weapon —
**heading line, image-caption line, blank line, body paragraph** — with exactly
one exception:

| Lines | Heading | Caption line | Icon file |
|---|---|---|---|
| 21–24 | `Gatling Gun` | `Gatling gun` | `I-icon-gatling-gun.webp` |
| 25–28 | `Booby Trap` | `Booby trap` | `I-icon-booby-trap.webp` |
| 29–32 | `Laser` | `Laser` | `I-icon-laser.webp` |
| 33–36 | `Death Ray` | `Death ray` | `I-icon-death-ray.webp` |
| 37–40 | `RC Missile` | `RC rocket` | `I-icon-rc-rocket.webp` |
| 41–44 | `Homing Missile` | `Rocket` | `I-icon-rocket-homing-missile.webp` |
| 45–48 | `Frag Bomb` | `Frag Bomb` | `I-icon-frag-bomb.webp` |
| **49–51** | **`Shotgun`** | **— (absent)** | **— (absent)** |

`[MEASURED]` Line 49 is `Shotgun`, line 50 is blank, line 51 is the body. **The
caption line is missing for Shotgun and only for Shotgun** — which is exactly the
structural trace of a section with no infobox image, and it explains the 7-vs-8
gap in the icon set without any guesswork. This is the cleanest single
confirmation in the file.

`[OBSERVED]` The caption strings are **the icon filenames**, with spaces
substituted for underscores. That closes the loop between the seven `.webp` files
and this article: they are its infobox images.

#### Mechanics, as the article states them

Transcribed faithfully. These are the **wiki's claims about the game**, not
verified behaviour, and where the prose is broken I have left it broken.

**Gatling Gun** (line 24) — *"fires a series of tiny bullets out in rapid
succession, in which bullets will bounce around at random, and are extremely
unpredictable. Has to charge up for approximately 1 second making this weapon
somewhat undesirable in close quarters. Can be unequipped by continuously pressing
the fire button without actually firing the weapon."*

**Booby Trap** (line 28) — *"it doesn't actually shoot something. Rather, it will
lay a land-mine over the area immediately behind the tank using it, which will
then become invisible. If a tank drives over the land-mine it will reappear and
almost immediately explode, sending shrapnel out in all directions in a way
similar to the frag bomb. If a tank reveals a booby trap and quickly stays
immobile, then it will not explode, but if the player moves it they will end up
exploding with it. Bullets and other weapons cannot trigger the booby trap."*

**Laser** (line 32) — *"works as both a weapon and targeting apparatus. Once you
have acquired the power-up, a dotted line will emerge from your tank's barrel,
tracing the path that the laser will follow when fired for almost half its range.
Once fired, the line will turn solid and continue out, destroying any tank in its
way and stopping once a tank has been hit or it's range has been met.once it either
reaches the end of its range or hits a tank. The laser must be prepared carefully,
such that it does not reflect of any walls back to the same tank."*

> `[OBSERVED]` Note the mangled fragment inside that passage, verbatim:
> `...or it's range has been met.once it either reaches the end of its range or hits a tank.`
> — a missing space after the full stop and a duplicated clause. That is a
> botched edit left in the article, not my transcription error. Flagged rather
> than tidied.

**Death Ray** (line 36) — **this line opens with vandalism.** The line begins,
verbatim and unaltered:

```
gang gang scince potty train Some consider this power up the most effective, however it has it's drawbacks as well.
```

> ⚠ **`[OBSERVED]` VANDALISM — QUARANTINED, NOT LAUNDERED.**
> The string `gang gang scince potty train ` is an inserted fragment at the head
> of the Death Ray body. It is not a sentence, it has no relation to the subject,
> it contains a misspelling (`scince`), and it sits immediately before what is
> plainly the paragraph's real opening word `Some`. It is recorded here **exactly
> as it appears** and is **not** to be paraphrased away.
> **Consequence:** this article has been edited by at least one bad-faith or
> careless contributor, and that edit survived to the moment of capture. Nothing
> in this file can be trusted without a second source — including the parts that
> read as sensible prose. That is a general downgrade on the whole file, not a
> local defect.

With the vandalism excluded, the remainder of line 36 reads: *"…Some consider this
power up the most effective, however it has it's drawbacks as well. When activated
this weapon will need to charge up, much like the Gatling gun, however it takes
approximately 2 seconds to fire and you cannot move during the entire process of
using this weapon. After charging, the tank will shoot out a brightly colored
energy beam in the direction the tank is pointing, (still not being able to move)
which will pass right through walls and curve slightly toward your target, however
if the target is close and the aim is slightly off, they are likely to miss and be
a sitting duck. The beam can destroy multiple tanks in one shot and will only stop
once it hits the outer wall. Custom mazes tend to have some of the outer walls
within the inner battlefield."*

**RC Missile** (line 40) — *"fires a single missile, which you can then guide using
you standard controls. It will still bounce off of walls if not given other
instructions, and is difficult to control, but for mouse or skilled keyboard users
it can be quite effective. The main draw back is that once it is fired you will be
unable to move your tank until it has either timed out or hit a tank, meaning you
can't dodge while using it."* (`using you standard controls` is the source's typo.)

**Homing Missile** (line 44) — *"When first fired this weapon will bounce around
just like the RC missile, however, after a few seconds the normally grey color of
its smoke will change to the color of the nearest tank, which it will then home in
on and destroy. Skilled Tank Trouble players will be able to avoid being hit by the
missile and have the ability to either have the missile chase them yo the next
nearest tank and have the missile switch targets, or avoid it until it times out.
It should only be used near an enemy tank to avoid the missile hitting yourself."*
(`chase them yo the next` is the source's typo.)

**Frag Bomb** (line 48) — *"fires a single bullet, the only difference in
appearance being it's a bit bigger than the average bullet. Once fired, you cannot
fire another one. If you press the fire button again, or it hits a tank, the bullet
will explode, sending shards everywhere, much like the Booby Trap. Skilled Tank
Trouble players will be able to avoid being hit by the shards that will stop when
it hits a wall then stays there."*

**Shotgun** (line 51) — *"**This weapon can be found in the Tank Trouble Beta.**
When the player fires, tiny bullets fly out and spread in the direction the tank is
facing. The bullets can also bounce on walls, and dissapear after 2-3 seconds. This
weapon is a double-edged sword, since it can be very effective against multiple
players in an open area, but can also result in you and your opponent's death in
small areas."* (`dissapear` is the source's spelling.)

#### The two dated claims, recorded as dated claims

`[OBSERVED]` **Laser vs Laika, line 32, verbatim:**

> `As of 28th February 2013, this is the only power up which can be used versus Laika. But, Tank Trouble are thinking of a new weapon to use versus Laika.`

Recorded as **a claim about 28 February 2013**, *not* as a present-tense fact about
the 2017–2018 target era. Two reasons to hold it loosely:

1. `[MEASURED]` The article itself flags the situation as in flux (*"thinking of a
   new weapon"*), so it was expected to change.
2. `[MEASURED]` Held bytes show the site actively changing Laika's armament:
   `srv/index.php:9436` is a news item headed **`Laika Goes to Laser Training
   Camp`**, and `:9441` reads *"The lab gets lots of requests that Laika should be
   given weapons. Scientists have been reluctant to do this, as Laika is already
   far beyond control. Now we gave her the…"*. The relationship between Laika and
   the laser was a moving target on the developer's side too.

`[OBSERVED]` **Shotgun is Beta-only, line 51** — *"This weapon can be found in the
Tank Trouble Beta."* This is the article's own generation marker and it is
load-bearing for this whole topic: it is why there are seven icons and not eight,
it is why the `I-weapon-toggle-panel.webp` panel lists seven and not eight, and it is
independent corroboration that the classic game's weapon roster is **seven**.

`[UNCERTAIN]` **Which "Beta"?** In 2013 the phrase could mean an early build of the
Flash game; `srv/index.php` uses *"Online BETA"* / *"BETA"* consistently for the
HTML5 `beta.tanktrouble.com` product, whose first news mention I can find is well
after 2013 in the same archive. The article says only *"the Tank Trouble Beta"*.
This is worth *not* resolving by assumption. What would settle it: any 2013-dated
mention of a TankTrouble beta in held bytes or CDX.

#### Links to the program

* **S102** (era game-SWF audio set, HIGH) — this roster is what the era weapon
  *sound* set should be checked against: seven weapons, Shotgun excluded. Does not
  move S102's status; gives its verification a target list.
* **S103** (`laika02.swf`) — the Laser/Laika claim is the only piece of *behavioural*
  Laika evidence in my whole assignment, and it is a secondary source. See the
  `I-laika-boss-artwork.webp` section.
* `srv/index.php:9436,9441` — corroborates that Laika/laser interaction was a real
  subject on the developer side.
* **Nothing in this file touches `docs/standards/MAZECREATOR-VISUAL-SPEC.md`.**

#### What this does NOT show

* `[NOT VISIBLE]` **Any wiki URL, revision id, contributor name or capture date.**
  The copy-paste dropped all of it. Under THE OVERHAUL RULE §3 and guide §6.5 a
  LEDGER row for this file needs *URL, uploader, date, timestamp* — **none of the
  four can be supplied from the file itself**. This is a real blocker on
  ledgering it and should be recorded as such.
* `[NOT VISIBLE]` Any numeric parameters — damage, cooldowns in frames, projectile
  speeds, spawn rates. All timings in the article are prose approximations
  (*"approximately 1 second"*, *"approximately 2 seconds"*, *"2-3 seconds"*).
* `[NOT VISIBLE]` Crate spawn logic — how often, where, how many at once.
* `[NOT VISIBLE]` What the weapons look like in flight (only the Homing Missile's
  smoke recolouring is described).

---

### `Game/I-laika-boss-artwork.webp` (336×486, 13 610 bytes, captured 16:29:47)  *(was `Laika.webp`)*

**Filename claim (repo owner):** `Laika` only — no descriptive claim to test.
`[OBSERVED]` The image carries its own caption reading `Laika`, so the filename is
corroborated by the image content.

#### Composition, element by element

`[OBSERVED]` A single character illustration on a **white** field, with a caption
below it.

`[MEASURED]` The canvas splits into two ink bands with a clean 18-row gap:

| Band | rows | content |
|---|---|---|
| artwork | y **3 – 418** | the illustration |
| *(gap)* | y 419 – 436 | pure white |
| caption | y **437 – 481** | the word `Laika` |

`[MEASURED]` Artwork ink bbox: **x 8..332, y 3..418 → 325 × 416 px**, aspect
(w/h) **0.781**. Caption ink bbox: **x 114..244, y 438..480 → 131 × 43 px**.
`[MEASURED]` All four canvas corners are `#ffffff`; there is **no alpha channel**
(mode `RGB`), so as with the icons the white is a baked matte.

**The composition** `[OBSERVED]`, top to bottom:

1. **A dog, upright, seen from its left side, head turned toward the viewer.**
   Two large erect triangular ears, the near one showing an inner fold. A long
   tapered muzzle pointing to the viewer's left, with a black nose mass at its tip
   and a visible lower jaw line. The neck runs down into a chest and a foreleg;
   the haunch and a curved tail are visible at the right of the figure.
   `[INFERRED]` a husky/laika breed silhouette, which matches the character's name
   and the site's own story (`srv/index.php:9838`).
2. **A single visible eye, glowing red.** `[MEASURED]` an almond-shaped black eye
   slot with a red core: strong-red cluster at **x 186..203, y 77..96 (18 × 20 px)**,
   peak values in the `#a90101`–`#ff0000` band falling off to `#510403`/`#630000`
   at the rim. `[OBSERVED]` The red is brightest at the centre and fades outward —
   it is drawn as a **glow**, not a flat fill. Only **one** eye is visible; the far
   eye is hidden by the head turn.
3. **A white specular streak** above and left of the eye, running along the top of
   the muzzle/brow. `[OBSERVED]` A second white highlight traces the back of the
   head and neck as a thin rim-light.
4. **A torn-open cavity in the neck/upper chest** exposing internal hardware:
   `[MEASURED]` a coloured cluster at **x 201..253, y 166..246** containing
   **red** wiring (`#a90101`-class, 357 px below y=130) and **blue** wiring
   (`#0301b5`, `#03038e`, `#00002b`; 485 px) plus a **bright metallic
   white/silver vertical rod** running through it. `[INFERRED]` this depicts the
   cybernetic interior — matching `srv/index.php:9838` verbatim: *"they wired it
   to a **pneumatic-powered titanium body**"*. Falsifier: an alternative reading of
   the cavity as damage rather than mechanism, which the wires argue against.
5. **A tank body, in front of and below the dog**, in near-black. A long
   cylindrical **barrel** projects to the viewer's **left**, drawn with a visible
   circular muzzle opening at its end and a slight downward tilt. Behind it a
   wedge-shaped hull, and along the hull's lower right a run of **circular road
   wheels** (I count 8–9 distinct dark circles in two rows) representing the track
   assembly. `[OBSERVED]` The dog is composed *behind* the tank — the tank
   silhouette occludes the dog's lower body — so the figure reads as "dog riding /
   fused with tank", which is exactly the character.
6. **The caption `Laika`**, centred under the artwork.

#### Palette

`[MEASURED]` **96.80 %** of the canvas is neutral (R==G==B): 158 064 of 163 296
pixels. Only **1340 pixels (0.82 %)** are saturated beyond `max−min > 50`, and
they are entirely the eye and the wires (bbox x 185..253, y 77..246). So the
artwork is **greyscale except for the eye and the wiring**, which is a deliberate
and effective piece of design, not an artefact.

`[MEASURED]` Dominant tones:

| Colour | count | share | role |
|---|---|---|---|
| `#ffffff` | 70 679 | 43.28 % | matte |
| **`#444444`** | 12 547 | **7.68 %** | the dog's mid-grey fur — the single largest ink tone |
| `#0a0a0a` | 6 068 | 3.72 % | tank body |
| `#161616` | 3 901 | 2.39 % | tank body shading |
| `#000000` | 2 470 | 1.51 % | outlines |
| `#666666` | 1 567 | 0.96 % | fur highlight / caption |
| `#1f1f1f`, `#1a1a1a`, `#1e1e1e`, `#262626` | ~5 700 | 3.5 % | tank/shadow ramp |

`[OBSERVED]` A worth-noting coincidence, flagged **as a coincidence**: the dog's
dominant fur tone is exactly `#444444`, which is also the pinned **wall colour** in
`docs/standards/MAZECREATOR-VISUAL-SPEC.md`. `[INFERRED]` This is almost certainly chance —
`#444444` is a common "dark grey" shorthand — and I would not treat it as evidence
of a shared palette. Recording it so a later reader does not "discover" it and
over-read it.

#### Rendering style

`[OBSERVED]` Hard black outlines of varying weight, flat interior fills with a
small number of discrete tones, and hard-edged white highlights. `[INFERRED]`
**vector/cel style** (Flash-native), not painted or raster-shaded. Falsifier: a
higher-resolution copy showing gradient interiors.

`[MEASURED]` But the *file* is **not** a native-resolution render. A cut across the
caption's `L` stem at row 460 reads
`255 255 236 191 143 99 56 75 92 111 127 150 180 208 238 255` — a **4-px
approach ramp and a 7-px exit ramp** around a 1-px core. A native vector render at
this size would give a 1–2 px anti-aliased edge. `[INFERRED]` this file was
**upscaled and/or heavily recompressed** before I saw it. Consequence: **do not
trace outlines or letterforms off this file for reproduction.** It is good for
composition, palette and proportion; it is not good for geometry.

#### Comparison with `laika02.swf` (S103) — carefully

**What S103 says** (`docs/standards/VISUAL-EVIDENCE-WANTED.md:313`), verbatim:

```
| S103 | **`laika02.swf` behaviour** | SWF | Held O, embedded once at 140×250 in a news item; never verified | `srv/index.php:9826` | Scroll to the Laika news item | MED |
```

**What I actually grepped** — `srv/index.php:9826`, verbatim, confirming the entry
is accurate:

```js
	var sy = new SWFObject("includes/laika02.swf", "laika", "140", "250", "8", "#ffffff");
```

`[MEASURED]` Surrounding context I also read and can cite:

* `:9822` — `<div id="newsLaika" style="position: absolute; top: -60px; left: 5px; width: 140px; height: 250px;"></div>`
* `:9827-9830` — `allowScriptAccess=sameDomain`, `menu=false`, `quality=best`,
  **`wmode=transparent`**
* `:9831` — `sy.write("newsLaika")`
* `:9835-9842` — the news body it illustrates, which contains the
  *"pneumatic-powered titanium body"* line matching the wiring in this artwork.

Two details the S103 entry does not currently record and which are free evidence:
`[MEASURED]` the embed is **`wmode="transparent"`** with bgcolor `#ffffff`, and it
is positioned **`top: -60px`** inside a `108px`-wide container, so **60 px of the
250 sits above the news item's content box**. Any reconstruction must reproduce
that overhang.

**The aspect-ratio test:**

| | width | height | aspect w/h |
|---|---|---|---|
| `I-laika-boss-artwork.webp` artwork ink bbox | 325 | 416 | **0.781** |
| `I-laika-boss-artwork.webp` full canvas | 336 | 486 | 0.691 |
| `laika02.swf` embed | 140 | 250 | **0.560** |

`[MEASURED]` They **do not match**. Scaling the wiki artwork to 140 px wide gives
**179 px tall** — 71 px short of the 250 px stage. Scaling it to 250 px tall gives
**195 px wide** — 55 px wider than the 140 px stage. Neither direction fits.

**Verdict on S103** `[INFERRED]`, and deliberately negative:

> This artwork is **not verified** to be `laika02.swf`, and the aspect ratio is
> evidence *against* a straight identity. It is **plausibly the same character
> art**: the news item at `:9835-9842` describes exactly this creature, the
> wiring in the artwork matches the story's "pneumatic-powered titanium body",
> and there is no competing Laika design in evidence. But "same character" is a
> long way from "same asset", and:
>
> * an SWF stage is a *stage*, not a bounding box — a 140×250 stage can hold a
>   0.781-aspect figure with headroom for animation, so the mismatch is not
>   conclusive either;
> * matching a fan-wiki illustration to an SWF render **by eye** is exactly the
>   weak-evidence move the brief warns against. I am not making it.
>
> **S103 stays `WANTED`.** This image does not move it.

#### What the project already holds that S103 does not mention

`[MEASURED]` `grep -n -i "laika" LEDGER.tsv` returns **six** rows, and S103 names
only one of them:

| LEDGER | path | tier | note |
|---|---|---|---|
| 4 | **`srv/Assets/Laika.swf`** | **`O`** | `sha256 c5bafd71685f…`; era method *identical+era-confirmed* |
| 58 | `srv/images/boxLaikaTopAndMiddleAndBottom.jpg` | `O` | recovered classic `/images/` set |
| 122 | `srv/images/shopBlackTShirtWithRedEyeYellowLaikaOnFront.jpg` | `O` | — |
| 125 | `srv/images/shopWhiteTShirtWithRedEyeBlackLaikaOnFront.jpg` | `O` | — |
| 176 | `srv/includes/laika02.swf` | `O` | the S103 subject |
| 323 | `srv/images/laika.jpg` | `known-lost` | referenced by era pages (`srv/index.php:10575`) |
| 324 | `srv/images/laikaSmall.jpg` | `known-lost` | see below |

Three things fall out of this, and they are the most useful part of this section:

1. `[MEASURED]` **`srv/Assets/Laika.swf` is held `O`** and is the *game-side* Laika —
   the boss the wiki article talks about. S103 is scoped to `laika02.swf` (the
   *news-item* Laika) and does not mention it. **S103 is under-scoped**: verifying
   `laika02.swf` leaves the game boss unverified. That is a want-list defect this
   evidence exposes.
2. `[MEASURED]` **The two shop T-shirt filenames both contain `RedEye`** —
   `shopBlackTShirtWith**RedEye**YellowLaikaOnFront.jpg` and
   `shopWhiteTShirtWith**RedEye**BlackLaikaOnFront.jpg`. Those are **held `O`
   bytes whose own filenames independently corroborate the single glowing red eye**
   measured above at x 186..203, y 77..96. That is a genuine cross-confirmation
   from original bytes to a wiki illustration, and it is the strongest thing this
   image achieves. `[INFERRED]` the red eye is canonical Laika, not a fan liberty.
3. `[MEASURED]` **LEDGER row 324** already records, verbatim in its notes column:
   *"basename matches elsewhere in the archive (`ia-items/extracted/images/LaikaSmall.jpg`;
   **`wiki-dumps/tt-game-wiki/images/LaikaSmall.jpg`**) are unproven — adjudicate by
   eye before any promotion"*. **The project already holds a wiki dump of a
   TankTrouble game wiki**, containing a Laika image. `[INFERRED]` that dump is very
   likely the same wiki this whole capture run came from. If so, the *upstream,
   un-upscaled* originals of `I-laika-boss-artwork.webp` and all seven weapon icons may already be
   sitting in `archive/wiki-dumps/tt-game-wiki/images/` — which would make every
   resolution complaint in this document go away. **This is the single highest-value
   next action arising from my topic**, and it costs one `ls`.

#### What a proper verification would require

Listing this explicitly because the brief asked:

1. **Render `srv/includes/laika02.swf`** (held `O`, LEDGER 176) under Ruffle or a
   Flash projector at its embedded 140×250, `wmode=transparent`, and capture frames.
   The `oracle/` Ruffle spike harness already exists (README §"What comes next" 2).
2. **Compare against `srv/Assets/Laika.swf`** (held `O`, LEDGER 4) rendered the
   same way — establish whether the news Laika and the game Laika are the same art.
3. **Compare both against this wiki illustration** on *structural* features that
   survive scaling — ear angle, muzzle length ratio, eye position as a fraction of
   head width, wheel count, barrel-length-to-hull ratio — **not** on outline
   tracing, which this upscaled file cannot support.
4. **Check `archive/wiki-dumps/tt-game-wiki/images/`** for the original of this file
   (per LEDGER 324's own note) and, if present, ledger it properly with URL /
   uploader / date / timestamp per guide §6.5.
5. Only then, if they match, promote anything.

Steps 1–2 need no new evidence at all: **both SWFs are already held as `O`.** S103
is blocked on *effort*, not on *material*. That is worth saying plainly in the
want-list, because "WANTED" currently implies the opposite.

#### What this does NOT show

* `[NOT VISIBLE]` **Any animation.** Laika's idle, turn, fire, hit and death
  states are all absent. S103 asks for *behaviour*; a still gives none of it.
* `[NOT VISIBLE]` **Laika in the maze**, at gameplay scale, next to a player tank.
  No size relationship can be derived.
* `[NOT VISIBLE]` **Laika's weapon firing** — nothing here bears on the
  `weapons.txt` laser claim.
* `[NOT VISIBLE]` **Any second colour state** (damaged, enraged, difficulty tiers).
  `srv/index.php:8595` says *"Laika is a very independent individual and does not
  come with a difficulty setting"*, so there may be no variants to find.
* `[NOT VISIBLE]` The source wiki, URL, revision or date — same ledgering blocker
  as `weapons.txt`.

---
### `TankTrouble.ttf` (114 092 bytes, captured 16:35:38)

**Filename claim (repo owner):** the name `TankTrouble.ttf` is itself the claim,
and it is the one thing in this whole document most likely to be believed without
checking. It turns out to be **half right in a way that matters**: the file really
is TankTrouble's own font, made by the classic site's own designer — and that
still does not make it a classic-site *asset*. Those are two different questions
and the rest of this section keeps them apart.

**Staging note.** This file reached me late; an earlier revision of this document
recorded it as absent. That was a staging fault, not a real absence. Everything
below was measured here with `fontTools 4.62.1` against the actual bytes.

#### Identity

`[MEASURED]`

| | |
|---|---|
| size | **114 092 bytes** (matches the stated size) |
| sha256 | `b5cf704099dc54ac37ec05fc8b6d9d5daa98fda13488e6c04adaf2cbddc13ed0` |
| md5 | `7c4cdb291711872052552fc07a9cb6c0` |
| sfntVersion | `\x00\x01\x00\x00` — **TrueType outlines**, not CFF/OTTO |
| tables | `LTSH OS/2 VDMX cmap cvt fpgm glyf hdmx head hhea hmtx kern loca maxp name post prep` |

The sha256 is recorded so a LEDGER row can be written the moment provenance
arrives, and so anyone else can confirm they are looking at the same bytes.

#### Name table — verbatim

`[MEASURED]` Every string is present **twice**, once on platform 1 (Macintosh,
enc 0, lang 0) and once on platform 3 (Windows, enc 1, lang 1033 = en-US), with
**identical content** in both. Transcribed verbatim:

| id | field | value |
|---|---|---|
| 0 | copyright | `Copyright (c) 2016 by TankTrouble. All rights reserved.` |
| 1 | family | `TankTrouble` |
| 2 | subfamily | `Regular` |
| 3 | uniqueID | `TankTrouble: TankTrouble: 2016` |
| 4 | fullName | `TankTrouble` |
| 5 | version | `Version 2.000` |
| 6 | psName | `TankTrouble` |
| 8 | manufacturer | `TankTrouble` |
| 9 | **designer** | **`Mads Purup`** |
| 10 | description | `Copyright (c) 2016 by TankTrouble. All rights reserved.` |
| 12 | **designerURL** | **`www.purup.com`** |

`[OBSERVED]` There is **no** name id 7 (trademark), 11 (vendorURL), 13 (license)
or 14 (licenseURL). `[OBSERVED]` id 10 (description) is not a description at all —
it duplicates the copyright string, which is what a font editor writes when the
field is left to default from another.

`[OBSERVED]` **`Version 2.000`** — this is a **second-generation** font. A version
1.x existed. That is a small but real fact: whatever this is, it was revised at
least once.

#### Metrics and technical profile

`[MEASURED]`

| | value | note |
|---|---|---|
| unitsPerEm | **1000** | PostScript-style upem on TrueType outlines |
| numGlyphs | **211** | |
| cmap entries | **210** | 3 subtables: (0,3,fmt4), (1,0,fmt6), (3,1,fmt4) |
| kern pairs | **392** | one subtable — real kerning, not a stub |
| OS/2 version | 3 | |
| usWeightClass | **400** | *see the disagreement below* |
| usWidthClass | 5 (medium) | |
| achVendID | **`pyrs`** | |
| **fsType** | **0** | **Installable Embedding — no restriction** |
| fsSelection | 64 (REGULAR) | |
| sCapHeight / sxHeight | **790 / 620** | **x/cap = 0.7848** |
| sTypoAscender/Descender/LineGap | 830 / −170 / 100 | |
| usWinAscent / usWinDescent | 830 / 170 | |
| hhea ascent/descent/lineGap | 950 / −170 / 0 | |
| head bbox | xMin 0, yMin −183, xMax **1158**, yMax 950 | xMax > upem — at least one glyph is wider than the em |
| head flags / macStyle | 25 / 0 | flags bits 0,3,4 |
| lowestRecPPEM | 9 | |
| post | format 2.0, italicAngle 0.0, not fixed-pitch, underline −75 / 50 | |
| PANOSE | **all ten digits are 0** | unclassified |

Two of these are worth pulling out.

`[MEASURED]` **The font is fully hinted.** `fpgm`, `prep`, `cvt `, plus the
`hdmx`, `LTSH` and `VDMX` device-metrics tables, are all present. `[INFERRED]`
Those three device tables are not written by hand or by casual converters — they
are emitted by a professional TrueType production pipeline. This is not a
five-minute fan export. Falsifier: a free converter that also emits `VDMX`.

`[MEASURED]` **`fsType = 0`** — *Installable Embedding*, the most permissive
setting. `[INFERRED]` there is **no licensing bar** to the project holding,
embedding or serving these bytes if provenance ever justifies it. That removes one
objection I raised in the earlier revision as a hypothetical; it is now settled and
the answer is favourable.

`[MEASURED]` **`achVendID = 'pyrs'`.** `[INFERRED]` This is **FontLab's** vendor
ID (registered to Pyrus, FontLab's predecessor) and it is what FontLab writes when
the designer never sets one. So the production tool was FontLab and the vendor
field was left at its default. Falsifier: another editor shipping the same default.
Note this **conflicts** with a tempting misreading — `pyrs` is *not* an
abbreviation of "Purup", and should not be cited as one.

**Where I disagree with a plain reading of the metrics:** `usWeightClass = 400`
declares this a **Regular**, and `fsSelection = 64` declares REGULAR too. Both are
`[MEASURED]` and both are, on the evidence of the outlines, **wrong** — the face is
visibly and measurably heavy (stem/cap **0.316** against Arial's 0.105; see the
specimen below). `[INFERRED]` the weight fields were left at their defaults, like
`achVendID` and PANOSE. Consequence: **do not select or substitute this font by
its declared weight.** Anything matching on `usWeightClass` will match it against
the wrong things.

#### Dates — and the contradiction I am not going to resolve

`[MEASURED]` Raw `head` values: `created = 3463189411`, `modified = 3592468330`.

`[MEASURED]` These are read on the **standard TrueType epoch, 1904-01-01 00:00:00
UTC** (the "Mac epoch"), which is what the OpenType `head` spec mandates:

| | raw | **1904 epoch (spec)** | 1970 epoch (alternative) |
|---|---|---|---|
| `head.created` | 3463189411 | **2013-09-28 05:03:31 UTC** | 2079-09-29 |
| `head.modified` | 3592468330 | **2017-11-02 11:52:10 UTC** | 2083-11-03 |

`[OBSERVED]` `fontTools` emits `'created' timestamp seems very low; regarding as
unix timestamp` while parsing. I checked what it then printed rather than trusting
the warning: `timestampToString` returned `Sat Sep 28 05:03:31 2013` and
`Thu Nov 2 11:52:10 2017` — i.e. **the 1904 reading**, which is also what its own
`epoch_diff` arithmetic produces. `[INFERRED]` the warning is a heuristic
false positive. The alternative 1970 reading is **self-refuting**: it dates the
file to 2079 and 2083, decades in the future. So the 1904 reading is not merely
preferred, it is the only tenable one. Falsifier: none that I can construct.

Now the part that matters, stated without picking a side:

* `head.created` **2013-09-28** — three years *before* the copyright year.
* copyright / uniqueID **2016**, and `srv/index.php:6657` puts "a custom
  TankTrouble font" in Online BETA on **2016-05-25**. These line up.
* `head.modified` **2017-11-02** — **inside the 2017–2018 target window.**

`[OBSERVED]` **These three facts do not agree.** A 2013 creation date predates the
BETA font announcement by nearly three years and sits close to the era this
corpus's wiki material is dated to (`weapons.txt`: "as of 28th February 2013"). A
2016 copyright and a `Version 2.000` fit the BETA announcement almost exactly. A
2017-11-02 modification falls squarely inside the classic reconstruction's target
window, when the classic site was still live.

`[UNCERTAIN]` Every reconciliation I can construct is speculative and I decline to
pick one. For the record, the ones I considered: (a) drawn 2013 for the classic
game, re-cut and re-copyrighted 2016 for BETA, touched again 2017 — which would
make it *both*; (b) drawn 2013 for something unrelated, adopted 2016 for BETA,
2017 being a routine re-export; (c) `head.created` inherited from a template or
predecessor file, which is common and would make the 2013 date meaningless.
**Nothing in these bytes distinguishes (a), (b) and (c)**, and the difference
between them is exactly the difference between "belongs in the rebuild" and "must
be kept out". What would distinguish them: a CDX row, an `@font-face`, or a v1.x
copy of the same family.

#### Coverage

`[MEASURED]` 210 mapped codepoints, range **U+0020 – U+2605**:

| block | count | detail |
|---|---|---|
| ASCII printable U+0020–007E | **95** | complete |
| Latin-1 Supplement U+0080–00FF | **94** | accented Latin, punctuation, symbols |
| Arrows U+2190–21FF | **4** | exactly `U+2190 ← U+2191 ↑ U+2192 → U+2193 ↓` |
| Box drawing U+2500–257F | **16** | exactly `U+2500`–`U+250F`, contiguous |
| Misc symbols U+2600–26FF | **1** | **`U+2605 ★ BLACK STAR`** |

**A correction to the reading I was given:** the second block was described to me
as "Latin-1/Ext". `[MEASURED]` It is **entirely Latin-1 Supplement (U+0080–00FF)**.
There is **no** Latin Extended-A, **no** Latin Extended-B, and no Greek, Cyrillic
or currency block. That matters — a font with Latin Extended-A is aiming at
European localisation; one that stops at Latin-1 is not. This one is not.

`[INFERRED]` The shape of that coverage is a **fingerprint**, and it is the most
useful thing in this section for future evidence-matching:

* 95 + 94 = 189 glyphs of ordinary Latin text support — a normal Western UI font;
* **plus** four directional arrows — the four a game would draw for arrow-key
  controls;
* **plus** exactly the first sixteen box-drawing characters — `U+2500`–`U+250F`,
  i.e. the light/heavy horizontals, verticals and the down-and-right corners.
  Nobody adds sixteen box-drawing glyphs to a display font by accident; they were
  added because something **drew boxes with them**;
* **plus** a single star.

`[INFERRED]` This is a **UI-drawing set, not a text set**. Falsifier: a stock
display font from a foundry shipping this exact combination. **Practical
consequence:** any era UI surface that draws a box rule, a frame, an arrow-key
hint or a star rating is a candidate site for this font, and matching one is the
cheapest available route to answering "was it ever served?" — see the rescoped
S116 below.

#### The specimen — what the face actually looks like

`[OBSERVED]` Rendered at 96 px (`Hamburgefons 1234567890`) and read back:

> a **heavy, wide, slightly irregular display sans**. Strokes are very thick;
> terminals are **cut at angles** rather than square or rounded; verticals are
> not quite vertical and the baseline is deliberately a little unsteady, giving a
> hand-drawn, comic/game feel. There is no contrast modulation. It reads as a
> *logotype/headline* face.

`[MEASURED]` Quantified against stock faces, all at a matched cap height of 19 px
(the cap height of the `I-weapon-toggle-panel.webp` title), rendering the string `Weapons`:

| Face | `Weapons` ink width | x-height | x/cap | `l` stem width | **stem/cap** |
|---|---|---|---|---|---|
| **`TankTrouble.ttf`** | **130** | 16 | 0.842 | **6** | **0.316** |
| Liberation Sans (Arial) | 113 | 15 | 0.789 | 2 | 0.105 |
| FreeSans (Helvetica) | 106 | 14 | 0.737 | 3 | 0.158 |
| DejaVu Sans (Verdana class) | 116 | 14 | 0.737 | 3 | 0.158 |
| **capture — `I-weapon-toggle-panel.webp` title** | **111** | **13** | **0.684** | — | — |

`[MEASURED]` Its stem is **three times** Arial's relative to cap height
(0.316 vs 0.105) and twice Helvetica's. That is not a marginal difference at the
noise floor; it is the difference between a text face and a black display face.

#### Cross-check against sibling analyst A — the foot bar agrees, and that means nothing

Analyst A concluded from measured glyph shapes that the **editor title face is in
the Arial/Helvetica class, with Verdana and Tahoma excluded**, on the grounds that
the digit `1` has **no foot bar**.

`[MEASURED]` I rendered `TankTrouble.ttf`'s digit `1` at 220 px and measured its
ink-width profile down the glyph:

```
top 5%   50 px      (the angled upper flag)
25%      69 px      (flag at its widest — the glyph's bbox maximum)
mid      52 px
75%      50 px
btm 5%   48 px
baseline 32 px      (narrowing — an angled terminal cut, NOT a widening foot)
```

`[OBSERVED]` The glyph is a bare, very heavy stem with a small angled upper flag,
and it **narrows** toward the baseline (69 → 48 → 32) instead of flaring. **There
is no foot bar.** So it passes A's exclusion test.

`[INFERRED]` **And that agreement is worthless as evidence, so it must not be
allowed to read as support.** A's test is discriminating *within a family of text
sans faces*, where a foot bar is a real design choice that separates
Verdana/Tahoma from Arial/Helvetica. It has no power here: this is a black display
sans in which a serif-like foot bar would be stylistically impossible. The font
passes the test the way a brick passes a test for "not being made of wood". Two
faces agreeing on one binary feature, when one of them could not have failed it,
is coincidence.

`[MEASURED]` The **discriminating** comparison rules the font out decisively and
on much stronger grounds:

* **weight** — stem/cap 0.316 vs the Arial/Helvetica class's 0.105–0.158, a **2–3×**
  gap;
* **width** — `Weapons` renders **130 px** against Arial's 113 and the capture's
  111, i.e. **17 % wider than the captured title** at matched cap height;
* **terminals** — angled cuts and an intentionally irregular baseline, against
  the flat horizontal terminals and rigid verticals of the Arial/Helvetica class;
* **role** — `lowestRecPPEM = 9` notwithstanding, a face of this weight is
  unreadable as 12–18 px body/UI text, which is the size band VE entry 7 measured
  (`~18px` title, `~12px` watermark).

`[INFERRED]` **`TankTrouble.ttf` is not the editor title face.** Falsifier: a
native-resolution editor frame whose title is visibly black display type — which
would also contradict A's measurement, so it would take two independent reversals.

#### Three faces, not two — reconciling the ratios

`[MEASURED]` Bringing every x-height/cap-height figure in this project's evidence
into one table:

| # | Face | source | x/cap | weight |
|---|---|---|---|---|
| 1 | **editor title face** | analyst A, from a genuine editor screenshot | *(not published as a ratio)* — Arial/Helvetica class, Verdana + Tahoma excluded | text weight |
| 2 | **wiki-corpus face** | `I-weapon-toggle-panel.webp` title (cap 19 px) and `I-laika-boss-artwork.webp` caption (cap 43 px) | **0.684** and **0.698** | text weight |
| 3 | **`TankTrouble.ttf`** | `OS/2` design metrics; rasterised check | **0.7848** design (0.79–0.84 rasterised) | **display weight, stem/cap 0.316** |

`[MEASURED]` Face 2's two samples agree to within 2 % across a 2.3× size
difference, so they are one face. `[MEASURED]` Face 3's design ratio 0.7848 is
**15 % above** face 2's, and its rasterised ratio at both 19 px and 43 px cap
(0.842, 0.791) never comes near it. `[MEASURED]` Face 3 is also 17 % wider than
face 2 at matched cap height, and vastly heavier.

`[INFERRED]` **The corpus demonstrably holds at least three distinct typefaces,
and they must not be conflated:** the editor title face (1), the face in the
wiki-derived images (2), and `TankTrouble.ttf` (3). Face 3 is excluded from being
face 1 (weight/width/terminals) **and** from being face 2 (measured width, x/cap,
weight). Falsifier for the 2-vs-3 exclusion: a demonstration that WebP
recompression systematically shrinks measured x-height — it does not, because it
blurs edges symmetrically and I thresholded both samples identically.

`[UNCERTAIN]` What face 2 *is* remains open. It is not face 3, not Arial, not
Helvetica, not Verdana, not Calibri. That is five exclusions and no identification.

#### Provenance — toward authenticity

This is where the earlier revision of this document was wrong, and the correction
is substantial.

`[MEASURED]` The name table names **`Mads Purup`** (id 9) and **`www.purup.com`**
(id 12). `[MEASURED]` I verified against held bytes and sibling documents rather
than taking that at face value:

* `srv/index.php:329`, verbatim:
  `Copyright <a href="http://www.purup.com" target="_blank" style="text-decoration: none;">www.purup.com</a> 2007 &ndash; 2018`
  — the era footer, in the held page, pointing at the same domain.
* Sibling [E — front-page chrome](./E-front-page-chrome.md) transcribes the footer
  from era frames at its lines 881-882, 1023-1024, 198, 368 and 1149 as
  `Copyright www.purup.com 2007 – <year>` plus
  `Design: Mads Purup, Programming: Brian Bunch Christensen, Server: Søren Boll Overgaard`.
* Sibling [F — gameplay HUD and chat](./F-gameplay-hud-and-chat.md) transcribes
  the same two lines from its own frames at lines 946-947, 338 and 1033-1034.
* Sibling [H — ranks](./H-ranks.md) transcribes them again at lines 397-398.
* `DEDUCE.md:430` independently identifies `purup.com` as *"the developer's own
  site"*.

`[MEASURED]` So three sibling analysts, working from different frames, transcribed
the same credit line naming the same designer and the same domain that this font's
name table names.

`[INFERRED]` **`TankTrouble.ttf` is first-party TankTrouble/Purup material.** It is
not fan-made, not a renamed retail face, not a community reconstruction. Falsifier:
evidence that the name table was forged, or that a third party wrote `Mads Purup`
into a font he did not make — neither of which has any support and both of which
are far-fetched given the hinting quality and the FontLab production signature.

**This supersedes what I wrote before.** The earlier revision offered
"fan-made" as a live and *worse* possibility and framed the quarantine partly on
that basis. That framing was wrong and is withdrawn. The correct framing is:

> **Authenticated as first-party — but not evidenced as a classic-era served
> asset.**

`[OBSERVED]` One further detail that cuts *against* over-reading the credit match,
which I record because it is inconvenient: sibling E's finding 31 records that the
`Design: Mads Purup, …` credits line is present in 2013 and 2015 frames and
**absent by 2016**, and `[MEASURED]` `grep -c -F "Mads" srv/index.php` returns
**0** — the era pages carry only the `www.purup.com` copyright line, not the
credits. So the *credits line itself* is a pre-2016 feature. That does not weaken
the identification (Purup remained the designer regardless), but it means the
credit-line match cannot be used to date the font.

#### Provenance — against classic-era use

`[MEASURED]` Everything established in the earlier revision still stands, unchanged
and unweakened by the name table:

1. **No ledger row.** `grep -n -i "TankTrouble.ttf" LEDGER.tsv` → no match,
   exit 1. `grep -c "\.webp" LEDGER.tsv` → 0 (for context: nothing from this
   manual-evidence run is ledgered).
2. **`c64` is the only webfont family in the reconstruction.**
   `grep -n -i -E "\.(ttf|woff2?|eot|otf|svg)\b" LEDGER.tsv` returns exactly four
   rows: `srv/includes/c64.eot` (167, `O`), `srv/includes/c64.ttf` (168, `O`),
   `srv/includes/c64.woff` (169, `O`) and `srv/images/facebookLogoWhite.svg` (84).
   `DEDUCE.md:189`'s recovered includes-tree listing likewise ends
   `c64.eot  c64.ttf  c64.woff` — **one family**.
3. **No `@font-face` in the held page.** `grep -n "@font-face" srv/index.php` → 0.
   The only font declaration in 812 KB is `font-family: Courier`, ten times
   (lines 538, 2123, 4702, 7819, 8219, 8224, 10680, 12399, 13948, 15404).
   `Verdana`, `Arial`, `Tahoma`, `Helvetica`, `sans-serif`, `Roboto`, `c64` and
   `commodore` all return **0**.
4. **`srv/index.php:6657`**, news item *Online BETA Development Report*, anchor and
   date `25-05-2016` (verified at lines 6646-6650), verbatim:
   *"Numerous other updates have been installed too; like in-game garage access
   with instant tank updating, a weapons stack display, **a custom TankTrouble
   font**, and a completely redesigned sign-up process. That, and many more goodies
   are now ready for testing on `https://beta.tanktrouble.com`."* Duplicated into
   the Facebook share payload at `:6664`, so not an archive typo.

`[OBSERVED]` And point 4 now lines up **uncomfortably well** with the bytes: the
font's copyright year is **2016**, its uniqueID is `TankTrouble: TankTrouble: 2016`,
and it is `Version 2.000` — a second cut. A custom TankTrouble font, version 2,
copyrighted 2016, announced as a BETA feature in May 2016. `[INFERRED]` that is a
coherent story and it is the single most likely one. Falsifier: a
`tanktrouble.com` CDX row for these bytes.

`[NOT VISIBLE]` **I still could not check the stylesheets.** Only `srv/index.php`
is staged from `srv/`; `styles.css`, `boxStyles.css`, `newsStyles.css`,
`forumStyles.css` and `shopStyles.css` are not. My "no `@font-face`" result is
limited to `index.php` and must not be over-read. The want-list's own S17 citation
(`styles.css:86-93`) shows those files have been read and yielded exactly one
`@font-face` family — `Commodore`/`c64` — so a second one naming TankTrouble would
almost certainly have surfaced. `[INFERRED]` there is none, but this is **unclosed**,
and `grep -n "@font-face" srv/includes/*.css` closes it in one command.

#### Verdict

Revised, and stated so both halves survive:

> **`TankTrouble.ttf` is authenticated first-party material and is not evidenced as
> a classic-era served asset.** Both clauses are load-bearing.
>
> *Authenticated:* the name table names `Mads Purup` and `www.purup.com`, the
> designer and domain that three sibling analysts independently transcribed from
> the classic site's own footer and that `srv/index.php:329` still carries. The
> production quality (full hinting, `hdmx`/`LTSH`/`VDMX`, 392 kern pairs, FontLab
> pipeline) is professional. `fsType = 0` means there is no licensing obstacle.
> **The "fan-made" hypothesis is dead** and my earlier framing of it is withdrawn.
>
> *Not evidenced as served:* no ledger row, no `@font-face` in the held page, no
> CDX row, and exactly one webfont family (`c64`) in the recovered includes tree.
> The only developer statement about a "custom TankTrouble font"
> (`srv/index.php:6657`, `25-05-2016`) places it in **Online BETA** — and the
> font's own 2016 copyright, `Version 2.000` and 2016 uniqueID fit that statement
> closely.
>
> *Unresolved, deliberately:* `head.modified` **2017-11-02** falls **inside** the
> 2017–2018 target window; `head.created` **2013-09-28** falls well before the
> BETA announcement; the copyright year **2016** falls between them and matches the
> announcement. **These pull in opposite directions and this document does not
> pick a side.** A file being touched inside the target window is not evidence it
> was served by the classic site inside the target window — but it is not nothing
> either, and pretending otherwise would be the same error in the other direction.
>
> **Disposition: hold, do not adopt, do not serve.** Not for the editor title
> (ruled out on weight, width and terminals — §above), not for page chrome (no
> `@font-face` asks for it), not as a substitute for `_sans`. The bar for adoption
> is *evidence of use*, and authenticity is not that evidence.
>
> The practical difference from the earlier revision: this is now worth **actively
> chasing** rather than merely fending off. First-party bytes with a plausible
> BETA attribution and one unexplained in-window timestamp are a lead, not a
> contaminant.

#### What would establish use (the falsification list, re-ordered by cost)

1. **`grep -n "@font-face" srv/includes/*.css`** and read every family name.
   One command; the project already has the files.
2. **A CDX sweep** for `.ttf` / `.woff` / `.woff2` / `.eot` under
   **`tanktrouble.com`** in 2017–2018 — and the same sweep under
   **`beta.tanktrouble.com`**, which would close it in the negative just as fast.
3. **The download URL** from the repo owner's browser history. The file was saved
   at 16:35:38, four minutes after the wiki run ended; the host is decisive and
   costs one lookup.
4. **A coverage match against captured pixels** — this is the new one, and the
   font's own fingerprint makes it cheap. Find any era surface that renders a
   **box rule or frame** (candidates for `U+2500`–`U+250F`), an **arrow-key hint**
   (`U+2190`–`U+2193`) or a **star** (`U+2605`), then compare the rendered glyph
   against this font at the same cap height. A hit would be strong; the box-drawing
   set in particular is not something two unrelated fonts would share by accident.
5. **A v1.x copy of the same family.** `Version 2.000` implies one existed. A v1
   with a pre-2016 copyright would substantially change the reading of the 2013
   `head.created`.

#### Consequences for the three open typography entries

**VE entry 7 — Title + watermark typography (PARTIAL)** — `[INFERRED]` **stays
`PARTIAL`.** This font does **not** answer it and must not be quietly adopted for
it: it is ruled out as the editor title face on weight (stem/cap 0.316 vs the
Arial/Helvetica class's 0.105–0.158), width (17 % wider than the wiki-corpus face
at matched cap height) and terminal treatment. The entry should gain a
"candidates ruled out" line naming it, with the reason, so nobody re-proposes it.

**S108 — Editor title font: device vs embedded (LOW)** — `[INFERRED]` **stays
`WANTED`**, with the same cheap narrowing as before, now sharpened: the classic
includes tree holds exactly one embedded family (`c64`) and this newly-inspected
font is not referenced by any held byte, so **no page-side embedded UI sans is in
evidence at all**. If the editor title were embedded, its bytes would be **inside
the editor SWF**, which makes a `DefineFont`/`DefineFont2` decompiler check the
direct answer — no native-scale frame required.

**S17 — `Commodore` (c64) webfont in the wild (LOW)** — `[NOT VISIBLE]`, **stays
`WANTED`, untouched.** Nothing in my eleven files shows a blocky pixel font.
`TankTrouble.ttf` is emphatically not it — it is a heavy display sans with smooth
outlines and 392 kern pairs, nothing like a C64 bitmap face. One clarification the
entry deserves: all three `c64` format files are held **`O`** (LEDGER 167/168/169),
so the *bytes* are safe and only the on-screen *rendering* is unobserved.

#### What this does NOT show

* `[NOT VISIBLE]` **Where the file came from.** No URL, no host, no archive path.
  The name table proves *authorship*, not *distribution*. This remains the single
  most valuable missing datum in my assignment and the owner can supply it from
  browser history in seconds.
* `[NOT VISIBLE]` **Whether any TankTrouble surface ever rendered it.** Not one
  pixel in this corpus is set in this face — I checked: the `I-weapon-toggle-panel.webp` title
  and the `I-laika-boss-artwork.webp` caption are both measurably a different face, and the seven
  weapon icons contain no text at all.
* `[NOT VISIBLE]` **What `Version 1.x` looked like**, or whether it had a different
  copyright year — which is exactly what would make the 2013 `head.created`
  interpretable.
* `[NOT VISIBLE]` **Any `beta.tanktrouble.com` asset listing** that would confirm
  or refute the BETA attribution directly.
* `[NOT VISIBLE]` **Whether a `.woff`/`.woff2`/`.eot` sibling exists.** A web
  deployment in 2016–2018 would almost certainly ship WOFF; a bare `.ttf` is what
  you get from a *desktop* install or a direct file grab. `[UNCERTAIN]` that mildly
  favours "the owner downloaded a font file" over "the owner extracted a served
  webfont", but a `.ttf` can be served directly and often was.

## Consequences for the rebuild

### Confirmed

1. **The classic game had a per-weapon enable/disable settings menu, reached by a
   gear during play, from 2008-12-16.** `[MEASURED]` from held page bytes
   (`srv/index.php:9969`, `:9974`, `:9976`, corroborated at `:10010` and `:9707`).
   This is confirmed *by original-derived bytes*, independent of the screenshot.
   It is a real user-facing surface that appears **nowhere** in the S1–S114 sweep.
2. **The classic weapon roster is seven.** `[MEASURED]` Seven icons, seven panel
   labels, and `weapons.txt`'s eighth entry (Shotgun) self-identifies as Beta-only
   with no infobox image. Three independent lines, same answer.
3. **The weapon crate is a square plate, ~22×22 native px, rendered rotated.**
   `[MEASURED]` seven fitted squares of side 43.0–44.2 capture px at seven
   different angles. The rotation is real behaviour; the specific angles are not
   constants.
4. **The crate art is strictly greyscale in this source** — R==G==B for
   7560/7560 px in all seven files, glyph floor exactly `#333333`, matte exactly
   `#e6e6e6`, no alpha. `[MEASURED]`
5. **Seven distinct crate glyph designs** are now described: 6-dot ring
   (Gatling Gun), solid bell/mine blob (Booby Trap), S-squiggle (Laser), 3
   horizontal bars (Death Ray), concentric arcs + dot (RC Missile), notched dart
   (Homing Missile), 6-point burst (Frag Bomb). `[OBSERVED]`
6. **Laika's single glowing red eye is canonical.** `[MEASURED]` the illustration
   shows it at x 186..203, y 77..96, and two **held `O`** shop assets independently
   name it in their filenames (`shopBlackTShirtWith**RedEye**YellowLaikaOnFront.jpg`,
   `shopWhiteTShirtWith**RedEye**BlackLaikaOnFront.jpg`, LEDGER 122/125).
7. **`srv/index.php:9826` is exactly as S103 describes it** — plus two details S103
   omits: `wmode="transparent"` and `top: -60px`, i.e. a 60 px overhang above the
   news content box. `[MEASURED]`
8. **A "custom TankTrouble font" is a documented Online BETA feature, May 2016.**
   `[MEASURED]` `srv/index.php:6657` (news anchor and date verified at `:6646-6650`).
9. **`TankTrouble.ttf` is first-party Purup material.** `[MEASURED]` name id 9 =
   `Mads Purup`, id 12 = `www.purup.com`; the same designer and domain that
   siblings [E](./E-front-page-chrome.md), [F](./F-gameplay-hud-and-chat.md) and
   [H](./H-ranks.md) transcribe from era footers and that `srv/index.php:329`
   still carries. Fully hinted (`fpgm`/`prep`/`cvt `/`hdmx`/`LTSH`/`VDMX`), 392
   kern pairs, `fsType = 0`. **The "fan-made" hypothesis is dead.**
10. **It is a third, distinct typeface.** `[MEASURED]` x/cap **0.7848** design,
    stem/cap **0.316**, `Weapons` **17 % wider** than the captured panel title at
    matched cap height — matching neither the wiki-corpus face (0.684 / 0.698) nor
    the Arial/Helvetica-class editor title face. At least three faces are in play
    across this project's evidence and must not be conflated.

### Contradicted — overhaul owed

**Nothing in the rebuild is contradicted by this evidence, and no overhaul is
owed.** Stated explicitly because the brief asks for it directly:

* The weapon crates, the weapons themselves, Laika and the in-game settings menu
  are **not implemented anywhere** in the reconstruction — they live inside
  `TankTrouble_v4.0.swf` (held `O`), which the project serves as original bytes
  rather than reimplementing. There is no M2/M3 invention here to supersede.
* `docs/standards/MAZECREATOR-VISUAL-SPEC.md` is **untouched**. Its *Crate spawn icon* row
  describes the editor's 16×16 amber placement marker, a different object from the
  22×22 grey in-play crate measured here. Neither reading challenges the other.
* VE entry 7's `_sans` placeholder is **not** superseded — see the font section. If
  anything this evidence *protects* it by naming a candidate that must not replace
  it.

One thing **this document contradicts is an earlier revision of itself**, and the
OVERHAUL RULE's spirit says to say so rather than quietly patch: an earlier draft
recorded `TankTrouble.ttf` as unreadable and offered "fan-made" as a live and worse
possibility, framing its exclusion partly on that. The bytes refute it — the font
is first-party Purup material. **That framing is withdrawn wholesale, not patched.**
The exclusion survives, but on entirely different and much narrower grounds:
*authorship is settled, deployment is not.*

Two **defects in project hygiene** are exposed, which is a different thing from a
contradiction:

* **`I-icon-rc-rocket.webp` is an unledgered foreign binary at the repository root, and
  gate D's documented walk (`srv/` only) would not find it.** Both the file and the
  gate need fixing.
* **S103 is under-scoped** — it names `laika02.swf` but not `srv/Assets/Laika.swf`
  (LEDGER 4, held `O`), which is the *game* Laika and equally unverified.

### Still unknown / stays on the want-list

| Entry | Status after this evidence | Why |
|---|---|---|
| **S103** — `laika02.swf` behaviour | **stays `WANTED`** | A still illustration with a **0.781** aspect cannot verify a **0.560** SWF stage, and eye-matching wiki art to an SWF render is exactly the weak move the brief forbids. **But**: both SWFs are held `O`, so S103 is blocked on *effort*, not material. |
| **S108** — editor title font | **stays `WANTED`** | No native-scale editor frame in my files. Narrowed, not closed: the includes tree holds exactly one embedded family (`c64`, a pixel face), which makes "device font" the strong prior and suggests a decompiler check for `DefineFont` in the editor SWF. |
| **S17** — `Commodore`/c64 in the wild | **stays `WANTED`, untouched** | `[NOT VISIBLE]` — no blocky pixel font anywhere in my eleven files. Recording the null result. |
| **VE 7** — title/watermark typography | **stays `PARTIAL`** | Unchanged as to the *answer*. Gains a measured **exclusion**: `TankTrouble.ttf` is ruled out (stem/cap 0.316 vs the Arial/Helvetica class's 0.105-0.158; `Weapons` 17 % wider than the wiki-corpus title at matched cap height). Its foot-bar-free `1` agrees with sibling A's test but is non-discriminating at this weight. |
| **S116 (new)** — was `TankTrouble.ttf` ever served? | **opens as `WANTED`** | Authorship is **closed** (first-party Purup, name ids 9/12, corroborated by siblings E/F/H and `srv/index.php:329`). Deployment is wide open: no ledger row, no `@font-face`, no CDX row, one webfont family (`c64`) in the includes tree, and `srv/index.php:6657` pointing at Online BETA. `head.modified` 2017-11-02 sits inside the target window and is **not** reconciled. |
| **S102** — era game-SWF audio | **stays `WANTED`** | Art, not audio. Gains a seven-item target roster to check sounds against. |
| **S114** — unnamed/unknown UI | **should shrink** | The weapons settings panel is exactly what S114 says to look for (*"Any on-screen control in era footage that maps to nothing in this document = a find"*). Promote it out of S114 into its own entry. |

Still missing after these eleven files, concretely:

* the **gear button** that opens the settings menu;
* the rest of the settings menu (mazes section, per `srv/index.php:9974`);
* the **opposite toggle state**;
* the crate at **gameplay scale**, next to a wall or tank, so 22 native px can be
  converted to stage px;
* **crate animation** (spin? bob? fade-in?) and the pickup transition;
* the **Shotgun** crate art (may not exist for the classic build at all);
* **any** Laika animation frame;
* provenance metadata — **URL, uploader, date, timestamp** — for every one of these
  eleven files. Without it none of them can be ledgered per guide §6.5. For
  `TankTrouble.ttf` the sha256 is now recorded
  (`b5cf704099dc54ac37ec05fc8b6d9d5daa98fda13488e6c04adaf2cbddc13ed0`), so only the
  URL/date half is missing;
* **any evidence that `TankTrouble.ttf` was ever served**, by either generation —
  an `@font-face`, a CDX row, or a rendered glyph match. Authorship is settled;
  deployment is not.

### New wants to add

**NEW — In-game settings menu: weapons section** *(category: page-look / flow;
recommendation: HIGH)*

* *What exists*: `I-weapon-toggle-panel.webp` (this corpus, M2, wiki-derived, generation
  unconfirmed) — seven pill toggles in two columns, column-major, labels
  transcribed verbatim above. Feature confirmed by held bytes.
* *Evidence pointer*: `srv/index.php:9969-9977` (news `16-12-2008`, *Customize Your
  Battles*), `:10010` (news `06-11-2008`), `:9707` (second gear mention).
* *Footage trigger*: **click the gear during a battle** — the menu pops up when the
  round ends. Any local-multiplayer video where a player changes weapon settings.
  A frame with at least one toggle in the *other* state is worth more than ten more
  frames of this one.
* *What it would replace/confirm*: nothing is built; it would establish that a
  whole in-game surface exists, its layout, and its era.

**NEW — Era evidence for the weapon-toggle panel** *(category: provenance;
recommendation: HIGH)*

The narrower, sharper version of the above. The panel's *feature* is confirmed
in-era; its *rendering* is not. Needed: a **dated** frame of it — browser chrome, a
username, a seasonal skin, an ad creative, a visible year, or a
`beta.tanktrouble.com` URL bar. Any one settles whether these pixels are classic or
BETA. Until then the crop is **quarantined: cite the feature, do not build the
pixels.**

**NEW — `TankTrouble.ttf`: was it ever served, and by which generation?**
*(category: typography / provenance; recommendation: MED)*

**Re-scoped.** The old question — *who made this?* — is **answered and closed**.
The open question is **deployment**.

* *What is settled* `[MEASURED]`: first-party Purup material (name id 9
  `Mads Purup`, id 12 `www.purup.com`, matching the era footer credits transcribed
  by siblings E/F/H and the `www.purup.com` link still in `srv/index.php:329`).
  114 092 bytes, sha256
  `b5cf704099dc54ac37ec05fc8b6d9d5daa98fda13488e6c04adaf2cbddc13ed0`. Family
  `TankTrouble`, `Version 2.000`, copyright 2016, upem 1000, 211 glyphs, 392 kern
  pairs, fully hinted, `fsType = 0` (no licensing bar). A heavy irregular display
  sans — **ruled out** as the editor title face on weight, width and terminals.
* *What is open*: **was it ever served, and by what surface?** No ledger row, no
  `@font-face` in `srv/index.php`, no CDX row; the classic includes tree holds
  exactly one webfont family (`c64`, LEDGER 167-169, all three formats `O`); and
  `srv/index.php:6657` (news `25-05-2016`) attributes "a custom TankTrouble font"
  to **Online BETA**, matching the font's own 2016 copyright and `Version 2.000`.
* *The unresolved tension* `[MEASURED]`, to be carried in the entry and **not**
  resolved by preference: `head.created` **2013-09-28**, copyright **2016**,
  `head.modified` **2017-11-02** — the last falls *inside* the 2017-2018 target
  window, the first two do not.
* *What is needed, in cost order*: (1) `grep -n "@font-face" srv/includes/*.css`;
  (2) a CDX sweep for `.ttf`/`.woff`/`.woff2`/`.eot` under **`tanktrouble.com`**
  *and* under **`beta.tanktrouble.com`** — either result closes it; (3) the
  **download URL** from the owner's browser history; (4) **a glyph match against
  an era UI**, using the coverage fingerprint below; (5) a `Version 1.x` copy,
  which would make the 2013 `head.created` interpretable.
* *The fingerprint that makes (4) cheap* `[MEASURED]`: coverage is 95 ASCII + 94
  **Latin-1 Supplement only** (no Latin Extended at all) + arrows
  **U+2190-2193** + box-drawing **U+2500-250F** (sixteen, contiguous) + **U+2605
  BLACK STAR**. Sixteen box-drawing glyphs are not added by accident — something
  drew boxes with them. **Any era surface that renders a box rule or frame, an
  arrow-key hint, or a star is a candidate site**, and a glyph match there would be
  strong evidence of use.
* *Disposition until then*: **hold — keep bytes, ledger nothing, serve nothing,
  adopt nowhere.** Note this is *hold*, not *quarantine*: the bytes are
  authenticated first-party material and are worth actively chasing, not merely
  fending off.

**NEW — Weapon crate appearance (`srv/Assets/Crate.swf`)** *(category: SWF /
icon-state; recommendation: MED)*

`Crate.swf` is held `O` (LEDGER 2) and its on-screen appearance is nowhere in the
S1–S114 sweep, despite being one of the most-seen objects in the game. This corpus
now gives seven glyph designs and a 22×22 native plate to check a render against.
*Needed*: render `Crate.swf` and compare — colour (is the grey real?), plate size in
stage px, rotation behaviour, and whether all seven glyphs are inside this one SWF
or one SWF per weapon.

**NEW — `srv/Assets/Laika.swf` behaviour** *(category: SWF; recommendation: MED)*

The sibling S103 does not cover. Held `O` (LEDGER 4), never verified, and it is the
*game* boss rather than the news-item ornament. Should be its own entry or S103
should be widened to name both.

**NEW — Wiki-dump reconciliation** *(category: provenance; recommendation: HIGH,
near-zero cost)*

LEDGER row 324 already records
`archive/wiki-dumps/tt-game-wiki/images/LaikaSmall.jpg` in the archive. `[INFERRED]`
that dump is plausibly the source of this entire capture run. **Check whether
`archive/wiki-dumps/tt-game-wiki/images/` already contains un-upscaled originals of
`I-laika-boss-artwork.webp` and the seven weapon icons.** If it does: better bytes, real
filenames, and possibly real provenance metadata, for the cost of one directory
listing. This single action could retire most of the resolution caveats in this
document.

---

## Recommended edits to existing docs (not applied)

Per the brief I have edited **no** repo file. These are proposals.

### 1. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — widen S103

**Change:** keep status `WANTED`; rewrite the "What exists / what's missing" cell.

> *from* — `Held O, embedded once at 140×250 in a news item; never verified`
> *to* —
> Two held-O Laika SWFs, neither verified: **`includes/laika02.swf`** (news
> ornament, embedded once at 140×250, `wmode=transparent`, `top:-60px` so 60 px
> overhangs the content box) and **`Assets/Laika.swf`** (the game boss, LEDGER 4).
> Blocked on effort, not material — both are already held. A wiki illustration
> (manualevidence, M2) shows the character (grey husky on a tank, single glowing
> red eye, exposed red/blue wiring) but its 325×416 artwork bbox has aspect 0.781
> vs the embed's 0.560, so it does not verify either SWF.

**Also change** the Evidence-pointer cell from `srv/index.php:9826` to
`srv/index.php:9822-9843; LEDGER 4,176`.

**Why:** `[MEASURED]` `grep -n "laika" LEDGER.tsv` returns six rows; the entry names
one. `srv/Assets/Laika.swf` (row 4, `O`) is unverified and unmentioned.

### 2. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — add a new entry for the settings menu

Add to section **A** (or wherever in-game surfaces belong), status `PARTIAL`:

```
| S115 | **In-game settings menu — weapons section** | page-look / flow | Feature proven by held bytes: gear during play opens a menu that selects **which weapons appear** (news 16-12-2008) and maze type. One M2 wiki-derived crop (`manualevidence/Game/I-weapon-toggle-panel.webp`) shows 7 pill toggles in 2 columns, column-major, labels `Laser / Frag bomb / Death ray / RC missile / Gatling gun / Homing missile / Booby traps`, knob `#cccccc`, track `#00ff00`, page `#ffffff`, row pitch 27-28px, column pitch 177px — but the frame is **undated** and its typeface is measurably outside the classic Verdana/Arial family, so the *rendering* is unconfirmed. | `srv/index.php:9969-9977`, `:10010`, `:9707`; `manualevidence/I-weapons-and-laika.md` | Click the gear mid-battle; menu pops up at round end. **A frame with a toggle in the opposite state is worth more than another frame of this one.** | HIGH |
```

**Why:** `[MEASURED]` a whole in-game surface with zero coverage in S1-S114. S114's
own instruction (*"Any on-screen control in era footage that maps to nothing in
this document = a find"*) says to promote it.

### 3. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — add `TankTrouble.ttf` deployment

Note the scope: authorship is **settled**, so the entry must ask about *use*, not
about *origin*. An entry phrased as "who made this" would be closed on arrival and
would mislead.

```
| S116 | **`TankTrouble.ttf` — was it ever served?** | typography / provenance | **Authorship settled**: first-party Purup material (name id 9 `Mads Purup`, id 12 `www.purup.com` — the designer and domain of the era footer credits, cf. `srv/index.php:329`). 114 092 B, sha256 `b5cf7040…c13ed0`, family `TankTrouble`, `Version 2.000`, copyright 2016, upem 1000, 211 glyphs, 392 kern pairs, fully hinted, `fsType=0`. A **heavy irregular display sans** — ruled out as the editor title face on weight/width/terminals. **Open**: no ledger row, no `@font-face` in `srv/index.php`, no CDX row; the includes tree holds only `c64` (LEDGER 167-169); `srv/index.php:6657` attributes "a custom TankTrouble font" to **Online BETA** (25-05-2016), matching the font's 2016 copyright + v2. **Unresolved tension**: `head.created` 2013-09-28 / copyright 2016 / `head.modified` **2017-11-02 (inside the target window)** pull opposite ways — do not resolve by preference. Disposition: **hold, do not adopt, do not serve.** | `srv/index.php:6657`, `:329`; LEDGER 167-169; `manualevidence/I-weapons-and-laika.md` | Not footage. (1) `grep @font-face srv/includes/*.css`; (2) CDX sweep for `.ttf`/`.woff`/`.eot` under **tanktrouble.com** *and* **beta.tanktrouble.com**; (3) the download URL; (4) **glyph match against any era UI drawing a box rule/frame, an arrow-key hint, or a star** — coverage is ASCII + Latin-1 only + arrows U+2190-2193 + box-drawing **U+2500-250F** + **U+2605 ★**, an unusual signature; (5) a `Version 1.x` copy | MED |
```

### 4. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — entry 7, add a ruled-out line

Append to entry **7. Title + watermark typography — PARTIAL**:

> *Ruled out:* **`TankTrouble.ttf`** (manual-evidence 2026-08-04). It is genuine
> first-party Purup material — name table designer `Mads Purup`, designerURL
> `www.purup.com` — so it will look like the obvious answer. **It is not.**
> Measured: a heavy irregular display sans, stem/cap **0.316** against the
> Arial/Helvetica class's 0.105-0.158, rendering `Weapons` **17 % wider** than the
> captured wiki-corpus title at matched cap height, with angled cut terminals and
> an intentionally unsteady baseline — unusable as 12-18 px UI text. Its digit `1`
> does have **no foot bar** and so passes the Verdana/Tahoma exclusion test, but
> that agreement is **non-discriminating**: a foot bar is stylistically impossible
> in a face of this weight, so passing proves nothing. **Do not adopt.**
>
> *Three distinct faces are now in evidence and must not be conflated:*
> (1) the **editor title face** — Arial/Helvetica class, Verdana + Tahoma excluded
> (sibling A, from a genuine editor screenshot); (2) the **wiki-corpus face** —
> `I-weapon-toggle-panel.webp` title and `I-laika-boss-artwork.webp` caption, x/cap **0.684** and **0.698**,
> below Arial (0.789), Helvetica (0.737) and Verdana (0.737), identity unknown;
> (3) **`TankTrouble.ttf`** — x/cap **0.7848** design, display weight. (3) is
> excluded from being (1) and from being (2) on measured grounds.

### 5. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — S108, record the cheap narrowing

Append to the S108 "What exists" cell:

> Narrowing available without footage: the recovered includes tree holds **exactly
> one** embedded family (`c64`, a blocky pixel face used by `.box.glitch` and two
> news rules) — no UI sans is embedded page-side. If the editor title were an
> embedded font its bytes would be **inside the editor SWF**, so a decompiler check
> for a `DefineFont`/`DefineFont2` tag answers "device vs embedded" directly and
> does not need a native-scale frame.

### 6. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — S17, clarify what is missing

Append to the S17 "What exists" cell:

> All three format files are held **`O`** (LEDGER 167/168/169) — the *bytes* are
> safe; only the on-screen *rendering* is unobserved. Null result recorded
> 2026-08-04: the eleven-file weapons/Laika manual-evidence set contains **no**
> blocky pixel font (`manualevidence/I-weapons-and-laika.md`).

### 7. `README.md` / `docs/standards/ASSET-DISCIPLINE.md` — widen gate D's walk

`README.md` currently describes gate D as *"every `srv/` file has a ledger row"*;
`docs/standards/ASSET-DISCIPLINE.md:21` phrases the gate-D question as *"does every file
under `srv/` have a row?"*.

**Proposed change:** extend gate D to walk the **repository root and any
non-source directory**, not only `srv/`, for foreign binaries — or add a small
companion check ("no unledgered binary anywhere outside `archive/`,
`archive-cleaned/` and `.git/`").

**Why:** `[MEASURED]` `I-icon-rc-rocket.webp` (658 bytes, wiki-derived, M2-at-best) has
been sitting at `websites/Game/I-icon-rc-rocket.webp` with **no ledger row**, and
gate D as documented **does not look there**. The README's own gate-E rationale —
*"without E a byte-perfect page serving zero images passes all three, which is
exactly what happened"* — is the same species of blind spot. This one is cheaper
to close.

**Immediate remedial action (independent of the gate change):** move
`I-icon-rc-rocket.webp` into `manualevidence/Game/` with its six siblings. Do not ledger
it yet — no URL/uploader/date/timestamp is available for any file in this run, and
guide §6.5 requires all four.

### 8. `DECISIONS.md` — append two entries

Neither is applied; both are proposals for the append-only log.

> **`weapons-roster-is-seven`** — The classic weapon roster is **seven**, not
> eight. Evidence: seven crate icons in the 2026-08-04 manual-evidence run; seven
> labels in the settings-panel crop; and `weapons.txt` (community wiki, "as of 28th
> February 2013") whose eighth entry, **Shotgun**, self-identifies as *"can be
> found in the Tank Trouble Beta"* and is the **only** section in the article with
> no infobox-image caption line. Three independent lines agree. Source is M2
> (wiki-derived), quarantined for provenance, but the roster claim is
> triangulated.

> **`tanktrouble-ttf-authenticated-not-adopted`** — `TankTrouble.ttf` (114 092 B,
> sha256 `b5cf704099dc54ac37ec05fc8b6d9d5daa98fda13488e6c04adaf2cbddc13ed0`)
> arrived in the 2026-08-04 manual-evidence run and was inspected with fontTools.
> **It is authentic first-party material and it is still not adopted.** Those are
> separate findings and both are recorded.
> *Authentic:* name id 9 = `Mads Purup`, id 12 = `www.purup.com` — the designer and
> domain of the classic footer credits (`srv/index.php:329`; era transcriptions in
> `manualevidence/E-front-page-chrome.md`, `F-gameplay-hud-and-chat.md`,
> `H-ranks.md`). Family `TankTrouble`, `Version 2.000`, copyright 2016, upem 1000,
> 211 glyphs, 392 kern pairs, fully hinted, `fsType = 0`. Any earlier suggestion
> that this might be fan-made is **withdrawn**.
> *Not adopted:* no ledger row, no `@font-face` in `srv/index.php`, no CDX row, and
> the recovered includes tree holds exactly one webfont family (`c64`, LEDGER
> 167-169). `srv/index.php:6657` (news `25-05-2016`) attributes "a custom
> TankTrouble font" to **Online BETA**, which matches the font's own 2016 copyright
> and `Version 2.000`. Authorship is not evidence of deployment.
> *Recorded unresolved:* `head.created` **2013-09-28**, copyright **2016**,
> `head.modified` **2017-11-02** — the last falls **inside** the 2017-2018 target
> window, the first two do not. **This decision does not resolve that tension**;
> it records it so a later reader does not mistake silence for agreement.
> *Also recorded:* the font is a **heavy irregular display sans** (stem/cap 0.316,
> `Weapons` 17 % wider than the captured wiki-corpus title at matched cap height)
> and is **ruled out as the editor title face**, which sibling A measured as
> Arial/Helvetica class. Its foot-bar-free digit `1` agrees with A's test but is
> non-discriminating at this weight and must not be cited as support.
> *Disposition:* hold — keep bytes, ledger nothing, serve nothing, adopt nowhere.
> Revisit on a `tanktrouble.com` CDX row, a held-CSS `@font-face`, a
> `beta.tanktrouble.com` match, or a measured glyph match against an era UI (see
> the U+2500-250F / U+2605 coverage fingerprint in S116).

### 9. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — add the crate and the wiki-dump check

Two more one-line additions, both cheap and both HIGH value per unit effort:

```
| S117 | **Weapon crate appearance (`Assets/Crate.swf`)** | SWF / icon-state | Held **O** (LEDGER 2) and absent from this document until now, despite being one of the most-seen objects in the game. M2 wiki icons give 7 glyph designs and a ~22×22 native-px rotated plate to check a render against. | LEDGER 2; `manualevidence/I-weapons-and-laika.md` | Render `Crate.swf`; also any in-play frame showing a crate beside a wall (gives stage-px scale) | MED |
```

> **Action, not an entry:** list `archive/wiki-dumps/tt-game-wiki/images/`. LEDGER
> 324 already records that directory. If the un-upscaled originals of `I-laika-boss-artwork.webp`
> and the seven weapon icons are in it, most of the resolution caveats in this
> document retire for the cost of one `ls`.
