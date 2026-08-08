# Manual evidence — visual analysis index

Analysis of the 99 images and 5 text notes in `manualevidence/`, captured by
the repo owner on **2026-08-04 between 16:22 and 17:46 NZST**, against the
classic-tanktrouble.com reconstruction in
[`../../../`](../../../README.md).

Eleven topic documents, one analyst each. Every assigned file is analysed in
exactly one document; nothing was skipped.

- [`../../../README.md`](../../../README.md) — the reconstruction's rules
- [`../../standards/VISUAL-EVIDENCE-WANTED.md`](../../standards/VISUAL-EVIDENCE-WANTED.md) — the want-list these documents feed (entries 1–10, S1–S114)
- [`../../standards/MAZECREATOR-VISUAL-SPEC.md`](../../standards/MAZECREATOR-VISUAL-SPEC.md) — the pinned constants several findings below contradict
- [`../../../DEDUCE.md`](../../../DEDUCE.md) · [`../../../DECISIONS.md`](../../../DECISIONS.md) · [`../../../LEDGER.tsv`](../../../LEDGER.tsv)

**Nothing in the reconstruction was edited.** These documents are analysis
only. Each one ends with a *Recommended edits to existing docs (not applied)*
section; applying them is a separate, deliberate act.

---

## Read this before using any finding

### 1. This corpus is not one era. It is at least five.

The repo targets **2017–2018**. Analysts dating frames independently — by
footer copyright year, by the monotonic Scrapyard and Visits counters, by nav
tab count, by ad creative, by the in-stage `version` watermark — found the
corpus spans roughly **2013 to post-classic HTML5**, and that *most* of it
sits outside the target window:

| Generation | Where it turns up | Admissible for the rebuild? |
|---|---|---|
| ~2013 (`version 3.7`, 5-tab nav, no shop) | [E](./E-front-page-chrome.md), [F](./F-gameplay-hud-and-chat.md), [K](./K-forum.md) | Only as *change* evidence — never as era look |
| Feb 2015 (Kickstarter countdown, `?forum`) | [K](./K-forum.md) | Same |
| 2015–2016 (`2007 – 2015`/`2007 – 2016` footers) | [C](./C-maze-slots-and-save-flow.md), [D](./D-garage-userpanel-and-paint.md), [E](./E-front-page-chrome.md) | Same |
| **2017–2018 target window** | [D](./D-garage-userpanel-and-paint.md) (Oct 2018), [E](./E-front-page-chrome.md) (E8), [J](./J-tell-a-friend.md) | **Yes** |
| Post-classic HTML5 / "Online BETA" | [F](./F-gameplay-hud-and-chat.md), [H](./H-ranks.md), [I](./I-weapons-and-laika.md) | **No — actively keep out** |

One consequence deserves its own line, from [F](./F-gameplay-hud-and-chat.md):
**page chrome and stage content date separately.** A frame whose sidebars are
from 2013 can still carry `TankTrouble_v4.0.swf` inside the stage — the same
`O`-tier binary the era page embeds (LEDGER row 163, `srv/index.php:404`). So
*in-stage* measurements from a `version 4.0` frame are admissible about the era
build even when the page around them is not. Check which layer a finding came
from before using it.

### 2. Provenance ceiling: M2, never O.

Confirmed in-frame, not assumed: a Chrome "**youtube.com** is now full screen"
toast and a `5:03 / 5:10` scrub bar ([D](./D-garage-userpanel-and-paint.md)),
YouTube transport controls and a `0:06 / 13:23` timecode
([E](./E-front-page-chrome.md)), burned-in video title cards and a subtitle
track ([C](./C-maze-slots-and-save-flow.md)), a Screencast-O-Matic watermark
and a recorder click-highlight ring ([F](./F-gameplay-hud-and-chat.md),
[C](./C-maze-slots-and-save-flow.md)). These are frames *of* the site, not its
bytes. Per guide §6.5 every LEDGER row derived from them is **M2 at best**, and
needs URL, uploader, upload date and timestamp. None of that metadata is
recoverable from the crops — **the owner must supply the source video URLs**,
and until he does these documents cite pixels with no citable source.

### 3. File mtimes are save times, not frame times.

All 104 mtimes fall inside 84 minutes of 2026-08-04. They order what the owner
was stepping through; they say nothing about the footage. Where sequence
mattered, analysts corroborated it against an in-frame clock rather than
trusting it — [C](./C-maze-slots-and-save-flow.md) used the Scrapyard
flip-counter to confirm its nine frames are strictly monotonic, and
[J](./J-tell-a-friend.md) used the same counter to prove its three frames are
in the **reverse** of their save order.

### 4. Confidence tags are load-bearing.

Every substantive claim carries one: `[OBSERVED]` (point at it), `[MEASURED]`
(a number a script printed), `[INFERRED]` (a reasoned step, with its
falsifier), `[UNCERTAIN]` (deniable at this resolution), `[NOT VISIBLE]`
(absent — which keeps the want-list honest). Roughly 700 `[MEASURED]` claims
across the eleven documents. **Do not promote a tag when quoting a finding.**

### 5. Video-authored overlays are not evidence.

Much of this corpus is frame-grabbed from YouTube, and the uploaders drew on
top of it. Anything the *video author* added — rather than the *site* drew —
carries no evidential weight and is not transcribed, measured or reasoned
from. It is recorded only where it **occludes** something, because that bounds
what can be read.

