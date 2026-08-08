<!-- Published copy. Do not edit prose below the rule: correct it by superseding
     in DECISIONS.md, then add a row to the "Superseded" table here. -->

# Published copy — read this box first

This is `REBUILD-GUIDE.md`, the document every other file in this repo cites as
"guide §N". Until 2026-08-08 it lived only in the read-only archive
(`archive/REBUILD-GUIDE.md`), which is not committed and is not always mounted —
so the repo's own constitution was unreadable from a clone. This copy is the
citable one.

* Source: `archive/REBUILD-GUIDE.md`
* sha256 of the archive original: `fba7b5bc308c7067b5d1680f924fb13dd2731501a094475ea78ea609aac4ce4a`
* Everything below the horizontal rule is verbatim. The archive original is
  never edited.

## Superseded sections — check here before following any §

The guide is the constitution, not scripture. Where later evidence overturned
it, the correction is authoritative and this table is the index.

| § | Guide says | Superseded by |
|---|---|---|
| §2 | tree shape incl. `RELEASE-*/`, `game/embed.php`, `theLabReport/vol{1..14}/` | `DECISIONS.md` 2026-08-02 "srv/ tree corrections" and 2026-08-03 "tree corrections from DEDUCE.md §2.2" |
| §2.2 | `signUpTankDesign04StandardColours.swf` never captured | held (2012-06-01 200 capture) — `DECISIONS.md` 2026-08-02 |
| §3.4 | one commit per file | batched by tier for the 21 skeleton stubs — `DECISIONS.md` 2026-08-02 |
| §4 | `LEDGER` row count == `srv/` file count | refined to set equality over non-`known-lost`/`pending` rows — `DECISIONS.md` 2026-08-02 |
| §6.2 | `loadMaze` response is `r=<b64>&s=<slot>` | body is `r=` + base64(shuffle(`t=..&n=..&d=..&s=..`)), `s` **inside** the base64 — `docs/plans/2026-08-03-milestone-3.md` |
| §6.5 | per-axis capture scale 1.209 / 1.390 | artifact of including page chrome; scale is uniform — `docs/mazecreator-visual-spec.md` |
| §7.2 | gate B = byte-identical 843/843 | unachievable (server shuffled per request); redefined as decoded pair-multisets + byte-exact notFound + outer format + 672-state coverage — `docs/plans/2026-08-03-milestone-3.md` |
| §7.5 | "Gate E — visual regression" | **name collision.** This repo's gate E is subresource resolution (`tests/test_subresources.py`, `docs/ASSET-DISCIPLINE.md`). Visual regression is gate C. |

---
# TankTrouble classic — rebuild guide

Prototype-to-real build plan. Companion files: `RECONSTRUCTION-STATUS.md`
(provenance ledger), `RECONSTRUCTION-PLAN.md` (what exists vs what must be
written), `HUNT-LOG.md` (evidence, §1–57).

**Decisions taken:**

| | Choice |
|---|---|
| Server | **Period-correct PHP 5.6 + MySQL 5.5**, in Docker |
| Flash | **Both** — Ruffle for the browsable build, Flash projector as **oracle** |
| First milestone | **Full folder skeleton, labelled stubs everywhere** |

---

## 0. The one rule everything else serves

> **A reconstruction that cannot be told apart from the original is a forgery, not
> a preservation.**

Every file carries its provenance tier (`O`, `O?`, `M1`, `M2`, `M3` — defined in
`RECONSTRUCTION-STATUS.md`). Original bytes are never edited in place. Made files
announce themselves in their first line. If in doubt, a file is **more** made than
you think, not less.

This is not ceremony. Five separate times this project has nearly filed invented or
wrong data as recovered — a CDN serving 2026 bytes under a 2018 path, a 151 KB HTML
error page saved as a `.png`, a wrong-host fetch reported as a MISS. The labelling
discipline is the thing that caught them.

---

## 1. Repository layout

Keep the archive and the rebuild **physically separate**. The archive is read-only
input; the rebuild is output. Never let a build script write into the archive.

