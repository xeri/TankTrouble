# Visual evidence — the Tell A Friend referral popup

> Analysis of 4 evidence files under `manualevidence/` (3 PNG frames + 1 owner text note).
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)
> · [LEDGER.tsv](../../../LEDGER.tsv) · achievements cross-reference: [G-achievements.md](./G-achievements.md)

---

## Scope and provenance

`docs/standards/VISUAL-EVIDENCE-WANTED.md` **S86** records `/tellAFriendMail/` as:

> | S86 | **`/tellAFriendMail/` popup** | page-look | 460×535 no-scrollbar popup; 21 CDX 200s 2008-2018 | LEDGER 226; `srv/index.php:1179` | "Tell a Friend" clicked | LOW |

[LEDGER.tsv](../../../LEDGER.tsv) row 226 is `srv/tellAFriendMail/index.php  M2  —  written 2026-08-02  directory /tellAFriendMail/ observed in CDX; index filename convention-inferred  —  501 stub (milestone 1)`.
[DEDUCE.md](../../../DEDUCE.md) line 155 adds `/tellAFriendMail/ | 21 | 19 | 2008-04-30 … 2018-02-22 | 13 paths incl. images/`.
Recoverability was rated **LOW**. The entire page was unknown; the served file is a 501 stub.

**This topic renders that page.** Three frames show the popup open, filled in, and submitted.

### The four files

| # | File | Size (px) | Original capture mtime (NZST) |
|---|---|---|---|
| 1 | [`UI/J-popup-name-typed-george.png`](./UI/J-popup-name-typed-george.png) | 1273 × 775 | 2026-08-04 **17:19:38** |
| 2 | [`UI/J-popup-blank-fields.png`](./UI/J-popup-blank-fields.png) | 1380 × 776 | 2026-08-04 **17:20:10** |
| 3 | [`UI/J-popup-send-pressed-still-open.png`](./UI/J-popup-send-pressed-still-open.png) | 1377 × 774 | 2026-08-04 **17:20:57** |
| 4 | [`UI/tellafriendpopup.txt`](./UI/tellafriendpopup.txt) | 700 B | 2026-08-04 **17:23:15** |

Per the shared brief, those mtimes are **when the repo owner saved the crop today**, not when the
source footage was made. They give a *save order*, nothing more. Below I show that the save order
is **not** the footage order, and derive the real footage order from the page itself.

Throughout I use short names: **P0** = `J-popup-blank-fields.png`, **P1** = `J-popup-name-typed-george.png`,
**CS** = `J-popup-send-pressed-still-open.png`.

### One session, one popup, three moments

`[MEASURED]` All three frames contain the **same popup window at the same on-screen size**:
the window's left and right border columns are at x 323/911 (P1), 377/965 (P0), 376/964 (CS) —
outer width **589 capture px in every frame**. Only the crop rectangle differs. Cross-correlating a
static region of the parent page (the right-column Victories box, 160×190 px) against P1 gives
integer offsets `P0 = P1 + (dx 54, dy 2)` and `CS = P1 + (dx 53, dy 1)` at mean absolute residuals
of 2.61 and 2.56 / 255 — i.e. compression noise only. **Same capture scale, same session, same
window position on the desktop.**

`[INFERRED]` **Footage order is P0 → P1 → CS, which is _not_ the save order.** The Scrapyard
odometer in the parent page's left column reads (first nine plates legible, tenth mid-roll):

| frame | Scrapyard reading | save time |
|---|---|---|
| P0 | `2 2 0 8 3 8 3 7 0 ·` | 17:20:10 |
| P1 | `2 2 0 8 3 8 3 7 4 ·` | 17:19:38 |
| CS | `2 2 0 8 3 8 3 9 0 ·` | 17:20:57 |

`220838370· < 220838374· < 220838390·`. The Scrapyard is a scraps-accumulated counter driven by
`getScraps(includeVelocity, cb)` (`srv/index.php:184-194`, `includes/scrapyard.js`), so it runs
**up**. Reasoning is therefore: the frame with the lowest counter is earliest.
*Falsifier:* if the era counter ever ran down, the order reverses — but `velocity` in the
`getScraps` contract and the odometer metaphor both argue up, and the three form-fill states below
independently agree with the same order.

Corroboration from the form itself, which only ever gains content:

| frame | field 1 (heading) | field 2 (signature) | field 3 (Send to) | mouse pointer |
|---|---|---|---|---|
| P0 | placeholder `name` | placeholder `your name` | placeholder `email` | inside the browser address bar |
| P1 | typed `george` | placeholder `your name` | placeholder `email` | over the tank illustration |
| CS | typed `george` | typed `george` | typed `example@exampleemail.com` | on the **Send** button |