| Overlay | Where | Handled in |
|---|---|---|
| **Comic speech bubbles** — a *TankTrouble comics* video in which the tank talks | `UI/D-paint-standard-palette-comic-overlay.png`, `D-paint-halloween-toolbox-comic-overlay.png`, `D-paint-chip-row-scrolled-one-step.png`, `D-paint-gold-toolbox-two-chips.png` | [D](./D-garage-userpanel-and-paint.md) — excluded; occlusion footprint only |
| Standalone motion-graphic **rank / league cards** — no UI chrome of any kind | `Game/F-video-card-beginner-league.png`, `F-video-card-beginner-league-caption.png`, `F-video-card-scientist-league.png`, `F-video-card-scientist-league-caption.png`, `Game/H-video-title-card-tank-trouble-ranks.png` | [H](./H-ranks.md), [F](./F-gameplay-hud-and-chat.md) |
| Video **thumbnail art** ("Tank Trouble Premium" crates) | `UI/E3-video-thumbnail-premium-crates.png` | [E](./E-front-page-chrome.md) |
| Burned-in **video title cards** | `UI/C-garage-before-maze-panel.png`, `UI/C-empty-slot-maze3-cam12win.png` | [C](./C-maze-slots-and-save-flow.md) |
| **Subtitle / caption track** ("You're a manager") | `UI/C-maze-icon-clicked.png` | [C](./C-maze-slots-and-save-flow.md) |
| Screen-recorder **click halo** (yellow ring) | many frames | [C](./C-maze-slots-and-save-flow.md), [D](./D-garage-userpanel-and-paint.md), [F](./F-gameplay-hud-and-chat.md) — masked out of every measurement |
| **Screencast-O-Matic watermark** | `UI/F-gameplay-2013-page-round-countdown.png`, `F-gameplay-2013-page-four-tanks.png` | [F](./F-gameplay-hud-and-chat.md) |
| **YouTube player chrome** and timecodes | `UI/E6-frontpage-2013-version-3-7.png`, `D-garage-2018-scrub-bar-visible.png` | [E](./E-front-page-chrome.md), [D](./D-garage-userpanel-and-paint.md) |
| Browser **fullscreen toast** | `D-garage-2018-url-bar-youtube-toast.png` | [D](./D-garage-userpanel-and-paint.md) |
| **Picture-in-picture** inset | `UI/A-editor-howto-step6-or-just-click.png` | [A](./A-maze-editor-toolbar.md) |

**The converse trap is just as real.** TankTrouble's own game UI is drawn in a
hand-made, slightly skewed paper style that *looks* like an annotation. Three
things were checked and are **site UI, not overlays**:

- the **skewed green chat bar** and its stacked message list — semi-transparent
  (maze walls read through it), with a live text caret ([F](./F-gameplay-hud-and-chat.md));
- the tilted white **round-countdown card** in `UI/F-gameplay-2013-page-round-countdown.png` — same drawn
  style as the chat bar ([F](./F-gameplay-hud-and-chat.md));
- the **achievement unlock float** in `UI/B-frontpage-achievement-unlock-float.png` — see the
  correction under §Corrections below.

So "it looks hand-drawn" is not a test. The tests that worked: does it appear
in more than one unrelated session; does page content read *through* it; does
it carry live state (a caret, a server-composed `<username>:` prefix); and does
its type ramp match the page's own chrome.

---

## The eleven documents