```
TankTrouble/
├── LEDGER.tsv                 ← the spine (§3)
├── DECISIONS.md               ← append-only log of every judgement call (§3.3)
├── docker/
│   ├── docker-compose.yml     php5.6-apache + mysql:5.5
│   ├── php/Dockerfile         + mysql ext, mod_rewrite, short_open_tag
│   └── mysql/init/*.sql       schema, seeded from the archive
├── srv/                       ← THE RECONSTRUCTED DOCUMENT ROOT (§2)
├── seed/                      ← importers: archive → MySQL (§5)
├── oracle/                    ← Flash projector + capture harness (§7.3)
├── tests/                     ← verification gates (§7)
└── archive -> ../_NOT-PART-OF-MAIN-ARCHIVE_swf-recovered-2026-08-02   (read-only)
```

---

## 2. The deduced document root

Tags: **[O]** original bytes exist · **[M1/M2/M3]** must be written, tier per
`RECONSTRUCTION-STATUS.md` · **(obs)** path observed in CDX · **(inf)** inferred.

```
srv/
├── index.php                       [M2] (obs) SAJAX dispatcher + all 6 routes
├── includes/                            (obs) — 75 paths enumerated, 61 held
│   ├── loadMaze.php                [M1] (obs) 17,411 CDX rows
│   ├── updateGameStatistics.php    [M2] (obs) 2,305 CDX rows
│   ├── achievement.php             [M2] (inf) 6 client call sites
│   ├── getUserAuthentication.php   [M3] (inf) 5 call sites — see §6.4
│   ├── getScrapyard.php            [M2] (obs) ?scraps &velocity
│   ├── db.php                      [M3] (inf) no evidence it existed by this name
│   ├── TankTrouble_v4.0.swf        [O]  366,827 b sha256 188062aff7f7d969…
│   ├── TankTrouble_v4.03.swf       [O]
│   ├── TankTrouble_v3.6c/3.6e.swf  [O]
│   ├── mazeCreator_v0.3.swf        [M2] ← THE LOST FILE (§6.5)
│   ├── mazeCreator_v0.2.swf        [M2] (obs 2010-09-08 only)
│   ├── signUpTankDesign{04,13,16,17,18}StandardColours.swf   [O]
│   ├── scrapyard{06,10,11}.swf     [O]   · scrapyard{05,07,08}.swf [M3] (obs)
│   ├── loggedInTank06.swf          [O]   · loggedInTank{02,04}.swf [M3] (obs)
│   ├── laika02.swf                 [O]
│   ├── ima3_preloader_1.5.swf      [O]
│   ├── styles.css main.css forumStyles.css boxStyles.css        [O]
│   │   newsStyles.css news.css shopStyles.css
│   ├── swfobject.js mootools-release-1.11.js embed.js           [O]
│   ├── phaser.min.js scrapyard.js                               [O] 2017+
│   ├── p2.js  src/p2.js            [M3] (obs, never 200)
│   ├── c64.{eot,ttf,woff}          [O]  the site's pixel font
│   ├── images/scrapyardPlates.png  [M3] (obs, never 200)
│   └── TTTradingCards{SeriesI,II,III,SpecialAnniversaryCard}.pdf [O]
├── images/                         [O]  122 classic UI images, complete
├── assets/images/{tankInfo,lobby}/ [O]  later asset tree
├── infirmary/index.html            [O]  password recovery
├── game/embed.php                  [M2] (obs)
├── faq/            ios/            [M2] (obs) images held, HTML not
├── shop/           privacy/        [M2] (obs)
├── like/           statistics/     [M2] (obs)
├── spreadTheWord/                  [M2] (obs) affiliate kit, source of ?r=
├── tellAFriendMail/                [M2] (obs)
├── theLabReport/vol{1..14}/        [M2] (obs) vol 14 missing
├── getimage.php    uploadimage.php [M2] (obs) ?id ?at2x
├── content.php     embed.php       [M2] (obs)
├── sendRequest.php changePassword.php  [M2] (inf) infirmary comments
└── RELEASE-YYYY-MM-DD-NN/          [O]  HTML5 client trees (separate vhost)
```