`[INFERRED]` The whole sequence reads as: popup opens → the recorder clicks into the address bar
and clears it (P0 shows Edge's empty-address-bar placeholder) → clicks back into the page, the
address bar reverts to the real URL → types the recipient name (P1) → types the signature and the
recipient email → clicks Send (CS). Every observable (counter, field states, pointer position,
address-bar state, input focus ring) is consistent with that single ordering, and no observable
contradicts it.

### What dates these frames — 2017-02-21 … 2018-12-18

This matters, because S86's era is the whole point.

1. `[OBSERVED]` The parent page's left column carries the **Scrapyard** box, populated with a live
   odometer. `DEDUCE.md:38` and `DEDUCE.md:358`: `getScraps()` first appears **2017-02-21**, "the
   exact date `scrapyard.js` went live — two independent sources, same day". ⇒ capture ≥ 2017-02-21.
2. `[OBSERVED]` The left-column red box reads **`OPEN BETA`** over **`Test online battles now!`**
   (underlined). The held body renders that slot as `PLAY ONLINE` (`srv/index.php:511`) over a
   `#countdown` div whose JS (`:517`) counts to `1475758800000` = 2016-10-06 12:00 CEST and, once
   past, prints `Online battles are in heavy development. Try now!` (`:550`). The held root body is
   stitched from `20181218_www.tanktrouble.com_.txt`. **Neither of the two strings the held file can
   produce is what is on screen** ⇒ the capture predates 2018-12-18.
3. `[OBSERVED]` Browser is **Microsoft Edge (EdgeHTML/"Edge Legacy")** on Windows 10 — the title bar
   reads `Tell a Friend - Microsoft Edge` and the empty address bar shows Edge Legacy's
   `Search or enter web address`. That browser shipped 2015-07 and was replaced 2020-01.
4. `[OBSERVED]` The Flash stage carries the watermark `version  4.0`, matching
   `TankTrouble_v4.0.swf` (`srv/index.php:404`, `:763`, …). `DEDUCE.md:365` gives that SWF one
   sha256 across 2013-03-13 → 2020-12-25, so this alone does not narrow the window; it only confirms
   the frames are not from a v3.x page.

`[INFERRED]` Combining 1 and 2: **the capture falls inside `[2017-02-21, 2018-12-18]`** — squarely
in the project's 2017–2018 target era. This is the strongest era-anchoring available for any
`/tellAFriendMail/` evidence, and it is what makes these frames usable rather than merely
interesting.

### Scale — how capture px convert to CSS px

`[MEASURED]` Anchor A: `srv/index.php:510` sets the beta box's outer div to `width: 120px`; both
inner panels are block children (padding `6px`, and at `:512` a `2px solid #ff0000` side border), so
the painted red area is exactly **120 CSS px** wide. Thresholding `R>170 ∧ G<80 ∧ B<80` in the left
column gives a red run of **152 capture px** in *all three* frames ⇒ `s = 152/120 = 1.26667`.

`[MEASURED]` Anchor B: the popup's client area measures **583 capture px** (see §Layout). If
`width=460` from `srv/index.php:1179` is exact, `s = 583/460 = 1.26739`.

The two independent anchors agree to **0.06 %**. Everything below uses
**`s = 1.2670 capture px per CSS px`**, and CSS figures are quoted to 0.1 px with that ±0.06 %
understood. Where a number is only meaningful in capture space I say so.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| J1 | The whole `/tellAFriendMail/` page is legible: illustration, heading, two body paragraphs, sign-off, logo lockup, three inputs, Send button — full verbatim transcript in §Transcription | `[OBSERVED]` + `[MEASURED]` | **S86**, LEDGER 226 | Yes — the 501 stub `srv/tellAFriendMail/index.php` is now writable from evidence |
| J2 | **Nothing in the copy is server-templated with a name.** The three "blanks" are `<input>` controls the *sender* fills in. Frame diffs show the only pixels that ever change inside the document are the three input interiors and the Send button | `[MEASURED]` | S86 | Yes — kills the "`Looking for trouble <name>?`" interpolation hypothesis before it is built |
| J3 | Client area measures **460.1 CSS px wide** and **≥ 534.3 CSS px tall visible with the bottom edge outside every crop** — matches `width=460,height=535` at `srv/index.php:1179` | `[MEASURED]` | S86, LEDGER 226 | Confirms |
| J4 | **No scrollbar.** Content runs to the viewport's right edge; the client width is the full 460 with nothing subtracted | `[MEASURED]` | S86 ("no-scrollbar") | Confirms |
| J5 | Canonical URL is `https://www.tanktrouble.com/tellAFriendMail/` — **with trailing slash, over HTTPS** (read from Edge's status bubble in CS) | `[OBSERVED]` | S86, LEDGER 226 (`index.php` filename convention) | Confirms the directory form |
| J6 | Document `<title>` is **`Tell a Friend`** (read from the popup's own title bar) | `[OBSERVED]` | S86 | New fact — the stub has no title |
| J7 | `J-popup-send-pressed-still-open.png` **does not show the popup closed.** It shows the popup still open, fully filled, Send greyed out, pointer on Send, and a status bubble naming the submit target | `[OBSERVED]` | S86 | **Contradicts the filename claim as written** |
| J8 | Graphic block is **384 CSS px wide, centred** (38 px margins each side) — tank-on-ridge at top, maze-textured torn card, `TANKTROUBLE.com` ink band at the bottom | `[MEASURED]` | S86 | New geometry |
| J9 | Body paragraphs are **justified** (`text-align: justify`): wrapped lines flush at both edges with 9.5–10.3 CSS px word gaps, last lines ragged with 4.7–5.5 px gaps | `[MEASURED]` | S86 | New — a rebuild that left-aligns will be visibly wrong |
| J10 | The dash in the copy is an **ASCII hyphen `-`**, not an en/em dash (ink 3.9 CSS px vs 7.8 for an en dash at this size) | `[MEASURED]` | S86 | Byte-level detail |
| J11 | The trailing ellipsis is **three ASCII periods `...`**, not `…` — dot pitch 3.95 CSS px ≈ one period advance | `[MEASURED]` | S86 | Byte-level detail; `[UNCERTAIN]` at 1 px margin |
| J12 | No `?r=` referral URL appears anywhere in any frame. The only URL in the copy is the plain `www.TankTrouble.com` | `[NOT VISIBLE]` | **S22** | S22 stays WANTED |
| J13 | `/spreadTheWord/` is not reached, linked or shown | `[NOT VISIBLE]` | **S87** | S87 stays WANTED |
| J14 | The parent page's "Got Feedback?" box is visible in its **closed** state, matching `srv/index.php:1184-1191` line for line; the open state is still unseen | `[OBSERVED]` / `[NOT VISIBLE]` | **S11** | S11 stays WANTED (closed state was already known) |
| J15 | `tellafriendpopup.txt`'s achievement claim (10 sign-ups → silver sunglasses) matches `root/acheivements.txt` line 13 independently; both are wiki-grade, neither is a capture | `[INFERRED]`, low grade | S86 ↔ achievements catalogue | No |
| J16 | The signature field is **not prefilled from the session** — `LaikaClone02` is logged in on the parent page yet the field shows its `your name` placeholder | `[OBSERVED]` | S86 | Behavioural constraint |
| J17 | Bonus, outside this topic: the login sidebar shows a populated logged-in user card (`LaikaClone02`, `Exp. 13360`, trophy `1197 (0)`, skull `955`) plus a second empty Log In box | `[OBSERVED]` | **S6**, **S7** | Hand to topic E |

---

## Transcription — every string in the popup, verbatim

Read off the pixels at 4–7× LANCZOS upscale from **CS** (the frame with the most content) and
cross-checked against P0/P1 for the placeholder states. Ambiguous glyphs are marked.

### Browser chrome (not page content — recorded for provenance)

```
Tell a Friend - Microsoft Edge                      [ — ]  [ ▢ ]  [ ✕ ]
```
```
🔒  tanktrouble.com/tellAFriendMail
```
- `[OBSERVED]` Title-bar string is exactly `Tell a Friend - Microsoft Edge`. The separator is a
  spaced hyphen `-` (Edge's own window-title format is `<document.title> - Microsoft Edge`), so the
  **document title is `Tell a Friend`** — capital T, lower-case `a`, capital F, no site suffix.
  Note the parent page's box header at `srv/index.php:1168` uses the *same* casing,
  `Tell a Friend`.
- `[OBSERVED]` Address bar in P1 and CS: `tanktrouble.com` in near-black, `/tellAFriendMail` in
  grey. Edge Legacy suppresses the scheme and the `www.` label in this view, and shows no trailing
  slash. Path casing is `tellAFriendMail` — camel-cased exactly as `window.open('tellAFriendMail', …)`
  writes it at `srv/index.php:1179`.
- `[OBSERVED]` Address bar in **P0**: the field is white/expanded and shows Edge Legacy's empty-state
  placeholder `Search or enter web address`, with the mouse pointer inside it. The title bar still
  reads `Tell a Friend - Microsoft Edge`, so the document is unchanged — only the address bar's
  editing state differs.
- `[OBSERVED]` Status bubble, bottom-left, **CS only**:

  ```
  https://www.tanktrouble.com/tellAFriendMail/
  ```
  Full scheme, `www.` label, **trailing slash**. This is the only frame that gives the canonical URL.

### Page content

```
Looking for trouble [ name ] ?

Check out www.TankTrouble.com - it's the most
explosive coffee break game I've ever seen!

But watch out! Once you go, there's no turning
back! You will soon learn why...

I dare you,
[ your name ]

TANKTROUBLE.com

Send to [ email ] ( Send )
```

Element by element, with everything I can and cannot settle:

| Element | Transcription | Tag / notes |
|---|---|---|
| Heading, before the field | `Looking for trouble` | `[OBSERVED]` capital L only; "for" and "trouble" lower-case |
| Heading field | `<input>` — placeholder `name` | `[OBSERVED]` all lower-case, grey |
| Heading, after the field | `?` | `[OBSERVED]` a lone question mark, separated from the field by whitespace (measured gap 7.9 CSS px ≈ one space + sidebearing) |
| Body ¶1 | `Check out www.TankTrouble.com - it's the most explosive coffee break game I've ever seen!` | `[OBSERVED]`. `www.TankTrouble.com` carries an underline and internal capitals **T** and **T**. Terminal `!`. |
| — the dash | `-` (hyphen-minus) | `[MEASURED]` ink 5 capture px = 3.9 CSS px wide × 1.6 tall, sitting at mid-cap height. An en dash at this size would be ≈ 7.8 CSS px of ink, an em dash ≈ 14. **Not** an en/em dash. |
| — the apostrophes in `it's`, `I've`, `there's` | `'` (U+0027) | `[UNCERTAIN]` ASCII-mapped at 1× the mark is a 1–2 px vertical wedge, wider at the top, 5 rows tall, with **no leftward tail**. U+2019 would curl left at the bottom. Leaning strongly to U+0027 but 5 px of ink is thin proof. |
| Body ¶2 | `But watch out! Once you go, there's no turning back! You will soon learn why...` | `[OBSERVED]` |
| — the ellipsis | `...` (three ASCII periods) | `[MEASURED]` three dots at x = 702, 706–707, 712 (capture) ⇒ pitch ≈ 5.0 capture px = **3.95 CSS px**. Arial's period advance at this size is 3.89 CSS px; U+2026 would space its dots at ≈ 4.67. Matches three periods. `[UNCERTAIN]` the margin is ~1 px per gap. |
| — space before the dots? | probably none | `[UNCERTAIN]` gap from the `y` of `why` to the first dot is 3.2 CSS px; a word space here (this is the *last*, unjustified line) would give ≈ 5. |
| Sign-off label | `I dare you,` | `[OBSERVED]` capital I, trailing **comma** (not a period) |
| Signature field | `<input>` — placeholder `your name` | `[OBSERVED]` both words lower-case |
| Logo lockup | `TANKTROUBLE.com` | `[OBSERVED]` white on a black torn ink band. Rendered in the TankTrouble small-caps display face: full-height `T`…`T`, small-cap `ANK` / `ROUBLE`, then a small-cap `.com`. This is artwork, not live text. |
| Send row label | `Send to` | `[OBSERVED]` capital S, lower-case `to` |
| Email field | `<input>` — placeholder `email` | `[OBSERVED]` lower-case |
| Submit control | `Send` | `[OBSERVED]` capital S |

### Values typed by the recorder (not page copy)

| Field | P0 | P1 | CS |
|---|---|---|---|
| heading field | `name` (ph.) | `george` | `george` |
| signature field | `your name` (ph.) | `your name` (ph.) | `george` |
| email field | `email` (ph.) | `email` (ph.) | `…xample@exampleemail.com` |

`[OBSERVED]` In CS the email field's text is **scrolled**: the first glyph is vertically sliced by
the field's left inner edge and reads as the right half of a lower-case `e`.
`[INFERRED]` the full value is `example@exampleemail.com` — 24 characters at the field's measured
~7.3 CSS px average advance ≈ 175 CSS px against ~176 CSS px of usable field width, i.e. it
overflows by about half a glyph, exactly what is drawn. *Falsifier:* a longer prefix (e.g.
`myexample@…`) would overflow more; the visible ink is 171.3 CSS px, leaving room for only ~0.6 of
a character off-screen.

`[MEASURED]` Placeholder ink bottoms out at **#a2a2a2 – #a9a9a9** in all three fields; typed text
reaches **#000000 – #0b0103**. That two-tier rendering is the browser's placeholder treatment.
`[UNCERTAIN]` whether the markup uses the HTML5 `placeholder=` attribute or an era JS
focus/blur trick — a single still cannot separate them. HTML5 `placeholder` is available in every
browser this page ran in during 2017–2018, so it is the cheaper assumption, but say so in the
provenance sidecar rather than asserting it.

---

## The interpolation question — settled by frame differencing

**The task hypothesis was that the heading is server-templated (`Looking for trouble <name>?`).
It is not.** Here is the proof.

`[MEASURED]` P1 and P0 were aligned by the integer offset derived above (`dx 54, dy 2`), the
overlapping 1273 × 773 region extracted, and `ImageChops.difference` taken. Thresholding the
per-pixel channel maximum at > 60/255 leaves **6 766 changed pixels out of 983 429 (0.69 %)**, in
exactly six clusters (coordinates in P1 space):

| rows | columns | what it is | inside the popup document? |
|---|---|---|---|
| 62–79 | 388–621 | address-bar text: URL vs `Search or enter web address` | no — browser chrome |
| 81–89 | 699–714 | mouse pointer in the address bar (P0) | no — cursor |
| 118–133 | 157–181 | Scrapyard odometer plates | no — parent page |
| 194–213 | 719–734 | mouse pointer over the tank (P1) | no — cursor |
| 291 | 632–651, 667–778 | the name input's **top border** (focus ring) | yes |
| 303–323 | 635–713 | the name input's **interior text** | yes |
| 486–559 | 252–324, 911–1028 | Flash stage animating, left and right of the popup | no — parent page |

**Inside the popup document, the only pixels that differ between the empty state and the
`george` state are the first input's border row and the glyphs inside that input.** The words
`Looking`, `for`, `trouble` and the trailing `?` are byte-identical between the two frames. So is
every pixel of the tank, the card, the two body paragraphs, `I dare you,`, the logo band, the
`Send to` label and the button.

`[MEASURED]` The P1 ↔ CS diff (8 940 changed px) tells the same story from the other side. Inside
the document the changed clusters are:

| rows | columns | what it is |
|---|---|---|
| 291 | 631–782 | name input top border (focus ring moved away) |
| 488–558 | 417–535 | **signature** input interior: `your name` → `george` |
| 698–719 | 503–792 | **email** input interior + the **Send** button's rendering |

and nothing else — the copy, the artwork and the `Send to` label are again untouched.

### What this means for the rebuild

`[INFERRED]` `/tellAFriendMail/` is a **static composer form, not a personalised page**. There is no
recipient name to interpolate at render time, because at render time the server does not know one:
the sender types it. Concretely:

1. `Looking for trouble` + `<input placeholder="name">` + `?` — three separate inline nodes; the
   heading string is constant.
2. Both body paragraphs are constant strings with no substitution points at all.
3. `I dare you,` + `<input placeholder="your name">` — constant label, sender types the signature.
4. `Send to` + `<input placeholder="email">` + `<input type="submit" value="Send">`.

`[OBSERVED]` **The signature is not prefilled from the session.** `LaikaClone02` is logged in on the
parent page (user card visible in the left column, `Exp. 13360`), and the signature field still
shows its `your name` placeholder in both P0 and P1. So do not build a
`value="<?php echo $username ?>"` into the signature field.

*Falsifier for all of the above:* a frame of the popup opened by a **different** account, or in a
**logged-out** session, showing different heading text. Nothing here rules out that the server
substitutes something the recorder's session happened to render identically — but there is no
positive evidence for any substitution, and the placeholder-grey rendering of all three blanks is
positive evidence that they start empty.

`[MEASURED]` One extra behavioural detail: in **P1** the name input's borders are distinctly darker
(top `#a2a4a1`, right `#4a4d4c`) than in P0 (`#c6c6c6`, `#979797`) and CS (`#c1c1c3`, `#8f8f8c`),
while the signature and email inputs' borders are identical to within 2/255 across all three frames.
`[INFERRED]` the name input holds keyboard focus in P1 — consistent with the recorder having just
typed into it, and with the address bar (focused in P0) having lost focus by then.

---

## Layout measurement

All popup-relative coordinates below are given in **CS** capture space; `s = 1.2670`.

### 1. The window, and the 460 × 535 check

```
window outer, CS                x 376 … 964   = 589 capture px
window border (blue, active)    2–3 capture px each side   ≈ 2 CSS px
client area, CS                 x 379 … 961   = 583 capture px
                                583 / 1.2670  = 460.1 CSS px
requested (srv/index.php:1179)  width=460
                                → agreement to 0.1 CSS px
```

`[MEASURED]` **The popup's inner content area is 460.1 CSS px wide.** Edge Legacy therefore applied
`width=460` to the *client* area, not the outer frame. `[MEASURED]` Confirmed identically in P0
(x 380 … 962 = 583) and P1 (x 326 … 908 = 583).

Vertically the chrome subtracts, and the arithmetic is:

```
window top border                y 0 … 2      (3 capture px)
title bar                        y 3 … 40     = 38 capture = 30.0 CSS
address-bar band                 y 41 … 97    = 57 capture = 45.0 CSS
                                 ───────────────────────────────────
chrome above content             y 0 … 97     = 98 capture = 77.3 CSS
content (page background) starts y 98
```

`[MEASURED]` `#e1e0e3` page background runs from y 98 to the **last row of the frame** in every
capture:

| frame | content top | last row in frame | visible content height | as CSS |
|---|---|---|---|---|
| CS | 98 | 773 | 676 capture px | **533.5** |
| P1 | 97 | 774 | 678 capture px | **535.1** |
| P0 | 99 | 775 | 677 capture px | **534.3** |

`[NOT VISIBLE]` The window's bottom border is outside all three crops — sampling column x = 900 for
the last ten rows of each frame returns unbroken `#e1e1e1`. So the height cannot be *closed off*.
`[MEASURED]` But **at least 533.5–535.1 CSS px of scroll-free content is visible**, which is
`height=535` to within measurement error, and there is no room left for a bottom border inside the
crop. `[INFERRED]` `height=535` is confirmed as far as a still can confirm it; the residual doubt is
±2 CSS px.

### 2. No scrollbar — confirmed

`srv/index.php:1179` passes `scrollbars=0`. Modern browsers ignore that feature flag, so the real
question is whether the content overflowed 535 px and forced one.

`[MEASURED]` Sampling column **x = 955** (≈ 5 CSS px inside the client area's right edge) over rows
100–769 returns `#e2e0e3` for 523/670 rows and shades within 2/255 of it for the rest — the page
background, uninterrupted. Column x = 948 likewise. Edge Legacy draws a classic, space-consuming
vertical scrollbar ≈ 17 CSS px ≈ 21.5 capture px wide with a `#f0f0f0` track, a `#cdcdcd` thumb and
arrow buttons. **None of that is present.**

`[MEASURED]` Second, independent proof: the client width measures the *full* 460.1 CSS px. Had a
classic scrollbar been rendered, the layout viewport would have been ≈ 443 px and the centred
384 px graphic would have sat 4 px right of the window centre. It does not — see §3.

`[MEASURED]` Third: total content height is 493.3 CSS px (§4), comfortably inside 535. There is
nothing to scroll.

**S86's "no-scrollbar" characterisation is confirmed on three independent grounds.**

### 3. Horizontal layout

```
client area          x 379 … 961        0.0 …  460.1 CSS
graphic block        x 428 … 913       38.7 …  422.3 CSS   width 383.6 CSS
  left margin        49 capture         38.7 CSS
  right margin       48 capture         37.9 CSS
```

`[INFERRED]` The graphic is **384 CSS px wide, horizontally centred**, giving symmetric 38 px
margins: `38 + 384 + 38 = 460`. The measured 383.6 / 38.7 / 37.9 split reproduces that to within a
third of a pixel, and 384 is the only nearby integer that makes the margins equal. *Falsifier:* an
image of 383 or 385 px with a 0.5 px rounding — but then the two margins would differ by 1 px, and
they do not.

Inside the card:

```
card black side rules   x 428–429 and 912–913   (≈ 1.6 CSS px thick, part of the artwork)
text column             x 467 … 874             69.5 … 390.7 CSS   width 322.0 CSS
  padding inside card   39 capture each side    30.8 CSS each side
```

Controls:

| control | capture x | CSS x (from client left) | CSS width |
|---|---|---|---|
| name input (outer border box) | 683 … 835 | 240.0 … 360.0 | **120.8** |
| `?` glyph | 845 … 856 | 367.8 … 376.5 | 9.5 |
| signature input (outer) | 466 … 644 | 68.7 … 209.2 | **141.3** |
| `Send`/`to` label ink | 497 … 547 | 93.1 … 132.6 | 40.3 |
| email input (outer) | 552 … 781 | 136.6 … 317.3 | **181.5** |
| Send button (outer) | 785 … 846 | 320.4 … 368.6 | **48.9** |

`[MEASURED]` The Send row is centred: its ink spans x 496 … 846, midpoint 671; the client area's
midpoint is 670. Inter-element gaps: `Send`→`to` 3.2 CSS px (a word space), `to`→input 2.4,
input→button 2.4.

`[MEASURED]` Heading spacing: `trouble` ink ends at x 675, the name input's border box starts at
683 → 6.3 CSS px; the input ends at 835, the `?` ink starts at 845 → 7.9 CSS px. Both are
one-space-plus-sidebearing at this font size. `[INFERRED]` the markup has whitespace on both sides
of the input, i.e. `Looking for trouble <input …> ?`.

### 4. Vertical rhythm

Offsets are from the top of the client area (y = 98 in CS).

| # | element | capture y | offset (CSS) | height (CSS) |
|---|---|---|---|---|
| 1 | client area top | 98 | 0.0 | |
| 2 | graphic block / tank ink top | 124 | **20.5** | |
| 3 | tank body (above the ridge) | 124 … 204 | 20.5 | 63.9 |
| 4 | ridge + torn top edge, full width | … 250 | | |
| 5 | name input (outer) | 291 … 326 | 152.3 | **28.4** |
| 6 | heading cap band (`L`) | 299 … 317 | 158.6 | cap 15.0 |
| 7 | body ¶1 ink | 359 … 395 | 206.0 | 29.2 (two lines) |
| 8 | body ¶2 ink | 424 … 459 | 257.3 | 28.4 (two lines) |
| 9 | `I dare you,` ink | 488 … 499 | 307.8 | 9.5 |
| 10 | signature input (outer) | 504 … 540 | 320.4 | **29.2** |
| 11 | logo ink band | 615 … 664 | 408.0 | **38.7** |
| 12 | graphic block bottom | 664 | **446.7** | |
| 13 | Send row (outer) | 694 … 720 | 470.4 | **21.3** |
| 14 | Send row bottom | 720 | **491.0** | |

`[MEASURED]` Gap from the graphic's bottom edge to the Send row's top: 30 capture px = **23.7 CSS px**.
Total drawn content: `20.5 + 427.0 + 23.7 + 21.3 = 492.5 CSS px`, leaving ≈ 42 CSS px of empty page
background below the Send row inside a 535 px viewport.

`[MEASURED]` A completeness scan (any pixel differing from the sampled background by > 14/255 in any
channel, across the whole client area) finds **exactly two content blocks** in every frame — the
graphic block and the Send row — plus, in CS only, the browser's status bubble. There is no header,
no footer, no close link, no secondary message area, nothing between the logo and the Send row.

### 5. The illustration, the card and the logo lockup

`[OBSERVED]` **Top — tank on a ridge.** A flat black-and-white cartoon tank in three-quarter view
facing right, cresting a jagged black ridge that forms the card's torn upper edge. The turret's
barrel points up and to the right and ends in a heavier muzzle block; a rounded light hatch/dome
sits at the turret's left. The hull carries a track assembly drawn as white circles/capsules on
black — I count five along the upper run and four below, `[UNCERTAIN]` on the exact count because
the lower ones merge with the ridge silhouette. Rendering is flat black + white; there is no grey
shading beyond compression.
`[MEASURED]` tank body alone (above the ridge): x 593…764, y 124…204 = **135.8 × 63.9 CSS px**.
Tank plus ridge: x 436…905, y 124…249 = **371.0 × 99.5 CSS px**.

`[OBSERVED]` **Middle — the note card.** A white panel bounded left and right by a ~1.6 CSS px black
ink rule, filled with a very faint grey **maze pattern**: right-angled wall segments in the
TankTrouble idiom.
`[MEASURED]` Autocorrelating a text-free 70 × 435 capture-px patch (x 470…905, y 548…618) along both
axes gives peaks at lags 6, 13, 19, 25, 32, 38, 44, 51, 57, 64, 70, 76 capture px in x and 6, 13,
19, 25, 32 in y — a **square grid of pitch (76−6)/11 = 6.36 capture px = 5.02 CSS px**.
`[MEASURED]` The pattern's ink sits at the 0.5th–10th percentile of the patch, i.e. grey levels
**237–243** against a **249–254** paper, so the walls are roughly `#eded ed`–`#f3f3f3` on near-white.

`[INFERRED]` **This does not challenge `docs/standards/MAZECREATOR-VISUAL-SPEC.md`.** The pinned constants
there are CELL = 32 px, wall `#444444` at 4 px. The popup texture is a decorative ~5 px-pitch tile
in near-white — a different asset for a different purpose. Record it as its own constant; do not
reconcile the two.

`[OBSERVED]` **Bottom — the logo lockup.** A solid black ink band with irregular/torn ends, carrying
`TANKTROUBLE.com` in white in the TankTrouble small-caps display face (full-height `T`, small-cap
`ANK`, full-height `T`, small-cap `ROUBLE`, small-cap `.com`).
`[MEASURED]` band bbox x 432…908, y 615…664 = **376.5 × 39.5 CSS px**; sampling column x = 660 the
band runs y 625…663 (30.0 CSS px tall there) with white lettering occupying y 637…656
(**15.8 CSS px** of small-cap height). `[UNCERTAIN]` the full-height `T` cap height — the band's
white lettering merges optically with the white card above and below at this resolution.

`[UNCERTAIN]` Whether the graphic is **one** image or a three-part header/middle/bottom stack. A
single still cannot tell. The three-part reading is more likely on two grounds: (a) the classic site
already uses that idiom — LEDGER row 66 holds `srv/images/boxTellAFriendMiddleAndBottom.jpg` as **O**
bytes for the sidebar box; (b) `DEDUCE.md:155` records the `/tellAFriendMail/` directory as
**"13 paths incl. `images/`"** across 21 CDX 200s, i.e. the popup ships its own image directory with
roughly a dozen files — more than one graphic. **Recommended next hunt: enumerate the CDX paths under
`/tellAFriendMail/images/` and refetch them.** That would turn this whole page from M2 to O for the
artwork.

### 6. Typography and colour

| run | measurement | derived |
|---|---|---|
| heading `Looking…` | cap `L` = 19 capture = **15.0 CSS**; ascender-to-descender 26 capture = 20.5 CSS | font-size ≈ **21 px** (Arial cap height 0.716 em) `[UNCERTAIN]` ±1 |
| body ¶ text | cap `C` = 13 capture = **10.3 CSS** | font-size ≈ **14 px** `[UNCERTAIN]` ±1 |
| `I dare you,` | cap `I` = 11 capture = **8.7 CSS** | font-size ≈ **12 px** `[UNCERTAIN]` ±1 — noticeably smaller than the body |
| `Send to` | ink height 12 capture = **9.5 CSS** | font-size ≈ **13 px** `[UNCERTAIN]` |
| name-input text `george` | x-height + descender = 21 capture = **16.6 CSS** | font-size ≈ **22–23 px** `[UNCERTAIN]` — the input's own font, slightly larger than the heading |
| signature-input text | 20 capture = **15.8 CSS** | font-size ≈ **21–22 px** `[UNCERTAIN]` |
| email-input text | 18 capture = **14.2 CSS** | font-size ≈ **13–15 px** `[UNCERTAIN]` |

`[OBSERVED]` Glyph shapes are Arial/Helvetica-family throughout the page copy: single-storey `g` with
an open tail, double-storey `a`, bare `I` stem, flat-cut `t`.

`[MEASURED]` **Justification.** In body ¶1's first line the inter-word ink gaps are 12–13 capture px
(**9.5–10.3 CSS**); in its second (final) line they are 6–7 capture px (**4.7–5.5 CSS**). Same for
¶2. Both wrapped lines terminate at exactly **x = 874** while both final lines stop short.
Arial's natural word space at ~14 px is 3.9 CSS px, so the wrapped lines carry ≈ 5 CSS px of
injected space per gap. **This is `text-align: justify`, not left alignment**, and it is the single
most visible thing a naïve rebuild would get wrong.

`[MEASURED]` Colours:

| surface | sampled hex | note |
|---|---|---|
| popup page background | **`#e1e0e3`** (8 385 / 8 400 px in a 120 × 70 sample); `#e1e1e1` in P0 | true CSS value is `#e1e1e1` or `#e0e0e0`; the `+2` blue in CS is chroma-subsampling drift |
| card paper | `#f8f8fa`…`#ffffff`, modal `#fafafc` | white with the faint maze tile |
| card maze tile ink | `#ededed`…`#f3f3f3` | 0.5th–10th percentile of the patch |
| card / logo ink | `#040406`, `#050505` | black |
| input fill | `#fefeff` | white |
| input border (idle) | top `#c1c1c3`, bottom `#a8a8a8`, right `#8f8f8c` | browser default 2 px inset field border |
| input border (focused, P1 name field) | top `#a2a4a1`, right `#4a4d4c` | focus ring |
| placeholder ink | `#a2a2a2` – `#a9a9a9` | all three fields |
| typed ink | `#000000` – `#0b0103` | |
| body copy ink | reaches `#000000` | black |
| heading ink | reaches `#060001` | black |
| `I dare you,` ink | floor `#272330` | `[UNCERTAIN]` grey, or just antialiasing at 12 px |
| `Send to` ink | floor `#351011` | `[UNCERTAIN]` same caveat, and it sits on the grey background |
| body link underline | one row at y = 373, x 561…743 (**144.4 CSS px**), ink `#1e1a1d` | |
| body link glyphs | darkest-25 mean `#1e1a1d` (R 30 G 26 B 29) | **not blue** — a default unvisited link would be `#0000ee` |

`[INFERRED]` `www.TankTrouble.com` is an anchor whose colour has been overridden to the body colour,
keeping only the underline. Any rebuild that lets the browser default apply will render it blue and
be wrong.

### 7. Window features requested vs. what Edge actually gave

`srv/index.php:1179` verbatim:

```js
window.open('tellAFriendMail', '_blank', 'width=460,height=535,left='+(screen.width-460)/2+',top='+(screen.height-535)/2+',resizable=0,toolbar=0,location=0,status=0,menubar=0, scrollbars=0,directories=0');
```

| feature | requested | what the frames show |
|---|---|---|
| `width=460` | 460 | `[MEASURED]` client area **460.1 CSS px** ✔ |
| `height=535` | 535 | `[MEASURED]` ≥ 533.5–535.1 CSS px visible, bottom edge out of frame ✔ (as far as visible) |
| `toolbar=0` | none | `[OBSERVED]` no back/forward buttons, no tab strip, no favourites bar ✔ |
| `menubar=0` | none | `[OBSERVED]` no `…` menu button ✔ |
| `directories=0` | none | `[OBSERVED]` ✔ |
| `location=0` | hide URL | `[OBSERVED]` **an address bar is shown anyway** ✘ — Edge Legacy (like every post-2010 browser) forces the URL visible in popups |
| `status=0` | no status bar | `[OBSERVED]` no persistent status bar; a transient link/navigation bubble appears in CS ✔/✘ |
| `scrollbars=0` | none | `[MEASURED]` none present ✔ (and the content genuinely fits) |
| `resizable=0` | fixed | `[UNCERTAIN]` the maximise button is drawn and looks enabled; a still cannot test resizing |

`[INFERRED]` **Do not treat the 98 capture px / 77.3 CSS px of chrome as an era constant.** It is
Edge Legacy's popup chrome under whatever DPI the recorder ran; a 2017 Chrome or IE11 popup would
have different chrome, and `location=0` might have been honoured in older engines. The chrome is
provenance, not specification. What *is* specification is the 460-px client area it encloses.

---

## File-by-file analysis

### `UI/J-popup-name-typed-george.png` — 1273 × 775, saved 17:19:38, **second** in footage order  *(was `tellafriendmailpopup1.png`)*

**Filename claim (repo owner):** the name itself only asserts "tell a friend mail popup" (the `1`
suffix distinguishes it from the sibling). **Corroborated** — the frame shows the
`/tellAFriendMail/` popup.

**What is drawn**

- `[OBSERVED]` A separate Edge Legacy browser window, title `Tell a Friend - Microsoft Edge`, with
  minimise / maximise / close glyphs at the right of the title bar. Border colour is the active-window
  blue (`#6790bf` sampled at the left border, y 400).
- `[OBSERVED]` Address bar shows `tanktrouble.com` (dark) + `/tellAFriendMail` (grey) with a padlock
  glyph at the left.
- `[OBSERVED]` The popup document: tank-on-ridge illustration; maze-textured card; heading
  `Looking for trouble` + input containing **`george`** + `?`; both body paragraphs; `I dare you,`
  above an input showing the grey placeholder `your name`; `TANKTROUBLE.com` ink band; a
  `Send to` row with an input showing the grey placeholder `email` and a `Send` button with a dark
  label and a `#a3a3a3` border.
- `[OBSERVED]` Mouse pointer (standard arrow) sits over the tank illustration at ≈ (720, 200).
- `[OBSERVED]` Parent page visible left and right of the popup: Scrapyard `220838374·`, the green
  Dimitrium news box (`Dimitrium has been found in the mazes!`), the red `OPEN BETA` /
  `Test online battles now!` box, an empty `Log In` box, and the `LaikaClone02` user card; on the
  right `Need Help? / Check the FAQ`, the `Victories` table, Facebook Like/Share, the App Store and
  Google Play badges, the `Tell a Friend` box and the `Got Feedback?` box.

**Measurements**

- `[MEASURED]` window outer x 323…911 = 589 capture px; client x 326…908 = 583 = **460.1 CSS px**.
- `[MEASURED]` content top y 97, last row 774 ⇒ **535.1 CSS px** of scroll-free content visible.
- `[MEASURED]` Send row: label 443…478 / 483…495, input 499…728 (**181.5 CSS**), button 732…793
  (**48.9 CSS**), row height 28 capture = **22.1 CSS**.
- `[MEASURED]` name input borders are darker than in the other two frames (top `#a2a4a1`,
  right `#4a4d4c` vs `#c1…`/`#8f…`) while the other two inputs match to 2/255 ⇒ focus is in the name
  input.

**Links to the program**

- **S86 / LEDGER 226:** first direct render of the page. Confirms the route, the 460 px client width,
  the no-scrollbar claim and the document title.
- **`srv/index.php:1179`** — the popup this frame shows is exactly what that line opens; the address
  bar's camel-cased `tellAFriendMail` matches the string literal.
- **`srv/index.php:1167-1173`** — the `Tell a Friend` box that triggers it is visible in the parent
  page's right column with header text `Tell a Friend` and the `images/tellAFriend.png` art
  (LEDGER row 417, held **O**, sha256 `7670fd47…`) overflowing its 35 px content div exactly as the
  inline `top: -10px; left: 14px` implies.

**What this does NOT show** — the popup's bottom edge; any success/failure state; any `?r=` URL;
the `Send` button's hover or active styling; whether the form is GET or POST.

---

### `UI/J-popup-blank-fields.png` — 1380 × 776, saved 17:20:10, **first** in footage order  *(was `tellafriendmailpopup.png`)*

**Filename claim (repo owner):** as above. **Corroborated.**

**What is drawn**

- `[OBSERVED]` Same window, same position, same title bar. The **address bar is in its
  empty/editing state**: white expanded field, Edge Legacy's placeholder `Search or enter web
  address`, mouse pointer inside it at ≈ (755, 82). The document beneath is unchanged — the title bar
  still reads `Tell a Friend`.
- `[OBSERVED]` **All three form fields show their placeholders**: `name`, `your name`, `email`, all
  grey (`#a2a2a2`–`#a9a9a9`). This is the pristine state of the page as served.
- `[OBSERVED]` `Send` button in its idle state: face `#d4d4d4`, border `#a1a1a1`, dark label.
- `[OBSERVED]` Scrapyard reads `220838370·` — the lowest of the three, hence the earliest frame.

**Measurements**

- `[MEASURED]` window outer x 377…965 = 589; client x 380…962 = 583 = **460.1 CSS px**.
- `[MEASURED]` content top y 99, last row 775 ⇒ **534.3 CSS px** visible, no scrollbar.
- `[MEASURED]` page background here reads a cleaner **`#e1e1e1`** (this frame has less chroma drift
  than CS), which is the best single estimate of the popup's `background-color`.
- `[MEASURED]` name input outer box x 687…834 (**116.8 CSS**, vs 120.8 measured in CS — the 4 px
  spread is the border-detection threshold, not a real difference).

**Links to the program**

- **S86:** this is the frame to redraw from. It is the only one showing the page exactly as a first
  visitor sees it, with every placeholder intact and nothing typed.
- **`srv/index.php:1179`** — same as above.

**What this does NOT show** — the URL (the address bar is cleared); the popup's bottom edge; any
submitted state.

---

### `UI/J-popup-send-pressed-still-open.png` — 1377 × 774, saved 17:20:57, **third** in footage order  *(was `closesafteryouclicksend.png`)*

**Filename claim (repo owner):** *"closes after you click send"*. **Not corroborated as written —
and this matters.**

**What is actually drawn**

- `[OBSERVED]` **The popup is still open and fully visible.** Same window, same position, blue
  (active) border. The parent page is *not* revealed where the popup was.
- `[OBSERVED]` Every field is now filled: heading input `george`, signature input `george`, email
  input showing `…xample@exampleemail.com` with the first glyph sliced by the field's left edge.
- `[OBSERVED]` The **Send button is washed out**: face `#e2e2e2` (against `#d4d4d4`/`#d5d5d5` in the
  other two frames), border `#cfcfcf` (against `#a1a1a1`/`#a3a3a3`), label greyed.
  `[MEASURED]` mean of the 40 darkest label pixels: **116.5** in CS vs **84.3** (P0) and **82.2**
  (P1); pixels below luminance 160 drop from 213 to 116. This is a *lightening*, which is the
  Windows/Edge **disabled** treatment — a pressed button darkens, it does not lighten.
- `[OBSERVED]` The mouse pointer sits **on** the Send button, at ≈ (826, 718).
- `[OBSERVED]` A status bubble at the window's bottom-left reads
  **`https://www.tanktrouble.com/tellAFriendMail/`**.
- `[OBSERVED]` The address bar still reads `tanktrouble.com/tellAFriendMail`.
- `[OBSERVED]` Scrapyard `220838390·` — the highest, hence the latest frame.

**Measurements**

- `[MEASURED]` window outer x 376…964 = 589; client x 379…961 = 583 = **460.1 CSS px**.
- `[MEASURED]` content top y 98, last row 773 ⇒ **533.5 CSS px** visible.
- `[MEASURED]` status bubble occupies y 745…770, x 384…697.
- `[MEASURED]` completeness scan finds only the graphic block (y 123…665) and the Send row
  (y 694…732, the extra rows being the cursor) inside the document, plus the bubble.

**What can and cannot be concluded about closing**

`[OBSERVED]` A single still can establish **that the popup is present** — which it is. It cannot
establish that anything closed.

`[INFERRED]` What the frame *does* support is that **Send has just been clicked and a navigation to
`https://www.tanktrouble.com/tellAFriendMail/` is in flight**, on three converging signals: the
pointer is on the button; the button is in a disabled rendering; and Edge is displaying the target
URL in its status bubble. In Edge Legacy that bubble appears for a hovered hyperlink or for an
in-progress navigation — a hovered `<input type="submit">` produces no bubble at all, so the bubble
is evidence of a navigation, not of hovering.

`[INFERRED]` The submit target is the popup's **own URL**, `/tellAFriendMail/`. So the form posts (or
gets) back to itself; there is no separate handler path such as `sendTellAFriend.php` visible.
*Falsifier:* if the Send control is an `<a>` styled as a button whose `href` is `/tellAFriendMail/`,
the same bubble appears without any form submission. The disabled-looking rendering argues against
that (anchors do not have a disabled state), but a still cannot close it.

`[UNCERTAIN]` **Whether the popup closes on send is not settled by this frame.** The only support for
it is the owner's filename plus the fact that this is the last frame he saved from the sequence
(17:20:57, 47 s after the previous one). Reasoning from "the recorder named the file *closes after
you click send*" and "no later frame exists" to "the popup closed" is an argument from the owner's
testimony and the capture order — **not** from the pixels. State it that way in any doc that cites
this, and keep the claim separable from the measurements.

**Links to the program**

- **S86 / LEDGER 226:** gives the canonical URL form `https://www.tanktrouble.com/tellAFriendMail/`
  (trailing slash, HTTPS, `www.`), which is what row 226's `index.php` convention-inference needs.
- **`srv/index.php:1179`:** the client-area measurement here is the one quoted in J3.

**What this does NOT show** — the response to the submit; a "message sent" confirmation; an error
state for a malformed address; the email that arrives; whether the window closed.

---

### `UI/tellafriendpopup.txt` — 700 bytes, saved 17:23:15

**Full content, verbatim** (the file is two runs of text with no newline between the first block's
sentences):

> To unlock the Sunglasses ("Advocate of Destruction") achievement in TankTrouble, send referral
> emails to 10 friends inviting them to create an account using the "Tell A Friend" option on the
> game's interface.Requirements & StepsAchievement Name: Sunglasses (Advocate of
> Destruction)Difficulty: HardAction Required: Use the "Tell A Friend" feature located on the right
> side of the game interface to invite 10 people/emails telling them to create an account.If you
> need help with other secret or difficult achievements in TankTrouble, let me know which item or
> trophy you are trying to unlock next!
>
> they get a link, from there and sign up, 10 friends and they sign up then you get silver
> sunglasses.

**Grading.** `[INFERRED]` The first block is **not a capture and not the owner's own writing**. The
"Requirements & Steps" scaffolding, the "Difficulty: Hard" label, the collapsed headings (missing
line breaks, so it was pasted out of a rendered chat/answer view) and the closing "If you need help
with other secret or difficult achievements … let me know which item or trophy you are trying to
unlock next!" are the signature of an LLM answer or a scraped guide page. Under the shared brief's
provenance rules this is **M2 at best and arguably weaker than M2** — it has no identifiable source.
The second sentence is the repo owner's own paraphrase in his own voice.

**What it claims about the referral mechanic**

1. Recipients receive **a link**.
2. They must **sign up** (create an account) — merely visiting is not enough.
3. The threshold is **10** friends who sign up.
4. The reward is the **Sunglasses / "Advocate of Destruction"** achievement, described as silver.
5. The feature is located on the **right side** of the interface.

**Cross-checks I can actually run**

- `[OBSERVED]` Claim 5 is **corroborated by the pixels**: the `Tell a Friend` box is in the right
  column in all three frames, and `srv/index.php:1167` places it in the `width: 120px; float: right`
  column opened at `:1090`.
- `[OBSERVED]` Claims 3 and 4 are **independently corroborated inside the same corpus** by
  `root/acheivements.txt` line 13:
  `Advocate of Destruction - Get 10 friends to sign up using "Tell a Friend"!`
  and by that file's reward list, which pairs `Advocate of Destruction` with **`Silver Glasses`**.
  That file is the achievements source analyst G works from — see [G-achievements.md](./G-achievements.md).
  `[UNCERTAIN]` the two disagree on the item's name: `tellafriendpopup.txt` says *"silver
  sunglasses"* / *"Sunglasses"*, `acheivements.txt` says **`Silver Glasses`**. Prefer the
  achievements file's string; both are wiki-grade.
- `[NOT VISIBLE]` Claims 1 and 2 — the link and the sign-up requirement — are **not testable from
  any frame here**. They describe the *email* and the *landing*, and this surface is only the
  composer.

**What would verify claims 1 and 2**

The two things that would settle them are both still stubs:

- **S22 — the `?r=` referral landing** (`srv/index.php:427`; `DEDUCE.md:152`), rated LOW.
- **S87 — `/spreadTheWord/`** (LEDGER 223; `srv/index.php:13837-13841`), rated LOW.

`[NOT VISIBLE]` **Neither frame contains a `?r=` URL.** I checked specifically:
- the only URL in the body copy is `www.TankTrouble.com`, rendered as underlined dark text with no
  query string;
- the address bar shows `tanktrouble.com/tellAFriendMail` in P1 and CS and is empty in P0;
- the status bubble in CS shows `https://www.tanktrouble.com/tellAFriendMail/` — the submit target,
  not a referral URL;
- no hover state exposes any `href`.

So **S22 gains nothing from this topic and stays WANTED**, and so does S87. What this topic *does*
give S22 is a narrowing: whatever `?r=` token the referral email carries, it is **not composed
client-side in this popup** — there is no visible field, hidden or otherwise, that would carry one,
and the sender never sees it. It must be minted server-side when the mail is generated. That is a
useful constraint for whoever eventually writes the handler.

---

## The parent page, as provenance (S11 and neighbours)

The three frames are also a decent capture of the 2017–2018 front page, seen around the popup.

`[OBSERVED]` **Right column, top to bottom:** `Need Help?` / `Check the FAQ` (black box) — `Victories`
table with rows `arielelcrack 1156`, `gyoker 1088`, `JessieTheTank 907`, `fastbomber 843`,
`SoccerKing10 837`, `pp95 700`, `Laika11116 692`, `14sdestroyer 637`, `hariskhan399 611`,
`tankandrewhe 537`, and `Weekly` / `Friends` tabs with **Weekly** selected — Facebook `Like` / `Share`
buttons — `Available on the App Store` — `GET IT ON Google play` — `Tell a Friend` — `Got Feedback?`.
That is `srv/index.php:1090-1195` in order — the `width: 120px; float: right` column opened at
`:1090`, `Need Help?` at `:1095`, `Check the FAQ` at `:1098`, the `Victories` header at `:1112`,
the Facebook like box at `:1160-1161`, `availableOnTheAppStore120.jpg` at `:1164`,
`getItOnGooglePlay.png` at `:1166`, `Tell a Friend` at `:1167`, `Got Feedback?` at `:1183`.

`[OBSERVED]` **The `Tell a Friend` box** — the trigger for this whole topic — is a black rounded box
with the white header `Tell a Friend` and, below it, two white stick figures: the left one holding a
telephone handset (visible cord) to a black open mouth, the right one with two black dot eyes and a
white speech balloon at the upper right containing a black tank silhouette. That is
`srv/images/tellAFriend.png`, LEDGER row 417, held **O** — so this frame *corroborates the held asset
in situ* rather than adding new bytes.

`[OBSERVED]` **`Got Feedback?` box, closed state** — bears on **S11**. Black header band with white
bold `Got Feedback?`; white body with grey centred copy laid out as six rendered lines:

```
Got ideas?
Found Bugs?
Urge to praise us
to the skies?
Then give us your
feedback
```

then a line-art envelope resting on a black rounded bar. That is exactly `srv/index.php:1187-1191`
(`Got ideas?<br/> Found Bugs?<br/> Urge to praise us to the skies?<br/> Then give us your feedback`
plus `images/envelope.jpg` at 72 × 29) wrapping inside the 120 px column.

`[NOT VISIBLE]` **The open state is not here.** S11 wants the in-page expanded form that existed
until (2018-04-22, 2018-05-23]; the box is never clicked in these frames. **S11 stays WANTED.** Note
also that the held occurrence at `srv/index.php:1183-1210` is the *late* variant — `openFeedback()`
at `:1199-1202` opens `https://beta.tanktrouble.com/#type=messages` rather than expanding in place —
and the closed box looks identical either way, so this capture cannot even tell which variant was
live. (`openFeedback()` is at `:1201-1205`, wired to the box at `:1207-1210`.)

`[OBSERVED]` **Left column:** Scrapyard odometer — green Dimitrium crystal box captioned
`Dimitrium has been found in the mazes!` — the red `OPEN BETA` / `Test online battles now!` box —
an empty `Log In` box (`?` help glyph, `Log In` header, `username` placeholder, a password field
showing 9 dots, a `Log in` button and a `Sign up` link) — a yellow custom-painted tank with a blue
flag and a green worm/snake motif — a user card headed `⊠ LaikaClone02` with `Exp. 13360` and, below,
a trophy glyph `1197 (0)` and a skull glyph `955`.

`[OBSERVED]` **Game stage:** tilted white menu cards reading `1` / `VS` on the left sliver and
`…YERS` on the right, with the watermark `version  4.0` at the lower right of the stage.

`[INFERRED]` **Cross-topic hand-off (not mine to write up):** the `LaikaClone02` card is direct
evidence for **S6** ("Logged-in user card in login sidebar … Score/rank/logout markup never
captured") and the simultaneous empty `Log In` box above it is evidence for **S7** (multi-user
stack). Both belong to topic E — `./E-front-page-chrome.md` — and I flag them
rather than claim them. The `OPEN BETA` box copy is also a divergence from the held
`srv/index.php:511`/`:550` strings and deserves its own note there.

---

## Consequences for the rebuild

### Confirmed

1. `[MEASURED]` **`srv/index.php:1179` is right about the geometry.** Client area 460.1 CSS px wide;
   ≥ 533.5–535.1 CSS px of content visible with the bottom edge outside frame. `width=460,height=535`
   holds. There are seven byte-identical occurrences of that line in the file
   (`1179, 2764, 5343, 11321, 13040, 14589, 16045`); this evidence validates all of them.
2. `[MEASURED]` **"no-scrollbar" (S86) is correct**, on three independent grounds: no scrollbar
   pixels at the right edge; the client width is the *undiminished* 460; total content height is
   ~493 CSS px inside a 535 px viewport.
3. `[OBSERVED]` **The route resolves and the popup is a genuine separate window** with its own title
   bar and border — `_blank` + sized features, as the source implies.
4. `[OBSERVED]` **Canonical URL:** `https://www.tanktrouble.com/tellAFriendMail/` with trailing
   slash. LEDGER 226's `srv/tellAFriendMail/index.php` (directory + convention-inferred index) is the
   right shape.
5. `[OBSERVED]` **`srv/images/tellAFriend.png` (LEDGER 417, O) is confirmed in situ** as the sidebar
   box art, and `srv/index.php:1167-1173`'s box markup reproduces what is on screen (header text,
   35 px content div, overflowing image).
6. `[OBSERVED]` **`srv/index.php:1184-1191`'s `Got Feedback?` closed-state copy is confirmed
   verbatim.**

### Contradicted — overhaul owed

Under [THE OVERHAUL RULE](../../standards/VISUAL-EVIDENCE-WANTED.md), invented M2/M3 pieces have zero authority
and are rewritten wholesale when evidence lands.

1. **`srv/tellAFriendMail/index.php` — LEDGER row 226, currently `M2`, "501 stub (milestone 1)".**
   A 501 stub is not a wrong drawing, it is *no* drawing, so strictly there is nothing to supersede —
   but the row's tier and note must both change, and the page must now be **written from this
   evidence, not invented**. Everything needed for a first pass is in §Transcription and §Layout:
   the title, the full copy, the three placeholders, the submit label, the 384 px centred graphic
   block, the justified 322 px text column, the 460 px viewport. What must be marked M2 (redrawn from
   footage) rather than O is the **artwork** — until `/tellAFriendMail/images/` is refetched.
   **A rewrite is owed, and it should be written once, complete, rather than stubbed again.**
2. **Any nascent assumption that the popup interpolates a recipient name.** Finding J2 kills it
   before it is coded. If any planning document, `DEDUCE.md` note or handler sketch anywhere in the
   tree describes `/tellAFriendMail/` as taking a name parameter or rendering a personalised
   greeting, that text is wrong and should be struck, not softened.
3. **`J-popup-send-pressed-still-open.png` must not be cited as "the popup closed".** If any doc records the
   close-on-send behaviour, it has to cite the owner's filename claim + capture order as its source,
   not the frame. The frame shows the opposite state (popup present, submit in flight).

### Still unknown / stays on the want-list

| Unknown | Why it matters | Status |
|---|---|---|
| **Server-side send handling** — GET vs POST, field names, the mail template, SMTP/`mail()` path | Without it the page is a dead form | stays WANTED |
| **Success state** — does the page re-render with a "sent" message, does the window `self.close()`, is there a redirect? | Determines whether the rebuild needs a second page state at all | stays WANTED |
| **Failure states** — empty field, malformed address, rate limit | `[NOT VISIBLE]` in every frame | stays WANTED |
| **The email that actually arrives** — subject, body, and crucially the referral link's form | The only thing that can resolve **S22** | stays WANTED |
| **`/tellAFriendMail/images/`** — `DEDUCE.md:155` says the directory has 13 paths incl. `images/` | Would turn the artwork from M2-redrawn to **O** | new want, see below |
| **Popup bottom edge** | Would close off `height=535` instead of confirming it to ±2 px | stays WANTED (cheap) |
| **`?r=` referral landing (S22)** | `[NOT VISIBLE]` here | stays **WANTED**, LOW |
| **`/spreadTheWord/` (S87)** | `[NOT VISIBLE]` here | stays **WANTED**, LOW |
| **Feedback box open state (S11)** | Only the closed state is captured | stays **WANTED**, MED |
| **Whether the placeholders are HTML5 `placeholder=` or era JS** | Byte-level difference in the rebuilt markup | new want |

### New wants to add

- **S86a — `/tellAFriendMail/images/` enumeration.** `DEDUCE.md:155` records 21 CDX 200s and
  "13 paths incl. `images/`". List them and refetch. The tank-on-ridge illustration, the maze paper
  and the `TANKTROUBLE.com` ink band are almost certainly among them, and recovering them promotes
  the whole page's artwork from M2 to **O**. Recoverability: **HIGH** — this is a CDX query plus
  `tools/fetch_missing.py`, not a footage hunt. *This is the single highest-value follow-up in this
  topic.*
- **S86b — `/tellAFriendMail/` post-submit state.** Footage trigger: someone fills the form and
  clicks Send with the recorder still rolling for 3–5 seconds afterwards. Answers close-vs-confirm,
  the success copy, and whether the URL changes. Recoverability: **LOW** (needs new footage).
- **S86c — the popup's own bottom edge.** Any frame whose crop includes the window's bottom border.
  Would convert `height=535` from "confirmed to ±2 px" to "closed". Recoverability: **LOW**, value
  small.
- **S22a — the referral email body.** An era screenshot of the mail a friend received. This, not any
  page capture, is what unlocks S22's `?r=` token format. Recoverability: **LOW**.

---

## Recommended edits to existing docs (not applied)

I have edited nothing. These are proposals.

### 1. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — S86

Change the status from an open want to **PARTIAL**, and rewrite the row's "what exists" column.
Proposed replacement:

```diff
-| S86 | **`/tellAFriendMail/` popup** | page-look | 460×535 no-scrollbar popup; 21 CDX 200s 2008-2018 | LEDGER 226; `srv/index.php:1179` | "Tell a Friend" clicked | LOW |
+| S86 | **`/tellAFriendMail/` popup** — **PARTIAL** | page-look | **Page rendered and fully transcribed** from 3 era frames (`manualevidence/UI/tellafriendmailpopup{,1}.png`, `J-popup-send-pressed-still-open.png`, capture window 2017-02-21…2018-12-18). Confirmed: client area 460.1 CSS px, no scrollbar, `<title>Tell a Friend`, `https://www.tanktrouble.com/tellAFriendMail/`, full copy, 3 placeholders (`name`/`your name`/`email`), Send button, 384px centred graphic. **Copy is NOT name-templated — the blanks are sender-filled `<input>`s** (frame diff). Still missing: send handler, success/failure states, the email sent, `/tellAFriendMail/images/` bytes, popup bottom edge | LEDGER 226; `srv/index.php:1179`; `manualevidence/J-tell-a-friend.md` | post-Send state; a frame including the window's bottom border | LOW (remaining) |
```

Rationale for **PARTIAL** rather than FETCHED/DONE: the page-look is recovered and the evidence is in
hand, but the *artwork bytes* are not, and none of the post-submit states are. Per the file's own
legend, PARTIAL = "some states held", which is exactly the situation.

### 2. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — S22 and S87

Leave both at **WANTED / LOW**, but add the negative result so the next analyst does not re-check
these frames:

```diff
 | S22 | **`?r=` referral landing** | flow | `?r=Link%20iframe/embed`, `/spreadTheWord/` source; on-screen effect unknown | `srv/index.php:427`; `DEDUCE.md:152` | Arrival via the banner inside an embedded portal copy | LOW |
+|     |  ↳ *checked and absent:* no `?r=` URL appears anywhere in the `/tellAFriendMail/` frames — body copy links plain `www.TankTrouble.com`, submit target is `/tellAFriendMail/` itself. The referral token is not composed sender-side (`manualevidence/J-tell-a-friend.md`). |
```

```diff
 | S87 | **`/spreadTheWord/`** | page-look | Stub; two banners held; page + `?r=` tracker copy unknown | LEDGER 223; `srv/index.php:13837-13841` | `?lab` banner section or direct visit | LOW |
+|     |  ↳ *checked and absent:* `/spreadTheWord/` is neither reached nor linked from the Tell-A-Friend popup. |
```

### 3. `docs/standards/VISUAL-EVIDENCE-WANTED.md` — S11

Keep **WANTED**. Add: *"closed state confirmed verbatim against `srv/index.php:1187-1191` by
`manualevidence/UI/J-popup-send-pressed-still-open.png`; the open state remains unseen, and the closed box
cannot distinguish the in-page-form variant from the `beta.tanktrouble.com` variant at `:1199`."*

### 4. New want-list rows

Add **S86a / S86b / S86c / S22a** as specified in §New wants to add. **S86a is the one to act on
first** — it is a CDX enumeration, not a footage hunt, and it is the difference between redrawing the
popup's artwork (M2) and serving the original bytes (O).

### 5. `LEDGER.tsv` row 226

Once the page is written from this evidence, the row should read something like:

```diff
-srv/tellAFriendMail/index.php	M2	—	written 2026-08-02	directory /tellAFriendMail/ observed in CDX; index filename convention-inferred	—	501 stub (milestone 1)
+srv/tellAFriendMail/index.php	M2	<sha256>	written from manual evidence 2026-08-04	directory /tellAFriendMail/ observed in CDX; index filename convention-inferred; page-look, copy and geometry from manualevidence/UI/tellafriendmailpopup{,1}.png + J-popup-send-pressed-still-open.png (era window 2017-02-21…2018-12-18) per manualevidence/J-tell-a-friend.md	tests/...	copy + layout evidence-pinned; ARTWORK still M2-redrawn pending /tellAFriendMail/images/ refetch; send handler + success/failure states still unknown
```

Per the shared brief's provenance rules and guide §6.5 this stays **M2** — it is derived from era
screen captures, never original bytes. Do not let the completeness of the transcription tempt anyone
into `O` or `O?`.

### 6. `DECISIONS.md`

Append a decision recording (a) that `/tellAFriendMail/` is being written from M2 manual evidence
rather than left as a 501 stub; (b) the explicit finding that the page carries **no server-side name
templating**, with the frame-diff numbers as the justification, so nobody re-litigates it later; and
(c) that the "closes on Send" behaviour rests on the repo owner's filename claim plus capture order,
**not** on any pixel, and must be labelled that way wherever it is relied on.

### 7. `DEDUCE.md`

Add to the era-dating notes: the front-page red sidebar box read **`OPEN BETA` / `Test online
battles now!`** at some point in `[2017-02-21, 2018-12-18]`, which is a **third** string for that
slot beyond the two the held `srv/index.php:511`/`:550` can produce. That is a genuine divergence
between the served page and the era page and belongs with topic E's front-page work.

---

## Method notes (so the numbers can be re-derived)

- All pixel work in Python 3 with PIL + numpy on the read-only originals under
  `/mnt/user-data/uploads/manualevidence/UI/`; images converted to `RGB` (the PNGs are `RGBA` with an
  opaque alpha).
- Frame alignment by exhaustive integer-offset SAD minimisation over a static 160 × 190 px region of
  the parent page; residuals reported above.
- Differencing via `PIL.ImageChops.difference` on the aligned overlap, thresholded at > 60/255 on the
  per-pixel channel maximum, then run-length grouped by row and column to give the cluster tables.
- Scale from the `#ff0000` run width of the beta box (`srv/index.php:510`, `width: 120px`),
  cross-checked against the popup client width vs `width=460` (`srv/index.php:1179`).
- Glyph and box geometry by thresholded ink-extent scans; colours by exact-value histograms and
  order statistics over stated rectangles, never by eye.
- Texture pitch by mean-removed 1-D autocorrelation along each axis of a text-free patch.
- Font sizes derived from Arial's cap height (0.716 em), ascender (0.728 em) and descender (0.212 em);
  all such derivations are tagged `[UNCERTAIN]` because the family is inferred from glyph shape, not
  known.