| Doc | Files | What it settles |
|---|---|---|
| [A — mazeCreator toolbar, tool icons, title typography](./A-maze-editor-toolbar.md) | 11 | Tool strip is **3 buttons**; `mazeConstructToolSelect` + two `Deselect` states recovered (Deselect is *exactly* greyscale, max R−B delta **1**); ✗/✓ colours; title `#666666` and watermark geometry confirmed against the spec; Verdana/Tahoma excluded for the title face |
| [B — mazeCreator editing interaction](./B-maze-editor-interaction.md) | 18 | **VE 5 answered in full**: drag-paint yes, hover wall preview yes, cursor ghost yes. VE 6 answered: the lattice **re-fits and re-centres live**. Floor-tone question narrowed |
| [C — maze preview slots, transitions, save flow](./C-maze-slots-and-save-flow.md) | 10 | **Three maze slots**, empty slot art, thumbnails are true mini-renders; save flow has **no spinner and no dialogue**; open transition is width-then-height, two sequential axes |
| [D — garage, userpanel, paint facility](./D-garage-userpanel-and-paint.md) | 16 | First pixels of the want-list's "largest single hole": panel box model measured to CSS px, four icons described, accessory toolboxes and scroll behaviour, three sign-up copy generations |
| [E — front-page and site chrome](./E-front-page-chrome.md) | 8 | 6-tab nav strip and 75 px pitch; a Scrapyard plate **caught mid-flip**; Halloween skin in 2016 *and* 2018; the advent-calendar overview; logged-in Top-10 Friends table; AdSense layout confirmed not to reflow |
| [F — in-game rendering, HUD, chat](./F-gameplay-hud-and-chat.md) | 14 | In-round floor is a **single flat `#e5e5e5`**, not the editor's two-tone mix; and a **complete chat system** that appears in no held byte, no ledger row and no want-list entry |
| [G — achievements](./G-achievements.md) | 4 | The achievements list is the **`openStats` sub-view of the user panel**, not a page; full **14-item catalogue transcribed**; locked vs unlocked treatment measured; progress bars found |
| [H — ranks](./H-ranks.md) | 6 | **Verdict: post-era. Do not adopt.** Five independent lines of evidence, zero dissenting; what would overturn it is stated |
| [I — weapon icons, roster, Laika, the typeface](./I-weapons-and-laika.md) | 11 | Icons are 2× upscales of a 45×42 native raster, 100 % greyscale; roster gap is **Shotgun only**; `TankTrouble.ttf` **authenticated as first-party Purup material but not evidenced as classic-served** |
| [J — the Tell A Friend popup](./J-tell-a-friend.md) | 4 | A 501 stub rendered and fully transcribed; client area **460.1 CSS px** against `width=460` in source; the copy is **not** name-templated — the task's own hypothesis, disproved |
| [K — the Tank Owner's Forum](./K-forum.md) | 1 | The first forum pixel the project has ever had. It is the **preview list**, and it is **Feb 2015** — so most of S57–S68 stays open, accurately |

---

## Where documents converge independently

Convergence between analysts who could not see each other's work is the
strongest signal in this set.

**The editor cell size is fitted, not fixed.** [A](./A-maze-editor-toolbar.md)
derived `cell = min(576/(w+2), 320/(h+2))` from three sessions;
[C](./C-maze-slots-and-save-flow.md) reached the same law independently from
four mazes (fit ≤0.26 %); [B](./B-maze-editor-interaction.md) then *tested* it
on growth frames and measured a **25 % pitch drop inside a single 27-second
window** as a maze grew 11→18 columns, and saw the `+2` margin ring directly as
a hover ghost one cell outside the maze. `CELL = 32` in
[`mazecreator-visual-spec.md`](../../standards/MAZECREATOR-VISUAL-SPEC.md)
is not a constant — it is what the fit returns for the 8-row maze in the single
screenshot the spec was derived from. `MazeRenderer.as` is owed a rewrite, not
a patch.

**The grey heading above the stage is the username, not the maze name.** Found
by [A](./A-maze-editor-toolbar.md) across three accounts, confirmed by
[B](./B-maze-editor-interaction.md) on two more, and proved outright by
[C](./C-maze-slots-and-save-flow.md), which caught the identical pixel row in
the collapsed garage panel *while the SWF was still at α≈0*. `Editor.as:338` is
contradicted three times over.

**The corpus holds at least three distinct typefaces.**
[A](./A-maze-editor-toolbar.md) measured the editor title as Arial/Helvetica
class; [I](./I-weapons-and-laika.md) measured the wiki-corpus caption face at
x/cap 0.684–0.698 and `TankTrouble.ttf` at 0.7848 display weight, excluding the
font from being either of the other two. They must not be conflated.

**"Online BETA" is the seam.** [H](./H-ranks.md) dates the rank ladder to it,
[I](./I-weapons-and-laika.md) dates the custom font's announcement to it
(`srv/index.php:6657`, news 2016-05-25), [F](./F-gameplay-hud-and-chat.md)
finds the chat system on the classic stage but nowhere in held bytes, and
[E](./E-front-page-chrome.md) tracks the sidebar box through **four** states
(`Online BETA / BETA Membership required` → `OPEN BETA` + live countdown →
`Test online battles now!` → the era-final `PLAY ONLINE`). Anything reached
through that box is a different product.

---

## Proposed want-list status changes

Proposed only — [`VISUAL-EVIDENCE-WANTED.md`](../../standards/VISUAL-EVIDENCE-WANTED.md)
is unedited. Each document argues its own case; go there before acting.

| Entry | Now | Proposed | Doc |
|---|---|---|---|
| VE 1 — tool icon states | PARTIAL (3/6) | **PARTIAL (5/6)** — only `tankSpawnToolSelect` unseen | [A](./A-maze-editor-toolbar.md) |
| VE 2 — editor error panel | WANTED | **WANTED** — verified absent in all frames | [A](./A-maze-editor-toolbar.md), [C](./C-maze-slots-and-save-flow.md) |
| VE 3 — save flow after ✓ | WANTED | **FETCHED** — no spinner, no dialogue, tools vanish, preview returns | [C](./C-maze-slots-and-save-flow.md) |
| VE 4 — maze preview / garage mode | WANTED | **FETCHED** — three slots, empty-slot art, hover glow, mini-renders | [C](./C-maze-slots-and-save-flow.md) |
| VE 5 — editing interaction semantics | WANTED | **FETCHED** — all three questions answered | [B](./B-maze-editor-interaction.md) |
| VE 6 — maze placement rule | PARTIAL | **FETCHED** — live re-fit and re-centre proved | [B](./B-maze-editor-interaction.md) |
| VE 7 — title / watermark typography | PARTIAL | **PARTIAL** — face narrowed, title source corrected | [A](./A-maze-editor-toolbar.md), [I](./I-weapons-and-laika.md) |
| VE 8 — fade transitions | PARTIAL | **PARTIAL** — two sequential axes confirmed | [C](./C-maze-slots-and-save-flow.md) |
| VE 8a — floor tone pattern | WANTED | **PARTIAL** — narrowed to the editor only | [B](./B-maze-editor-interaction.md), [C](./C-maze-slots-and-save-flow.md) |
| VE 10 — selected nav tabs | PARTIAL | **PARTIAL** — no raised NEWS/SHOP/FORUM tab in any frame | [E](./E-front-page-chrome.md), [K](./K-forum.md) |
| S3 — Top-10 Friends logged in | MED | **FETCHED** | [E](./E-front-page-chrome.md) |
| S5 — achievement unlock content | MED | **PARTIAL** — 14-item catalogue recovered **and the unlock float captured in situ**; only the 5 s glow in motion still missing | [G](./G-achievements.md), [B](./B-maze-editor-interaction.md) |
| S14 — scrapyard counter in motion | HIGH | **PARTIAL** — mid-flip frame caught; direction still open | [E](./E-front-page-chrome.md) |
| S16 / S106 — seasonal boxes | MED/HIGH | **PARTIAL** | [E](./E-front-page-chrome.md) |
| S18 — advent-calendar UI | MED | **PARTIAL** — overview banner, 25 sprites | [E](./E-front-page-chrome.md) |
| S23 — AdSense as rendered | HIGH | **DONE** — layout does not reflow | [E](./E-front-page-chrome.md), [D](./D-garage-userpanel-and-paint.md) |
| S24 — the userpanel itself | MED | **FETCHED** — box model measured | [D](./D-garage-userpanel-and-paint.md) |
| S25 — userpanel icon strip | MED | **PARTIAL** — 4 of 5 icons; SherifStar confirmed absent | [D](./D-garage-userpanel-and-paint.md), [C](./C-maze-slots-and-save-flow.md) |
| S26 / S28–S32 — paint facility | LOW–MED | **PARTIAL** | [D](./D-garage-userpanel-and-paint.md) |
| S34 — account settings form | MED | **WANTED** — every form in the corpus is the *sign-up* form | [D](./D-garage-userpanel-and-paint.md) |
| S37 — garage → maze transition | MED | **FETCHED** | [C](./C-maze-slots-and-save-flow.md) |
| S39 — maze-creator toolbar row | MED | **FETCHED** | [A](./A-maze-editor-toolbar.md) |
| S42 — cursor over the editor stage | — | **PARTIAL** — no custom cursor art; a stage-drawn ghost exists | [B](./B-maze-editor-interaction.md) |
| S43 — multiple maze slots | MED | **FETCHED** — three | [C](./C-maze-slots-and-save-flow.md) |
| S44 / S45 / S48 — delete, warning, limits | LOW–MED | **WANTED** — absence recorded in every frame | [B](./B-maze-editor-interaction.md), [C](./C-maze-slots-and-save-flow.md) |
| S46 — garage maze-icon art | MED | **FETCHED** | [C](./C-maze-slots-and-save-flow.md) |
| S57 — forum thread-preview list | HIGH | **PARTIAL** — recovered, but Feb 2015 | [K](./K-forum.md) |
| S58–S68 — forum internals | HIGH–LOW | mostly **WANTED**; S58/S59 → **PARTIAL** | [K](./K-forum.md) |
| S83 — `/tankRanks/` popup | LOW | **WANTED** — and now the decisive test for the rank question | [H](./H-ranks.md) |
| S86 — `/tellAFriendMail/` popup | LOW | **PARTIAL** — rendered, transcribed, geometry pinned | [J](./J-tell-a-friend.md) |
| S103 — `laika02.swf` behaviour | MED | **WANTED** — and under-scoped; `srv/Assets/Laika.swf` (LEDGER 4) is unmentioned | [I](./I-weapons-and-laika.md) |
| S105 — frozen live regions | HIGH | **PARTIAL** — format constant 2013→2018 | [E](./E-front-page-chrome.md) |
| S108 / S17 — typography | LOW | **WANTED** — narrowed at no cost | [I](./I-weapons-and-laika.md) |
| S114 — unknown-existence UI | MED | **PARTIAL** — achievements list identified as `openStats` | [G](./G-achievements.md) |

### New wants proposed

An in-game **chat system** on the classic stage, in no held byte
([F](./F-gameplay-hud-and-chat.md)) — the highest-value new item, and its
first recovery step costs nothing because the SWF that contains it is already
in the repo. Plus: `TankTrouble.ttf` provenance and its U+2500–250F + U+2605
coverage fingerprint, an in-game settings menu, crate appearance
([I](./I-weapons-and-laika.md)); refetching `/tellAFriendMail/images/`
([J](./J-tell-a-friend.md)); editor growth and refit behaviours
([B](./B-maze-editor-interaction.md)); a three-user garage stack
([D](./D-garage-userpanel-and-paint.md)).

---

## Corrections these documents make to their own briefs

Recorded because a brief that misdescribes evidence propagates.

- `Game/F-video-card-beginner-league-caption.png` is a **rank card**, not a login sidebar; the "Access Online
  BETA" panel is in `Game/F-gameplay-2015-page-beta-sidebar.png`. There is no clone-rehost watermark in
  the corpus — the bottom-left text is Screencast-O-Matic's.
  ([F](./F-gameplay-hud-and-chat.md))
- The Sunglasses / Tell-A-Friend prose is in `UI/tellafriendpopup.txt`, not
  `acheivements.txt`. `acheivements.txt` is a **transcription of the pixels**
  with at least one outright error. ([G](./G-achievements.md))
- `Game/H-classic-gameplay-1p-vs-laika.png` is a gameplay frame, not a league card.
  ([H](./H-ranks.md))
- `J-popup-send-pressed-still-open.png` does **not** show the popup closed — it shows
  it open with the Send button in a disabled render. ([J](./J-tell-a-friend.md))
- `manualevidence/TankTrouble.ttf` was missing from the first staging; the
  document was revised against the real bytes, and the earlier "presumed
  fan-made" reading is withdrawn wholesale rather than patched.
  ([I](./I-weapons-and-laika.md))
- The panel over the front-page headline in `UI/B-frontpage-achievement-unlock-float.png` was first
  called "a chat bubble overlay". It is the **achievement unlock float** — site
  UI, and the exact thing S5 says was never captured. It reads
  `Hallowed Be Thy Name` / `mr_enderman: You trick'r'treated your way to new
  swag!` with the full-colour jack-o'-lantern icon overhanging the panel's top
  edge. That resolves `achievement_cb`'s open ambiguity in favour of
  `<name>: <You…>` over `Achievement: <You…>`, and the strings match
  [G](./G-achievements.md)'s panel transcription verbatim — the same copy
  attested on two independent surfaces.
  ([B](./B-maze-editor-interaction.md), [G](./G-achievements.md))
- The four `foxter` paint frames carry **comic speech bubbles** from a
  *TankTrouble comics* video. Their content was transcribed in the first pass;
  it has been **removed**. Only the paint facility behind them is analysed, and
  the palette finding (toolbox selection drives the can colours) rests on pixels
  alone — the open pumpkin toolbox and an all-Halloween accessory row.
  ([D](./D-garage-userpanel-and-paint.md))

## Housekeeping the corpus itself needs

- ~~`RC_rocket.webp` sits in the **reconstruction's root**~~ — **done.** It has
  been moved in beside its six siblings as
  `Game/I-icon-rc-rocket.webp`. The underlying gap is not fixed: it still has
  **no LEDGER row**, and gate D as documented walks only `srv/`, so a stray
  binary in the repo root **would not be caught**. Widening that walk is still
  owed. ([I](./I-weapons-and-laika.md))
- `H-classic-gameplay-1p-vs-laika.png` (`Game/`) and
  `H-classic-gameplay-1p-vs-laika-duplicate.png` (`UI/`) are the same bytes,
  same size, same mtime. 99 image files, 98 distinct — the `-duplicate` suffix
  now says so on sight. Deleting one is safe; nothing cites the `UI/` copy.
- Five text notes (`acheivements.txt`, `Game/ranks.txt`, `Game/weapons.txt`,
  `UI/B-owner-note-spawn-icons.txt`, `UI/tellafriendpopup.txt`) are the owner's or
  wiki prose, not captures. They are graded below the pixels throughout, and
  where they conflict with pixels the pixels win.

---

## Appendix — rename map

Every evidence image was renamed on 2026-08-04 from its original
Windows-clipboard GUID or ad-hoc name to a descriptive one, prefixed with the
letter of the document that analyses it. Nothing was re-cropped, re-encoded or
altered — only renamed, so hashes are unchanged.

Two notes on reading this table. The letter prefix marks **which document owns
the analysis**, not the only document that cites the file: several frames are
cross-referenced by two or three analysts, and a few sit in a topic whose
letter is not the obvious one (the beginner and scientist league cards are
`F-` because [F](./F-gameplay-hud-and-chat.md) identified them, while the
soldier card is `H-`). And `E1`–`E8` keep the numbering
[E](./E-front-page-chrome.md) uses internally for its eight frames.

**Original names are preserved in the documents.** Each file-by-file section
now carries a *(was `oldname`)* marker after its heading, so the analyses that
test the owner's own filename claims — "can drag it to create walls
continuously", "empty maze is like this, maze 3" — still point at the name
that made the claim.

The five text notes were left alone (`acheivements.txt`, `Game/ranks.txt`,
`Game/weapons.txt`, `UI/tellafriendpopup.txt`) except `New Text Document.txt`,
which named nothing at all and is now `UI/B-owner-note-spawn-icons.txt`.
`TankTrouble.ttf` keeps its name: the name *is* the claim
[I](./I-weapons-and-laika.md) examines.

| New name | Was | Doc |
|---|---|---|
| `Game/F-gameplay-2015-page-beta-sidebar.png` | `{B77B6A43-B2D1-4D46-9BDD-880073BB9C63}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `Game/F-gameplay-maze-61-crates.png` | `{60BCFBE2-EF13-4549-A040-8BAA1119828E}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `Game/F-gameplay-three-guests-maze-crop.png` | `{C276DC91-7517-42D5-8AC9-59CD05FC525A}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `Game/F-html5-generation-contrast-case.png` | `{F11210C7-8FE2-441F-938C-962FE5591AD3}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `Game/F-video-card-beginner-league-caption.png` | `{9DF5F575-CCBE-4C44-A576-EAC0B1AF8251}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `Game/F-video-card-beginner-league.png` | `{47111A69-3425-4628-BA3A-F77E1D02E573}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `Game/F-video-card-scientist-league-caption.png` | `{91B492F8-C25F-440A-A1CF-5F3105D1AEAA}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `Game/F-video-card-scientist-league.png` | `{46F00358-FE88-40FF-9150-6A21DBA00B38}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `Game/G-achievements-panel-full.webp` | `Achievements.webp` | [G](./G-achievements.md) |
| `Game/H-classic-gameplay-1p-vs-laika.png` | `{345B2DAE-524B-4F4B-9505-42E8DDE5EC8B}.png` | [H](./H-ranks.md) |
| `Game/H-hud-crop-score-10-clean.png` | `{E9B6C77D-D098-42E5-80C6-00B8D37A19A9}.png` | [H](./H-ranks.md) |
| `Game/H-hud-crop-score-10-with-transient.png` | `{327420A9-A461-476D-AF80-ED41F6A7CB16}.png` | [H](./H-ranks.md) |
| `Game/H-league-card-soldier.png` | `{3E6BCAF8-943C-4431-8340-49370DDF366D}.png` | [H](./H-ranks.md) |
| `Game/H-video-title-card-tank-trouble-ranks.png` | `ranks.png` | [H](./H-ranks.md) |
| `Game/I-icon-booby-trap.webp` | `Booby_trap.webp` | [I](./I-weapons-and-laika.md) |
| `Game/I-icon-death-ray.webp` | `Death_ray.webp` | [I](./I-weapons-and-laika.md) |
| `Game/I-icon-frag-bomb.webp` | `Frag_Bomb.webp` | [I](./I-weapons-and-laika.md) |
| `Game/I-icon-gatling-gun.webp` | `Gatling_gun.webp` | [I](./I-weapons-and-laika.md) |
| `Game/I-icon-laser.webp` | `Laser.webp` | [I](./I-weapons-and-laika.md) |
| `Game/I-icon-rc-rocket.webp` | `RC_rocket.webp` | [I](./I-weapons-and-laika.md) |
| `Game/I-icon-rocket-homing-missile.webp` | `Rocket.webp` | [I](./I-weapons-and-laika.md) |
| `Game/I-laika-boss-artwork.webp` | `Laika.webp` | [I](./I-weapons-and-laika.md) |
| `Game/I-weapon-toggle-panel.webp` | `Weapons.webp` | [I](./I-weapons-and-laika.md) |
| `UI/A-editor-howto-step6-or-just-click.png` | `6orjustclick.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-editor-panel-highlight-outside-maze.png` | `{851E5C49-BBC4-4CE1-B061-D5A37CC9651D}.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-editor-panel-kill-the-player.png` | `{C2BC325C-D127-4F7B-A66F-D188E2B42ABA}.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-editor-panel-primary-source-hq.png` | `mazeditorhq.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-editor-preview-mode-lone-tick.png` | `{5243A3F8-38F5-4DB2-8589-17C8F75A505A}.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-maze-crop-4x4-hollow-centre.png` | `{4CEE81F1-5F4D-4B08-9AEC-CF6BE2CA6820}.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-maze-crop-cell-highlight-on-spawn.png` | `{48554A6F-E546-42A0-B785-2824B4B4D7E3}.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-maze-crop-wall-highlight-vertical.png` | `{BFBF9223-3000-4A0B-AF02-70983B4C0C3E}.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-toolbar-confirm-click-midfade.png` | `clickonconfirm.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-toolbar-row-crop-run-around-the-world.png` | `{7EB8BFD4-E208-4674-A24A-B5879F8FEBC5}.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/A-toolbar-three-tool-icons-visible.png` | `{145AE34F-9EA7-4B2A-BF15-DFF015A87A17}.png` | [A](./A-maze-editor-toolbar.md) |
| `UI/B-crate-spawn-placement-effect.png` | `placingboxescreatethiseffect.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-editor-howto-step3-epic-twister.png` | `3.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-editor-howto-step4-lag-note.png` | `4shouldntbethislaggy-sourcescomputerisslow.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-editor-howto-step5-nearly-solid.png` | `5.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-editor-howto-step7-drag-paint-wall-run.png` | `7candragittocreatewallscontinuously.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-frontpage-achievement-unlock-float.png` | `beforetankrenders.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-frontpage-after-float-dismissed.png` | `aftertankrenders.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-hover-ghost-contains-cursor.png` | `selectedblock2.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-hover-ghost-in-margin-ring.png` | `{FE109AA4-CB09-4B9D-AEE2-EFF3223B7D59}.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-hover-ghost-on-cell.png` | `mazeditor-selectedblockistheblockonmousehover.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-maze-growth-mechanism.png` | `expandingwallsbyclicking.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-maze-growth-step1.png` | `expandingwallsbyclicking1.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-maze-growth-step2-width-term-binds.png` | `expandingwallsbyclicking2.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-owner-note-spawn-icons.txt` | `New Text Document.txt` | [B](./B-maze-editor-interaction.md) |
| `UI/B-tank-spawn-placement-effect.png` | `placingtankscreatethiseffect.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-wall-slot-preview-horizontal.png` | `horizontalwall.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-wall-slot-preview-second-location.png` | `anotherwall.png` | [B](./B-maze-editor-interaction.md) |
| `UI/B-wall-slot-preview-vertical.png` | `selectedwall-smallbluebitbetweenblocks.png` | [B](./B-maze-editor-interaction.md) |
| `UI/C-after-confirm-preview-returned.png` | `afterrfadeinanimationcomplete.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/C-after-confirm-tools-hidden.png` | `afterclickingonconfirmbeforeanimationisfinished.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/C-editor-opened-on-slot1.png` | `fadeintomazeeditor.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/C-empty-slot-maze3-cam12win.png` | `emptymazeislikethis,maze3.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/C-garage-before-maze-panel.png` | `garage1.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/C-maze-icon-clicked.png` | `clickintomaze.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/C-open-transition-height-phase.png` | `secondanimationcardexpandsdown.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/C-open-transition-width-phase.png` | `firstanimationcardexpandsright.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/C-preview-boot-state.png` | `fadeintothispage.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/C-slot-hover-green-glow.png` | `selectmaze.png` | [C](./C-maze-slots-and-save-flow.md) |
| `UI/D-game-teaser-screen-not-garage.png` | `{D2FDA7ED-766D-43EF-9DEF-1A9380A364CA}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-garage-2018-scrub-bar-visible.png` | `garage2.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-garage-2018-url-bar-youtube-toast.png` | `garage3.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-garage-kickstarter-countdown-later.png` | `{44AB875B-556E-4C57-82F5-6C209ECB78DB}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-garage-kickstarter-eve-foxter25.png` | `garage.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-accessory-hover-bandana.png` | `click.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-accessory-hover-pirate-hat.png` | `click (2).png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-can-hover-violet-later.png` | `paint.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-can-hover-violet.png` | `{6BB20BAB-F536-4835-AA05-485EF95830FD}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-chip-row-scrolled-one-step.png` | `{3484955B-8535-4207-88D9-139691F86921}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-gold-toolbox-two-chips.png` | `{94759D97-DF31-429F-B3F8-857A7D0661CB}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-halloween-toolbox-comic-overlay.png` | `{4B3EFDCC-0F18-49A3-98A5-42D977D888AC}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-older-build-grid-expanded.png` | `{E62C5D8C-A919-4DF9-98A3-8909F6BBC9BA}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-older-build-grid-no-hover.png` | `{02E885A2-F8C7-40B4-8366-23A9BE4CAA53}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-paint-standard-palette-comic-overlay.png` | `{267995BB-A52F-4E42-8404-9965232F9302}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/D-userpanel-older-build-collapsed.png` | `{B53D30AB-BC36-4C1C-A61A-F0C196DA3B7C}.png` | [D](./D-garage-userpanel-and-paint.md) |
| `UI/E1-frontpage-2016-ads-filled.png` | `{B2424E7E-6BD9-4C82-81FF-1DA8621A4A27}.png` | [E](./E-front-page-chrome.md) |
| `UI/E2-frontpage-2016-halloween-countdown.png` | `{1711C6FA-DEF7-4BF9-9929-23E922BFD96E}.png` | [E](./E-front-page-chrome.md) |
| `UI/E3-video-thumbnail-premium-crates.png` | `{F9D54A4F-227A-40FC-82B6-EF757DFEBBD9}.png` | [E](./E-front-page-chrome.md) |
| `UI/E4-advent-calendar-overview-banner.png` | `{054A27F4-2171-41A2-BF64-B3C65F976AF0}.png` | [E](./E-front-page-chrome.md) |
| `UI/E5-left-sidebar-strip-two-user-cards.png` | `{4AEB403B-1EA9-467D-A910-229E048760FB}.png` | [E](./E-front-page-chrome.md) |
| `UI/E6-frontpage-2013-version-3-7.png` | `{1DA5327B-1A7B-4CD8-8582-E83744D7051C}.png` | [E](./E-front-page-chrome.md) |
| `UI/E7-teaser-control-chooser-2015.png` | `{85AAE09B-C1C4-4455-917C-7F9240741A7B}.png` | [E](./E-front-page-chrome.md) |
| `UI/E8-frontpage-2018-halloween-in-era.png` | `{5EC85EF6-FE4D-4A53-BB60-1F9FF21CDC37}.png` | [E](./E-front-page-chrome.md) |
| `UI/F-chat-bar-crop-1.png` | `{099B8E88-41F9-46DC-B4BD-552ABD22B5F4}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `UI/F-chat-bar-crop-2.png` | `{6AA2EF0E-D4C6-434A-AD4D-89676F01B1A1}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `UI/F-chat-bar-crop-3.png` | `{CB3725C2-5442-4122-8096-E15264753533}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `UI/F-chat-message-stack-in-stage.png` | `{5234E61B-0B7D-47D5-8E71-3CA300A31A82}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `UI/F-gameplay-2013-page-four-tanks.png` | `{FFAE5568-B5FA-478F-B166-4CA448E1C6C3}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `UI/F-gameplay-2013-page-round-countdown.png` | `{DE1A72E2-BEDF-4001-9ABE-C5BB117CED10}.png` | [F](./F-gameplay-hud-and-chat.md) |
| `UI/G-achievements-panel-fade-alpha-052.png` | `{41F86D44-32E6-4048-8AF5-493A7B7E233D}.png` | [G](./G-achievements.md) |
| `UI/G-achievements-panel-progress-bars.png` | `{CF0BFA0E-A568-4D70-81CC-4F6B236F2B7A}.png` | [G](./G-achievements.md) |
| `UI/H-classic-gameplay-1p-vs-laika-duplicate.png` | `{345B2DAE-524B-4F4B-9505-42E8DDE5EC8B}.png` | [H](./H-ranks.md) |
| `UI/J-popup-blank-fields.png` | `tellafriendmailpopup.png` | [J](./J-tell-a-friend.md) |
| `UI/J-popup-name-typed-george.png` | `tellafriendmailpopup1.png` | [J](./J-tell-a-friend.md) |
| `UI/J-popup-send-pressed-still-open.png` | `closesafteryouclicksend.png` | [J](./J-tell-a-friend.md) |
| `UI/K-forum-thread-preview-list-2015.png` | `{77910683-A2A9-45B8-A639-94A12325BDAE}.png` | [K](./K-forum.md) |

---

## Appendix — capture timeline

All times NZST on 2026-08-04. Save order, not footage order (see §3 above).
"Doc" is the topic document that analyses the file.

| Time | File | Doc |
|---|---|---|
| 16:22:54 | `Game/F-gameplay-three-guests-maze-crop.png` | F |
| 16:23:14 | `Game/F-gameplay-2015-page-beta-sidebar.png` | F |
| 16:24:11 | `Game/H-classic-gameplay-1p-vs-laika.png` | H |
| 16:24:11 | `UI/H-classic-gameplay-1p-vs-laika-duplicate.png` | H |
| 16:24:50 | `Game/F-gameplay-maze-61-crates.png` | F |
| 16:29:15 | `acheivements.txt` | G |
| 16:29:29 | `Game/I-weapon-toggle-panel.webp` | I |
| 16:29:41 | `Game/G-achievements-panel-full.webp` | G |
| 16:29:47 | `Game/I-laika-boss-artwork.webp` | I |
| 16:29:56 | `Game/I-icon-gatling-gun.webp` | I |
| 16:30:01 | `Game/I-icon-booby-trap.webp` | I |
| 16:30:07 | `Game/I-icon-laser.webp` | I |
| 16:30:16 | `Game/I-icon-death-ray.webp` | I |
| 16:30:21 | `.Game/I-icon-rc-rocket.webp` | I |
| 16:30:25 | `Game/I-icon-rocket-homing-missile.webp` | I |
| 16:30:30 | `Game/I-icon-frag-bomb.webp` | I |
| 16:31:46 | `Game/weapons.txt` | I |
| 16:32:32 | `Game/H-video-title-card-tank-trouble-ranks.png` | H |
| 16:34:05 | `Game/F-video-card-beginner-league.png` | F |
| 16:34:19 | `Game/F-video-card-beginner-league-caption.png` | F |
| 16:34:37 | `Game/H-league-card-soldier.png` | H |
| 16:35:38 | `TankTrouble.ttf` | I |
| 16:36:14 | `Game/F-video-card-scientist-league.png` | F |
| 16:36:31 | `Game/F-video-card-scientist-league-caption.png` | F |
| 16:37:38 | `Game/F-html5-generation-contrast-case.png` | F |
| 16:41:18 | `Game/H-hud-crop-score-10-with-transient.png` | H |
| 16:41:25 | `Game/H-hud-crop-score-10-clean.png` | H |
| 16:41:37 | `UI/E1-frontpage-2016-ads-filled.png` | E |
| 16:43:32 | `UI/E2-frontpage-2016-halloween-countdown.png` | E |
| 16:47:33 | `UI/K-forum-thread-preview-list-2015.png` | K |
| 16:48:02 | `UI/D-garage-kickstarter-eve-foxter25.png` | D |
| 16:51:42 | `UI/D-garage-kickstarter-countdown-later.png` | D |
| 16:52:09 | `UI/E3-video-thumbnail-premium-crates.png` | E |
| 16:53:12 | `UI/E4-advent-calendar-overview-banner.png` | E |
| 16:55:20 | `UI/F-chat-message-stack-in-stage.png` | F |
| 16:55:44 | `UI/F-gameplay-2013-page-round-countdown.png` | F |
| 16:56:05 | `UI/F-gameplay-2013-page-four-tanks.png` | F |
| 16:57:18 | `UI/C-garage-before-maze-panel.png` | C |
| 16:58:07 | `UI/C-maze-icon-clicked.png` | C |
| 16:58:41 | `UI/C-open-transition-width-phase.png` | C |
| 16:58:58 | `UI/C-open-transition-height-phase.png` | C |
| 16:59:13 | `UI/C-preview-boot-state.png` | C |
| 16:59:42 | `UI/C-slot-hover-green-glow.png` | C |
| 17:00:16 | `UI/C-editor-opened-on-slot1.png` | C |
| 17:00:43 | `UI/B-hover-ghost-on-cell.png` | B |
| 17:01:49 | `UI/B-hover-ghost-contains-cursor.png` | B |
| 17:02:06 | `UI/B-wall-slot-preview-vertical.png` | B |
| 17:02:46 | `UI/B-wall-slot-preview-second-location.png` | B |
| 17:03:26 | `UI/A-toolbar-row-crop-run-around-the-world.png` | A |
| 17:03:53 | `UI/E5-left-sidebar-strip-two-user-cards.png` | E |
| 17:04:37 | `UI/B-wall-slot-preview-horizontal.png` | B |
| 17:04:59 | `UI/A-toolbar-confirm-click-midfade.png` | A |
| 17:05:15 | `UI/C-after-confirm-tools-hidden.png` | C |
| 17:05:39 | `UI/C-after-confirm-preview-returned.png` | C |
| 17:07:34 | `UI/B-owner-note-spawn-icons.txt` | B |
| 17:08:46 | `UI/F-chat-bar-crop-1.png` | F |
| 17:08:54 | `UI/F-chat-bar-crop-2.png` | F |
| 17:09:01 | `UI/F-chat-bar-crop-3.png` | F |
| 17:09:45 | `UI/D-paint-standard-palette-comic-overlay.png` | D |
| 17:10:00 | `UI/D-paint-halloween-toolbox-comic-overlay.png` | D |
| 17:10:29 | `UI/D-paint-chip-row-scrolled-one-step.png` | D |
| 17:10:39 | `UI/D-paint-gold-toolbox-two-chips.png` | D |
| 17:11:31 | `UI/E6-frontpage-2013-version-3-7.png` | E |
| 17:12:05 | `UI/D-userpanel-older-build-collapsed.png` | D |
| 17:13:50 | `UI/D-paint-older-build-grid-expanded.png` | D |
| 17:13:57 | `UI/D-paint-older-build-grid-no-hover.png` | D |
| 17:14:12 | `UI/D-paint-accessory-hover-bandana.png` | D |
| 17:14:28 | `UI/D-paint-accessory-hover-pirate-hat.png` | D |
| 17:15:19 | `UI/D-paint-can-hover-violet.png` | D |
| 17:15:26 | `UI/D-paint-can-hover-violet-later.png` | D |
| 17:16:14 | `UI/D-game-teaser-screen-not-garage.png` | D |
| 17:16:19 | `UI/E7-teaser-control-chooser-2015.png` | E |
| 17:19:38 | `UI/J-popup-name-typed-george.png` | J |
| 17:20:10 | `UI/J-popup-blank-fields.png` | J |
| 17:20:57 | `UI/J-popup-send-pressed-still-open.png` | J |
| 17:23:15 | `UI/tellafriendpopup.txt` | J |
| 17:23:30 | `UI/G-achievements-panel-fade-alpha-052.png` | G |
| 17:23:39 | `UI/G-achievements-panel-progress-bars.png` | G |
| 17:26:19 | `UI/B-frontpage-achievement-unlock-float.png` | B |
| 17:26:46 | `UI/B-frontpage-after-float-dismissed.png` | B |
| 17:27:09 | `UI/E8-frontpage-2018-halloween-in-era.png` | E |
| 17:28:41 | `UI/D-garage-2018-url-bar-youtube-toast.png` | D |
| 17:29:27 | `UI/D-garage-2018-scrub-bar-visible.png` | D |
| 17:29:57 | `UI/A-editor-panel-primary-source-hq.png` | A |
| 17:30:14 | `UI/A-editor-panel-kill-the-player.png` | A |
| 17:30:25 | `UI/A-maze-crop-4x4-hollow-centre.png` | A |
| 17:30:31 | `UI/A-maze-crop-cell-highlight-on-spawn.png` | A |
| 17:30:46 | `UI/A-toolbar-three-tool-icons-visible.png` | A |
| 17:30:50 | `UI/A-maze-crop-wall-highlight-vertical.png` | A |
| 17:31:12 | `UI/A-editor-panel-highlight-outside-maze.png` | A |
| 17:31:26 | `UI/B-hover-ghost-in-margin-ring.png` | B |
| 17:34:57 | `UI/B-maze-growth-step1.png` | B |
| 17:35:22 | `UI/B-maze-growth-step2-width-term-binds.png` | B |
| 17:35:51 | `UI/B-maze-growth-mechanism.png` | B |
| 17:36:30 | `UI/B-editor-howto-step3-epic-twister.png` | B |
| 17:36:57 | `UI/B-editor-howto-step4-lag-note.png` | B |
| 17:37:27 | `UI/B-editor-howto-step5-nearly-solid.png` | B |
| 17:38:00 | `UI/B-editor-howto-step7-drag-paint-wall-run.png` | B |
| 17:38:37 | `UI/A-editor-howto-step6-or-just-click.png` | A |
| 17:39:04 | `UI/B-tank-spawn-placement-effect.png` | B |
| 17:39:32 | `UI/B-crate-spawn-placement-effect.png` | B |
| 17:39:57 | `UI/A-editor-preview-mode-lone-tick.png` | A |
| 17:40:06 | `UI/C-empty-slot-maze3-cam12win.png` | C |
| 17:46:27 | `Game/ranks.txt` | H |

---

*Generated 2026-08-04 from `manualevidence/`. Eleven analyst passes,
one per topic. No file under `../../../` was modified.*
