# Visual evidence — front-page and site chrome

> Analysis of 8 evidence files under `manualevidence/`.
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)

## Scope and provenance

Eight files, given to me in capture order (mtimes are when Ethan saved the crop
on 2026-08-04, **not** when the footage was made — I use them only as an
ordering of what he was stepping through):

| # | File | px | mtime | What it turns out to be |
|---|------|----|-------|--------------------------|
| E1 | `E1-frontpage-2016-ads-filled.png` | 1177×572 | 16:41:37 | Full front page, footer year **2016**, both AdSense skyscrapers filled |
| E2 | `E2-frontpage-2016-halloween-countdown.png` | 1917×897 | 16:43:32 | Full front page, footer year **2016**, **Halloween skin**, live launch countdown, **logged-in Top-10 "Friends"** |
| E3 | `E3-video-thumbnail-premium-crates.png` | 1464×1035 | 16:52:09 | "TANK TROUBLE PREMIUM" crate art — **not classic site chrome** |
| E4 | `E4-advent-calendar-overview-banner.png` | 1918×1045 | 16:53:12 | Advent-calendar overview banner, 25 numbered tankcessories |
| E5 | `E5-left-sidebar-strip-two-user-cards.png` | 225×881 | 17:03:53 | Left sidebar strip only, two logged-in user cards, **~2013** |
| E6 | `E6-frontpage-2013-version-3-7.png` | 1121×637 | 17:11:31 | Full page **~Jan 2013**, game `version 3.7`, YouTube player chrome visible |
| E7 | `E7-teaser-control-chooser-2015.png` | 1286×711 | 17:16:19 | Teaser + control-chooser, footer year **2015**, `version 4.0` |
| E8 | `E8-frontpage-2018-halloween-in-era.png` | 900×561 | 17:27:09 | Front page, footer year **2018**, **Halloween skin**, `version 4.0` — **in-era** |

