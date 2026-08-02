# How everything here was deduced

The original server is gone. Nothing in `srv/` may rest on "it probably worked like
this." This file records **what was observed, what was inferred from it, and how
strong each inference is** — for the filesystem, the wire formats, the PHP, the
timeline, and the artwork.

Companion files: `LEDGER.tsv` (per-file provenance), `DECISIONS.md` (judgement
calls), `archive/HUNT-LOG.md` (the raw investigation, §1–63),
`archive/FILESYSTEM-EVIDENCE.tsv` (1,341 paths, machine-readable).

---

# Part 0 — Principles

## 0.1 Evidence grades

Applied to any claim, not just paths.

| Grade | Meaning |
|---|---|
| **A** | Directly observed. A 200 response, a decompiled function, an archived payload |
| **B** | Observed indirectly but unambiguously. A 403 proves a path existed and was protected |
| **C** | The **name** or **shape** is proven, the content is not. A 404; a call site with no response body |
| **D** | Wrong era or wrong site — says nothing about the target |
| **X** | Artefact. Looks like evidence, is not |

Grades map onto the `LEDGER.tsv` provenance tiers: A→`O`/`M1`, B/C→`M2`, nothing→`M3`.

## 0.2 The seven techniques that produced almost everything here

| # | Technique | Worked example |
|---|---|---|
| 1 | **Find the counterpart of the lost thing** | `mazeCreator_v0.3.swf` is gone, but `MazeDataFetcher.as` — its *reader* — survives in four decompiled game builds and fully specifies what the writer emitted |
| 2 | **Corpus statistics reveal enforced limits** | Across 843 user-authored mazes nothing exceeds 18×10, no title exceeds 32 chars, never more than 5 of either object type. What thousands of users never did is what the tool forbade |
| 3 | **Machine-generated output inverts exactly** | SAJAX stubs were emitted by a library from a function list; PageSpeed bundle names enumerate their own inputs. Both can be run backwards to recover the input |
| 4 | **Diff across time separates constant from variable** | Bytes identical across 46 `?garage` captures spanning a decade are literal text in the PHP; bytes that vary are `echo`ed |
| 5 | **First/last appearance dates a feature** | `getScraps()` appears in stubs from 2017-02-21 — the exact date `scrapyard.js` went live. Two independent sources, same day |
| 6 | **Error messages leak schema** | The modern JSON-RPC layer's validation errors reported expected parameter counts and types, mapping 144 methods without documentation |
| 7 | **Siblings predict the lost thing** | `signUpTankDesign18StandardColours.swf` (held) shares author, era, embed convention and control protocol with mazeCreator (lost). Its internals bound the design space |

## 0.3 Rules that stop deduction becoming invention

**Absence of evidence needs a mechanism before it becomes evidence of absence.**
`mazeCreator_v0.3.swf` appears nowhere in CDX — not even a 404 — yet it is
provably the real path. Explanation: it was instantiated inside a deferred
`setTimeout` string on a logged-in click, so nothing ever linked to it and no
crawler ever requested it. **Until you can say *why* something is absent, absence
means nothing.**

**A refusal is not a negative.** Three separate services in this project return
something that looks exactly like "no results":

| Service | Refusal | Looks like |
|---|---|---|
| Wayback CDX | `matchType=prefix` + a trailing `*` | 0 rows |
| Wayback CDX | large-domain scan | HTTP 200, empty body |
| Common Crawl | CloudFront WAF rate-limit | `403 Request blocked` |

The Common Crawl case recorded **1,148 of 1,260 jobs as zero-row results that were
never actually asked.** Always record "asked and got nothing" separately from
"never successfully asked."

**Corroboration must be independent.** Two sources that both derive from the same
capture are one source. The mobile-port developer's blog describes TankTrouble's AI
in detail — but he writes *"I haven't looked at the code for [the online version]"*,
so he is **not** a second source on the Flash implementation.

**sha256 of the decoded payload is the only identity.** CDX `digest` over-splits
(same payload, different gzip → different digest); CDX `length` is stored record
size, not payload size (one digest spanning 367,324–367,733). A magic-byte pass
counted 43 builds where sha256 counted 42.

**Size is never integrity.** Wayback returns a ~151 KB HTML error page on failure,
which passes any "bigger than N" check. Validate magic bytes. This bug landed three
separate times.

---

# Part 1 — What each source can and cannot tell you