### 2.1 What the tree does NOT claim

* **File lists above `/includes/` are directory-level only.** The set of directories
  is solid (every one observed in CDX). The files inside them are not — mod_autoindex
  was off, so nothing ever enumerated them. `faq/index.php` is a guess about the
  *name*, not about the directory.
* **`db.php` is pure invention.** Some shared DB include almost certainly existed;
  nothing tells us its name. Mark it `M3` and do not let its plausibility harden.
* **`/includes/` never contained a `maze*` file in any capture**, yet §39 proves
  `includes/mazeCreator_v0.3.swf` is the real path. The absence is a *crawler*
  artefact. Do not "correct" the tree back to a garage-scoped path.

### 2.2 Version history the tree understates

CDX proves these names existed but never captured bytes:
`TankTrouble_v1.11 1.3 1.31 1.4 2.01 2.1 2.2 3.02a 3.11 3.1a 3.41 3.42 3.43 3.5
3.6 3.6a 3.6b 3.6e 3.7`, `scrapyard.swf`, `scrapyard01 03 04 05`,
`signUpTankDesign01 04 09 11StandardColours`.

Do not create empty stubs for these. Record them in `LEDGER.tsv` with status
`known-lost` so the count of what is missing stays honest.

---

## 3. The ledger — how to record every change

### 3.1 `LEDGER.tsv`, one row per path, append-only in spirit

```
path	tier	sha256	source	evidence	verified_by	notes
srv/includes/TankTrouble_v4.0.swf	O	188062aff7f7d969…	archive/includes-tree/20130313_…	4 independent copies; 1 CDX digest 2013-03→2020-12	tests/test_assets.py	frozen 7.5y
srv/includes/loadMaze.php	M1	—	written 2026-08-02	17,411 CDX rows; 843 decoded responses; MazeDataFetcher.as	tests/test_loadmaze_replay.py	replays 843/843
srv/includes/db.php	M3	—	written 2026-08-02	none — name invented	—	DO NOT PROMOTE
srv/includes/scrapyard07.swf	known-lost	—	—	CDX 2 captures 2014-10-30/31, no 200	—	
```

Rules:

1. **Every file in `srv/` has a row.** A file with no row fails CI.
2. `O` rows must carry a sha256 that matches a file in the archive. CI re-checks.
3. `M*` rows must name their evidence, or the tier is wrong.
4. **Promotion requires a new evidence citation** in the same commit. Demotion is
   always allowed and needs no justification.
5. `known-lost` rows have no file. They exist so the denominator stays truthful.

### 3.2 Provenance header in every made file

First lines of every `M*` file, machine-parseable:

```php
<?php
/* @provenance M1
 * @evidence   17,411 CDX rows; 843 decoded responses in archive/maze-corpus/raw/;
 *             reader source archive/decompiled/…/MazeDataFetcher.as
 * @verified   tests/test_loadmaze_replay.py — 843/843 byte-exact
 * @written    2026-08-02
 * @caveat     Response is byte-exact. The QUERY side is reconstructed from the
 *             client, so unknown parameters are rejected rather than ignored —
 *             the original's behaviour on unknown params is not known.
 */
```

For a `.swf` or binary you cannot annotate internally, put the block in a sidecar
`<name>.provenance` and make CI require it.

### 3.3 `DECISIONS.md` — append-only

Every judgement call gets an entry. This is the file that stops a future reader (or
you in six months) mistaking a coin-flip for a finding.

```markdown
## 2026-08-02 — mazeCreator save endpoint named `saveMaze.php`
Tier: M3. No evidence for the NAME. Chosen because it mirrors `loadMaze.php`.
Rejected: `submitMaze.php`, `storeMaze.php` — equally unevidenced.
Reversible: yes, single constant in includes/config.php.
Supersedes: nothing. Superseded by: nothing yet.
```

### 3.4 Git discipline

