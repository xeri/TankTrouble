# Visual evidence — rank milestones, league cards and tank rank insignia

> Analysis of 6 assigned evidence files under `manualevidence/`, plus 7
> cross-referenced files assigned to topic F (cited, never claimed).
> Provenance: M2 at best (era footage / wiki-derived screen captures) — never O.
> See [the shared index](./INDEX.md) · [VISUAL-EVIDENCE-WANTED.md](../../standards/VISUAL-EVIDENCE-WANTED.md)
> · [mazecreator-visual-spec.md](../../standards/MAZECREATOR-VISUAL-SPEC.md)
> · [README.md](../../../README.md) · [DEDUCE.md](../../../DEDUCE.md) · [DECISIONS.md](../../../DECISIONS.md)

---

## Headline verdict, stated first

**The twelve-rank ladder in `ranks.txt` and the three league cards are
post-era. They describe the HTML5 "TankTrouble Online" client, not the
2017–2018 PHP/Flash site this project reconstructs. Nothing in this topic
may be adopted into `srv/`.**

Five independent lines of evidence agree, and none dissents. They are set
out in full in §"The provenance question" below. In one line each:

1. `ranks.txt`'s own first sentence scopes the feature to "TankTrouble
   Online" — which in the classic site's own news vocabulary means the
   separate BETA/HTML5 product at `beta.tanktrouble.com`, not the classic
   site (`srv/index.php:6988-6990`).
2. Zero of the twelve rank names occurs anywhere in the era
   `srv/index.php` (812 KB, all seven route copies). Nor does `\branked\b`,
   `League`, `matchmaking`, `leaderboard`, `\belo\b`, or `tank info box`
   (all word-bounded counts = 0).
3. The classic site's actual skill metric is **experience**, with a
   published formula (`srv/index.php:9479`), and its only rank surface is
   the `?lab` link **"Tank Rank by Experience"** (`srv/index.php:13848`).
   Experience ≠ a 12-step win/loss ladder.
4. The cards are typeset in the custom rounded TankTrouble display face.
   `srv/index.php` contains **zero** `@font-face` rules and **zero** `.ttf`
   references; its only inline `font-family` is `Courier` (×10). The news
   item at `srv/index.php:6657` records the "custom TankTrouble font" being
   deployed **to Online BETA** on 2016-05-25 — it never reached the classic
   site.