| Source | Strong evidence for | Blind to |
|---|---|---|
| **Wayback CDX index** | which paths existed, when, with what status | anything never linked |
| **Wayback content** | logged-out HTML, CSS, JS, binaries | anything behind login |
| **Common Crawl** | same, plus raw bodies with no rewriting; hosts not named tanktrouble | same login gap |
| **Decompiled SWFs** | client logic, wire formats, constants, endpoint names | server internals |
| **Archived API responses** | exact response bytes (843 `loadMaze` payloads) | request handling of bad input |
| **PageSpeed bundle names** | the client's source-module tree | module contents |
| **SAJAX stubs in HTML** | the server's exported RPC surface + dates | function bodies |
| **Wikis** | screenshots of logged-in UI, community knowledge | accuracy — user-written, often wrong |
| **Video** | logged-in UI *in motion*, i.e. state transitions | exact pixels — lossy and rescaled |
| **Clone/portal sites** | which builds circulated when | anything server-side |
| **Distribution zips** | client bundles as shipped | server code (all four were client-only) |

**Nothing above can ever yield server-side PHP source.** A web server emits output,
never source. That is a property of HTTP, not a gap in coverage — confirmed by four
independent negatives (CDX extension sweep, regex scan of 4,434 recovered text files
for `<?php`/`Fatal error:`/`DOCUMENT_ROOT`/`mysql_*`, authenticated GitHub code
search, and extraction of all four distribution zips).

---

# Part 2 — The filesystem

Regenerated from raw CDX (74,165 rows) plus Common Crawl, **not** from notes.
Scope: `tanktrouble.com`, `www.tanktrouble.com`, `classic.tanktrouble.com`.

## 2.1 Two filters that must be applied, or the evidence lies

### Era partition — one hostname, two different sites

| Era | Window | Nature |
|---|---|---|
| **CLASSIC** | … 2020-12-04 | PHP + Flash, six **`?query`** routes |
| **MODERN** | 2020-12-22 … | SPA, client-side **path** routes |

⚠ **The modern SPA answers `200` for any path** — it serves the app shell and routes
in the browser. A modern-era 200 is worth **nothing** as filesystem evidence.

So `/garage`, `/forum`, `/shop`, `/news`, `/privacy`, `/game`, `/css`, `/ajax`,
`/assets` are **modern-only**. Classic reached those features through `?garage`,
`?forum`, `?shop`, `?news` — which is itself the proof that classic used query
routes and the rewrite happened at migration.

### Crawler-artefact paths — JS strings misread as URLs

Bare paths appearing 2019-10-04 … 2021-04-01, **never 200**, 2–4 observations each:

* mootools easings — `/Quad.easeInOut`, `/Bounce.easeIn`, `/Elastic.easeOut` … (33)
* ActiveX progids — `/Microsoft.XMLDOM`, `/Msxml2.XMLHTTP`, `/ShockwaveFlash.ShockwaveFlash`
* p2.js modules and classes — `/shapes`, `/collision`, `/constraints`, `/equations`,
  `/objects`, `/world`, `/material`, `/math`, `/solver`, `/utils`, `/events`,
  `/Island`, `/IslandManager`, `/Convex`, `/Polygon`, `/TupleDictionary`, `/Spring` …
* misc — `/avc1.42E01E` (a codec string), `/package.json`, `/src`

**Grade X.** Creating these would invent structure wholesale.

## 2.2 Classic directories — grade A