* One commit per file or per tightly-coupled pair. Commit message states the tier:
  `feat(M2): includes/achievement.php — from 6 client call sites`
* **Never** commit archive bytes and written code in the same commit.
* Tag milestones: `skeleton-complete`, `loadmaze-replay-green`, …

---

## 4. Milestone 1 — the skeleton (what you asked to build first)

Goal: **every directory and filename exists, nothing works, everything is labelled.**

1. Create the tree in §2, directories only.
2. Copy `[O]` files from the archive. **Copy, never move.** Verify sha256 on arrival
   and write the row into `LEDGER.tsv`.
3. For every `[M*]` path, write a stub that is *loud*:

```php
<?php
/* @provenance M2
 * @evidence   6 client call sites in decompiled AS2; no response body ever captured
 * @verified   none
 * @written    2026-08-02
 */
header('HTTP/1.1 501 Not Implemented');
die("STUB achievement.php [M2] — behaviour not yet reconstructed\n");
```

A stub that returns `501` and dies is correct. A stub that returns plausible fake
data is the single most dangerous thing you can write in this project.

4. Run the CI checks from §8. Skeleton milestone is done when they pass with every
   file at tier `M*`-stub and every `[O]` sha256 matching.

**Exit criterion:** `LEDGER.tsv` row count == file count in `srv/`, and
`tests/test_no_unlabelled.py` is green.

---

## 5. Milestone 2 — data before code

Seed MySQL from the archive before writing a single query. Real data makes the
schema's mistakes visible immediately.

| Table | Source | Tier |
|---|---|---|
| `mazes` | `archive/maze-corpus/raw/` — 843 payloads, growing | data **O**, schema **M1** |
| `forum_threads`, `forum_replies` | `archive/forum-archive/` — 468 threads, 225,438 replies | data **O**, schema **M1** |
| `news` | 49 `?news` captures | data **O**, schema **M1** |
| `users` | **synthetic** — see below | **M3** |
| `accessories` | paint editor `initCode`: `tal baral fal bacal` as `id-tier,` | **M2** |
| `achievements` | `achievementId`/`achievementIds`/`achievementProgress` | **M2** |

### 5.1 Users are synthetic, and must be obviously so

Real usernames appear throughout the maze corpus and forum archive as authorship
metadata — that is public authorship and fine to preserve. **Real credentials also
exist**, in the public Wayback CDX index, because the original site ran SAJAX over
GET. They are deliberately not in this archive and must never be reintroduced.

Seed users with obviously-fake names (`testuser01`…) and random passwords. Where a
maze's `n=` field names a real author, keep it as **display metadata**, not as a
foreign key to a login. Do not create accounts for real people.

### 5.2 Schema is M1 in shape, M3 in types

Every column in `mazes` was observed in real payloads — that is why it is M1.
Column **types, widths, indexes, charset and collation were never observable
through HTTP**. Pick sane period-correct values (`latin1`/`utf8`, MyISAM vs InnoDB)
and record the choice in `DECISIONS.md` as M3. Do not present the DDL as recovered.

---

## 6. Milestone 3 — writing PHP

### 6.1 Order, easiest evidence first

1. `includes/loadMaze.php` — **M1, fully specified, verifiable.** Do this first; it
   is the only endpoint you can prove correct, so it calibrates everything else.
2. `index.php` route dispatch (6 routes) — M1.
3. `index.php` SAJAX dispatcher shell + the 36 function names — M2.
4. Read-only SAJAX functions: `showForumThread`, `showForumPreviews`, `updateTop10`,
   `getAllUserInfo` — M2, and the forum data to check them against is 100% complete.
5. `updateGameStatistics.php`, `achievement.php`, `getScrapyard.php` — M2.
6. Write-side and auth — M3, last, deliberately.

### 6.1a De-rendering — inverting captured HTML back into PHP source

**This is the core method of the whole rebuild, and the archived HTML is the single
richest evidence we have.** Every captured page is the *output* of a PHP file.
Reconstruction means inverting the rendering, not hand-writing a lookalike.