5. A frame in the same capture run (`Game/F-html5-generation-contrast-case.png`, topic F's file)
   shows the **modern HTML5 site** carrying a sidebar box reading
   **"Tank Rank has been Deployed"** with a 3-chevron/3-star insignia, and
   a modern HUD in which each player's name is followed by a small gold
   chevron. That is the system `ranks.txt` describes, on the platform it
   belongs to.

What would overturn this: an in-era (2017–2018) capture of
`tanktrouble.com` — a CDX row, a WARC body, a dated video frame — showing
any of the twelve names, or any chevron/star insignia, on the classic
Flash site. `/tankRanks/` (LEDGER row 225) is the one place it could
hide, and its content remains completely unknown (86 CDX 200s, all
2010-2015, zero bodies). **If** `/tankRanks/` turns out to have contained
this ladder, the verdict flips — but the 2010-2015 CDX window and the
"by Experience" link text both argue against it.

---

## Scope and provenance

### The six assigned files, and what they actually are

The task brief describes three of my large PNGs as league cards. **One of
them is not.** `Game/H-classic-gameplay-1p-vs-laika.png` is a classic Flash gameplay frame,
not a rank card. Recording that correction is part of the finding.

| File | Size | Capture time (NZST) | What it actually is |
|---|---|---|---|
| `Game/H-classic-gameplay-1p-vs-laika.png` | 1293×720 | 16:24:11 | **Classic Flash `TankTrouble_v4.0.swf` gameplay frame** (1-player vs Laika). Not a league card. |
| `Game/H-video-title-card-tank-trouble-ranks.png` | 1270×686 | 16:32:32 | Title/thumbnail card, "Tank Trouble Ranks" |
| `Game/H-league-card-soldier.png` | 1267×696 | 16:34:37 | League card — **"The Soldier league"** |
| `Game/H-hud-crop-score-10-with-transient.png` | 103×55 | 16:41:18 | Crop of a **classic** HUD: green tank + score `10`, plus a grey transient |
| `Game/H-hud-crop-score-10-clean.png` | 101×53 | 16:41:25 | Same crop, same score, transient gone |
| `Game/ranks.txt` | 974 B | 17:46:27 | Wiki-derived text: the 12-milestone ladder |

Capture times are from `ASSIGNMENTS.md` (the owner's original mtimes). The
staged copies here all carry the staging mtime 2026-08-04 05:53, which is
useless; I used the assignment list, as the brief instructs.

### The claimed duplicate does not exist in this staging

The task states that a byte-identical copy of `Game/H-classic-gameplay-1p-vs-laika.png` also
sits at `UI/H-classic-gameplay-1p-vs-laika-duplicate.png`, and asks me to hash both and record the
duplication.

`[MEASURED]` **There is no such file.** `find /mnt/user-data/uploads -iname
"*345B2DAE*"` returns exactly one path:
`manualevidence/Game/H-classic-gameplay-1p-vs-laika.png`.
`UI/` holds 76 files and none of them is that GUID.

`[MEASURED]` I then sha256'd **every** file in the corpus
(`find . -type f -exec sha256sum {} \; | sort | awk '{print $1}' | uniq -d`)
and got **zero** repeated digests. The staged corpus contains **101 files
(24 `Game/` + 76 `UI/` + 1 `root/acheivements.txt`) and no duplicates at
all.**

`[INFERRED]` Either the duplicate existed on the owner's disk and was
de-duplicated during staging, or the claim was a mis-recollection. Either
way, **for the purpose of counting this corpus there is no duplication to
subtract.** Falsifiable by listing the owner's own `UI/` folder.

sha256 of the file itself, for the ledger:
`85ed945afa1b7f61401e2d0d41591218db31116b7b9fc0484e74b55d4c9fdc5a`.

Direct links to the evidence, from this document's location
(`manualevidence/`):
[`H-classic-gameplay-1p-vs-laika.png`](./Game/H-classic-gameplay-1p-vs-laika.png) ·
[`H-video-title-card-tank-trouble-ranks.png`](./Game/H-video-title-card-tank-trouble-ranks.png) ·
[`H-league-card-soldier.png`](./Game/H-league-card-soldier.png) ·
[`H-hud-crop-score-10-with-transient.png`](./Game/H-hud-crop-score-10-with-transient.png) ·
[`H-hud-crop-score-10-clean.png`](./Game/H-hud-crop-score-10-clean.png) ·
[`ranks.txt`](./Game/ranks.txt)

### Seven files I did not own but had to read

Deliverables 1 and 2 ask for **all twelve** rank names and **all twelve**
insignia. My assignment contains one league card, which covers four. The
other eight are in files assigned to topic F. I examined them **only** to
complete the ladder and to settle the era question, and I flag every claim
drawn from them. They are not mine to write up.

| File (topic F) | Capture | Why I looked |
|---|---|---|
| `Game/F-video-card-beginner-league.png` | 16:34:05 | beginner league card, title mid-fade-in |
| `Game/F-video-card-beginner-league-caption.png` | 16:34:19 | beginner league card, title full |
| `Game/F-video-card-scientist-league.png` | 16:36:14 | Scientist league card, no title |
| `Game/F-video-card-scientist-league-caption.png` | 16:36:31 | Scientist league card, title full |
| `Game/F-html5-generation-contrast-case.png` | 16:37:38 | modern HTML5 site: "Tank Rank has been Deployed" + rank chevrons in the HUD |
| `Game/F-gameplay-maze-61-crates.png` | 16:24:50 | classic 2-player HUD — the layout my two tiny crops match |
| `Game/F-gameplay-three-guests-maze-crop.png` | 16:22:54 | classic 3-player HUD — same |
| `Game/F-gameplay-2015-page-beta-sidebar.png` | 16:23:14 | classic sidebar — only to place the session in sequence |

### Reconstructed capture sequence

`[INFERRED]` Ordering all thirteen `Game/*.png` by the owner's mtimes gives
a coherent session. I am explicitly reconstructing a sequence from capture
order, as the brief permits:

```
16:22:54  F-gameplay-three-guests-maze-crop.png  classic v4.0, 3 players, scores 28 / 29 / 21
16:23:14  F-gameplay-2015-page-beta-sidebar.png  classic sidebar: "Log in / Sign up", "Access Online BETA /
                      Beta access required", "Shop Open / Get BETA access here!",
                      Visits box (42315370 since 2007-12-16)
16:24:11  H-classic-gameplay-1p-vs-laika.png  classic v4.0, 1 player vs Laika, scores 24 / 1     ← mine
16:24:50  F-gameplay-maze-61-crates.png  classic v4.0, 2 players, scores 1 / 0
   …
16:32:32  H-video-title-card-tank-trouble-ranks.png   title card                                         ← mine
16:34:05  F-video-card-beginner-league.png  beginner card, league title at ~5-12 % opacity
16:34:19  F-video-card-beginner-league-caption.png  beginner card, league title opaque
16:34:37  H-league-card-soldier.png  Soldier card, league title opaque                  ← mine
16:36:14  F-video-card-scientist-league.png  Scientist card, no league title
16:36:31  F-video-card-scientist-league-caption.png  Scientist card, league title opaque
16:37:38  F-html5-generation-contrast-case.png  MODERN HTML5 site, "Tank Rank has been Deployed"
16:41:18  H-hud-crop-score-10-with-transient.png  tiny crop: classic HUD tank + score 10 + grey blob  ← mine
16:41:25  H-hud-crop-score-10-clean.png  tiny crop: same, blob gone                          ← mine
17:46:27  ranks.txt   wiki text pasted                                    ← mine
```

`[INFERRED]` Two readings of that sequence, both supported:

* 16:34:05 → 16:36:31 is one pass through a **video** presenting the three
  leagues. For two of the three leagues the owner grabbed a
  before-the-title and an after-the-title frame; for the Soldier league he
  grabbed only the after. That before/after pairing only makes sense if
  the league title **animates in** — which the measurement in
  §`F-video-card-beginner-league.png` confirms.
* 16:41:18 → 16:41:25 is a deliberate two-frame isolation. Something
  changed between the two frames and the owner wanted it pinned. The diff
  says exactly what changed (§"The two tiny crops").

`[OBSERVED]` The 16:22–16:24 classic frames and the 16:34–16:37 rank
frames are **not the same source**. The classic frames are
`version 4.0` Flash captures; `F-html5-generation-contrast-case.png` is the modern HTML5 site with
App Store/Google Play badges and a War Thunder ad. The brief's rule 4
applies: do not merge them into one imagined session.

---

## Findings at a glance

| # | Finding | Confidence | Bears on | Supersedes? |
|---|---|---|---|---|
| H1 | The 12-milestone ladder + 3 league cards are **post-era (HTML5 "TankTrouble Online")**, not 2017–2018 classic | `[INFERRED]`, 5 converging lines, none dissenting | S83, S114, DECISIONS 2026-08-03 `/tankRanks/` | Nothing. It **blocks** an adoption that would have been a forgery |
| H2 | The classic era's metric is **experience**, formula published in-page; the only rank surface is the `?lab` link "Tank Rank by Experience" → `window.open('tankRanks',…)` | `[MEASURED]` grep of `srv/index.php:9479`, `:13845-13856` | S83 | — |
| H3 | Ladder reconciles **exactly**: 12 milestones = 4+4+4 card slots, no gap, no duplicate | `[MEASURED]` | — | — |
| H4 | Insignia grammar is fully systematic: **chevrons = league (1/2/3), stars = position in league (0/1/2/3)** | `[OBSERVED]` all 12 | — | — |
| H5 | `H-classic-gameplay-1p-vs-laika.png` is **not** a league card — it is a classic `v4.0` gameplay frame, and its copyright reads **2007 – 2015** where the era page reads **2007 – 2018** (`srv/index.php:329`) | `[OBSERVED]`/`[MEASURED]` | S105 | Corrects the task brief |
| H6 | `H-classic-gameplay-1p-vs-laika.png` is **anamorphically stretched ≈1.50× horizontally**; do not measure stage geometry from it without de-stretching | `[MEASURED]` maze lattice 115.0 px h vs 76.8 px v | any future use of this frame | — |
| H7 | The two tiny crops are **classic HUD score counters, not rank icons**: green tank + score `10`, right-hand player slot | `[MEASURED]` vs `F-gameplay-maze-61-crates.png`/`F-gameplay-three-guests-maze-crop.png` | S114 | — |
| H8 | The crops differ **only** by a soft neutral-grey transient (~29×23 px) over the score; the tank and the digits are identical to sub-pixel | `[MEASURED]` ImageChops diff after (−3,−3) alignment | — | — |
| H9 | The modern HUD **does** show a rank chevron — after the **username**, on a line above and distinct from the `kills • deaths` numerals | `[OBSERVED]` `F-html5-generation-contrast-case.png` (topic F) | S114 | — |
| H10 | `H-video-title-card-tank-trouble-ranks.png`'s tank is the **same tank design** as the classic HUD tank, at much higher fidelity, with an inverted track/wheel value structure | `[MEASURED]` silhouette overlay; `[UNCERTAIN]` on redraw-vs-resolution | — | — |
| H11 | `2.000 / 1.500 / 1.000` are **European dot-thousands** = 2000/1500/1000, not literal 2.0 | `[INFERRED]` monotonicity; studio is Danish | — | — |
| H12 | The league title **animates in** over the finished 2×2 grid | `[MEASURED]` ghost at ~5-12 % opacity in `F-video-card-beginner-league.png` | — | — |
| H13 | **No duplicate files anywhere in the 101-file corpus** — the claimed `UI/H-classic-gameplay-1p-vs-laika-duplicate.png` twin is absent | `[MEASURED]` sha256 of every file | corpus inventory | Corrects the task brief |

---

## File-by-file analysis

### `Game/ranks.txt` (974 bytes, ASCII, CRLF, captured 17:46:27)

sha256 `98ae9ebbf777a6316b3f1ef1a9efcc49bf163573977eede17a49c956ad800a09`

**Filename claim (repo owner):** none in the filename; but the file's own
closing paragraph is the owner's claim and is quoted in full below.

#### What it contains — verbatim, byte-exact

`[OBSERVED]` The file opens with a blank CRLF, then:

```
Ranks
Sign In to Save
Edit
```

`[OBSERVED]` "Sign In to Save" and "Edit" are **wiki editor chrome**, not
site copy. Under guide §6.5 this alone caps the whole file at **M2, never
O**, and it means the wording is a *fan's* description of the feature, not
the developer's.

`[OBSERVED]` Body paragraphs, verbatim (line breaks as in file):

> Ranks is the skill measuring system in TankTrouble Online. Rank icons are
> displayed on tanks when in a ranked match. A more detailed look of a
> player's rank is shown when you open their tank info box. There are
> twelve rank milestones in total.

> Rank is subtracted from your profile if you lose in a ranked match. You
> earn rank by winning. If you have zero rank on your account, you will
> still distribute one rank point on loss. If you leave a match before it
> ends and there are no winners, rank will be subtracted regardless.

`[OBSERVED]` Then the heading `Rank Milestones` and the ladder.

#### The ladder, transcribed exactly, with byte-level separators

`[MEASURED]` From `od -c`: every row is `<threshold>` **SPACE** **TAB**
`<name>` CRLF. The final row additionally has a **trailing space** after
`Dog Food`, and the file ends **without** a trailing newline.

| # (ascending) | Threshold as written | Name as written | Byte form of the row |
|---:|---|---|---|
| 12 | `2.000` | `Mad Scientist` | `2 . 0 0 0 SP TAB M a d SP S c i e n t i s t CR LF` |
| 11 | `1.500` | `Lead Scientist` | `1 . 5 0 0 SP TAB …` |
| 10 | `1.000` | `Scientist` | `1 . 0 0 0 SP TAB …` |
| 9 | `500` | `Jr. Scientist` | `5 0 0 SP TAB …` |
| 8 | `250` | `Commander` | `2 5 0 SP TAB …` |
| 7 | `150` | `Captain` | `1 5 0 SP TAB …` |
| 6 | `100` | `Sergeant` | `1 0 0 SP TAB …` |
| 5 | `50` | `Cadet` | `5 0 SP TAB …` |
| 4 | `25` | `Scavenger` | `2 5 SP TAB …` |
| 3 | `10` | `Intern` | `1 0 SP TAB …` |
| 2 | `5` | `Lab Rat` | `5 SP TAB …` |
| 1 | `Rank 0` | `Dog Food` | `R a n k SP 0 SP TAB D o g SP F o o d SP CR LF` |

`[OBSERVED]` The file lists them **descending** (Mad Scientist first).
Note `Jr. Scientist` carries a full stop; `Rank 0` is a word, not a bare
`0`.

#### The `2.000` question — European thousands, decisively

`[INFERRED]` `2.000` is **two thousand**, written with a European (dot)
thousands separator. Reasoning: the sequence must be monotone increasing
from `Rank 0` upward, and it is —
5, 10, 25, 50, 100, 150, 250, 500, **1000, 1500, 2000** — only if the
dotted values are thousands. Read literally as decimals they would be
2.0, 1.5, 1.0, which would place the three highest ranks **below** Lab Rat
at 5. Falsifiable by any capture showing a four-digit rank score.

`[OBSERVED]` Corroborating, not proving: the studio is Danish, and Danish
uses `.` as the thousands separator. The classic site's own copyright
credit (visible in `H-classic-gameplay-1p-vs-laika.png`, see below) names Mads Purup, and
`srv/index.php:6802` gives the address "Mejlgade 43A 8000 Aarhus Denmark".
`[UNCERTAIN]` whether the dots came from the game UI or from the wiki
editor's own habit — the wiki chrome means either is possible.

#### The owner's caveat, verbatim

The file ends:

> i dont know if these ranks were in the original tank trouble, not the
> beta revamp where tank models are 3d with full multiplayer support.
> probably not multiplayer, but online accounts local play.

`[OBSERVED]` This is the right doubt and it is correct. See §"The
provenance question". One correction to the owner's own framing: the
evidence points at the **HTML5/BETA generation**, which is the "beta
revamp" he suspects — not at the classic site. His instinct was right.

#### Internal claims tested against pixels

| Claim in `ranks.txt` | Verdict |
|---|---|
| "There are twelve rank milestones in total." | `[MEASURED]` **Corroborated.** 12 rows; and 3 cards × 4 cells = 12 named slots that match one-for-one. |
| "Rank icons are displayed on tanks when in a ranked match." | `[OBSERVED]` **Corroborated for the modern client only** — `F-html5-generation-contrast-case.png` shows a small gold chevron after each player's username in the HUD. **Not corroborated for the classic client**: my two tiny crops show a score, not an insignia (§"The two tiny crops"). |
| "A more detailed look of a player's rank is shown when you open their tank info box." | `[NOT VISIBLE]` No frame in the corpus shows a tank info box. `[MEASURED]` The string "info box"/"infobox"/"tankInfo" does not occur in `srv/index.php` at all — the classic site has no such element (its nearest analogue is the usertrail hover card, S4, `srv/index.php:1301-1362`). |
| "Rank is subtracted … if you lose", "you will still distribute one rank point on loss" | `[NOT VISIBLE]` Pure behaviour; no frame can show it. Note "distribute" is odd phrasing — a fan's paraphrase, not developer copy. |

**Links to the program.** Bears on **S83** (`/tankRanks/` popup) and
**S114** ("ranks surfaced outside lab"). Contradicts nothing in `srv/`,
because `srv/` says nothing about a ladder. **What this does NOT show:**
any evidence at all that the ladder existed on the classic site.

---

### `Game/H-classic-gameplay-1p-vs-laika.png` (1293×720, captured 16:24:11)  *(was `{345B2DAE-524B-4F4B-9505-42E8DDE5EC8B}.png`)*

sha256 `85ed945afa1b7f61401e2d0d41591218db31116b7b9fc0484e74b55d4c9fdc5a` ·
RGBA · pHYs 3779 px/m (≈96 dpi) · gamma 0.45455 · 18 347 distinct RGB values

**Task brief's claim:** "may be one of the three league cards".
**Verdict: contradicted.** This is a classic Flash gameplay frame.

#### What is drawn

`[OBSERVED]` Top two-thirds: the `TankTrouble_v4.0.swf` game stage — a
white maze floor bounded by a mid-grey wall lattice, with ten
grey-bordered white rectangles (closed wall boxes) laid out 5 across × 2
down inside an 11-column × 5-row wall lattice.

`[OBSERVED]` In the maze: an orange top-down tank sprite near centre; a
dark top-down tank sprite at top right; several small black dots
(projectiles); a small hollow circle at centre.

`[OBSERVED]` Bottom third — the classic HUD band:

* far left: a **gear** icon and a **speaker** icon, stacked;
* left player: a 3/4-perspective **orange tank** wearing two black
  round "mouse-ear" accessories and a white flag accessory bearing a red
  "no-mouse" prohibition symbol; a pale bone-shaped decal across the hull;
  name label `_-Death-_` beneath; score **`24`** to its **right**;
* centre: a grey **`+`** glyph, x[723,760) y[497,523);
* right player: **Laika** — a grey dog with red eyes and a red/blue
  scarf, seated on a black tank chassis; name label `Laika` beneath;
  score **`1`** to its **left**;
* far right, in pale grey: `587` / `by _-death-_` (maze number and
  author) and `version   4.0` with wide letter-spacing;
* bottom centre, two lines of grey page text (see below).

#### Measurements

`[MEASURED]` Connected-component analysis of dark ink in the HUD band
(`scipy.ndimage.label`, luminance < 190, rows 440-640):

| Element | bbox | w × h |
|---|---|---|
| score `2` | x[411,428) y[560,575) | 17 × 15 |
| score `4` | x[431,450) y[560,575) | 19 × 15 |
| score `1` (Laika) | x[858,870) y[560,575) | 12 × 15 |
| centre `+` | x[723,760) y[497,523) | 37 × 26 |
| `L` of "Laika" | x[928,939) y[585,597) | 11 × 12 |
| `a` of "Laika" | x[941,952) y[588,597) | 11 × 9 |

`[MEASURED]` Score digit **cap height = 15 px**; digit pitch 20 px
(`2` starts 411, `4` starts 431). Name-label ascender 12 px, x-height 9 px.

`[MEASURED]` Score ink is **neutral grey, not black**. Over the 295 ink
pixels of `24` (luminance < 170 inside x[411,450) y[560,575)):
**mean `#717171`, darkest pixel `#343434`**. Individual samples along the
antialiased edges: `(151,151,149)`, `(134,133,132)`, `(110,110,107)`,
`(80,80,77)`, `(72,73,70)` — grey at every level, never black, never tinted.

`[MEASURED]` **Maze lattice.** Vertical wall runs at row 100/140/300 are at
x = 5, 121, 234, 350, 463, 581, 694, 810, 923, 1039, 1154, 1270, each
**12–13 px** wide. Successive gaps: 116, 113, 116, 113, 118, 113, 116,
113, 116, 115 → **mean pitch 114.9 px (sd ≈ 1.8)**.
Horizontal wall runs down column 650 are at y = 13, 90, 165, 243, 317
(+ ≈397), each **7–8 px** tall. Gaps: 77, 75, 78, 74, 80 →
**mean pitch 76.8 px**.

`[MEASURED]` **This frame is anamorphically stretched.**
115.0 / 76.8 = **1.497**. Wall stroke 12.4 px horizontal vs ≈8 px vertical
= 1.55. Cross-check against the classic frames that topic F holds:
`F-gameplay-maze-61-crates.png` has wall runs **6–7 px in both axes** and horizontal cell
pitch 68.7 px; `F-gameplay-three-guests-maze-crop.png` has 6–7 px runs and pitch 65.8 px. TankTrouble
maze cells are square, so the 1.5:1 in `H-classic-gameplay-1p-vs-laika.png` is a display artefact
(4:3 footage stretched to 16:9, or an anamorphic re-encode), not geometry.
**Anyone measuring stage constants from this frame must divide x by ≈1.50
first.**

`[INFERRED]` If the SWF stage top maps to capture y ≈ 0 — the page places
`#TankTrouble` at `top:60px` and `#gameCopyright` at `top:550px`
(`srv/index.php:325,328`), i.e. exactly 490 px apart, and the copyright
text top sits at capture y ≈ 662 — then the vertical scale is
662/490 ≈ 1.35 and the horizontal is 1.35 × 1.497 ≈ 2.02. Both give
**cell ≈ 57 stage px** (76.8/1.35 = 56.9; 114.9/2.02 = 56.9). That
agreement is the check, not the assumption. Falsified if the capture is
cropped vertically anywhere other than the SWF top edge — which I cannot
rule out, so I report it as inferred and not as a constant.

#### The dating evidence: `2007 – 2015` and a second credit line

`[OBSERVED]` Bottom-centre, in grey, two lines:

```
Copyright www.purup.com 2007 – 2015
Design: Mads Purup, Programming: Brian Bunch Christensen, Server: Søren Boll Overgaard
```

`[MEASURED]` The era page carries **only the first line**, and with a
different year:

```
srv/index.php:328  <div class="text small gray" id="gameCopyright" style="… top: 550px;">
srv/index.php:329    Copyright <a href="http://www.purup.com" …>www.purup.com</a> 2007 &ndash; 2018
```

`[MEASURED]` `grep -o "2007 &ndash; [0-9]*"` over all 812 KB returns
exactly one distinct value: `2007 &ndash; 2018`. `grep -in "Design:"`,
`"Mads"`, `"Programming"`, `"Overgaard"` over `srv/index.php` all return
**zero hits**.

`[INFERRED]` Therefore this frame is **out of era**: it comes from a
period when the copyright range ended 2015 and a second credit line was
still present. Both had gone by the era-final capture
(`archive/commoncrawl/warc-bodies/20181218_www.tanktrouble.com_.txt`, the
`@O` source fenced at `srv/index.php:320`). Best estimate: **2015, or the
early part of 2016 before the year was bumped.** Falsifiable by any dated
capture showing "2007 – 2015" later than that.

`[OBSERVED]` The `version 4.0` watermark is consistent with
`includes/TankTrouble_v4.0.swf` (`srv/index.php:404`), which the era page
also embeds — so the *build* is era-compatible even though the *page* is
not. The frame is useful for HUD anatomy and useless for dating the era.

#### Links to the program

* `srv/index.php:404` — `new SWFObject("includes/TankTrouble_v4.0.swf", "TankTroubleGame", "712", "490", "8", "#ffffff")`. **This frame confirms the 712×490 stage is the thing being rendered** and gives the first look at the in-stage HUD row that no held byte describes.
* `srv/index.php:328-330` — `#gameCopyright`. **This frame contradicts the era text** (2015 vs 2018) and reveals a second credit line that the era page dropped. That is a datable page-chrome change nobody had pinned; it belongs to **S105** (frozen live regions / formatting constancy) and to the DECISIONS "annotation pass" family of date-window narrowings.
* **Rank content: `[NOT VISIBLE]`.** There is no chevron, no star, no insignia, no league, and no rank word anywhere in this frame. The only per-player numeral is the round score.

**What this does NOT show.** Nothing about ranks. It does not show the
left sidebar, the nav strip, or the page above the stage, so it cannot
date the page any more tightly than the copyright line does.

---

### `Game/H-league-card-soldier.png` (1267×696, captured 16:34:37) — "The Soldier league"  *(was `{3E6BCAF8-943C-4431-8340-49370DDF366D}.png`)*

sha256 `4e638ee9dc4d036c3fd18fb756363c906b8fee0f101066bf3defc34367dbb485` ·
RGBA · ≈96 dpi · 72 809 distinct RGB values

#### What is drawn

`[OBSERVED]` A 2×2 grid of pale-blue cells inside a solid dusty-rose
border, divided by heavy black rules. Each cell holds a gold chevron/star
insignia above a rank name in a white outlined display face. A blue league
title is superimposed across the horizontal rule, straddling both halves.

`[OBSERVED]` Text, **verbatim, casing exact**:

| Cell | Text |
|---|---|
| top-left | `Cadet` |
| top-right | `Sergeant` |
| bottom-left | `Captain` |
| bottom-right | `Commander` |
| centre overlay | `The Soldier league` |

`[OBSERVED]` Note the casing of the title: capital `S` on *Soldier*,
**lower-case `l` on *league***. The sibling cards use
`The beginner league` (lower-case `b`, lower-case `l`) and
`The Scientist League` (capital `S`, **capital `L`**). The three titles
are mutually inconsistent. That inconsistency is a fingerprint of
hand-authored motion-graphics text, not of a templated game UI, and it is
worth quoting exactly if this ever gets cited.

#### Measurements — frame and grid

`[MEASURED]` Colours (single-pixel samples, hex printed by the script):

| Element | Value | Where sampled |
|---|---|---|
| Outer border | `#ba678c` | (2,2), (694,1264), and every margin sample |
| Cell ground | `#e8f3f9` | (350,35), (350,1232), (40,600) |
| Divider rules | `#000000`–`#000103` | x=639 at y=100/200/400/600 |

`[MEASURED]` Border thickness is **asymmetric**: left 22 px, top 29 px,
right 15 px, bottom 23 px — i.e. this is a **crop of a larger frame**, not
the card's own edge.

`[MEASURED]` Divider geometry, by column/row darkness fraction (> 80 % of
the axis dark):
vertical rule occupies **x 635–643 (9 px)**;
horizontal rule occupies **y 327–339 (13 px)**.
Sibling cards agree: 9–10 px vertical, 13–14 px horizontal.

`[MEASURED]` That 9 vs 13 is **not** an aspect artefact. A five-pointed
star's bounding box has aspect 1.0515; the Captain left star measures
**39 × 39 px (aspect 1.000)**, and the `o` counters in "Dog Food" on the
sibling card measure 44×48 and 45×48 (0.92). The cards are isotropic to
within ≈5 %. The rules are simply drawn at different weights.

#### Measurements — the insignia

`[OBSERVED]` All four devices share one construction: a **solid black
chevron plaque** carrying **gold chevron bars** across its upper part, with
**gold stars** seated in the notch below.

`[MEASURED]` Gold-mask connected components (mask:
`r>150 & g>110 & b<120 & r−b>70 & g−b>40`), per cell:

| Cell / rank | Chevron bars | Star components | Total gold bbox |
|---|---|---|---|
| Cadet | 2 — x[276,372) y[68,104) and x[277,372) y[93,132) | **0** | x[276,371] y[68,131] = 96 × 64 |
| Sergeant | 2 — x[912,1009) y[66,104), x[912,1008) y[94,132) | **1** — x[941,979) y[123,159), 38×36, centred | x[912,1008] y[66,158] = 97 × 93 |
| Captain | 2 — x[279,376) y[380,417), x[279,376) y[407,445) | **2** — x[282,321) y[448,487) 39×39 and x[333,373) y[450,484) 40×34, side by side, symmetric about the axis | x[279,375] y[380,486] = 97 × 107 |
| Commander | 2 — x[918,1013) y[382,420), x[917,1013) y[409,447) | **3** — centre x[950,983) y[438,472) sits **higher**; flanks x[913,949) y[453,486) and x[983,1017) y[454,485) sit lower | x[913,1016] y[382,485] = 104 × 104 |

`[OBSERVED]` **Chevron count is constant at 2 across the whole Soldier
league.** The star count is what changes: 0 → 1 → 2 → 3.

`[MEASURED]` Chevron bar structure, from a vertical transect down the apex
at x = 323:

```
y 60–66   black outline           #130705 … #5f5631   (≈7 px)
y 67–79   gold bar 1              #f2dd8c #f5d76b #ffca45 #fdc437 #ffc73d #efc86f  (13 px)
y 80–92   black separator         #4a3609 … #090d11 … #100e00  (13 px)
y 93–106  gold bar 2              #958846 #d0b243 #ffdd4f #ffc637 #f7c436 #f9cd5a  (14 px)
y 107–114 black outline
```

`[MEASURED]` **Gold, for redrawing.** Over all 13 231 gold pixels on this
card: mean `#dbb541`, p10 `#ae9330`, **median `#e1b840`**, p90 `#fad157`,
min `#976f06`, max `#fff177`. The bar reads as a soft vertical bevel:
a lighter rim (≈`#ffdd4f` / `#f2dd8c`) into a saturated core
(≈**`#ffc637`**) into a dark toe (≈`#976f00`).
The sibling cards give the same numbers — median `#e4bc41` (beginner),
`#e1b740` (Scientist) — so **one gold serves all twelve insignia**.

`[MEASURED]` **Star gold** (Captain left star): horizontal transect core
`#ffcf3b … #ffd94a`; vertical transect core `#ffc73a`, top rim `#ffe667`.
Same palette as the chevrons; the star is not a different gold.

`[MEASURED]` **The coloured halo.** Each device sits on a soft radial glow
whose hue equals the card's border colour. Transect leftwards from the
Cadet device at y = 99: `#b68a9c` immediately outside the black outline,
then a monotone ramp `#bd8fa4 → #c091a9 → #cda0b6 → #d5b7cb → #dcd3e0 →
#e1e3ec` reaching the `#e8f3f9` ground about **32 px** out.

Halo peaks and radii across all three cards `[MEASURED]`:

| Card | Border | Cell ground | Halo peak | Fade distance |
|---|---|---|---|---|
| beginner | `#a178af` | `#e8f3f9` | `#a690ac` | ≈22–26 px |
| Soldier | `#ba678c` | `#e8f3f9` | `#b68a9c` | ≈32 px |
| Scientist | `#e94e36` | `#a3dbcc` | `#d56b63` | ≈45 px |

`[UNCERTAIN]` The halo is *not* the border colour at a single alpha over
the ground — solving `#b68a9c = α·#ba678c + (1−α)·#e8f3f9` gives
inconsistent per-channel α (1.09 / 0.75 / 0.85). Treat the measured peaks
as the spec, not a compositing rule.

#### Measurements — the typography

`[MEASURED]` Rank names: fill **`#ffffff`** (exact), outline
**`#000000`** ≈4 px, then a soft dark drop shadow.

Horizontal transect through the left edge of the `C` in "Cadet" at y=240:
`#e8f3f9`(ground) … `#dce3e9 #d1d7dd #91979b`(shadow ramp)
`#1c2023 #000000 #000000 #010304 #373a39`(outline)
`#d0d2d2 #ffffff`(fill).

`[MEASURED]` **Drop-shadow geometry**, measured on the isolated word
"Intern" on the beginner card (glyph+outline bbox x[193,458] y[504,583];
halo bbox x[187,476] y[505,605]): the halo overhangs **6 px left,
18 px right, −1 px above, 22 px below**. Solving
`right = ox+R`, `left = R−ox`, `below = oy+R`, `above = R−oy` gives
**blur radius R ≈ 11–12 px, offset ≈ (+6, +11.5) px** — a shadow thrown
down and slightly right, roughly 62° below horizontal.

`[MEASURED]` Glyph metrics for "Cadet" (white fill only, outline excluded):

| Glyph | bbox | w × h |
|---|---|---|
| `C` | x[207,247) y[204,267) | 40 × 63 |
| `a` | x[255,296) y[216,267) | 41 × 51 |
| `d` | x[303,347) y[201,267) | 44 × 66 |
| `e` | x[357,400) y[217,267) | 43 × 50 |
| `t` | x[406,447) y[201,267) | 41 × 66 |

**Cap height 63 px, x-height 50–51 px → x-height / cap = 0.81.** Advances
48, 48, 54, 49 px. That very large x-height with near-monoline rounded
strokes is the signature of the custom TankTrouble display face — the same
face measures 0.78 on `H-video-title-card-tank-trouble-ranks.png` (cap 127-134, x-height 99-101).

`[MEASURED]` League title `The Soldier league`: fill **`#5f7ce7`**
(dominant, 1501 px; neighbours `#617ce7`, `#5f7ce9`), black outline,
bbox x[211,1065] y[280,358], **height 79 px**. Siblings: beginner
`#7dc8e9`, Scientist `#ee6f63`.

#### Links to the program

* **Contradicts nothing in `srv/`** — because `srv/` contains nothing to contradict. `grep -c` over `srv/index.php`: `Cadet` **0**, `Sergeant` **0**, `Captain` **0**, `Commander` **0**, `Mad Scientist` **0**, `Dog Food` **0**, `League` **0**. (`Lab Rat` = 2 and `Scavenger` = 2, both in *news headlines* — `srv/index.php:9489` "Damages repaired After Great Lab Rat Escape", `:9502` "Lab Rats Escape", `:6610`/`:6625` "Scavenger Team Recovers Fabled Machine". `Intern` = 20 and `Scientist` = 34, all lore prose. **None is a rank.**)
* **Typography dates it.** `grep -in "\.ttf\|font-face\|@font" srv/index.php` → **zero hits**. `grep -o "font-family:[^;\"']*" | sort | uniq -c` → **`10 font-family: Courier`** and nothing else. The era chrome is Verdana/Arial (VE entry 7). The cards are set in a face the classic site provably never loaded.
* Bears on **S114** ("ranks surfaced outside lab" — this is *not* that evidence) and **S83**.

**What this does NOT show.** No thresholds — the cards carry names and
insignia only, never a number. No context: no browser chrome, no page, no
URL, no video player UI, nothing that would date the source or name it.
No indication of where in a UI these devices are actually used.

---

### `Game/H-video-title-card-tank-trouble-ranks.png` (1270×686, captured 16:32:32) — the title card  *(was `ranks.png`)*

sha256 `71f1512b60c04d2c15ee07a1ea3aecc016c5fd9ebb3b9c6e169877fecd801c33` ·
RGBA · ≈96 dpi · 122 739 distinct RGB values

`[OBSERVED]` A landscape title/thumbnail graphic. No UI chrome of any
kind. Composition: two lines of display type top and centre, a large tank
illustration centred low, a rank insignia in the upper-left and
upper-right flanks, and a paw print low-left and low-right.

#### Measurements

`[MEASURED]` **Background.** A vertical gradient from warm pale yellow to
near-white. Sampled down x=30: `#fef4a9` (y=0) → `#fff5ac` → `#fdf6ac` →
`#fdf5b0` → `#fdf7bf` → `#fdf8c5` → `#fffad0` → `#fefadb` → `#fffce6` →
`#fefeee` → `#fdfef5` → `#fefefc` (y=660). Horizontally uniform at the top
(`#fef4a9` at every 120 px across y=8). Behind the tank there is an
additional **warm radial glow**: along y=520 the row runs
`#fdf5e5 #fde4ce #ffc7b2` inward to the tank and `#fea688 #ffcbb5 #ffead6`
outward.

`[MEASURED]` **"Tank Trouble"** — fill `#ececec` (28 540 px; the near
neighbours `#ebebeb`, `#ededed`, `#eeeeee` make up the AA), outline
`#0d0d0d`–`#161616`, plus a soft dark drop shadow down-right.
Overall bbox x[100,1166] y[56,189].
Glyph fills: `T` 80×127, `a` 72×101, `n` 74×100, `k` 73×134,
`T` 80×127, `r` 61×99, `o` 77×100, `u` 73×99, `b` 75×132, `l` 34×134,
`e` 75×101. **Cap/ascender 127–134 px, x-height 99–101 px → ratio 0.78.**

`[MEASURED]` **"Ranks"** — fill `#fc861a` (orange; neighbours `#fa953c`,
`#fa871a`, `#fa8e30`), same black outline and drop shadow, set **larger
and overlapping the baseline of the line above**. bbox x[424,1045]
y[179,387]; glyph fills `R` 122×144, `a` 92×129, `n` 94×128,
`k` 94×171, `s` 81×136.

`[MEASURED]` **The two insignia**, both rotated (decorative, not
axis-aligned):

* upper-left, x≈[187,276] y≈[398,492], tilted ≈20–25° clockwise:
  **2 chevrons + 3 stars = Commander** (top of the Soldier league).
* upper-right, x≈[1051,1138] y≈[430,513], tilted ≈10°:
  **1 chevron + 2 stars = Intern** (third of the beginner league).

`[MEASURED]` Their gold is **`#ffd300`** — a fully saturated gold with
**zero blue**. This is *not* the league cards' gold (median `#e1b840`,
core `#ffc637`, which carries a blue component of 0x37–0x40). Their dark
interior is warm near-black (`#2a1800`, `#281500`), where the cards use
neutral `#000000`. `[INFERRED]` The title card was drawn separately from
the league cards — same design language, different asset. Falsifiable if a
colour-managed re-encode of one source is shown to produce both.

`[MEASURED]` **The paw prints** — one lower-left (x≈[115,190] y≈[550,640]),
one lower-right (x≈[1155,1215] y≈[560,650]). Each is a **five-part dog
paw**: one large rounded triangular metacarpal pad below, four separate
oval toe pads above (the outer two set lower and angled outward). Fill
`#ffca00`, outline warm near-black (`#3c2612`, `#2a1c00`).
`[INFERRED]` The paw is a **Laika** reference — the site's space-dog
mascot (`srv/index.php:9826` embeds `laika02.swf`; S103) — and it rhymes
with the bottom rank being called "Dog Food". Falsifiable only by a
statement from the author.

`[MEASURED]` **The tank illustration.** Outline bbox x[457,834] y[414,622]
= 378 × 209 px. Body tones: highlight `#f65c36`, mid `#943d28`, shadow
`#51291e`. Drawn in 3/4 view, facing right, with a thick uniform black
outline that has a visible hand-drawn wobble; flat cel shading with a hard
diagonal top-face highlight; dome turret with an angled barrel ending in a
thick muzzle ring; two rows of road wheels along the left of the hull.

#### Does the tank match the classic site's art, or is it a later redraw?

`[MEASURED]` I extracted three tanks, mirrored the two that face left, and
scaled all three to a common 150 px height:

* `H-video-title-card-tank-trouble-ranks.png` tank — 378 × 209 px;
* the classic HUD tank from `H-classic-gameplay-1p-vs-laika.png` — orange hull bbox 154 × 60 px in
  capture pixels; the crop actually compared was that bbox padded 6 px all
  round (166 × 72) and **de-stretched by ÷1.497 to 111 × 72** first;
* the green tank from crop `H-hud-crop-score-10-with-transient.png` — 55 × 33 px.

`[OBSERVED]` Side by side they are **the same tank design**: identical
hull silhouette (wedge nose at the low-left, angled counter at the
high-right), identical turret dome and barrel angle, identical
two-row road-wheel arrangement, identical ground shadow placement.

`[UNCERTAIN]` One consistent difference: **the value structure of the
tracks is inverted.** On both classic tanks the track band is *light*
(hull colour) with *dark* slots punched through it. On the `H-video-title-card-tank-trouble-ranks.png`
tank the band is *dark* with *light* elliptical wheels inside it and a
ringed drive sprocket at each end. I cannot say whether that is a genuine
redraw or simply what the classic art resolves to when it is only 27–60 px
tall. **What would settle it:** a native-resolution classic tank render —
`loggedInTank06.swf` played back, or any `?garage` frame at 1:1 (S24/S113).

`[INFERRED]` On balance: same lineage, higher-fidelity render, most likely
the **HTML5 generation's** version of the tank (`srv/index.php:7405`
lists "New improved tank design prepped for accessories extravaganza"
among the Online BETA launch features, news dated 2015-07-09). Do not treat this file as a
reference for classic tank art.