| Path | 200s | non-200 | span | note |
|---|---:|---:|---|---|
| `/` | 1,457 | 204 | 2008-01-16 … 2020-12-03 | the dispatcher; all six routes are `?query` on this |
| `/includes/` | 20,860 | 4,109 | 2010-11-28 … 2020-11-21 | 79 distinct paths — §2.4 |
| `/images/` | 5,652 | 6,722 | 2010-11-28 … 2020-10-26 | 408 distinct paths |
| `/robots.txt` | 1,056 | 2,497 | 2008-01-08 … 2020-07-05 | |
| `/infirmary/` | 116 | 26 | 2010-09-15 … 2020-02-09 | its HTML comments are the only evidence for `sendRequest.php` / `changePassword.php` |
| **`/tankRanks/`** | **86** | 11 | 2010-10-30 … 2015-05-23 | ⚠ missed by the first tree |
| `/favicon.ico` | 79 | 237 | 2010-11-28 … 2020-06-20 | |
| `/embed.php` | 75 | 66 | 2009-01-29 … 2020-10-26 | **top-level**, not `/game/embed.php` |
| `/faq/` | 72 | 0 | 2013-02-19 … 2020-06-20 | 14 paths incl. `images/` |
| `/spreadTheWord/` | 40 | 36 | 2008-10-04 … 2020-11-27 | source of the `?r=` tracker |
| **`/Assets/`** | **25** | 371 | 2012-06-15 … 2019-05-28 | ⚠ **capital A**, distinct from modern `/assets/` |
| `/index.php` | 21 | 0 | 2008-05-28 … 2009-09-07 | explicit only in the earliest era |
| `/tellAFriendMail/` | 21 | 19 | 2008-04-30 … 2018-02-22 | 13 paths incl. `images/` |
| `/statistics/` | 14 | 19 | 2010-12-21 … 2017-07-10 | |
| `/ios/` | 7 | 8 | 2012-01-09 … 2019-10-31 | |
| **`/verification/`** | **4** | 1 | 2013-09-24 … 2015-03-10 | ⚠ missed; pairs with SAJAX `sendVerificationEmail` (from 2013-12-06) |
| `/theLabReport/` | 3 | 0 | 2019-06-06 … 2020-09-26 | 3 paths observed, **not** 14 |
| **`/facebook/`** | **1** | 0 | 2010-02-01 | ⚠ missed |
| **`/kickstarterFAQ/`** | **1** | 0 | 2015-02-27 | ⚠ missed — there was a Kickstarter |

## 2.3 Grades B and C — names proven, content never captured

| Path | Grade | Evidence | Reading |
|---|---|---|---|
| `/includes/` as a directory | **B** | `403` ×1 | **listing was forbidden** — the one concrete `.htaccess` fact available (`Options -Indexes`) |
| `/logIn.php` | **C** | `404` ×36, 2008-05-28 … 2009-09-07 | requested persistently, never served |
| **`/mazeCreator`** | **C** | `404` ×1, **2009-01-31** | ⚠ a top-level probe 20 months before `mazeCreator_v0.2.swf` appears in the garage — the earliest trace of the name anywhere |
| `/explanation.html`, `/static/`, `/u/` | C | `404` ×1 each | |

## 2.4 `/includes/` — the best-evidenced directory on the site

**37 paths with a classic-era 200:**

```
TTTradingCardsSeriesI.pdf      TTTradingCardsSeriesII.pdf
TTTradingCardsSeriesIII.pdf    TTTradingCardsSpecialAnniversaryCard.pdf
TankTrouble_v3.5.zip  TankTrouble_v3.6.zip  TankTrouble_v3.6e.zip  TankTrouble_v3.8c.zip
TankTrouble_v3.6c.swf          TankTrouble_v4.0.swf
laika02.swf                    loggedInTank06.swf
scrapyard06.swf  scrapyard10.swf  scrapyard11.swf
signUpTankDesign{04,13,16,17,18}StandardColours.swf
ima3_preloader_1.5.swf
loadMaze.php   updateGameStatistics.php   getScrapyard.php
styles.css  boxStyles.css  forumStyles.css  newsStyles.css  shopStyles.css
swfobject.js  mootools-release-1.11.js  embed.js
phaser.min.js  scrapyard.js
c64.eot  c64.ttf  c64.woff
```

**34 names proven by 404 — the file existed once, the bytes are gone:**

```
TankTrouble_v1.11 v1.3 v1.31 v1.4 v2.01 v2.1 v2.2 v3.02a v3.11 v3.1a
              v3.41 v3.42 v3.43 v3.5 v3.6 v3.6a v3.6b v3.6e v3.7 .swf
scrapyard.swf  scrapyard01  scrapyard03  scrapyard04  scrapyard05 .swf
signUpTankDesign01  signUpTankDesign04  signUpTankDesign09StandardColours
signUpTankDesign11StandardColours .swf
Assets/Tank.swf        ← proves an Assets/ subdirectory inside /includes/
images/scrapyardPlates.png
p2.js        src/p2.js
```

`TankTrouble_v3.5.swf` 404 ×13 and `scrapyard05.swf` 404 ×17 — repeatedly requested
after removal, i.e. pages in the wild still referenced them.