Do **not** treat archived HTML as static pages to be served, and do not hand-write
PHP that emits something similar. Both throw away evidence.

#### Step 1 — clean the capture back to what the server actually sent

| Artefact | Fix |
|---|---|
| Wayback toolbar / injected JS + CSS | use the `id_` raw form, or strip the injected block |
| Rewritten URLs `/web/<ts>/http://…` | restore the original relative URL |
| Common Crawl bodies | already raw — **prefer these** |
| gzip body saved under `.html` | check magic `1f 8b`, decompress |

Keep the cleaned capture as **`O`** in `archive-cleaned/`. It is the ground truth
every later gate diffs against.

#### Step 2 — un-do PageSpeed to recover the original markup

Captures were served through Google PageSpeed, so asset URLs are mangled:

```
a.js+b.js+tt,_log.js.pagespeed.jc.56Z5iHEEbt.js
```

The original PHP emitted **separate** `<script>` tags for `a.js`, `b.js`,
`tt/log.js` — PageSpeed combined them at serve time. `,_` encodes `/`.

So **split every bundle back into its constituent tags.** The bundle filename is a
verbatim listing of its inputs, which is how the 568-module client tree was
recovered in the first place (`HUNT-LOG.md` §45). Same trick, applied to markup:
the mangled name tells you exactly what the source line looked like.

Also reverse: inlined small CSS/JS (`.pagespeed.ic.`), image spriting, and
whitespace collapsing. Anything PageSpeed did is **not** in the original source.

#### Step 3 — diff captures against each other to separate static from dynamic

This is where the deduction actually happens, and it is mechanical rather than
guesswork.

* **Same page, many dates** — 46 `?garage`, 49 `?news`, 46 `?game`, 45 `?lab`,
  43 `?forum`, 36 `?shop` captures. Byte-identical regions across years are
  **literal text in the PHP**. Regions that vary are **`echo`ed variables**.
* **Same page, same day, different captures** — anything still differing is
  per-request: session, counters, ads, timestamps, random.
* **Repeated blocks with identical indentation** are a `foreach`/`while`. The
  number of repetitions varies across captures; the template does not. Extract the
  block, not the instances.
* **Diff across years to date template changes** — this already produced the dated
  SAJAX inventory (§54) and the JS API timeline (§56). Same technique, applied to
  markup, dates every template edit.

Write the classification down per region before writing any PHP. A region you
cannot classify is a region you do not yet understand.

#### Step 4 — exploit machine-generated regions, which invert exactly

Some output was generated by a library, not typed by hand. That is a gift: the
generator is deterministic, so you can recover its **input** precisely.

* **SAJAX stubs.** The `x_<name>(…)` JS functions and `sajax_do_call` were emitted
  by the SAJAX library from a list of `sajax_export()` calls. The stub format
  identifies the library version, and the 36 function names *are* the export list.
  Do not hand-write the stubs — reimplement the generator and feed it the 36 names.
  Then diff your generated output against the captures: it should match byte-for-byte.
  **That is a gate**, and it promotes the dispatcher from M2 toward M1.
* **SWFObject embeds** follow a fixed emission pattern; the varying parts are the
  arguments, which §55 already enumerates with dates.

#### Step 5 — mine what the original author left behind

* **HTML comments** survive PageSpeed and are literal author text. The `infirmary`
  comments are how `sendRequest.php` and `changePassword.php` are known at all.
* **Whitespace and indentation** reveal PHP block boundaries — a sudden indentation
  reset usually marks where PHP resumed emitting.
* **Element `id` and `class` naming** reveals the server-side variable names, since
  ids like `userpanel-<user>` are string-concatenated in PHP.

#### Step 6 — write the PHP, then gate it

Target: your PHP, given the same inputs, reproduces the cleaned capture
**byte-for-byte** except for regions explicitly classified as dynamic in step 3.

```
tests/test_render_diff.py
  for each cleaned capture:
    render the route with the capture's known inputs
    mask regions classified dynamic
    assert remaining bytes identical
```