**Links to the program.** `[NOT VISIBLE]` — nothing here maps to any
served file. **What this does NOT show:** no thresholds, no league names,
no UI, no provenance marker (no watermark, no channel name, no player
name). It is a promotional/thumbnail graphic and carries no evidentiary
weight about the classic site beyond the typeface argument.

---

### The two tiny crops — `Game/H-hud-crop-score-10-with-transient.png` (103×55, 16:41:18) and `Game/H-hud-crop-score-10-clean.png` (101×53, 16:41:25)

sha256 `350e4d50424ca5cb63dd6bfeb1b1d41d2c22eff4c3018d66250c559afe5c1222`
and `aef22184101932b81c8e0108e4215212a52cb6ef4358fda247d644a3c227e7f5` ·
both RGBA with a fully opaque alpha (min = max = 255) · both ≈96 dpi ·
1 488 and 1 149 distinct RGB values.

#### What is drawn — upscaled 8× and 16×

`[OBSERVED]` Both crops show, on a white ground:

* a **green tank in 3/4 view, facing left** (barrel pointing left and
  slightly up), with a dome turret, an angled barrel with a muzzle ring, a
  wedge-nosed hull, and two rows of dark road-wheel slots along the right
  of the hull;
* to the **left** of the tank, two grey digits reading **`10`**;
* in `H-hud-crop-score-10-with-transient.png` only, a **soft, shapeless mid-grey cloud** overlapping
  and partly obscuring the area above and left of the digits;