⚠ **`mazeCreator_v0.2.swf` and `v0.3.swf` appear nowhere in `/includes/` CDX — not
even a 404** — yet the garage page's own JavaScript proves
`includes/mazeCreator_v0.3.swf` is the real path. The cleanest example in the whole
corpus of §0.3's first rule.

## 2.5 Grade D — modern-only, do NOT create under the classic root

`/assets/` (744), `/getimage.php` (267), `/forum` (93), `/css/` (67), `/ajax/` (66),
`/game` (40), `/news` (18), `/shop` (12), `/privacy` (11), `/garage` (6),
`/ads.txt`, `/app-ads.txt`, `/RELEASE-*/`.

Also modern-only and **not paths at all** — JSON-RPC method names leaking into the
index as if they were URLs, independently corroborating the 144-method map:

```
/forum.getForumThreads  /forum.createForumReply  /forum.setForumThreadPinned …
/garage.getGarageContent  /garage.setAccessory  /garage.setColour
/admin.getAdminLogs  /admin.getAdminRoles  /admin.getAdminStatistics
/gamestate  /gamemodel  /gameendedmessage  /gamestatemessage  /gamemode
```

---

# Part 3 — Wire formats, from decompiles plus archived payloads

## 3.1 The maze format — grade A, verified 100%

Two independent sources agree exactly:

* **The reader.** `MazeDataFetcher.as`, present in decompiles of TankTrouble v3.5,
  v3.6, v3.6e and v3.8c. It parses what the lost editor wrote.
* **The data.** 843 archived `loadMaze.php` responses.

```
GET includes/loadMaze.php?q=<base64( shuffleMessage("userName=<n>&a=<r>&b=<r>") )>
200 →  r=<base64>&s=<slot>
b64 →  t=<title>&n=<author>&d=<grid>
grid = <w>#<cells>#<reserved>#<objCount>#(<x>#<y>#<type>#<params>)…#0#
```

* height is implicit: `h = len(cells) / w` — exact integer for 843/843
* `cells` is one octal digit per cell, row-major:
  **bit0** floor present · **bit1** wall shared with the cell above · **bit2** west wall.
  South and east borders are implicit, from the absence of a neighbour
* objects are **four** fields; `type 5` = tank spawn, `type 8` = crate spawn,
  coordinates 1-indexed
* `reserved` is read into a local and never referenced — a dead field. Emit it anyway
* `shuffleMessage()` randomly permutes `&`-separated pairs. **Not encryption**

**Verification:** a cell whose north or west neighbour is absent must carry that
wall, or the arena leaks. Across 843 mazes / 79,492 cells: **0 violations**.

## 3.2 Editor limits — grade B, from corpus statistics (technique 2)

| Constraint | Value |
|---|---|
| grid | ≤ 18 × 10 |
| title | ≤ 32 chars over `A–Za–z0–9`, space, `! , - . ?` |
| author | ≤ 16 |
| object types | only 5 and 8 |
| max per type | 5 tank spawns, 5 crate spawns; ≤10 total |
| absent cells | legal — 24.4% of corpus cells; 630 of 806 mazes use at least one |

Independently corroborated by the one surviving editor screenshot, which shows a
non-rectangular arena with exactly 5 tanks and 5 crates placed and exactly three
tools in the toolbar.

## 3.3 The maze *save* protocol — grade **none**

Chain of reasoning, each step observed:

1. The 36 SAJAX functions contain **no** maze function → the page did not save it
2. The sibling paint editor writes results into hidden form fields via
   `getURL("javascript: …")` and lets the page do the RPC. mazeCreator cannot have,
   since there is no RPC to call
3. The recovered JS sets `_root.errorPanel.hide` → the SWF owns an error panel →
   the SWF sees the response
4. Therefore it posted directly to its own PHP URL

That URL's **name exists only inside the lost binary**. Every fetch channel is
exhausted, including the HTML5 client (Part 5.3). **M3 — invention.** Keep it behind
one constant.

---

# Part 4 — Server behaviour and PHP

## 4.1 De-rendering: archived HTML is the output of the PHP

The captures are not pages to serve — they are the *result* of the code being
reconstructed. Method in `archive/REBUILD-GUIDE.md` §6.1a; the deduction content:

* **Clean first.** Strip Wayback toolbar injection and URL rewriting (or use `id_`);
  prefer Common Crawl bodies, which are raw