A page passing that gate is **M1**, not M2 — it is verifiable against archived
output, exactly like `loadMaze.php`. **This is the main lever for moving the rebuild
from "plausible" to "provable", and it applies to every one of the six routes.**

> **Do not "improve" anything while de-rendering.** Non-semantic quirks — trailing
> whitespace, inconsistent quoting, a stray `<br>`, tables used for layout — are
> evidence of how the original was written. Normalising them destroys the diff gate
> and silently converts O-derived structure into invention.

### 6.2 The template for a reconstructed endpoint

```php
<?php
/* @provenance M1  … (block from §3.2) */

require_once __DIR__ . '/db.php';   // M3 — name invented

// WIRE FORMAT — observed, do not "improve"
//   GET includes/loadMaze.php?q=<base64( shuffleMessage("userName=<n>&a=<r>&b=<r>") )>
//   200 →  r=<base64>&s=<slot>
//   b64 →  t=<title>&n=<author>&d=<grid>
//   grid = <w>#<cells>#<reserved>#<objCount>#(<x>#<y>#<type>#<params>)…#0#
//   cells: octal per cell, row-major, h = len/w
//          bit0=floor  bit1=wall shared with cell above  bit2=west wall
//   object type 5 = tank spawn, 8 = crate spawn; coords 1-indexed
//   `reserved` is read and discarded by the client — always emit "0"
//   trailing "0" is a terminator the client skips unconditionally
```

Rules for the body:

* **Reproduce quirks, do not fix them.** The `reserved` field is dead. Emit it
  anyway. The client's parser advances a fixed number of `#` fields; "cleaning up"
  the format silently breaks it.
* **`shuffleMessage()` is a random permutation of `&`-pairs, not encryption.** Order
  is not significant. Parse accordingly; do not assume positions.
* Where the original's behaviour on bad input is unknown, **fail loudly** and note
  it in `@caveat`. Guessing an error format invents evidence.

### 6.3 Period-correct without being period-vulnerable

You chose PHP 5.6 for fidelity. That is the right call for structure, and it means
the container must never be exposed.

* `docker-compose.yml` binds **127.0.0.1 only**. No published ports on `0.0.0.0`.
* Put a `SECURITY.md` at the repo root: *this stack is intentionally obsolete and
  must not be internet-facing.*
* `mysql_*` functions are fine for fidelity **inside** the container. Still escape
  everything — an SQL injection in a preservation project corrupts your own seeded
  archive, which is the data you are trying to protect.

### 6.4 Authentication is deliberately NOT reconstructed

The original ran SAJAX auth over **GET**. That is *why* real credentials are
permanently in the public CDX index. Reproducing it would be reproducing the
vulnerability that caused the leak.

`getUserAuthentication.php` and the login path are **M3 by choice**. Use POST over
TLS, hash properly. Put this in the file header, not just in a doc:

```php
/* @provenance M3
 * @caveat     DELIBERATE DIVERGENCE. The original used SAJAX over GET, which is
 *             why real credentials are still in the public Wayback CDX index.
 *             This file does NOT reconstruct that. POST + TLS + password_hash.
 */
```

### 6.5 mazeCreator — the one big rewrite

Everything except the pixels is specified. Build it as an **AS2 SWF** targeting
Flash 8, so it drops into the original embed unchanged:

* Stage **688×400**, `wmode=transparent`, `menu=false`,
  `allowScriptAccess=sameDomain`, bg `#ffffff`
* FlashVar **`initCode`** = Base64 of `k=v&k=v`, decoded by the same
  `decodeMessage()` the game and paint editor share
* Inbound `SetVariable`: `fadeOut`, `newToolRequested`, `_root.saveRequested`,
  `_root.mazeName`, `_root.errorPanel.hide`, `previewLoaded`
* The page-side JS already exists — all 9 functions, unchanged 2010→2020:
  `openMazeCreator closeMazeCreator attemptToSaveMaze cancelSaveMaze
  selectMazeCreatorTool updateMazeTitle showMazeCreatorToolsAndTitle
  hideMazeCreatorToolsAndTitle mazeTitleLegalCharacters`