* in `H-hud-crop-score-10-clean.png` only, a 47 × 1 px black bar along the very top edge
  (x[0,47) y[0,1)) — a crop artefact where the selection caught the edge of
  something dark above.

#### Reading the digits

`[MEASURED]` ASCII pixel dump of the glyph region confirms the value
against a threshold sweep:

`H-hud-crop-score-10-with-transient.png` — `1` at x[23,29) y[28,37) (6 × 9); `0` at x[30,37) y[28,37)
(7 × 9). The `1` shows the small upper-left flag serif; the `0` is a closed
oval.
`H-hud-crop-score-10-clean.png` — `1` at x[26,31) y[31,40); `0` at x[33,40) y[31,43).

**Both read `10`.** `[MEASURED]` Digit ink is neutral grey: mean
`#6b6869` / `#686566`, darkest `#312f2f` / `#282526` — the same neutral
grey family as the `24` / `1` scores in `H-classic-gameplay-1p-vs-laika.png`.

`[UNCERTAIN]` In each crop there is a faint isolated diagonal mark ≈13 px
left of the `1` (`H-hud-crop-score-10-with-transient.png` at x≈18-20 y≈34-37; `H-hud-crop-score-10-clean.png` at
x≈15-18 y≈38-42). At this blur level I cannot resolve it. It does not
align between the two crops after the measured offset, so I will not claim
it is the same element. It is **not** a minus sign — it sits far too far
left and is not on the digit baseline.