**These are not one session.** They span at least five distinct site
generations. `[OBSERVED]` The footer year alone separates them: `2007` (E6),
`2007 – 2015` (E7), `2007 – 2016` (E1, E2), `2007 – 2018` (E8). E5 has no
footer in frame but shares two usernames (`creed`, `revengexx1`) with E6, and
every monotone counter in it (scrapyard, visits, tank-owners, that user's Exp)
is **larger** than E6's — so E5 is later than E6 but from the same
account/footage family.

**E6 carries YouTube transport controls** (`[OBSERVED]` a play triangle, a
volume icon, the timecode `0:06 / 13:23`, a scrub bar, a pause button overlaid
at frame centre-right, and a `CC` button bottom-right). That is direct
confirmation of the corpus provenance the repo owner stated: era footage,
frame-grabbed. **M2 at best, never O**, per guide §6.5.

### Scale derivation (used throughout)

Every frame is a screen capture of footage at an unknown zoom. I derive a
per-frame scale from an element whose CSS width is proven in
`srv/index.php`, then quote both capture px and derived CSS px.

`srv/index.php:465` — `<!-- LEFT COLUMN --> <div style="width: 120px; float: left;">`
and `:1090` — `<!-- RIGHT COLUMN --> <div style="width: 120px; float: right;">`.
So every sidebar `.box` is **120 CSS px** wide. `[MEASURED]` the Scrapyard
`.box.special` outer bbox in each frame:

| Frame | box w×h (capture px) | derived scale | box height in CSS px |
|---|---|---|---|
| E1 | 81 × 31 | **0.675** | 45.9 |
| E2 | 168 × 63 | **1.400** | 45.0 |
| E5 | 190 × 71 | **1.583** | 44.8 |
| E6 | 114 × 42 | **0.950** | 44.2 |
| E8 | 115 × 47 | **0.958** | 49.0 |

E7 has no sidebar in frame; `[MEASURED]` its footer string
`Copyright www.purup.com 2007 – 2015` is 354 px wide against E1's
`…2007 – 2016` at 154 px, giving scale ≈ 0.675 × 354/154 = **1.55**.

Two independent cross-checks on E2's 1.400: `[MEASURED]` the red countdown
box, whose container is declared `width: 120px` at `srv/index.php:495`,
measures 168 capture px (168/120 = 1.400); and the footer string ratio
E2/E1 = 318/154 = 2.06 against the box ratio 1.400/0.675 = 2.07.

`[INFERRED]` The Scrapyard box is therefore **120 × ~45 CSS px** in every
frame from ~2013 to 2018 — the box geometry never changed. Falsifier: a frame
where the box's height/width ratio departs from 0.375.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| 1 | Era nav strip has **6 tabs**; icons are newspaper / wrench / T-shirt / speech-bubble / flask after the logo; deselected plates light grey, selected (logo) plate white | `[OBSERVED]`+`[MEASURED]` | VE 10, S2, S114 | no — confirms held `tabNDeselect` art by eye |
| 2 | **No frame shows a raised NEWS/SHOP/FORUM tab.** Every frame is `?game`/root; tab1 is the selected one in all four frames with a visible strip | `[NOT VISIBLE]` | VE 10 | VE 10 stays **PARTIAL** |
| 3 | Nav-tab pitch = **75 CSS px** (E1 51 capture/0.675 = 75.6; E2 105/1.400 = 75.0) | `[MEASURED]` | VE 10, S2 | no |
| 4 | **Pre-shop nav strip: only 5 tabs** in E6 (~2013) — no T-shirt tab — and the logo reads `TANKTROUBLE.com` | `[OBSERVED]` | S110, S114 | no |
| 5 | Scrapyard counter has **two skins across the years**: white/silver plates (E5, E6, E8) and **gold/amber plates** (E1, E2) | `[MEASURED]` hex | S14, S15 | no invention to supersede; new fact |
| 6 | Counter digit counts and verbatim values: E6 `554506351` (9), E5 `665708128` (9), E1 `198167706?` (10), E2 `201505431?` (10), E8 `258???031?` (10) | `[OBSERVED]`/`[MEASURED]` | S14, S15, S78 | no |
| 7 | **A plate caught mid-flip.** In E2 the units plate's lit face is 14 px tall vs 24 px for its nine neighbours, at the same vertical centre, full width | `[MEASURED]` | **S14** | S14 → **PARTIAL** |
| 8 | The flip is a rotation about the plate's **horizontal centre axis** (symmetric compression, single squashed glyph, no split-flap seam, no two-digit drum window) | `[INFERRED]` | S14 | rules out split-flap and drum readings |
| 9 | Roll **direction** still unrecoverable — a symmetric mid-flip frame is direction-blind | `[NOT VISIBLE]` | S14 | S14 stays open on direction |
| 10 | Halloween skin renders in **2016 (E2) and 2018 (E8)**: 120 px orange box (`#f87128`), pure-black inner panel, orange copy **"Let the candy feast begin!"**, jack-o'-lantern PNG overhanging upward | `[OBSERVED]`+`[MEASURED]` | **S16, S106** | S16 → **PARTIAL** |
| 11 | The Halloween skin **also retints the site-wide header band** from light-grey maze tile to orange-on-black maze tile | `[OBSERVED]` | S16, S106 | new — not in any entry |
| 12 | A **live launch countdown box** in E2: header `OPEN BETA`, then `launch in / 2 / days / 15 / hours / 1 / minute / 46 / seconds` in descending type sizes | `[OBSERVED]` | S16, S106 | confirms `srv/index.php:512-546` renderer, contradicts nothing |
| 13 | E1 shows the same slot as a **grey** box: `Online BETA / BETA Membership required` — a third generation of that box | `[OBSERVED]` | S16, S106 | new |
| 14 | E8 shows the era-final state of that box verbatim: `PLAY ONLINE` / `Online battles are in heavy development. Try now!` — the exact string at `srv/index.php:551` | `[OBSERVED]` | S106 | **confirms served bytes** |
| 15 | E4 is an advent-calendar overview: **25 numbered tankcessory sprites**, `Collect all the jolly swag!` / `Log in everyday!` | `[OBSERVED]` | **S18** | S18 → **PARTIAL**; strong candidate for known-lost `AdventCalendarOverview.jpg` |
| 16 | Logged-in **user card layout is constant 2013→2018**: tank render overhanging above, header row `⊠` + username, `Exp. N`, then trophy `N` `(M)` and skull `K` | `[OBSERVED]` | **S6, S7, S8** | S6 → **PARTIAL**, S7 → **PARTIAL** |
| 17 | **Top-10 "Friends" tab, logged in, three times** (E2, E6, E8) — header flips to `Top 10 Exp.` exactly as `srv/index.php:1113` declares | `[OBSERVED]` | **S3** | S3 → **FETCHED** for the logged-in table |
| 18 | Top-10 tab selected/unselected states measured: selected text darkest `#444443`; unselected `#c3c3c5` inside a raised rounded outline | `[MEASURED]` | S3, S114 | gives values for `.bottom2Tabs .tab1/.tab2` |
| 19 | Own-row highlight in the Friends table was **blue `#4c4cb4` in 2013 (E6)** and **gone by 2018 (E8)** | `[MEASURED]` | S3, S105 | new |
| 20 | Visits box **format identical 2013→2018**: `Since 2007-12-16` / big number / `Today: N` / `Online: N` / `Tank owners: N` / `Logged in: N` | `[OBSERVED]` | **S105** | S105 → **PARTIAL (format DONE)** |
| 21 | But `Online` ≠ `Logged in` in all observed frames (508/97, 283/95, 192/67) while they are **equal** in all four archived era-final captures | `[MEASURED]` | S105 | flags the frozen bytes as an atypical state |
| 22 | AdSense skyscrapers **filled, layout unmoved** in E1: 20 px gutters intact, sidebar-outer span 963 CSS vs 932 declared | `[MEASURED]` | **S23** | S23 → **DONE (no reflow)** |
| 23 | In E2 the two ad columns occupy **zero width** and the sidebars spread to the viewport edges — almost certainly client-side ad blocking | `[MEASURED]`+`[INFERRED]` | S23 | worth a caveat in DIVERGENCES §2 |
| 24 | Both taglines observed (`Face your primal instincts…`, `Tanks 'n' Trouble - Watch out…`) are **members of the 10-string pool** at `srv/index.php:169-180` | `[OBSERVED]` | **S1** | pool not broken |
| 25 | Control-chooser screen transcribed in full, twice, including `<name>,` / `choose your controls!` — and the page teaser is **still visible** behind it | `[OBSERVED]` | **S13** | S13 → **PARTIAL** |
| 26 | Right-column box **order changed between 2015 and 2016**: the Facebook widget moved from below Google Play (E7) to above App Store (E1/E2/E8, = era-final) | `[OBSERVED]` | S19, S105 | new dating tool |
| 27 | Facebook box was a **`facebook` status feed** in 2013 (E6) with `Status: / Happy New Year to all TankTroublers!`, an old `✓Like | 7k` button; by 2015 it is the fb-like **Like + Share** pair | `[OBSERVED]` | **S19** | S19 → **PARTIAL** |
| 28 | `Need Help?` box: **red, left column, "Check the F.A.Q."** (E6) → **black, left column, "Check the F.A.Q."** (E5) → **black, right column, "Check the FAQ"** (E1/E2/E7/E8) | `[OBSERVED]` | S85, S105, S114 | new three-step ladder |
| 29 | Feedback box header was `Feedback ?` (E6, 2013) and `Got Feedback?` (2015+), with the body copy `Got ideas? / Found Bugs? / Urge to praise us to the skies? / Then give us your feedback` **unchanged** and matching `srv/index.php:1187-1190` | `[OBSERVED]` | **S11** | S11 → **PARTIAL** (closed state only) |
| 30 | A **red T-shirt product photo** sits in the 2013 right column (E6) — a shop creative in the sidebar | `[OBSERVED]` | S70, S69 | new |
| 31 | The footer **credits line** `Design: Mads Purup, Programming: Brian Bunch Christensen, Server: Søren Boll Overgaard` is present in 2013 (E6) and 2015 (E7), **absent** by 2016 (E1, E2) and absent in the era-final bytes | `[OBSERVED]` | S105, S107 | new dating tool |
| 32 | No clone/rehost watermark anywhere. Every page frame carries `www.purup.com` in the footer; E3 is the only off-site item | `[OBSERVED]` | **S110** | none of these are mislabelled rehosts |
| 33 | Game build watermarks read `version 3.7` (E6) and `version 4.0` (E7, E8) | `[OBSERVED]` | **S110** | S110 → **PARTIAL** for v3.7 dating |

---

## File-by-file analysis

### `UI/E1-frontpage-2016-ads-filled.png` (1177×572, captured 16:41:37) — E1  *(was `{B2424E7E-6BD9-4C82-81FF-1DA8621A4A27}.png`)*

`./UI/E1-frontpage-2016-ads-filled.png`

**Filename claim (repo owner):** none — GUID filename, no embedded description.
Nothing to corroborate or contradict.

**Derived scale: 0.675** (Scrapyard `.box.special` = 81 capture px ÷ 120 CSS px).
This is the lowest-resolution page frame in the set; several small numbers are
at the edge of legibility and I mark those.

**What is drawn — top to bottom, left to right**

- `[OBSERVED]` **Header band**, full width, y 0..30 capture. Light grey with a
  fine texture. `[MEASURED]` mean RGB over x 20..120, y 4..28 =
  `(190.4, 190.0, 190.4)` ≈ `#bebebe`, std 4.5 — a very low-contrast pattern.
  `[UNCERTAIN]` autocontrast reveals a fine irregular grid, consistent with
  the maze tile that is unambiguous in E6, but at 0.675 scale it cannot be
  resolved. Settled by any native-resolution frame of the band.
- `[OBSERVED]` **Nav strip**, clipped at the frame's top edge. The logo tab
  (`TANKTROUBLE` in the bevelled outline face) has a **white** plate; the five
  icon tabs to its right have **light grey** plates. `[MEASURED]` at y=30,
  a sample inside the logo tab = `#fffcff` and inside an icon tab = `#e7e7e7`.
  `[MEASURED]` separator columns at x ≈ 606, 657, 708, 759, 810, 861 →
  **pitch 51 capture px = 75.6 CSS px**.
- `[OBSERVED]` **Left AdSense skyscraper**, a Minecraft-branded creative:
  the blocky `MINECRAFT` logotype at top, a large Steve character holding a
  diamond sword against a cave/hillside background, an orange rectangular
  `PLAY` button near the bottom, and beneath it the small disclaimer
  `*Download of the GamesCrystal.com extension is required`. The AdChoices
  `▷|✕` glyph sits at the creative's top-right corner.
  `[MEASURED]` bbox x 178..290, y 44..453 → 113 × 410 capture = **167 × 607 CSS**
  against the declared `width:160px;height:600px` (`srv/index.php:456-457`).
- `[OBSERVED]` **Left column** (x 302..384 capture):
  - **Scrapyard** `.box.special` — black rounded plate, white `Scrapyard`
    header in a bold sans, then **ten gold plates**.
    `[OBSERVED]` digits read `1 9 8 1 6 7 7 0 6` + a tenth plate that is too
    dark to read. So the value is **1,981,677,06?**.
    `[MEASURED]` plate-face colour (brightest 15 % of the plate band) =
    `#b09a46`; page white sampled at (600,500) = `#ffffff`, so the gold is
    real, not a colour cast on the capture.
    `[MEASURED]` column-max profile: columns x 306..364 peak at 200–255;
    columns x 365..379 peak at only 117–206 — the **last ~two plates are
    markedly dimmer**.
  - **Log In** `.box.standard` — grey header with a `?` at the far left and
    `Log In` centred; a text input showing the placeholder `username`; a
    password input showing **8 bullet glyphs** (browser-autofilled, not typed);
    a `Log in` button and a `Sign up` link on the same row. This matches
    `srv/index.php:562-579` element for element, including the `?` link
    positioned `top: 4px; left: 6px`.
  - **Visits** `.box.standard` — `[OBSERVED]` `Visits` header, then
    `Since 2007-12-16`, `48137787`, `Today: 774`, `Online: 508`,
    `Tank owners: 1793397`, `Logged in: 97`.
    `[UNCERTAIN]` `Online: 508` — the middle glyph could be `6`; and
    `1793397` — the sixth glyph could be `0`. Everything else is unambiguous.
  - **Online BETA** box — `[OBSERVED]` a light-grey/silver box with a faint
    tank-and-gears watermark behind the text, black header `Online BETA`, body
    `BETA / Membership / required` on three lines. This is a **third state** of
    the beta-promo slot that E2 and E8 also occupy, and it is not in the
    era-final bytes.
- `[OBSERVED]` **Centre column** — the Flash stage with a 2-player maze in
  progress: grey walls on a light floor, a red tank at score `11` (left) and a
  green tank at score `10` (right), a green crate near the right of the maze
  and a red mine-like item below it. A gear icon and a speaker icon sit at the
  stage's bottom-left (x ≈ 396, y ≈ 339/355), and the `version 4.0` watermark
  is faintly present at x ≈ 815..855, y ≈ 355.
- `[OBSERVED]` **Right column** (x 867..951 capture), in order:
  **Need Help? / Check the FAQ** (black), **Victories** Top-10,
  **Like | Share** Facebook pair, **App Store** badge, **Google play** badge,
  **Tell a Friend** (black, two stick figures + a speech bubble), and
  **Got Feedback?**. `[OBSERVED]` this is exactly the order in
  `srv/index.php:1091-1215`.
  Top-10 rows, `[UNCERTAIN]` at this scale but readable:
  `george8888 955`, `aedm_71 950`, `szymonrq 782`, `sarekaddouri 755`,
  `123sazoki 706`, `beleko123 688`, `wilmer888 682`, `lordnorbert 671`,
  `killero49 635`, `khad-10 626`. `Weekly` is the dark (selected) tab.
- `[OBSERVED]` **Right AdSense skyscraper**: a Goodgame Studios creative —
  the blue `GG` logo top-left, four stacked parchment cards labelled
  `LVL 1`, `LVL 2`, `LVL 3`, `LVL 4` (the fourth is behind a dark overlay),
  each showing progressively larger groups of blue medieval soldiers, red
  chevron arrows between the cards, and a green `Play` button at the bottom.
  AdChoices glyph at top-right. `[MEASURED]` bbox x 963..1078, y 43..459.
- `[OBSERVED]` **Footer**: `Copyright www.purup.com 2007 – 2016`, single line,
  centred, grey. **No credits line.**

**Measurements**

| Quantity | Capture px | CSS px (÷0.675) | Declared / expected |
|---|---|---|---|
| Left ad creative | 113 × 410 | 167 × 607 | `160 × 600` (`index.php:456`) |
| Right ad creative | 116 × 417 | 172 × 618 | `160 × 600` (`index.php:1080`) |
| Left ad → left column gutter | 12 | 17.8 | `margin-right: 20px` (`:453`) |
| Right column → right ad gutter | 12 | 17.8 | `margin-left: 20px` (`:1076`) |
| Left-column left edge → right-column right edge | 650 | 963 | `120 + 692 + 120 = 932` |
| Ad-outer span | 901 | 1335 | `160+20+120+692+120+20+160 = 1292` |
| Footer text centre | x 625.5 | — | midpoint of the two sidebars = 626.5 |
| Nav-tab pitch | 51 | 75.6 | — |

`[MEASURED]` The footer centre (625.5) and the sidebar midpoint (626.5) agree
to **1 capture px**, i.e. `#gameCopyright` (`width:100%` of `#centerColumn`,
`srv/index.php:328`) is exactly centred between the sidebars. Combined with
the two 17.8 CSS-px gutters and the 963 CSS-px sidebar span, **the page laid
out at its declared widths with both ads filled**.

**Links to the program**

- **S23** — "Full-window frame — confirm layout never reflowed by ads."
  Answered: `[MEASURED]` it did not. The 20 px gutters and the 932-px sidebar
  span survive with both creatives rendered. `docs/standards/DIVERGENCES-SERVED.md` §2's
  claim ("the layout never depended on an ad rendering") is **confirmed from
  the other direction**: it also did not depend on an ad *not* rendering.
- **S23 / third-party creatives** — the Minecraft/GamesCrystal and Goodgame
  creatives are **third-party ad inventory and are NOT candidates for
  reproduction**. Their only value is dating and layout confirmation. Do not
  archive them as site assets; do not add ledger rows.
- **VE 10 / S2** — the strip is visible and `tab1Select` is the raised tab.
  Does not move VE 10.
- **S14/S15** — gold plate skin, 10 plates, value 1,981,677,06?.
- **S105** — Visits format matches `srv/index.php:1069` exactly.
- **S106** — `Online BETA / BETA Membership required` is a seasonal/promo-slot
  state that exists in **no** captured page.
- `srv/index.php:329` — footer string confirmed with the `&ndash;` rendering
  as a true en dash, just with `2016` instead of `2018`.

**What this does NOT show**

`[NOT VISIBLE]` No hover state on any nav tab (S2). No usertrail card (S4).
No logged-in user card — this session is logged out. No favicon/browser tab
(S20). No seasonal skin. The 10th scrapyard plate is unreadable.

---

### `UI/E2-frontpage-2016-halloween-countdown.png` (1917×897, captured 16:43:32) — E2  *(was `{1711C6FA-DEF7-4BF9-9929-23E922BFD96E}.png`)*

`./UI/E2-frontpage-2016-halloween-countdown.png`

**Filename claim (repo owner):** none.

**Derived scale: 1.400.** This is the **highest-resolution page frame in the
whole set** and the best available look at the nav strip, the counter and the
seasonal boxes.

**What is drawn**

- `[OBSERVED]` **Header band retinted for Halloween.** Full width, y 0..~50.
  It is a **maze pattern** — orange/amber corridors on black, tiled, high
  contrast. `[MEASURED]` sampled tones run from `#3a2900` through `#8f6b27`
  on black. This is unmistakably the same tile family as the light-grey band
  in E6, recoloured. `[INFERRED]` the seasonal skin is site-wide, not just a
  sidebar box. Falsifier: a Halloween frame with a grey band.
- `[OBSERVED]` **Nav strip, six tabs**, clipped at the top of the frame.
  Left to right (icons described element by element at 1.4× native, 3× upscale):
  1. **tab1 — game.** The `TANKTROUBLE` logotype in a heavy bevelled outline
     face with a light fill and a dark keyline, on a **white** plate. In this
     frame the `O` of `TROUBLE` is replaced by a **jack-o'-lantern** — the
     Halloween logo variant.
  2. **tab2 — news.** A **rolled/folded newspaper** seen at about −20°, drawn
     in grey line art with soft interior shading; the word `NEWS` is printed
     on the visible face in a blackletter/Old-English face.
  3. **tab3 — garage.** An **open-end wrench**, running lower-left to
     upper-right, the C-jaw at the top right, a round hole through the handle's
     lower end.
  4. **tab4 — shop.** A **short-sleeved T-shirt**, front view, collar at the
     top, with a small dark **tank silhouette** printed on the chest.
  5. **tab5 — forum.** A plain rounded **speech bubble** with the tail at the
     lower-left.
  6. **tab6 — lab.** A **round-bottomed flask** tilted to the right, neck to
     the upper right, with liquid in the bulb and four or five bubbles in it.
  `[MEASURED]` separator columns at x = 910, 1012, 1118, 1223, 1328 and the
  strip ends at x ≈ 1433 → **tab pitch 105 capture px = 75.0 CSS px**, with
  each separator only 2–3 capture px (≈ 2 CSS px) wide. Deselected plate fill
  sampled at (1200, 30) = `#e7e7e7`; the selected logo plate at (900, 30) =
  `#fcfcfc`.
- `[OBSERVED]` **Left column** (x 27..194 capture = 120 CSS px):
  - **Scrapyard** — see the measurement block below.
  - **Countdown box.** `[OBSERVED]` a **solid red** rounded rectangle
    (`[MEASURED]` sample at (100,400) = `#ff1c11`, i.e. the declared
    `background-color: #ff0000` at `srv/index.php:495` with JPEG/video bleed),
    120 CSS px wide, containing, on separate centred lines:

    ```
    OPEN BETA
    launch in
    2
    days
    15
    hours
    1
    minute
    46
    seconds
    ```

    `[OBSERVED]` the four number/label pairs descend in type size exactly as
    `srv/index.php:526-528` specifies —
    `numberSize = [56, 32, 20, 14]`, `labelSize = [24, 20, 16, 14]` — and the
    numerals/labels are set in a **monospaced slab** face, matching
    `font-family: Courier; font-weight: bold` at `:530`. The pluralisation
    rule at `:534` is visible too: `1` takes the singular `minute` while `2`,
    `15` and `46` take `days`, `hours`, `seconds`.
    **The header string is `OPEN BETA`, not `PLAY ONLINE`.** The era-final
    bytes at `srv/index.php:493` read `PLAY ONLINE`. So this is an **earlier
    generation of the same widget**.
  - **Halloween box.** `[MEASURED]` orange body x 27..194, y 600..731 →
    **120 × 94 CSS px**. `[OBSERVED]` a photographic **jack-o'-lantern** —
    brown-orange ribbed gourd, black curled stem, two angled triangular eyes
    and a wide zig-zag mouth, both glowing pale yellow — sits **above** the
    box and overhangs it, exactly the negative-`top` image trick used for
    `christmasPresent18.png` at `srv/index.php:501-502`. Inside the orange
    frame is a **pure-black** panel (`[MEASURED]` `#000000`) carrying the
    orange copy, two lines, centred:
    `Let the candy` / `feast begin!`
    `[MEASURED]` the copy's orange, averaged over its orange pixels, `#ac5d27`.
  - **Log In box**, identical in structure to E1's; password field again shows
    8 bullets.
  - Frame bottom cuts here. `[NOT VISIBLE]` whatever is below the Log In box —
    which is where `#loginmessageswrapper` (`srv/index.php:581`) puts the
    logged-in user cards.
- `[OBSERVED]` **Centre column** — a 2-player game running.
  `BallisticBlaster` (red tank, score 1) vs `Laika` (dark grey/black cat-shaped
  tank, score 0); a small watermark `olla maze` / `by ojt` at the lower right
  of the stage and `version 4.0` below it. Gear + speaker icons bottom-left.
- `[OBSERVED]` **Right column** — order: `Need Help? / Check the FAQ` (black),
  Top-10, `Like | Share`, `Available on the App Store`, `GET IT ON Google play`,
  `Tell a Friend` (black, two stick figures, the right one with a speech bubble
  containing a tank), `Got Feedback?` (black header, white body,
  `Got ideas? / Found Bugs? / Urge to praise us / to the skies? / Then give us your / feedback`
  and an envelope illustration below). This is the era-final order.
- **The Top-10 box is in its logged-in "Friends" state.** `[OBSERVED]`
  the header reads **`Top 10 Exp.`** — the exact string of
  `#top10FriendsHeader` at `srv/index.php:1113`, which is `display:none` in
  every archived byte. The rows, verbatim:

  ```
  ati1089            31018
  BallisticBlas...   16162
  Neon-Wolf123       10502
  h-devil            10137
  KiwiKing            9056
  Utomic-Raider       8675
  Moonwalker9...      7837
  Banana-Bom...       6789
  shezz               5757
  kkcoolcat           5442
  ```

  `[UNCERTAIN]` `16162` could be `16182`; `8675` could be `8875`.
  `[OBSERVED]` three names are **truncated with a literal `...`** — direct
  visual confirmation of `text-overflow: ellipsis; overflow: hidden;
  white-space: nowrap` on the 75 px name cell at `srv/index.php:1114`.
  `[OBSERVED]` `BallisticBlas...` is the same player driving the red tank in
  the stage, so this **is** the logged-in user's friend list.
- `[OBSERVED]` **Footer**: `Copyright www.purup.com 2007 – 2016`, one line, no
  credits.

**Measurements — the scrapyard counter**

`[MEASURED]` Box bbox x 27..194, y 85..147 → 120 × 45 CSS px.
`[MEASURED]` Plate band y 114..137 = 24 capture px = **17.1 CSS px** tall.
`[MEASURED]` Plate runs (gold threshold, x from 27):

```
plate  1: x  34.. 47  w 14      pitch to next 16
plate  2: x  50.. 62  w 13      14
plate  3: x  64.. 78  w 15      16
plate  4: x  80.. 93  w 14      16
plate  5: x  96..108  w 13      15
plate  6: x 111..124  w 14      15
plate  7: x 126..140  w 15      16
plate  8: x 142..155  w 14      15
plate  9: x 157..170  w 14      15
plate 10: x 173..186  w 14      —
```

→ **10 plates**, pitch **15.6 capture = 11.1 CSS px**, plate face
**~9.7 CSS px** wide, **gap ~1.4 CSS px**.
`[OBSERVED]` digits, verbatim, left to right: `2 0 1 5 0 5 4 3 1` and a tenth
plate whose glyph is squashed and dim. **Value = 2,015,054,31?**.
`[MEASURED]` plate face colour = `#af8d2c` (gold).

**The mid-flip.** `[MEASURED]` per-plate row profile (max red channel across
each plate's width, y 110..142):

| y | p1 | p3 | p9 | **p10** |
|---|---|---|---|---|
| 114 | 114 | 119 | 90 | **47** |
| 119 | 136 | 181 | 124 | **112** |
| 125 | 210 | 226 | 212 | **167** |
| 131 | 148 | 203 | 206 | **125** |
| 137 | 131 | 126 | 134 | **61** |

Taking "lit" as > 100: plates 1–9 are lit from y 114 to y 137 = **24 rows**;
plate 10 is lit only from y 119 to y 132 = **14 rows**. The two bands share the
same centre (y 125.5). Plate 10's peak (167) is ~25 % below its neighbours'
(~210–236). Plate 10's **width is unchanged**.

`[INFERRED]` A plate whose lit face shrinks vertically by 42 % **symmetrically
about its own centre line**, keeps full width, and darkens, is a plate rotated
out of the screen plane about a **horizontal axis through its centre**. The
apparent rotation is `acos(14/24) ≈ 54°`.
Three readings are ruled out by this geometry:
- **not a split-flap**: a hinged top leaf falling would compress only the upper
  half and leave the lower half at full height — the compression here is
  symmetric;
- **not an odometer drum**: a drum shows two partial glyphs separated by a
  horizontal seam inside a fixed-height window — here the window itself
  shrinks and only **one** squashed glyph is present;
- **not a horizontal/sideways roll**: that would compress width, not height.
`[UNCERTAIN]` the glyph on the rotating face reads as a loop over a short spur
— consistent with a squashed `9`, possibly `8` or `6`. Not settleable here.
`[NOT VISIBLE]` **roll direction.** A symmetric mid-rotation frame is
direction-blind: up-roll and down-roll produce the same silhouette at 54°.
Only two frames a few tens of ms apart, or a frame at < 45° with a readable
glyph orientation, can settle it.

**Measurements — layout, and the ad columns**

`[MEASURED]` Scrapyard box left edge x 27; `Need Help?` box right edge x 1869
(box width 167 capture = 119 CSS px). Sidebar-outer span = 1843 capture =
**1316 CSS px**, against the declared `120 + 692 + 120 = 932`.
`[MEASURED]` The footer centre sits at x 947.5 and the sidebar midpoint at
948.0 — again centred, so `#centerColumn` is simply pushed right.
`[MEASURED]` At row 120, x 0..20 is `#fffeff` (page white) and x 1900..1916 is
`#c4c4c3` — the browser's **vertical scrollbar**. So the viewport is
≈ 1895 capture px = **1354 CSS px**, and the two sidebars sit ~19 CSS px from
the left edge and ~34 CSS px from the right.

`[INFERRED]` The two skyscraper columns occupy **zero horizontal space** in
this frame. The float model explains it exactly: with the banner wrappers
removed, the left float is 120 wide and the right float group is
692 + 120 = 812, so a 1354-px container leaves a ~420-px gap between the left
column and the centre column, which is what is measured. Had the wrappers been
present at their declared `width:160px` plus 20 px margins
(`srv/index.php:453`, `:1076`), the left column would begin 180 CSS px in, not
19. The most likely cause is a **client-side ad blocker with cosmetic
filtering** in the capturing browser; a 2016-vintage markup without the
fixed-width wrapper is the alternative. Falsifier either way: any 2016 frame
of the same page with the ad columns filled (E1 is exactly that, and it has
them).

**Links to the program**

- **VE 10** — the strip is visible at the best resolution in the corpus, and
  all five deselected icons are now describable by eye. But the raised tab
  here is **tab1 (game)**, so this does **not** upgrade `tab2Select.jpg`,
  `tab4Select.jpg` or `tab5Select.jpg`. VE 10 stays **PARTIAL**.
- **S2** — no hover state captured; `tabNSelect2.jpg` remains unexplained.
- **S3** — **directly answered for the logged-in Friends table.** Header
  string `Top 10 Exp.` confirmed against `srv/index.php:1113`; the table is
  name + Exp, ten rows, ellipsis truncation confirmed against `:1114`.
- **S14/S15** — plate geometry, colour and a mid-flip, above.
- **S16** — `.box.halloween`-class rendering observed; also a red countdown
  box that is **not** any of `.christmas/.halloween/.glitch/.kickstarter`
  but the inline-styled `PLAY ONLINE` widget of `srv/index.php:493-546` in an
  earlier `OPEN BETA` guise.
- **S106** — a **fourth** state of the beta-promo slot is now known
  (`OPEN BETA` + live countdown), alongside E1's `Online BETA / BETA
  Membership required` and E8's/era-final's `PLAY ONLINE`.
- **S23** — see the ad-column measurement; this is a *counter-example frame*
  worth recording, not a contradiction of DIVERGENCES §2.
- `srv/index.php:512-546` — the countdown renderer's size ladder and
  pluralisation are confirmed on screen.

**Dating**

`[INFERRED]`, with the reasoning stated and both branches given:
the era-final page freezes the countdown target at `1475758800000`
(`srv/index.php:514`) = **2016-10-06 13:00:00 UTC**. If that is the target this
frame is counting to, the frame is **2016-10-03 21:58:14 UTC**. The competing
reading is that the Halloween skin implies late October and the target was a
later, since-overwritten date. `DECISIONS.md:396` records the Halloween box as
byte-identical at **20171119** and **20181020** — i.e. the site kept it up at
least from 20 Oct to 19 Nov — which shows the seasonal window is wide and
therefore **does not rule out** an early-October appearance. I do not pick a
winner. What is certain: the frame is 2016 (footer), it is **later than E1**
(scrapyard 2,015,054,31? > 1,981,677,06?), and it precedes an open-beta launch
by 2 d 15 h 1 m 46 s.

**What this does NOT show**

`[NOT VISIBLE]` The logged-in user card(s) — cut off below the Log In box.
No ad creatives. No favicon. No nav-tab hover. No `Weekly` table in the
logged-in state (only `Friends` is showing).

---

### `UI/E3-video-thumbnail-premium-crates.png` (1464×1035, captured 16:52:09) — E3  *(was `{F9D54A4F-227A-40FC-82B6-EF757DFEBBD9}.png`)*

`./UI/E3-video-thumbnail-premium-crates.png`

**Filename claim (repo owner):** none.

**What is drawn**

Two stacked regions with no page chrome at all.

- `[OBSERVED]` **Upper band, y 0..~455, full frame width.** Background: a
  TankTrouble maze — flat mid-grey walls on a near-white floor, with black
  round bullets, grey smoke trails, and three floating weapon icons (a blue
  rounded-square holding a pale sphere; a grey rounded-square holding a
  concentric-arc "ray" glyph; a green rounded-square holding a rocket).
  Foreground, left to right: a **yellow/black hazard-stripe block** with steel
  cog wheels; a **grey T-shirt** printed with a green tank and the words
  `TANK TROUBLE` on two lines; a **green crate** with two steel hinges and a
  large green `K` on its face; the title
  **`TANK TROUBLE PREMIUM`** in heavy extruded **gold** 3-D lettering, with a
  gold toy tank (blue turret cap) resting on the top edge; a **black crate**
  with a faceted diamond on its face; more cogs; and at the right a
  **rainbow-gradient crate** with two brown leather straps and a pink/white
  **unicorn horn** rising from it.
- `[OBSERVED]` **Lower region, y ~460..1035.** A white sheet (x ≈ 36..1436,
  with black letterboxing outside it) carrying the same three crates —
  green-`K`, black-diamond, rainbow-unicorn — rendered larger and isolated.

**Measurements**

`[MEASURED]` frame corner samples are dark blue-grey (`(2,53,62)` top-left,
`(43,150,165)` bottom-right) and the first ~4 rows fade in from dark — a
video vignette / fade artefact, not page content.
`[MEASURED]` no white page background, no 120-px column, no nav strip, no
footer anywhere in the frame — I checked the full edge rows.

**What I think it is, stated candidly**

`[INFERRED]` This is **promotional / marketing artwork for "TankTrouble
Premium", not classic-site chrome**. The evidence: the maze is drawn in the
flat modern (HTML5-client) style rather than the classic Flash renderer's
palette; the weapon icons are rounded-square HUD tiles that appear nowhere in
the classic page; "Premium" is a subscription product of the modern
tanktrouble.com, and the classic 2017-2018 pages reconstructed here contain no
reference to it (`grep` of `srv/index.php` for "Premium" — no hits in any of
the strings I searched). The composition (wide hero band over a white content
sheet) reads like a **web page hero or a video thumbnail**, and the outer
letterboxing is consistent with a video frame.

`[UNCERTAIN]` The green `K` crate is very likely a **Kickstarter** crate — the
project holds `kickstarterCrates120x12B-editor-howto-step5-nearly-solid.png`, `kickstarterLogo100x39.png` etc.
(LEDGER 96-101) and `kickstarterCrates554x227.png` is known-lost (LEDGER 321).
I cannot compare pixels because `srv/images/` is not in the staged tree, so I
will not claim a match. Someone with the repo checked out should diff this
crate against `kickstarterCrates120x12B-editor-howto-step5-nearly-solid.png`.

**Links to the program**

- `[NOT VISIBLE]` Nothing here bears on S1-S23 chrome entries.
- **S110 (mislabelled clone rehosts)** — this frame is the one item in my set
  that is **not** classic tanktrouble.com. It should be flagged in any ledger
  or index so it is never mistaken for era site material.
- **S30/S32 (accessory catalogue)** — the unicorn-horn and diamond crate art
  might be modern-client loot-box art; do **not** feed it into the classic
  accessory catalogue.

**What this does NOT show**

`[NOT VISIBLE]` No nav, no sidebar, no counter, no footer, no seasonal box,
no ad slot, no URL bar. Nothing datable to the 2017-2018 target era.

---

### `UI/E4-advent-calendar-overview-banner.png` (1918×1045, captured 16:53:12) — E4  *(was `{054A27F4-2171-41A2-BF64-B3C65F976AF0}.png`)*

`./UI/E4-advent-calendar-overview-banner.png`

**Filename claim (repo owner):** none.

**What is drawn**

A single landscape banner filling the frame, no page chrome.

- `[MEASURED]` **Background**: pale cyan, `#c2f9fe` at frame centre falling to
  `#9bebf8` toward the edges (a gradient, or video-compression falloff).
- `[OBSERVED]` **Top-left**: a green wrapped **present** with a red ribbon and
  bow and a small brown gift tag; **bottom-right**: a second, similar green
  present with a red bow, angled the other way.
- `[OBSERVED]` **Title line**, red, heavy rounded display face, centred:
  **`Collect all the jolly swag!`**
  `[MEASURED]` bbox x 18..1802, y 90..214 → cap height ≈ 125 px;
  glyph red averaged over its red pixels = **`#f42009`**.
- `[OBSERVED]` **Bottom line**, same face and colour:
  **`Log in everyday!`** — written as one word `everyday`, not `every day`.
  `[MEASURED]` bbox x 497..1707, y 900..1016.
- `[OBSERVED]` Two **candy-cane bars** run the full width, striped diagonally
  in red / white / green. `[MEASURED]` the upper bar occupies rows 252..283
  (32 px); the lower bar's green rows end at 875.
- `[OBSERVED]` Between the bars, **two rows of accessory sprites with red
  hand-lettered day numbers beneath each**. `[MEASURED]` row 1 label centres
  run x 272 → 1593 (12 labels, pitch ≈ 120 px); row 2 label centres run
  x 284 → 1571 (13 labels, pitch ≈ 107 px). **25 sprites, numbered 1 to 25.**
  The numerals are hand-drawn — `[OBSERVED]` the `0` in `10` is drawn small and
  round like a lowercase `o`, and the `4` in `24` has an open top.

**The 25 sprites, described one by one** (`[OBSERVED]` unless marked):

| Day | What is drawn |
|---|---|
| 1 | Red **Santa hat** with a white fur brim and a white bobble |
| 2 | A green-and-red rounded shape — `[UNCERTAIN]` reads as a **holly/ivy leaf pair with berries**, or a folded green cap with red patches |
| 3 | A red **hanging ornament / stocking-shaped bauble** with yellow stars and a loop of red cord at the top |
| 4 | A brown curved **wand/branch** with a yellow five-pointed **star** at the tip |
| 5 | A white two-ball **snowman** with a black top hat, an orange carrot nose, black coal eyes and thin stick arms |
| 6 | A brown **gingerbread man** with a smiling face and two magenta buttons |
| 7 | A red-and-white striped **candy cane** |
| 8 | A grey brick **chimney** with a red Santa hat perched on its rim |
| 9 | A pair of brown **antlers** (left side) |
| 10 | A single red ovoid — `[UNCERTAIN]` a **reindeer nose** (pairs with 9) |
| 11 | A draped string of small **fairy lights**, dark beads in blue/red/green on a thin wire |
| 12 | A yellow **hand bell** with a brown handle |
| 13 | A green base holding three lit white **candles** with yellow flames |
| 14 | A white block above a pale-blue pointed shard — `[UNCERTAIN]` an **icicle** or a **tooth** |
| 15 | A red **Christmas stocking** with a white/grey cuff |
| 16 | A tan oval **tag/biscuit** with a dark paw print and a thin metal ring |
| 17 | A large red **ribbon bow** with two trailing tails |
| 18 | Four pale-blue **icicles** hanging in a row |
| 19 | A smaller red **ribbon bow** |
| 20 | A red **Santa hat** with a white brim and a yellow **star** at its tip |
| 21 | A green **wreath** with a red bow at the top |
| 22 | A cluster of green **holly leaves with red berries** |
| 23 | A long white shape with a black eye and a rounded snout — `[UNCERTAIN]` a **polar-bear/snow-creature rug** or a snow drift |
| 24 | A brown **sack** overflowing with red and blue wrapped presents |
| 25 | A red **pennant flag** on a brown pole reading `MERRY` / `X-MAS` in green hand lettering |

**Links to the program — this is the big one for S18**

- `[OBSERVED]` `srv/index.php:8552-8567` is the news item `25-12-2012`,
  headed **"Merry Christmas"**, whose body reads
  *"Our laboratory is now decorated with the 25 Christmas tankcessories that we
  recovered from an old archive box…"* and which embeds
  `<img src='images/AdventCalendarOverview.jpg'/>` at **line 8561**.
  `LEDGER.tsv:232` records `srv/images/AdventCalendarOverview.jpg` as
  **known-lost** — no era CDX row, no held bytes.
  `[INFERRED]` This frame shows **exactly 25 numbered Christmas tankcessories**
  in the site's own house style, captioned in the site's own vocabulary
  (`jolly swag` appears verbatim at `srv/index.php:504` and `:6205`; "log in
  every day … collect all the jolly swag" at `:6205` and `:7101`). This is a
  **strong candidate for `AdventCalendarOverview.jpg`**. What would falsify it:
  a different aspect ratio to the archived CDX size, or a second era image with
  the same content. What would confirm it: any CDX thumbnail, or a frame of the
  `?news` page scrolled to the 25-12-2012 item showing this image in situ.
- **Provenance discipline.** Even if the identification holds, this is a
  **video frame of a JPEG**, upscaled and re-compressed. Under guide §6.5 it is
  **M2 at best**. `AdventCalendarOverview.jpg` **stays `known-lost` in the
  LEDGER**; what changes is that its *content* is now known and a redraw is
  possible. Do not promote the row.
- **S18** — "8 day-sprites held, ~16 unheld/unnamed". The project holds
  `christmasPresent{2,4,6,8,14,15,18,23}.png` (LEDGER 76-82, 303).
  `[INFERRED]`, offered as a **testable prediction, not a claim**: if
  `christmasPresentNN.png` is the day-`NN` tankcessory rather than a generic
  wrapped present, then the held files should depict, respectively, the day-2
  green/red leaf pair, the day-4 star wand, the day-6 gingerbread man, the
  day-8 chimney, the day-14 icicle/tooth, the day-15 stocking, the day-18
  icicle row and the day-23 white creature. **Anyone with `srv/images/`
  checked out can settle this in one minute** — I could not, because the staged
  tree contains only `srv/index.php`. If the held files are all wrapped
  presents instead, then `christmasPresentNN.png` is the *news-box* sprite and
  the 25 items here are a separate, wholly unheld set — which would itself be a
  useful negative result.
- **S18 / `christmasPresentOpen.jpg`** (LEDGER 304, known-lost) — `[NOT VISIBLE]`.
  This banner is the overview, not the opened-present state.
- **S78** — the banner is a news-page image, so it belongs to the "~30
  known-lost news images" bucket as well.

**What this does NOT show**

`[NOT VISIBLE]` No page chrome, so no confirmation of *where* it sat on the
page, at what rendered width, or whether it was clickable. No advent-calendar
**UI** (the interactive per-day claim flow) — only the overview art.
`[NOT VISIBLE]` The `More News` advent box that `srv/index.php:494-508`
renders (`Dec. 18th` + `christmasPresent18.png` + `Log in now to unlock
today's jolly swag`) is **not** in this frame.

---

### `UI/E5-left-sidebar-strip-two-user-cards.png` (225×881, captured 17:03:53) — E5  *(was `{4AEB403B-1EA9-467D-A910-229E048760FB}.png`)*

`./UI/E5-left-sidebar-strip-two-user-cards.png`

**Filename claim (repo owner):** none.

**Derived scale: 1.583** (Scrapyard box 190 capture px ÷ 120 CSS px). A tall
narrow crop of the **left sidebar only**, at the second-highest resolution in
the set.

**What is drawn — every element, top to bottom**

1. **Scrapyard** `.box.special`. `[MEASURED]` bbox x 21..210, y 19..89 →
   120 × 44.8 CSS px. Black rounded plate; `Scrapyard` in white bold sans,
   centred, in the header area.
   `[OBSERVED]` **Nine plates, white/silver faces with black digits**, reading
   verbatim **`665708128`**.
   `[MEASURED]` plate-face colour = `#eeeeee` (vs `#af8d2c` gold in E2 —
   these are genuinely different skins, not a colour cast).
   `[MEASURED]` plate runs x 24..41, 45..61, 65..82, 86..103, 107..123,
   127..144, 148..165, 169..185, 189..206 → pitch **20.6 capture = 13.0 CSS px**,
   face width 18 capture = **11.4 CSS px**, gap ≈ **1.6 CSS px**.
   `[MEASURED]` per-column maxima across all nine plates run 226–255 with no
   dimming anywhere — **no plate is mid-flip in this frame**, and the last two
   digits read cleanly as `2` and `8`.
2. **Log In** `.box.standard`. `[OBSERVED]` `?` at the far left of the grey
   header, `Log In` centred; `username` placeholder; 8 password bullets;
   `Log in` button + `Sign up` link. Identical to E1/E2.
3. **User card 1.** `[OBSERVED]` A **tank render overhangs the card from
   above**, its lower third overlapping the card's grey header row. The tank is
   brown/tan with an orange-tipped barrel and a white **skull-and-crossbones
   pennant** accessory. Below it:
   - grey header row: a small **`⊠`** glyph (a square enclosing an ×) at the
     far left, then the username **`creed`** centred in grey;
   - white content: **`Exp. 7820`** in a larger grey face, centred;
   - a single row of two stat groups: a **trophy/cup outline icon** followed by
     `585` with `(0)` set beneath it in smaller type, then a **skull icon**
     followed by `1028`.
4. **User card 2.** Same structure. Tank: red hull with an orange
   **jack-o'-lantern head**, a black hanging **lantern** on a curved arm, a
   black **ghost/eye** accessory and a gold **star**. Username
   **`revengexx1`**; **`Exp. 10500`**; trophy `2259` `(2)`; skull `2957`.
5. **Need Help?** box. `[OBSERVED]` **Black** rounded box, white/pale copy on
   two lines: **`Need Help?`** (larger) and **`Check the F.A.Q.`** (smaller).
   `[OBSERVED]` note the **periods**: `F.A.Q.`, not `FAQ`.
   `[OBSERVED]` It is in the **left** column here, under the user cards.
6. **Visits** `.box.standard`. `[OBSERVED]` verbatim:

   ```
   Visits
   Since 2007-12-16
   17858418
   Today: 9805
   Online: 283
   Tank owners: 518873
   Logged in: 95
   ```

   All seven lines are crisp; no glyph is ambiguous.

**Links to the program**

- **S6 — "Logged-in user card in login sidebar."** `[OBSERVED]` The card's
  content model is now known: **username, `Exp. <n>`, a trophy count with a
  parenthesised secondary count, and a skull count**, with the tank SWF
  overhanging above the header. `srv/index.php:598-657` builds this HTML via
  `x_login`; `:655-657` contains the `71 + 10` IE fudge, and 71 px is the row
  height. `[MEASURED]` card height here (grey header top to white body bottom,
  card 1) ≈ y 218..300 capture = 82 capture = **52 CSS px** for the visible box,
  with the tank occupying roughly another 45 CSS px above it — i.e. the
  ~71 px row is card + tank overlap, not card alone. **S6 → PARTIAL.**
- **S7 — "Multi-user stack (up to 3 logged in)."** `[OBSERVED]` Two cards
  stacked, and **the Log In box is still shown above them** — exactly what
  `srv/index.php:593-596` predicts (`if (numUsers == 3) … display = 'none'`,
  else visible). The stack grows **downward** from the Log In box, consistent
  with `#loginmessageswrapper` sitting after `#login` at `:581`.
  **S7 → PARTIAL** (2 of 3 observed; the 3-user case, where the Log In box
  disappears, is still unseen).
- **S8 — "Logout animation + card removal."** `[OBSERVED]` The logout affordance
  is the **`⊠` glyph at the left of the card header**. `[NOT VISIBLE]` the
  animation itself, and no confirm dialog can be ruled in or out from a still.
  **S8 stays WANTED**, but the control's position and art are now known.
- **S105 — frozen live regions, "confirm formatting stayed constant across
  years."** `[OBSERVED]` This box's six lines are **character-for-character the
  same template** as the frozen bytes at `srv/index.php:1069`
  (`Since 2007-12-16<br/><div …>68466319</div>Today: …<br/>Online: …<br/>Tank
  owners: …<br/>Logged in: …<br/>`), including the space after each colon and
  the absence of thousands separators. **Format confirmed unchanged.**
- **S14/S15** — the **white-plate, 9-digit** counter generation.
  `LEDGER 191-198` holds `scrapyard06/10/11.swf` referenced by no era page;
  `[INFERRED]` this frame shows one of those SWF-era widgets, since the Phaser
  widget of `srv/index.php:475-491` is only introduced with
  `includes/scrapyard.js` (dated **O 2017-02-21** in the comment at
  `srv/index.php:185-187`). **S15 → PARTIAL.**

**Dating**

`[INFERRED]` The counter reads 665,708,128. Three milestone news items give
hard anchors: `images/300000000.jpg` in the item dated **10-05-2011**
(`srv/index.php:9113-9122`), `images/500000001.jpg` in **05-09-2012**
(`:8781-8790`), and `images/999MillionAndCounting.jpg` in **09-11-2014**
(`:8131-8141`, whose copy says *"less than 1 million short of running out of
digits … we will impact 1B in less than 24 hours"*). Linear interpolation
between the 500 M and 999 M anchors (499 M over 795 days = 628 k/day) puts
665.7 M at **≈ 2013-05-27**. An independent estimate from the Visits counter —
E6 at 15,295,988 with `Today: 10443`, E5 at 17,858,418, a gap of 2.56 M ≈ 256
days after E6 — puts E5 at **≈ 2013-09**. `[UNCERTAIN]` So **mid-to-late 2013**,
±3 months. The rate is not constant, so neither estimate is tight.

`[OBSERVED]` A secondary, hard confirmation of ordering: the 999 M news copy
says the counter was about to "run out of digits" at 9 digits, and E5/E6 have
**9 plates** while E1/E2/E8 have **10** — the widget gained a plate when the
count crossed 1 billion, exactly as that news item foreshadows.

**What this does NOT show**

`[NOT VISIBLE]` No nav strip, no centre column, no right column, no ad slots,
no footer, no seasonal box. The crop is the left column and nothing else.

---

### `UI/E6-frontpage-2013-version-3-7.png` (1121×637, captured 17:11:31) — E6  *(was `{1DA5327B-1A7B-4CD8-8582-E83744D7051C}.png`)*

`./UI/E6-frontpage-2013-version-3-7.png`

**Filename claim (repo owner):** none.

**Derived scale: 0.950.** A complete page, plus **YouTube player chrome**
along the bottom of the frame.

**What is drawn**

- `[OBSERVED]` **Header band** — a light-grey **maze pattern**, unmistakable at
  this scale: short orthogonal corridors, dead ends, a 90°-only lattice. This
  is the same asset family that E2 shows recoloured orange-on-black.
- `[OBSERVED]` **Nav strip — FIVE tabs, not six.** Left to right:
  1. `TANKTROUBLE.com` logotype on a **white** raised plate — note the
     **`.com` suffix**, which the era logo does not have;
  2. newspaper with `NEWS`;
  3. wrench;
  4. speech bubble;
  5. flask.
  **There is no T-shirt tab.** `[INFERRED]` the shop tab was inserted later;
  in the era strip the T-shirt sits at position 4 (`srv/index.php:302`,
  `?shop` → `tab4Deselect.jpg`), so the whole strip was renumbered when it
  was added. Falsifier: a dated frame between this one and 2015 showing six
  tabs with a different order.
- `[OBSERVED]` **Left AdSense/ad column** — a "DEER DRIVE" hunting-game
  creative: the game logotype on a torn-paper banner, a deer in a rifle
  crosshair over a forest, simulated bullet holes, and a large orange `PLAY!`
  button, with fine print `*Click … download … Optional software included.`
  `[MEASURED]` bbox x 0..169, y 66..599 — it runs off the left frame edge, so
  its true width is not measurable.
- `[OBSERVED]` **Left column**: Scrapyard, Log In, one user card, `Need Help?`,
  Visits.
  - Scrapyard: `[MEASURED]` box 114 × 42 capture = 120 × 44.2 CSS px;
    **nine white plates**, `[MEASURED]` face `#e6e6e6`; pitch 12.4 capture =
    **13.1 CSS px**. `[OBSERVED]` verbatim **`554506351`**.
  - User card: tank = red hull with a grey **tombstone** accessory (a faint
    `RIP` is `[UNCERTAIN]` legible on it), a black hanging lantern, a gold
    star. `⊠` + **`revengexx1`**; **`Exp. 9453`**; trophy `2068` `(0)`;
    skull `2730`.
  - **`Need Help?` box is RED here** — `[OBSERVED]` a red rounded box with a
    red header bearing `Need Help?` in white, and a white content strip
    bearing `Check the F.A.Q.` in dark grey, inside a red border.
  - Visits, verbatim: `Since 2007-12-16` / `15295988` / `Today: 10443` /
    `Online: 192` / `Tank owners: 354232` / `Logged in: 67`.
    `[UNCERTAIN]` the final `67` could be `87`.
- `[OBSERVED]` **Centre column** — a game in progress: `revengexx1` (red tank,
  score 0, its name also floating in red over the maze) vs `Laika` (the black
  cat tank wearing a red Santa hat, score 0, name floating in black). A yellow
  circular cursor highlight sits mid-maze. Gear + speaker icons bottom-left.
  `[OBSERVED]` the build watermark reads **`version 3.7`**.
- `[OBSERVED]` **Right column**, in order:
  1. **`Top 10 Exp.`** box in its **Friends** state, rows verbatim:
     `revengexx1 9453` (rendered in **blue**), `creed 7500`, `Laika 1000`.
     Only three rows — the rest of the 110-px table is blank white.
     `Weekly` is the pale raised tab, `Friends` the dark selected one.
  2. **`Tell a Friend`** — a **RED** box: red field, white header text, two
     white stick figures (the left one holding a cup/can to its ear, joined by
     a string to the right one) and a speech balloon containing a dark tank.
  3. **App Store** badge (black, `Available on the App Store`).
  4. An **old-style Facebook Like button**: `✓Like` in a grey pill next to a
     bordered count bubble reading **`7k`**.
  5. A **Facebook status box**: a blue `facebook` header bar, then
     `Status:` and `Happy New Year to all TankTroublers!`.
  6. A **red T-shirt** product photograph with a dark tank graphic on the chest.
  7. **`Feedback ?`** — black header (note the space before the `?`), body
     `Got ideas?` / `Found Bugs?` / `Urge to praise us…` (partly hidden behind
     the YouTube pause button).
- `[OBSERVED]` **Footer, two lines**, centred:

  ```
  Copyright www.purup.com 2007
  Design: Mads Purup, Programming: Brian Bunch Christensen, Server: Søren Boll Overgaard
  ```

  `[MEASURED]` bbox of line 1: x 535..713. No year *range* — just `2007`.
- `[OBSERVED]` **YouTube transport controls** overlay the bottom of the frame:
  a play triangle at the far left, a speaker icon, the timecode
  **`0:06 / 13:23`**, a red progress sliver, a `CC` button at the far right,
  and a large translucent **pause button** centred over the right column.

**Links to the program**

- **Provenance** — this frame is the corpus's own receipt. `[OBSERVED]` It is a
  YouTube video frame at t = 0:06 of a 13:23 video. Per the brief and guide
  §6.5 everything derived from it is **M2 at best**. A LEDGER row for anything
  taken from this family must carry URL / uploader / date / timestamp, and the
  timestamp `0:06` is recoverable from the frame itself.
- **VE 10 / S2** — five-tab strip, `tab1` raised. Does not move VE 10 (the era
  strip is a different generation).
- **S3** — **the clearest Friends-table capture in the set.** Header
  `Top 10 Exp.`, three friends, own row highlighted.
- **S19 — Facebook box.** `[OBSERVED]` In 2013 the right column carried **two**
  Facebook elements: a Like button with a `7k` count, and a **status feed box**
  with a blue `facebook` header. The era-final page has neither — it has the
  single `div class="box fb-like" data-width="120" data-layout="button"
  data-action="like" data-share="true"` at `srv/index.php:1161`, which renders
  as the Like + Share pair seen in E1/E2/E7/E8. **S19 → PARTIAL**: the era
  render is now confirmed (see E1/E2/E8) and a pre-era generation is
  documented.
- **S11 — feedback box.** `[OBSERVED]` closed-state copy and header
  (`Feedback ?`). `[NOT VISIBLE]` the open/expanded form. **S11 stays WANTED
  for the open state.**
- **S69/S70 — shop.** `[OBSERVED]` A shop product photograph (red T-shirt with a
  tank print) rendered **in the right sidebar**, not on `?shop`. That is a
  placement nobody had recorded. `LEDGER 338` lists `hoodies.png` as
  known-lost and `LEDGER 318` `shopCollection00.jpg` likewise; `[UNCERTAIN]`
  this may be one of them or one of the 9 held product PNGs — undecidable
  without `srv/images/`.
- **S110 — "Old gameplay videos date each build by visible UI."**
  `[OBSERVED]` `version 3.7` on screen, alongside a datable page (see below).
  `LEDGER 139-161` lists all of `TankTrouble_v1.x-v3.7` as known-lost.
  **S110 → PARTIAL**: this frame pins v3.7 to a page state datable to
  ~Dec 2012 – Jan 2013. It is not the SWF, but it is a dated sighting.
- **S105** — Visits format again identical to `srv/index.php:1069`.
- **S85 (`/faq/index.html` popup)** — `[OBSERVED]` the FAQ box copy in 2013 is
  `Check the F.A.Q.`, versus `Check the FAQ` in the era-final bytes
  (`srv/index.php:1098`). A copy edit, not a route change.

**Dating**

`[INFERRED]` Four independent signals converge on **late Dec 2012 – Jan 2013**:
(a) the Facebook status reads `Happy New Year to all TankTroublers!`;
(b) `Laika` wears a **Santa hat** in the stage;
(c) the scrapyard reads 554,506,351, which linear interpolation between the
500 M (2012-09-05) and 999 M (2014-11-09) anchors places at **≈ 2012-12-01**;
(d) the footer year is `2007` alone, i.e. before the range form appeared.
The New-Year greeting is the sharpest of the four, so **early January 2013** is
my best single estimate. Falsifier: any archived `?news` item showing the
"Happy New Year" status came from a different year.

**What this does NOT show**

`[NOT VISIBLE]` No seasonal sidebar box (the Christmas box, if there was one,
is not present — the promo slot is simply absent from the left column).
No mid-flip plate. No favicon. No nav hover. No `Weekly` Top-10 state.

---

### `UI/E7-teaser-control-chooser-2015.png` (1286×711, captured 17:16:19) — E7  *(was `{85AAE09B-C1C4-4455-917C-7F9240741A7B}.png`)*

`./UI/E7-teaser-control-chooser-2015.png`

**Filename claim (repo owner):** none.

**Derived scale ≈ 1.55** (footer-string width ratio against E1; see the scale
section). This frame is the **teaser + control-chooser state** — S13's
pre-game state — with the right column partly in shot. The left column and
both ad slots are outside the crop.

**What is drawn**

- `[OBSERVED]` **Page teaser text**, two lines, centred over the stage:

  ```
  The most explosive 2 player tank game online
  Face your primal instincts and prepare for savage encounters at the office
  ```

  Line 1 is larger and darker (`class="text large"`), line 2 smaller and grey
  (`class="text normal"`) — matching `srv/index.php:312-317` exactly.
- `[OBSERVED]` **The control-chooser screen inside the stage.** A very large
  pale-grey **tank in profile**, barrel raised to the upper right, drawn as a
  flat silhouette with a lighter fill and a mid-grey outline, sitting on a
  soft grey ground shadow. Behind it, a faint grey **maze pattern** watermark.
  Overlaid on and around the tank, three control affordances, each with a
  caption beneath:
  1. **left** — a single dark keycap marked `Q`, set apart, plus a four-key
     cluster arranged as `E` above `S D F`. Caption **`Press Q`**.
  2. **centre** — a single dark keycap marked `M`, plus a four-key cluster of
     **arrow keys**: `↑` above `← ↓ →`. Caption **`Press M`**.
  3. **right** — a grey **computer mouse** in three-quarter view with a cable
     curling to the left. Caption **`Press left`**.
- `[OBSERVED]` Beneath the tank, a small dark-blue player tank with two small
  accessories above it, then two centred lines:

  ```
  _-Death-_,
  choose your controls!
  ```

  The username carries a **trailing comma** on its own line; the instruction is
  on the second line and ends with an exclamation mark.
- `[OBSERVED]` **`version 4.0`** watermark, grey, at the stage's lower right.
  Gear and speaker icons at the stage's far left (x ≈ 20, y ≈ 527/558).
- `[OBSERVED]` **Right column**, partly cropped at the frame's right edge, in
  order: `Victories` Top-10 → `Available on the App Store` → `GET IT ON Google
  play` → `f Like | Share` → `Tell a Friend` (**black** here, not red) →
  `Got Feedback?` with the full body copy and the envelope illustration.
  `[OBSERVED]` **the Facebook pair sits BELOW Google play in this frame**,
  where the era-final order (`srv/index.php:1160-1168`) puts it **above** the
  App Store box. E1, E2 and E8 all show the era-final order.
- `[OBSERVED]` Top-10 in the **Victories / Weekly** state, rows verbatim:

  ```
  swis4              1271
  fivip456789123     1266
  karimkhalil1234    1231
  RENJIE             1185
  SwagRanger45       1064
  akashi4            1026
  Warsome             973
  biggles12           842
  kavkasiuri1         818
  nika1234567         792
  ```

  `[UNCERTAIN]` `1266` could be `1268`; `1026` could be `1028`.
  `[OBSERVED]` `fivip456789123` (14 chars) is **not** truncated — it fits the
  75 px cell — whereas E2's `BallisticBlas...` is. Consistent.
- `[OBSERVED]` **Footer, two lines**:

  ```
  Copyright www.purup.com 2007 – 2015
  Design: Mads Purup, Programming: Brian Bunch Christensen, Server: Søren Boll Overgaard
  ```

**Measurements**

`[MEASURED]` Top-10 tab text, darkest pixel: `Weekly` (selected) `#4d4945`;
`Friends` (unselected) `#ccc6c6`. `[OBSERVED]` the **unselected** tab is drawn
inside a raised rounded-rect outline that reads as a separate pill; the
**selected** tab is flush with the box body and has no outline on its outer
side. This is the inverse of the naive "selected = raised" reading and it is
consistent across E2, E6, E7 and E8.

**Links to the program**

- **S1 — tagline pool completeness.** `[OBSERVED]` The tagline is
  `Face your primal instincts and prepare for savage encounters at the office`.
  I checked it against the pool literal at `srv/index.php:169-180`: it is
  **line 174**, character-for-character. **It is a pool member. No 11th string
  here.** The pool is not broken by this frame. (S1 can never be closed by
  positive sightings alone — only an unlisted string closes it, negatively.)
- **S13 — game stage slide-up transition.** `[OBSERVED]` This frame is the
  **pre-slide state**: `#TankTroubleTeaserText` is still displayed *and* the
  SWF is already showing the control-chooser. `srv/index.php:442` calls
  `document.getElementById('TankTroubleTeaserText').style.display='none'` and
  `:433-443` polls for the stage's `top` reaching `-10px` from `60px`
  (`:324`). `[INFERRED]` the teaser is therefore **not** hidden when the
  chooser appears — it is hidden later, when the slide-up runs. That
  constrains the sequencing: chooser first, teaser+slide second.
  **S13 → PARTIAL** (states known; duration/easing still unmeasured — that
  needs consecutive frames, which a single still cannot give).
- **S19** — `Like` + `Share` pair confirmed rendering at ~120 px.
- **S23** — `[NOT VISIBLE]`, the ad columns are outside the crop.
- **S105/S107** — the credits line is **present** in 2015 and **absent** in
  2016 (E1, E2) and in the era-final bytes. That is a new, cheap dating cut at
  the 2015/2016 boundary, independent of the sign-up-template windows.

**What this does NOT show**

`[NOT VISIBLE]` No nav strip (above the crop), no left column, no scrapyard,
no seasonal box, no ads, no favicon, no logged-in card in the sidebar (the
player name only appears inside the SWF).

---

### `UI/E8-frontpage-2018-halloween-in-era.png` (900×561, captured 17:27:09) — E8  *(was `{5EC85EF6-FE4D-4A53-BB60-1F9FF21CDC37}.png`)*

`./UI/E8-frontpage-2018-halloween-in-era.png`

**Filename claim (repo owner):** none.

**Derived scale: 0.958.** **This is the only frame in my set that is squarely
inside the 2017-2018 target era**, and it matches the served bytes in several
places verbatim.

**What is drawn**

- `[OBSERVED]` **Nav strip** — only the bottom 2–3 px of the tab plates are in
  frame. `[NOT VISIBLE]` icons, selected state, everything. The bottom edges do
  show a wide left plate and several narrow right plates, consistent with the
  six-tab strip, but nothing is measurable.
- `[OBSERVED]` **Left column**:
  1. **Scrapyard** — `[MEASURED]` box 115 × 47 capture = 120 × 49 CSS px;
     **ten plates, white/silver**, `[MEASURED]` face `#f8f8f8`, plate band
     y 43..62 = 20 capture px = **20.9 CSS px** tall (the `#scrapyard` div is
     `height: 18px` with `padding: 4px 0 0 0` at `srv/index.php:468`, so its
     `clientHeight` is 22 — the plates fill it). `[MEASURED]` pitch
     11.33 capture = **11.8 CSS px**, face ≈ 10.4 CSS px, gap ≈ 1.4 CSS px.
     `[OBSERVED]` digits: `2 5 8` then **three plates occluded by the
     pumpkin's stem**, then `0 3 1` and a final plate reading `9` or `6`.
     Value = **2,58?,??0,31?**.
     `[MEASURED]` per-column maxima are 197–255 uniformly across all ten
     plates, including the last — **no plate is mid-flip here**.
     `[UNCERTAIN]` at 20× the last two plates show a faint horizontal line at
     mid-plate height, which would be a split-flap seam; but it is 1 px at
     native scale and I would not build anything on it.
  2. **Halloween box** — `[MEASURED]` orange frame x 22..135 = **119 CSS px**
     wide, y 120..193 = **74 CSS px** tall; frame colour sampled at (25,150) =
     **`#f87128`**; inner panel `#000000`; copy orange, brightest `#e4784b`.
     `[OBSERVED]` The **same jack-o'-lantern** as E2 overhangs the box from
     above, its stem crossing the Scrapyard plates. Copy, verbatim, two lines:
     `Let the candy` / `feast begin!`
  3. **PLAY ONLINE box** — `[MEASURED]` x 22..134 = **118 CSS px** wide,
     y 207..305 = **103 CSS px** tall; red sampled at (60,230) = `#f13529`.
     `[OBSERVED]` header **`PLAY ONLINE`** in white bold caps on the red
     header block, then the body, three lines:
     `Online battles` / `are in heavy` / `development.` / `Try now!`
     `[OBSERVED]` This is **verbatim** `srv/index.php:551` —
     `t = "Online battles are in heavy development. Try now!";` — the branch
     the countdown takes once its target time has passed. **The served bytes
     render exactly this on screen.**
  4. **Log In** box — `?` + `Log In` header, `username` placeholder, password
     bullets, `Log in` + `Sign up`.
  5. **User card** — tank overhanging above: an indigo/purple hull with a
     grey hooded **reaper** figure whose wings are patterned with `10101`
     binary digits, plus a gold **bone**. Header: `⊠` + **`mr_enderman`**.
     Body: **`Exp. 7697`**; trophy `3470` `(0)`; skull `3532`.
  6. **Visits** — `[OBSERVED]` cut off by the frame's bottom edge after two
     lines: `Since 2007-12-16` and **`66977586`**. `[NOT VISIBLE]`
     `Today` / `Online` / `Tank owners` / `Logged in`.
- `[OBSERVED]` **Centre column** — teaser + control-chooser, exactly as E7:

  ```
  The most explosive 2 player tank game online
  Tanks 'n' Trouble - Watch out, before you turn to rubble
  ```

  and, under the tank:

  ```
  mr_enderman,
  choose your controls!
  ```

  with the same `Press Q` / `Press M` / `Press left` affordances and the same
  key clusters (`Q` + `E S D F`; `M` + arrow keys; a mouse).
  `[OBSERVED]` **`version 4.0`** watermark.
- `[OBSERVED]` **Right column**, cropped at the frame edge: `Need Hel[p?]` /
  `Check the FA[Q]`, `Top 10 Ex[p.]` in the **Friends** state, `Like`/`Sh[are]`,
  `Available o[n the] App St[ore]`, `GET IT ON Google [play]`,
  `Tell a Frie[nd]`, `Got Feedba[ck?]` with the body copy and envelope.
  Friends rows, names only (scores are off-frame):
  `mr_enderman`, `_nothing_`, `chaos_boy`, `doggy_king`, `crash_david`,
  `choasboy`. `[MEASURED]` all six rows' darkest text pixel is neutral grey
  (`#6d6d68`, `#636b5e`, `#7c7f7d`) — **the own-row blue highlight seen in E6
  is gone**.
- `[OBSERVED]` **Footer**: `Copyright www.purup.com 2007 – 2018`, single line,
  no credits — **byte-identical in content to `srv/index.php:329-330`**.

**Measurements**

`[MEASURED]` Left column left edge x 21 = 22 CSS px from the frame edge;
`Need Help?` box left edge x 818, so its right edge is at ≈ 933 capture =
974 CSS px. Sidebar-outer span ≈ **952 CSS px** against 932 declared — i.e.
**the normal, un-spread layout**, in contrast to E2's 1316.

**Links to the program**

- **S106 / DIVERGENCES §3** — `[OBSERVED]` the **Halloween box and the
  `PLAY ONLINE` box coexist**. `DECISIONS.md:396` records the Halloween box
  byte-identical at `20171119` and `20181020`; this frame shows the same box
  in the same slot with a 2018 footer.
  `[MEASURED]` Visits total 66,977,586 here vs the frozen era-final
  68,466,319 (`srv/index.php:1069`); the difference is 1,488,733. Two other
  archived captures give 68,374,157 and 68,466,315, i.e. ~92 k over the ~2.7 d
  between them ≈ 34 k/day. At 34 k/day the 1.49 M gap is **44 days** before the
  era-final capture. `docs/standards/DIVERGENCES-SERVED.md` §3 dates that capture
  `20181214/18`. 44 days earlier is **≈ 2018-10-31**.
  `[INFERRED]` **This frame is Halloween 2018**, and the arithmetic is a
  genuinely independent confirmation of the seasonal reading.
- **S16** — `.box.halloween` (or whatever the class is) now has measured
  geometry and colours in two separate years.
- **S14** — the **era** counter is the white-plate, 10-plate widget with
  ~11.8 CSS px pitch. That is the geometry the Phaser rebuild
  (`srv/includes/scrapyard.js`, driven from `srv/index.php:475-491`) must
  match. `[MEASURED]` value ≈ 2.58–2.59 billion in late Oct 2018, against the
  frozen seed `scraps = 1785664230` in
  `docker/mysql/init/60-scrapyard.sql` (per DIVERGENCES §5). **The seed is
  ~800 million low for the era-final date** — it is the 2016-01-26 archived
  value, and DIVERGENCES already labels it ARBITRARY, but this frame quantifies
  how far off it is.
- **S1** — tagline `Tanks 'n' Trouble - Watch out, before you turn to rubble`
  is `srv/index.php:178` verbatim (straight apostrophes, a spaced
  hyphen-minus). **Pool member.**
- **S13** — second instance of the pre-game state, this time with the teaser
  and chooser both up on an **in-era** page.
- **S3** — third Friends-table sighting, in-era.
- **S110** — `[OBSERVED]` no clone branding, no rehost watermark, footer reads
  `www.purup.com`. This is tanktrouble.com.

**What this does NOT show**

`[NOT VISIBLE]` The nav strip's icons. The Visits box's lower four lines. The
Top-10 scores. Any ad creative. The favicon. The seasonal header-band tint
(the band is above the crop).

---

## Consequences for the rebuild

### Confirmed

1. **Sidebar column geometry.** `120 CSS px` for both columns and the
   Scrapyard `.box.special` at `120 × ~45`, unchanged across five frames
   spanning 2013→2018. Confirms `srv/index.php:465` and `:1090`.
2. **Nav strip geometry, era generation.** Six tabs; icon-tab pitch
   **75.0–75.6 CSS px**, measured independently in two frames at different
   scales; separators ~2 CSS px; deselected plate fill ≈ `#e7e7e7`; selected
   plate fill ≈ `#fcfcfc`. Confirms the strip in `srv/index.php:302`.
3. **All five deselected tab icons confirmed by eye** at 1.4× native:
   newspaper (`NEWS` in blackletter), wrench, T-shirt with a tank print,
   speech bubble, flask with bubbles.
4. **Right-column box order, era.** FAQ → Top-10 → fb-like → App Store →
   Google Play → Tell a Friend → Got Feedback. Exactly `srv/index.php:1091-1215`.
5. **Visits box template.** Six lines, labels and punctuation identical
   2013→2018 to `srv/index.php:1069`. **S105's "did formatting stay constant"
   question is answered: yes.**
6. **Footer.** `Copyright www.purup.com 2007 – <year>` with a real en dash,
   `class="text small gray"`, centred on `#centerColumn`
   (measured to 1 capture px in E1 and E2). Confirms `srv/index.php:328-330`.
7. **`PLAY ONLINE` box copy.** `Online battles are in heavy development. Try
   now!` rendered on screen in an in-era frame, verbatim to
   `srv/index.php:551`.
8. **Countdown renderer.** The descending size ladder and singular/plural rule
   of `srv/index.php:526-534` are visible on screen (E2).
9. **Top-10 ellipsis truncation** (`srv/index.php:1114`) — visible as literal
   `...` on three names in E2.
10. **Tagline pool not broken.** Two sightings, both pool members
    (`srv/index.php:174`, `:178`).
11. **S23 — the layout never reflowed around the ads.** E1 has both 160×600
    slots filled and the 20 px gutters and 932-px sidebar span are intact.

### Contradicted — overhaul owed

Nothing in the served bytes is contradicted. But three **invented or
assumed** things are now superseded or newly constrained:

1. **The scrapyard counter's motion model.** Nothing in the repo commits to a
   flip mechanism, but `docs/standards/DIVERGENCES-SERVED.md` §5 leaves it open. E2
   settles the *mechanism*: **whole-plate rotation about a horizontal centre
   axis**, ruling out split-flap and odometer-drum readings. Under THE
   OVERHAUL RULE, if the Phaser rebuild in `srv/includes/scrapyard.js` (or any
   test pinned to it) assumes a drum or a split-flap, that is a wholesale
   rewrite against this evidence, not a tweak. **The file to check is
   `srv/includes/scrapyard.js` and whatever renders `#scrapyard`.** I could not
   check it — it is not in the staged tree.
2. **The frozen scrapyard seed.** `scraps = 1785664230` (the 2016-01-26
   archived value). E8 measures **≈ 2.58–2.59 billion** at ≈ 2018-10-31, and
   E1/E2 measure 1.982 B and 2.015 B in 2016. So the seed is ~0.8 B below the
   era-final reality, and the era-final page would have shown a **10-plate**
   counter beginning `2 5 8 …` or `2 6 …`. This does not force a change (the
   no-invention default stands), but it should be recorded in DIVERGENCES §5
   that the true era value is now *observed within a range*, not merely unknown.
3. **Ad-slot geometry assumption.** DIVERGENCES §2 says "the layout never
   depended on an ad rendering". E1 confirms that with ads filled. E2 shows the
   other tail: when the ad **wrappers** are absent (ad blocker), the sidebars
   spread to the viewport edges by ~380 CSS px. Worth a sentence in §2 so that
   nobody screenshots the rebuild through a blocker and calls it a divergence.

### Still unknown / stays on the want-list

- **VE 10 — selected-state news / shop / forum tabs.** `[NOT VISIBLE]` in all
  eight files. Every frame with a strip is on `?game`/root, so `tab1Select` is
  the only selected art shown. `tab2Select.jpg`, `tab4Select.jpg`,
  `tab5Select.jpg` **stay `O?`**. VE 10 stays **PARTIAL**.
  What I *can* add: the strip's pitch (75 CSS px) and its deselected plate
  colour, so any future capture can be validated for scale before use.
- **S2 — `tabNSelect2.jpg`.** No hover frame anywhere. Stays **WANTED**.
- **S14 — roll direction.** Stays **WANTED**. The mechanism is now known; the
  direction is not, and a single symmetric mid-flip frame can never give it.
  New, sharper want: **two consecutive video frames of the gold-plate counter**
  (E2's generation), or any frame at < 45° rotation where the glyph's
  orientation is readable.
- **S15 — pre-2017 scrapyard SWFs.** Two skins are now observed
  (white 9-plate ~2013, gold 10-plate 2016), but neither can be tied to a
  specific held file (`scrapyard06/10/11.swf`). Stays **PARTIAL**.
- **S18 — advent calendar UI.** The *overview* art is now known (E4). The
  **interactive UI** (a day being clicked, `christmasPresentOpen.jpg`, the
  per-day claim flow) is still entirely unseen. Stays **PARTIAL**.
- **S11 — feedback box open state.** Only the closed state, twice. Stays
  **WANTED**.
- **S4 — usertrail hover card.** `[NOT VISIBLE]`. Stays **WANTED**.
- **S8 — logout animation.** The `⊠` control is located and drawn; the
  animation is not. Stays **WANTED**.
- **S20 — favicon.** `[NOT VISIBLE]` in all eight; no browser tab strip is in
  any frame. Stays **WANTED**.
- **S12, S5, S9, S10** — no sighting.
- **S3 — the logged-in `Weekly` state.** Three Friends-tab sightings, zero
  logged-in Weekly sightings. Minor, but the `Victories` header with a
  logged-in user's row highlighted is still unseen.

### New wants to add

1. **A frame of the gold-plate (2016) scrapyard widget in two consecutive
   video frames.** Rationale: settles S14's roll direction, which the
   mid-flip frame cannot. FOOTAGE TRIGGER: any 2016 front-page video, sidebar
   in shot, ≥ 2 s — the units digit is rolling continuously at ~1.4 M
   scraps/day.
2. **The `?news` item dated `25-12-2012` scrolled into view**, to confirm E4
   is `AdventCalendarOverview.jpg` in situ and to get its rendered width.
3. **A 2016 front page with the ad columns *filled* AND a seasonal box**, to
   separate "the ad column collapsed" from "the 2016 markup had no fixed-width
   wrapper" (the E2 question).
4. **Any frame of the `OPEN BETA` countdown box on a *different* day**, which
   would let the target timestamp be solved from two remaining-time readings
   and would date E2 to the minute.
5. **A 3-user logged-in stack** (S7's remaining case), where the Log In box
   should vanish per `srv/index.php:593-596`.
6. **Any frame showing `Online:` and `Logged in:` in 2017-2018.** The four
   archived era captures all have them **equal**, while every observed
   2013-2016 frame has `Online` 2-5× larger. One in-era frame settles whether
   the equality is a real behaviour change or a coincidence of the crawls.

---

## Recommended edits to existing docs (not applied)

**`docs/standards/VISUAL-EVIDENCE-WANTED.md`**

- **Entry 10** — keep status `PARTIAL`, but append to the "Needed to upgrade to
  O" paragraph:
  > *Checked against manual-evidence frames `UI/E1-frontpage-2016-ads-filled.png` (2016) and
  > `UI/E2-frontpage-2016-halloween-countdown.png` (2016, 1.4× native): both show the six-tab strip with
  > **tab1 selected**, so neither upgrades tab2/4/5Select. Useful by-products:
  > icon-tab pitch measured at **75.0–75.6 CSS px**, separators ~2 CSS px,
  > deselected plate fill `#e7e7e7`, selected plate fill `#fcfcfc`; all five
  > deselected icons confirmed by eye. A pre-shop **five-tab** strip with a
  > `TANKTROUBLE.com` logo exists (`UI/E6-frontpage-2013-version-3-7.png`, ~Jan 2013) — the shop tab
  > was inserted later and renumbered the strip.*
- **S3** — change status to **FETCHED (logged-in Friends table)**. Reason:
  three independent frames (`E2-frontpage-2016-halloween-countdown.png`, `E6-frontpage-2013-version-3-7.png`, `E8-frontpage-2018-halloween-in-era.png`) show
  the `Top 10 Exp.` header of `srv/index.php:1113` with a live friend list;
  ellipsis truncation confirmed; tab colours measured (selected `#444443`,
  unselected `#c3c3c5`). Remaining gap: the logged-in **Weekly** state.
- **S6** — `WANTED` → **PARTIAL**. Card model observed: tank SWF overhanging
  above the header, header row = `⊠` logout glyph (left) + username (centred),
  body = `Exp. <n>` then a trophy count with a parenthesised secondary count
  and a skull count. Identical in 2013 (`E5-left-sidebar-strip-two-user-cards.png`) and 2018
  (`E8-frontpage-2018-halloween-in-era.png`).
- **S7** — `WANTED` → **PARTIAL**. Two-card stack observed with the Log In box
  still visible above it (`E5-left-sidebar-strip-two-user-cards.png`). Three-card case still unseen.
- **S8** — keep `WANTED`; add "the logout control is a `⊠` glyph at the left of
  the card's header row (`UI/E5-left-sidebar-strip-two-user-cards.png`, `UI/E8-frontpage-2018-halloween-in-era.png`)".
- **S11** — keep `WANTED`; add that the **closed** state is now doubly
  confirmed and that the header string was `Feedback ?` in 2013 and
  `Got Feedback?` from 2015, with the body copy unchanged.
- **S14** — `WANTED` → **PARTIAL**. Add:
  > *Mid-flip caught in `UI/E2-frontpage-2016-halloween-countdown.png`: the units plate's lit face is 14 px
  > tall against 24 px for its nine neighbours, same vertical centre, full
  > width, ~25 % dimmer — a rotation of ≈54° about the plate's **horizontal
  > centre axis**. Rules out split-flap (asymmetric) and odometer drum (two
  > partial glyphs behind a fixed window). **Direction still unknown** —
  > symmetric mid-flip frames are direction-blind. Plate metrics: gold
  > generation 10 plates, pitch 11.1 CSS px, face 9.7, gap 1.4, band 17.1 tall;
  > era/Phaser generation 10 plates, pitch 11.8, face 10.4, gap 1.4, band 20.9
  > tall; 2013 generation 9 plates, pitch 13.0, face 11.4, gap 1.6.*
- **S15** — keep `PARTIAL`; add that **two visually distinct pre-Phaser skins**
  are now on record — white/silver 9-plate (~2013, `E5-left-sidebar-strip-two-user-cards.png`,
  `E6-frontpage-2013-version-3-7.png`) and gold/amber 10-plate (2016, `E1-frontpage-2016-ads-filled.png`,
  `E2-frontpage-2016-halloween-countdown.png`) — and that the plate count grew from 9 to 10 when the count
  crossed 1 B, as the `09-11-2014` news item foreshadows
  (`srv/index.php:8141`).
- **S16** — `WANTED` → **PARTIAL**. Halloween skin rendered in 2016 and 2018:
  120 CSS px box, frame `#f87128`, inner panel `#000000`, orange copy
  `Let the candy` / `feast begin!`, jack-o'-lantern PNG overhanging above.
  **Add the new fact that the skin also retints the site-wide header band**
  from a light-grey maze tile to an orange-on-black maze tile.
  Christmas/glitch/kickstarter classes remain unrendered.
- **S18** — `WANTED` → **PARTIAL**. Add:
  > *`UI/E4-advent-calendar-overview-banner.png` shows an advent overview banner — pale-cyan ground,
  > candy-cane bars, two green presents, `Collect all the jolly swag!` /
  > `Log in everyday!` in red (`#f42009`), and **25 numbered tankcessory
  > sprites** (day 1 Santa hat … day 25 `MERRY X-MAS` pennant). Strong
  > candidate for the known-lost `images/AdventCalendarOverview.jpg`
  > (`srv/index.php:8561`, LEDGER 232), whose news item
  > (`25-12-2012`) says "the 25 Christmas tankcessories". **M2 at best — the
  > LEDGER row stays `known-lost`.** Open test: compare the eight held
  > `christmasPresentNN.png` files against days 2, 4, 6, 8, 14, 15, 18, 23 of
  > this banner.*
- **S19** — `WANTED` → **PARTIAL**. Era render confirmed (Like + Share pair,
  ~120 px, `srv/index.php:1161`); a 2013 generation with a separate
  `facebook` status box and a `✓Like | 7k` button is documented; the
  right-column position moved between 2015 and 2016.
- **S23** — `WANTED` → **DONE**. `UI/E1-frontpage-2016-ads-filled.png` has both 160×600 slots filled
  and the layout is unmoved: 17.8 CSS px gutters (declared 20), sidebar-outer
  span 963 CSS (declared 932), footer centred on the sidebar midpoint to 1
  capture px. Note the creatives are third-party (Minecraft/GamesCrystal,
  Goodgame) and are **not reproduction candidates**.
- **S105** — mark the *format* question **answered**: the Visits template is
  character-identical 2013→2018. Add the open sub-question that
  `Online:` ≠ `Logged in:` in every observed frame but they are **equal** in
  all four archived era-final captures.
- **S106** — add the **four observed states** of the left-column promo slot:
  `Online BETA / BETA Membership required` (grey, 2016), `OPEN BETA` + live
  countdown (red, 2016), `PLAY ONLINE / Online battles are in heavy
  development. Try now!` (red, 2018 + era-final), and `More News / Dec. 18th`
  (era-final December).
- **S110** — add the two dated build sightings: `version 3.7` on a page
  datable to ~Jan 2013 (`E6-frontpage-2013-version-3-7.png`) and `version 4.0` on pages dated 2015
  and 2018. Also record that **`UI/E3-video-thumbnail-premium-crates.png` ("TANK TROUBLE PREMIUM") is
  NOT classic-era material** — modern-client art, flagged so it is never
  mistaken for era chrome.
- **New entry S115 — footer credits line as a dating cut.**
  > *The footer carried a second line —
  > `Design: Mads Purup, Programming: Brian Bunch Christensen, Server: Søren
  > Boll Overgaard` — in 2013 (`E6-frontpage-2013-version-3-7.png`) and 2015 (`E7-teaser-control-chooser-2015.png`) and had
  > lost it by 2016 (`E1-frontpage-2016-ads-filled.png`, `E2-frontpage-2016-halloween-countdown.png`) and in the era-final bytes.
  > Any dated frame between those two narrows the removal date, and the
  > line's presence/absence dates any undated frame to before/after it.*
- **New entry S116 — `Need Help?` box generations.**
  > *Red box, left column, `Check the F.A.Q.` (~Jan 2013) → black box, left
  > column, `Check the F.A.Q.` (~mid 2013) → black box, **right** column,
  > `Check the FAQ` (2015-2018, = `srv/index.php:1095-1098`). Three cuts, all
  > cheap to read off any frame.*

**`docs/standards/DIVERGENCES-SERVED.md`**

- **§2** — append: *"Confirmed against era footage: `UI/E1-frontpage-2016-ads-filled.png` shows both
  slots filled with real creatives and the layout unmoved (20 px gutters, 932
  px sidebar span). Note the converse: `UI/E2-frontpage-2016-halloween-countdown.png` was captured through an
  ad blocker that removed the banner wrappers entirely, and there the sidebars
  spread ~380 CSS px apart. Screenshots of this stack taken through a blocker
  will not match era captures either."*
- **§3** — append the observed live-region values as a range check:
  Visits 15.30 M (~Jan 2013) → 17.86 M (~mid 2013) → 48.14 M (2016) →
  66.98 M (~2018-10-31) → 68.47 M (frozen, 2018-12); implied rate ~34 k/day in
  late 2018. Also: `Online` and `Logged in` are **equal** in all four frozen
  captures and **unequal** in every observed frame.
- **§5** — append: *"Observed era values now bound the real counter:
  554,506,351 (~Jan 2013), 665,708,128 (~mid 2013), 1,981,677,06? (2016),
  2,015,054,31? (2016, ~23 days later), 2,58?,??0,31? (~2018-10-31). The frozen
  seed 1,785,664,230 is therefore ~0.8 B below the era-final reality. Motion:
  the plate rotates about its horizontal centre axis (see
  `manualevidence/E-front-page-chrome.md` finding 7-9); direction still
  unobserved."*

**`LEDGER.tsv`**

- **No promotions.** Every one of these is a video frame — M2 at best, never O.
  `AdventCalendarOverview.jpg` (row 232) and `christmasPresentOpen.jpg`
  (row 304) **stay `known-lost`**. If E4 is archived under `archive/`, it needs
  its own M2 row with URL / uploader / date / timestamp, and its `notes` must
  say it is a *frame of* the lost JPEG, not the JPEG.

**`DECISIONS.md`**

- Suggested new entry, "seasonal-promo, extended": the Halloween box is now
  observed in **2016** as well as the archived 20171119 / 20181020, and the
  skin extends to the site header band. Also: the left-column promo slot held
  at least four different widgets between 2016 and Dec 2018.