Editor constraints to enforce (verified against 843 mazes, 0 violations):
grid ≤ 18×10 · title ≤ 32 chars over `A–Za–z0–9`, space, `! , - . ?` ·
author ≤ 16 · ≤ 5 tank spawns and ≤ 5 crate spawns, ≤ 10 objects ·
non-rectangular arenas legal.

Artwork, source 1 — the screenshot: crop from
`archive/ia-items/extracted/images/Making a maze.png` (832×556, v0.3, 2016-01-30).
It shows all three tools, the layout, and both spawn types. **It gives you 3 of 6
icon states** — wall=deselect, crate=**select**, tank=deselect. The opposite states
are M3. Note that in the ledger. The capture is not a uniform scale of the stage
(1.209× horizontal, 1.390× vertical), so it includes panel chrome — measure with a
per-axis factor.

Artwork, source 2 — **video** (`HUNT-LOG.md` §61): TankTrouble has substantial
YouTube coverage from its active years, and gameplay/tutorial footage shows UI that
no crawler could ever fetch, because it only existed behind a logged-in click.
Video beats the screenshot on one axis that matters: it shows **transitions**, so a
tool being clicked gives you the same icon in *both* states — exactly the 3 states
the screenshot cannot supply. Also the only likely record of the error panel
(known only from `_root.errorPanel.hide`) and the save dialogue.

This is manual work — frame-stepping, cropping, upscaling from compressed footage.
Budget it as such. **Provenance: M2 at best, never O.** Video is lossy and
rescaled, so a crop is a reference for redrawing, not recovered bytes. Record
video URL, uploader, upload date and timestamp in `LEDGER.tsv` for every asset
derived this way.

**The save endpoint is M3, and that is now final for this phase.** No maze SAJAX
function exists among the 36, so the page did not save it; the SWF owned an error
panel, so the SWF saw the response. It posted directly to a URL whose name lives
only in the lost file. The last hope was the HTML5 client — but across **all 11**
2017–2019 releases the `infoMazeCreator` button is registered with `standard`,
`active` and `disabled` images and **no click handler**, and `saveMaze` / `saveArena`
appear zero times. The HTML5 maze editor was stubbed, never built, so it inherited
nothing. Put the name in one constant so a future discovery is a one-line change.

---

## 7. Verification gates

Gates are the point. Without them "M1" is just a comment.

### 7.1 Gate A — asset integrity (blocks every commit)

Every `O` row's sha256 recomputed against `srv/`. Any drift fails. This catches the
build accidentally rewriting original bytes.

### 7.2 Gate B — replay (the strongest gate you have)

`tests/test_loadmaze_replay.py`: seed the DB from the 843 archived payloads, then
for each one, request it back through your `loadMaze.php` and require the response
to be **byte-identical** to the archived response.

843 of 843 or the gate is red. This is why `loadMaze.php` is M1 and everything else
is not — no other endpoint has archived responses to replay against.

Extend the corpus as the fetcher recovers more (4,192 known). More payloads, more
gate.

### 7.3 Gate C — the Flash oracle

You chose both runtimes. Use the projector as ground truth:

1. Render maze *N* in the real Flash projector, screenshot.
2. Render the same maze in Ruffle in-browser, screenshot.
3. Diff. Log divergences in `oracle/DIVERGENCES.md`.

Expect AS2 gaps — **specifically the ones the garage depends on**: `SetVariable`,
and the `getURL("javascript: …")` bridge the paint editor uses to write into hidden
form fields. Those are exactly the APIs mazeCreator needs. Test them **before**
building the editor, not after; if Ruffle cannot do the bridge, that changes the
mazeCreator design and you want to know on day one.

### 7.4 Gate D — structural

* Every file in `srv/` has a `LEDGER.tsv` row
* Every `M*` file has a parseable `@provenance` header
* No `M*` file returns plausible data without a passing gate — CI greps for stubs
  that return `200`
* Grep the whole tree for credential-shaped strings before every push

### 7.4a Gate F — render byte-diff (the second-strongest gate, and it scales)

