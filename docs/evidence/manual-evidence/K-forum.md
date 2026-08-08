# Visual evidence — the Tank Owner's Forum

> Analysis of 1 evidence file under `manualevidence/`.
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)

---

## Scope and provenance

One file, and it is the only forum pixel this corpus contains:

- `./UI/K-forum-thread-preview-list-2015.png` — 1886×1047, RGBA
  PNG. Assignment sheet records the capture as **16:47:33**; the staged copy's mtime is
  `2026-08-04 05:53:24 UTC`. Per BRIEF §"Consequences" (2) that mtime is **when Ethan saved the
  crop**, not when the footage was made, and with a single file there is no capture *order* to
  reconstruct. It belongs to the `{GUID}.png` batch (auto-named screen grabs), so unlike the
  `selectedwall-…`-style files it carries **no filename claim from the repo owner** — nothing to
  corroborate or contradict on that axis.

`docs/standards/VISUAL-EVIDENCE-WANTED.md` §F opens: *"Forum — second-largest hole (100% SAJAX-rendered).
Era-final `?forum` = `<div id="forumwrapper"></div>` only. **No archived rendered forum HTML
exists at all.**"* and the ranked shortlist puts *"A forum thread view with mixed bubble colours
(S57-S63) — the only way any forum pixel is ever recovered"* at #4. This frame is the first
recovered forum pixel. It is **not** the thread view that was asked for — it is the
**thread-preview list (S57)** — and it is **not from the target era**.

**Headline caveat, stated up front:** this frame is from **February 2015**, not 2017–2018 (see
§8 Dating). Everything below is evidence about the *forum as it stood ~3 years before the target
era*. Some of it is provably era-stable (strings and markup that survive verbatim into the
era-final `srv/index.php`); some of it is provably *not* (the nav strip has five tabs here and
six in the era-final markup). I flag which is which at every point.

I could only read `srv/index.php` — **`srv/includes/forumStyles.css` is not present in the staged
copy** (`srv/` contains `index.php` and nothing else; `srv/images/` likewise absent). All
`forumStyles.css` facts below are quoted from the want-list's own summary of it, never from the
file, and I say so each time.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| 1 | The frame is a **thread-preview list**, not a thread view: 8 preview rows visible, ordered by most-recent activity descending | `[OBSERVED]` | S57 → PARTIAL | first forum pixel; nothing to supersede |
| 2 | Preview row anatomy = *[N participant tanks][pointer][speech bubble: bold title / body+`[click to open]` / participants+times]* | `[OBSERVED]` | S57 | — |
| 3 | Bubble geometry measured: fixed 70 px (53 CSS) pointer, fixed apex offset, 3–5 CSS px corner radius, ~1 CSS px near-black border, soft down-right shadow, ~21.5 CSS px vertical overhead | `[MEASURED]` | S58 → PARTIAL | — |
| 4 | **All eight bubbles are white.** No `.grayBubble`, no `.yellowBubble` anywhere in frame | `[MEASURED]` | S58 stays WANTED | — |
| 5 | **All eight pointers are on the LEFT.** The preview list does not alternate | `[OBSERVED]` | S58 | narrows the "alternating" claim to thread view |
| 6 | Bubble left edge is **identical to 0.1 px across five different single-participant posters** → `scale` was the same for all five | `[MEASURED]` | S59 → PARTIAL | first empirical constraint on "scale varies per user" |
| 7 | Tallest tank sprite = 55.7 CSS px, i.e. exactly `55 × scale` with `scale = 1` (`index.php:12074`) | `[MEASURED]` | S59 | confirms the 110×55 base |
| 8 | Per-extra-participant horizontal advance = **55–59 CSS px**, about half the 110 px SWF width → tank slots overlap | `[MEASURED]` | S59 | new constant, previously unknown |
| 9 | A **three-speech-bubbles + grey right-arrow icon**, 58×32 CSS, right-aligned above the list — the only control on the page | `[OBSERVED]` meaning `[UNCERTAIN]` | S65 / S66 | first candidate art for either |
| 10 | **No composer, no reply box, no filter dropdown, no page numbers, no per-post icons** anywhere in the visible page | `[NOT VISIBLE]` | S61, S62, S64, S65, S66 stay WANTED | — |
| 11 | Nav strip has **five tabs (game/news/garage/forum/lab) — no shop tab**; forum tab is selected and renders as pure white with a black-outline bubble icon | `[OBSERVED]` | VE entry 10 | does **not** upgrade `tab5Select.jpg`; it is a different generation |
| 12 | Frame dates to **~17–21 Feb 2015** (Kickstarter countdown at 2 d 10 h 43 m before the 23-02-2015 launch; no shop tab; visits 30,730,115 ≪ era-final 68,374,157) | `[INFERRED]`, high | S110, dating discipline | — |
| 13 | It is **tanktrouble.com itself**, not a clone: omnibox reads `www.tanktrouble.com/?forum` | `[OBSERVED]` | S110 | — |
| 14 | Countdown widget (`index.php:12394-12398`) confirmed in Courier with the coded 4-tier size ladder — but the 2015 string is **"launches in"**, era-final code says **"launch in"** | `[MEASURED]` | new | — |
| 15 | Mod Activity box (`index.php:13044-13049`) confirmed live on `?forum`: three name/time pairs, name in `text small gray`, time in `text tiny` | `[OBSERVED]` | S105 | validates the frozen live region's *shape* |
| 16 | Login box confirmed: "?" at header top-left, grey `username` placeholder, **exactly 8 password bullets** (= `value="password"`, `index.php:12438`), `Log in` + `Sign up` | `[MEASURED]` | S6/S9 context | — |
| 17 | Anomaly: a thread with **two participants and "no posts yet"** — the participant list is not simply "starter + repliers" | `[OBSERVED]` | S57 / S64 | new want |

---

## File-by-file analysis

### `UI/K-forum-thread-preview-list-2015.png` (1886×1047, captured 16:47:33)  *(was `{77910683-A2A9-45B8-A639-94A12325BDAE}.png`)*

**Filename claim (repo owner):** none — this is a GUID-named auto-capture. Nothing to corroborate.

---

#### 0. Calibration — how capture pixels convert to CSS pixels

Everything below is quoted twice: capture px (what I measured) and CSS px (what the rebuild needs).
The conversion factor was derived four independent ways before I used it.

| Anchor | Nominal (CSS) | Measured (capture px) | Implied factor |
|---|---|---|---|
| Page content block, `<div style="width: 1312px; margin: auto;">` `index.php:12035` | 1312 | left-most page ink x=85 → right-most x=1798 = **1713** | 1.306 |
| `#centerColumn` `width: 692px` `index.php:12039` | 692 | derived span 493…1397 = **904** | 1.306 |
| `images/availableOnTheAppStore120.jpg` (filename asserts 120 px) `index.php:13025` | 120 | badge x 1634…1791 = **158** | 1.317 |
| `images/envelope.jpg height="29px" width="72px"` `index.php:13058` | 72 × 29 | black slot bar 1666…1759 = **94** wide; graphic ink 871…908 = **37** tall | 1.31 / 1.28 |

`[MEASURED]` **Adopted factor: 1.31 ± 0.01 capture px per CSS px.** All CSS figures below are
`capture ÷ 1.31`, rounded to 0.1.