* **Un-do PageSpeed.** `a.js+b.js+tt,_log.js.pagespeed.jc.HASH.js` means the original
  emitted **separate** `<script>` tags. `,_` encodes `/`. Anything PageSpeed did —
  combining, inlining, spriting, whitespace collapse — is **not** in the source
* **Diff across dates** (technique 4). Byte-identical regions across years are
  literal; varying regions are `echo`ed. Repeated blocks at identical indentation
  are a loop — extract the block, not the instances
* **Invert generated regions** (technique 3). Reimplement the SAJAX generator, feed
  it the 36 known names, diff output against captures. A byte match promotes the
  dispatcher from M2 toward M1

## 4.2 Status codes as evidence

| Code | Deduction |
|---|---|
| 200 | path existed and served content |
| 403 | path existed and was protected — `/includes/` → `Options -Indexes` |
| 404 | the **name** was requested by something real; the file may never have existed |
| 200 from an SPA | nothing (Part 2.1) |
| 200 from a versioned CDN path | **check before believing** — five RELEASE tags with no CDX rows returned 200, all serving the *current* build, including a version that never existed |

## 4.3 Endpoints, by evidence strength

| Endpoint | Evidence | Grade |
|---|---|---|
| `includes/loadMaze.php` | 17,411 CDX rows, 843 archived responses, the reader source | **A** — replayable, so `M1` |
| `includes/updateGameStatistics.php` | 2,305 CDX rows, 37 client call sites | C |
| `includes/getScrapyard.php` | CDX with `?scraps`, `?velocity` | C |
| `includes/achievement.php` | 6 client call sites | C |
| `includes/getUserAuthentication.php` | 5 client call sites | C |
| `index.php` SAJAX dispatcher | 36 function names, each dated | C |
| `sendRequest.php`, `changePassword.php` | infirmary HTML comments | C |
| `getimage.php`, `uploadimage.php`, `content.php`, `embed.php` | CDX parameter names only | C |
| maze save endpoint | none | — |

Authentication is deliberately **not** reconstructed. The original ran SAJAX over
GET, which is why real credentials sit in the public Wayback CDX index permanently.
Reproducing it reproduces the leak.

---

# Part 5 — Timeline, from appearance and disappearance

## 5.1 The RPC surface dates the features (technique 5)

Scanning every captured HTML body for `function x_<name>(…)` yields **36** SAJAX
functions, each with a first and last sighting:

| Function(s) | First | Last | Reading |
|---|---|---|---|
| `login logout signup post vote edit updateTank updateTop10 …` (23) | 2010-02-08 | 2020-12-04 | the original surface |
| `generateUsertrail`, `updateFormData` | 2012-01-28 | 2020-12-04 | one release |
| `changePassword`, `sendRequest` | 2012-02-06 | **2018-07-22** | **removed** |
| `checkForAchievements setBan setBanThread …` (5) | 2013-05-23 | 2020-12-04 | one big release |
| `sendVerificationEmail` | 2013-12-06 | 2020-12-04 | pairs with `/verification/` |
| `showShop` | 2015-08-01 | **2017-03-30** | the classic shop was temporary |
| `formCheckEmail` | 2016-05-25 | 2020-12-04 | |
| `getScraps` | **2017-02-21** | 2020-12-04 | same day `scrapyard.js` went live — two independent sources |

Last sighting of any stub is **2020-12-04**, which also bounds the garage teardown.

## 5.2 Embeds date the client (technique 5)

`new SWFObject("…")` across all captures → **20 filenames with live windows**.
`TankTrouble_v4.0.swf` holds one sha256 across 2013-03-13 → 2020-12-25 — the game
binary was **frozen for 7½ years**. `mazeCreator_v0.3.swf` is named in 39 captures
across the same period and never captured once.

⚠ The embed inventory **undercounts**: two `signUpTankDesign` builds we hold appear
in no capture at all. It only sees versions live on a day a crawler fetched the page.

## 5.3 A stub is not a feature

Across all **11** HTML5 releases (2017-10-27 → 2019-11-27), `infoMazeCreator` is
registered with `standard`, `active` and `disabled` images and **no click handler**;
`saveMaze` and `saveArena` appear **zero** times. The HTML5 maze editor was UI
furniture for two years and never built — so it inherited no save endpoint.

*(Caveat: the scan looked for a handler within 120 chars of the registration. A
generic dispatcher elsewhere would not be caught.)*

---

# Part 6 — The client's source tree, from bundle names

Google PageSpeed names a combined file after every input:

```
a.js+b.js+dir,_c.js.pagespeed.jc.HASH.js      (`,_` encodes `/`)
```

Each bundle filename is therefore a **verbatim directory listing the server never
exposed**. Harvesting them across all captures reconstructs **568 client modules**
and 40+ overlays.

Deduction from it: **there is no maze overlay** in the HTML5 client — the third
independent confirmation of Part 5.3.

---

# Part 7 — Visual appearance

The weakest layer, because the editor UI only ever existed behind a logged-in click.

| Source | What it gives | Grade |
|---|---|---|
| `Making a maze.png` (832×556, wiki, 2016-01-30, `version 0.3` watermark) | the complete editor: three toolbar icons, title top-centre, name field bottom-left, ✗/✓ bottom-right, non-rectangular arena, 5 tanks + 5 crates | **A** for layout, **C** for pixels |
| Two other wikis | 821 pages, 105 images, exhaustively enumerated — **zero** editor imagery | firm negative |
| `images/mazeCreator.png`, `tankInfo/mazeCreator{,Active}.png` | the garage's *entry-point* icon, both states | **A** — original bytes |
| Video (YouTube) | UI **in motion** — a tool being clicked gives the same icon in *both* states; likely the only record of the error panel and save dialogue | **M2 at best, never O** |

The screenshot supplies **3 of 6 toolbar icon states** (wall=deselect,
crate=**select**, tank=deselect). The other three are M3.

⚠ 832×556 against a 688×400 stage is 1.209× horizontal and 1.390× vertical — **not
a uniform scale**, so the frame includes panel chrome. Measurements need a per-axis
factor and the icons are not guaranteed 1:1.

Anything traced from video records video URL, uploader, upload date and frame
timestamp in `LEDGER.tsv`. Lossy and rescaled means *reference for redrawing*, not
recovered bytes.

---

# Part 8 — Third-party sources, and their limits

| Source | Verdict |
|---|---|
| **Clone / portal rehosts** | Audited to exhaustion. 2 new builds; all 50 remaining digests trace to three WordPress portals that suffix every game with "tank-trouble". Every 2017–2019 capture is a stale re-upload of a 2011–2014 build |
| **`purup.com`** (the developer's own site) | Swept across 126 crawls. A **one-page contact card** for 16 years — 413 rows, 12 distinct URLs. The dev-blog hypothesis is **disproved**, not unconfirmed |
| **`sublabgames.com`** (his current studio) | Confirmed same owner by shared phone number. No TankTrouble content |
| **`subterraneansoftware.com`** | The **mobile port** developer's blog. Rich detail on Laika's AI (23 raycasts over a 230° arc, bounce prediction by difficulty). **Not authority on the Flash build** — he says he never read that code. M2 for mobile, nothing for Flash |
| **Wikis** | User-written. Useful for screenshots, unreliable for facts. Four exist; one contained the only editor screenshot |
| **Distribution zips** | All four extracted. Client-only, no server code |

---

# Part 9 — What cannot be deduced at all

| Thing | Why |
|---|---|
| PHP source text | a web server emits output, never source |
| DB column types, widths, keys, indexes, collation | never observable through HTTP |
| `.htaccess`, vhosts, `php.ini` | no evidence — except `Options -Indexes`, from the `/includes/` 403 |
| The maze save endpoint's name | lives only inside the lost binary |
| 3 of 6 toolbar icon states | never captured in that state |
| `mazeCreator_v0.2/v0.3.swf` bytes | nothing ever linked to them |

For each of these, `srv/` carries an `M3` file and `DECISIONS.md` carries the reason
the specific choice was made. **M3 is not a failure state — it is an honest label.**
The failure state is an M3 file that reads like an O file.

---

# Part 10 — Reproducing this

```
scratchpad/path_evidence.py     un-partitioned rollup + FILESYSTEM-EVIDENCE.tsv
scratchpad/path_evidence2.py    era partition, artefact filter, /includes/ listing
scratchpad/maze_analyse{,2,3}.py  wire-format decode from the payload corpus
scratchpad/maze_render.py       the 0-violation boundary proof
scratchpad/modules.py           568-module tree from PageSpeed bundle names
scratchpad/maze_button.py       per-release HTML5 button state
```

Re-run after any new fetch lands. Counts move; grades should not. If a grade moves,
that is a finding — record it in `DECISIONS.md`.