For each cleaned capture: render the route with that capture's known inputs, mask
the regions classified dynamic in §6.1a step 3, and assert the remaining bytes are
**identical**.

Unlike gate B, which only `loadMaze.php` can satisfy, **gate F applies to all six
routes** — 265 captured bodies to diff against. Any page that passes is **M1**.
This is the single biggest lever for converting the rebuild from plausible to
provable, so build the harness before writing page PHP, not after.

Corollary: the mask file *is* the specification of what is dynamic. Review it. A
mask that keeps growing is a sign the reconstruction is drifting, not that the
original was more dynamic than thought.

### 7.5 Gate E — visual regression

Archived logged-out HTML for all six routes exists. Render each in the rebuild,
screenshot, diff against the capture. Not pixel-perfect (fonts, ads, timestamps) —
gate on layout boxes, not pixels.

---

## 8. Traps this project already hit — do not re-learn these

| Trap | What it looked like | Guard |
|---|---|---|
| **Size ≠ integrity** | 151 KB HTML error page saved as `.png`, reported recovered. **Hit 3×** | Validate magic bytes: `CWS/FWS/ZWS`, `\x89PNG`, `\xff\xd8\xff` |
| **CDN catch-all** | 5 RELEASE tags with no CDX rows returned 200 — all the *current* 2026 build, incl. a nonexistent version | Always probe a bogus version as control; hash 200s against the current build |
| **`matchType=prefix` + `*`** | Returns 0 rows, indistinguishable from a real negative. Cost a "never crawled" verdict that was false | Exact URL, no wildcard; or `matchType=domain` + `filter=original:` |
| **`id_` returns raw gzip** | 12 CSS/JS files saved gzip-encoded under `.css`/`.js` | Check magic `1f 8b`, decompress |
| **Wrong host hard-coded** | `images/mazeCreator.png` reported MISS — it lives on `classic.` | Try every known host before recording a negative |
| **Digest ≠ payload identity** | Same payload, two CDX digests (gzip); same digest, lengths 367,324–367,733 | **sha256 of the decoded payload** is the only identity |
| **Substring name match** | `TankTrouble_v4.0` matched `v4.03`, produced a false "two builds" finding | Match on exact filename |
| **Windows path length** | PageSpeed bundle names > 255 chars, `Errno 22` | Truncate + sha1 suffix, record the mapping |
| **Self-throttling** | ~16 parallel IA streams → connections refused (exit 000, *not* 429) | ≤2 concurrent, adaptive backoff |

---

## 9. Order of work

```
1  Skeleton + LEDGER + CI gates A/D          ← milestone 1, nothing works
2  Ruffle vs projector spike on SetVariable  ← do EARLY, it can change the design
3  Clean captures + un-do PageSpeed (§6.1a steps 1–2)  → archive-cleaned/ as O
4  Seed DB from archive (mazes, forum, news)
5  loadMaze.php → gate B green, 843/843      ← the calibration point
6  De-render the 6 routes (§6.1a steps 3–6)  → gate F byte-diff, M1 not M2
7  SAJAX generator reimplemented, not hand-written → diff vs captures = gate
8  Remaining M2 endpoints
9  mazeCreator SWF rebuild                    → gate C
10 Auth, deliberately last and deliberately different
```

Step 2 before step 8 is the important ordering. Everything else can slip.

---

## 10. Open questions to settle before milestone 3

1. **Save endpoint name** — M3 until the cdn-beta HTML5 editor is searched. Keep it
   in one constant.
2. **Charset/collation** — `latin1` vs `utf8`. The maze title charset is 68 ASCII
   characters, but forum posts are not. Check the forum archive for non-ASCII
   before choosing.
3. **`index.php` vs per-route files** — CDX shows `?game` etc. as query strings on
   `/`, so a single dispatcher is the evidenced reading. Confirm no
   `garage.php`-style path exists in CDX before committing.
4. **`db.php`** — pure invention. Consider naming it something obviously modern so
   nobody mistakes it for recovered.
