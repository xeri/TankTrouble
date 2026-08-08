# Visual evidence — logged-in garage, userpanel and tank paint facility

> Analysis of 16 evidence files under `manualevidence/`.
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)

`docs/standards/VISUAL-EVIDENCE-WANTED.md` §B opens with *"Everything from
`x_updateUserPanels` / `x_getAllUserInfo` SAJAX. **Zero bytes of that HTML
archived**; only the JS survives"*. These sixteen frames are the first pixels
the project has of that surface. They resolve S24 (the panel itself) and S29
/ S30 / S31 almost completely, give S25 four of five icons, give S28 the
accept ✓ artwork, and — unexpectedly — they do **not** touch S34 at all,
because every form in this set is the **sign-up** form, not the garage
settings form. That distinction is argued in detail below.

---

## Scope and provenance

**All sixteen files are screen captures of video.** `D-garage-2018-url-bar-youtube-toast.png` settles the
question outright: it contains a Chrome full-screen toast reading
"**youtube.com** is now full screen · Exit Full Screen (Esc)" laid over the
captured browser window. `[OBSERVED]` The "browser" visible in that frame is
therefore *content inside a YouTube player*, not the capturer's own browser.
Everything in this corpus that shares that visual signature is
**YouTube footage → M2 at best, never O** (guide §6.5). I state that
explicitly because it bears on the grading of every claim below.

File mtimes are the repo owner's crop times on 2026-08-04 and are used here
**only as capture order**. Reconstructing sequence from that order is an
explicit inference, flagged where used.

The sixteen files fall into **four distinct sessions/builds** plus one
outlier. They must not be merged.

| Group | Files (capture order) | Account | Build markers |
|---|---|---|---|
| **V1** | `D-garage-kickstarter-eve-foxter25.png` 16:48:02, `D-garage-kickstarter-countdown-later.png` 16:51:42 | `Foxter25` | Windows Chrome, `www.tanktrouble.com/?garage` (http, no padlock); **5-tab** nav with a `TANKTROUBLE.com` logo (no shop tab); `.box.kickstarter` countdown in the left column; sign-up e-mail helper reads *"So you can recover your password if you forget it"* |
| **V2** | `D-paint-standard-palette-comic-overlay.png` 17:09:45, `D-paint-halloween-toolbox-comic-overlay.png` 17:10:00, `D-paint-chip-row-scrolled-one-step.png` 17:10:29, `D-paint-gold-toolbox-two-chips.png` 17:10:39 | `foxter` | No page chrome (heavily zoomed crops, ~1.8× the V1 zoom); paint facility identical in structure to V1 (four toolboxes, chip row, ◀▶ arrows); **comic speech-bubble overlays burned into the video — excluded from evidence, see below** |
| **V3** | `D-userpanel-older-build-collapsed.png` 17:12:05, `D-paint-older-build-grid-expanded.png` 17:13:50, `D-paint-older-build-grid-no-hover.png` 17:13:57, `D-paint-accessory-hover-bandana.png` 17:14:12, `D-paint-accessory-hover-pirate-hat.png` 17:14:28, `D-paint-can-hover-violet.png` 17:15:19, `D-paint-can-hover-violet-later.png` 17:15:26 | `revengexx1` | **Older build**: only **3** userpanel icons; a centred heading *"Customize your tank"* sits **above** the panel; paint facility is a **two-row grid** of 16 accessories with **no** toolboxes and **no** arrows; sign-up copy is *"Get your own tank. Sign up here"* / *"First the boring stuff…"* / *"Pick a username"* |
| **—** | `D-game-teaser-screen-not-garage.png` 17:16:14 | `_-Death-_` | Not a garage frame at all — the `?game` teaser screen |
| **V4** | `D-garage-2018-url-bar-youtube-toast.png` 17:28:41, `D-garage-2018-scrub-bar-visible.png` 17:29:27 | `mr_enderman` | `https://tanktrouble.com/?garage` (padlock); **6-tab** nav exactly matching the era-final markup at `srv/index.php:3471`; Fortnite *Season 6 Darkness Rises* skyscraper; Halloween `.box`; YouTube full-screen toast |

Two files not on my list are used **only as cross-checks** and are labelled as
such wherever they appear: `UI/C-garage-before-maze-panel.png` (topic C) is the only frame in the
corpus showing **two** userpanels side by side, which is the direct evidence
for S7; it belongs to the same build family as V1.

**Relationship between V1 and V2** — `[INFERRED]` same creator, probably the
same video. `D-garage-kickstarter-eve-foxter25.png`'s Top-10 *Friends* tab lists exactly two names,
`foxter 18510` and `Foxter25 117`; V2's account is `foxter`. The paint UI is
structurally identical. I cannot prove same-video from pixels because the crops
are at different zoom.

---

## Video-authored overlays are excluded from evidence

The four **V2** frames come from a *TankTrouble comics* video: the uploader
has burned hand-drawn comic speech bubbles over the recording, in which the
tank talks. **These bubbles are not site UI and carry no evidential weight
here.** They are not transcribed, not measured, and no finding in this
document rests on their content. Only the paint facility *behind* them is
analysed.

They still matter in one way, and only one: they **occlude** parts of the
frame. Each V2 entry below records the overlay's occlusion footprint, because
that is what bounds how much of the accessory row and the toolbox strip can be
enumerated. Where a reading would have depended on an occluded region, it is
marked `[NOT VISIBLE]` rather than guessed.

Same principle applies corpus-wide to everything the *video author* added
rather than the *site* drew — burned-in title cards, subtitle tracks,
recorder click-halos and watermarks, player chrome, picture-in-picture insets,
and standalone motion-graphic cards. [`INDEX.md`](./INDEX.md) §5 lists every
instance found across the eleven documents and which document handles it.

---

## How scale was derived — read this before trusting any CSS number

These are screen captures of video at unknown zoom, so every CSS-pixel figure
below rests on a derivation. I used two independent rulers.

**Ruler A — the menu strip.** `srv/index.php:3471` is
`<td style="width: 708px;">` — the middle cell of the nav table, containing
`menuStartDeselect.jpg` + six tabs + `menuEndDeselect.jpg`. It is a hard,
markup-declared 708 CSS px. `[MEASURED]` I isolated the raised block by
averaging rows inside the menu band and finding where the profile steps above
the darker `menuBackground.jpg` texture:

| Frame | raised block, capture px | scale if block = 708 |
|---|---|---|
| `D-garage-2018-url-bar-youtube-toast.png` | x 418 → 1389 = **972** | **1.3729** |
| `D-garage-2018-scrub-bar-visible.png` | x 474 → 1445 = **972** | **1.3729** |
| `D-garage-kickstarter-eve-foxter25.png` | x 477.6 → 1391.6 = **914** | 1.291 |
| `D-garage-kickstarter-countdown-later.png` | x 475 → 1388 = **914** | 1.291 |
| `C-garage-before-maze-panel.png` (cross-check) | x 260 → 1359 = **1100** | 1.5537 |

**Ruler B — the sidebar `.box`.** `[MEASURED]` The *Top 10 Exp.* box outer
width: `D-garage-2018-url-bar-youtube-toast` 1571.5−1405.5 = **166** capture px → 166/1.3729 = **120.9**
CSS. `C-garage-before-maze-panel` 1567.5−1379.5 = **188** → 188/1.5537 = **121.0** CSS. The two
agree to 0.1 px, which validates Ruler A on both frames and pins `.box`
outer width at **121 CSS px** (a value the project can use directly).
Applying Ruler B to `D-garage-kickstarter-eve-foxter25.png` (Top-10 box = 156 capture px) gives
scale = 156/121 = **1.289** — within 0.2 % of Ruler A's 1.291. Adopted:
**s(V1) = 1.29 ± 0.01**, **s(V4) = 1.3729**.

Ruler A also proves the **5-tab nav of V1 is still 708 CSS px wide** — the
older `TANKTROUBLE.com` logo tab is simply wider, absorbing the missing shop
tab. `[INFERRED]`, from the fact that Rulers A and B agree on `D-garage-kickstarter-eve-foxter25.png`.

**V3 and V2 have no page chrome**, so:
- **V3** scale is back-derived from the collapsed panel outer width (277
  capture px ÷ 228 CSS, see below) → **s(V3) ≈ 1.215**. Circular for the
  width itself, but the *height* and *expanded-width ratio* it yields are
  independent checks and they land correctly, so I use it for ratios only.
- **V2** scale is back-derived from the spray-can pitch measured in V1
  (16.5 CSS px) → **s(V2) ≈ 2.29**. Weak; all V2 CSS numbers are `[UNCERTAIN]`.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| 1 | The userpanel is a white, 1 px `#cfcfcf`-bordered, ~4 px rounded card, **228 × 181 CSS px outer**; username centred at the top in `#666`-family grey; tank render centred beneath; a bottom-aligned strip of icons | MEASURED | **S24** WANTED → **FETCHED** | Nothing built yet — this is the spec |
| 2 | Single panel sits at `left: 232` in the 692 px centre column — i.e. exactly `(692−228)/2`. Two panels sit at `left: 113` and `351` (pitch 238, 10 px gap) | MEASURED | **S24**, **S7** | Fills the unknown `position` argument of `closePaintFacility(user, position)` (`:3567`) |
| 3 | Four icons visible for an ordinary user, not five: **wrench-with-a-"beta"-tag / trophy / isometric maze / document-with-yellow-warning-triangle**. All greyscale 3-D art except the yellow triangle. `userpanelSherifStar-` absent, as the JS null-guard predicts | OBSERVED + MEASURED | **S25** WANTED → **PARTIAL**; **S26**; **S27**; **S46** | — |
| 4 | An older build (V3) shows only **three** icons — no trophy. The trophy (`userpanelStats-`) was added later | OBSERVED | **S25**, **S33** | — |
| 5 | Paint facility = two mirrored banks of **9 spray cans** flanking the tank + a row of accessory **chips** + a row of **four 3-D "toolboxes"**. Clicking a toolbox swaps **both** the can palette **and** the accessory catalogue | OBSERVED | **S29** WANTED → **PARTIAL**; **S30** WANTED → **PARTIAL** | — |
| 6 | Four toolboxes identified: grey metal crate (default), Halloween jack-o'-lantern, Christmas present, gold star-embossed box. The selected one is drawn **open** | OBSERVED | **S30** ("toolbox grouping") | — |
| 7 | Four complete can palettes sampled to hex: standard 9-hue rainbow, Halloween grey→orange→red, Christmas red/green interleaved, gold/brass 9-shade | MEASURED | **S29/S30**, paint SWF rebuild | Directly usable palette |
| 8 | The differing palettes are **not** a locked/unpurchased presentation — they are toolbox-selected sets. S32's question is instead answered by the gold box, which offers **only two** accessories with no arrows | MEASURED + INFERRED | **S32** | — |
| 9 | Accessory chips render in three states: `#f1f1f1` normal, `#b4b4b4` = currently fitted to the tank, and a partially transparent state during scroll | MEASURED | **S30**, **S31** | — |
| 10 | ◀ ▶ arrows (solid `#c0c0c0` triangles) page the chip row **one item at a time**; page 1 has no ◀ | MEASURED | **S30** WANTED → **PARTIAL** | — |
| 11 | Hovering a can, an accessory chip or an arrow **enlarges it ~1.8×** on top of its neighbours | MEASURED | **S51**, new want | — |
| 12 | The accept ✓ (`userpanelAcceptPaint-`) is a hand-drawn green tick with a black outline, ~26 × 34 CSS px, inset ~12 px from the right border and ~14 px from the bottom border | MEASURED | **S28** WANTED → **PARTIAL** | — |
| 13 | With paint open, the icon strip is **completely invisible** — confirming `disableUserPanelIcons` drives opacity to a true 0 | OBSERVED | **S25** | Confirms `:3501-3536` |
| 14 | Expanded/collapsed panel width ratio measured **3.072** against a predicted 3.071 — confirms the 224 → 692 pair in *both* builds | MEASURED | **S24**, **S29** | Confirms `:3556`, `:3575` |
| 15 | Every form in this set is `signupform` (`:4167-4231`), **not** the garage settings form. S34 is untouched | OBSERVED | **S34** stays WANTED; **S52/S54** gain evidence | — |
| 16 | Three generations of sign-up copy captured verbatim, including one string that is **not** in the held bytes | OBSERVED | **S107**, **S52-S55** | — |
| 17 | `userpanelsheader` was **non-empty** in the older build — it held the centred line *"Customize your tank"*; it is empty in V1 and V4 | MEASURED | **S24** | — |
| 18 | V4 is datable to **early-to-mid October 2018** — inside the target window | INFERRED | **S106**, **S16** | — |
| 19 | V1 is pinned to **1 day 20 h before the TankTrouble Kickstarter launch** — outside the 2017-18 target window | INFERRED | **S16**, **S99** | Must be labelled |
| 20 | `D-garage-2018-url-bar-youtube-toast.png` URL bar reads `https://tanktrouble.com/?garage` verbatim — direct route evidence | OBSERVED | route confirmation | — |
| 21 | Bonus: the `.box.halloween` seasonal skin and the sidebar logged-in user card are both fully rendered | OBSERVED | **S16**, **S6**, **S8** | — |
| 22 | Bonus: the `PLAY ONLINE` countdown widget (`:4674-4719`) confirmed against pixels in **both** branches — expired string byte-exact, and the live branch's Courier-bold `[56,32,20,14]`/`[24,20,16,14]` size ladder and singular/plural rule measured | MEASURED | `:4675`, `:4697-4706`, `:4714`; **S16** | — |

