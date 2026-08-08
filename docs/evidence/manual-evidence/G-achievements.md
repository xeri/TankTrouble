# Visual evidence — achievements catalogue and artwork

> Analysis of 4 evidence files under `manualevidence/`.
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)

Assigned files, in the capture order given with the assignment (mtimes are when
Ethan saved the crop on 2026-08-04, **not** when the source footage was made —
they are useful only as an ordering of what he was stepping through):

| # | File | Size | Capture time |
|---|---|---|---|
| 1 | [`manualevidence/acheivements.txt`](./acheivements.txt) (sic — misspelled) | 1737 B | 16:29:15 |
| 2 | [`manualevidence/Game/G-achievements-panel-full.webp`](./Game/G-achievements-panel-full.webp) | 692×683 | 16:29:41 |
| 3 | [`manualevidence/UI/G-achievements-panel-fade-alpha-052.png`](./UI/G-achievements-panel-fade-alpha-052.png) | 1069×754 | 17:23:30 |
| 4 | [`manualevidence/UI/G-achievements-panel-progress-bars.png`](./UI/G-achievements-panel-progress-bars.png) | 1128×772 | 17:23:39 |

Throughout this document the three images are shorthanded **W** (the `.webp`),
**A** (`G-achievements-panel-fade-alpha-052.png`) and **B** (`G-achievements-panel-progress-bars.png`).

---

## Scope and provenance

### One correction to the assignment brief, up front

The assignment says *"`acheivements.txt` … describes unlocking the Sunglasses /
'Advocate of Destruction' achievement by using 'Tell A Friend'"*. **It does
not.** `[OBSERVED]` `manualevidence/acheivements.txt`
(md5 `62b766b9b55094a9ad8ca5e5284670b1`, 1737 bytes, CRLF line endings) is a
14-item achievement list plus a 13-row achievement→reward table. The Sunglasses /
Tell-A-Friend prose the brief describes is in a **different** file,
[`manualevidence/UI/tellafriendpopup.txt`](./UI/tellafriendpopup.txt)
(700 bytes), which belongs to topic J. I have cross-checked both against the
pixels below (§ "Cross-check with the two text files"), because the substantive
question the brief asks — *do the images corroborate sunglasses ⇄ "Advocate of
Destruction" ⇄ "Tell a Friend"?* — is answerable either way, and the answer is
**yes, emphatically**.

### The three images are the same UI surface. Two are live footage; one is a still.

The brief's working hypothesis was that `G-achievements-panel-full.webp` is "almost certainly
a community-wiki page capture" like `Game/weapons.txt` and `Game/ranks.txt`
(which still carry wiki chrome — `Sign In to Save`, `View source`, `Edit`).
**That hypothesis is wrong about what the image shows, and right about how it
travelled.** The distinction matters a great deal for this topic.

`[OBSERVED]` W contains **no wiki chrome whatsoever**. No "Sign In to Save", no
"View source", no article title, no Fandom rail. What it contains is a rounded
white panel with:

* a centred grey username string **`WikiaContributor`** at the top
  (bbox x 271–418, y 10–22) `[MEASURED]`,
* a centred black section heading **`Achievements`** (bbox x 282–405, y 54–74)
  `[MEASURED]`,
* a 7×2 grid of achievement cards,
* a **green tick button** at the bottom right (25×32 px at x 655–679,
  y 638–669; fill ramp `#00b000`→`#00f000` with a black outline) `[MEASURED]`.

`[OBSERVED]` That is the TankTrouble **logged-in user panel**, not a wiki table.
The proof is a same-corpus chrome comparison: `UI/D-garage-kickstarter-eve-foxter25.png` (topic D's file,
address bar reads `www.tanktrouble.com/?garage`) shows the identical panel —
same rounded white box, same centred grey username (`Foxter25`), same green tick
at the bottom right — holding the accessory grid instead of achievements. And
`UI/D-garage-2018-url-bar-youtube-toast.png` (address bar `https://tanktrouble.com/?garage`, user
`mr_enderman`) shows the same panel in its **closed** state with a row of four
navigation buttons along the bottom: a wrench with a `beta` tag, a **silver
trophy**, a maze tile, and a document with a yellow warning triangle.

`[OBSERVED]` A and B are frames of **live video** of that same panel, not stills
of a wiki image:

* A has a **hand/pointer cursor** rendered over the pumpkin icon at ≈ (480, 140).
* B has an **arrow cursor** at ≈ (530, 80).
* Both carry lossy block/ringing artefacts typical of H.264 screen capture; W
  has flat exact plateaus (`#d3d3d3` = 211,211,211 over thousands of contiguous
  pixels; pure `#ffffff` glyph cores) typical of a lossless screenshot later
  re-encoded to WebP.
* A is at **~52 % opacity** (measured in § "A is a caught fade", below) — a
  static wiki illustration cannot be at 52 % opacity.

`[MEASURED]` A and B are **not** the same frame cropped differently. Scale
ratios, from three independent rulers:

| Ruler | A | B | B/A |
|---|---|---|---|
| Row pitch (card top → card top) | 127.0 px | 144.7 px | 1.139 |
| Right-column card width (threshold) | 496 px | 565 px | 1.139 |
| "Do You Feel Lucky" hood chroma bbox width | 137 px | 159 px | 1.16 |

`[INFERRED]` So B is 1.139× A in linear scale. Since neither is a crop of the
other, the capture zoom (browser zoom, or a zoom applied to the video) changed
between the two frames. Their **content state is identical** (same twelve rows,
same six unlocked / six locked), so they are the same account, almost certainly
the same session, 9 s apart in Ethan's save order. Falsifier: a frame showing a
different unlock set at either scale.

`[MEASURED]` **W is at 1:1 CSS pixels** — see the next section, which pins this
against held O bytes rather than assuming it. Every geometric number I quote
from W is therefore directly usable as a CSS constant. A and B are at unknown
absolute zoom and I quote them in capture pixels only.

`[INFERRED]` W was almost certainly rehosted through a community wiki (`.webp` is
Fandom's delivery format; `Game/` in this corpus is the wiki-derived folder; the
username `WikiaContributor` is a wiki-flavoured account name someone made to take
the screenshot). **Under guide §6.5 that keeps it M2 at best, never O.** But its
*content* is a capture of the live site's own UI, not a wiki editor's
reconstruction of it — which is exactly the distinction that lets it carry
geometry.

### Dating

`[NOT VISIBLE]` None of the three frames contains an ad creative, seasonal skin,
app-store badge, browser chrome or URL bar. I cannot date any of them from pixels.

`[INFERRED]` Lower bound only: `srv/index.php:8537-8546` carries a news item
`Achievements Unlocked!` dated **10-02-2013**, so no achievements panel existed
before that. `srv/index.php:8621-8622` (news dated 07-12-2012) describes "The
Golden Box … contains special tankcessories that can only be unlocked by special
achievements", so the reward mechanism preceded the panel by ~2 months.

`[INFERRED]` The A/B account is **younger than one year** and **not a mouse
player**: "Old Dog — Hang around for more than a year!" and "Of Mice and Men —
Get 100 victories using the mouse!" are both still locked while 637 tank kills
have accumulated. Weak, but it is a real constraint on the session.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| G1 | The achievements list is the **`openStats` sub-view of the logged-in user panel** (`#userpanelStatsPage`), opened by the trophy button, closed by a green tick — not a standalone page | `[MEASURED]`+`[OBSERVED]` | **S114** ("achievement list page"), S113 | Answers an "unknown-existence" item |
| G2 | `G-achievements-panel-full.webp` is **692×683 px = exactly the `openStats` geometry in held O bytes** (`index.php:4046` width→692; `:4050` content height→605; 605+78=683) | `[MEASURED]` | S114, S5 | Pins W as 1:1 CSS px |
| G3 | **Full 14-item catalogue transcribed**: 14 titles, 14 locked descriptions, 6 unlocked descriptions, 14 icons described and measured | `[OBSERVED]` | **S5** (the missing content) | Nothing invented yet — first content |
| G4 | Locked and unlocked rows carry **two different description strings** (imperative goal vs past-tense "You …") | `[OBSERVED]` | S5 | New requirement for any rebuild |
| G5 | Locked row = `#d4d4d4` card, **white** text, icon desaturated to R=G=B with black point lifted to ≈`#383838`. Unlocked row = white card + drop shadow, `#1d1c1c` text, full-colour icon | `[MEASURED]` | S5, S113 | — |
| G6 | **Progress counters exist**: `637 of 1000`, `637 of 10000`, `… 100`, rendered over a **full-card-height progress bar** whose width is linear in progress (measured 63.98 % vs 63.70 % expected; 6.29 % vs 6.37 %) | `[MEASURED]` | **S97** (`achievementProgress`), S5 | — |
| G7 | Image A is a **caught opacity fade at α ≈ 0.52**, matching the 200 ms linear tween on `#userpanelStatsPage` at `index.php:4053` | `[MEASURED]` | S114, S113 | Confirms held JS |
| G8 | The progress bars are **absent in A and present in B** at identical account state → the bars are drawn/animated separately from the panel opacity fade | `[MEASURED]`+`[INFERRED]` | S5, S97 | New want |
| G9 | Sunglasses ⇄ "Advocate of Destruction" ⇄ `Get 10 friends to sign up using "Tell a Friend"!` fully corroborated in pixels | `[OBSERVED]` | S5, [J](./J-tell-a-friend.md) | Upgrades `tellafriendpopup.txt` from hearsay to corroborated |
| G10 | `acheivements.txt` is a **transcription of an image like W**, read column-major, with **one outright error** ("Old Dog — Hang around for 1 month" vs pixels "…for more than a year!") and one reward contradiction ("Sailor hat" vs a polka-dot bandana) | `[OBSERVED]` | — | Grades the txt below the pixels |
| G11 | The two **secret** achievements are **listed, not hidden** — they appear in a fully-locked account with cryptic descriptions | `[OBSERVED]` | S5 | — |
| G12 | The "Hallowed Be Thy Name" icon appears to be the **same artwork as the Garage Halloween box** | `[INFERRED]` | asset reuse | — |
| G13 | Nothing here shows `achievement.php`'s response | `[NOT VISIBLE]` | **S97** | Records absence |
| G14 | Nothing in **my four files** shows the unlock float — but `UI/B-frontpage-achievement-unlock-float.png` (topic [B](./B-maze-editor-interaction.md)) does, and its description line resolves `achievement_cb`'s ambiguity as `<name>: <You…>` | `[OBSERVED]` | **S5** → **PARTIAL** | Answers the ask I was about to file |