#### The frame-to-frame diff

`[MEASURED]` Exhaustive SAD search over ±12 px gives a best alignment of
**(ox, oy) = (−3, −3)** — i.e. `H-hud-crop-score-10-clean.png` = `H-hud-crop-score-10-with-transient.png` shifted by
(+3, +3) — over a 98 × 50 overlap. That is also exactly what the green-mask
bounding boxes say independently: A = x[41,89] y[11,37], B = x[44,92]
y[14,40], both **49 × 27**.

`[MEASURED]` `PIL.ImageChops.difference` on the aligned overlap:
mean channel-sum difference 33.7; 802 px above 30; **498 px above 90**,
confined to bbox x[11,83] y[5,39]. The column profile of the difference
peaks between x = 18 and x = 41 and is essentially flat elsewhere.

`[OBSERVED]` Rendering the difference map: **the tank is identical; the
digits are identical; the only substantive change is the grey cloud**,
present in `H-hud-crop-score-10-with-transient.png` and absent in `H-hud-crop-score-10-clean.png`.

`[MEASURED]` The cloud: bbox ≈ x[12,40] y[5,27] (**≈29 × 23 px**),
**neutral** (max channel spread across the region 23/27/11), values from
`#393637` at its darkest to `#eaeaea` at its faintest, mean `#aaa8a9`.
Its edges are soft in every direction; posterising it into five bands
shows a lobed, dome-shaped puff with a small darker horizontal streak
inside and a hook at the left edge.

`[UNCERTAIN]` **What the cloud is.** Candidates, none provable at 29 × 23
blurred pixels:
1. a **smoke / dust puff sprite** — this is the closest match by texture
   and value: the classic game's smoke puff, visible in the maze of
   `F-gameplay-three-guests-maze-crop.png` at ≈(335,345), is a lobed soft neutral-grey cloud of the
   same character;
2. an interframe compression ghost from a heavily-recompressed video;
3. a recording-software cursor/click highlight;
4. a transient UI element.
**What would settle it:** the uncropped frame, or the source video with
one second either side.

#### Rank icon, or score counter? — the question the topic asks

**It is a score counter.** `[MEASURED]`, on four independent grounds.

1. **Layout matches the classic HUD exactly.** In `F-gameplay-maze-61-crates.png` (topic F,
   16:24:50) a classic 2-player round shows a red tank facing **right**
   with score `1` on its **right**, and a green tank facing **left** with
   score `0` on its **left**. In `F-gameplay-three-guests-maze-crop.png` (topic F, 16:22:54) a
   3-player round shows red `28` (right), green `29` (right), blue `21` on
   its **left**. My crops are exactly the right-hand slot: tank facing
   left, numeral on its left, no name visible above the crop line.
2. **The artwork is the classic HUD tank.** Green-mask bbox 49 × 27
   (aspect **1.81**) in the crops, vs 114 × 62 (**1.84**) in `F-gameplay-maze-61-crates.png`
   and 122 × 66 (**1.85**) in `F-gameplay-three-guests-maze-crop.png` — same drawing, different scale.
   Tank-height ratio 27/62 = 0.435 and 27/66 = 0.409; digit-height ratio
   9/21 = 0.43 and 9/20 = 0.45. **Tank and type scale by the same factor**,
   so the crops are one coherent capture at ≈0.41–0.44× the scale of the
   topic-F frames — not a montage.
   The tracks are dark slots on a light hull — the classic treatment, not
   `H-video-title-card-tank-trouble-ranks.png`'s inverted treatment.
3. **The typeface is the page/SWF grotesque, not the rank font.** The `10`
   is a plain neutral-grey Arial/Verdana-family numeral matching
   `H-classic-gameplay-1p-vs-laika.png`'s `24`. The rank material is set in the rounded custom
   display face throughout.
4. **A real rank icon looks different, and I have one to compare against.**
   In `F-html5-generation-contrast-case.png` (topic F) the modern HUD renders, per player:
   `<name in the outlined display font><small gold chevron device>` on one
   line, and `<kills> • <deaths>` on the next. The rank icon is a **gold
   chevron**, sits **after the name**, and is **adjacent to but distinct
   from** the numeric line. My crops contain no gold pixel at all
   (the mask `g > 60 & g > 1.3r & g > 1.3b` matches only the tank body), no
   `•` separator, and no second numeral.

`[INFERRED]` What the owner was doing at 16:41:18–16:41:25: testing
`ranks.txt`'s claim that "Rank icons are displayed on tanks". He grabbed
two frames of the same tank to see whether the thing beside it persisted.
The answer his own crops give is that the persistent element is the
**score**, and the transient grey cloud is not an insignia — it is soft,
neutral, shapeless, and gone in the next grab. Falsifiable by the source
video.

**Links to the program.** These crops are the **first look this project
has at the classic in-SWF HUD row** — tank render, name label, score
numeral, their relative placement and their type colour. That is genuinely
new and it is not currently an S-number: the sweep covers the page around
the stage but not the inside of the stage. See "New wants" below.
Bears on **S114** by *removing* a candidate: the numeral beside a classic
tank is a score, not a rank.

**What this does NOT show.** No name label (cropped away), no left-hand
player, no maze, no page chrome, nothing datable. No rank insignia of any
kind.

---

## The provenance question, head-on

The owner's caveat is the correct instinct. Here is the evidence in full.

### 1. `ranks.txt` scopes itself to a different product

`[OBSERVED]` Sentence one: *"Ranks is the skill measuring system in
**TankTrouble Online**."*

`[MEASURED]` "TankTrouble Online" occurs **38 times** in `srv/index.php`,
and the era site defines it explicitly at `srv/index.php:6988-6990`:

> In **TankTrouble Online** players from all over the world will be able to
> meet in epic, online battles. It is currently in development so you
> cannot play online just yet. […] **Online BETA** is a test version of
> TankTrouble Online. […] we take it for a test-drive on
> beta.tanktrouble.com.

`[MEASURED]` `beta.tanktrouble.com` occurs 30 times in the era page.
"TankTrouble Online" is, in the classic site's **own vocabulary**, the
name of the *other* product. So `ranks.txt` is, on its own testimony, not
about the site being reconstructed.