`[MEASURED]` The Chrome bookmark star in the omnibox measures **exactly 16 × 16 capture px** and
the vertical scrollbar ~17 px — both are their native 100 %-DPI sizes. So the *video* is 1:1 with
the screen and the 1.31 factor is **page-side** (browser zoom and/or Windows DPI scaling), not a
video upscale. `[OBSERVED]` corroborating this, the omnibox shows Chrome's **zoom indicator**
(magnifier with a `+`) at x≈1795, which only appears when page zoom ≠ 100 %. I cannot decompose
1.31 into a specific zoom step (Chrome's steps are 110/125/150 — none is 131 %), so I record the
factor empirically and note the residual uncertainty. It does not affect the CSS numbers, which
are anchored on page elements.

Two consequences worth stating: (a) at 1.31 the *visible* page is 1047/1.31 ≈ **799 CSS px tall**;
(b) the browser window is maximised (`[OBSERVED]` the restore-down icon, two overlapping
rectangles, at the top right).

---

#### 1. Page identity and chrome

**Browser chrome** `[OBSERVED]`, transcribed verbatim:

- Tab title, truncated by the tab width: **`TANK TROUBLE Tan…`** (the favicon is the black-and-white
  maze square). The full title is cut; I will not guess the rest.
- Omnibox: **`www.tanktrouble.com`** rendered in near-black, **`/?forum`** in grey — Chrome's
  domain-emphasis rendering. `[OBSERVED]` **This is tanktrouble.com itself.** Against S110's clone
  warning: the host string is legible at 2× and unambiguous, there is no `tanktrouble.io` /
  `-unblocked` / school-proxy path segment, and the URL is the exact era route `?forum`
  (`index.php:12029` links `<a href="?forum">`). `[OBSERVED]` **Not a clone rehost.**
- Toolbar right: zoom magnifier `+`, bookmark star, then a **red octagon with a white hand and a
  small `1` badge** — an AdBlock/AdBlock Plus button reporting 1 blocked item — then the
  three-bar (pre-2018) Chrome menu. `[INFERRED]` this explains why both AdSense skyscraper slots
  are blank (see §"Layout" below); the ad markup at `index.php:12313-12320` (LEFT BANNER) and its
  RIGHT BANNER twin are present in the era-final source but produce nothing here.
- Window frame: blue Aero-style title bar with the Chrome profile-person icon, minimise, **restore**
  (so: maximised), close. Consistent with Chrome on Windows 7/8, mid-2010s.

**Page header** `[OBSERVED]`, transcribed verbatim:

> `Tank Owner's Forum`

This is **byte-identical to `srv/index.php:12041`**, inside
`<div class="text large" style="text-align: center; width: 100%; …">` at `:12040`. `[MEASURED]`
cap-height of the `T` = 17 capture px = **13.0 CSS px**, implying a font-size ≈ 18 CSS px for
`.text.large` (cap/em ≈ 0.72). Ink spans x 817…1059, centre **x = 938** — which is the centre of
the derived `#centerColumn` (493…1397, centre 945) to within 7 capture px. `[MEASURED]` the title
baseline sits 31 capture px (23.7 CSS) below the nav strip, consistent with the
`margin-bottom: 20px` on the menu table at `index.php:12025` plus half-leading.

**Nav tab strip** `[OBSERVED]` — left to right:

| Cell | Content | x (capture) | Width (CSS) | State |
|---|---|---|---|---|
| background | grey **maze-pattern texture** (`menuBackground.jpg`) | 0…480 and 1402…1886 | — | — |
| tab 1 | **`TANKTROUBLE.com`** chrome/silver 3-D wordmark on a light panel | 481…1000 | 396 | deselected |
| tab 2 | rolled **newspaper** with `NEWS` on it | 1001…1098 | 74 | deselected |
| tab 3 | **spanner / wrench** | 1100…1195 | 73 | deselected |
| tab 4 | **speech bubble** | 1196…1299 | **79** | **SELECTED** |
| tab 5 | **conical flask** with bubbles | 1300…1395 | 73 | deselected |

`[OBSERVED]` **There are five tabs. There is no shop tab.** The era-final strip at
`srv/index.php:12029` is six: `?game / ?news / ?garage / ?shop / ?forum / ?lab`. The 2015 order is
`game / news / garage / forum / lab` — the wrench tab sits *immediately* left of the selected
bubble tab, with only a `menuDeselectToSelect`-style rounded corner between them, so nothing is
hidden. `[INFERRED]` this is a genuine era difference, not a rendering artefact: the shop did not
exist yet — `index.php:7327-7332` dates *"Kickstarter Latecomers' Shop Opens"* to **18-07-2015**,
five months after this frame.

**Selected-state artwork** `[MEASURED]`:

- Deselected tab body: light grey with a top-down gradient, sampled down the centre of tab 3 —
  `#e6e6e6` (230) at y=70, `#e8e8e8` (232) at 85, `#dcdcdc` (220) at 100, `#c6c6c6` (198) at 104,
  ending at y=105. Bottom corners rounded (radius ≈ 8 capture px ≈ 6 CSS px). Between two
  deselected tabs there is a single 1–2 px dark vertical rule (x = 1000, 1099); between a
  deselected and the selected tab the deselected tab ends in a rounded corner and the strip goes
  white.
- Selected tab body: **`#ffffff` (255) at every sampled y from 63 to 105** — the tab has no body at
  all; it is the page background punched through the strip. The tab does **not** break the strip's
  top edge: the 7 px top highlight band (y 56…62, values 219→199) runs unbroken across it.
- Icon treatment: the deselected icons are **light-grey with a dark outline and a bevel/emboss**
  (newspaper bbox 63×35 capture = 48×27 CSS; wrench 71×34 = 54×26 CSS). The selected bubble icon is
  drawn in a **strong black outline with a soft drop shadow to the lower-left**, bbox 56×36
  capture = **43×27 CSS**. So "selected" = *lose the grey tab body, gain a black-ink icon*.
- Strip metrics `[MEASURED]`: grey band y 56…105 = 50 capture = **38.2 CSS px** tall; whole tab
  block x 480…1402 = 922 capture = **704 ± 5 CSS px**.

**Bearing on VE entry 10** (`tab5Select.jpg` ships **O?** on a timeline argument). This frame does
**not** upgrade it, and I want to be blunt about why:

- Entry 10 argues the strip is *"versioned as a set"* with the strip-wide change dated **20181218**,
  and ships the 2019-09 capture backwards into 2017–2018.
- This frame is Feb 2015 — i.e. *before* the 2015-03 CDX edge, on the **far side** of that change.
  It shows a **five-tab** strip; the era-final markup is six-tab. So it is direct proof that the
  strip was re-cut between 2015 and the era-final, but it says nothing about what
  `tab5Select.jpg` looked like in 2017–2018.
- What it *does* give: (a) the total tab-block width is **704 ± 5 CSS px in Feb 2015 vs the coded
  708 px** at `index.php:12028` — essentially unchanged across the redesign, so the shop tab was
  inserted by *shrinking the logo cell*, not by widening the strip; (b) the strip art was
  **38.2 CSS px tall in 2015 vs the 53 px table height** coded at `index.php:12025`, so the strip
  also got taller; (c) the *selected-state idiom* (white body + black-ink icon vs grey body +
  embossed grey icon) is documented for the first time, and is a reasonable prior for what the
  2018 art does even if the drawing changed.

**Everything above the fold, catalogued** (so absence claims later are trustworthy):

- Left column, x 85…244 (160 capture = **122 CSS px** wide): Scrapyard odometer → TankTrouble logo
  promo image → Kickstarter countdown box → Log In box → "Need Help? / Check the FAQ" → Visits box.
- Centre column, x 493…1397: title → three-bubble icon → 8 preview rows.
- Right column, x 1633…1792 (160 capture = 122 CSS): Victories (Top-10) → App Store badge →
  Google Play badge → Facebook Like + Share → Tell a Friend → Mod Activity → Got Feedback?.
- Between them, x 245…492 and 1398…1632 (≈188 and ≈179 CSS px): **empty**. `[INFERRED]` these are
  the 160 px + 20 px margin AdSense skyscraper slots (`index.php:12313-12320` and its RIGHT BANNER
  twin), blanked by the AdBlock extension visible in the toolbar.

---

#### 2. S57 vs S58 — which is this?

`[OBSERVED]` **This is the thread-preview list (S57), not a thread view (S58).** The decisive
evidence, in order of strength:

1. Every bubble ends with the grey affordance **`[click to open]`** — a thread has been *listed*,
   not opened.
2. Every bubble's metadata line ends with **`last post <n> ago`** or **`no posts yet`** — a
   per-thread reply summary, meaningless on an individual post.
3. Every bubble carries a **bold title line** above the body, i.e. the thread header.
4. Several rows carry **multiple tanks and multiple `&`-joined names** for a single bubble — a
   participant roster, not a single author.

`[MEASURED]` **8 rows are visible; the 8th is cut by the bottom of the frame.** Bubble top borders
at y = 228, 332, 420, 525, 631, 736, 860, 981. `x_showForumPreviews(1, 20, updateThread_cb)` at
`srv/index.php:12048` asks for 20; the rest are below the fold.

`[MEASURED]` The scrollbar thumb runs y 106…487 (382 capture px) and is **flush with the top of the
track** — the page is not scrolled. `[INFERRED]` with a track of ≈940–990 capture px the document
is ≈2.4–2.6 × the 799 CSS px viewport, i.e. ≈1900–2100 CSS px. At the measured mean row pitch of
**82.1 CSS px** (107.6 capture) that leaves room for ~12 more rows below the fold, for ~20 total —
**consistent with, though not proof of, the page size of 20 at `index.php:12048`.**

**Row anatomy** `[OBSERVED]`, uniform across all 8 rows:

```
[ tank 1 ][ tank 2 ][ tank 3 ]   ◄────pointer────  ┌─────────────────────────────┐
   (one 110×55 SWF per participant, left-aligned    │ Title                (bold, black, ~14px)
    at the centerColumn's left edge, slots          │ Body text… [click to open]  (14px black
    overlapping)                                    │                              + 10px grey)
                                                    │        participants, age - last post age
                                                    └──────────────── (12px grey, right-floated) ┘
```

- Tank cell is **left-aligned at the centre column's left edge (x ≈ 494 capture)** and grows
  rightwards with participant count; the bubble's left edge therefore moves right as participants
  are added, while its **right edge is pinned at x = 1389.8 capture for every row**.
- No avatar, no rank badge, no reply-count *number*, no thread-id, no category, no "sticky" marker,
  no unread dot. The reply count is expressed only as prose (`last post …` / `no posts yet`).

**Ordering** `[OBSERVED]` — this is a real, reproducible rule:

| # | Thread | Age | Last activity |
|---|---|---|---|
| 1 | wow | 40 minutes ago | last post **27 minutes** ago |
| 2 | how are you | 58 minutes ago | **no posts yet** (→ key = 58 min) |
| 3 | How to get the dog | 3 hours ago | last post **1 hour** ago |
| 4 | Challenge! | 5 hours ago | last post **1 hour** ago |
| 5 | when does online comes out? | 2 hours ago | last post **2 hours** ago |
| 6 | Random Discussion! | **34 weeks ago** | last post **2 hours** ago |
| 7 | KickStarter | 4 hours ago | last post **2 hours** ago |
| 8 | Hello | (cut off) | (cut off) |

`[OBSERVED]` The sequence 27 min → 58 min → 1 h → 1 h → 2 h → 2 h → 2 h is monotonically
non-decreasing, and row 6 — a **34-week-old** thread — sits sixth, between two 2-hour threads.
`[INFERRED]` **previews are ordered by `max(created, last_post)` descending, not by creation date.**
Falsifiable by any capture showing an older-last-post thread above a newer one.

---

#### 3. S58 — speech-bubble rendering

The want records a 9-slice bubble with alternating left/right pointers and three colour variants
(default, `.grayBubble` #cccccc, `.yellowBubble`), meaning of grey/yellow unknown, evidence pointer
`srv/includes/forumStyles.css`; `srv/index.php:12303-12307`. **`forumStyles.css` is not in the
staged tree, so I never read it** — I am testing the want's own summary against pixels.

**Fill colour — the answer nobody wants but the one the frame gives:**

`[MEASURED]` Interior modal colour of every bubble, sampled over the full inner rectangle,
counting only pixels with min channel > 235:

| Bubble | Thread | Modal interior | 2nd mode | pixels within ±25 of `#cccccc` | yellowish px |
|---|---|---|---|---|---|
| 1 | wow | `#fefefe` (19 043) | `#ffffff` (13 311) | 4.01 % | 0.02 % |
| 2 | how are you | `#ffffff` (21 541) | `#fefefe` | 3.54 % | 0.02 % |
| 3 | How to get the dog | `#ffffff` (28 521) | `#fefefe` | 3.75 % | 0.04 % |
| 4 | Challenge! | `#ffffff` (25 010) | `#fefefe` | 4.65 % | 0.04 % |
| 5 | when does online comes out? | `#ffffff` (27 742) | `#fefefe` | 2.67 % | 0.02 % |
| 6 | Random Discussion! | `#ffffff` (26 372) | `#fefefe` | 4.73 % | 0.05 % |
| 7 | KickStarter | `#ffffff` (25 593) | `#fdfdfc` | 4.84 % | 0.02 % |
| 8 | Hello | `#fefefe` (10 859) | `#ffffff` | 2.17 % | 0.03 % |

The 2.2–4.8 % "`#cccccc`-ish" fraction is **text anti-aliasing**, not fill: it tracks text density
across rows (row 6 has the most text and the highest count; row 8 is cut off and has the least).
The yellowish fraction is 0.02–0.05 %, i.e. JPEG chroma noise.

`[MEASURED]` **All eight bubbles are the default white variant. Neither `.grayBubble` nor
`.yellowBubble` appears in this frame. S58's colour-meaning question is not answered.**

**What the frame *permits* and what it *supports*, on grey/yellow semantics.** Candidate meanings,
each tested against what is here:

| Candidate | Test in this frame | Verdict |
|---|---|---|
| **yellow = thread starter's post** | every preview bubble *is* the thread starter's opening post, and all 8 are white | `[INFERRED]` **not supported for previews.** It survives only if the variants are thread-view-only. Weak evidence, but it is evidence. |
| **grey/yellow = moderator** | row 6 (`ben314`, "Random Discussion!", 34 weeks old, worded exactly like a pinned staff thread, poster's tank wears a **gold sheriff star**) is white | `[UNCERTAIN]` — suggestive against, but `ben314` is not in the Mod Activity box and the sheriff star is buyable swag, so this is not a mod identification |
| **grey/yellow = the logged-in user's own post** | the session is **logged out** (login form present, §6) — no own posts exist | untestable here; **fully consistent** |
| **grey = disabled/deleted post** (S64's `setDisable` / `setDelete`) | none of the 8 threads shows deletion markers | untestable here; **fully consistent** |
| **grey/yellow = read/unread** | logged out ⇒ everything default | untestable here; **fully consistent** |

`[OBSERVED]` One structural fact from the code does bear on this and is worth recording:
`updatePost_cb` at `srv/index.php:12141-12146` sets `className` on **two** elements — the post
bubble *and* a separately-identified `threadBubbleId` — and `updateModeratedPost_cb` at
`:12175-12176` does the same for the thread bubble alone. `[INFERRED]` the colour classes therefore
apply to **thread-level bubbles too, not only to reply bubbles**, so preview bubbles are eligible
for grey/yellow and their being uniformly white here is a real (if weak) datum rather than a
category error.

**Pointer — measured on all eight, and it is fixed art:**

| Bubble | Bubble left border (capture x) | Pointer apex x | Apex − border | Apex y − bubble top |
|---|---|---|---|---|
| 1 | 787.8 | 720 | 68 | 28 |
| 2 | 715.9 | 648 | 68 | 27 |
| 3 | 638.8 | 570 | 69 | 28 |
| 4 | 638.8 | 571 | 68 | 27 |
| 5 | 638.8 | 571 | 68 | 27 |
| 6 | 638.8 | 570 | 69 | 29 |
| 7 | 787.8 | 720 | 68 | 27 |
| 8 | 638.8 | 570 | 69 | 29 |

`[MEASURED]` Pointer horizontal reach **68.4 ± 0.5 capture px = 52.2 ± 0.4 CSS px**; apex sits
**27.8 ± 0.9 capture px = 21.2 ± 0.7 CSS px** below the bubble's top border. Identical across
bubbles that differ in height by 37 capture px and in width by 149 capture px → `[INFERRED]`
**the pointer is fixed corner art (a 9-slice corner tile), not stretched.**

`[MEASURED]` Pointer shape (traced on bubble 3): the **upper** edge is a straight diagonal from
(642, 421) — just below the bubble's top-left corner — down-left to the apex at (571, 447):
Δx 71, Δy 26, slope ≈ 0.37, i.e. **≈20° below horizontal**. The **lower** edge returns from the
apex almost horizontally (y 448→450) to the bubble's left border at x ≈ 640. So it is a **thin
wedge with its tip at the bottom-left**, not a symmetric triangle. The bubble's own left border
begins *below* the wedge (first clean vertical run at y ≈ 451).

`[OBSERVED]` **All eight pointers are on the left**, and every tank cluster is on the left of its
bubble. There is no ink at all between the bubble right border (x 1389.8) and the centre column's
right edge. `[INFERRED]` **the preview list does not alternate sides.** This is consistent with —
and sharpens — the code: alternation is carried by an explicit per-post argument, `leftSide`, in
`x_edit(forumId, replyId, text, leftSide, updatePost_cb)` at `srv/index.php:12285`. Alternation is
a **thread-view** property. The want's phrase "left/right pointers alternating" should be scoped
to S58/thread view and removed from any S57 preview reconstruction.

**Border, corners, shadow:**

- `[MEASURED]` Border darkest samples along long straight runs: `#414141` (65) on bubble 6's bottom
  edge, `#565656` (86–92) elsewhere, spread over 2 capture px. `[INFERRED]` at a 1.31× resampling a
  1 CSS px line's darkest output pixel retains ~76 % of the ink, so the true border is
  **≈ #000000–#333333, 1–1.5 CSS px wide**; video compression prevents pinning it tighter.
- `[MEASURED]` Corner arcs: top-right of bubble 4 — horizontal border ends x = 1386 (y = 526),
  vertical border starts y = 530 (x = 1389–1391) → arc ≈ 6 × 5 capture px. Bottom-left — vertical
  ends y = 618, horizontal starts x = 642 (y = 621) → arc ≈ 4 × 4. `[INFERRED]` **corner radius
  ≈ 3–4.6 CSS px.**
- `[MEASURED]` Shadow, asymmetry test on bubble 6: **above** the top border y 849 = 255, 848 = 251
  (clean); **below** the bottom border y 853…856 = 211, 227, 237, 248. **Left** of the right border
  x 1387 = 251; **right** x 1391…1396 = 129, 169, 189, 215, 235, 248. `[MEASURED]` **soft drop
  shadow offset down-and-right, decaying over 4–5 capture px = 3–4 CSS px.**

**The bubble really is a table** `[INFERRED]`: `srv/index.php:12158` addresses the bubble as
`document.getElementById(bubbleId).rows[1].cells[1]` — row 1, cell 1 of a table, i.e. the centre
of a 3×3. The frame shows eight bubbles of five different heights and three different widths with
pixel-identical corner and pointer art — exactly the 3×3 nine-slice that markup implies. Confirmed.

**Vertical size model** `[MEASURED]`, from bubble heights and their line counts:

| Bubble | Lines (title / body / click / meta) | Height (capture) | Height (CSS) |
|---|---|---|---|
| 2 | 1 / 1 / 0 / 1 | 80 | 61.1 |
| 1 | 1 / 1 / 0 / 2 | 97 | 74.0 |
| 3 | 1 / 2 / 0 / 1 | 98 | 74.8 |
| 5 | 1 / 1 / 1 / 1 | 98 | 74.8 |
| 4 | 1 / 2 / 0 / 1 | 99 | 75.6 |
| 7 | 1 / 2 / 0 / 2 | 114 | 87.0 |
| 6 | 1 / 2 / 1 / 1 | 117 | 89.3 |

`[MEASURED]` title/body line-height **18 capture = 13.7 CSS px**; metadata line-height
**16 capture = 12.2 CSS px** (from the two two-line metadata blocks, bubbles 1 and 7).
`[INFERRED]` **fixed vertical overhead of the bubble (top + bottom slices + padding) ≈ 21–22 CSS px**,
fitting all seven measured heights to ±1.5 px.

`[MEASURED]` Horizontal: text inset from the border centre **11.5–12.5 capture = 8.8–9.5 CSS px**
on the left (measured on bubbles 1, 4, 7) and **13 capture ≈ 10 CSS px** on the right. Inter-row
gap (bubble bottom border → next bubble top border) is **exactly 8 capture px = 6.1 CSS px in all
seven gaps**.

**Typography inside the bubble** `[MEASURED]` (bubble 4/5, band-profile method):

| Element | Colour | Cap / x-height (capture) | Implied CSS font-size | Likely class |
|---|---|---|---|---|
| Thread title | black, **bold**, darkest px `#000000` | cap 13 | ≈ 14 | `text normal` bold |
| Body | black, regular, darkest px `#050709` | cap 13, x-height 10 | ≈ 14 | `text normal` |
| `[click to open]` | grey, darkest px `#737373` | x-height **7** (0.70 × body) | ≈ 10 | `text tiny gray` |
| Participants + times | grey, darkest px `#7d7c7f` | cap 11 (0.85 × body) | ≈ 12 | `text small gray` |
| Page title (outside bubble) | black | cap 17 | ≈ 18 | `text large` |

`[INFERRED]` three sizes inside the bubble — 14 / 12 / 10 — which map cleanly onto the site's
`text normal` / `text small` / `text tiny` ladder used throughout `index.php`
(`class="content text small gray"` at `:13046`, `class="content text tiny gray"` at `:12975`).
`[UNCERTAIN]` the exact grey: measured darkest ink is `#737373`/`#7d7c7f`, but thin AA'd strokes at
1.31× never reach the true value, so the ink is somewhere in **#444444–#7d7d7d**. `#666666` — the
value `index.php:12437-12438` uses for the login placeholders — sits inside that band and is the
most economical candidate, but the frame cannot prove it.

**Metadata alignment — a subtle finding worth the ink** `[MEASURED]`:

- Single-line metadata is flush **right**: bubble 2 ends at x = 1376, bubble 3 at 1376, bubble 4 at
  1376 — i.e. at the right text inset.
- Two-line metadata is flush **left**: bubble 1 line 1 spans 800…1313 and line 2 ("minutes ago")
  starts at **800**, the left text inset; bubble 7 line 1 spans 800…1349 and line 2 starts at 800.

`[INFERRED]` a `text-align: right` block would right-align *both* lines. A **shrink-to-fit
right-floated element** (or `display:table; margin-left:auto`) does exactly what is drawn: it hugs
its content and floats right while the content fits, and once the content exceeds the available
width the box fills the container and its text wraps left-aligned. **Falsifiable** by any capture
where a wrapped metadata block's second line is right-aligned.

---

#### 4. S59 — per-post tank render and scale

The want: *"`forumTank-<name>` embeds tank SWF at `110×scale` — scale varies per user
(rank-linked?)"*, `srv/index.php:12071-12082`. The code reads
`var width = 110 * parseFloat(currentElement.getAttribute('scale'));` at `:12073` and
`var height = 55 * …` at `:12074`.

**Every tank sprite in the frame, measured.** Bounding boxes are of the *drawn sprite* (the SWF is
`wmode=transparent` with no visible frame), found by thresholding non-white pixels:

| Row | Participant (positional) | Sprite bbox x (capture) | w | Sprite bbox y | h (capture) | h (CSS) |
|---|---|---|---|---|---|---|
| 1 | bro123456789102 | 466…566 | 101 | 235…296 | 62 | 47.3 |
| 1 | 32572 | 566…641 | 76 | 233…294 | 62 | 47.3 |
| 1 | y346 | 641…709 | 69 | 237…293 | 57 | 43.5 |
| 2 | miil | 482…561 | 80 | 349…400 | 52 | 39.7 |
| 2 | jklg | 566…639 | 74 | 341…397 | 57 | 43.5 |
| 3 | FH1111 | 477…561 | 85 | 426…487 | 62 | 47.3 |
| 4 | VIDthekiller | 472…561 | 90 | 528…600 | **73** | **55.7** |
| 5 | Kiler21 | 466…561 | 96 | 646…698 | 53 | 40.5 |
| 6 | ben314 | 482…561 | 80 | 757…812 | 56 | 42.7 |
| 7 | NintendoMAERSK | 473…566 | 94 | 863…934 | **72** | **55.0** |
| 7 | MAERSKMario | 566…641 | 76 | 865…931 | 67 | 51.1 |
| 7 | LuigiMAERSK | 641…709 | 69 | 868…930 | 63 | 48.1 |
| 8 | Kiler21 (2nd thread) | 466…561 | 96 | 997…1045 | 49 (clipped) | — |

`[MEASURED]` **The two tallest sprites measure 55.7 and 55.0 CSS px.** That is exactly
`55 × scale` with **`scale = 1`** (`index.php:12074`). No sprite exceeds it. No sprite is below
72 % of it. `[INFERRED]` **all twelve users in this frame render at scale ≈ 1**; the spread in the
table is accessory height, not scale (Kiler21's flat red tank vs VIDthekiller's dog-accessory
stack). Two independent checks: rows 5 and 8 are the same user (`Kiler21`) two threads apart and
measure **identically, 466…561** — so the measurement is repeatable; and the raw bboxes never
exceed the 110 CSS px (144 capture) box width either (max 101).

**The far stronger measurement — cell width, which is scale-driven and accessory-immune:**

`[MEASURED]` the bubble's left border, sub-pixel located by intensity-weighted centroid:

| Participants | Rows | Bubble left border (capture x) | Δ from previous |
|---|---|---|---|
| 1 | 3 (FH1111), 4 (VIDthekiller), 5 (Kiler21), 6 (ben314), 8 (Kiler21) | **638.8, 638.8, 638.8, 638.8, 638.8** | — |
| 2 | 2 (miil & jklg) | **715.9** | +77.1 capture = **+58.9 CSS** |
| 3 | 1, 7 | **787.8, 787.8** | +71.9 capture = **+54.9 CSS** |

This is the S59 result:

1. `[MEASURED]` **Five different single-participant posters produce a tank cell of identical width
   to 0.1 capture px.** If `scale` were rank-linked and these five users had different ranks, the
   cell width would differ. **They do not.** This is the first direct empirical constraint ever
   placed on the varying-scale claim, and it points at *constant*.
2. `[MEASURED]` Each extra participant widens the cell by **55–59 CSS px** — roughly **half** the
   110 CSS px SWF width at `index.php:12073`.
3. `[INFERRED]` Combining (2) with the cell's left edge: for n = 1, 2, 3 the cell's *left* edge lands
   at capture x 494.1, 496.9 and 494.2 — i.e. **the tank cell is left-aligned at the centre
   column's left edge (derived 493)** and grows rightwards. That is a three-way consistency check
   on a ≈74.5 capture px per-tank advance and it holds to ±3 px.
4. `[INFERRED]` Since each SWF is 110 CSS px wide but each slot advances only ≈57 CSS px, **adjacent
   `forumTank-<name>` boxes overlap by ≈53 CSS px** (equivalently: a ≈57 px container with the
   110 px object overflowing, or a `margin-left: -53px`). This is visible directly — the three-tank
   clusters in rows 1 and 7 are contiguous with no gap, and sprite hulls abut. **This constant did
   not previously exist anywhere in the reconstruction.**
5. `[MEASURED]` **Vertical placement:** every sprite's top edge sits 3…21 capture px *below* its
   bubble's top border, and every sprite's bottom sits 64…76 capture px below it — i.e. within the
   72 capture px (= 55 CSS px) box height. `[INFERRED]` **the tank SWF box is top-aligned with the
   bubble's top border**, and the tank is bottom-anchored inside it.
6. `[MEASURED]` The tank sprites' **right edge is x = 561 for all five single-participant rows**
   despite completely different accessories. `[INFERRED]` the tank in `loggedInTank06.swf` has a
   **fixed anchor** — barrel pointing right at a fixed x — so all thirteen tanks are in the *same*
   pose, and the bbox differences really are accessory-driven, not heading-driven.

**Colour and accessories, tank by tank** `[OBSERVED]` (descriptions only — I am not claiming to
identify catalogue items):

- **Row 1 / bro123456789102** — dark indigo-purple hull with white "shark teeth" painted on the
  flank; green spiked barrel; a red-and-orange **flame/feather plume** at the barrel root; a curved
  red horn accessory at the rear.
- **Row 1 / 32572** — magenta/pink hull with darker pink treads, purple barrel, a **brown
  cowboy/leather hat** on the deck, a **red-and-blue balloon** at the muzzle.
- **Row 1 / y346** — pink hull, purple barrel, red-and-blue balloon, a **yellow smiley-face badge**
  on the flank, silver muzzle brake.
- **Row 2 / miil** — khaki/olive hull with dark port holes, khaki barrel, a **red-and-white spotted
  mushroom** on the barrel and a **white star** at the muzzle.
- **Row 2 / jklg** — deep purple hull, red crest/mohawk, a **black top hat (or chimney)**, orange-brown
  barrel ending in a ring.
- **Row 3 / FH1111** — gold/olive hull; **carved jack-o'-lantern** turret glowing orange with a
  grinning face; **black bat wings** behind it; barrel glowing green-to-cyan with a dripping
  effect; a white **skeletal hand** at the lower right. A full Halloween loadout.
- **Row 4 / VIDthekiller** — periwinkle-purple hull, red scarf/cape, a large purple **dog** figure
  standing over the tank, a **yellow bone**, an olive barrel, and a grey plaque above the tank
  carrying characters I read as `…1O1P1…` `[UNCERTAIN]` — too small and too compressed to
  transcribe.
- **Row 5 & 8 / Kiler21** — bright red hull with white shark-teeth, a red horn at the rear, a
  red-orange-yellow **flame plume**, olive barrel with a white/silver **star muzzle**.
- **Row 6 / ben314** — solid **black** hull (no visible grille), **ice-blue / chrome** turret and
  barrel, a small **gingerbread man** figure on the deck, and a large **gold six-pointed sheriff
  star** at the front.
- **Row 7 / NintendoMAERSK, MAERSKMario, LuigiMAERSK** — three near-identical rigs: purple **dog**
  accessory (same as VIDthekiller's), a bone, and painted hulls in orange, yellow-green and green
  respectively, each with a **text banner** above the dog's head. I can read `…feel` on the second
  and something ending `…NUTS` on the third `[UNCERTAIN]`; the first is illegible.

`[INFERRED]` the three MAERSK accounts share a rig and post together; likewise VIDthekiller's dog
matches theirs. This is presumably why thread 3 asks *"How to get the dog"* — the accessory was
current and desirable in Feb 2015. It does **not** tell us whether the dog is rank-gated.

**Bottom line on S59:** the *sizes* question is answered as far as one frame can answer it —
`scale = 1` for these twelve users, cell advance 57 CSS px, box top-aligned to the bubble. Whether
`scale` varies for *other* users (higher ranks, staff) is still open, because this frame is
logged-out and shows twelve ordinary accounts from one day.

---

#### 5. Post anatomy — full transcription

Verbatim, including typos, spacing and casing. Ambiguous glyphs flagged.

**Row 1** — bubble x 787.8…1389.8, y 228…324
- Title: `wow`
- Body: `this is awesome!!!!1` + grey `[click to open]`
- Meta (2 lines, left-aligned): `bro123456789102 & 32572 & y346, 40 minutes ago - last post 27 minutes ago`
- Tanks: 3

**Row 2** — bubble 715.9…1389.8, y 332…411
- Title: `how are you`
- Body: `do you want to challange me` + `[click to open]` *(sic — "challange")*
- Meta (1 line, right-aligned): `miil & jklg, 58 minutes ago - no posts yet`
  `[UNCERTAIN]` glyphs: `miil` — chars 2 and 3 carry tittles (i), char 4 has none and is
  full-height (l); read at 6× the string is `m-i-i-l`. `jklg` is unambiguous.
- Tanks: 2

**Row 3** — bubble 638.8…1389.8, y 420…517
- Title: `How to get the dog`
- Body: `i mean if i want to get the dog stand nare by i need to finish which code?` + `[click to open]`
- Meta: `FH1111, 3 hours ago - last post 1 hour ago`
- Tanks: 1

**Row 4** — bubble 638.8…1389.8, y 525…623
- Title: `Challenge!`
- Body: `I think this battle is fair: WARMACHINE2014 vs VIDthekiller.Vote for who you think is gonna win when online comes out!` + `[click to open]` *(sic — no space after the full stop)*
- Meta: `VIDthekiller, 5 hours ago - last post 1 hour ago`
- Tanks: 1

**Row 5** — bubble 638.8…1389.8, y 631…728
- Title: `when does online comes out?`
- Body: `when?` then a **line break**, then `[click to open]` on its own line
- Meta: `Kiler21, 2 hours ago - last post 2 hours ago`
- Tanks: 1

**Row 6** — bubble 638.8…1389.8, y 736…852
- Title: `Random Discussion!`
- Body: `If you want to have a discussion with a friend, talk about how your day went, or anything else as long as it's appropriate to our forums, go ahead and post it here!` then a **line break**, then `[click to open]`
- Meta: `ben314, 34 weeks ago - last post 2 hours ago`
- Tanks: 1

**Row 7** — bubble 787.8…1389.8, y 860…973
- Title: `KickStarter` *(note the internal capital S)*
- Body: `What type "items" do you guys think will be in the crate?` + `[click to open]`
- Meta (2 lines, left-aligned): `NintendoMAERSK & MAERSKMario & LuigiMAERSK, 4 hours ago - last post 2 hours ago`
- Tanks: 3

**Row 8** — bubble 638.8…1389.8, y 981…(cut)
- Title: `Hello`
- Body: `Can someone tell me how to play online` then a **line break**, then `plz` + `[click to open]`
- Meta: `[NOT VISIBLE]` — below the frame edge
- Tanks: 1 (same rig as row 5 → Kiler21)

**Where the author names sit** `[OBSERVED]`: **not** next to the tank, and **not** above the body.
They are the first element of the **metadata line at the bottom of the bubble**, `&`-joined,
followed by `, <thread age> ago - last post <age> ago` (or `- no posts yet`). Same 12 CSS px grey
as the timestamps — **no separate colour, weight or link treatment for the username**. The tanks
carry no name label at all.

**Participant order** `[INFERRED]`: the tank count equals the name count in every row (3/3, 2/2,
1/1 ×5, 3/3), and they are laid out left-to-right in the same order as the `&`-joined list.
Falsifiable by any capture where counts diverge.

**The anomaly that must be recorded** `[OBSERVED]`: row 2 reads
`miil & jklg, 58 minutes ago - no posts yet` — **two participants, two tanks, and no posts.**
A "starter + repliers" roster cannot produce this. Candidate explanations:

- (a) The roster is retained but the post was **deleted or disabled** — S64's `setDelete` /
  `setDisable` endpoints (`srv/index.php:12167-12185`) would plausibly clear the last-post summary
  while leaving the author in the thread's user set. This is the explanation I'd bet on, and it
  would be *indirect* evidence that S64's moderation actions were in live use.
- (b) The `no posts yet` branch is keyed on a different counter from the roster — an original bug.
- (c) Some now-unknown "addressed to" mechanic (the body is `do you want to challange me`).

`[UNCERTAIN]` — the frame cannot decide, and any faithful reimplementation of
`x_showForumPreviews` must be able to produce this state.

**Per-post controls** `[NOT VISIBLE]`. There is no edit pencil, no reply arrow, no delete/ban/close
icon, no hover trail, no cursor anywhere in the centre column. I verified this by masking out every
identified bubble, pointer, tank cluster and the header icon, then scanning the remaining centre
column (x 450…1420, y 120…1047) for any pixel below 240 — the only residue is bubble-border and
pointer edge pixels 1–2 px outside my masks. **S64 gains nothing.** Note the session is logged out,
so absence here is weak evidence about what a moderator would see.

---

#### 6. S61 / S62 — new-thread and reply forms

`[NOT VISIBLE]`.

- No `forumthreadheader` input, no `Discussion header` placeholder, no `forumthreadtextarea`
  (`srv/index.php:12189-12191`).
- No `forumcommenttextarea`, no `forumcommenterror` (`srv/index.php:12246, :12250`).
- No submit button, no error strip, anywhere in the visible page.

`[INFERRED]` the reason is straightforward and should be recorded as a *behavioural* finding rather
than a null: **the session is logged out.** The left sidebar shows the login form with the
untouched `username` / `password` defaults (§ below). A logged-out visitor gets neither composer.
This means the frame is evidence that **the composer is gated on login and is not rendered at all
for anonymous visitors** — which is more than nothing, but it does not describe the form.

S61 and S62 stay `WANTED`.

---

#### 7. S65 thread filter and S66 pagination

**The one candidate control in the frame** `[OBSERVED]`: an icon at capture x 1319…1394,
y 175…216 — **58 × 32 CSS px** — sitting between the page title and the first preview row, and
**right-aligned to the centre column's right edge** (its right edge x = 1394 vs the derived column
edge 1397; the bubbles stop at 1389.8).

`[OBSERVED]` It is **three overlapping speech bubbles** drawn in black outline with white fill
(dark cluster bbox 1320…1365 × 176…212 = 35 × 28 CSS px), with a **light-grey right-pointing arrow**
behind and to their right, fill sampled at `#d3d3d3` (211, 211, 211).

`[UNCERTAIN]` — its function. Candidates, with the argument for and against each:

| Reading | For | Against |
|---|---|---|
| **Next page of discussions (S66)** | the arrow is directional and points right; the list is newest-first so "→" reads as *older*; there is **no mirrored control on the left**, exactly what page 1 of a paged list looks like; `firstPreview`/`lastPreview` at `:12241` and `:12263` prove paging exists | a next-page control at the *top* of a list is unusual (bottom is conventional) — but the bottom of the page is off-frame, so a second control there is not excluded |
| **Start a new discussion (S61)** | the new-thread form must be reachable from somewhere, and this is the only control on the page; three-bubbles = "discussions" | the session is **logged out**, and a logged-out user cannot start a thread — yet the control is shown; the arrow reads as navigation, not composition |
| **Decorative masthead** | `?news` uses a themed masthead graphic | the grey arrow is an affordance, not ornament |

I lean to **pagination/navigation** on the directional-arrow argument, but I will not assert it.
`[NOT VISIBLE]` for everything else: no dropdown, no `<select>`, no tab row, no page-number strip,
no "all / unanswered / mine" control anywhere above the list. The `'all'` literal at
`srv/index.php:12241` and `:12263` still has **no recovered UI**.

**S65 stays `WANTED`. S66 moves to `PARTIAL` at best** — one 58×32 CSS px icon of *possible*
pagination, plus the indirect page-length arithmetic in §2 supporting a 20-row page.

The bottom of the page — where a conventional pager would live — is **below the frame edge**
(the capture stops mid-row-8 at y = 1047). There is no footer and no copyright line in view.

---

#### 8. Dating — and why this frame is outside the target window

`[MEASURED]` **Kickstarter countdown box** (left sidebar, x 85…244, y 338…720), transcribed
verbatim top to bottom:

> `KICK` (black) `STARTER` (Kickstarter-green)
> `launches in`
> `2` / `days`
> `10` / `hours`
> `43` / `minutes`
> `0` / `seconds`
> `Read more...`

Cross-referenced against `srv/index.php`, this pins the date almost to the hour:

- `index.php:7736-7739` — news item **`Kickstarter Countdown Has Started`, 16-02-2015**: *"The
  countdown has already begun and we are getting all our dogs in a row for the grand launch this
  Friday."*
- `index.php:7689-7695` — **`TankTrouble Kickstarter Approved - Countdown Resumes`, 21-02-2015**:
  *"our original countdown turned out to be faster than Kickstarter's approval time. Hence, we had
  to put the countdown on hold."*
- `index.php:7669-7672` — **`TankTrouble Kickstarter Launched`, 23-02-2015**.

`[INFERRED]` **The frame was captured 2 days 10 hours 43 minutes before a Kickstarter launch
target, therefore between 17-02-2015 and 21-02-2015** (either the first countdown, aimed at Friday
20-02, or the resumed one aimed at 23-02). **Confidence: high.** Falsifiable only by a second,
earlier or later Kickstarter countdown that I am unaware of.

Five independent corroborations, all pointing the same way:

1. `[OBSERVED]` **No shop tab in the nav strip.** The shop opened 18-07-2015
   (`index.php:7327-7332`). A Feb-2015 page cannot have it. **Strong.**
2. `[OBSERVED]` **Thread 7 is titled `KickStarter`** and asks *"What type "items" do you guys think
   will be in the crate?"* — the reward crate, discussed in the days before launch. **Strong.**
3. `[OBSERVED]` Threads 5 and 8 ask *"when does online comes out?"* and *"how to play online"*, and
   thread 4 says *"when online comes out"*. Online BETA opened **10-07-2015**
   (`index.php:7373-7381`). The frame therefore predates July 2015. **Strong.**
4. `[MEASURED]` **Visits counter reads `30730115`** (`Since 2007-12-16` / `Today: 5090` /
   `Online: 964`). The era-final served value is **68374157** (`index.php:12930`, the forum route's
   copy; the game route at `:1069` holds 68466319). A counter at 45 % of its Dec-2018 value is
   emphatically not 2017–2018. **Strong.**
5. `[MEASURED]` **Scrapyard odometer reads ten digits: `1152966 49…`** with the last wheel mid-roll,
   i.e. ≈ **1.153 billion**. `index.php:8083-8085` dates *"1.000.000.000 Tanks Destroyed!"* to
   **10-11-2014**, followed by *"Scrapyard Duct Taped"* (24-11-2014) and *"Destruction Too Fast for
   Scrapyard"* (28-11-2014) — the widening from nine to ten wheels. 153 M scraps in the ~14 weeks
   since is ≈1.5 M/day, which is the right order. **Moderate, and it rules out pre-Nov-2014.**

**Signals that do *not* date the frame, stated so nobody over-reads them:**

- `[OBSERVED]` The **old "Available on the App Store"** badge (black, with the phone glyph) is
  present. Apple replaced this artwork with "Download on the App Store" in ~Sept 2016 — **but
  TankTrouble never updated it**: the era-final markup still serves
  `images/availableOnTheAppStore120.jpg` at `index.php:13025`. So the badge gives only a *lower*
  bound (after the iOS app existed) and no upper bound at all.
- `[OBSERVED]` No seasonal skin, no Christmas box, no Halloween decoration on the page chrome (only
  on individual users' tanks, which persist year-round). Consistent with February; not probative.

**Clone check (S110)** `[OBSERVED]`: omnibox `www.tanktrouble.com/?forum`; page title begins
`TANK TROUBLE Tan…`; the Facebook widget points at `facebook.com/TankTrouble`; the Mod Activity,
Scrapyard, Victories and Visits boxes are all live with plausible values; the `Since 2007-12-16`
epoch matches `index.php:12929`. **This is the real site.** No clone indicators.

**Verdict on era:** **outside the 2017–2018 target window by roughly 2½–3½ years.** Everything in
this document must be read as *"the forum as it stood in Feb 2015"*, and any of it that gets used
in the rebuild must be logged as an era-extrapolation, not as era evidence.

---

#### 9. Other page furniture confirmed by this frame

These are not my topic, but they are era-checkable facts sitting in the same pixels and they are
cheap to record.

- `[OBSERVED]` **Mod Activity box** (right column, y 517…?): header `Mod Activity` in grey, then
  three name/time pairs — `bbc` / `3 hours ago`, `revengexx1` / `3 hours ago`, `Dalek-Buster` /
  `3 hours ago` — name in a larger grey face, time in a smaller one. `[OBSERVED]` this exactly
  reproduces `srv/index.php:13044-13049`, where the block is
  `<div class="content text small gray">purup<br><span class="text tiny">54 minutes ago</span><br>…`
  with three entries. **Note: `Mod Activity` occurs exactly once in the whole 812 KB
  `index.php`, at line 13045 — it is a forum-route-only box**, and this frame confirms it renders
  on `?forum`. Bears on **S105** (frozen live regions): the *shape* and entry count are era-stable
  from 2015 to 2018.
- `[OBSERVED]` **Victories box**: header `Victories` (matching `top10WeeklyHeader` at
  `index.php:12973`), ten rows — `NooBPlay 1190`, `fivip123456 1036`, `TAJMIR 777`,
  `rapzkiemalupet 764`, `james_45 740`, `Quickbullet 721`, `Jasmine7 703`, `2020dan 665`,
  `monkeyquest456 662`, `teekaw 642` — and two bottom tabs, **`Weekly` bold/black (selected)** and
  **`Friends` grey on a raised tab (deselected)**, matching `bottom2Tabs tab1Selected` at
  `index.php:12975-12977`. `[MEASURED]` row pitch 13.7 capture = 10.5 CSS px, i.e. ten rows in the
  coded `height: 110px` content div. This is the selected/deselected idiom **S3** needs half of.
- `[MEASURED]` **Login box** (`index.php:12420-12442`): header `Log In`; a small **`?`** at the
  header's **top-left** — exactly the `position: absolute; top: 4px; left: 6px` link to
  `/infirmary/` at `:12433-12434`; a text input showing grey `username`
  (`value="username"`, `color: #666666`, `:12437`); a password input showing **exactly 8 bullets**,
  measured as 8 discrete dark blobs at y = 818, x-runs (98-100)(104-106)(110-113)(116-119)
  (123-125)(129-132)(135-138)(142-145) — i.e. `value="password"`, 8 characters, `:12438`; a
  `Log in` button and a plain `Sign up` link (`:12440-12441`). **Every one of those markup details
  is confirmed visually.**
- `[OBSERVED]` **Got Feedback? box, closed state**: `Got ideas?` / `Found Bugs?` / `Urge to praise
  us to the skies?` / `Then give us your feedback` over an **envelope-going-into-a-slot** graphic —
  byte-identical copy to `index.php:13054-13058`, and the graphic is `envelope.jpg` at its coded
  72×29. **S11** wants the *open* state; this is the closed one, which was already known, but it
  does confirm the copy has been unchanged since Feb 2015.
- `[MEASURED]` **The countdown widget is the same code.** `srv/index.php:12394-12399` codes
  `numberSize = [56, 32, 20, 14]`, `numberLineHeight = [40, 24, 16, 12]`, `labelSize = [24,20,16,14]`,
  `font-family: Courier; font-weight: bold`, and the string `"launch in"`. In the frame: the labels
  `days` / `hours` / `minutes` / `seconds` are unmistakably **monospaced with slab serifs**
  (Courier), and the four digit tiers measure **47 / 28 / 18 / 13 capture px** tall. Normalised to
  the coded 56 px top tier that is a font-size ladder of **56 / 33.4 / 21.5 / 15.5** against the
  coded **56 / 32 / 20 / 14** — agreement within 1.5 px at every tier.
  `[OBSERVED]` **But the leading string is `launches in`, where the era-final code emits
  `launch in`** (`:12398`). So the same widget, with the string changed between Feb 2015 (counting
  down to the Kickstarter) and the era-final (counting down to `1475758800000` = 2016-10-06,
  under a red `PLAY ONLINE` box). Worth a DECISIONS note if that widget is ever rebuilt.
- `[OBSERVED]` **Right-column order in Feb 2015**: Victories → App Store → Google Play →
  Like + Share → Tell a Friend → Mod Activity → Got Feedback?. The era-final forum route
  (`index.php:13022-13051`) is Victories → **Like** → App Store → Google Play → Tell a Friend →
  Mod Activity → Got Feedback?. The Facebook widget moved from *above* the badges to *below* them
  at some point after Feb 2015. Minor, but it is a real difference and I would rather log it than
  let a future reader treat this frame as an era-final layout reference.
- `[MEASURED]` Facebook widget renders as two buttons, `Like` and `Share`, total 124 × 26 capture
  px = 95 × 19.8 CSS — i.e. the 20 px "small button" layout, consistent with
  `data-layout="button" … data-share="true"` at `index.php:13022`.

---

#### Measurements — consolidated table

All CSS values = capture ÷ 1.31.

| Quantity | Capture px | CSS px | How obtained |
|---|---|---|---|
| Page→capture scale factor | — | — | 4 anchors, §0; **1.31 ± 0.01** |
| Bubble right border (all rows) | x 1389.8 | — | intensity centroid |
| Bubble left border, 1 participant | x 638.8 (×5 rows) | — | intensity centroid |
| Bubble left border, 2 participants | x 715.9 | — | " |
| Bubble left border, 3 participants | x 787.8 (×2 rows) | — | " |
| Bubble width, 1 / 2 / 3 participants | 751.0 / 673.9 / 602.0 | **573.3 / 514.4 / 459.5** | derived |
| Per-extra-participant advance | 77.1 and 71.9 | **58.9 and 54.9** | derived |
| Pointer horizontal reach | 68.4 ± 0.5 | **52.2 ± 0.4** | 8 rows |
| Pointer apex offset below bubble top | 27.8 ± 0.9 | **21.2 ± 0.7** | 8 rows |
| Pointer upper-edge slope | Δx 71 / Δy 26 | ≈20° | traced, bubble 3 |
| Bubble corner radius | 4–6 | **3–4.6** | arc spans, bubble 4 |
| Bubble border width | ~2 (spread) | **1–1.5** | darkest `#414141` |
| Bubble drop shadow reach (down/right) | 4–5 | **3–4** | asymmetry test, bubble 6 |
| Bubble fixed vertical overhead | ~28 | **21–22** | 7-height regression |
| Title / body line-height | 18 | **13.7** | consecutive body lines |
| Metadata line-height | 16 | **12.2** | 2-line metas, bubbles 1 & 7 |
| Text inset from border, left / right | 11.5–12.5 / 13 | **8.8–9.5 / ~10** | bubbles 1, 4, 7 |
| Inter-row gap | 8 (all 7 gaps) | **6.1** | border-to-border |
| Mean row pitch | 107.6 | **82.1** | 8 bubble tops |
| Title / body font-size | cap 13 | **≈14** | cap-height ÷ 0.72 |
| Metadata font-size | cap 11 | **≈12** | " |
| `[click to open]` font-size | x-height 7 | **≈10** | x-height ratio 0.70 |
| Page title font-size | cap 17 | **≈18** | " |
| Tallest tank sprite | 73 / 72 | **55.7 / 55.0** | = `55 × scale`, scale = 1 |
| Tank box top alignment | +3…+21 below bubble top | — | 13 sprites |
| Header icon (3 bubbles + arrow) | 76 × 42 | **58 × 32** | bbox |
| Header icon arrow fill | — | `#d3d3d3` | modal sample |
| Nav strip height | 50 | **38.2** | y 56…105 |
| Nav tab block width | 922 | **704 ± 5** | x 480…1402 |
| Selected tab width | 104 | **79** | x 1196…1299 |
| Deselected tab width | 96–97 | **73–74** | x 1001…1098, 1100…1195 |
| Selected tab body colour | — | `#ffffff` | y 63…105 at x 1250 |
| Deselected tab body gradient | — | `#e6e6e6` → `#c6c6c6` | y 70 → 104 at x 1150 |
| Sidebar box width (both columns) | 160 | **122** | x 85…244, 1633…1792 |
| Scrollbar thumb | y 106…487 (382) | — | doc ≈2.4–2.6 × viewport |

---

#### What this frame does NOT show

- **A thread view.** No open thread, no reply bubbles, no alternating pointers, no per-post
  timestamps, no post ids. **S58's core want is not met.**
- **Any grey or yellow bubble.** Measured, not eyeballed — see the table in §3.
- **Any composer** (S61, S62) — the session is logged out.
- **The inline edit + `Bounce.easeOut` height animation** (S63) — needs a logged-in user editing.
- **Any moderation UI** (S64) — no icons, no hover trail, no `forumHideTrail()` artefact.
- **The 75 ms × index fade-in stagger** (S60) — the page is fully settled; this is a single frame,
  and S60 needs frame-stepping the first second after load.
- **`forumAllUserInfo`** (S68) — it is `display:none` by construction; nothing to see.
- **Any filter control** (S65) or **numbered pager** (S66); the bottom of the page is off-frame.
- **The page footer / copyright year** — cut by the frame edge at y = 1047.
- **The 2017–2018 forum.** This is Feb 2015. The nav strip alone proves the page changed.

---

## Consequences for the rebuild

### Confirmed

1. `[OBSERVED]` `srv/index.php:12041` `Tank Owner's Forum` renders verbatim, centred in
   `#centerColumn`, `text large` ≈ 18 px. **Era-stable string** (unchanged 2015 → 2018).
2. `[INFERRED]` `srv/index.php:12048` `x_showForumPreviews(1, 20, …)` — the preview-list route is
   real, the previews are speech bubbles, and the page-length arithmetic supports 20 rows.
3. `[MEASURED]` `srv/index.php:12074` `55 * scale` — the tallest tank sprite is 55.0–55.7 CSS px,
   confirming the 110×55 base with `scale = 1`.
4. `[INFERRED]` `srv/index.php:12158` `rows[1].cells[1]` — the bubble is an HTML table; eight
   bubbles at five heights and three widths share pixel-identical corner and pointer art.
5. `[INFERRED]` `srv/index.php:12285` `leftSide` is a **per-post** argument: previews never
   alternate, so alternation belongs to the thread view only.
6. `[OBSERVED]` `srv/index.php:13044-13049` Mod Activity — a forum-route-only box, confirmed live
   with three name/time pairs and the two-size treatment.
7. `[MEASURED]` `srv/index.php:12437-12438` — login placeholders `username` and `password`
   (8 bullets) confirmed; `:12433-12434` the `?` link sits at the header's top-left.
8. `[OBSERVED]` `srv/index.php:13054-13058` Got Feedback? closed-state copy and the 72×29 envelope.
9. `[OBSERVED]` `srv/index.php:12973`, `:12975-12977` — Victories header and the
   `Weekly`(selected, bold black) / `Friends`(deselected, grey, raised) bottom tabs.
10. `[MEASURED]` `srv/index.php:12394-12399` — the Courier 4-tier countdown ladder, confirmed to
    within 1.5 px per tier.
11. `[MEASURED]` `srv/index.php:12028` — the tab block was 704 ± 5 CSS px in Feb 2015 vs the coded
    708 px, i.e. the strip width survived the redesign.

### Contradicted — overhaul owed

Per **THE OVERHAUL RULE**, invented M2/M3 pieces are rewritten wholesale when evidence lands.
Two calls, and I want to be careful about how far each goes:

1. **Nothing in the forum reconstruction is contradicted, because nothing exists.** Era-final
   `?forum` is `<div id="forumwrapper"></div>` and the SAJAX response was never built. There is no
   invention to supersede — this frame is **greenfield input**, not a correction. If anyone has
   since drafted a speculative preview-row layout, it should be rewritten against §§3–5 above
   rather than patched: the constants (57 px tank advance, 52 px pointer, 6 px row gap,
   21.5 px bubble overhead, 14/12/10 px type ladder, right-floated metadata, sort-by-last-activity)
   are all now measured and would not survive a patch-shaped merge.
2. **VE entry 10 must not be upgraded on this frame, and the timeline argument should be tightened,
   not weakened.** The strip here is **five tabs**; the era-final is six. That is direct proof the
   strip was re-cut between Feb 2015 and the era-final — which *supports* entry 10's premise that
   the strip is versioned as a set, but also means this capture is on the wrong side of the change.
   `tab5Select.jpg` stays **O?**. Concretely: do **not** let anyone cite
   `K-forum-thread-preview-list-2015.png` as in-era confirmation of the forum tab artwork.

### Still unknown / stays on the want-list

Proposed status for every S-number in §F, individually:

| # | Item | Proposed status | Why |
|---|---|---|---|
| **S57** | Thread-preview list (page 1, 20 items) | **WANTED → PARTIAL** | Row anatomy, geometry, typography, sort order and the participant-roster rule are now measured — but from a **Feb 2015** page, only 8 of 20 rows are visible, and the bottom of the page (and any pager) is off-frame. Do not mark FETCHED. |
| **S58** | Speech-bubble post rendering | **WANTED (partially informed)** | The **default** variant is fully characterised (white fill, ~1 px near-black border, 3–4.6 px radius, 52 px fixed left pointer at +21 px, down-right shadow, 21.5 px overhead). **Grey and yellow are still unseen and their meaning is still unknown.** The "alternating" clause should be re-scoped to the thread view. |
| **S59** | Per-post tank render + scale | **WANTED → PARTIAL** | `scale = 1` for all 12 users here; five different posters give a cell width identical to 0.1 px; per-participant advance 55–59 CSS px; box top-aligned to the bubble. Whether scale is rank-linked for *other* ranks is still open — this is one logged-out page from one day. |
| **S60** | Post fade-in stagger (75 ms × index) | **WANTED** | Single settled frame. Needs frame-stepping the first second after load. |
| **S61** | New-thread form | **WANTED** | `[NOT VISIBLE]`. New sub-fact: the composer is **not rendered for logged-out visitors**. |
| **S62** | Reply form | **WANTED** | `[NOT VISIBLE]`, same reason. |
| **S63** | Inline edit + `Bounce.easeOut` | **WANTED** | Needs a logged-in user editing their own post. |
| **S64** | Moderation controls (8 endpoints) | **WANTED** | Zero UI evidence still. The row-2 "two participants / no posts yet" anomaly is a *hint* that a delete/disable had occurred, but it is a hint, not a control. |
| **S65** | Thread filter (`'all'`) | **WANTED** | No dropdown, tab row or filter control anywhere above the list. Absence recorded. |
| **S66** | Pagination (`firstPreview`/`lastPreview`) | **WANTED → PARTIAL (weak)** | One 58×32 CSS px "three bubbles + grey right arrow" icon, right-aligned above the list, is the only candidate; meaning `[UNCERTAIN]`. Page-length arithmetic independently supports a 20-row page. |
| **S67** | Scroll-to-top after posting (3 s) | **WANTED** | Requires a post being made on camera. |
| **S68** | `forumAllUserInfo` hidden block | **WANTED (unchanged, LOW)** | Hidden by construction; but §4's cell-width result now makes the block's `scale` attribute *inferable as 1* for these users, which is what the want said would happen via S59. |

### New wants to add

- **W-a. A logged-in `?forum` preview list.** Would settle S61/S65/S66 in one shot (composer entry
  point, filter control, pager) and would show whether any per-row control appears for an
  authenticated user. Trigger: any footage where the player logs in *then* clicks the forum tab.
- **W-b. A second `?forum` preview list from a different day.** Diffing two preview lists isolates
  which parts of the row are per-thread and which are chrome, and — crucially — a page-2 capture
  would decide the three-bubble icon's meaning outright.
- **W-c. Any capture of the thread with two participants and `no posts yet`.** Whatever produces
  that state is a rule the rebuild must reproduce.
- **W-d. Confirmation of the metadata element's CSS.** The right-float shrink-to-fit inference in
  §3 is falsifiable by a single capture where a wrapped metadata block is right-aligned. Cheap and
  decisive.
- **W-e. A 2017–2018 `?forum` capture, at any quality.** Everything in this document is Feb 2015.
  The forum could have been restyled with the nav strip. This want should be recorded explicitly
  so nobody assumes 2015 geometry is era-final.
- **W-f. The `forumStyles.css` bytes themselves.** They are cited throughout §F of the want-list
  but are not in the staged tree; if they exist in the repo they would let a future analyst check
  my pointer/radius/shadow numbers against the real 9-slice slice sizes in one pass.

---

## Recommended edits to existing docs (not applied)

1. **`docs/standards/VISUAL-EVIDENCE-WANTED.md` §F, S57** — change status to `PARTIAL` and replace the
   "What exists" cell with:
   > *Preview row layout recovered from one Feb-2015 frame
   > (`manualevidence/UI/K-forum-thread-preview-list-2015.png`, see
   > `manualevidence/K-forum.md`): 8 of 20 rows, sort key = `max(created, last_post)` desc,
   > row = `[N participant tanks][52 px left pointer][bubble: bold 14 px title / 14 px body +
   > 10 px grey "[click to open]" / 12 px grey right-floated "A & B & C, <age> ago - last post
   > <age> ago"]`. Still missing: rows 9–20, the era-final (2017-18) styling, the page bottom.*

2. **`docs/standards/VISUAL-EVIDENCE-WANTED.md` §F, S58** — keep `WANTED` but split the cell:
   > *Default variant now measured (white fill, 1–1.5 px near-black border, 3–4.6 px radius,
   > fixed 52 px pointer at +21 px from the bubble top, down-right 3–4 px shadow, ~21.5 px vertical
   > overhead) — see `manualevidence/K-forum.md` §3. **Grey and yellow still never seen;
   > meaning still unknown.** Note: previews do **not** alternate pointer sides — all eight in the
   > recovered frame point left. Alternation is carried per-post by the `leftSide` argument at
   > `srv/index.php:12285`, so it is a thread-view property; re-scope this row's "alternating"
   > clause accordingly.*

3. **`docs/standards/VISUAL-EVIDENCE-WANTED.md` §F, S59** — change to `PARTIAL`:
   > *Twelve users measured in one frame: all render at `scale = 1` (tallest sprite 55.0–55.7 CSS px
   > = `55 × scale`); five different single-participant posters give a tank-cell width identical to
   > 0.1 px. Per-participant horizontal advance is 55–59 CSS px — about half the 110 px SWF width —
   > so adjacent tank boxes overlap by ≈53 px. The SWF box is top-aligned with the bubble's top
   > border. Open: whether `scale` differs for ranks not present in that frame.*

4. **`docs/standards/VISUAL-EVIDENCE-WANTED.md` §F, S66** — change to `PARTIAL (weak)`:
   > *A 58×32 CSS px icon — three overlapping black-outline speech bubbles with a `#d3d3d3`
   > right-pointing arrow — sits right-aligned above the preview list with no mirrored control on
   > the left. Candidate next-page art; could also be a new-thread entry point. Undecided.*

5. **`docs/standards/VISUAL-EVIDENCE-WANTED.md` entry 10** — leave the status at `PARTIAL, era-inferred` and
   **add a warning line**:
   > *NOTE: `manualevidence/UI/K-forum-thread-preview-list-2015.png` shows `/?forum` with the tab strip and the forum
   > tab selected, but it dates to **Feb 2015** and shows a **five-tab** strip (game/news/garage/
   > forum/lab — no shop; the shop opened 18-07-2015 per `srv/index.php:7327`). It therefore
   > **does not** upgrade `tab5Select.jpg` to O. What it does give: the selected-state idiom
   > (selected tab = pure `#ffffff` body with a black-ink icon; deselected = `#e6e6e6`→`#c6c6c6`
   > gradient body with an embossed grey icon), a 704 ± 5 CSS px tab block (vs the coded 708 px)
   > and a 38.2 CSS px strip height (vs the coded 53 px table).*

6. **`docs/standards/VISUAL-EVIDENCE-WANTED.md` §"Highest-yield single shots"** — item 4 currently reads
   *"A forum thread view with mixed bubble colours (S57-S63)"*. Suggest amending to:
   > *4. **A forum thread view with mixed bubble colours** (S58, S59, S63) — still the only way the
   > bubble variants are ever recovered. (S57 is now partially served by the Feb-2015 preview-list
   > frame; a **logged-in** preview list is the next-best shot after the thread view, because it
   > collapses S61/S65/S66 at once.)*

7. **`DECISIONS.md`** — append (do not edit existing entries):
   > *2026-08-04 — Forum preview-list geometry adopted from one Feb-2015 frame. Recorded as an
   > **era-extrapolation**, not era evidence: the source page has a five-tab nav strip and a visits
   > counter of 30 730 115 vs the era-final 68 374 157, so it predates the target window by ~3 years.
   > Constants taken: per-participant tank advance 57 CSS px, pointer reach 52 CSS px at +21 px,
   > inter-row gap 6 px, bubble vertical overhead 21.5 px, type ladder 14/12/10, metadata as a
   > right-floated shrink-to-fit element, previews sorted by last activity. Each is flagged for
   > re-derivation if any 2017-18 forum capture ever lands.*

8. **`DEDUCE.md`** — append a short method note: the 1.31 capture→CSS factor for this frame was
   derived from four page-side anchors (`width: 1312px` at `index.php:12035`, `#centerColumn`
   692 px at `:12039`, `availableOnTheAppStore120.jpg` at `:13025`, `envelope.jpg` 72×29 at
   `:13058`) and cross-checked against the Chrome bookmark star measuring its native 16 px, which
   establishes the video as 1:1 with the screen. Useful for any future analyst working the same
   `{GUID}` batch.

9. **`docs/standards/DIVERGENCES-SERVED.md` §3 (frozen live regions, S105)** — worth a footnote that the
   Mod Activity box's rendered shape (three name/time pairs, name in `text small gray`, time in
   `text tiny`) is confirmed unchanged from Feb 2015 to the served 20181214 bytes.

---

## Frank assessment: how much of the forum hole does this close?

**Honestly: perhaps a fifth of it, and not the fifth that was asked for.**

The want-list ranked *"a forum thread view with mixed bubble colours"* fourth of all outstanding
shots because it is the only route to S58–S63. This frame is **not that shot**. It is the
preview list, it is logged out, it is three years early, and every bubble in it is white. Of the
twelve S-numbers hanging off §F, **eight are untouched** (S60, S61, S62, S63, S64, S65, S67 and,
effectively, S68), one moves to a weak PARTIAL (S66), and only **S57 and S59** are genuinely
advanced.

What it *does* deliver is disproportionately useful for its size, because it is the first forum
pixel of any kind:

- **The default bubble is now a specified object**, not a guess: fill, border, radius, shadow,
  pointer shape and offset, vertical overhead, padding, and a three-level type ladder — all
  measured, all reproducible, all falsifiable.
- **S59's headline question — "does scale vary per user?" — has its first data**, and the data say
  *no, not among these twelve*. Five different posters producing a cell width identical to a tenth
  of a pixel is about as clean as this corpus gets.
- **A brand-new constant nobody had**: participants' tank boxes advance ~57 CSS px, i.e. they
  overlap. Any reconstruction that laid 110 px boxes end to end would have been wrong by 53 px per
  participant, and would have blown the centre column apart on a three-participant thread.
- **The sort rule** (by last activity, with `no posts yet` threads keyed on creation) is a server
  behaviour, not just a look, and it was not previously known.
- **A negative that keeps the want-list honest**: the preview list does not alternate pointer
  sides. That clause needs re-scoping before someone builds it wrong.

The single most valuable thing it proves is the one I would put in the README: **`scale` was 1 for
every user on that page, and the tank slots overlap at ~57 CSS px** — because it converts S59 from
an open design question into a measured layout constant, and because it is the kind of fact that
would have been invented wrongly and then, under THE OVERHAUL RULE, thrown away later.

**The next-best shot, in order:**

1. **A logged-in `?forum` preview list.** One frame collapses S61 (composer entry point), S65
   (filter control) and S66 (pager) at once, and finally tells us what a user's *own* row looks
   like — which is the most likely home of the yellow bubble.
2. **Any thread view at all**, even one post, even blurry. It is the only route to S58's colour
   semantics, S59's in-thread scale comparison and S63's bounce.
3. **A page-2 preview list**, which would settle the three-bubble icon in a single click.
4. **A 2017–2018 `?forum` capture of any quality**, purely to tell us how much of this document
   still applies. Right now the answer is: unknown, and that uncertainty is the largest single
   caveat on everything above.