---

## The identification, in detail — why this is `#userpanelStatsPage`

This is the single most load-bearing chain in the document, so it is set out
step by step. Every line number below was grepped from
`/mnt/user-data/uploads/websites/TankTrouble/srv/index.php` (812 KB; the file
repeats each route's JS — these are the occurrences inside `tt_page_garage()`,
which begins at **line 3374** and is the O body from
`archive/commoncrawl/warc-bodies/20181214_tanktrouble.com__garage.txt`).

`srv/index.php:4042-4056`, `function openStats(user)`:

```js
tempFX.start(692);   // #userpanel-<user>          'width',  500ms Quad.easeInOut   (:4046)
tempFX.start(605);   // #userpanelContent-<user>   'height', 500ms Quad.easeInOut   (:4050)
tempFX.start(720);   // #userpanelswrapper         'height', 500ms Quad.easeInOut   (:4051)
… 'opacity', {duration: 200, transition: Fx.Transitions.linear} … #userpanelStatsPage-<user>  (:4053)
… 'opacity', {duration: 200, transition: Fx.Transitions.linear} … #userpanelAcceptStats-<user> (:4055)
```

1. `[MEASURED]` **W is 692 px wide.** `openStats` animates the panel width to
   **692**. Three of the four sub-views open at 692 (`openPaintFacility` :3554,
   `openMazeCreator` :3609, `openStats` :4042); `openForm` (:3755) opens at 350.
2. `[MEASURED]` **W is 683 px tall.** The three 692-wide sub-views set different
   `#userpanelContent` heights: Paint **245**, MazeCreator **385**, Stats
   **605**. Only Stats gives 605.
3. `[MEASURED]` `683 − 605 = 78`, and **the first achievement card's top edge in
   W is at y = 78 exactly** (column scan at x = 200: y 77 = `#ffffff`,
   y 78 = `#d3d3d3`). So `#userpanelContent` occupies y 78–682 (605 px) and
   everything above it — the 2 px top border, the `WikiaContributor` line and the
   `Achievements` heading — occupies exactly 78 px. The two independent numbers
   close on the same boundary.
4. `[MEASURED]` The green tick at the bottom right of W is
   `#userpanelAcceptStats`. Every sub-view has its own tick:
   `userpanelAcceptPaint`, `userpanelAcceptMaze`, `userpanelAcceptForm`,
   `userpanelAcceptStats` (10, 10, 6 and 6 occurrences respectively across the
   file). `D-garage-kickstarter-eve-foxter25.png` shows the same tick on the accessories view.
5. `[OBSERVED]` The panel's closed state (`D-garage-2018-url-bar-youtube-toast.png`) carries a **trophy**
   button. The held JS names five panel buttons —
   `userpanelPaint`, `userpanelMaze`, `userpanelSherifStar` (guarded by
   `!= null`, i.e. moderators only), `userpanelForm`, `userpanelStats`
   (`disableUserPanelIcons` at `:3501`ff / `enableUserPanelIcons` at `:3538`ff).
   Four are visible in `D-garage-2018-url-bar-youtube-toast.png`; the trophy is the only unclaimed glyph and
   `userpanelStats` is the only unclaimed id.
6. `[MEASURED]` Image A is at α ≈ 0.52 (below). `#userpanelStatsPage` fades in
   over **200 ms linear** at `:4053`. α = 0.52 ⇒ ≈ 105 ms into that tween.

`[INFERRED]` Conclusion: `G-achievements-panel-full.webp` is a 1:1 capture of the user panel
in its Stats state, and the "achievements list" is `#userpanelStatsPage`. What
would falsify it: a frame of the panel at 692×683 showing something other than
achievements, or a standalone URL that renders this grid.

`[UNCERTAIN]` One box-model wrinkle I cannot settle: the page is XHTML 1.0
Transitional with a full system identifier (`:3377`), i.e. standards mode, so
`style.width = 692px` is a **content-box** width and a CSS border would add to
it. W's 692 px **includes** its 2 px `#d3d3d3` frame on each side. The
economical reading is that the visible frame is not a border on `#userpanel` at
all but the parent's `#d3d3d3` background showing through a 2 px inset — which
makes 692 the outer measurement and everything consistent. Settling it needs the
era `styles.css`/`boxStyles.css` rules for `#userpanel`, which I did not have
staged.

---

## File-by-file analysis

### `manualevidence/acheivements.txt` (1737 B, captured 16:29:15)

**Filename claim (repo owner):** the filename is only a (misspelled) topic
label; there is no descriptive claim to corroborate.

**What it contains** — `[OBSERVED]`, transcribed verbatim including its own
typography (CRLF endings; the reward table's rows are separated by a lone TAB
line, i.e. it was pasted out of an HTML table):

Header: `Achievements in TankTrouble Classic** (14) (OBSOLETE)`

Then 14 `Title - Description` lines, then:

```
*Secret achievements

**TankTrouble Classic has now gone obsolete as Flash was discontinued, achievements, the garage and all other log-in required content has been stripped from the site, leaving the game tab and the news tab.
```

Then a two-column `Achievement` / `Reward` table with **13** rows.

**Links to the program.** `[OBSERVED]` The 14 titles appear in exactly the order
you get by reading W **down the left column, then down the right column**:
Hallowed Be Thy Name, Put Her Down, Apprentice of Destruction, Of Mice and Men,
Do You Feel Lucky Punk?, Never Saw It Coming, Suit Up! ‖ Old Dog, Master of
Destruction, Lord of Destruction, Advocate of Destruction, Doggy Bag, Mirror
Mirror On The Wall, Elite Hackers' Society. `[INFERRED]` The txt is therefore a
**transcription of a screenshot of this panel**, not an independent source. It
does not corroborate the pixels; it is derived from them. It must be graded
strictly below them.

**Reliability, graded honestly.** `[OBSERVED]` It contains at least one
substantive error and several normalisations:

| txt says | pixels say | verdict |
|---|---|---|
| `Old Dog - Hang around for 1 month.` | `Hang around for more than a year!` (W **and** B, both legible) | **CONTRADICTED** — the txt is wrong |
| `Put Her Down - Kill Laika 10 times in a row without dying!` | `Kill Laika ten times in a row without dying!` | numeral normalised; wording otherwise exact |
| reward `Apprentice of Destruction → Sailor hat` | icon is a knotted polka-dot **bandana/kerchief** (red in A/B), not a hat | **CONTRADICTED** as written |
| reward table omits `Of Mice and Men` entirely | the row exists, icon = mouse-ear headband | **INCOMPLETE** (13 of 14) |
| the other 12 descriptions | match verbatim | corroborated |

`[INFERRED]` The prose register ("gone obsolete as Flash was discontinued…") and
the mixed provenance (a clean list + a table + an editorial footnote) read as
forum-sourced or LLM-assembled rather than as a primary capture. Combined with
the demonstrable error, **this file is evidence of the transcriber's reading, not
of the site**. Where it and the pixels disagree, the pixels win with no argument.

`[INFERRED]` What it *does* add that pixels cannot: the **reward accessory names**
(the panel shows the artwork but never names it) and the `*` marking of the two
secret achievements. Those are M3-grade at best and should be labelled as
community claims if used.

**What this does NOT show.** `[NOT VISIBLE]` No ids, no ordering rationale, no
dates, no progress semantics, no unlocked-state description strings, no geometry.

---

### `Game/G-achievements-panel-full.webp` (692×683, captured 16:29:41)  *(was `Achievements.webp`)*

**Filename claim (repo owner):** "Achievements" — corroborated; the panel's own
heading reads `Achievements`.

#### What is drawn — element by element

`[OBSERVED]` A single rounded rectangle filling the whole image. `[MEASURED]`
2 px `#d3d3d3` frame on all four sides (rows 0–1 and 681–682, columns 0–1 and
690–691), white `#ffffff` fill, corner radius ≈ 3–4 px (at (0,0) the pixel is
still white; (1,1) = 232; (2,2) = 213).

`[OBSERVED]` Header block, y 0–77:
* `WikiaContributor`, centred (bbox x 271–418 → centre 344.5; panel centre 345.5),
  cap height 13 px, darkest glyph core `#6a6561` (≈ mid grey) `[MEASURED]`.
* `Achievements`, centred (bbox x 282–405 → centre 343.5), cap height 16 px
  (rows 54–69), darkest glyph core `#000000` `[MEASURED]`.

`[MEASURED]` Card grid — 7 rows × 2 columns, all fourteen cards in the **locked**
presentation:

| property | value (W = 1:1 CSS px) | how obtained |
|---|---|---|
| left column card | x 32 … 337 (306 px wide) | horizontal run-length scan at y = 130 |
| right column card | x 352 … 656 (305 px wide) | same |
| gutter between columns | 14 px (x 338–351) | same |
| card top edges | y 78, 158, 238, 318, 398, 478, 558 | column scan at x = 40 and x = 200 |
| card height | 64 px | x = 200 scan: 78→141 solid, 142 = white |
| row gap | 16 px |  |
| **row pitch** | **80 px** |  |
| card corner radius | ≈ 5–6 px | corner run map (y 78 starts at x 37; y 83 at x 32) |
| card fill | `#d3d3d3` (211,211,211) — 1409 identical pixels in one 20-row title band | modal colour |
| card drop shadow | **none** — `#d3d3d3` → `#ffffff` in one AA pixel | x = 200 vertical profile |

`[MEASURED]` Type metrics inside a card (row 1 left, y-profile of pixels ≥ 238):

| element | rows | height | left inset |
|---|---|---|---|
| title glyphs (caps + x-height) | 91–101 (descenders to 104) | 11 px cap height | x 41 → 9 px from card edge |
| description line 1 | 107–114 (descenders to 117) | 8 px cap height | x 40 → 8 px |
| description line 2 | 121–126 | | |
| description line pitch | 107 → 121 | **14 px** | |

`[INFERRED]` That puts the title around 15–16 px and the description around
11 px with a 14 px line box, if the face's cap-height ratio is ≈ 0.72 em. I will
not round this into a constant — the defensible statement is *cap heights 11 px
and 8 px, description leading 14 px*.