`[OBSERVED]` The phrase "ranked match" reinforces this: the classic Flash
game is local-only multiplayer on one keyboard. There is no matchmaking to
be ranked in.

`[MEASURED]` `grep -icE` over `srv/index.php`, **word-bounded** (an
unbounded `elo` matches inside *below*, *velocity* and *developer*, which
is why the loose form must not be quoted):
`\branked\b` **0**, `matchmaking` **0**, `matchmake` **0**,
`leaderboard` **0**, `\belo\b` **0**, `rank point` **0**, `rank icon` **0**.

### 2. Every rank name, grepped

`[MEASURED]` `grep -c -F` over `srv/index.php` (812 KB, all seven route
copies of the page JS):

| Name | Hits | Every hit accounted for |
|---|---:|---|
| `Dog Food` | **0** | — |
| `Lab Rat` | 2 | news headlines `:9489` "Damages repaired After Great Lab Rat Escape", `:9502` "Lab Rats Escape" |
| `Intern` | 20 | 1 × `HTTP/1.1 500 Internal Server Error` (`:193`); 19 × lore prose about the laboratory's intern |
| `Scavenger` | 2 | news headline `:6610` / its share-JSON `:6625` "Scavenger Team Recovers Fabled Machine" |
| `Cadet` | **0** | — |
| `Sergeant` | **0** | — |
| `Captain` | **0** | — |
| `Commander` | **0** | — |
| `Jr. Scientist` | **0** | — |
| `Scientist` | 34 | all lore prose ("the lead scientist", "Scrapyard Scientist", …) |
| `Lead Scientist` | **0** | (lower-case "lead scientist" appears in prose, e.g. `:6539`) |
| `Mad Scientist` | **0** | — |
| `League` / `league` | 0 / 1 | the one hit is `:10489` "Tell your **colleagues**…" — a substring, not the word |
| `milestone` / `Milestone` | 2 / 1 | `:7366`, `:7381` (Online BETA opening); `:8783` "Scientists Miss Major Milestone" |

`[MEASURED]` `grep -in "rank"` returns **12** hits, and none is a rank
name. They are: a comment (`:21`), a pun on "dog biscuit" (`:8586`), and
the ten lines that make up the *experience*-ranking feature described next.

`[MEASURED]` `grep -in "rank" LEDGER.tsv` returns **exactly one row**,
line **225**:

```
srv/tankRanks/index.php	M2	—	written 2026-08-03	dir /tankRanks/ 86x200 CDX 2010-2015; era ?lab pages open it via window.open('tankRanks',...) (DEDUCE.md 2.2); index filename convention-inferred	—	501 stub (tree correction, DEDUCE.md)
```

`[MEASURED]` `grep -in "rank"` over `DEDUCE.md` returns one line
(`DEDUCE.md:148`, the CDX table row: `/tankRanks/` **86** 200s, 11
non-200, **2010-10-30 … 2015-05-23**, "⚠ missed by the first tree").
Over `DECISIONS.md` it returns lines 107-109 (the stub decision), 394 and
472 (top-10 *rankings*, a frozen live region), and 540 (the stub list).
Over `docs/standards/DIVERGENCES-SERVED.md`, one line (`:72`, "top-10 rankings").
Over `docs/standards/ASSET-DISCIPLINE.md`, **zero**.

**Nothing in the repo knows about a twelve-step ladder. Nothing.**

### 3. What the classic era actually had

`[MEASURED]` The classic metric is **experience**, and the site published
the formula. `srv/index.php:9462-9479`, news dated **25-07-2009**,
headline "New Experience System Separates the Sheep from the Wolves":

> - Defeat tank owners with the same experience to gain 10 experience points.
> - Defeat tank owners with more experience and gain more.
> - Defeat tank owners with less experience and gain less.
> […]
> `winnerExperience += round(min(20, max(1, 10 + (loosersExperience - winnerExperience) / 100)))`

`[MEASURED]` The only rank *surface* on the classic site is on `?lab`
(`$tt_routes['lab']`, `srv/index.php:16666`):

```
srv/index.php:13845  <!-- Tank Ranks link -->
srv/index.php:13847    <span class="text medium black">What's Your Tank Rank?<br/></span>
srv/index.php:13848    Are you curious to know how you rank amongst other tank owners? Then check out this
                       useful, little prototype made by our intern: <a href='' id='tankRanks'>Tank Rank by Experience</a>
srv/index.php:13852    document.getElementById('tankRanks').onclick = function()
srv/index.php:13854      window.open('tankRanks', '_blank', 'width=460,height=535,…,scrollbars=1,…');
```

announced by the news item at `srv/index.php:9181-9187`, dated
**12-09-2010**.

`[OBSERVED]` Three things follow from that link text:
* the feature is called **"Tank Rank by Experience"** — it *ranks by the
  experience metric*, i.e. it is a leaderboard/percentile tool, not a
  12-step badge ladder;
* it is "a useful, little **prototype** made by our intern" — the site's
  own framing is a throwaway;
* it opens in a **460 × 535 popup with scrollbars** — the shape of a
  table, not of a badge gallery.

`[MEASURED]` Supporting: the front-page Top-10 box's logged-in header is
literally `Top 10 Exp.` (`srv/index.php:1113` and six sibling copies at
`:2698 :5277 :11255 :12974 :14523 :15979`). Experience is the currency the
classic site displays.

`[MEASURED]` And the Online BETA feature announcement of 2015-07-09
(`srv/index.php:7405-7415`) lists under **"In development"**:
`<li>New score and experience system</li>` — i.e. the *replacement* for the
2009 experience system was scoped to the Online/BETA generation, not to
the classic site.

### 4. The typography dates the cards to the later generation

`[MEASURED]` `grep -in "\.ttf\|font-face\|@font" srv/index.php` →
**zero hits**. `grep -o "font-family:[^;\"']*" srv/index.php | sort |
uniq -c` → **`10 font-family: Courier`**, and nothing else. VE entry 7
records the era chrome as the Verdana/Arial family; the classic HUD text
in `H-classic-gameplay-1p-vs-laika.png` and `F-gameplay-three-guests-maze-crop.png` is visibly that.

`[MEASURED]` `srv/index.php:6657` (news block opens at `:6646`, dated
**25-05-2016**, "Online BETA Development Report"):