---

## The userpanel geometry model (S24) — assembled from `D-garage-2018-scrub-bar-visible`/`D-garage-2018-url-bar-youtube-toast`

All figures CSS px at s = 1.3729, quoted from border-centre to border-centre
unless stated. Both frames agree to ≤1 capture px on every number.

```
                      ┌─────────────────────────────┐  ← card top      (y=0)
   userpanel-<user>   │                             │
   outer 228 × 180.6  │        mr_enderman          │  name  9.5 → 22.6
   border 1px #cfcfcf │                             │
   radius ≈ 3–4       │        ██ tank art ██       │  tank 24.8 → 107.1
   background #ffffff │       (125 × 82, centred)   │      userpanelContent-
                      │                             │      = 99 px tall
                      │                             │
                      │ 🔧  🏆  ▦  📄               │  icons 133.3 → 174.1
                      └─────────────────────────────┘  ← card bottom  (180.6)
                        ↑4                       ↑25
```

`[MEASURED]` numbers, `D-garage-2018-url-bar-youtube-toast.png` unless noted:

| Property | capture px | CSS px | Note |
|---|---|---|---|
| card outer width | 312 (747.5→1059.5) | **227.3** | `D-garage-2018-scrub-bar-visible` identical |
| card outer height | 248 (204→452) | **180.6** | `D-garage-2018-scrub-bar-visible` identical; `C-garage-before-maze-panel` at its own scale gives 180.2 |
| card left in centre column | — | **232.0** | = (692−228)/2 exactly |
| card top below page top | 102 | **74.1** | = nav 53 + table `margin-bottom:20px` + 1 |
| border darkest sample | `#cfcfcf` (207–208) | — | 1 CSS px, blurred to 2 capture px |
| name ink, darkest / median | `#5f5f62` / `#797778` | — | consistent with the site-wide `#666666`; **not** black |
| name box (ascender→baseline) | 19 | **13.8** | ⇒ font-size ≈ 18–19 px `[INFERRED]` |
| name bbox `mr_enderman` | 170 wide | 123.8 | horizontally centred in the card |
| tank art bbox (`D-garage-2018-scrub-bar-visible`) | 172 × 114 | **125 × 83** | centred to within 2 capture px |
| icon strip band | 57 tall | **41.5** | icons are **bottom**-aligned, tops ragged |
| icon pitch | 70.8 | **51.5** | 4 icons |
| left inset of first icon | 5.5 | **4.0** | |
| right inset of last icon | 34.5 | **25.1** | asymmetric, reproducible in both frames |

**The 99 px accounting works out.** `userpanelContent-<user>` is 99 px
(`srv/index.php:3573`). Name block ≈ 24.8 + content 99 = 123.8, icons occupy
133.3 → 174.1, bottom padding 6.5 → 180.6. `[INFERRED]` `userpanelContent-`
is the **tank slot only**; the name label sits above it and the icon strip
below it, both outside the animated element. That is exactly what the JS
implies — the tank flash is written into `userSettingsTank-<user>` and the
paint facility grows `userpanelContent-` from 99 to 245 without touching the
name or the icons.

**Wrapper accounting.** `userpanelswrapper` is 214 px (`:3573`); the card is
180.6 tall and flush to its top, leaving ~33 px of slack below. `[MEASURED]`
In `D-garage-2018-url-bar-youtube-toast` the *"Sign up another tank"* header begins ~10 CSS px below the
wrapper's computed bottom edge — consistent, and it means the header the
project must render sits at `card_top + 214 + ~10`.

**Multi-user positions (S7).** `[MEASURED]` from `C-garage-before-maze-panel.png` (cross-check
frame, s = 1.5537, two panels `revengexx1` and `creed`):

- card 1 outer x 447 → 803 (357 capture = 229.8 CSS)
- card 2 outer x 819 → 1176 (358 capture = 230.4 CSS)
- gap between them 16 capture = **10.3 CSS**
- distance from the centre column's left edge to card 1 = **112.7 CSS**
- distance from card 2 to the column's right edge = **110.1 CSS**

Predicted for two 228-wide panels with a 10 px gap, centred in 692:
`(692 − (2×228 + 10)) / 2 = 113`. Measured 112.7 / 110.1. `[MEASURED]`
So the server-side `position` values are:

| users | `left` values | derivation |
|---|---|---|
| 1 | `232` | (692−228)/2 |
| 2 | `113`, `351` | pitch 238 |
| 3 | **unknown** | 3×228 + 2×10 = 704 > 692, so the gap must shrink; `0 / 232 / 464` (pitch 232, gap 4) is the only clean fit `[INFERRED]` |

No 3-user frame exists in this corpus, so the 3-user row **stays on the
want-list**.

**Panels are absolutely positioned.** `closePaintFacility(user, position)`
(`:3567`) and `closeMazeCreator` / `closeForm` / `closeStats` all animate
`left` back to a caller-supplied `position`, and `openForm` (`:3762`) hard-codes
`left → 171`, which is exactly `(692−350)/2`. `[MEASURED]` My 232 for one user
and 113/351 for two are the same arithmetic. That is a self-consistent model
the rebuild can implement without further evidence.

---

## The paint facility model (S29 / S30 / S31 / S32 / VE entry 9)

Two structurally different generations are present.

### Generation B — "toolbox" build (V1, V2, and `C-garage-before-maze-panel.png`)

Layout inside the expanded panel, top to bottom:

1. username (unchanged, still at the top of the card)
2. **left can bank (9) — tank — right can bank (9)**, the right bank being the
   left bank in reverse order `[MEASURED]`
3. **one row of accessory chips** — 10 to 11 circular chips, flanked by ◀ / ▶
   grey triangles
4. **one row of four 3-D toolboxes**
5. the green accept ✓ at the bottom right

`[MEASURED]` expanded card outer, `D-garage-kickstarter-eve-foxter25.png`: x 478 → 1392 (914 capture),
y 154 → 579 (425 capture). At s = 1.29 that is **709 × 329.7 CSS**.
Predicted from the JS: width 692 + 4 = 696; height 180.6 + (245 − 99) = 326.4.
The height lands within **1.0 %**; the width is **1.9 %** over. `[UNCERTAIN]`
I cannot separate 696 from 709 at this precision. What I *can* say firmly:
the expanded panel's left border coincides with the nav strip's left edge to
within 0.5 capture px, which is 8 CSS px further left than a 692-wide,
centre-column-centred box would sit. Either the V1 build's centre column was
wider than 692, or my scale is 2 % low. **The V4/era-final 692 is not
challenged by this** — V1 is a different, older build.

### Generation A — "two-row grid" build (V3)

No toolboxes, no arrows, no paging. **Two rows of eight** accessories, each on
a faint circular chip. `[MEASURED]` collapsed card 277 × 216.5 capture;
expanded card 851 × 297 capture (`D-paint-older-build-grid-no-hover.png` and `D-paint-older-build-grid-expanded.png` agree).

- **width ratio 851 / 277 = 3.072**, against a predicted
  `(692+2)/(224+2) = 3.071`. `[MEASURED]` This is the single strongest
  confirmation in the whole document that the **224 → 692 width animation is
  correct**, and it holds in a build years older than the archived bytes.
- **height**: at s(V3) = 1.215 the expanded outer is **244.4 CSS**, so
  `userpanelContent-` in this build was ≈ **163 px**, not 245. `[INFERRED]`
  The older paint facility was shorter because it had no toolbox row. The
  rebuild should treat 245 / 360 as era-final values only.

### Spray cans — the palette (directly usable)

`[MEASURED]` Detected by saturation-mask column grouping; the quoted hex is the
median of the saturated pixels of each can body. Video compression means the
low-order bits are unreliable; the *ordering and hue family* are solid.

**Standard set** — grey crate open (`D-paint-standard-palette-comic-overlay.png`, the cleanest crop; left bank,
left→right). The right bank is this list reversed.

| # | hex | reading |
|---|---|---|
| 1 | `#005cc5` | blue |
| 2 | `#6614c6` | violet |
| 3 | `#c852b6` | magenta / pink |
| 4 | `#ce1e00` | red |
| 5 | `#663300` | brown — lands **exactly** on the web-safe value `#663300` |
| 6 | `#c96300` | orange |
| 7 | `#c2b300` | yellow |
| 8 | `#78ad00` | chartreuse |
| 9 | `#00a100` | green |

Cross-check from `D-garage-kickstarter-eve-foxter25.png` (different frame, different compression):
`#055cb3 #611ab7 #c555b7 #be240d #643507 #c76607 #bdb60f #7fae0e #07a10e`.
Same nine hues in the same order. `[MEASURED]` Nine cans per bank, two banks,
mirrored — **18 clickable cans, 9 distinct colours**.

**Halloween set** — pumpkin open (`D-paint-halloween-toolbox-comic-overlay.png`, left bank left→right):
three greys (dark → light), then `#c96700`, `#ca5200`, `#a74d00` (oranges),
then `#b9301c`, `#7b0c00`, `#4e0700` (reds → near-black). `[MEASURED]` The
grey members needed a lower saturation threshold; the three grey plates are
visible in the crop and counted by eye `[OBSERVED]`.

**Christmas set** — present open (`D-garage-kickstarter-countdown-later.png`, left bank left→right), red and
green strictly interleaved, each colour ramping dark → bright:

`#600b07` `#033a06` `#7e0f05` `#035c08` `#950f03` `#027e07` `#ae1505` `#04910a` `#c61805`

i.e. **5 reds** `#600b07 #7e0f05 #950f03 #ae1505 #c61805` and **4 greens**
`#033a06 #035c08 #027e07 #04910a`. `[MEASURED]`

**Gold set** — (`D-paint-gold-toolbox-two-chips.png`, left bank left→right), nine olive/brass shades:

`#ad9700` `#c3a733` `#a68a00` `#c3ab00` `#967a2f` `#c0bc70` `#948659` `#c1b622` `#8e7140`

`[MEASURED]` All nine sit in the yellow-olive wedge; the alternation of lighter
and darker suggests a metallic gold/brass/bronze family rather than a hue ramp.
`[UNCERTAIN]` — this crop is the most compressed of the four.

**Can geometry.** `[MEASURED]` Pitch 21.25 capture px in `D-garage-kickstarter-eve-foxter25.png`
(s = 1.29) → **16.5 stage px**; can body ~18 capture → **14 stage px**.
Confirmed at 21.1 capture in `D-garage-kickstarter-countdown-later.png` and 37.75 capture in the 2.29×-zoom
V2 crops (37.75/2.29 = 16.5). Because the cans are drawn inside a
600 × 250 SWF written at its natural size (`:4219`, `:4147`), stage px = CSS px.

### The differing palettes — candidate explanations, and which the evidence forces

The brief flags "an all-amber/gold row vs a full-spectrum row" as potentially
significant (S32). `[OBSERVED]` The evidence forces one explanation and rules
out the others:

- In `D-garage-kickstarter-eve-foxter25.png` and `D-paint-chip-row-scrolled-one-step.png` and `D-paint-standard-palette-comic-overlay.png` the **grey crate is drawn
  open** (lid tipped back, latched body visible) and the cans are the full
  spectrum.
- In `D-paint-halloween-toolbox-comic-overlay.png` the **pumpkin is drawn open** (its lid, with stem, tipped off
  and leaning) and the cans are the Halloween ramp.
- In `D-garage-kickstarter-countdown-later.png` the **present is drawn open** (lid tipped to the right, bow
  lying loose at the front-left) and the cans are the Christmas ramp.
- In `D-paint-gold-toolbox-two-chips.png` the other three boxes are all drawn **closed** and the cans
  are the gold ramp; the fourth box is behind the speech bubble but the visible
  sliver is a brighter yellow than the closed gold box in `D-garage-kickstarter-eve-foxter25.png`
  `[UNCERTAIN]`.

So: **the toolbox selects the set**, and each set carries its own can palette
*and* its own accessory catalogue. `[OBSERVED]` This is not a seasonal skin
(all four boxes are present simultaneously in every frame), not a different
build (V1 and V2 show all four), and not a locked presentation.

**What S32 actually gets from this** — the gold box's accessory row contains
**exactly two** items and **no arrows at all**, where the standard box shows
10-11 items with arrows. `[MEASURED]` The candidate readings, none of which
the evidence settles:

1. *Unowned items are simply not rendered.* The gold box holds
   achievement/Kickstarter-backer items and this account owns two. Supported
   by the loader behaviour cited in the want-list (`DoAction.as:1610-1616`
   skips `_width == 0` clips) — an empty clip renders as nothing, not as a
   greyed slot.
2. *The gold box genuinely only ever contained two accessories.*
3. *The gold box is an "earned" box and its contents grow with achievements.*

Reading 1 is the most economical and is consistent with the held decompile
note, but a second account with a different gold-box inventory would be needed
to prove it. **S32 stays WANTED**, now with a much sharper ask (see New wants).

### Accessory chips (S30 / S31)

`[MEASURED]` Chip circle diameter ≈ 74 capture px in `D-paint-chip-row-scrolled-one-step.png`
(s ≈ 2.29) → **≈ 32 stage px**; pitch 78 capture → **≈ 34 stage px**.
Confirmed independently in `D-garage-kickstarter-eve-foxter25.png`: pitch 44 capture at s = 1.29 →
**34.1 stage px**. Two frames, two scales, same answer.

**Three chip background states**, sampled as the modal near-neutral grey inside
a disc at each chip centre:

| state | grey | hex | seen in |
|---|---|---|---|
| normal | 241 | `#f1f1f1` | every frame |
| **fitted to the tank** | 180–183 | `#b4b4b4` | `D-garage-kickstarter-eve-foxter25.png` (flag), `D-paint-standard-palette-comic-overlay.png`/`D-paint-chip-row-scrolled-one-step.png` (red pen), `D-paint-gold-toolbox-two-chips.png` (flag), `D-garage-kickstarter-countdown-later.png` (three chips) |
| mid-fade | 246 / 253 | — | last chip only, in `D-garage-kickstarter-eve-foxter25.png` and `D-garage-kickstarter-countdown-later.png` |

`[INFERRED]` mid-grey = *currently equipped*. The reasoning: in each of the
four frames the darker chip's sprite is visibly worn by the tank in the same
frame — `D-garage-kickstarter-eve-foxter25.png`'s red tank flies the blue flag whose chip reads 180;
`D-paint-gold-toolbox-two-chips.png`'s brown tank flies the white "no-paw" flag whose chip reads 180;
`D-paint-standard-palette-comic-overlay.png`/`D-paint-chip-row-scrolled-one-step.png`'s tanks carry the red pen accessory whose chip reads
180. `D-garage-kickstarter-countdown-later.png` has three chips at 181-183, and the tank there wears a Santa
hat, a candy cane and a bow — consistent with the JS's four accessory slots
(`oldTurretAccessory`, `oldBarrelAccessory`, `oldFrontAccessory`,
`oldBackAccessory`, `:3579-3581`). **Falsified if** a frame turns up with a
mid-grey chip whose sprite is absent from the tank.

**Paging.** `[MEASURED]` `D-paint-standard-palette-comic-overlay.png` (17:09:45) shows the chip row starting
with a brown cowboy hat; `D-paint-chip-row-scrolled-one-step.png` (17:10:29), 44 s later in capture order,
shows the identical row **shifted left by exactly one item** — the cowboy hat
has gone and a gold peace sign has appeared at the right end. Both frames show
10 chips between a ◀ and a ▶. `[OBSERVED]` `D-garage-kickstarter-eve-foxter25.png` shows 11 chips, a ▶,
and **no ◀** — i.e. page 1. So:

- the row is a **sliding window** over a longer catalogue,
- **one click = one item**, not a page,
- the ◀ is **hidden (not disabled)** at the start of the list.

**Arrows.** `[MEASURED]` `D-paint-standard-palette-comic-overlay.png`: 26 × 46 capture px, modal grey **192
(`#c0c0c0`)**, solid filled triangles, left one at x 47-72 and right at
984-1009. At s = 2.29 that is **≈ 11.4 × 20.1 stage px** — taller than wide.

**Scroll fade.** `[MEASURED]` In both `D-garage-kickstarter-eve-foxter25.png` and `D-garage-kickstarter-countdown-later.png` the mouse
pointer is parked on the ▶ and the **last** chip is partially transparent.
Solving `bg = 255 − α(255 − 241)` for the measured chip background:
`D-garage-kickstarter-eve-foxter25.png` bg 246 → **α ≈ 0.64**; `D-garage-kickstarter-countdown-later.png` bg 253 → **α ≈ 0.14**.
Two different values in two frames of the same control ⇒ this is an
**animation in progress**, not a permanent "there is more" affordance.
`[INFERRED]` scrolling fades items in/out at the ends rather than sliding them.
Falsified if a frame shows a chip mid-way *between* two slot positions.

**Hover.** `[MEASURED]` `D-paint-can-hover-violet-later.png` and `D-paint-can-hover-violet.png` catch the third can under
the cursor drawn **much larger than its neighbours and overlapping them**:
normal can body ≈ 25 capture px wide, hovered ≈ 45 → **≈ 1.8×**. `D-paint-accessory-hover-bandana.png`
and `D-paint-accessory-hover-pirate-hat.png` catch the same effect on accessories (item 1, then item 2).
`D-garage-kickstarter-eve-foxter25.png`'s ▶ measures 27 capture px wide (21 CSS) against `D-paint-standard-palette-comic-overlay.png`'s
11.4 CSS — the cursor is on it, so the arrows scale too. `[OBSERVED]` The
yellow halo around the pointer in these frames is the **screen recorder's
click-highlight effect**, not site UI — it is a soft radial yellow disc
centred on the hotspot and appears identically over the page background.

**The toolboxes (S30 "toolbox grouping").** `[OBSERVED]` Four 3-D rendered
objects with soft drop shadows, evenly spaced:

1. **Grey metal crate** — light-grey box, mid-grey right face, a horizontal lid
   seam and **two white latch plates** on the front, each drawn as a small
   rectangle with four dots. Open state: the lid is tipped back and up, hinges
   visible.
2. **Halloween jack-o'-lantern** — orange ribbed pumpkin, dark-green curled
   stem, carved triangular eyes, a small triangular nose and a jagged grin.
   Open state: the top (with the stem) is lifted off and tilted to the left.
3. **Christmas present** — green box, red ribbon cross, a large multi-loop red
   bow, and a beige gift tag on a string. Open state: the lid is tipped off to
   the right and the bow lies loose at the front-left.
4. **Gold box** — pale gold/brass box with the **same two latch plates** as the
   grey crate and a **five-pointed star** embossed on the front face.

`[MEASURED]` In `D-garage-kickstarter-eve-foxter25.png` the four boxes' bounding boxes sit between
capture x ≈ 640 and x ≈ 1230 within a 914-wide card, i.e. the row is centred
and occupies roughly 64 % of the panel width; the boxes are ~110-130 capture px
(85-100 CSS) tall including shadow.

**Badges (S31).** `[OBSERVED]` Three distinct badge artworks occupy the same
position — the lower-right of the hull, half over the tracks:

- a **white skull-and-crossbones** (`D-garage-kickstarter-eve-foxter25.png`, `Foxter25`'s red tank)
- a **yellow sheriff-style five-point star** with a white highlight
  (`D-paint-standard-palette-comic-overlay.png`, `D-paint-halloween-toolbox-comic-overlay.png`, `D-paint-chip-row-scrolled-one-step.png`, `D-paint-gold-toolbox-two-chips.png`)
- a **gold bone** (`D-garage-2018-scrub-bar-visible.png` `mr_enderman`, and `D-game-teaser-screen-not-garage.png`'s tank)

`[INFERRED]` these are `oldBadge` (`:3581`), because they share one mount point
distinct from the four accessory slots and none of them ever appears in the
chip row. That gives S31 three confirmed sprites and a confirmed anchor point,
but **no picker UI is visible in any frame** — S31's chooser stays WANTED.

---

## File-by-file analysis

### `UI/D-garage-kickstarter-eve-foxter25.png` (1879×1043, captured 16:48:02) — **the single most valuable frame**  *(was `garage.png`)*

**Filename claim (repo owner):** "garage" — corroborated. The URL bar reads
`www.tanktrouble.com/?garage`.

**What is drawn**
- `[OBSERVED]` Windows Chrome window; one tab titled `TANK TROUBLE Tank…`;
  omnibox `www.tanktrouble.com/?garage` with a page icon (no padlock ⇒ http).
- `[OBSERVED]` Nav strip: `TANKTROUBLE.com` logo tab, `NEWS`, a **raised
  (selected) wrench** tab, a speech-bubble tab, a lab-flask tab. **Five** tabs
  — no shop t-shirt tab. The wrench tab is the raised/selected one, matching
  `tab3Select.jpg` at `:3471`.
- `[OBSERVED]` Left column: black `Scrapyard` box with **amber/gold** digit
  plates reading **`115388534?`** — nine plates legible, the tenth caught
  mid-flip (a 4 over a 9), so the final digit is `[UNCERTAIN]`; a
  TankTrouble-logo-over-maze image; a **Kickstarter countdown box** — "KICK"
  in near-black, "STARTER" in bright green, then `launches in` / `1` / `day` /
  `20` / `hours` / `54` / `minutes` / `17` / `seconds` / `Read more…`; a
  `? Log In` box with `username` / dots / `Log in` `Sign up`; below it a red
  tank render and the logged-in card `⊠ Foxter25` / `Exp. 117` / `🏆 6 (3)`
  `💀 8`.
- `[OBSERVED]` Right column: `Top 10 Exp.` with the **Friends tab selected**
  (white; `Weekly` greyed) showing only `foxter 18510` and `Foxter25 117`;
  App Store badge; Google Play badge; Facebook `Like` / `Share`;
  `Tell a Friend`; `Got Feedback?`.
- `[OBSERVED]` Centre: the userpanel, **expanded with the paint facility open**.
  Username `Foxter25` centred at the top in grey. Two banks of nine spray cans
  flanking a red tank that wears a blue flag on the turret, a blue barrel item,
  and a white skull-and-crossbones badge on the hull. Below: eleven accessory
  chips and a ▶ arrow (cursor on it). Below that: the four toolboxes, grey
  crate **open**. Green ✓ at the bottom right.
- `[OBSERVED]` **The icon strip is entirely absent** from the card.
- `[OBSERVED]` Below the card: `Sign up another tank`, then the four-field
  form, then `Customize your tank`, then a second can row (the sign-up tank
  designer) cut off by the frame edge.

**Measurements**
- `[MEASURED]` scale 1.289–1.291 (two independent rulers, §"How scale was
  derived").
- `[MEASURED]` expanded card outer x 478 → 1392 = 914 capture = **709 CSS**;
  y 154 → 579 = 425 capture = **329.7 CSS**. Border darkest ≈ 214-218.
- `[MEASURED]` accept ✓ bbox x 1344-1376, y 518-561 = 33 × 44 capture =
  **25.6 × 34.1 CSS**; **15 capture px (11.6 CSS) inside the right border**,
  **18 capture px (14.0 CSS) above the bottom border**. Green fill median
  `#13941a`, brightest sampled `#00d107`, with a black outline.
- `[MEASURED]` can palette and pitch — see §"Spray cans".
- `[MEASURED]` accessory chips at pitch 44 capture (34.1 CSS), eleven of them,
  first at x ≈ 703, ▶ at 1194-1220. **No ◀** — the region x 600-681 in the chip
  band is pure white.
- `[MEASURED]` chip 9 (blue flag) background grey **180**; chip 11 background
  **246** (α ≈ 0.64).

**Accessory row, left → right** `[OBSERVED]`: a grey ring/tyre with a dark nub;
a grey shell/wedge; a black-and-white spiked star with a dark ring; a red
firecracker with a gold fuse; a yellow smiley; a white `LOL` plaque with a
black border; a gold peace sign on grey; a white zig-zag strip; a **blue flag
on a pole** (chip mid-grey — worn by the tank); a red-and-blue balloon/heart on
a stick; a pale grenade (fading); then ▶.

**Links to the program**
- **S24** — first pixels ever. Expanded-state geometry above.
- **S25** — the four/five icons are at opacity **0** while paint is open,
  which is exactly `disableUserPanelIcons` (`srv/index.php:3501-3536`). This is
  positive confirmation that the fade goes to a *true* 0, not a dim state.
- **S28** — accept ✓ art, size and inset (above). `:3563`.
- **S29** — the open state that `openPaintFacility` (`:3554-3565`) produces.
- **S30 / S31 / S32** — toolboxes, chips, arrows, badge.
- **S16** — the `.box.kickstarter` variant, which `boxStyles.css:31-70+`
  declares and which the want-list says *"used by zero captured page"*. It is
  rendered here in full.
- **S3** — the Top-10 **Friends** tab is selected and populated. Not my topic;
  flagged for whoever owns it.
- **S6** — the sidebar logged-in card is fully legible.
- **Route** — `?garage` confirmed in the omnibox.

**Dating** `[INFERRED]` The Kickstarter countdown reads 1 day 20 h 54 m 17 s to
launch. The repo's own docs place the Kickstarter period in 2015 (S99;
`DEDUCE.md:158-161`, `kickstarterFAQBanner.png`). So this frame is **one day
before the TankTrouble Kickstarter launched**, i.e. **outside the 2017-2018
target window**. Confidence: high that it is Kickstarter-launch-eve; medium on
the calendar year, because I am relying on the repo's own dating of the
campaign rather than on anything in the pixels. Anyone applying this evidence
must label it as pre-era.

**What this does NOT show:** the collapsed panel; the icon strip; the maze,
form or stats panels; any 3-user stack; the ✓ being clicked; the close
animation; the `Ready for action !` button.

---

### `UI/D-garage-kickstarter-countdown-later.png` (1891×1051, 16:51:42)  *(was `{44AB875B-556E-4C57-82F5-6C209ECB78DB}.png`)*

Same session as `D-garage-kickstarter-eve-foxter25.png`. `[MEASURED]` The Kickstarter countdown has moved
from `54 minutes 17 seconds` to `48 minutes 0 seconds` — **6 min 17 s later in
the source video**, though only 3 min 40 s later in Ethan's crop order, so the
video was being scrubbed rather than played straight. `[MEASURED]` Scrapyard
now reads `11538953` + two plates caught mid-flip (`11538953??`), i.e. roughly
**+10 000** on `D-garage-kickstarter-eve-foxter25.png`'s `115388534?` over those 6 min — consistent with a
monotonically rising counter, though the last two digits are `[UNCERTAIN]`.

**What is drawn** `[OBSERVED]` Identical page, identical scale (nav raised block
914 capture px in both), except that the **Christmas present toolbox is now
open** and the paint facility has switched to the Christmas set:

- cans: 5 reds interleaved with 4 greens, both banks mirrored (hex above)
- tank: a red-and-white "Santa" tank with a candy cane, a red bow and a white
  trim
- accessory row, left → right: a brown **sack of presents** with red/green/blue
  baubles (chip mid-grey); a rolled patterned **mat/rug**; a **Santa hat**;
  a **red bow** (chip mid-grey); a **Santa hat with a gold star** on the
  pompom; a **candy cane** (chip mid-grey); a **green wreath with a red bow**;
  a **holly sprig** with red berries; a **smoking pipe**; a grey chequered
  **box/parcel**; and an eleventh, almost fully transparent item; then ▶.
- `[MEASURED]` chip backgrounds: three at **181-183** (fitted), the rest at
  241-245, last at **253** (α ≈ 0.14).

**Links to the program** S30 (a second, seasonal catalogue, and the toolbox
open/closed art), S31, S29. Confirms that the toolbox row is not decorative.

**What this does NOT show:** any collapsed state; the icon strip; how a toolbox
is closed again.

---

### `UI/D-paint-standard-palette-comic-overlay.png` (1040×737, 17:09:45)  *(was `{267995BB-A52F-4E42-8404-9965232F9302}.png`)*

Account `foxter`. A tight, ~2.3×-zoomed crop of video, with a comic speech
bubble burned in by the uploader. No browser chrome, no sidebars.

**What is drawn** `[OBSERVED]` The card top border, `foxter` centred in grey,
a **dark-green** tank with a white flag bearing a **red prohibition roundel
over a dark animal silhouette** ("no dogs"), a red band at the turret base, and
a **yellow sheriff star badge**. Standard 9-hue cans both sides. Accessory row:
◀, then brown cowboy hat, red-orange mohawk/flame, black sunglasses, red pen on
a bar (**chip grey 180**), grey ring/tyre, grey wedge, spiked star with a brown
ring, red firecracker, yellow smiley, white `LOL` plaque, then ▶. Below: the
grey crate **open**, the pumpkin closed, and (partly behind the bubble) the
present and gold boxes.

**Overlay** A comic speech bubble is burned into the video over the lower right
of the frame. Per §"Video-authored overlays are excluded from evidence" it is
not analysed; only its **occlusion footprint** is recorded — it covers the
present and gold toolboxes and the right end of the chip row.

**Measurements** `[MEASURED]` cans at pitch 37.75 capture; chips at pitch 78,
circle diameter ≈ 74; arrows 26 × 46 capture, modal grey 192. Scale
`≈ 2.29` back-derived from the can pitch, so all CSS conversions here are
`[UNCERTAIN]`.

**Links to the program** S30 (the ◀ present ⇒ this is not page 1), S31, S24
(name label styling holds across accounts).

**What this does NOT show:** any page chrome, so nothing about layout, scale or
route can be taken from it directly.

---

### `UI/D-paint-halloween-toolbox-comic-overlay.png` (1044×702, 17:10:00)  *(was `{4B3EFDCC-0F18-49A3-98A5-42D977D888AC}.png`)*

15 s later. **Halloween toolbox open** — the pumpkin's top is lifted off and
tilted left; the grey crate is closed.

**What is drawn** `[OBSERVED]` The tank has turned **grey**. Cans: three greys
(dark→light), three oranges, three reds (bright→near-black); right bank
mirrored. Accessory row: ◀, then a grey **RIP gravestone**, a **black witch's
hat with an orange band**, a lit **white candle**, two **jack-o'-lanterns**
(different carvings), a **white ghost**, an **orange brain**, a **green frog**,
a partly obscured item, and an **orange-and-yellow bone or corn cob**; then ▶.

**Overlay** A comic speech bubble covers the right ~40 % of the chip row and
the right-hand toolboxes. Not analysed (see §"Video-authored overlays are
excluded from evidence"); recorded here only because it is what limits the
accessory enumeration above.

`[OBSERVED]` Note that the palette shift is established by pixels alone and
does not depend on the overlay: the **pumpkin toolbox is open**, the accessory
row is entirely Halloween-themed, and the can banks have gone grey/orange/red.
Toolbox selection drives the can palette.

**Links to the program** S30 (third catalogue + palette), S29.

**What this does NOT show:** the full accessory row (~40 % occluded); the gold
and Christmas boxes.

---

### `UI/D-paint-chip-row-scrolled-one-step.png` (1042×698, 17:10:29)  *(was `{3484955B-8535-4207-88D9-139691F86921}.png`)*

Back to the **standard** set (grey crate open). Tank is now **blue with a
purple barrel**.

**The paging proof.** `[MEASURED]` Set against `D-paint-standard-palette-comic-overlay.png` 44 s earlier, the
ten chips are the same list **advanced by exactly one**: `D-paint-standard-palette-comic-overlay.png` =
hat, mohawk, glasses, pen, ring, wedge, star, firecracker, smiley, LOL;
`D-paint-chip-row-scrolled-one-step.png` = mohawk, glasses, pen, ring, wedge, star, firecracker, smiley,
LOL, **peace**. Both flanked by ◀ and ▶. This is the direct answer to S30's
"accessory toolboxes **scrolled**" ask.

`[MEASURED]` chip backgrounds by disc-modal sampling at pitch 78:
`241, 241, 180, 241, 152*, 241, 241, 253, 253, 253` — the 180 is the red-pen
chip (equipped); the 152 is the grey **wedge sprite itself**, not a
background, and is called out here so nobody mistakes it for a fourth state.
`[MEASURED]` chip circle bbox for the 180 chip: 74 × 73 capture px.

**Overlay** A small comic speech bubble sits over the lower right; it occludes
no part of the can banks, chip row or toolboxes, so nothing above is affected.
Not analysed.

**Links to the program** S30 (one-item scroll step, ◀ hidden on page 1
elsewhere), S31, S29.

**What this does NOT show:** whether the arrow can be held for continuous
scroll; what happens at the end of the list.

---

### `UI/D-paint-gold-toolbox-two-chips.png` (1046×697, 17:10:39)  *(was `{94759D97-DF31-429F-B3F8-857A7D0661CB}.png`)*

**The S32 frame.** `[OBSERVED]` The gold/star toolbox set: the tank is
**brown/bronze**, both can banks are nine olive-gold shades, and the accessory
row contains **exactly two chips and no arrows at all**:

1. a **white skull-and-crossbones** — a cartoon skull with two bones crossed
   behind it, black outline, two round eye sockets and a small nose triangle —
   on a **normal `#f1f1f1` chip** (`[MEASURED]` modal 241)
2. a **white pennant flag** on a pole carrying a **red prohibition roundel**
   (circle with a diagonal bar) over a dark silhouette, on a **mid-grey
   `#b4b4b4` chip** (`[MEASURED]` modal 180) — and the tank is flying exactly
   that flag

`[OBSERVED]` The two chips are **centred** in the row where the standard set's
ten would run edge to edge, and the ◀ / ▶ triangles are absent entirely (not
greyed).

**Overlay** A comic speech bubble sits over the lower right, clear of the chip
row and both can banks. Not analysed.

**Links to the program** **S32** — see §"The differing palettes" for the three
candidate readings. The important, unambiguous part is the *rendering rule*:
when a toolbox has few items, the row **centres what exists and drops the
arrows**; it does not pad with empty or greyed slots. That is directly
implementable and it constrains any rebuild of the loader.

**What this does NOT show:** whether unowned items exist and are hidden, a
price tag, a lock icon, or a purchase affordance — none is present anywhere.

---

### `UI/D-userpanel-older-build-collapsed.png` (1046×584, 17:12:05)  *(was `{B53D30AB-BC36-4C1C-A61A-F0C196DA3B7C}.png`)*

New session, account `revengexx1`, **older build**.

**What is drawn** `[OBSERVED]`
- A centred grey heading **`Customize your tank`** immediately above the card.
- The **collapsed** userpanel: `revengexx1` in grey at the top; a **red** tank
  with a red flag bearing a hammer-and-sickle, and a yellow star badge; and a
  strip of **three** icons — wrench-with-"beta"-tag, isometric maze, document
  with a yellow warning triangle. **No trophy.**
- The screen-recorder's yellow click-halo pointer inside the card, to the right
  of the tank.
- Below the card: `Get your own tank. Sign up here` (with "Sign up"
  underlined), then a grey `First the boring stuff...`, then a **bordered
  panel** containing `Pick a username` / `username` / `Something awesome!`,
  `Pick a password` / dots / `Something secret..`, `Password again` / dots.
- Left column (clipped): a Scrapyard box reading `…21322`, a `…er Opens` promo
  box drawn with a wrench and newspapers, `…more…`, and an **American Express /
  MembershipMiles®** text ad. Right column (clipped): `Top 10` with
  `revengexx1`, `creed`, `Laika`; `Weekly` greyed; a Facebook box whose status
  begins `3 LONG yea… waiting. FIN… it's open. N…`; a dark hoodie (shop
  merchandise); `Tell a F…`.

**Measurements** `[MEASURED]` collapsed card outer x 382 → 658 = **277 capture**,
y 64.5 → 281 = **216.5 capture**. Taking the outer as 228 CSS gives
s(V3) ≈ 1.215, under which the height is **178.2 CSS** — against 180.6 measured
in the 2018 frames at a completely different scale. `[MEASURED]` The panel's
box model is therefore stable across at least two build generations.

**Links to the program**
- **S24** — `userpanelsheader` (`srv/index.php:3483`) is a `text-align:center`
  div whose content the server supplies via `updateUserPanels_cb` (`:4117-4126`,
  which reads the first child of the SAJAX response into it). `[INFERRED]` In
  this build that content was the string **"Customize your tank"**. Falsified if
  the heading turns out to be a static page element; but its position — dead
  centre, flush above the panel, and *absent* in V1/V4 where the panel sits
  exactly 73 CSS px below the page top with no room for anything — is what
  `userpanelsheader` is for.
- **S25** — three icons in this generation. `[INFERRED]` `userpanelStats-`
  (trophy) did not yet exist; `C-garage-before-maze-panel.png` and V4 both show four.
- **S34** — *not* this. See §"Which form is this?" below.

**What this does NOT show:** the fourth/fifth icon; the paint facility open;
any page chrome that would let me date it.

---

### `UI/D-paint-older-build-grid-expanded.png` (1038×580, 17:13:50)  *(was `{E62C5D8C-A919-4DF9-98A3-8909F6BBC9BA}.png`)*

Same card, now **expanded with paint open**. `[OBSERVED]` Two banks of nine
standard-palette cans flank the red tank; below them a **two-row grid of
sixteen accessories** on faint pale-grey circular chips; the green ✓ sits at
the bottom right. **No toolboxes, no arrows.** The heading `Customize your
tank` is still above the card; `Get your own tank. Sign up here` and
`First the boring stuff...` are still below it.

`[OBSERVED]` The pointer (with recorder halo) sits on **row 1, item 5** and
that sprite is drawn noticeably **larger than its neighbours and overlapping
them** — the same hover-enlarge seen in `D-paint-can-hover-violet-later.png`.

**Measurements** `[MEASURED]` expanded card outer x 94 → 945 = **851 capture**,
y 61 → 358 = **297 capture**.
- width ratio against the collapsed card in `D-userpanel-older-build-collapsed.png`: 851/277 = **3.072**,
  versus a predicted `(692+2)/(224+2) = 3.071`. This is the tightest
  confirmation in the document of the **224 → 692** pair
  (`srv/index.php:3556`, `:3575`).
- height at s(V3)=1.215 → **244.4 CSS**, implying `userpanelContent-` ≈
  **163 px** in this build, not the era-final 245 (`:3560`). `[INFERRED]` the
  shorter panel is what a two-row grid with no toolbox row needs.
- `[MEASURED]` accept ✓: bbox x 901-930, y 304-343 = 30 × 40 capture; green
  median `#1c9222`. Same artwork as `D-garage-kickstarter-eve-foxter25.png`'s.

**Links to the program** S29 (a second, older open state), S28, S24, S30.

**What this does NOT show:** any toolbox or paging control — they did not exist
in this build.

---

### `UI/D-paint-older-build-grid-no-hover.png` (1039×575, 17:13:57)  *(was `{02E885A2-F8C7-40B4-8366-23A9BE4CAA53}.png`)*

7 s later, the same expanded card with **no hover** — the cleanest read of the
older accessory grid. The pointer has moved to the right of the card, near the ✓.

**Accessory grid, verbatim description** `[OBSERVED]`, 8 + 8 on faint
`#f1f1f1`-ish circular chips:

*Row 1* — red bandana with white polka dots · black pirate/tricorn hat with a
white skull · black wrap-around sunglasses · red pen/dart lying on a bar ·
a grey club or periscope with a **blue** grip · a red cap seen side-on ·
a **brown cowboy hat** · a red hood/cap.

*Row 2* — a yellow sticky-note with scribbled writing · a plain **grey shark
fin** · a **red flag with a yellow hammer-and-sickle** · a white pennant flag
with a small round picture · a dark grey **hand grenade** · a white
**skull-and-crossbones** · a **gold peace sign** on a grey disc · a **yellow
smiley**.

`[MEASURED]` Chip modal backgrounds across both rows cluster at 241-243
(`#f1f1f1`-ish) with none at 180 — `[UNCERTAIN]` whether this build had the
"fitted" mid-grey state at all, because the tank's fitted items (soviet flag,
star badge) may be on chips whose sprites cover the whole disc.

**Links to the program** S30 (the pre-toolbox catalogue: **16 items, fixed, no
paging**), S31, S29.

**What this does NOT show:** any paging; any locked/priced presentation; the
icon strip (hidden while paint is open — consistent with `:3501-3536`).

---

### `UI/D-paint-accessory-hover-bandana.png` (1430×800, 17:14:12)  *(was `click.png`)*

**Filename claim (repo owner):** "click" — corroborated: the frame catches an
accessory mid-interaction.

`[OBSERVED]` Same expanded card, wider crop. **Row 1 item 1 (the red polka-dot
bandana) is drawn roughly twice its normal size**, overlapping item 2, with the
recorder's yellow click-halo under the pointer on it. Simultaneously the tank
shows a **white smoke/spray puff** over its hull — the paint/weld effect firing.
The ✓ is present at the bottom right.

`[INFERRED]` The puff is the SWF's "apply" animation (`DoAction.as:1530-1562`,
cited by **S51**), triggered by the click. Falsified if the puff turns out to be
a persistent decoration; it is absent in `D-paint-older-build-grid-no-hover.png` and `D-paint-can-hover-violet.png` of the
same session, so it is transient.

**Links to the program** S51 (first external sighting of the spray/weld
animation), S30, S29.

**What this does NOT show:** the frames either side of the puff, so its
duration and easing are unrecoverable here.

---

### `UI/D-paint-accessory-hover-pirate-hat.png` (1434×803, 17:14:28)  *(was `click (2).png`)*

16 s later. `[OBSERVED]` Now **row 1 item 2 (the black pirate hat with the white
skull)** is the enlarged one and the pointer is on it; item 1 has returned to
normal size. The white puff is still on the tank and the tank's hull now reads
darker/mottled where the puff sits.

`[MEASURED]` Taken with `D-paint-accessory-hover-bandana.png`, this is a two-frame demonstration that the
enlargement **follows the pointer** and affects exactly one item at a time —
i.e. it is a hover/rollover scale, not a selection indicator.

**Links to the program** S30, S51.

**What this does NOT show:** whether the scale is animated or instantaneous.

---

### `UI/D-paint-can-hover-violet.png` (1384×770, 17:15:19)  *(was `{6BB20BAB-F536-4835-AA05-485EF95830FD}.png`)*

`[OBSERVED]` Same card. Now a **spray can** is the hovered element: the third
can of the left bank (violet) is drawn large, overlapping cans 2 and 4, with the
pointer and halo on it. All sixteen accessories are at normal size. The tank is
red with the soviet flag and the star badge.

`[MEASURED]` normal can body ≈ 25 capture px wide; hovered ≈ 45 → **1.8×**.

**Links to the program** S51 (the "spray-can shake/pop" family), S29.

---

### `UI/D-paint-can-hover-violet-later.png` (1389×773, 17:15:26)  *(was `paint.png`)*

**Filename claim (repo owner):** "paint" — corroborated; this is the paint
facility.

7 s after `D-paint-can-hover-violet.png`. `[OBSERVED]` Nearly identical: the same violet can is
still hovered and enlarged, drawn slightly larger and higher than in
`D-paint-can-hover-violet.png`. `[MEASURED]` Its saturated bbox is 80 capture px tall here
against 56 in `D-paint-can-hover-violet.png` — `[INFERRED]` the enlargement is **animated**, and
these two frames catch it at two points, which means the rebuild owes a tween
rather than a snap. Falsified if the difference is instead a different can
being hovered — but both frames put the pointer on can 3 and both show the same
violet body, so I do not think it is.

**Links to the program** S51, S29, S30.

---

### `UI/D-game-teaser-screen-not-garage.png` (1279×658, 17:16:14)  *(was `{D2FDA7ED-766D-43EF-9DEF-1A9380A364CA}.png`)*

**`[NOT VISIBLE]` for this topic.** This is the `?game` teaser screen, not the
garage. Recording it is still worth something:

`[OBSERVED]` `The most explosive 2 player tank game online` /
`Face your primal instincts and prepare for savage encounters at the office`;
the grey outline tank over a faint maze; `Press Q` under a Q + ESDF key
cluster; `Press M` under an M + arrow cluster; a mouse graphic labelled
`_-Death-_`; `version 4.0` watermark bottom right; a gear icon and a speaker
icon bottom left; right column `Victories` Top-10 with the **Weekly** tab
selected (`swis4 1271… fivip456789123 1266… karimkhalil1234 1231… RENJIE 1185…
SwagRanger45 1064… akashi4 1026… Warsome 973… biggles12 842… kavkasiuri1 818…
nika1234567 792…`).

The one thing it does contribute to my topic: `[OBSERVED]` the small tank at
bottom centre is a **customised player tank** — indigo/purple hull, khaki
turret and barrel, black sunglasses fitted to the turret, three small dark
spiked items above it, and a **gold bone badge** on the hull's lower right,
in the same position as the star and skull badges seen in the garage frames.
`[INFERRED]` This corroborates that `oldBadge` renders at a fixed hull anchor
and is carried through to the game/teaser tank renders.

**What this does NOT show:** anything about the garage, the userpanel or the
paint UI.

---

### `UI/D-garage-2018-url-bar-youtube-toast.png` (1695×905, 17:28:41) — **the provenance frame**  *(was `garage3.png`)*

**Filename claim (repo owner):** "D-garage-2018-url-bar-youtube-toast" — corroborated.

**Browser chrome, transcribed verbatim** `[OBSERVED]`
- omnibox: a **padlock** then `https://tanktrouble.com/?garage`
- bookmarks bar: `Apps    For quick access, place your bookmarks here on the
  bookmarks bar. Import bookmarks now…`
- overlaid toast, dark grey rounded rectangle with a padlock glyph:
  **`youtube.com is now full screen`** with `youtube.com` in bold, and a
  bordered button reading **`Exit Full Screen (Esc)`**

`[OBSERVED]` **This pins the provenance.** The captured "browser window" is a
video playing full-screen on youtube.com; Chrome's own full-screen notice has
been captured *over* it. Every frame in this corpus that shares this
presentation is YouTube footage. Under guide §6.5 that caps all of it at **M2**
and forbids any O claim, exactly as the brief requires me to state.

`[OBSERVED]` The route `?garage` in the URL bar is **direct route evidence**,
independent of the page content.

**What is drawn**
- `[OBSERVED]` Nav: `TANKTROUBLE` logo (no `.com`), `NEWS`, raised **wrench**,
  a **t-shirt** tab, a speech bubble, a lab flask — **six** tabs, matching
  `srv/index.php:3471` exactly.
- `[OBSERVED]` Left: a **160 × 600 AdSense** slot filled with a Fortnite
  *SEASON 6 / DARKNESS RISES / JUMP IN* creative; a Scrapyard box with **white**
  digit plates — `258` legible, then three plates obscured by the pumpkin's
  stem, then `080` and a final plate mid-flip: `258???080?`, `[UNCERTAIN]`.
  Note the **skin has changed** from V1's amber-on-black plates to
  white-on-black, so V1's and V4's counters are not directly comparable
  (`[OBSERVED]`; cf. LEDGER 191-198, `scrapyard06/10/11.swf` vs the modern
  `scrapyard.js` widget); a **Halloween seasonal box** — a glowing jack-o'-lantern above an
  orange panel with black inset text `Let the candy feast begin!`; a red
  rounded box `PLAY ONLINE` / `Online battles are in heavy development. Try
  now!` — byte-exact against `srv/index.php:4675` and `:4714`, i.e. the
  **expired** branch of the countdown widget;
  the `? Log In` box; a purple tank; the card `⊠mr_enderman / Exp. 7722 /
  🏆 3495 (25) 💀 3559`.
- `[OBSERVED]` Right: `Need Help? / Check the FAQ`; `Top 10 Exp.` with
  `mr_enderman 7722 / _nothing_ 5950 / chaos_boy 5654 / doggy_king 4653 /
  crash_david 1340 / choasboy 60`, `Weekly` greyed and `Friends` active; Like /
  Share; App Store; Google Play; `Tell a Friend`; `Got Feedback?`; then a
  second AdSense slot with a **Flight Centre** creative
  (`FLI… CEN… / The Airf… / Sale ends Oct 18 / Explore… Holiday… $1395*… / Fin…`).
- `[OBSERVED]` Centre: the **collapsed userpanel** — `mr_enderman` in grey at
  the top, an **empty tank area** (the SWF has not painted, or has been faded
  out), and four bottom-aligned greyscale icons.
- `[OBSERVED]` Below: `Sign up another tank`, the four-field form, and
  `Customize your tank`.

**Measurements** — this is the frame all the S24 geometry comes from. Scale
1.3729 (Ruler A, cross-checked by Ruler B). Full table in §"The userpanel
geometry model". Additionally:

- `[MEASURED]` sign-up inputs: outer x 918 → 1101 = **183 capture = 133.3 CSS**
  wide; **25 capture = 18.2 CSS** tall; row pitch **56 capture = 40.8 CSS**;
  border grey ≈ 215.
- `[MEASURED]` label column `Name your tank` runs x 707 → 872; the input starts
  at 918, i.e. **30 CSS px** after the label cell — exactly the
  `padding-right: 30px` at `srv/index.php:4174`.
- `[MEASURED]` icon 4's warning triangle is the **only** colour in the whole
  strip: yellow median `#e3d02e`. Icons 1-3 have a maximum channel spread of
  **1** — they are pure greyscale.

**Dating** `[INFERRED]` **Early-to-mid October 2018.** Three independent
markers agree: Fortnite Chapter 1 Season 6 "Darkness Rises" (late Sep – early
Dec 2018); the Halloween seasonal box being live; and the Flight Centre
creative's `Sale ends Oct 18`. The last of these puts the frame **before 18
October 2018**. Confidence: high. This frame is **inside** the project's
2017-2018 target window and is therefore the most directly usable in the set.

**Links to the program** S24, S25, S26, S16 (`.box.halloween` rendered),
S23 (both AdSense slots filled, layout unreflowed — the want-list's exact ask),
S6, S8 (the `⊠` logout control), S105, and — outside my topic but confirmed
here — the expired branch of the `PLAY ONLINE` countdown at
`srv/index.php:4674-4719`.

**What this does NOT show:** the tank render inside the panel; any expanded
sub-panel; the sherif-star icon.

---

### `UI/D-garage-2018-scrub-bar-visible.png` (1675×961, 17:29:27)  *(was `garage2.png`)*

46 s later, same session, scrolled slightly and with the YouTube toast gone —
the player's scrub bar (a red line and a `5:03 / 5:10` timestamp) is visible at
the bottom, `[OBSERVED]` reconfirming the YouTube provenance independently.

**What is drawn** `[OBSERVED]` Everything from `D-garage-2018-url-bar-youtube-toast.png` plus:
- the **tank render inside the panel** — an indigo/violet hull, a black turret
  with a white skull, grey stencilled decals that read as `1919` either side, a
  dark barrel, and a **gold bone badge** on the hull's lower right
- the mouse pointer resting on the **maze icon**, with a hand cursor drawn over
  it
- a `Visits / Since 2007-12-16 / 66977609` box, partly clipped
- Scrapyard `258` + obscured plates + `0839` — the last four plates read `0839`
  against `D-garage-2018-url-bar-youtube-toast`'s `080?`, `[MEASURED]` i.e. the counter has advanced by a
  few tens in the 46 s between the two crops, confirming `D-garage-2018-url-bar-youtube-toast` precedes
  `D-garage-2018-scrub-bar-visible` in the video

**Measurements** `[MEASURED]` The card and its contents measure identically to
`D-garage-2018-url-bar-youtube-toast` on every axis (312 × 248 capture, icon pitch 70.7, strip band
347-403). Additional:
- tank art bbox x 872 → 1043, y 198 → 311 = 172 × 114 capture =
  **125 × 83 CSS**, horizontally centred in the card to within 2 capture px,
  top at **24.8 CSS** below the card's top border.
- the tank sits inside the 99 px `userpanelContent-` slot with ~16 px to spare
  at the bottom.

**Links to the program** S24 (this is the frame that fills in "tank position"),
S6, S46.

**What this does NOT show:** the expanded panel; any sub-panel.

---

## Bonus: the countdown widget (`srv/index.php:4674-4719`) confirmed against pixels

This was not on my topic list, but two of my frames render the same widget in
its two opposite branches, and both match the held bytes, so it is worth
recording.

`srv/index.php:4674-4678` (garage-route copy; siblings at `:510`, `:2095`,
`:10652`, `:12371`, `:13920`, `:15376`) is a **120 px wide, `#ff0000`, 6 px
top-rounded** clickable box that opens `https://beta.tanktrouble.com`. Its
heading is the literal `PLAY ONLINE` (`:4675`); its lower half is
`<div id="countdown">`, filled by the JS at `:4679-4718` counting down to the
epoch **`1475758800000`** = **2016-10-06 13:00:00 UTC**.

**Branch 1 — expired** (`:4712-4715`,
`t = "Online battles are in heavy development. Try now!"`). `[OBSERVED]`
`D-garage-2018-url-bar-youtube-toast.png` and `D-garage-2018-scrub-bar-visible.png` (Oct 2018, i.e. long past the epoch) render a
red rounded box reading exactly:

> PLAY ONLINE
>
> Online battles are in heavy development. Try now!

Byte-for-byte agreement with `:4675` and `:4714`. `[OBSERVED]`

**Branch 2 — live** (`:4684-4711`). `D-garage-kickstarter-eve-foxter25.png`'s Kickstarter box is the same
widget with a different heading and target. `[MEASURED]` I scanned the ink-row
runs down the box at s = 1.289 and compared them with the source's declared
ladders `numberSize = [56, 32, 20, 14]` (`:4697`) and
`labelSize = [24, 20, 16, 14]` (`:4699`):

| rendered line | ink height, capture px | ink height, CSS px | source ladder |
|---|---|---|---|
| `1` | 46 | **35.7** | `numberSize[0] = 56` — Courier bold digit ≈ 0.61 em ≈ 34 |
| `day` | 31 | **24.0** | `labelSize[0] = 24` — ascender-to-descender of "day" at 24 px |
| `20` | 27 | **20.9** | `numberSize[1] = 32` → digit ≈ 19.5 |
| `hours` | 17 | **13.2** | `labelSize[1] = 20` |
| `54` | 17 | **13.2** | `numberSize[2] = 20` → digit ≈ 12.2 |
| `minutes` | 14 | **10.9** | `labelSize[2] = 16` |
| `17` | 13 | **10.1** | `numberSize[3] = 14` → digit ≈ 8.5 |
| `seconds` | 12 | **9.3** | `labelSize[3] = 14` |

`[MEASURED]` The number ratios are 1 : 0.585 : 0.370 : 0.283 against a declared
1 : 0.571 : 0.357 : 0.250 — agreement to within one AA pixel at every step.
`[OBSERVED]` The face is a bold typewriter/slab form (the `1` has a flag and a
full serif foot), matching `font-family: Courier; font-weight: bold` at `:4702`.
`[OBSERVED]` The pluralisation rule at `:4706`
(`a[i][0] + (a[i][1] != 1 ? "s" : "")`) is visible in the pixels: the frame
reads **`1` / `day`** (singular) alongside **`20` / `hours`**, **`54` /
`minutes`**, **`17` / `seconds`** (plural).

**One copy difference.** `[OBSERVED]` `:4701` ships `t = "launch in"`;
`D-garage-kickstarter-eve-foxter25.png` renders **`launches in`**. That is a datable copy change on the
same axis as the sign-up e-mail helper, and it independently corroborates that
V1 predates the archived bytes.

`[INFERRED]` So the Kickstarter box in `D-garage-kickstarter-eve-foxter25.png` is *not* a separate
`.box.kickstarter` implementation — it is this same countdown component with a
Kickstarter-flavoured header image and a `Read more…` footer. That materially
changes what S16 needs: the CSS class may only supply the skin, while the
countdown body is this JS. Worth verifying against `boxStyles.css` (not staged
for me).

---

## Which form is this? (S34 vs S52-S55)

The brief asks me to distinguish carefully. `[OBSERVED]` **Every form in these
sixteen frames is the sign-up form, not the garage settings form.**

The proof is textual and exact. `srv/index.php:4167-4231` is the `signupform`
block on the garage route. Its `signupformheader` (`:4169`) ships as
`Sign up for your own tank` and is rewritten to **`Sign up another tank`** by
`x_login`'s callback at `:702` (and again at `:2287`, `:4866`, `:10844`,
`:12563`, `:14112`, `:15568` — one copy per route). Its fields are exactly:

| line | element | copy |
|---|---|---|
| `:4174` | `signupusernametext` `.text medium` | `Name your tank` |
| `:4175` | `signupusername` | placeholder `tank name`, colour `#666666`, `maxlength=32` |
| `:4178` | `signupusernamemessage` `.text tiny` | `Something awesome!` |
| `:4182` | `signuppassword1text` | `Password` |
| `:4186` | `signuppassword1message` | `Something secret...` |
| `:4187` | `passwordstrength` | 4 px bar — **S54** |
| `:4190` | `signuppassword2text` | `Password` |
| `:4194` | `signuppassword2message` | `&nbsp;` |
| `:4198` | `signupemailtext` | `Email address` |
| `:4202` | `signupemailmessage` | `Needed to recover your<br/>password and other<br/>important stuff!` |
| `:4207` | `signupcolortext` `.text medium` | `Customize your tank` |
| `:4215` | `signUpTankDesign` | 600 × 250 SWF in a 460 × 100 window at `top:-10; left:-70` |
| `:4229` | `signupbutton` | ` Ready for action ! ` |

The garage **settings** form (S34) is a completely different surface:
`openForm(user)` at `:3755` animates `userpanel-` to width **350** and
`left: 171`, grows `userpanelContent-` to **335** and the wrapper to **450**,
then fades in `userpanelFormInput-<user>` and `userpanelAcceptForm-<user>` at
t = 1700 ms. Its fields are `formname-`, `formpassword1/2-`, `formemail-`,
`formbirthyear-`, `formcountry-`, `formsubscribe-` (`:3782-3788`), and its
placeholder set is different again (`:3495-3498`:
`If you want us to be on a first name basis`, `Something secret...`, `&nbsp;`,
`Needed to recover your password and other important stuff!`).

**None of my sixteen frames shows a 350 px panel, a birth-year field, a country
dropdown or a subscribe checkbox.** So **S34 stays WANTED, untouched.**

### Three generations of sign-up copy, transcribed verbatim

**V4 (`D-garage-2018-url-bar-youtube-toast.png`, `D-garage-2018-scrub-bar-visible.png`) — matches the held bytes exactly:**

> Sign up another tank
>
> Name your tank &nbsp;&nbsp; [ tank name ]
> Something awesome!
> Password &nbsp;&nbsp; [ •••••••• ]
> Something secret...
> Password &nbsp;&nbsp; [ •••••••• ]
> Email address &nbsp;&nbsp; [ email ]
> Needed to recover your
> password and other
> important stuff!
>
> Customize your tank

`[OBSERVED]` Byte-for-byte agreement with `:4174-4208`, including the three-line
break of the e-mail helper. This is a clean confirmation that the served
sign-up block renders as archived.

**V1 (`D-garage-kickstarter-eve-foxter25.png`, `D-garage-kickstarter-countdown-later.png`, and cross-check `C-garage-before-maze-panel.png`) — one string
differs:**

> Email address &nbsp;&nbsp; [ email ]
> So you can recover your
> password if you forget it

`[OBSERVED]` **This string is not in the held bytes.** It is the earlier
`signupemailmessage`, two lines instead of three. Everything else in the V1
form is identical to V4. That makes it a **copy-change marker** for
`S107` ("sign-up template swap dates") — any dated capture showing
`So you can recover your password if you forget it` is pre-swap.

**V3 (`D-userpanel-older-build-collapsed.png` and the whole `revengexx1` group) — an entirely different
template:**

> Get your own tank. <u>Sign up</u> here
>
> First the boring stuff...
>
> ┌─────────────────────────────────────┐
> │ Pick a username &nbsp;&nbsp; [ username ]  │
> │ Something awesome!                  │
> │ Pick a password &nbsp;&nbsp; [ •••••••• ]  │
> │ Something secret..                  │
> │ Password again  &nbsp;&nbsp; [ •••••••• ]  │
> └─────────────────────────────────────┘

`[OBSERVED]` with these specifics:
- "Sign up" is **underlined** (a link) inside the header line.
- `First the boring stuff...` is rendered in a **lighter grey** than the header
  above it — plainly a smaller/secondary class.
- The fields sit inside a **1 px light-grey bordered panel with rounded
  corners**; V1/V4 have no such box.
- `Something awesome!` survives unchanged across all three generations.
- `[UNCERTAIN]` `Something secret..` — I count two dots at this resolution
  where the held bytes have three. The glyphs are 1-2 capture px apart and
  video-blurred. **Do not** treat the two-dot reading as settled.
- The e-mail row is below the frame edge in every V3 frame, so I cannot say
  whether this generation had an e-mail field or what its helper said.

`[INFERRED]` This is a **pre-2015 sign-up template** and is the most useful
thing in this document for **S52-S55** and **S107**: it proves at least three
sign-up copy generations existed, and gives the earliest one's headings and
labels verbatim.

---

## The icon strip (S25) — what four icons look like, and the one open question

`[OBSERVED]` Ordinary (non-moderator) users show **four** icons, left to right,
bottom-aligned, all rendered as small 3-D chrome/pencil objects with soft drop
shadows on white:

**1 — wrench with a "beta" tag.** An open-ended spanner drawn diagonally
(open jaws upper-right, a closed ring with a dark bore at lower-left) with a
rectangular paper **tag reading `beta`** in a serif-ish lowercase, overlapping
the shaft at an angle. `[MEASURED]` art bbox **48.8 × 33.5 CSS**; pure
greyscale (max channel spread 1).

**2 — trophy.** A two-handled loving cup with a **five-pointed star** engraved
on the bowl and sparkle marks, on a **black cube base**. `[MEASURED]` art bbox
**37.9 × 40.8 CSS**; greyscale.

**3 — maze.** An isometric shallow **tray** seen from above-left, with white
raised walls and dark-grey blocks laid out as a small maze; the tray has a
thick dark rim and a black side wall. `[MEASURED]` art bbox
**44.4 × 38.6 CSS**; greyscale.

**4 — form with a warning.** A sheet of paper, top-left corner square and the
bottom-right corner curling up, ruled with grey scribble-lines standing in for
text, and a **yellow warning triangle with a black exclamation mark** sitting
over its lower-right corner. `[MEASURED]` art bbox **40.8 × 40.8 CSS**; the
triangle's yellow sampled at median **`#e3d02e`** — the only colour in the
whole strip.

**Mapping to the JS ids** `[INFERRED]`:

| icon | id | basis |
|---|---|---|
| 3 (maze tray) | `userpanelMaze-` | unambiguous artwork; **S46** gets its answer — the classic icon is a 3-D isometric maze tray, *not* any of the held HTML5-client `mazeCreator*.png` files |
| 4 (form + ⚠) | `userpanelForm-` | a form sheet; and the warning triangle is exactly the "profile incomplete" state that **S26** describes (`updateFormData_cb` swapping `formIconToUpdate.src`, `:4036-4040`). So the **second** sprite in that pair is the same sheet *without* the triangle |
| 2 (trophy) | `userpanelStats-` | trophy = statistics/records; and it is **absent** from the older 3-icon build, matching a later-added stats panel (`openStats`, `:4042`) |
| 1 (wrench + beta) | `userpanelPaint-` | **by elimination**, and because it is present in the 3-icon build where the paint facility demonstrably exists |
| — | `userpanelSherifStar-` | **`[NOT VISIBLE]`** — absent in all six card-showing frames, which is exactly what `:3515` / `:3544` / `:4083` / `:4091` predict for non-moderators (`if (… != null)`) |

**The honest caveat on icon 1.** A wrench with a "beta" label does not
*depict* paint. The elimination argument is: `D-userpanel-older-build-collapsed.png` shows three icons —
wrench+beta, maze, form — and `D-paint-older-build-grid-expanded.png` (same account, ~2 min later in
capture order) shows the paint facility open on that same card. If the wrench
is not `userpanelPaint-`, then that build had no paint icon at all and paint
opened from somewhere else. `[UNCERTAIN]` I could not catch a frame with the
pointer on the wrench immediately before the panel expands. The alternative
reading — that the wrench+beta is a link to a beta client and paint opens by
clicking the tank — is weakened by the fact that `beta.tanktrouble.com` (which
the era-final cookie-consent config at `:3429` references) is a late-2010s
thing, whereas this icon is already present in the oldest build here. I put
this at **probable, not proven**, and it is the single highest-value follow-up
in this document: *one frame of a pointer hovering the wrench, or a cursor
change on it, settles S25 completely.*

**The fade (S25's specific ask).** `[OBSERVED]` The want-list asks for a pair
of frames showing the strip with different icons faded, to measure the
opacity difference. I do not have that pair — but I have something stronger for
the *endpoint*: in `D-garage-kickstarter-eve-foxter25.png`, `D-paint-older-build-grid-expanded.png`, `D-paint-older-build-grid-no-hover.png`, `D-paint-accessory-hover-bandana.png`,
`D-paint-accessory-hover-pirate-hat.png`, `D-paint-can-hover-violet.png` and `D-paint-can-hover-violet-later.png` — seven frames with a sub-panel
open — the icon strip is **completely, undetectably absent**. `[MEASURED]` The
card interior in `D-garage-kickstarter-eve-foxter25.png` between y = 500 and the bottom border contains no
non-white pixel other than the ✓. So `disableUserPanelIcons`' target opacity is
a true **0**, and the 200 ms `Fx.Transitions.linear` tween at `:3503` runs to
completion before any of these frames. **No intermediate opacity value is
captured anywhere in this set** — the 0↔1 midpoints stay on the want-list.

---

## Consequences for the rebuild

### Confirmed

- **`userpanel-<user>` collapsed width 224 and expanded width 692**
  (`srv/index.php:3556`, `:3575`). Measured expanded/collapsed ratio 3.072
  against a predicted 3.071, in a build older than the archived bytes.
- **The panel's box model**: outer 228 × 180.6 CSS, 1 px `#cfcfcf`-family
  border, ~3-4 px radius, white fill. Stable across at least three build
  generations (V1 180.2, V3 178.2, V4 180.6).
- **`position` for `closePaintFacility(user, position)`**: 232 for one user;
  113 / 351 for two. Derived arithmetic `(692 − 228)/2` reproduces both.
- **`userpanelContent-` = 99 px is the tank slot only**; the name label and the
  icon strip live outside it, which is why they survive the 99 → 245 growth.
- **`userpanelswrapper` = 214** with the card flush at the top and ~33 px of
  slack below.
- **`disableUserPanelIcons` fades to a true 0** — the strip is invisible, not
  dimmed, in every open-sub-panel frame.
- **`userpanelSherifStar-` is genuinely conditional** — four icons, not five,
  for ordinary users. The rebuild must not render a placeholder fifth slot.
- **The era-final `signupform` block renders exactly as archived**
  (`:4167-4231`), including the three-line e-mail helper.
- **Route `?garage`** — read directly from a URL bar.

### Contradicted — overhaul owed

Nothing invented has been contradicted, because **nothing in section B has been
built yet** (`S24`: *"Nothing built"*). That is the good news: this evidence
lands *before* the invention, which is precisely the discipline
`docs/standards/VISUAL-EVIDENCE-WANTED.md` asks for in its opening paragraph. Two
warnings for whoever builds it:

1. **Do not treat 99/245/214/360 as build-invariant.** `D-paint-older-build-grid-expanded.png` measures
   an expanded panel of 244 CSS px outer, implying `userpanelContent-` ≈ 163 in
   that generation. The archived numbers are era-final (2018-12) values only.
   Any "restore the classic garage" work aimed at a different year needs its
   own evidence.
2. **Do not assume the centre column was always 692.** In V1 the expanded panel's
   left border sits flush with the 708 px nav strip's left edge, 8 CSS px
   further left than a 692-centred box would. `[UNCERTAIN]` — it may be a 2 %
   scale error on my part — but a rebuild that targets the V1 era should
   measure before committing.

### Still unknown / stays on the want-list

- **S25** — the fifth icon (`userpanelSherifStar-`), the file names of all five,
  the intermediate opacity frames, and positive confirmation that the
  wrench+beta is `userpanelPaint-`.
- **S26** — the *second* form-icon sprite (the sheet **without** the warning
  triangle). Half of the pair is now known.
- **S27** — the sherif-star icon and whatever panel it opens. Untouched.
- **S28** — three of the four accept ✓ variants (`Maze`, `Form`, `Stats`).
  Only `userpanelAcceptPaint-` is captured, and only in its settled state; the
  200 ms fade-in at t = 1700 ms is not caught mid-tween.
- **S29** — the 0 → 2 s open sequence. All my frames are post-settle. Nothing
  here constrains the 700/1200/1700 ms timings or the easing.
- **S30** — the full catalogue. I have four partial windows (10-11 of the
  standard set, 11+ Christmas, ~9 Halloween, 2 gold) and no view of the end of
  any list.
- **S31** — the badge **picker**. Three badge sprites are now known, but no
  chooser control appears anywhere.
- **S32** — whether unowned items are hidden or simply absent. See the three
  candidate readings above.
- **S33** — the stats page. The trophy icon is now known; what it opens is not.
- **S34, S35, S36** — the garage settings form, entirely. **Nothing** in this
  set touches it.
- **S37, S38, S39, S40** — the maze-creator transition from the garage.
- **S7** — the **three**-user stack. Only 1- and 2-user layouts are captured.
- **S8** — the logout animation. The `⊠` control is visible but never clicked.

### New wants to add

1. **`userpanelPaint-` positive identification.** One frame with the pointer
   over the wrench+beta icon (cursor changes to `pointer` per `:3549`), or the
   500 ms window between that click and the panel starting to widen. This is
   the single cheapest shot that would close S25.
2. **Why "beta"?** Any era page or news item explaining a "beta" label on a
   garage control. If the wrench really is the paint icon, the tag needs an
   explanation before it is redrawn.
3. **The end of an accessory list.** Footage where ▶ is clicked until it
   disappears — proves the ◀/▶ hide-at-the-end behaviour symmetrically (only
   the ◀-hidden-at-start case is captured).
4. **A second account's gold toolbox.** Two accounts, same gold box, different
   item counts would settle **S32** in one shot. If the counts match, reading 2
   wins; if they differ, reading 1 wins.
5. **The chip scroll mid-tween.** Two consecutive frames during a ▶ click, to
   fix whether items fade in place (my reading) or translate.
6. **Hover-scale tween.** `D-paint-can-hover-violet-later.png` vs `D-paint-can-hover-violet.png` shows the enlargement is
   animated; its duration, easing and target scale are unknown. Any repeated
   can-click footage gives it, and it doubles as **S51** ground truth.
7. **The three-user row.** A local-multiplayer video with three logins on one
   page, to pin the third `position` value.
8. **`userpanelsheader` content over time.** The older build put
   *"Customize your tank"* above the panel; the 2015 and 2018 builds put
   nothing. When and why it emptied is unknown.
9. **A capture of the `PLAY ONLINE` box *before* its countdown expired** —
   i.e. any frame dated before 2016-10-06 13:00 UTC (see the countdown section
   below). That would show the un-expired branch of `:4684-4711` rendered, and
   is the only state of that widget still unseen on the `?garage` route.
10. **A dated frame showing `launch in` rather than `launches in`** in a
    countdown box, to bracket that copy change (see below).

---

## Recommended edits to existing docs (not applied)

These are suggestions only; I have edited no repo file.

**`docs/standards/VISUAL-EVIDENCE-WANTED.md`**

1. **S24 `MED` → `FETCHED`.** Replace the "What exists / what's missing" cell
   with: *"Geometry measured from Oct-2018 footage: outer 228 × 180.6 CSS,
   1 px #cfcfcf border, ~4 px radius, white fill; username centred at the top in
   #666-family grey (~18 px); tank art 125 × 82 centred, top 24.8; icon strip
   bottom-aligned 133.3 → 174.1, pitch 51.5. `position` = 232 (1 user),
   113/351 (2 users). Still missing: the 3-user row."*

2. **S25 `WANTED` → `PARTIAL`.** *"Four of five icons captured (Oct 2018):
   wrench-with-'beta'-tag, star-engraved trophy on a black base, isometric maze
   tray, ruled form sheet with a yellow ⚠. All greyscale except the ⚠
   (`#e3d02e`-ish). `userpanelSherifStar-` confirmed absent for ordinary users.
   Id↔art mapping certain for Maze/Form, probable for Stats, **inferred by
   elimination** for Paint. Both opacity endpoints seen (icons fully invisible
   with a sub-panel open); no intermediate frame."*

3. **S26 `LOW` → `PARTIAL`.** *"The 'profile incomplete' sprite is a ruled paper
   sheet with a yellow warning triangle over its lower-right corner. The
   'complete' sprite is presumably the same sheet without the triangle —
   unconfirmed."*

4. **S28 `WANTED` → `PARTIAL`.** *"`userpanelAcceptPaint-` captured: a
   hand-drawn green tick with a black outline, brighter green on the long
   stroke, ~26 × 34 CSS, inset ~12 px from the right border and ~14 px from the
   bottom border. Identical art in a much older build. Maze/Form/Stats variants
   and the 1700 ms fade-in still unseen."*

5. **S29 `WANTED` → `PARTIAL`.** *"The settled open state is captured in two
   build generations. Era-final layout: 9+9 mirrored cans flanking the tank, one
   chip row with ◀▶, one row of four toolboxes, ✓ bottom right. Older layout:
   9+9 cans, a 2×8 accessory grid, no toolboxes, no arrows, panel content ≈163
   px not 245. The 0→2 s timing is still unobserved."*

6. **S30 `WANTED` → `PARTIAL`.** *"Toolbox grouping identified: four 3-D boxes —
   grey metal crate (default), Halloween jack-o'-lantern, Christmas present,
   gold star-embossed box — the selected one drawn open. Each carries its own
   spray-can palette AND accessory catalogue (all four palettes sampled to hex).
   The chip row is a sliding window: ◀▶ solid `#c0c0c0` triangles, **one item
   per click**, ◀ hidden on page 1, items cross-fade at the ends. Chip circle
   ≈32 stage px on a ≈34 px pitch; backgrounds `#f1f1f1` normal / `#b4b4b4`
   fitted. Partial catalogues recorded for all four boxes; no list end seen."*

7. **S31 `WANTED` → `PARTIAL`.** *"Three badge sprites observed at a fixed
   lower-right hull anchor: white skull-and-crossbones, yellow sheriff star,
   gold bone. The picker UI is still unseen."*

8. **S32** — keep `LOW`/`WANTED` but sharpen the ask to: *"Two accounts opening
   the SAME gold toolbox. In the one capture held, the gold box offers exactly
   two accessories, centred, with the ◀▶ arrows dropped entirely — no greying,
   no price tag, no empty slots."*

9. **S46 `MED` → `FETCHED`.** *"The classic `userpanelMaze-` icon is a 3-D
   isometric maze tray: white raised walls and dark-grey blocks in a rimmed
   shallow box, greyscale, ~44 × 39 CSS. Confirmed different from the held
   HTML5-client `mazeCreator*.png` tree."*

10. **S16 `MED` → `PARTIAL`.** *"`.box.kickstarter` rendered (countdown:
    'KICK'/'STARTER'/'launches in'/D/H/M/S/'Read more…') and `.box.halloween`
    rendered (glowing jack-o'-lantern over an orange panel, black inset text
    'Let the candy feast begin!')."*

11. **S107** — add: *"Marker string found: the pre-swap
    `signupemailmessage` reads `So you can recover your password if you forget
    it` (two lines) where the held bytes have `Needed to recover your / password
    and other / important stuff!` (three lines). Any dated capture separates
    the two."*

12. **S52-S55** — add a note: *"A third, earlier sign-up template exists:
    header `Get your own tank. Sign up here` ('Sign up' underlined), sub-header
    `First the boring stuff...`, fields inside a rounded bordered panel labelled
    `Pick a username` / `Pick a password` / `Password again`, sub-messages
    `Something awesome!` / `Something secret..`(dot count uncertain)."*

13. **S16** — add: *"The Kickstarter box body is the same countdown component
    as the `PLAY ONLINE` box (`srv/index.php:4674-4719`), not a separate
    implementation. Both of that component's branches are now confirmed against
    pixels: the expired string `Online battles are in heavy development. Try
    now!` (`:4714`) byte-exact in Oct-2018 footage, and the live branch's
    Courier-bold size ladder `[56,32,20,14]` / `[24,20,16,14]` (`:4697`,
    `:4699`) plus the `!= 1` pluralisation (`:4706`) measured in the
    Kickstarter-eve frame. One copy difference: that frame says `launches in`
    where `:4701` ships `launch in`."*

14. Consider adding a **§B footnote** recording the sub-panel width/left
    arithmetic now that it is confirmed:
    `openForm` 350 @ left 171 = `(692−350)/2`; collapsed 228 outer @ left 232 =
    `(692−228)/2`; two panels @ 113/351.

**`DECISIONS.md`** — a new entry along the lines of:

> **2026-08-04 — garage userpanel geometry taken from footage, not invented.**
> Before any of section B was built, sixteen YouTube-derived frames
> (`manualevidence/UI/D-garage-*.png`, `D-paint-*.png`, `D-userpanel-*.png`)
> fixed the userpanel's box model (228 × 180.6 CSS outer, 1 px #cfcfcf border,
> ~4 px radius), its internal stack (name / 99 px tank slot / 41 px
> bottom-aligned icon strip / 6.5 px pad), the per-user `left` values
> (232; 113+351), the four-icon strip for non-moderators, and the paint
> facility's toolbox model. Provenance M2 (`?garage` footage, Oct 2018 and
> ~2015). No invention is superseded because none had been written; the
> OVERHAUL RULE is satisfied prospectively.

**`LEDGER.tsv`** — the guide requires a row per derived asset with
URL/uploader/date/timestamp. I could not recover the source video URLs from the
pixels. `D-garage-2018-url-bar-youtube-toast.png` proves the class (YouTube, full-screen) and
`D-garage-2018-scrub-bar-visible.png` shows a `5:03 / 5:10` player position, which narrows a search
considerably; the V4 pair is datable to **before 18 Oct 2018**. Recommend
opening ledger rows marked *source URL pending* rather than leaving the
evidence unrecorded.

**`docs/standards/DIVERGENCES-SERVED.md` §2** — S23 asks whether the layout ever reflowed
around the AdSense slots. `D-garage-2018-url-bar-youtube-toast.png` shows **both** 160 × 600 slots filled
with live creatives and the centre column in exactly its measured position
(nav-centred, card at `left: 232`). `[OBSERVED]` The layout does not reflow.
Worth recording as settled.