`[OBSERVED]` Both title and description are set in a squarish, wide, low-contrast
sans with straight-sided lowercase and a single-storey feel to the digits; the
**description is noticeably bolder than the title** at a smaller size. `[UNCERTAIN]`
Whether that is the custom `TankTrouble.ttf` (topic I's file) or a CSS `font-weight`
on a device font — the AA at this size cannot distinguish; a native-resolution
frame would.

`[MEASURED]` Text colours in the locked state: **both title and description are
pure `#ffffff`** on the `#d3d3d3` card. (Brightest-30 median = `#ffffff` in every
title and description band sampled; the "dark" extremes in those bands are icon
pixels bleeding into the sample window.)

`[OBSERVED]` **No progress counters and no progress bars anywhere in W** — every
card is a flat unbroken `#d3d3d3`. See § "Locked vs unlocked" for what that
implies.

`[MEASURED]` Green tick, bottom right: 25×32 px at x 655–679, y 638–669;
16 px below the last card, 12 px above the panel's inner bottom, 11 px in from
the right border. Fill is a vertical green ramp, modal quantised colours
`#00b000` / `#00c000` / `#00f000`, with a near-black outline.

#### Icons — measured

`[MEASURED]` Bounding boxes from a background-model + morphological-opening +
connected-component pass (background modelled as `#d3d3d3` inside a card rect,
`#ffffff` outside; 5×5 opening removes text strokes; components < 400 px
discarded). **The boxes include each icon's own drop shadow**, so treat them as
upper bounds by ~4–6 px on the right and bottom.

| Row·Col | Achievement | Icon bbox (x, y) | w × h | Notes |
|---|---|---|---|---|
| 1 L | Hallowed Be Thy Name | 256–332, 68–144 | 77 × 77 | overflows 10 px above the card |
| 1 R | Old Dog | 570–657, 80–139 | 88 × 60 | |
| 2 L | Put Her Down | 249–335, 153–229 | 87 × 77 | pole overflows 5 px above, 7 px below |
| 2 R | Master of Destruction | 572–655, 162–213 | 84 × 52 | |
| 3 L | Apprentice of Destruction | 250–335, 242–298 | 86 × 57 | |
| 3 R | Lord of Destruction | 574–656, 232–313 | 83 × 82 | pole overflows 6 px above, 11 px below |
| 4 L | Of Mice and Men | 251–334, 331–372 | 84 × 42 | |
| 4 R | Advocate of Destruction | 573–662, 327–371 | 90 × 45 | right edge 662 > card right 656 — bleeds 6 px |
| 5 L | Do You Feel Lucky, Punk? | 246–335, 401–460 | 90 × 60 | |
| 5 R | Doggy Bag | 569–655, 409–455 | 87 × 47 | |
| 6 L | Never Saw It Coming | 252–319, 471–557 | 68 × 87 | overflows 7 px above, 15 px below |
| 6 R | Mirror, Mirror, On The Wall | 567–655, 483–548 | 89 × 66 | |
| 7 L | Suit Up! | 244–341, 569–614 | 98 × 46 | right edge 341 > card right 337 — bleeds 4 px |
| 7 R | Elite Hackers' Society | 586–639, 564–619 | 54 × 56 | |

`[INFERRED]` The icon **anchor is the card's right edge, not a fixed box**: right
edges cluster at 332–341 (left column, card right = 337) and 639–662 (right
column, card right = 656). Artwork is free to overflow the card vertically —
flag poles and the dog-tag chain do — so there is no clipping on the card. That
is a concrete constraint for any rebuild: the card cannot be `overflow: hidden`.

#### Measurements — locked palette

| element | hex | how |
|---|---|---|
| page / panel fill | `#ffffff` | flat |
| panel frame | `#d3d3d3`, 2 px | rows 0–1 / 681–682 |
| card fill | `#d3d3d3` | modal, 1409 px in one band |
| title text | `#ffffff` | brightest-30 median |
| description text | `#ffffff` | brightest-30 median |
| heading `Achievements` | `#000000` | darkest-30 median |
| username | `#6a6561` (≈ `#666`) | darkest-25 median |
| icon black point | luminance 51–52 (≈ `#333334`) | min over 4 icon bboxes |
| icon white point | 255 | max, ≥ 250 on 600–1600 px per icon |

#### Links to the program

* **S114** — see G1/G2 above. This image, plus `D-garage-2018-url-bar-youtube-toast.png`'s trophy button,
  plus `index.php:4042-4056`, converts *"achievement list page"* from
  unknown-existence to **existent and identified as `#userpanelStatsPage`**.
* **S5** — supplies 14 titles + 14 locked descriptions + 14 icon descriptions.
* `srv/index.php:8537-8546` — the news item that says *"Go to `<a href="?garage">`
  the Garage `</a>` to see which ones you already have"* is held O bytes and
  independently states that the list lives under `?garage`. That is a **second,
  byte-level source** for G1 that does not depend on my pixels at all.
* [`docs/standards/MAZECREATOR-VISUAL-SPEC.md`](../../standards/MAZECREATOR-VISUAL-SPEC.md) — no pinned
  constant here is touched. `CELL=32`, wall `#444444` 4 px, floor
  `#dddddd`/`#eeeeee` belong to the maze renderer; the achievements card grid is
  a different surface with its own constants (80 px pitch, `#d3d3d3` cards) and
  they must not be conflated. Worth noting only that the panel's card grey
  `#d3d3d3` is **not** the maze floor `#dddddd` — 211 vs 221, a 10-level
  difference, easily eyeballed as "the same light grey" and demonstrably not.

#### What this does NOT show

`[NOT VISIBLE]` The unlocked presentation (this account has nothing unlocked);
any progress counter or bar; any achievement id; the panel's closed state; the
trophy button; the surrounding page; any URL; any date; the unlock float.

---

### `UI/G-achievements-panel-fade-alpha-052.png` (1069×754, captured 17:23:30) — "A"  *(was `{41F86D44-32E6-4048-8AF5-493A7B7E233D}.png`)*

**Filename claim (repo owner):** GUID only — no claim to test.

#### What is drawn

`[OBSERVED]` The same panel, cropped to just above the `Achievements` heading
(heading glyph bbox y 4–31) down to mid-row-6. Six card rows visible per column;
**row 7 (Suit Up! / Elite Hackers' Society) is below the crop and not visible**.
The card edges run x 24–510 (left) and 533–1028 (right); the crop's white margins
carry no browser chrome, no scrollbar, no site header on any edge
(`[MEASURED]` top/left/right 4-px strips contain zero pixels below luminance 200).

`[OBSERVED]` Six rows are **white** (unlocked, dark text, colour icons) and six
are **grey** (locked, light text, grey icons):

| row | left column | right column |
|---|---|---|
| 1 | Hallowed Be Thy Name — **unlocked** | Old Dog — locked |
| 2 | Put Her Down — **unlocked** | Master of Destruction — locked |
| 3 | Apprentice of Destruction — **unlocked** | Lord of Destruction — locked |
| 4 | Of Mice and Men — locked | Advocate of Destruction — locked |
| 5 | Do You Feel Lucky, Punk? — **unlocked** | Doggy Bag — locked |
| 6 | Never Saw It Coming — **unlocked** | Mirror, Mirror, On The Wall — **unlocked** |

`[OBSERVED]` A hand/pointer cursor sits over the pumpkin icon at ≈ (480, 140).

#### A is a caught fade — measurement

`[MEASURED]` Every element in A is a linear blend of the corresponding element in
B toward the page white `#fefefe` (254), at one single alpha:

| element | B value | A value | implied α |
|---|---|---|---|
| locked card fill (flat, 340×35 px sample, σ = 1.67) | 212 | 232.19 | 0.519 |
| unlocked title glyph core | `#1d1c1c` (29) | `#878888` (135) | 0.529 |
| unlocked description glyph core | `#312829` (42) | `#8f8d8d` (141) | 0.533 |
| unlocked-card drop-shadow minimum | 150 | 199 | 0.529 |

`[MEASURED]` Applying the inverse transform `A′ = (A − 254·(1−α))/α` with
α = 0.529 restores A's locked card fill to **exactly `#d4d4d4`** — B's measured
value — and its page background stays 254. The reconstruction is
self-consistent, so the model is right and **α = 0.52 ± 0.01**.

`[INFERRED]` A is therefore ≈ 52 % of the way through the **200 ms linear**
opacity tween on `#userpanelStatsPage` (`srv/index.php:4053`), i.e. ≈ 105 ms in
— assuming the video codec's transfer function is close enough to linear in
sRGB, which is why I quote ±0.01 rather than a frame number. `[UNCERTAIN]` I
cannot tell a fade-**in** (`openStats`, `:4053`) from a fade-**out**
(`closeStats`, `:4068`) from one frame; the capture order (A saved 9 s before B)
weakly favours the opening.

`[INFERRED]` This also explains why A's *locked* rows are visibly mushier than
its *unlocked* rows: at α = 0.52 the locked rows' white-on-`#d4d4d4` contrast
drops from 42 levels to 22, which an H.264 encoder smears. It is a capture
artefact, not a design feature — **W renders locked text crisply at full
opacity**, which settles it.

#### The absent progress bars

`[MEASURED]` B shows a darker `#afafaf` progress fill occupying the left 64 % of
the Master of Destruction card and the left 6 % of Lord of Destruction. In A,
**at the same account state, with the fade divided out, those cards are a uniform
`#d4d4d4` across their full width** — a 23-row band average across x 530→1035
stays inside 232–235 with no step where a 63.7 % boundary would fall (x ≈ 849).
At α = 0.52 a real fill would read 213 against a 232 base: a 19-level step,
trivially detectable. It is not there.

`[INFERRED]` The progress fill is therefore **not** a static child of
`#userpanelStatsPage` — it is drawn or width-tweened separately, and at A's
moment it was still at zero. Alternative reading I cannot exclude: A is a
fade-out and the bar was torn down first. Either way the operational conclusion
is the same: **a rebuild must not assume the bar is painted at its final width
the instant the page becomes visible.** Falsifier: a frame at partial panel
opacity that already shows a partial bar.

#### Measurements — unlocked palette (A, after un-fading; cross-checked against B)

| element | A un-faded | B (native) |
|---|---|---|
| page background | 254 | 254 |
| locked card fill | `#d4d4d4` | `#d4d4d4` |
| unlocked card fill | ≈ `#ffffff` | `#fdfdfd`–`#fefefe` (video) |
| unlocked title glyph core | ≈ `#1d1c1c` | `#1d1c1c` … `#2b262e` |
| unlocked description glyph core | ≈ `#312829` | `#312829` … `#292627` |
| unlocked-card outline | ≈ `#e9e9e9` | `#e9e9e9` (dip at the card's top edge) |
| unlocked-card drop shadow, darkest | 199 → 150 restored | `#969696` (150) at 1–3 px below the card, easing back to page white over ≈ 24 px |
| locked-card drop shadow | none | **none** (212 → 254 in 3 px) |

`[MEASURED]` That last row is a real, reproducible design difference and it
matches W: **locked cards have no shadow; unlocked cards are elevated.**

#### Links to the program

* **S5** — A is the source for five of the six unlocked description strings (its
  left column is uncropped where B's is not).
* **S113** ("any page rendered logged-in") — A and B are logged-in renderings of
  a garage sub-view. They do not close S113 but they are the first pixels of it
  in this corpus for this surface.
* **S114** — the α = 0.52 measurement pins A to `index.php:4053`, an O-byte line.

#### What this does NOT show

`[NOT VISIBLE]` Row 7; the username header; the green tick; the trophy button;
any browser chrome or URL; any achievement id; the unlock float; any date.

---

### `UI/G-achievements-panel-progress-bars.png` (1128×772, captured 17:23:39) — "B"  *(was `{CF0BFA0E-A568-4D70-81CC-4F6B236F2B7A}.png`)*

**Filename claim (repo owner):** GUID only — no claim to test.

#### What is drawn

`[OBSERVED]` The same panel at 1.139× A's scale, panned so that the **left column
is clipped** — row titles read `lowed Be Thy Name`, `Her Down`, `orentice of
Destruction`, `Mice and Men`, `You Feel Lucky, Punk?`, `ver Saw It Coming`.
The right column is complete: cards run x 523 … 1087 (565 px by threshold,
551 px by 50 %-crossing). Card tops at y 115, 260, 405, 549, 690; **pitch
144.7 px**; card height ≈ 118 px. Row 1 and row 6 are clipped at the top and
bottom of the frame; **row 7 is not visible.**

`[OBSERVED]` An arrow cursor at ≈ (530, 80). `[OBSERVED]` A 1 px uniform dark
grey column (values 71–89) runs the entire height at x = 0; `[UNCERTAIN]` this is
the crop landing on the edge of something dark to the left (window border, video
frame edge) — it is not part of the panel.

`[OBSERVED]` Identical unlock state to A, row for row. Same account.

#### The progress bars — the headline measurement

`[OBSERVED]` Two locked cards carry a **darker region filling the left part of
the card, full card height**, plus a small text line at the bottom left of the
card:

* Master of Destruction — `637 of 1000`
* Lord of Destruction — `637 of 10000`
* Of Mice and Men (left column, clipped) — `[…] 100` legible; the numerator is
  off-crop in B and illegible in A.

`[MEASURED]` Colours: fill `#afafaf` / `#adadad`; unfilled remainder `#d4d4d4`
(identical to a card with no bar at all, e.g. Old Dog); counter text light
(`#ededed` brightest-40 median) sitting **on top of** the fill and continuing
past its right edge where the fill is short (visible on Lord: the fill ends at
x ≈ 559 and the string `of 10000` continues to x ≈ 660 on the lighter ground).
The fill spans the card's full height (column scan at x = 700 reads ≈ 174 from
y 116 to y 230, i.e. card top to card bottom).

`[MEASURED]` **The bar width is linear in progress.** Using a consistent 50 %-
crossing edge definition on band averages:

| card | card left | card right | fill edge | fill fraction | counter | expected | Δ |
|---|---|---|---|---|---|---|---|
| Master of Destruction | 524.8 | 1074.8 | 876.7 | **63.98 %** | 637 / 1000 | 63.70 % | +0.28 pp |
| Lord of Destruction | 524.8 | 1076.4 | 559.5 | **6.29 %** | 637 / 10000 | 6.37 % | −0.08 pp |

`[MEASURED]` This is also what disambiguates the leading digit: the glyph is
compression-mushy between `6` and `8`, but `837/1000` would put the Master edge
at x ≈ 985, 108 px away from where it is. **It is 637.** (The brief's provisional
readings "657 of 1000" and "437 of 10000" are both wrong; both cards read the
same numerator, 637, which is exactly what you would expect — one tank-kill
counter feeding two thresholds.)

#### Which rows get a counter

`[OBSERVED]` Of the six locked rows visible, only three carry a counter line
(Master, Lord, Of Mice and Men). Old Dog, Advocate of Destruction and Doggy Bag
show title + description and then **empty card space** where the counter would be.

`[INFERRED]` The most economical rule that fits: **the counter line and bar are
rendered only when progress > 0.** Old Dog is time-based, Doggy Bag is a streak,
and this account has invited 0 friends — all three would be 0. Falsifier: any
frame showing `0 of N`, or a counter on a streak/time achievement.

#### Locked vs unlocked, measured side by side (all from B, one image, one frame)

| sample | bright (unlocked) row | dim (locked) row |
|---|---|---|
| row background | `#fdfdfd`–`#fefefe` (Apprentice) | `#d4d4d4` (Lord, Old Dog) |
| row background, in-progress part | — | `#afafaf` (progress fill) |
| title glyph core | `#1d1c1c` (Apprentice) / `#2b262e` (Mirror) | `#f9f9f9` (Old Dog) / `#f5f5f6` (Master, on fill) |
| description glyph core | `#312829` (Apprentice) / `#292627` (Mirror) | `#fafafa` (Old Dog) / `#f2f3f3` (Master) |
| counter glyph core | — | `#ededed` on `#b0b0b0` |
| card shadow | `#969696` at 1–3 px below the card, ≈ 24 px falloff | **none** |
| icon mean chroma | 132.7 (pumpkin), 93.4 (hood), 58.8 (bow), 56.0 (bandana), 14.2 (paw flag) | **0.1 – 0.2** on every locked icon |
| icon 99th-pct chroma | 249, 213, 164, 254, 190 | **1** |
| icon black point (min luminance) | 0.3 (pumpkin), 1.7 (hood) | 56–59 (skull, hat, flag, glasses) |
| icon white point (max luminance) | 255 | **255** |

`[MEASURED]` The locked treatment is **not** an alpha fade toward the card: an
80 % alpha over `#d4d4d4` would cap whites at 246, and locked icon whites are a
full 255 over hundreds of pixels. It is a **desaturation to exact R = G = B
(mean chroma ≤ 0.2, 99th percentile chroma = 1 on every locked icon) with the
black point lifted from ≈ 0 to ≈ 52–59 (≈ `#343434`–`#3b3b3b`) and the white
point held at 255.**

`[OBSERVED]` The desaturation claim does not rest on the locked objects merely
being grey by design. Three icons are **coloured in B and grey in W**: the
pumpkin (`#f86000` orange), the bandana (`#f80008` red), the bow (`#f860c8`
pink). One icon is **unlocked and still grey** — Never Saw It Coming's dog tags,
mean chroma 0.7, because the artwork is silver. So "grey" alone never proves
locked; the paired comparison does.

`[UNCERTAIN]` I could **not** pin which desaturation formula (Rec. 601, Rec. 709,
plain average) was used: comparing W's grey icons against A/B's colour icons
requires pixel-aligned crops, and my bounding boxes include different fractions
of card background, which swamps the 17–40 level differences between candidate
formulas. Nor can I rule out that the locked icon is simply a **separately
authored greyscale asset** rather than a filter. What would settle it: a single
native-resolution capture containing the same icon locked and unlocked (i.e. two
accounts, same zoom), or the asset files themselves.

`[OBSERVED]` Locked rows keep **everything**: icon, title, description, and (where
progress > 0) the counter. Nothing is hidden behind a silhouette or a "???".
`[OBSERVED]` That includes both achievements the txt marks as secret — see
"Mirror, Mirror, On The Wall" and "Elite Hackers' Society" in W, a fully-locked
account. **"Secret" means the description is cryptic, not that the row is
hidden.** In the locked state Mirror reads `Who's the fairest of them all?`; the
same row unlocked reads `You changed your look 20 times!` — the requirement is
revealed only on unlock. Same pattern for `Do You Feel Lucky, Punk?`:
`Did she fire four or five bullets?` → `You killed Laika when she was out of
bullets!`

#### Links to the program

* **S5** — B is the source for the right column's locked strings, both progress
  counters, and the whole locked/unlocked palette.
* **S97** — `LEDGER.tsv:165` records `achievement.php`'s parameter names as
  `achievementId` / `achievementIds` / `achievementProgress`. B is the first
  sight of what **`achievementProgress` looks like on screen**: an integer over a
  target, rendered as `N of M` plus a proportional full-height bar.

#### What this does NOT show

`[NOT VISIBLE]` Row 7; the left column's left edge; the username header; the
green tick; any id; any URL, chrome or date; the unlock float; `achievement.php`'s
response.

---

## 1 · The complete achievement catalogue

**Reading key.** `W` = `Game/G-achievements-panel-full.webp` (crisp, 1:1, all locked).
`A` = `G-achievements-panel-fade-alpha-052.png` (un-faded before reading; best for the left column).
`B` = `G-achievements-panel-progress-bars.png` (best for the right column and for the counters).
Confidence: **high** = every glyph unambiguous at ≥ 4× zoom; **med** = one or
more glyphs reconstructed from context but consistent across two images.

Layout position is given as (row, column) in W's 7×2 grid.

### 1a · Titles and both description strings

| Pos | Title (verbatim) | Locked description (verbatim) | Unlocked description (verbatim) | Progress counter | Read from | Conf. |
|---|---|---|---|---|---|---|
| 1 L | `Hallowed Be Thy Name` | `Come around for Halloween and pick up new swag!` | `You trick'r'treated your way to new swag!` | — | locked: W · unlocked: A · title: all three | high |
| 2 L | `Put Her Down` | `Kill Laika ten times in a row without dying!` | `You showed that Space Dog who's the leader of the pack!` | — | locked: W · unlocked: A | high |
| 3 L | `Apprentice of Destruction` | `Destroy 100 tanks!` | `You've destroyed 100 tanks!` | — | locked: W · unlocked: A, B | high |
| 4 L | `Of Mice and Men` | `Get 100 victories using the mouse!` | *not observed* | `[…] 100` (numerator illegible) | locked: W, B · counter: B | high (strings) / low (counter) |
| 5 L | `Do You Feel Lucky, Punk?` | `Did she fire four or five bullets?` | `You killed Laika when she was out of bullets!` | — | locked: W · unlocked: A, B | high |
| 6 L | `Never Saw It Coming` | `Zap Laika with a direct laser hit!` | `You zapped Laika with a direct laser hit!` | — | locked: W · unlocked: A | high |
| 7 L | `Suit Up!` | `Be suited for a crisis!` | *not observed* | — | W only (row 7 is below both PNG crops) | high |
| 1 R | `Old Dog` | `Hang around for more than a year!` | *not observed* | — | W, B (independent, agree) | high |
| 2 R | `Master of Destruction` | `Destroy 1000 tanks!` | *not observed* | `637 of 1000` | W, B | high |
| 3 R | `Lord of Destruction` | `Destroy 10000 tanks!` | *not observed* | `637 of 10000` | W, B | high |
| 4 R | `Advocate of Destruction` | `Get 10 friends to sign up using "Tell a Friend"!` | *not observed* | — | W, B (independent, agree) | high |
| 5 R | `Doggy Bag` | `Kill Laika twenty-five times in a row without dying!` | *not observed* | — | W, B | high |
| 6 R | `Mirror, Mirror, On The Wall` | `Who's the fairest of them all?` | `You changed your look 20 times!` | — | locked: W · unlocked: A | high |
| 7 R | `Elite Hackers' Society` | `Prove your worth as a hacker and unlock all 16 secret backdoors!` | *not observed* | — | W only | high |

Notes on the exact typography, since this project cares:

* `[OBSERVED]` `You trick'r'treated your way to new swag!` — verified at 5×.
  Three glyph groups `trick` `'r'` `treated` with straight apostrophes, no
  spaces. (The brief's provisional "You kick'n'trailed your way to new swag!" is
  a mishearing; the pixels are unambiguous.)
* `[OBSERVED]` `You've destroyed 100 tanks!` — straight apostrophe, verified at 7×.
* `[OBSERVED]` `who's` in Put Her Down and `Who's` in Mirror — straight apostrophes.
* `[OBSERVED]` `Get 10 friends to sign up using "Tell a Friend"!` — **straight
  double quotes**, capital T and F, lowercase `a`. Line-breaks after `using`.
* `[OBSERVED]` `Space Dog` is capitalised in the unlocked Put Her Down string,
  where the locked string names her `Laika`. Two different names for the same
  character in the same row.
* `[OBSERVED]` `Elite Hackers' Society` — apostrophe **after** the `s`.
* `[UNCERTAIN]` `Do You Feel Lucky, Punk?` — the comma is clear at 3× in W and A;
  I read no other punctuation in any title.

### 1b · The icon artwork, element by element

Dimensions are in **W's pixels, which are CSS pixels** (see G2). Colours for
unlocked artwork are modal quantised values from B unless noted; every locked
value is R = G = B.

| Pos | Achievement | Icon — what it depicts | Locked palette (W) | Unlocked palette (A/B) | Size (W) |
|---|---|---|---|---|---|
| 1 L | Hallowed Be Thy Name | A carved jack-o'-lantern, three-quarter view: ribbed round body, short curved stem, two angled slit eyes, small triangular nose, wide zig-zag saw-tooth mouth | ramp `#404040`→`#f8f8f8`, modal `#d0d0d0` | body `#f86000` orange with darker orange ribs; face cut-outs ≈ `#000000`; stem green | 77 × 77 |
| 1 R | Old Dog | A human skull with a hairline crack across the crown, over two crossed bones; one eye socket larger than the other | white `#f8f8f8` body, sockets `#404040` | *not observed unlocked* | 88 × 60 |
| 2 L | Put Her Down | A white triangular pennant on a slim pole, bearing a circle-and-diagonal-slash "prohibited" sign over a four-toe dog paw print | flag `#f8f8f8`, ring/paw mid-grey | ring and slash `#b80828`–`#c00010` (crimson); paw dark grey; flag white | 87 × 77 |
| 2 R | Master of Destruction | A dark bicorne/pirate hat, brim curled up at both sides, with a small white skull-and-crossed-bones badge on the crown | crown `#686868`, badge `#f8f8f8` | *not observed unlocked* | 84 × 52 |
| 3 L | Apprentice of Destruction | A knotted head-scarf / bandana with large round spots, tied in a bow with two tails at the left | modal `#d0d0d0`, spots `#f8f8f8`, folds `#585858` | cloth `#f80008` red, spots white, shadow `#500000` | 86 × 57 |
| 3 R | Lord of Destruction | A rectangular Jolly Roger flying from a long thin pole: dark ground, white skull with two crossed bones **above** and one below | ground `#404040`, device `#f8f8f8` | *not observed unlocked* | 83 × 82 |
| 4 L | Of Mice and Men | Two dark filled discs — one large, one small — joined by a curved band. Reads as a **mouse-ear headband** seen at an angle | flat `#3d3d3d`-class dark grey on `#d0d0d0` | *not observed unlocked* (locked in A and B too) | 84 × 42 |
| 4 R | Advocate of Destruction | A pair of **aviator sunglasses**, teardrop lenses, thin double bridge, temples splayed back | mirrored-silver ramp `#c8c8c8`→`#f8f8f8` on `#d0d0d0` | *not observed unlocked* (locked in A and B) | 90 × 45 |
| 5 L | Do You Feel Lucky, Punk? | A tall pointed **hood** with a floppy tip falling to the left and two small dark eye holes at the right | mid-grey with a darker brim | `#c80000` red (21–40 % of icon pixels), eye holes near-black | 90 × 60 |
| 5 R | Doggy Bag | A single **bone**, classic dumbbell shape with two knobs at each end, seen at a slight angle | modal `#d0d0d0`, highlights `#f8f8f8`, shading `#a8a8a8` | *not observed unlocked* | 87 × 47 |
| 6 L | Never Saw It Coming | Two rounded-rectangle **military dog tags** hanging from a ball chain; the front tag is embossed `LAIKA` reading bottom-to-top, the rear tag shows the same lettering mirrored | silver, `#f8f8f8` highlights | still silver — mean chroma **0.7** — the artwork is achromatic by design | 68 × 87 |
| 6 R | Mirror, Mirror, On The Wall | A **bow / hair ribbon**, two loops and two tails, covered in large round polka dots | modal `#d0d0d0`, dots `#f8f8f8` | ribbon `#f860c8`–`#f858c8` hot pink, dots white | 89 × 66 |
| 7 L | Suit Up! | A **gas mask**: squarish faceplate with two round eye lenses (each crossed by a diagonal highlight), a filter grille below, and a long ribbed corrugated hose curling to the right ending in a white perforated canister | mid-greys, hose banded light/dark | *not observed unlocked* | 98 × 46 |
| 7 R | Elite Hackers' Society | A square plate/**badge** with a recessed 8-bit relief cut into it: two square notches at the top corners, two small square holes, a stepped diagonal stroke down the middle, and a separate horizontal bar near the bottom | flat `#a8a8a8`-class grey with a bevelled edge | *not observed unlocked* | 54 × 56 |

`[UNCERTAIN]` The Elite Hackers' Society relief: the geometry is unambiguous, the
**reading** is not. The stepped diagonal plus the detached bar below is
consistent with a **pixel-art question mark**; it is equally consistent with a
blocky face or a deliberate "glitch" block. I describe the geometry and decline
to name it. What would settle it: any capture of that icon unlocked and at
native resolution, or the asset file.

`[INFERRED]` **The Hallowed Be Thy Name icon appears to be the same artwork as
the Garage's Halloween box.** Side-by-side at 3×, `UI/D-garage-kickstarter-eve-foxter25.png`'s pumpkin box
and B's achievement pumpkin share eye shape, nose, zig-zag mouth tooth count,
rib lines and stem angle. Two different sessions/years, so this is asset reuse
rather than one image. Falsifier: a native-resolution pair showing different
geometry. If true it means at least one achievement icon is **not** a wearable
tankcessory but the box art.

### 1c · How many distinct achievements can I name?

`[OBSERVED]` **Fourteen.** All fourteen titles, all fourteen locked
descriptions, all fourteen icons. Six of the fourteen also give an unlocked
description. Two of the fourteen (Suit Up!, Elite Hackers' Society) are attested
**only** by W — they fall below both PNG crops.

`[UNCERTAIN]` Whether fourteen was the *complete* catalogue in the A/B era. W's
grid is exactly full at 7×2 with no empty slot, and the txt header says "(14)".
A and B show rows 1–6 of both columns paired identically to W —
(Hallowed, Old Dog), (Put Her Down, Master), (Apprentice, Lord),
(Of Mice, Advocate), (Do You Feel Lucky, Doggy Bag), (Never Saw It, Mirror).
If the grid is filled **column-major** (item *n* at row *n*, item *n+7* opposite)
that pairing forces the A/B catalogue to also be 14 in 7 rows — a 16-item list
would pair Hallowed with Master, not Old Dog. If the grid is filled
**row-major** (1,2 / 3,4 / …) the pairing is preserved no matter how many items
follow, and A/B could hold more. I cannot decide from these frames.

`[INFERRED]` Weak support for column-major: it places the two secret
achievements last and adjacent (positions 13 and 14), and it puts the easier half
in the left column and the harder half in the right. Falsifier, and the thing to
look for in footage: **one frame showing row 7 of A/B's session, or any frame
where the panel is taller than 683 px.**

---

## 2 · Locked vs unlocked presentation — the reproducible spec

Everything below is `[MEASURED]` unless tagged otherwise. The two columns are
sampled from **the same image** (B) wherever possible; where a cross-image
comparison was unavoidable it is flagged.

### 2a · Row chrome

| Property | Unlocked | Locked |
|---|---|---|
| Card fill | `#ffffff` (B reads `#fdfdfd`–`#fefefe` through video) | `#d3d3d3` (W, lossless) / `#d4d4d4` (B) |
| Card outline | ≈ `#e9e9e9`, ~1 CSS px | none distinguishable from the fill |
| Drop shadow | **yes** — darkest `#969696` 1–3 px below the card, easing to page white over ≈ 24 capture px in B | **none** — `#d4d4d4` → `#fefefe` inside 3 px (B); `#d3d3d3` → `#ffffff` in one AA pixel (W) |
| Title colour | `#1d1c1c` (Apprentice) / `#2b262e` (Mirror) | `#ffffff` (W, exact) → reads `#f9f9f9` through video |
| Description colour | `#312829` / `#292627` | `#ffffff` (W, exact) → reads `#fafafa` |
| Icon | full colour, black point ≈ 0 | R = G = B (chroma ≤ 1 at the 99th percentile), black point lifted to 52–59, white point 255 |
| Icon shown? | yes | **yes** — locked rows show the full icon, not a silhouette |
| Description shown? | yes | **yes** — locked rows show the goal text |

`[INFERRED]` The design intent is a **polarity flip**, not a dimming: unlocked is
a raised white card with dark text; locked is a flat grey card with white text.
A rebuild that implements "locked" as `opacity: 0.5` on the unlocked card will be
wrong in every particular.

### 2b · Progress bar and counter

| Property | Value |
|---|---|
| Bar fill | `#afafaf` / `#adadad` |
| Bar track (unfilled remainder) | `#d4d4d4` — identical to a card with no bar |
| Bar height | **full card height** (x = 700 column scan: ≈ 174 from y 116 to y 230, card 115→231) |
| Bar origin | the card's left edge |
| Bar width | **linear in progress/target across the full card width** — 63.98 % measured vs 63.70 % expected; 6.29 % vs 6.37 % |
| Counter text | light, `#ededed` brightest-40 median, sits **over** the bar and continues past its edge |
| Counter position | bottom-left of the card, below the description block |
| Counter format | `N of M` — `637 of 1000`, `637 of 10000` — lowercase `of`, single spaces, no thousands separator |
| Counter appears when | `[INFERRED]` progress > 0 only (three of six locked rows have one; the three without are a time achievement, a streak achievement, and one at zero) |
| Counter/bar in the fully-locked account (W) | **absent everywhere** — consistent with "progress > 0 only", since that account had nothing |

`[INFERRED]` What this implies about how progress was surfaced: the panel showed
**absolute counters, not percentages**, and the bar was a background wash on the
row rather than a separate widget. A player could read exactly how many kills
they had (`637`) from a page whose only other numeric surface was the Top-10 box.
That is a real product fact the reconstruction did not have.

---

## 3 · Link to S5 — the achievement unlock float

**[S5](../../standards/VISUAL-EVIDENCE-WANTED.md) as it stands:** *"Box art + glow tween
O-exact. Title/description/icon from `x_checkForAchievements` never captured;
only ids {28-32,34-36} known, 1-27+33 existed unobserved."* Evidence pointer
`srv/index.php:1218-1261`.

### The real lines

`[OBSERVED]` grepped, not assumed:

* `srv/index.php:1218` — `<div id="achievementfloat" class="text black" style="… background-image: url('images/achievementNotificationBox.png'); position: fixed; z-index: 1002; top: 10px; left: 50%; margin-left: -160px; width: 230px; height: 50px; opacity: 0; padding: 15px 75px 15px 15px;">`
* `srv/index.php:1219` — `<img id="achievementfloatimage" src="images/attentionSign.jpg" style="width: 100px; height: 100px; position: absolute; top: -15px; left: 218px;"/>`
* `srv/index.php:1220-1221` — `#achievementfloattitle` (`class="text medium"`) and `#achievementfloatdescription`
* `srv/index.php:1223` — `#achievementfloatglow`, `background-color: #ffffaa`, `box-shadow: 0px 0px 20px 20px #ffffaa`
* `srv/index.php:1231-1262` — `function achievement_cb(response)`
* `srv/index.php:1752-1754` — `function x_checkForAchievements() { sajax_do_call("checkForAchievements", …) }`
* `srv/index.php:683-684` — `// Check for achievements` / `x_checkForAchievements(achievement_cb);` (the login-time call)
* `srv/index.php:1261` — the 5001 ms re-arm that calls `x_checkForAchievements(achievement_cb)` again when the float finishes fading

(The same block repeats at 2803/2816/2846, 5382/5395/5425, 11360/11373/11403,
13085/13098/13128, 14628/14641/14671, 16084/16097/16127 — one per route. The
`:1218-1261` occurrence is the one inside `tt_page_root()`, which begins at
`:204`.)

### What `achievement_cb` needs, and what I can now supply

`[OBSERVED]` The callback reads four children off the response node
(`:1243-1252`):

```js
document.getElementById('achievementfloattitle').innerHTML = currentUnlock.childNodes[1].innerHTML;
document.getElementById('achievementfloatdescription').innerHTML =
        currentUnlock.childNodes[0].innerHTML + ": " + currentUnlock.childNodes[2].innerHTML;
if (currentUnlock.childNodes[3].innerHTML != "") { … .src = currentUnlock.childNodes[3].innerHTML; }
```

So the wire format is a node with **four** children: `[0]` and `[2]` are joined
by `": "` to make the description line, `[1]` is the float title, `[3]` is an
image URL (empty ⇒ hide the image).

`[INFERRED]` **My transcription is directly the missing content for `[2]`.** The
float fires at the moment of unlocking, so the string it shows must be the
**unlocked** ("You …") description, not the locked imperative. I can now name six
of them exactly:

| Achievement | String that plugs into the float |
|---|---|
| Hallowed Be Thy Name | `You trick'r'treated your way to new swag!` |
| Put Her Down | `You showed that Space Dog who's the leader of the pack!` |
| Apprentice of Destruction | `You've destroyed 100 tanks!` |
| Do You Feel Lucky, Punk? | `You killed Laika when she was out of bullets!` |
| Never Saw It Coming | `You zapped Laika with a direct laser hit!` |
| Mirror, Mirror, On The Wall | `You changed your look 20 times!` |

`[UNCERTAIN]` Which of `[0]` / `[1]` carries the achievement **name**. Two
readings fit the code equally:

* **(a)** `[1]` = the achievement name (`Hallowed Be Thy Name`) and `[0]` = a
  category word, giving a description line like `Achievement: You trick'r'treated
  your way to new swag!`
* **(b)** `[1]` = a fixed banner (`Achievement Unlocked!`) and `[0]` = the
  achievement name, giving `Hallowed Be Thy Name: You trick'r'treated your way to
  new swag!`

Reading (b) is the more natural sentence and explains why the author bothered
with a third string at all — but this is style, not evidence. **A single frame of
the float in situ settles it**, and that frame remains the top want for S5.

`[INFERRED]` For `[3]`, the icon: the float image slot is fixed at 100×100 px
(`:1219`). The panel icons measure 54–98 px wide by 42–87 px tall in CSS pixels.
So the same artwork family fits the slot without upscaling. Whether the float
served the **colour** icon (it should — the achievement has just been unlocked)
or a distinct larger asset is `[NOT VISIBLE]`.

`[OBSERVED]` The default `src` is `images/attentionSign.jpg` — a placeholder that
is replaced on every real unlock. Nothing here contradicts the held box art or the
glow tween, both of which S5 already holds as O-exact.

### The id mapping — what a wiki table (or this panel) does NOT establish

`[OBSERVED]` **None of these three images shows an achievement id.** Not in the
DOM (I have pixels, not markup), not in a URL, not in a tooltip, not in the
artwork.

`[INFERRED]` This is worth stating flatly because it is the natural mistake to
make: *a list of names, however complete, cannot be zipped against a list of ids,
however complete.* `DECISIONS.md:168-170` records that only ids
{28, 29, 30, 31, 32, 34, 35, 36} appear at v4.0 call sites and that the numbering
proves 1–27 and 33 existed. I can now name **fourteen** achievements. Fourteen
names and thirty-six-plus ids do not line up under any ordering. Either the id
space is shared with something else (accessories are the obvious candidate —
`DECISIONS.md:192` records the seeded DB as `accessories 21, achievements 8`), or
many ids are retired/unreleased, or ids are not one-per-achievement at all.
Guessing the mapping from name order would be exactly the kind of invention the
[OVERHAUL RULE](../../standards/VISUAL-EVIDENCE-WANTED.md) exists to prevent.

**Evidence that would actually establish id ⇄ achievement**, in descending order
of decisiveness:

1. `[INFERRED]` **An era HTML capture of `?garage` while logged in.** The panel
   markup is server-generated; each card almost certainly carries an id in an
   element id, class or handler. That single artefact would deliver the mapping,
   the exact markup, the CSS class names, and the progress-bar mechanism at once.
   **This should be a new want.**
2. `[INFERRED]` **The decompiled AS2 call sites already in `archive/decompiled/`.**
   `LEDGER.tsv:165` says there are six client call sites carrying
   `achievementId` / `achievementIds` / `achievementProgress`. The *surrounding
   game code* at each site — which branch fires it — ties an id to a behaviour,
   and behaviours map onto these fourteen descriptions unambiguously (a laser
   kill on Laika can only be "Never Saw It Coming"). This needs no new evidence,
   only reading what the repo already holds. **Highest value per unit of effort.**
3. `[INFERRED]` **A captured `checkForAchievements` SAJAX response body.** Its
   `childNodes[3]` is an image URL; if that URL is of the form
   `images/achievement<NN>.png` it gives the mapping directly.
4. `[INFERRED]` **A CDX row for `achievement.php?achievementId=NN`** paired with
   an identifiable in-game moment. `DECISIONS.md:536-537` says there are zero CDX
   rows of any kind for `achievement.php`, so this is a long shot.
5. `[INFERRED]` **Frame-stepping era footage of a float in the moment of an
   identifiable action** (e.g. a 100th kill) gives name ⇄ trigger but still not
   name ⇄ id.

**Proposed S5 status: `WANTED` → `PARTIAL`.** Title, description (both variants
where seen), icon artwork and icon dimensions are now held for the whole
catalogue; the float's own composed layout and the id mapping are not.

---

## 4 · Cross-check with the two text files

### `acheivements.txt`

Covered in full under its file section. Summary: `[OBSERVED]` **12 of 14
descriptions verbatim-correct, 1 normalised (`10` for `ten`), 1 flatly wrong
(`Old Dog - Hang around for 1 month.` vs the pixels' `Hang around for more than a
year!`)**; the reward table omits one row and mislabels another
(`Sailor hat` for what the pixels show as a polka-dot bandana). `[INFERRED]`
Because its ordering is exactly W's column-major reading order, it is a
transcription of an image like W, not an independent witness — it corroborates
nothing and inherits every error of its transcriber. **Grade it strictly below
the pixels. Use it only for the reward accessory names and the secret-achievement
asterisks, and label those as community claims.**

### `UI/tellafriendpopup.txt` — where the Sunglasses claim actually lives

`[OBSERVED]` Verbatim, in full:

> To unlock the Sunglasses ("Advocate of Destruction") achievement in TankTrouble,
> send referral emails to 10 friends inviting them to create an account using the
> "Tell A Friend" option on the game's interface.Requirements & StepsAchievement
> Name: Sunglasses (Advocate of Destruction)Difficulty: HardAction Required: Use
> the "Tell A Friend" feature located on the right side of the game interface to
> invite 10 people/emails telling them to create an account.If you need help with
> other secret or difficult achievements in TankTrouble, let me know which item or
> trophy you are trying to unlock next!
>
> they get a link, from there and sign up, 10 friends and they sign up then you
> get silver sunglasses.

`[INFERRED]` The first paragraph has run-together headings
(`interface.Requirements & StepsAchievement Name:`), a "Difficulty: Hard" rating
nothing in the game surfaces, and closes with `let me know which item or trophy
you are trying to unlock next!` — **it is a chatbot answer pasted into a file**,
not a capture. The second paragraph is Ethan's own note. Grade the first
paragraph as hearsay (M3-class) and the second as an owner claim.

`[OBSERVED]` **The pixels corroborate the substance completely**, which is why
this matters:

| Claim in the txt | Pixel evidence | Verdict |
|---|---|---|
| The achievement is named "Advocate of Destruction" | W row 4 R title, and B row 4 R title, independently | **corroborated** |
| It is unlocked via "Tell A Friend" | description reads `Get 10 friends to sign up using "Tell a Friend"!` — W and B, independent | **corroborated**, including the exact casing `Tell a Friend` |
| The count is 10 | `Get 10 friends…` | **corroborated** |
| They must **sign up**, not merely be emailed | `…to sign up using…` | **corroborated** — this is the operative distinction and the pixels back it |
| The reward is sunglasses | icon is a pair of aviator sunglasses, 90 × 45 px | **corroborated** |
| The sunglasses are silver | icon is a mirrored-silver ramp `#c8c8c8`→`#f8f8f8` — but the row is **locked** in every frame I have, so this is the desaturated render | **unsettled**: consistent, not proven. `acheivements.txt` independently calls the reward `Silver Glasses` |
| "located on the right side of the game interface" | not in my frames | `[NOT VISIBLE]` — but see below |
| "Difficulty: Hard" | no difficulty rating appears anywhere in the panel | **not corroborated**; likely invented |

`[OBSERVED]` One more thing the pixels add that neither text file has: in B, the
Advocate row carries **no progress counter**, while Master and Lord do. Under the
"counter only when progress > 0" rule that means this account had invited **zero**
successful sign-ups. `[INFERRED]` It also means the counter for Advocate would
have read `N of 10` — a directly testable prediction for any future footage.

**Link to the Tell-A-Friend surface.** The panel-side half of this achievement
is documented here; the sending surface — the popup, its form, its copy, and the
`J-popup-send-pressed-still-open` behaviour — is another analyst's topic. See
[`J-tell-a-friend.md`](./J-tell-a-friend.md). The two documents together are what
close the loop: this one proves the achievement text says `"Tell a Friend"`
verbatim with that exact casing, which is a string the J surface must match.

---

## 5 · Link to S97 — `achievement.php`

**[S97](../../standards/VISUAL-EVIDENCE-WANTED.md) as it stands:** *"Stub, zero CDX rows;
6 AS2 call sites; user-visible output unknown."* Pointer `LEDGER 165`.
`LEDGER.tsv:165` reads:

```
srv/includes/achievement.php	M2	—	written 2026-08-02	6 client call sites in decompiled AS2; achievementId/achievementIds/achievementProgress; no response body captured	—	501 stub (milestone 1)
```

`DECISIONS.md:536-537`: *"achievement.php: zero CDX rows of any kind — no
observed response ever."*

**Does anything here tell you what that endpoint returned?**

`[NOT VISIBLE]` **No.** These are three renders of a *page* surface. The Flash
game's RPC to `includes/achievement.php` is invisible in any screen capture, and
none of the frames shows a network panel, a console, an error body or a URL.
`[NOT VISIBLE]` is the honest and correct answer, and it should stay recorded as
such so the want-list does not quietly drift into thinking this topic covered it.

`[INFERRED]` What these images *do* contribute to S97 is one thing, and it is
worth writing down: **they show what `achievementProgress` looks like when it
reaches a user.** The ledger row names the parameter; B shows the rendered form —
an integer numerator over a fixed target, printed as `N of M`, plus a
proportional full-card-height bar. That does not constrain the wire format, but
it does mean any reconstruction of `achievement.php` must be able to answer with
a *per-achievement integer*, not just a boolean unlocked flag. That is a real
constraint the stub did not previously have.

`[INFERRED]` A second, weaker note: the panel's progress numbers (`637` for both
Master and Lord) are the **same** integer against two thresholds. So the server
stores one counter per *statistic*, not one per *achievement*, and
`achievementProgress` is a projection of a shared counter. Falsifier: any frame
where two thresholds of the same statistic show different numerators.

**Proposed S97 status: stays `WANTED`.** Its "See S5" pointer is still correct.

---

## 6 · Is there an achievements PAGE?

**[S114](../../standards/VISUAL-EVIDENCE-WANTED.md) as it stands** lists *"achievement list
page"* among *"code hints without names"* whose very existence is unknown.

`[OBSERVED]` **The chrome is the site's, not a wiki's.** Set out plainly, since
the brief asks me to be explicit:

* W carries **zero** wiki UI strings. Compare `Game/weapons.txt`
  (`Weapons` / `Sign In to Save` / `View source`) and `Game/ranks.txt`
  (`Ranks` / `Sign In to Save` / `Edit`), which are unmistakably wiki article
  text. W has none of that — no article title bar, no edit affordance, no rail.
* W's chrome is a **centred username**, a **section heading** and a **green tick
  button** — the exact chrome of `UI/D-garage-kickstarter-eve-foxter25.png`, whose address bar reads
  `www.tanktrouble.com/?garage`, and of `UI/D-garage-2018-url-bar-youtube-toast.png`, whose address bar reads
  `https://tanktrouble.com/?garage`.
* A and B carry a **live cursor** and video compression, i.e. they are footage of
  a running browser, not a rendered wiki table.

`[MEASURED]` **And it is not merely "site-like" — it matches held O bytes to the
pixel.** W is 692 px wide; `srv/index.php:4046` animates the panel width to
**692**. W is 683 px tall; `srv/index.php:4050` animates the content height to
**605**, and W's first card top edge is at **y = 78**, with 605 + 78 = 683.

**So: yes, the surface exists, and this is the first evidence of it.** But I want
to be precise about the word *page*, because S114's phrasing invites the wrong
conclusion:

`[INFERRED]` **It is a sub-view of the logged-in user panel, not a page with its
own URL.** It is opened by the `userpanelStats` trophy button (visible in
`D-garage-2018-url-bar-youtube-toast.png`), it expands the panel in place (width 692, content height 605,
wrapper height 720), it fades its content in over 200 ms, and it is dismissed by
`userpanelAcceptStats` — the green tick in W's bottom-right corner. All of that
happens inside `?garage`. Held O bytes agree independently: the 10-02-2013 news
item at `srv/index.php:8545` says *"Go to the Garage to see which ones you
already have and to scope out your next goal!"*, linking `?garage`.

`[NOT VISIBLE]` Whether the trophy click also changed the URL (a hash, a query
parameter) — nothing in these frames shows an address bar.

`[UNCERTAIN]` The id name is `Stats`, not `Achievements`, and the heading in W
reads `Achievements`. Two readings: either the "Stats" view *is* the achievements
view and the id is a legacy name, or the view could show other statistics for
other accounts/eras and this account's render happens to be all achievements. The
605 px content height is fully consumed by 7 card rows (544 px) plus the tick
strip (61 px), which leaves no room for an additional statistics block, so I lean
to the first. Falsifier: a 692×683 panel frame showing anything other than the
achievement grid.

**Proposed S114 status: split the entry.** The *"achievement list page"* item
should move from `speculative / unknown-existence` to **`PARTIAL` — exists,
identified as `#userpanelStatsPage` (the `openStats` sub-view of the garage user
panel), geometry 692 × 683 with 605 px content**, leaving the rest of S114's list
(filter values beyond `'all'`, sherif-star panel, `content.php`, `Select2` tabs,
add-friend UI, ranks outside the lab) untouched. Note in passing that this
evidence also **names the sherif-star**: `userpanelSherifStar` is one of the five
user-panel buttons at `srv/index.php:3512-3520`, guarded by a `!= null` check —
i.e. it is rendered only for some users — which is consistent with S114's
"sherif-star panel" being a moderator affordance. That is a bonus, not my topic,
and I have not looked for it in pixels.

---

## Consequences for the rebuild

### Confirmed

* `[MEASURED]` `srv/index.php:4046` `tempFX.start(692)` — the panel really is
  692 px wide in the Stats state. W is 692 px wide.
* `[MEASURED]` `srv/index.php:4050` `tempFX.start(605)` — content height 605.
  W's height (683) minus its first card's top offset (78) is exactly 605.
* `[MEASURED]` `srv/index.php:4053` — the 200 ms linear opacity tween on
  `#userpanelStatsPage`. Image A is a frame of it at α ≈ 0.52.
* `[MEASURED]` `srv/index.php:4055` — `#userpanelAcceptStats`. W's green tick,
  25 × 32 px, bottom right.
* `[OBSERVED]` `srv/index.php:8545` (news, 10-02-2013) — achievements are
  reached "in the Garage". Corroborated by pixels.
* `[OBSERVED]` `srv/index.php:8622` (news, 07-12-2012) — the Golden Box holds
  achievement-only tankcessories. `UI/D-garage-kickstarter-eve-foxter25.png` shows the gold star box beside
  the plain, Halloween and Christmas boxes.
* `[OBSERVED]` `LEDGER.tsv:165` — `achievementProgress` is real and
  user-visible; B shows its rendered form.

### Contradicted — overhaul owed

* `[OBSERVED]` **`manualevidence/acheivements.txt` must not be used as a source
  for description strings.** `Old Dog — Hang around for 1 month.` is wrong; the
  panel says `Hang around for more than a year!` in two independent images. If
  any M2/M3 seed, fixture or doc in the repo took its achievement copy from a
  community list of this kind, **the OVERHAUL RULE applies and it is rewritten
  wholesale against the table in §1a**, not patched. I could not check
  `docker/mysql/init/*.sql` (only `srv/index.php` was staged), so this is
  flagged rather than asserted: **grep the seed for `Old Dog` and for
  `1 month`.**
* `[INFERRED]` Any invented "locked" styling that implements dimming as an
  opacity reduction on the unlocked card is contradicted. The real treatment is a
  **polarity flip** (white card + `#1d1c1c` text ⟷ `#d4d4d4` card + `#ffffff`
  text) plus **shadow present ⟷ shadow absent**, plus icon **desaturation with a
  lifted black point**, not a fade.
* `[MEASURED]` `DECISIONS.md:168-170`'s framing — "only ids {28-32,34-36} appear"
  — is not contradicted, but the arithmetic now visible (14 achievements vs
  36+ ids) means **no future doc should imply the id space is one-per-achievement**.
  If any note does, it needs correcting.

### Still unknown / stays on the want-list

* ~~`[NOT VISIBLE]` **The unlock float in situ.**~~ **FOUND — in another
  topic's file.** Nothing in *my* four files shows it, but
  [`UI/B-frontpage-achievement-unlock-float.png`](./UI/B-frontpage-achievement-unlock-float.png) (topic
  [B](./B-maze-editor-interaction.md)'s list) does: a rounded white panel with a
  drop shadow, top-centre over the front-page headline, reading

  > **Hallowed Be Thy Name**
  > `mr_enderman: You trick'r'treated your way to new swag!`

  with the jack-o'-lantern icon at the right, overhanging the panel's top edge.

  `[OBSERVED]` **That answers the sharper ask I was about to file:** the
  description line is `<name>: <You…>`, **not** `Achievement: <You…>` — the one
  thing `achievement_cb` left ambiguous. It also confirms the icon shown in the
  float is the **unlocked, full-colour** artwork, and that title and body use
  two different sizes of the same face.

  `[OBSERVED]` The strings match my locked-row transcription for this
  achievement **verbatim**, so the same copy is now attested on two independent
  surfaces (panel row and unlock float) in two different account states. That is
  a stronger corroboration than either alone.

  **S5 moves from MED/WANTED to PARTIAL** on this basis. What still stays on the
  list: the float's **5-second glow/tween in motion** (a still cannot show it),
  and floats for the other thirteen achievements.
* `[NOT VISIBLE]` **The id ⇄ achievement mapping.** See §3 for the five evidence
  classes that would establish it, ranked.
* `[NOT VISIBLE]` `achievement.php`'s response body. S97 stays `WANTED`.
* `[NOT VISIBLE]` The eight unlocked description strings not yet seen: Of Mice
  and Men, Suit Up!, Old Dog, Master, Lord, Advocate, Doggy Bag, Elite Hackers'
  Society.
* `[NOT VISIBLE]` The unlocked (colour) artwork for eight of the fourteen icons.
* `[UNCERTAIN]` Whether the catalogue was still exactly 14 in the A/B era —
  needs one frame showing row 7 of that session.
* `[UNCERTAIN]` The desaturation formula, and whether locked art is a filter or a
  separate asset.
* `[NOT VISIBLE]` The panel's markup, class names, the trophy button's `onclick`,
  and whether the trophy click changes the URL.

### New wants to add

1. **`?garage` HTML captured while logged in.** Not a screenshot — the *body*.
   One such artefact delivers the panel markup, the per-card ids (hence the S5 id
   mapping), the exact strings, the progress-bar element and its class, and the
   CSS hooks. This is the highest-value single artefact for this whole topic and
   for S113. Look in CommonCrawl/Wayback for any `?garage` body longer than the
   held 2018-12-14 logged-out one (`index.php:3375`, 2574 lines).
2. **A frame of the achievements panel showing row 7 and the green tick** in a
   live session — settles both the catalogue length and the column-fill order.
3. **A frame at 0 progress on a countable achievement** — tests the "counter only
   when progress > 0" rule. Advocate of Destruction at `0 of 10` would do it.
4. **Two frames of the same icon, one account locked and one unlocked, at the
   same zoom** — settles the desaturation formula.
5. **The unlock float, frame-stepped** — S5's existing trigger, with the
   sharpened ask above.
6. **Read the six AS2 `achievementId` call sites in `archive/decompiled/`.** Not
   footage — desk work on bytes the repo already holds. Highest value per unit of
   effort for the id mapping.

---

## Recommended edits to existing docs (not applied)

These are suggestions only. I have edited nothing.

**1 · `docs/standards/VISUAL-EVIDENCE-WANTED.md`, S5 — status `WANTED` → `PARTIAL`, and
rewrite the "what's missing" cell:**

> | S5 | **Achievement unlock float — content** | animation / page-look | Box art + glow tween O-exact. **PARTIAL: the achievement catalogue is now held — 14 titles, 14 locked descriptions, 6 unlocked ("You …") descriptions, 14 icons measured — from `manualevidence/Game/G-achievements-panel-full.webp` + two UI frames; see `manualevidence/G-achievements.md`.** Still missing: the float's own composed layout (`childNodes[0]`/`[1]` roles), and the id↔achievement mapping — a name list does NOT establish it | `srv/index.php:1218-1261`, `:1231-1262`, `:1752-1754` | Yellow glow flashes top-centre after login/round — freeze the 5s; read whether the description line is `<name>: <You…>` or `<category>: <You…>` | MED |

**2 · `docs/standards/VISUAL-EVIDENCE-WANTED.md`, S114 — promote the achievement-list item
out of the speculative list into its own entry:**

> | S114a | **Achievements list — the `openStats` panel view** | page-look | **EXISTS, IDENTIFIED.** `#userpanelStatsPage`, the Stats sub-view of the logged-in garage user panel; opened by the `userpanelStats` trophy button, dismissed by `userpanelAcceptStats` (green tick). Geometry pinned: panel 692 × 683 px, `#userpanelContent` 605 px, header block 78 px, 7 × 2 cards at 80 px pitch. Still unknown: the markup, per-card ids, whether the URL changes | `srv/index.php:4042-4056`, `:3501-3552`, `:8545`; `manualevidence/G-achievements.md` | Logged-in user clicks the trophy in the Garage panel — hold the 200 ms fade and the finished grid | MED |

and strike `achievement list page` from S114's remaining list, leaving the other
unknown-existence items as they are.

**3 · `docs/standards/VISUAL-EVIDENCE-WANTED.md`, S97 — keep `WANTED`, add one line to
"what exists":**

> …6 AS2 call sites; user-visible output unknown. **`achievementProgress` is now
> known to surface as `N of M` plus a proportional full-card-height bar
> (`manualevidence/G-achievements.md`), so the endpoint must be able to
> answer with a per-achievement integer, not a boolean. The two 1000/10000 rows
> show the same numerator (637), so the counter is per-statistic, not
> per-achievement.**

**4 · `DECISIONS.md` — append a new dated entry** (append-only, per the repo's
own rule):

> ## 2026-08-04 — the achievement catalogue is 14 names, and names are not ids
>
> Three manual-evidence images (`Game/G-achievements-panel-full.webp` 692×683,
> `UI/G-achievements-panel-fade-alpha-052.png`, `UI/G-achievements-panel-progress-bars.png`) give the full achievement
> catalogue: 14 titles, 14 locked descriptions, 6 unlocked descriptions, 14
> icons. The webp is a 1:1 capture — its 692×683 is exactly `openStats`'
> `tempFX.start(692)` (`srv/index.php:4046`) and `605` content height (`:4050`)
> plus a 78 px header — so the achievements list is `#userpanelStatsPage`, the
> Stats sub-view of the garage user panel, not a page. M2 at best (wiki-rehosted
> / era footage), never O.
>
> The 2026-08-03 entry stands: ids {28-32,34-36} are still the only observed
> ones. But 14 names against 36+ ids means the id space is not one-per-
> achievement, and **nothing in a name list maps a name to an id**. No seeded
> achievement row may acquire a name on the strength of this evidence. The
> mapping needs either a logged-in `?garage` body or the surrounding code at the
> six AS2 `achievementId` call sites.
>
> Also recorded: `manualevidence/acheivements.txt` is a transcription of a
> screenshot of this same panel (its order is the panel's column-major reading
> order) and contains at least one outright error — `Old Dog - Hang around for
> 1 month.` where the pixels say `Hang around for more than a year!`. It is
> graded below the pixels wherever they disagree.

**5 · `DEDUCE.md` §4.3 — the `includes/achievement.php` row keeps grade C**, but
its evidence cell could gain *"+ rendered `achievementProgress` observed in era
footage (M2)"*.

**6 · `LEDGER.tsv`** — if and when these three images are archived under
`archive/`, they need M2 rows with URL / uploader / date / timestamp per guide
§6.5 and the [OVERHAUL RULE](../../standards/VISUAL-EVIDENCE-WANTED.md) step 3. I have not
archived anything.

**7 · A note for whoever writes the achievements panel** — the constants worth
pinning, all from W at 1:1 CSS px, all `[MEASURED]`:

```
panel            692 × 683, fill #ffffff, 2px #d3d3d3 frame, radius ~3-4px
header block     78px  (username #666-ish, centred, cap 13px;
                        section heading #000000, centred, cap 16px)
content          605px, y 78..682
card grid        7 rows × 2 cols
  left card      x  32..337   (306 wide)
  right card     x 352..656   (305 wide)
  gutter         14px
  card height    64px,  row gap 16px,  row pitch 80px
  card radius    ~5px
  card fill      locked #d3d3d3 (no shadow) | unlocked #ffffff (+ shadow, darkest ~#969696)
  text inset     9px from the card's left edge
  title          cap height 11px, top at card_top+13
  description    cap height  8px, line pitch 14px, bolder than the title
  text colour    locked #ffffff | unlocked ~#1d1c1c (title) / ~#312829 (desc)
  icon           right-aligned to the card's right edge, 54-98 wide × 42-87 tall,
                 free to overflow the card vertically — do NOT clip
  progress fill  #afafaf, full card height, from the left edge,
                 width = progress/target × card width (verified to ±0.3pp)
  counter        "N of M", light (~#ededed), bottom-left, over the fill
accept tick      25 × 32 green (#00b000..#00f000), bottom right,
                 16px below the last card, ~11px in from the frame
```

`[UNCERTAIN]` The 692/683 figures include the 2 px frame; see the box-model note
in §"The identification, in detail". Resolve against the era `styles.css` /
`boxStyles.css` rules for `#userpanel` before hard-coding.