> Numerous other updates have been installed too; like in-game garage
> access with instant tank updating, a weapons stack display, **a custom
> TankTrouble font**, and a completely redesigned sign-up process. That,
> and many more goodies are now ready for testing on
> [TankTrouble Online BETA](https://beta.tanktrouble.com).

`[OBSERVED]` The league cards, the `H-video-title-card-tank-trouble-ranks.png` title, and the player names
in `F-html5-generation-contrast-case.png`'s modern HUD are all set in one rounded, heavy,
large-x-height display face (measured x-height/cap 0.81 on the cards, 0.78
on `H-video-title-card-tank-trouble-ranks.png`). `[INFERRED]` That is the custom TankTrouble face, which
by the site's own news shipped **to BETA in May 2016** and which the
classic page never declares or loads. Falsifiable by finding an era
capture of `tanktrouble.com` that loads a webfont.

(Independently: topic I's assignment includes `root/TankTrouble.ttf`, so
the owner holds the face itself. Whoever writes topic I should be asked to
render "Cadet" from it and compare against my glyph metrics — that would
turn `[INFERRED]` into `[MEASURED]`.)

### 5. The smoking gun — `F-html5-generation-contrast-case.png` (topic F's file, 16:37:38)

`[OBSERVED]` This frame shows the **modern HTML5 tanktrouble.com**: HTML5
nav tabs, an `✕` close button over the stage, "Download on the App Store"
and "GET IT ON Google play" badges, a "WALL of FAME COMMEMORATING BACKERS
AND FRIENDS" panel, a "Message the laboratory" panel, a War Thunder ad
creative in the left rail, and a "Battle mode: **Classic** / Never-ending
destruction! / Next battle mode starts in 1 minute" box — battle-mode
rotation is a feature the classic site never had.

`[OBSERVED]` In the left rail, a promo box carrying a **3-chevron,
3-star** insignia (= Mad Scientist, top of the Scientist league — exactly
the grammar the cards establish) above the headline, verbatim:

```
Tank Rank
has been
Deployed
```

with a `Read more` link beneath.

`[OBSERVED]` At the bottom, a five-player HUD. Per player, two lines:
`<username, in the outlined custom display face><small gold rank device>`,
then `<n> • <n>` (kills • deaths) in the same face. Read at 3× and 14×:

| Username (verbatim; `[UNCERTAIN]` glyphs marked) | Rank device | Reads as | Score line |
|---|---|---|---|
| `Happyh0ur888` (the 4th glyph is `0`-or-`o`, `[UNCERTAIN]`) | 1 chevron, 0 stars | Dog Food | `6 • 2` |
| `Moscles25` | 1 chevron, **1 star** | Lab Rat | `0 • 0` |
| `carlosr117` | 1 chevron, **1 star** | Lab Rat | `15 • 8` |
| `yungkidd12` | 1 chevron, 0 stars | Dog Food | `25 • 10` |
| `Vireaux` | 1 chevron, 0 stars | Dog Food | `6 • 5` |

`[OBSERVED]` Two further per-player glyphs appear on the score line and
must not be confused with rank insignia: a small **gold crown** immediately
before `6 • 5` (the round leader, `[INFERRED]` — it sits with the highest
kill count of the visible five only if 6 is highest, which it is not, so
`[UNCERTAIN]` what it marks), and a soft grey **skull-like smudge** before
`6 • 2`. Both are at the size and roughly the value that a rank badge
would occupy, which is exactly why the distinction in §"Rank icon, or
score counter?" had to be made by construction rather than by eye.

`[OBSERVED]` The live client therefore **confirms the card grammar
independently**: the two players with a star outrank the three without, and
the promo box's 3-chevron/3-star device is the top of the ladder.

`[INFERRED]` This is decisive on three points at once:
* the rank system is a **modern-client** feature, and the promo box calls
  it newly "**Deployed**" — a launch announcement;
* `ranks.txt`'s claim that "rank icons are displayed on tanks" is **true
  of the modern client**;
* a rank icon and a score readout are **two separate elements** in that
  HUD, which is precisely the distinction my two tiny crops needed.

Falsifiable only by showing that `F-html5-generation-contrast-case.png` is not tanktrouble.com — the
logo, the nav, the scrapyard counter and the "Message the laboratory" copy
all say it is.

### Verdict

**Post-era.** `[INFERRED]`, at the strongest confidence this evidence set
can support: five independent lines, none dissenting, one of them (§5) a
direct sighting of the feature on the later platform.

**What would overturn it**, in descending order of decisiveness:
1. An archived body for `/tankRanks/` showing chevron/star insignia or any
   of the twelve names. (86 CDX 200s exist, 2010-10-30 … 2015-05-23; no
   body is held. This is the single highest-value fetch in the topic.)
2. A dated 2017–2018 video frame of `tanktrouble.com` showing a chevron
   next to a player name or in any panel.
3. An era WARC body containing any of the eight zero-hit names.
4. An era capture that loads a webfont — which would break the typography
   argument (line 4) but not lines 1, 2, 3 or 5.

**Getting this wrong in the other direction** — declaring it post-era when
it was in fact in-era — costs the project only a `WANTED` entry that stays
open. Getting it wrong in the direction of adoption would put invented,
wrong-generation artwork into `srv/` under an era tier. Under
`README.md`'s governing sentence that is precisely the forgery the project
exists to avoid.

---

## The full ladder and the twelve insignia

### Reconciliation: 12 milestones vs 4 + 4 + 4 slots

`[MEASURED]` **They reconcile exactly. No name is missing; no name is
duplicated; no card cell is unaccounted for.**

Cards read in normal reading order (TL, TR, BL, BR) are **ascending**;
`ranks.txt` lists **descending**. The two orders are exact reverses.

| Asc. # | `ranks.txt` threshold | Name (verbatim) | League card | Cell | Chevrons | Stars |
|---:|---|---|---|---|---:|---:|
| 1 | `Rank 0` | `Dog Food` | The beginner league | TL | 1 | 0 |
| 2 | `5` | `Lab Rat` | The beginner league | TR | 1 | 1 |
| 3 | `10` | `Intern` | The beginner league | BL | 1 | 2 |
| 4 | `25` | `Scavenger` | The beginner league | BR | 1 | 3 |
| 5 | `50` | `Cadet` | **The Soldier league** | TL | 2 | 0 |
| 6 | `100` | `Sergeant` | **The Soldier league** | TR | 2 | 1 |
| 7 | `150` | `Captain` | **The Soldier league** | BL | 2 | 2 |
| 8 | `250` | `Commander` | **The Soldier league** | BR | 2 | 3 |
| 9 | `500` | `Jr. Scientist` | The Scientist League | TL | 3 | 0 |
| 10 | `1.000` | `Scientist` | The Scientist League | TR | 3 | 1 |
| 11 | `1.500` | `Lead Scientist` | The Scientist League | BL | 3 | 2 |
| 12 | `2.000` | `Mad Scientist` | The Scientist League | BR | 3 | 3 |

Bold rows are from my assigned file. The other eight are read off topic
F's `F-video-card-beginner-league-caption.png` and `F-video-card-scientist-league-caption.png` and are flagged as such.

`[OBSERVED]` **The construction rule**, for `n` = 0…11:

```
chevrons = floor(n / 4) + 1        // 1 = beginner, 2 = Soldier, 3 = Scientist
stars    = n mod 4                 // 0, 1, 2, 3 within the league
```

`[MEASURED]` Corroborated by total gold-device height, which grows one
chevron-pitch per league: beginner top-left device 95 × 37 px, Soldier
top-left 96 × 64 px, Scientist top-left 95 × 93 px — increments of
**27–29 px per additional chevron**, matching the 13 px bar + 13 px gap
measured on the Cadet transect.

### The twelve devices, described for redrawing

`[OBSERVED]` **Shared construction**, identical across all twelve:
a solid black chevron-shaped plaque (apex up, arms sweeping down and out,
squared-off arm ends), carrying **N gold chevron bars** across its upper
part separated by black stripes of the same weight, with **M gold
five-pointed stars** seated in the notch beneath the lowest bar. Every
element carries a black outline; the whole device sits on a soft coloured
halo whose hue equals its card's border colour.

`[MEASURED]` **Star placement** within the notch:
* M = 1 → single star on the axis, tucked into the notch;
* M = 2 → two stars side by side, symmetric about the axis, both at the
  same height, straddling the notch;
* M = 3 → three stars, **the centre one set higher** (Soldier/Commander:
  centre y[438,472), flanks y[453,486) and y[454,485) — a **15 px** rise),
  the two flanks lower and pushed outward past the plaque edges.

| Rank | Chevrons | Stars | Arrangement | Gold | Halo (card colour) |
|---|---:|---:|---|---|---|
| Dog Food | 1 | 0 | bare chevron | core `#ffc637`, median `#e1b840` | violet `#a690ac` |
| Lab Rat | 1 | 1 | star centred in notch | " | violet |
| Intern | 1 | 2 | two stars, level, symmetric | " | violet |
| Scavenger | 1 | 3 | centre star raised, flanks low/outboard | " | violet |
| Cadet | 2 | 0 | bare 2-bar chevron | " | rose `#b68a9c` |
| Sergeant | 2 | 1 | star centred | " | rose |
| Captain | 2 | 2 | two stars, level (39 × 39 px each) | " | rose |
| Commander | 2 | 3 | centre raised 15 px, flanks low/outboard | " | rose |
| Jr. Scientist | 3 | 0 | bare 3-bar chevron | " | coral `#d56b63` |
| Scientist | 3 | 1 | star centred | " | coral |
| Lead Scientist | 3 | 2 | two stars, level | " | coral |
| Mad Scientist | 3 | 3 | centre raised, flanks low/outboard | " | coral |

### Card palette, complete

| | The beginner league | **The Soldier league** | The Scientist League |
|---|---|---|---|
| Source file | `F-video-card-beginner-league-caption.png` (topic F) | **`H-league-card-soldier.png` (mine)** | `F-video-card-scientist-league-caption.png` (topic F) |
| Border | `#a178af` | **`#ba678c`** | `#e94e36` (`#e84d35` on `F-video-card-scientist-league.png`) |
| Cell ground | `#e8f3f9` | **`#e8f3f9`** | `#a3dbcc` |
| Divider rules | `#000000` | **`#000000`** | `#000000` |
| Vertical rule width | 10 px | **9 px** | 10 px |
| Horizontal rule height | 13 px (`F-video-card-beginner-league.png`) | **13 px** | 14 px (`F-video-card-scientist-league.png`) |
| Insignia gold, median | `#e4bc41` | **`#e1b840`** | `#e1b740` |
| Insignia gold, core / rim / toe | `#ffc637` / `#ffdd4f` / `#976f00` | **same** | same |
| Halo peak | `#a690ac` | **`#b68a9c`** | `#d56b63` |
| Halo fade distance | ≈22–26 px | **≈32 px** | ≈45 px |
| Rank-name fill | `#ffffff` | **`#ffffff`** | `#ffffff` (except Mad Scientist) |
| Rank-name outline | `#000000`, ≈4 px | **`#000000`, ≈4 px** | `#000000`, ≈4 px |
| Drop shadow | R ≈ 11–12 px, offset ≈ (+6, +11.5) | **same** | same |
| League title fill | `#7dc8e9` | **`#5f7ce7`** | `#ee6f63` |
| League title, verbatim | `The beginner league` | **`The Soldier league`** | `The Scientist League` |

### The red-on-glow treatment

`[OBSERVED]` One rank is not white: **`Mad Scientist`**, the top of the
ladder, is rendered in red-orange on both Scientist frames
(`F-video-card-scientist-league.png` *and* `F-video-card-scientist-league-caption.png`) — so it is a permanent treatment, not an
animation state.

`[MEASURED]` Fill ranges `#ec563f` (highlight) down through `#dc4f38`,
`#d34c39` to `#c94936` (shade) — 4 006 px pass a strict red mask over the
word. Same black outline and same drop-shadow geometry as its white
siblings, **plus** a warm red halo around the glyphs, on the mint-green
`#a3dbcc` ground.

`[MEASURED]` Its red is **darker and more saturated** than "The Scientist
League" title above it (`#ee6f63`), and darker than the card border
(`#e94e36`). Three distinct reds on one card.

### The league title animates in

`[MEASURED]` `F-video-card-beginner-league.png` (topic F) is the same beginner card as
`F-video-card-beginner-league-caption.png`, but the title is present at only a few percent opacity:
the ghost glyph fill samples `#e4f1f7` against the `#e8f3f9` cell ground,
where the finished frame gives `#7dc8e9`. Solving per channel gives
α ≈ 0.04 / 0.05 / 0.13 → **≈5–12 % opacity**.
`F-video-card-scientist-league.png` shows the Scientist card with the title fully absent.
`[INFERRED]` The three cards are frames of a **video** in which each 2×2
grid is presented and the league title then fades (or scales) in over it.
Falsifiable by the source video.

---

## Consequences for the rebuild

### Confirmed

* **`srv/index.php:404`** — the game SWF really is embedded at
  **712 × 490** and that is what the classic frames render.
  (`H-classic-gameplay-1p-vs-laika.png`, `F-gameplay-maze-61-crates.png`, `F-gameplay-three-guests-maze-crop.png`, all `version 4.0`.)
* **`srv/index.php:9479`** — the classic skill metric is **experience**,
  and the era `?lab` link `Tank Rank by Experience`
  (`srv/index.php:13848`) is the *only* rank surface the site had.
  Nothing in this evidence set changes either.
* **DECISIONS 2026-08-03 `/tankRanks/`** — the reasoning that put
  `srv/tankRanks/index.php` in the tree as a 501 stub is untouched and
  still right. The stub stays a stub.
* **VE entry 7 / typography** — the era chrome is Verdana/Arial, not a
  webfont. `grep` for `@font-face` in `srv/index.php` returns zero. This
  evidence *reinforces* that, because the thing that isn't Verdana/Arial
  is exactly the thing that turns out to be post-era.

### Contradicted — overhaul owed

**None, and that is the point.** No invention in `srv/` is superseded by
this evidence, because nothing about ranks was ever invented. THE OVERHAUL
RULE is not triggered.

Two smaller corrections, neither to `srv/`:

* **To the task brief, not the repo:** `Game/H-classic-gameplay-1p-vs-laika.png` is a classic
  gameplay frame, not a league card; and there is **no** duplicate copy of
  it in `UI/` (nor any duplicate anywhere in the 101-file corpus).
* **`srv/index.php:329` vs `H-classic-gameplay-1p-vs-laika.png`:** the frame's
  `Copyright www.purup.com 2007 – 2015` plus a second credit line
  (`Design: Mads Purup, Programming: Brian Bunch Christensen, Server:
  Søren Boll Overgaard`) show a page-chrome generation that the era-final
  bytes do not have. That is a **new dated divergence between generations**,
  not a divergence in the served bytes. It belongs in the S105 /
  "annotation pass" family as a date anchor, not as an overhaul.

### Still unknown / stays on the want-list

* **S83 `/tankRanks/`** — completely unknown. This evidence does **not**
  touch it and must not be recorded as touching it. What the 460 × 535
  popup contained remains the open question, and the "by Experience" link
  text is the only clue to its content.
* **S114** — "ranks surfaced outside lab" stays open, but is now better
  posed: the answer for the **classic** site is still unknown, and the
  answer for the **modern** site is "yes, in the HUD after the username"
  (which is out of scope).
* **S105** — the `H-classic-gameplay-1p-vs-laika.png` credit line adds a data point but does not
  close it.
* **S24 / S113** — a native-resolution classic tank render is still needed
  to settle whether `H-video-title-card-tank-trouble-ranks.png`'s tank is a redraw or the same art.

### New wants to add

1. **The classic in-SWF HUD row** — *not currently an S-number.* The sweep
   covers the page around the 712 × 490 stage but not the inside of it. My
   crops and topic F's classic frames give the first look: per player, a
   3/4 tank render + a name label beneath + a grey score numeral placed on
   the *inboard* side (right of players 1–2, left of the right-most
   player), with a grey `+` between the two sides in the 1v1 layout; a
   gear and a speaker icon at far left; maze number / author / `version
   4.0` in pale grey at far right. Recoverability **HIGH** (any gameplay
   video). Worth its own entry because the rebuild will eventually need
   these positions to validate a Ruffle/projector render (gate C).
2. **In-era evidence that ranks were surfaced anywhere outside `?lab`** —
   the want this topic creates. Status **WANTED**, recoverability **LOW**.
   The trigger to look for: any 2017–2018 `tanktrouble.com` frame showing a
   chevron/star device, or any of the twelve names, on the classic site.
   Also: an archived body for `/tankRanks/` (86 CDX 200s, 2010-2015 — a
   Wayback fetch may still succeed even though no body is held locally).
3. **A native-resolution classic tank render**, to settle the
   track/wheel-value difference between `H-video-title-card-tank-trouble-ranks.png`'s tank and the classic
   HUD tank. Folds into S24/S113.

### What must NOT be adopted, explicitly

On this evidence alone, **none of the following may enter `srv/` at any
tier**:

* the twelve rank names or their thresholds;
* the three league names or the league grouping;
* the chevron/star insignia artwork, its gold (`#ffc637` / `#e1b840`), its
  halo colours, or the `chevrons = league, stars = position` grammar;
* the card palette (`#a178af`, `#ba678c`, `#e94e36`, `#e8f3f9`, `#a3dbcc`)
  or the outlined-display-face treatment;
* `H-video-title-card-tank-trouble-ranks.png`'s tank illustration, its paw-print motif, or its type;
* any rank icon beside a tank in a rebuilt HUD.

`srv/tankRanks/index.php` stays a **501 stub**. Filling it with this
material would be exactly the case
`docs/standards/VISUAL-EVIDENCE-WANTED.md` §"THE OVERHAUL RULE" is written to
prevent: an M2 invention given false authority, and — worse here —
a *wrong-generation* invention, which no later overhaul could detect from
the inside.

The one thing that **is** safe to carry forward from these files is the
classic HUD anatomy in `H-classic-gameplay-1p-vs-laika.png` (de-stretched by ÷1.497 first) and in
the two tiny crops, and that belongs to the game-stage work, not to ranks.

---

## Recommended edits to existing docs (not applied)

### `docs/standards/VISUAL-EVIDENCE-WANTED.md`

**1. S83 — leave `WANTED`, but annotate.** Do *not* mark it PARTIAL or
FETCHED. Suggested replacement for the "What exists / what's missing" cell
of row S83:

> 460×535 popup w/ scrollbars from `?lab`; 86 CDX 200s 2010-2015; link text
> is **"Tank Rank by Experience"** (`srv/index.php:13848`) and the news
> that announced it (`:9181`, 12-09-2010) calls it "a useful, little
> prototype made by our intern" — so the content is a *leaderboard by the
> 2009 experience metric*, not a badge ladder. **A twelve-milestone
> chevron/star ladder circulated in the community (manual-evidence
> `Game/ranks.txt`, `Game/H-league-card-soldier.png` + siblings, 2026-08-04) is
> post-era HTML5 "TankTrouble Online" material and is NOT a candidate for
> this page** — see `manualevidence/H-ranks.md`.

**2. S114 — narrow the "ranks surfaced outside lab" clause.** Suggested
edit to that cell:

> …achievement list page, ranks surfaced outside lab **(the community
> 12-rank ladder is post-era — see `manualevidence/H-ranks.md`; what
> remains unknown is whether the CLASSIC site surfaced experience or rank
> anywhere beyond `?lab` and the `Top 10 Exp.` box at
> `srv/index.php:1113`)**

**3. Add a new row to §A (Game-page chrome).** Proposed:

> | S115 | **In-SWF HUD row (tank render, name label, score numeral)** | page-look | Nothing in the repo describes the inside of the 712×490 stage. First look now held: per-player 3/4 tank render + name label beneath + grey score numeral placed inboard; grey `+` divider between sides; gear + speaker icons far left; maze number / author / `version 4.0` far right. Measured in `manualevidence/H-ranks.md` | manual-evidence `Game/H-classic-gameplay-1p-vs-laika.png`, `F-gameplay-maze-61-crates.png`, `F-gameplay-three-guests-maze-crop.png`, `H-hud-crop-score-10-with-transient.png`, `H-hud-crop-score-10-clean.png` | Any gameplay video at native scale, un-stretched | HIGH |

**4. Add a new row to §I (Statistics / Lab / popup subpages).** Proposed:

> | S116 | **In-era evidence that ranks were surfaced outside `?lab`** | page-look / flow | Post-era 12-rank ladder ruled out (H-ranks.md). Open: did the classic site ever show a rank/experience badge on the front page, in the forum (`forumTank-` scale varies per user — S59), or on a user card (S6)? | `srv/index.php:13845-13856`; `:1113`; `:9462-9479` | Any dated 2017-2018 frame with a chevron/star device or one of the twelve names on `tanktrouble.com` | LOW |

### `DECISIONS.md` (append-only — a new entry, not an edit)

> **2026-08-04 — community rank ladder is post-era; not adopted.**
> A twelve-milestone rank ladder (Dog Food → Mad Scientist, thresholds
> 0/5/10/25/50/100/150/250/500/1000/1500/2000, the top three written
> `1.000`/`1.500`/`2.000` with European dot-thousands) and
> three league cards (beginner / Soldier / Scientist, 4 ranks each,
> chevrons = league and stars = position within league) arrived in
> manual-evidence. **Rejected as out-of-era**, on five converging grounds:
> (a) `ranks.txt` scopes itself to "TankTrouble Online", which
> `srv/index.php:6988-6990` defines as the separate `beta.tanktrouble.com`
> product; (b) zero of the twelve names occurs in `srv/index.php`, nor do
> "ranked"/"league"/"leaderboard"/"matchmaking"/"tank info box";
> (c) the classic metric is *experience*, formula published at
> `srv/index.php:9479`, surfaced only as the `?lab` link
> "Tank Rank by Experience" (`:13848`) and the `Top 10 Exp.` header
> (`:1113`); (d) the cards use the custom TankTrouble display face, which
> `srv/index.php:6657` records shipping to Online BETA on 2016-05-25 and
> which the classic page never declares (`@font-face` count = 0; only
> `font-family: Courier`); (e) manual-evidence `Game/F-html5-generation-contrast-case.png` shows the
> modern HTML5 site carrying a "Tank Rank has been Deployed" promo box and
> a HUD with rank chevrons after each username.
> `srv/tankRanks/index.php` stays a 501 stub. Analysis:
> `manualevidence/H-ranks.md`.
>
> Also recorded from the same evidence: manual-evidence
> `Game/H-classic-gameplay-1p-vs-laika.png` shows the game page with
> `Copyright www.purup.com 2007 – 2015` **and** a second credit line
> ("Design: Mads Purup, Programming: Brian Bunch Christensen, Server:
> Søren Boll Overgaard"). The era-final bytes at `srv/index.php:328-330`
> have neither: one line, `2007 – 2018`. That dates the frame to ≈2015 and
> identifies a page-chrome change between generations. No served byte
> changes.

### `LEDGER.tsv`

No new rows. **Nothing from this topic is served.** If the images are
archived for the record, they belong under `archive/` with M2 rows and
provenance noted as *community-wiki-derived / post-era, retained as
counter-evidence*, and must never be referenced from `srv/`.

Optionally, extend the **notes** field of row 225 (`srv/tankRanks/index.php`)
with: `content unknown; community 12-rank ladder is post-era, see
manualevidence/H-ranks.md`.

---

## Appendix — how each number was obtained

All measurements were produced with Python 3.11 + Pillow 12.2.0 + NumPy
2.4.4 + SciPy, reading the staged files read-only. The techniques used:

* **Colour sampling** — direct indexing into the RGB array, printed as hex;
  no averaging unless stated ("mean", "median", "p10/p90" are labelled).
* **Component finding** — `scipy.ndimage.label` on a stated boolean mask,
  with the mask written out in the text (e.g. the gold mask
  `r>150 & g>110 & b<120 & r−b>70 & g−b>40`), filtered by pixel count.
* **Run lengths** — thresholded row/column scans, consecutive runs
  collected, used for the maze lattice and the card dividers.
* **Axis-fraction dividers** — a column counts as a rule if > 80 % of its
  pixels are below luminance 80; this is what separated the 9 px vertical
  rule from insignia pixels that a single-row scan mistook for it.
* **Frame alignment** — exhaustive integer-offset search over ±12 px
  minimising mean absolute difference on the overlap, cross-checked
  against independent mask bounding boxes.
* **Frame differencing** — `PIL.ImageChops.difference` on the aligned
  overlap, then thresholded and bounded.
* **Upscaling** — `Image.NEAREST` for reading pixel structure,
  `Image.LANCZOS` for reading shapes; both were produced for every small
  crop and both were consulted.
* **ASCII pixel dumps** — for the two tiny crops, luminance mapped to a
  ten-level ramp and printed with x/y rulers, which is how the digits were
  read at three separate thresholds (140 / 170 / 190) rather than eyeballed.
* **De-stretching** — `H-classic-gameplay-1p-vs-laika.png` was resampled to `width / 1.497` before
  any silhouette comparison, and that factor was derived from the maze
  lattice (115.0 px horizontal pitch / 76.8 px vertical pitch), then
  sanity-checked against two un-stretched classic frames whose wall runs
  measure 6–7 px in both axes.

Where a number could not be pinned, the range is given and the claim is
tagged `[UNCERTAIN]` with the shot that would settle it.
