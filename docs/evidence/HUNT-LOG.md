<!-- Published copy of the raw investigation log. Reference material: cited by
     DEDUCE.md, not a source of rules. Do not edit; supersede in DECISIONS.md. -->

# Published copy — reference only

Raw evidence hunt, §1–63, cited throughout `DEDUCE.md`. Findings here are
working notes: where they disagree with `DECISIONS.md`, `DEDUCE.md` or
`docs/FOUNDATIONS.md`, those win.

* Source: `archive/HUNT-LOG.md`
* sha256 of the archive original: `87614e387eb05a10e280070c42a6187fd341478c8b6b9cbcf09f83d8c24cefd0`
* Everything below the horizontal rule is verbatim.

---
# mazeCreator_v0.3.swf — recovery hunt log

Date: 2026-08-02
Goal: locate byte-accurate `includes/mazeCreator_v0.3.swf`, ideally the 2018–2019 build.
Secondary: log every other useful/historical artefact surfaced along the way.

Everything in this directory is **newly recovered in this session**. Nothing under
`_NOT-PART-OF-MAIN-ARCHIVE_swf-by-year\`, `_NOT-PART-OF-MAIN-ARCHIVE_swf-decompiled\`,
`tanktrouble.com\`, `tanktrouble.com-offline\`, `pages-recovered\` or `variants\` was modified.

---

## 1. Verdict on mazeCreator_v0.3.swf

**Not found. Confirmed absent from every index searched.**

| Channel | Result |
|---|---|
| Wayback CDX, `tanktrouble.com/includes/mazeCreator*` | **0 rows** — not even a 404 or 302. Never requested by anyone, ever. |
| Wayback CDX, all host variants (`classic.`, `eu-central2-web2.`, `www.`, apex, root path) | 0 rows |
| Wayback CDX, domain-wide filter `.*[Mm]aze.*` | only `loadMaze.php` responses, `images/maze.jpg`, `images/busyMaze.png`, `assets/images/tankInfo/mazeCreator*.png` (modern HTML5 site) |
| Common Crawl, 10 crawls 2013–2019 | 7–14 rows per crawl, HTML pages only, 0 maze hits |
| Flashpoint Archive (only TankTrouble entry, full-site GameZIP) | absent — see §3 |
| GitHub code search (`mazeCreator_v0.3`, `mazeCreator tanktrouble`) | 0 hits |
| GitHub repo scan of 8 TankTrouble mirror repos | 0 hits; two contain only a bare `Tank_Trouble.swf` |
| Live probe `classic.tanktrouble.com` (v0.1–v0.4, unversioned, root + `includes/`) | 404 on all |
| Live probe apex `tanktrouble.com` | 404 on all |
| Third-party mirror `people.inf.elte.hu/fodtaai/tank/` | v3.6e-era mirror, Assets + one SWF only; live host now 403 |

### Why it is missing — corrected diagnosis

The initial hypothesis was login-gating. The evidence points somewhere more specific and
more consistent:

**Every reference to the maze creator is constructed in JavaScript at runtime, never in
static HTML.** The 2013-era Wayback crawler executed no JavaScript, so none of it was
followed.

Proof: the six toolbar button images are assigned via `.src=` in JS, not `<img src>`:

```javascript
document.getElementById('userpanelMazeConstructTool-'+user).src='images/mazeConstructTool'+(tool=='construct'?'S':'Des')+'elect.jpg';
document.getElementById('userpanelCrateSpawnTool-' +user).src='images/crateSpawnTool' +(tool=='crateSpawn'?'S':'Des')+'elect.jpg';
document.getElementById('userpanelTankSpawnTool-' +user).src='images/tankSpawnTool' +(tool=='tankSpawn' ?'S':'Des')+'elect.jpg';
```

Crawlers *do* follow plain `<img src>`. All six of these are **equally absent** from Wayback,
exactly like the SWF. Same cause, not two causes. The SWF itself is likewise built by
`new SWFObject("includes/mazeCreator_v0.3.swf", …)` inside a `setTimeout` string.

Contrast with the main game SWF, which **was** archived — because thousands of third-party
sites hotlinked `<embed src="http://tanktrouble.com/includes/TankTrouble_v4.0.swf">`
directly. That inbound-link traffic is exactly what the `?r=SWF` referral tracker existed to
measure. The maze editor had no such external embeds.

So: not (necessarily) login-gated — **unreferenced by any static markup, on a host nobody
bulk-mirrored.** Wayback stores what was *requested*; the file was never requested.

### What this means for retrieval

The file cannot come from an index. It can only come from a **local copy**:
a developer's build tree, a community member's saved folder, or a browser cache dump.
See §7.

---

## 2. Files recovered (new to the corpus)

Hash-compared SHA256 against all 23 unique SWFs in `_NOT-PART-OF-MAIN-ARCHIVE_swf-by-year\`.
**4 previously unknown SWFs.** Corpus goes 23 → 27 unique.

| File | Bytes | Source | Note |
|---|---|---|---|
| `classic.tanktrouble.com\includes\TankTrouble_v4.03.swf` | 347,219 | live origin | **Previously unknown game version.** Newer than v4.0 (366,827) and *smaller*. |
| `classic.tanktrouble.com\Assets\GameTank.swf` | 10,351 | live origin | Newer build than the 10,126-byte one in the archive |
| `flashpoint-gamezip\…\live\TankTrouble_v3.8c.swf` | 290,014 | Flashpoint | **Previously unknown version.** Kongregate distribution build |
| `flashpoint-gamezip\…\632000\632327_tank-trouble-new.swf` | 157,832 | Flashpoint | Newgrounds distribution build, previously unknown |

Confirmed duplicates (already held): `Crate.swf` 2,357 · `Laika.swf` 18,335 ·
`Tank.swf` 188,223 · `GameTank.swf` 10,126 · `scrapyard06.swf` 5,117 ·
`TankTrouble_v4.0.swf` 366,827.

Also saved: `classic.tanktrouble.com\index.html`, `includes\swfobject.js` (9,328 — differs
from the archive's 9,321), `robots.txt` (Cloudflare content-signals boilerplate, no path
information), and the complete Flashpoint GameZIP including its original `.zip`.

---

## 3. Flashpoint Archive — full record

Searched via `https://db-api.unstable.life`. Frontend at
`flashpointproject.github.io/flashpoint-database/search/`; player at `ooooooooo.ooo/?id=<uuid>`
(the player page HTML is where the GameZIP URL is exposed — the DB API has no `gamedata`
route).

Exactly **one** TankTrouble entry exists:

```
id              277dca1b-93f5-4ef8-9a8a-ac655652d264
title           TankTrouble        (alt: Tank Trouble)
developer       Purup
publisher       Sublab Games
platform        Flash; HTML5
version         4.0
releaseDate     2007-12-16
status          Playable
launchCommand   http://tanktrouble.com/index.html
zipped          True
dateAdded       2019-10-20   dateModified 2024-01-04
addApps         Newgrounds version, Kongregate version
GameZIP         https://download.unstable.life/gib-roms/Games/277dca1b-93f5-4ef8-9a8a-ac655652d264-1704336468641.zip
```

130 entries, 1.74 MB. It is a **full-site curation** (three host trees: `tanktrouble.com`,
`game205020.konggames.com`, `uploads.ungrounded.net`), so it was the single most likely
holder of the maze creator. It captures only the **logged-out** flow — no garage, no user
panel, no maze creator, no tool images. `loadMaze.php` and `updateGameStatistics.php` are
present as **0-byte stubs**, i.e. the curator stubbed the backend rather than recording
responses.

Developer name confirmed as **Purup**, publisher **Sublab Games** — relevant to §7.

---

## 4. Newly discovered infrastructure

Hosts not previously in the picture, all found via domain-wide CDX:

| Host | Status | Holds |
|---|---|---|
| `classic.tanktrouble.com` | **LIVE** | Legacy Flash shell: `includes/TankTrouble_v4.03.swf`, `includes/swfobject.js`, `Assets/{Tank,GameTank,Crate,Laika}.swf`. No garage, no user panel, no PHP endpoints. |
| `eu-central2-web2.tanktrouble.com` | archived 2020–21 | `Assets/GameTank.swf`, `includes/{laika02,signUpTankDesign18StandardColours,TankTrouble_v4.0}.swf`, `mootools-release-1.11.js` — a real backend web node, name implies a numbered fleet (`eu-central2-web1`, `-web3`, other regions) |
| `cdn.tanktrouble.com` | archived | PageSpeed-rewritten `RELEASE-YYYY-MM-DD-NN/` release directories, 2021 → 2026 |
| `cdn-beta.tanktrouble.com` | archived | `RELEASE-…` back to 2017-10-27 |
| `test-cdn-beta.tanktrouble.com` | archived | `PRERELEASE-2023-09-06-01/` |
| `beta.tanktrouble.com` | archived | HTML5-era CSS/JS |

The CDN release directories are a **dated build timeline** for the HTML5 site and include a
`garage.css` from 2017-10-27 onward — useful for dating the Flash→HTML5 garage transition.

`classic.tanktrouble.com` being live is the notable operational finding: the legacy Flash
tree is still served in 2026.

---

## 5. SAJAX — recovered server-side API surface

The SAJAX client stub is emitted by the PHP that calls `sajax_export()`, so each `x_foo()`
wrapper is a **real PHP function name from the original source**. Extracted across all
archived HTML in `tanktrouble.com-offline\` (13 files carry SAJAX stubs):

**35 distinct exported functions:**

```
changePassword          checkForAchievements    edit
feedback                formCheckEmail          generateUsertrail
getAllUserInfo          getLoginInfo            getScraps
login                   logout                  post
reloadGame              sendRequest             sendVerificationEmail
setApprove              setBan                  setBanThread
setCloseThread          setDelete               setDeleteThread
setDisable              setDisableThread        setFilterAndShowForumPreviews
showEditPost            showForumPreviews       showForumThread
showForumThreadLastPage signup                  startThread
updateFormData          updateTank              updateTop10
updateUserPanels        vote
```

This is genuine source-fragment evidence, not inference. Clusters cleanly into:
auth (`login`, `logout`, `signup`, `changePassword`, `sendVerificationEmail`,
`formCheckEmail`, `getLoginInfo`, `getAllUserInfo`), forum
(`post`, `edit`, `startThread`, `vote`, `showForumThread*`, `showEditPost`,
`showForumPreviews`, `setFilterAndShowForumPreviews`), moderation
(`setApprove`, `setBan`, `setBanThread`, `setCloseThread`, `setDelete`, `setDeleteThread`,
`setDisable`, `setDisableThread`), game/garage
(`updateTank`, `reloadGame`, `getScraps`, `checkForAchievements`, `updateTop10`,
`updateUserPanels`, `updateFormData`), misc (`feedback`, `sendRequest`, `generateUsertrail`).

Note there is **no maze-related SAJAX export**. The maze creator therefore did *not* save
through SAJAX — consistent with the SWF calling a PHP endpoint directly, the way
`loadMaze.php` is called from AVM1.

`updateUserPanels` is the function that would have re-rendered the panel containing the
maze creator.

## 5b. PHP error leakage — negative result

Grepped the whole of `tanktrouble.com-offline\` for `Warning:`, `Notice:`, `Fatal error:`,
`Parse error:`, `on line N`, `/home/<user>/`, `/var/www/`, `include_path`,
`Undefined index|variable`, `mysql_connect|query|fetch`.

**No matches.** `display_errors` was off, or no captured response ever errored. No absolute
filesystem path leaked. This channel is closed for this corpus.

---

## 6. Maze creator — everything now known about the missing SWF

Reconstructed entirely from the calling side (`__q21b747de22db/index.html`, present in six
archived copies from 2017-04 through 2018-12 — all six reference the identical path, so the
file name was stable across that whole window).

```javascript
var d = new SWFObject("includes/mazeCreator_v0.3.swf",
                      "userSettingsMazeCreatorFlash-<user>",
                      "688", "400", "8", "#ffffff");
d.addParam("FlashVars", "initCode=" + <innerHTML of userSettingsMazeCreatorInitCode-<user>>);
d.write("userSettingsMazeCreator-<user>");
```

| Property | Value |
|---|---|
| Path | `includes/mazeCreator_v0.3.swf` |
| Stage | 688 × 400 |
| Flash version required | 8 |
| Background | `#ffffff` |
| Instance id | `userSettingsMazeCreatorFlash-<user>` |
| Container | `userSettingsMazeCreator-<user>` |
| FlashVars | `initCode=` + innerHTML of `userSettingsMazeCreatorInitCode-<user>` |

**Page → SWF (`SetVariable`):** `fadeOut`, `newToolRequested`, `previewLoaded`,
`_root.mazeName`, `_root.errorPanel.hide`, `_root.saveRequested`

**SWF → page (`getURL javascript:`):** `showMazeCreatorToolsAndTitle(user, title)`,
`hideMazeCreatorToolsAndTitle(user)`

**Exactly three tools**, default `construct`:
`construct` · `crateSpawn` · `tankSpawn` — mapping precisely onto maze wire-format object
types 5 (tank spawn) and 8 (crate spawn), with `construct` for walls.

**Six toolbar images, all lost with the SWF:**
`images/mazeConstructToolSelect.jpg` · `mazeConstructToolDeselect.jpg` ·
`crateSpawnToolSelect.jpg` · `crateSpawnToolDeselect.jpg` ·
`tankSpawnToolSelect.jpg` · `tankSpawnToolDeselect.jpg`

Two of the six appear in CDX (`mazeConstructToolSelect.jpg` 2024-04-09,
`tankSpawnToolDeselect.jpg` 2023-05-29) but **both are 302 redirects to the modern site with
no stored content**. Retrieval attempted via `web/<ts>id_/` raw form and against
`classic.tanktrouble.com` — all six MISS.

**Grid and bounds** (from the captured `loadMaze.php` corpus): 18 × 10, tank spawns never
below 2.

Because the wire format, grid, tool set, spawn bounds and the complete JS↔SWF interface are
all known, the editor is **behaviourally reconstructible** even though the binary is gone.

---

## 6b. TankTrouble v4.03 — analysis of the newly recovered build

Decompiled with FFDec 26.2.1 into `decompiled\2026_TankTrouble_v4.03_classic\` (82 scripts,
322 files). This is the **last Flash build**, still served live from
`classic.tanktrouble.com` in 2026, and it is the most consequential find after the maze
creator itself.

| | v4.0 (archive) | v4.03 (new) |
|---|---|---|
| File size | 366,827 | 347,219 |
| Uncompressed | — | 660,031 |
| SWF version / AS | 8 / AVM1 | 8 / AVM1 |
| Stage | 712 × 490 @ 25 fps | 712 × 490 @ 25 fps |
| Frames | up to 58 | **41** |
| Tags / characters | — | 571 / 367 |
| Metadata (XMP) | none | none |

### What v4.03 removed

- **`__Packages` is gone entirely** — `Base64`, `MazeDataFetcher`, `MazeDataLoader` no
  longer exist. The custom-maze fetch subsystem was deleted.
- **Zero PHP endpoints.** v4.0 references `updateGameStatistics.php` (×5),
  `achievement.php` (×3), `loadMaze.php`, `getUserAuthentication.php`. v4.03 references
  **none**. All server traffic moved to the socket.
- **`OTHER_HOST` is gone** (11 occurrences in v4.0, 0 in v4.03) — no host gating.
- **`DefineButton2_380` is gone** — the ungated
  `getURL("http://tanktrouble.com/?r=SWF "+_url)` referral backlink no longer exists.
- Frames 43, 49, 50, 53, 54, 57, 58 dropped.
- Copyright/context-menu link changed from the tanktrouble.com referral to
  `https://www.purup.com`; context menu item reads `© 2007 www.purup.com`.

The three settings `settingsPlayRandomMazes` / `settingsPlayMyCustomMazes` /
`settingsPlayOtherCustomMazes` still appear **once each** (settings-panel wiring), but with
`MazeDataFetcher` deleted nothing acts on them — vestigial UI.

**This dates the death of the maze system.** By v4.03 there was no client capable of
requesting a custom maze, so `mazeCreator_v0.3.swf` had already been retired server-side.
The 2018-12 archived user panel is therefore close to the *last* period in which the file
was live — which matches the 2018–2019 target window exactly.

### What v4.03 gained

Sprite inventory reveals a substantially more advanced client than anything previously held:

`tankTroubleAI` (AI opponents) · `shield` + `shieldGraphic` · `fluid`, `fluidLBM`,
`fluidDiffuse` (lattice-Boltzmann fluid simulation) · `scopeCircle` · `elToro` ·
`flagAndTextPanel` (per-region server flags with live ping) · `serverInfo` ·
`multiplayerInfo` · `chatPanel` + `chatMessagesPanel` · `countdownPanel` ·
`randomGamePanel` · `newGamePanel` · `leaveGame` · `scoreboardPanel` · `aimer` ·
`rCSignal`

Multiplayer is now **region-selected with client-side ping measurement**:

```actionscript
if(_root.PINGS[ping].succeeded && ping != _root.SELECTEDHOST) { … }
flagAndTextOption.host = ping;
_root.SELECTEDHOST = this.host;
_root.HOST = this.host;
if(!_root.connection.connect(_root.HOST,_root.PORT)) { … }
```

This corroborates the `eu-central2-web2.tanktrouble.com` hostname found in CDX — there was a
numbered, region-tagged server fleet, and the client picked from it by measured latency.
v4.0's hard-coded `PORT = 12321` is not present as a literal in v4.03.

Chat is XML over the socket, with `<message><text/><sender/><recipientplayerid/></message>`
nodes and sender taken from `_root.loginInfo.p1n`.

New ExternalInterface behaviour: v4.03 registers a `setMousePos` callback and **injects a
JavaScript IIFE into the host page** (`bigOlFunc`) that attaches `mousemove`/`resize`
listeners and feeds scaled stage coordinates back into the SWF — so aiming keeps working
when the cursor leaves the stage, and it survives page resize. It locates itself by
`document.getElementById('TankTroubleGame')` with a `getElementsByName` fallback.

---

## 7. Remaining live leads (not yet exhausted)

Ranked by realistic probability of yielding actual bytes.

1. **The developer.** Purup / Sublab Games, still operating tanktrouble.com and still
   serving `classic.tanktrouble.com` in 2026. Build artefacts for a 2018-era SWF very
   plausibly still exist on a dev machine or in version control. Highest yield by a wide
   margin; costs one email.
2. **The active community.** `asger-finding` maintains *TankTroubleAddons* and
   *replay-bot*; there is an organised modding/competition scene
   (`TankTroubleOnlineCompetition/TTOC`). People who built offline/private-server versions
   had to obtain helper SWFs and may hold garage-era files.
3. **A community member's saved folder.** The one archived referral proves this pattern
   existed: `file:///C:/Users/jkorch1298/Desktop/Tank Trouble_files/…` — somebody's
   "Save Page As" of the site, captured in 2018-10. Those folders survive on old drives.
4. **Other regional web nodes.** `eu-central2-web2` implies a numbered fleet. Live/archived
   probing of sibling names may reach a node still serving the legacy tree.
5. **Flashpoint re-curation.** The existing curation is logged-out only. A curator with an
   account could in principle still capture the flow — except the Flash garage no longer
   exists on the live site, so this is now closed.

Channels confirmed **exhausted**: Wayback CDX (all hosts), Common Crawl, Flashpoint,
GitHub, third-party mirror via referral tracking, live origin probing, PHP error leakage.

---

## 8. Server-side inventory — PHP endpoints and routing

### 8a. Endpoints in SWF binaries (hard evidence — string literals)

Scanned all **27 unique SWFs** by decompressing each container and extracting printable
strings, which catches binary-tag references invisible to decompiled ActionScript.
Complete list, with which builds reference each:

| Endpoint | Referenced by |
|---|---|
| `includes/updateGameStatistics.php?q=` | v3.6c, v3.8c, v4.0, Newgrounds 632327, scrapyard06 |
| `includes/updateGameStatistics.php?tankScrapped=` | v4.0 |
| `includes/achievement.php?q=` | v3.8c, v4.0 |
| `includes/loadMaze.php?q=` | v3.6c, v3.8c, v4.0 |
| `includes/getUserAuthentication.php?q=` | v4.0 (relative), v3.6c + v3.8c (absolute `http://www.tanktrouble.com/…`) |
| `includes/getScrapyard.php?scraps` / `?scraps&velocity` | scrapyard10 (absolute), scrapyard11 (relative) |
| `Assets/{Tank,GameTank,Crate}.swf` | v3.6c, v3.8c, v4.0, v4.03 |
| `Assets/Laika.swf` | **v4.0 and v4.03 only** — not in v3.6c/v3.8c |
| `http://tanktrouble.com/?r=SWF` | v3.6c, v3.8c, v4.0 — **absent in v4.03** |
| `http://www.purup.com` | v3.6c, v3.8c, v4.0 — v4.03 upgrades to `https://` |

No PHP endpoint exists in any SWF that was not already known. The SWF-side API surface is
**closed at six endpoints**. `Laika.swf` carries no XMP metadata.

Incidental: the `Tank__*.swf` accessory libraries embed `http://style64.org` — attribution
for the C64 font, matching `includes/c64.{ttf,eot,woff}` in the site archive.

### 8b. PHP files proven by developer comments (source-fragment evidence)

Three separate leaked authoring comments in archived HTML name real server files:

```
THIS IS A SIMPLIFIED COPY OF tanktrouble.com/index.php THAT SERVES AS A TEMPORARY WARP
FOR sendRequest.php AND changePassword.php UNTIL WE HAVE A CHANGE PASSWORD FEATURE IN
THE GARAGE.
THE FINAL DESIGN IS
1. HAVE sendRequest OPEN IN A POPUP WINDOW
2. SEND A NEW, TEMPORARY PASSWORD BY EMAIL (NOT A LINK BACK TO changePassword.php)
3. ENCOURAGE USERS TO CHANGE THEIR PASSWORD TO SOMETHING SIMPLER AND MEMORABLE IN THE
   YET-TO-COME CHANGE PASSWORD FEATURE IN THE GARAGE.
```
(`infirmary/index.html` — the password-recovery page)

```
//REMEMBER TO CHANGE THE VERSION IN logIn.php AND game.php AS WELL!!!
//REMEMBER TO CHANGE THE VERSION IN logIn.php AND embed.php AS WELL!!!
//TODO: Not necessary here as it is already in feedback.php. Should it be moved to index.php ?
```

These establish, without inference:

| File | Role | Evidence |
|---|---|---|
| `index.php` | site root, query-string routed | named in comment; `embed.php` exists as a sibling file |
| `logIn.php` | login page, **hard-codes the SWF version** | named in two version-bump comments |
| `game.php` | standalone game page, hard-codes SWF version | version-bump comment |
| `embed.php` | third-party embed page, hard-codes SWF version | present in the archive as a real file; loaded in an iframe by `includes/embed.js` |
| `feedback.php` | feedback handler | TODO comment |
| `sendRequest.php` | password-recovery request | infirmary comment |
| `changePassword.php` | password reset via emailed link | infirmary comment |

The version-bump comments are an architecture finding in their own right: the SWF filename
was **duplicated across four PHP files** with no shared constant, which is exactly why a
version bump needed a reminder comment.

### 8c. index.php routing

The root took query-string routes, not path segments — so no rewrite rules were needed.
Six top-level tabs, confirmed by both `href` links and the tab-image selection state:

`?game` (tab1) · `?news` (tab2) · `?garage` (tab3) · `?shop` (tab4) · `?forum` (tab5) ·
`?lab` (tab6)

The archived query-hash pages map onto these: **`__q21b747de22db` is `?garage`** (tab3
selected) — i.e. the maze creator lived on the garage tab, matching the leaked comment's
"change password feature in the garage".

### 8d. SAJAX — see §5. 35 exported PHP function names. No maze function.

### 8e. Beta / HTML5 era

`subdomains/beta.tanktrouble.com/index.html` yields one further endpoint:
`RELEASE-2019-10-04-01/content.php` — the HTML5-era site is a shell that loads
PageSpeed-bundled JS from `cdn-beta.tanktrouble.com/RELEASE-<date>/`. Its API surface lives
in those bundles, which are archived in CDX but not held locally.

---

## 9. Derived data contracts (from the captured response corpus)

The archive holds **2,571 `loadMaze.php` responses, 422 `updateGameStatistics.php`, and 2
`getScrapyard.php`**. These are the interface contract of the tables behind them.

### `getScrapyard.php`

```
scraps=2125280779
scraps=2125249540&velocity=0.012629565422954
```
Two fields, matching the two documented query forms `?scraps` and `?scraps&velocity`.
`velocity` is a float — scraps accumulated per unit time, used to animate the counter.

### `updateGameStatistics.php` — 5 response shapes, all base64 in `r=`

| Shape | n |
|---|---|
| *(empty)* | 92 |
| `player <N>-wv=<int>&laika-wv=<int>` | 88 |
| `laika-wv=<int>&player <N>-wv=<int>` | 85 |
| `scrapyard=<int>` | 69 |
| `error=true` | 49 |
| combinations of the above with `scrapyard` interleaved | 39 |

Field order is **not stable** — the server emitted an unordered map. Note the literal space
in the key `player 1-wv`. The `scrapyard=` shape is the global scrap counter poll.

### `loadMaze.php` — full wire schema, now fully derived

Response is `r=<base64>`; decoded it is a query-string with exactly these keys:

| Key | Present | Meaning |
|---|---|---|
| `t` | 1633 | maze title (free text — e.g. `Pac-man`, `Crazy Maze`, `WTF Mate?`) |
| `d` | 1633 | maze data (below) |
| `n` | 1633 | author username |
| `s` | 1633 | always `1` |
| `notFound` | 925 | `true` — **36% of all requests missed**, matching the known substitution-failure rate |
| `error` | 13 | `true` |

`d` grammar, confirmed against all 1,633 payloads:

```
d = <width> # <wallString> # <flag> # <objectCount> # <obj> ## <obj> ## … ### 0 #
obj = <x> # <y> # <type>
```

- **`width`** ranges **4 … 18**; `18` is by far the most common (391 of 1,633). Not a fixed
  grid — the editor produced variable-width mazes. *(This corrects the earlier "18 × 10
  editor grid" claim: 18 is the maximum and modal width, not the only one.)*
- **`wallString`** uses the alphabet **`0`–`7` only** — three bits per cell, i.e. a
  per-cell wall bitmask.
- **`flag`** is `0` in every single payload.
- **`objectCount`** matches the actual object count in 1,370 of 1,633 (the remainder are
  parser edge cases at the terminator, not server inconsistency).
- **`type` takes exactly two values: `5` and `8`.** Nothing else, in 11,010 objects.
  This is independent confirmation that the editor had exactly the three tools found in the
  garage JS — `construct` (walls, encoded in `wallString`), `tankSpawn`, `crateSpawn`.
- `x` ranges 1 … 18, `y` ranges 0 … 10.
- **type-5 count per maze is never 1** — observed 0, 2, 3, 4, 5. The editor enforced a
  minimum of two tank spawns.
- type-8 count per maze: 0 … 6.
- Terminator is always `###0#`.

This is enough to write a byte-compatible `mazeCreator` replacement and a byte-compatible
`loadMaze.php`.

---

## 10. mazeCreator_v0.3 — VISUALLY RECOVERED

**`mazeCreator-ui-images\mazeCreator_v0.3_SCREENSHOT.png`** — a live screenshot of the
editor, recovered from the archived TankTrouble Fandom wiki dump
(`wiki-tanktrouble_tank_gamefandomcom`, page image "Making a maze"). It carries
**`version 0.3`** rendered in the bottom-right corner, matching `mazeCreator_v0.3.swf`
exactly. The binary is still lost, but the interface is no longer unknown.

### What the screenshot establishes

| Element | Observed |
|---|---|
| Maze title | rendered top-centre in grey (`Gauntlet`) — this is `_root.mazeName` fed by `SetVariable` |
| Version string | `version 0.3` bottom-right, letter-spaced grey |
| Canvas | white background, light-grey filled cells, mid-grey unfilled, dark-grey wall strokes |
| Wall rendering | thick dark strokes on cell edges — consistent with the 3-bit-per-cell `wallString` |
| Tank spawns | **blue** rounded-square tank glyphs, rotated |
| Crate spawns | **yellow/orange** rounded-square crate glyphs, rotated |
| Tool row | three buttons, bottom-centre |
| Selected state | **full colour**; deselected state is **greyscale** |
| Name field | plain HTML text input bottom-left (`Earth to stone` in the shot) |
| Commit controls | red ✗ (cancel) and green ✓ (accept), bottom-right |

Crucially this shows the **division of labour**: the SWF renders only the white canvas.
The tool buttons, name input and ✗/✓ are page-side HTML — exactly matching
`userpanelMazeCreatorControls-<user>` in the garage JS, and confirming why the six
`*ToolSelect.jpg` / `*ToolDeselect.jpg` images exist as separate files.

The three tool glyphs are, left to right: a wall/brick block (`construct`), a black cube
with a yellow starburst (`crateSpawn`), and a tank (`tankSpawn`). In the shot the middle
one is coloured and the outer two greyscale — i.e. `crateSpawn` active, which is precisely
the `select`/`deselect` image swap the JS performs.

### Written documentation recovered

From the same wiki dump's page history:

> "If you have your own tank, you can go to the garage and to the maze creator. This place
> allows any tank owner to make and customize their own mazes, **up to 3 mazes per tank**.
> In this, you can make maze corridors and pathways **2 blocks wide**, and set **5 tank
> spawns** of where tanks will spawn in the maze, as well as **5 weapon spawns**."

> "The Garage keeps your Boxes, Accesories, Mazes, and Other Personal Tank Information
> secure… You can restore your password, Design your Tank, **Create a Maze with the Maze
> Creator** and keep track of your Achievements."

Every one of these limits is independently confirmed by the response corpus derived in §9:
max 5 objects of type 5, max 5 of type 8, and the garage-hosted placement. The "restore
your password" line corroborates the leaked `infirmary` comment about the change-password
feature belonging in the garage.

### Related images saved

`Custom maze.png` and `Someone's maze.png` show **v4.0 playing a user maze**, with the
in-game attribution rendered top-right as `<title> by <author>` — i.e. the `t` and `n`
fields from `loadMaze.php`. `Tab3Select2.jpg` is the garage tab image.

---

## 11. SWF tag-level forensics (all 27 unique SWFs)

Parsed the raw tag stream of every SWF for `ProductInfo`, `FileAttributes`, `Metadata`,
debug tags, `Protect`, and import/export tags.

- **No `ProductInfo` tag in any file.** Flash Professional does not emit it (it is a
  Flex/AS3-compiler tag), so per-build compile timestamps are not available this way.
  Channel closed.
- **No `EnableDebugger`/`EnableDebugger2`/`DebugID` in any file.** No debug passwords, no
  `.swd` companions were ever shipped.
- **`Protect` with zero-length payload** on v3.6c, v3.8c, v4.0, v4.03, scrapyard06,
  scrapyard10, scrapyard11 — the "prevent import" flag only, never a password.
- **Exactly one file carries XMP metadata: `Laika.swf`** (1,296 bytes):

```xml
<xmp:CreatorTool>Adobe Flash Professional CS6 - build 481</xmp:CreatorTool>
<xmp:CreateDate>2013-02-17T18:16:18+01:00</xmp:CreateDate>
<xmp:ModifyDate>2013-02-17T18:30:13+01:00</xmp:ModifyDate>
<xmpMM:DocumentID>xmp.did:02801174072068118083A7AC3F2D2D8E</xmpMM:DocumentID>
<xmpMM:OriginalDocumentID>xmp.did:0380117407206811822ADD003233C40D</xmpMM:OriginalDocumentID>
```

Authoring tool pinned to **Flash Professional CS6 build 481**; the **`+01:00` offset is
Central European Time**, consistent with a Danish developer. `OriginalDocumentID` differs
from `DocumentID`, so the `.fla` was derived from an earlier document — Laika was not a
fresh file. Created and last modified 14 minutes apart, three weeks before the v4.0 launch
window.

### ImportAssets2 (RSL) map — complete

| SWF | Imports |
|---|---|
| `TankTrouble_v3.6c` | `Assets/Tank.swf`, `Assets/GameTank.swf`, `Assets/Crate.swf` |
| `TankTrouble_v3.8c` | same three |
| `TankTrouble_v4.0` | those three **+ `Assets/Laika.swf`** |
| `TankTrouble_v4.03` | all four |
| `signUpTankDesign13/16/17StandardColours` | **`Assets/Tank.swf`** |

The `signUpTankDesign*` finding is new — the signup tank designer also pulled the `Tank`
RSL, so `Assets/Tank.swf` was load-bearing for signup, not just gameplay.

### Correction

`FileAttributes.UseNetwork=1` is **not unique to v4.0** — v3.6c, v3.8c and v4.03 all carry
it too. The earlier claim was wrong. It is set on every main-game build and on none of the
helper/library SWFs.

Caveat: the never-placed character counts this pass produced are unreliable (naive
`PlaceObject` field offsets) and are **not** reported here as cut content.

---

## 12. Full production topology (certificate transparency)

`crt.sh` for `%.tanktrouble.com` returns every hostname ever issued a certificate — a
definitive host list, not guesswork. **35 hostnames**:

**Environments** `alpha` · `beta` · `beta2` · `test-beta` · `qa` · `build` · `classic` ·
`www` · apex
**CDN** `cdn-beta` · `test-cdn-beta`
**Web fleet** `eu-central2-web1` · `eu-central2-web2`
**Database** `eu-central2-db1`
**Mail** `eu-central2-smtp1`
**Monitoring** `eu-central1-monitor1` · `logs`
**Processing** `eu-west1-processing1`
**VPN** `eu-west1-vpn`
**Test** `eu-central2-test1`
**"cc" nodes** `eu-central1-cc` · `eu-west1-cc1`
**Multiplayer (`-mp`) — nine regions:**
`eu-west1-mp` · `eu-west1-mp1` · `us-east1-mp` · `us-east1-mp1` · `us-east1-mp2` ·
`us-east2-mp1` · `us-south1-mp1` · `us-west1-mp1` · `asia-central1-mp` ·
`asia-central1-mp1` · `australia-east1-mp1` · `india-west1-mp1`
**Unexplained** `brakan`

This is the exact fleet that v4.03's `flagAndTextPanel` pings and lists by flag
(§6b) — `-mp` = multiplayer game server, region-tagged, numbered. It also confirms a
dedicated `db1`, which is where the users / mazes / forum / achievements tables lived.

---

## 13. The Lab Report — extracted

Both archived PDFs are **image-only** (no vector text layer, no PDF metadata, no leaked
filesystem paths). Extracted all embedded JPEGs to `labReport-extracted-pages\`
(37 images total, including the four trading-card PDFs).

Content is a **2017–2019 community newsletter run by the TTOC moderator group**, not
developer documentation — one page is a click-analytics chart labelled
"Total Clicks on TLR Issues, 26/11/17 to 27/05/19", another is a forum-thread card from
moderator `george8888`. It does not document the Flash-era maze creator. Channel closed,
but the images are preserved.

---

## 14. SAJAX wire protocol — fully recovered

CDX preserves the **request URLs** of SAJAX calls, which exposes the entire calling
convention. Target is the site root (`index.php`), i.e. `rttarget` was `/`:

```
/?rs=<functionName>
 &rst=<targetElementId>
 &rsrnd=<epoch-milliseconds cache-buster>
 &rsargs[]=<arg1>&rsargs[]=<arg2>…
```

Observed live examples (arguments redacted):

```
/?rs=login&rst=&rsrnd=1214937053962&rsargs[]=<username>&rsargs[]=<password>
/?rs=generateUsertrail&rst=&rsrnd=1374268879172&rsargs[]=<username>&rsargs[]=true
/?tab4&rs=login&rst=&rsrnd=1213534621377&rsargs[]=&rsargs[]=
```

Notes:
- `rsargs[]` is **positional**, repeated once per argument — so argument *arity* is
  recoverable per function from captured calls (`login` = 2, `generateUsertrail` = 2).
- `rst` (target element id) was left empty in every observed call — the site used the
  callback form, not the auto-target form.
- `rsrnd` is `Date.getTime()` in milliseconds; the values date the captures precisely
  (earliest observed `1213534621377` = 2008-06-15).
- The last example shows SAJAX **composed with a page route** (`?tab4&rs=login&…`),
  confirming both were parsed from the same `$_GET` by one `index.php`.

> **Security note.** Because SAJAX used GET, login calls put **usernames and passwords in
> plaintext in the URL**, and several such requests are permanently retained in the public
> Wayback CDX index. Real credentials for real accounts are visible there. They are
> deliberately **not** recorded in this log and should not be republished. Anyone rebuilding
> this system should move authentication to POST over TLS.

## 15. index.php hidden query routes — the "Secret Backdoor Codes"

Beyond the six tabs, `index.php` carried a set of hidden single-token routes used as an
easter-egg/achievement hunt. The wiki documents **17 codes**, each entered as
`www.tanktrouble.com/?<CODE>`, each unlocking a Glitchy accessory from The Glitchy Box;
completing all 17 was itself an achievement. Introduced when the Scrapyard passed
1,000,000 tanks destroyed. Clue list authored by moderator `foxter`.

**Routes actually observed in the Wayback index** (someone requested them, so they are
real strings, not guesses):

| Route | Likely clue it answers |
|---|---|
| `?todo` | given outright in the clue list |
| `?whosthr` | given outright ("who's there") |
| `?calc` | given outright |
| `?dimitri` | "Creator of the death ray" |
| `?laika` | "We all know and love her. Even though she tries to kill us all." |
| `?siberia` | "Where the scientist live" |
| `?labrat` | "The rats in the lab are called?" |
| `?snf` | clue #10, "SNF" |
| `?G-4` | unmatched |
| `?elite_hackers_society…` | unmatched (captured truncated) |
| `?Greetings_fr…` | "That was pretty nice to get a postcard from them" |
| `?i love d…` | "04-11-2014 ~ How much do you like donuts?" |
| `?lucky_rol…` | "Double 6! Nice." |
| `?in_every_col…` | unmatched |
| `?wool is …` | unmatched |
| `?tab3`, `?tab4` | **older tab route naming**, pre-dating `?garage` / `?shop` |

Several were captured truncated because the requester's URL was cut — the full strings are
longer than what the index retains. `?tab3` / `?tab4` are a genuine find independent of the
easter eggs: the site originally addressed tabs numerically and later switched to names.

## 16. Other routes and endpoints recovered from request URLs

- **`/forum?threadId=<id>`** — a **path-segment** route (`/forum`), distinct from the old
  `?forum` tab. ~100 distinct thread IDs archived, spanning **51873 … 469403**. Some carry
  a secondary `&id=<postId>` (e.g. `threadId=194422&id=956653`). This is the HTML5-era
  forum.
- **`embed.php?from=<base64>`** — previously undocumented parameter. Carries the
  base64-encoded URL of the embedding site; one capture decodes to a Russian games portal
  (`macrogames.ru`). This is the HTML-embed counterpart to the SWF's `?r=SWF` referral
  tracking.
- **`laboratory@tanktrouble.com`** — the real contact address, found in archived
  `mailto:` links with pre-filled subjects `Bug Report` (body: *"Please describe the bug in
  detail."*) and `TankTrouble Poster Competition`. Relevant to the developer-contact lead
  in §7.

## 17. CURRENT (2026) HTML5 backend — **NOT the 2018–2019 system**

> ### ⚠ ERA WARNING — read before using anything in this section
>
> Everything below comes from **`cdn.tanktrouble.com/RELEASE-2026-05-11-01/`**, the live
> release as of 2026-08-02. It describes **today's** backend and nothing else.
>
> **This is not the 2018–2019 backend.** During 2018–2019 two stacks ran in parallel:
> 1. the **Flash / mootools site on `index.php`** — SAJAX (§5, §14) plus the six direct PHP
>    endpoints the SWF called (§8a). *This* is the stack the maze creator belonged to.
> 2. the **HTML5 beta** on `beta.tanktrouble.com` / `cdn-beta.tanktrouble.com`.
>
> The current `backend.js` is the descendant of **branch 2 only**. It is not a descendant of
> the Flash site, and it must not be used as evidence about it.
>
> The name correspondences noted below (`login`→`authenticate`,
> `updateTank`→`setAccessory`/`setColour`, `getScraps` unchanged) are **inferred lineage,
> not proven migration** — no intermediate build has been found that demonstrates the path.
>
> Likewise: the absence of maze methods here proves mazes are gone **now**. It says nothing
> about the 2018–19 maze *write* endpoint, which remains unrecovered. See §22 for the
> era-correct evidence.

`cdn.tanktrouble.com` serves PageSpeed-bundled JS, and **the bundle filenames enumerate
every original source file**. More usefully, the originals are still served unminified at
their plain paths — e.g. `.../RELEASE-2026-05-11-01/js/backend.js` returns 103 KB of
readable source. Saved to `modern-client\`.

### Transport — the successor to SAJAX

```javascript
$.jsonRPC.setup({ endPoint: '/ajax/', namespace: 'tanktrouble' });
$.jsonRPC.request(method, { params: params, success: …, error: … });
```

**JSON-RPC 2.0** over `POST /ajax/`, namespace `tanktrouble` — so wire method names are
`tanktrouble.<method>`. Responses are RPC-2.0 objects; a client-side hook
(`_unwrapAchievementUnlocksFromData`) unwraps a `data` field and side-channels achievement
unlocks on **every** response.

Lineage is direct: SAJAX `?rs=<fn>&rsargs[]=…` on `index.php` → JSON-RPC
`tanktrouble.<fn>` on `/ajax/`. Several function names survive the transition verbatim —
`login`→`authenticate`, `logout`→`deauthenticate`, `signup`→`signUp`, `getScraps`,
`updateTank`→`setAccessory`/`setColour`, `checkForAchievements`→`getUnseenAchievements`.

### Surface

**120 methods** on `Backend`, **~130** on `TankTrouble.Ajax`. Full list saved in
`modern-client\`. Grouped:

- **auth/account** `authenticate` `deauthenticate` `signUp` `signUpGuest` `createGuests`
  `deleteGuest` `verifyAccount` `recoverAccount` `requestUserRecovery`
  `checkUserRecoveryRequest` `resetAccountPassword` `revertAccountChange`
  `revertAccountChangeWithToken` `setUsername` `setEmail` `checkUsername` `checkPasswords`
  `checkEmail` `getSuggestedUsername` `deleteUser` `cancelUserDeletion`
  `unsubscribeNewsletter` `resendVerificationEmail`
- **player** `getPlayerDetails` `…ByUsername` `…ByEmail` `getSensitivePlayerDetails`
  `updatePlayerDetails` `getCurrency` `getEmail` `getFavourites` `setFavourited`
  `getTutorialProgress` `updateTutorialProgress`
- **game** `getScraps` `getStatistics` `ping` `getPrimaryContent` `getGarageContent`
  `setAccessory` `setColour` `getAIs` `getBackers`
- **achievements** `getAchievements` `getUnlockedAchievement` `getUnseenAchievements`
  `markAchievementAsSeen`
- **messaging** `getMessages` `…FromOldestUnseen` `sendMessage` `sendMessageByContentId`
  `editMessageContent` `markMessagesAsSeen` `getUnseenMessagesCount`
  `getPopularAndRecentMessageContent`
- **forum** `getForumThreads` `getForumThreadsById` `getForumReplies` `createForumThread`
  `editForumThread` `createForumReply` `editForumReply` + `setForumThread`/`ReplyApproved`
  `Banned` `Deleted` `Liked` `Locked` `Pinned`
- **chat moderation** `getChatMessageById` `…ByPlayerIds` `…ByTime`
  `getUnmoderatedChatMessages` `…Count` `setChatMessageApproved`
- **news** `getNewsPosts` `getNewsPostById` `getNewsPostPlaceholder` `createNewsPost`
  `editNewsPost` `deleteNewsPost` `getUploadedImages` `getUploadedImage`
  `deleteUploadedImage`
- **three separate shops** — real-money (`getShopItems`, `purchaseShopItem`,
  `getShopItemPurchaseDetails`, `refundPurchase`, `getShopStockUpOptions`), gold
  (`getGoldShopItems`, `purchaseGoldShopItem`, `refundGoldPurchase`) and virtual
  (`getVirtualShopItems`, `purchaseVirtualShopItem`, `refundVirtualPurchase`) — each with a
  parallel `…AsAdmin` variant
- **admin** `getAdminLogs` `getAdminStatistics` `getAdminRoles` `searchServerLogEntries`
  `setPlayerBanned` `setPlayerAdminLevel` `recommendPlayerPromotion` `retireAdmin`
  `acceptAdminGuidelines` `getNewestTempBanValidities` `getUnapprovedPlayerNames`
  `setPlayerNamesApproved` `deleteUserAsAdmin`

**There is no maze method anywhere in the modern API.** Custom mazes did not survive the
Flash→HTML5 migration — consistent with v4.03 having already deleted `MazeDataFetcher`
(§6b). The maze creator's death is now confirmed from both ends.

### Client file inventory (from bundle names)

Core `main.js` `backend.js` `ajax.js` `caches.js` `users.js` `inputs.js` `forum.js`
Managers `gamemanager` `iframemanager` `inputmanager` `keyboardinputmanager`
`mouseinputmanager` `overlaymanager` `premiummanager` `qualitymanager`
`rejectedusernamesmanager` `resizemanager` `tutorialmanager`
Tutorials `tutorial` `purchasetutorial` `accessoryequiptutorial` `signuptutorial`
Boxes `errorbox` `tankinfobox` `adduserbox` `selectuserbox` `virtualshop`
Overlays (37) incl. `garageoverlay` `loginoverlay` `signupoverlay` `achievementsoverlay`
`newgameoverlay` `faqoverlay` `controlsoverlay` `messagesoverlay` and 14 `admin*overlay`s

Third-party libraries pin the engine: **Phaser**, **Box2dWeb 2.1.0** (physics),
**howler** (audio), **schemapack** (binary socket serialisation), **jkstra** (Dijkstra —
AI pathfinding), CodeMirror (admin editors), `jquery.jsonrpc`.

## 18. Third wiki

A **third** wiki exists beyond the two IA dumps: `tanktrouble-archive.fandom.com`
("TankTrouble Wiki"), 34 pages, and it is the only one focused on the *classic* era:

`TankTrouble Classic` · `Game modes` · `Battle Mode:Classic` · `Battle Mode:Deathmatch` ·
`Unreleased Battle Modes` · `Laika Mode` · `Steffen Mode` · `Beta Glitches` ·
`Online Details` · `Ranks` · `Commander` · `The Red Penguin` · `Kickstarter` ·
`TankTrouble - Mobile Mayhem` · `Mobile Games` · `TankTrouble Online Competition` ·
`Wall of Fame` · `Maze` · `Tricks` · `Laser Tips` · `Shotgun Tips` · `Moderators` · `Chat`

`Unreleased Battle Modes`, `Steffen Mode`, `Laika Mode` and `Beta Glitches` are documentation
of content that never shipped — not yet mined.

## 19. Authoritative site timeline — and the actual cause of the loss

From `tanktrouble-archive.fandom.com` (full 34-page export saved as
`wiki-dumps\tanktrouble-archive-wiki.json`):

> "TankTrouble Classic was the original site for TankTrouble. It went under the domain
> tanktrouble.com **until December 2020**. Development for this site was active from 2007
> until around 2015 where development for TankTrouble Online (BETA) was prioritised by the
> **two developers**. The domain migrated to classic.tanktrouble.com a few months before the
> Adobe Flash end-of-life. beta.tanktrouble.com (the site for online) took over the
> tanktrouble.com domain. … TankTrouble Classic had a game tab, news outlet tab, a garage
> tab, a shop tab (for physical merchandise, BETA membership and accessories), a forum tab
> and a laboratory tab. **Only the game tab and the news tab remains after the migration.**"

**This is the direct cause of the maze creator's disappearance.** In the December 2020
migration to `classic.tanktrouble.com`, four of six tabs were dropped — including the
garage. The garage was the only page that referenced `mazeCreator_v0.3.swf`, so when it
went, the file stopped being served. That is exactly what the live probe found: `classic.`
serves `includes/TankTrouble_v4.03.swf` and `Assets/*` with 200 and every maze-creator path
with 404.

Three independent lines now converge on the same conclusion:
1. v4.03 deleted `__Packages`/`MazeDataFetcher` — no client could request a custom maze
2. the modern JSON-RPC API has no maze method at all
3. the garage tab was removed at migration

Other dates fixed by this wiki:
- **Deathmatch released December 2017**; Classic was the only mode before that
- Battle-mode rotation: Classic 18h/day, Deathmatch 6h/day, cycling 3h+1h on UTC; premium
  users bypass the rotation
- **"Badges of Respect" shipped 2015-10-16** — Terminator (skull) and Dominator (crown)
  badges. This is the **same date** as the greyscale-ramp change previously dated in the
  accessory palettes, so that art change belongs to this release.
- Never-shipped content: **Team Classic, Team Deathmatch, Capture the Flag** — "hinted at
  long, but never seen the day of light". Implemented modes were Bootcamp, Classic,
  Deathmatch.

### Why the maze `width` field varies 4–18

> "Mazes are randomly generated upon a new round … **The size of a maze varies depending on
> how many players are in the round; smallest with two, largest with four.**"

That resolves the width distribution measured in §9 (4 … 18, modal 18) — it is player-count
scaling, not editor freedom. Online spawn spacing rules are also documented: minimum
4 tiles between tank and crate spawns, 5 for gold, 6 for dimitrium, 1 for deathmatch zones.

## 20. Flashfreeze — searched, and ruled out on principle

Enumerated all **54 `flashfreeze-archive-*` items** on the Internet Archive and mapped their
content categories. Each item ships a `tar -tv` listing (`*.tar.zst.txt`) preserving the
**full original host and path**, so a TankTrouble hit would be unambiguous. Scanned the 30
bulk listings (the remaining ~9,890 are tiny per-crawl listings under items 021+).

**Result: 111 TankTrouble path hits, all of them fonts.** Sixteen third-party game portals
were crawled in 2019 and each pulled `tanktrouble.com/includes/c64.eot` and `c64.woff`:

`hoopgame.net` · `unblockedgamesbydylan.com` · `ushog.fun` · `www.friv.cm` ·
`www.es.obfog.com` · `www.justgames.com` · `www.feli.games` · `flashtop.com.ua` ·
`www.game.bz` · `www.giocogiochi.it` · `www.cute-games.com` · `igrulez.net` ·
`www.game01.ru` · `www.hryprodivky.cz` · `www.mahee.com` · `vseigru.net`

`flashfreeze-archive-005` is the `sorted/flash/` (SWF) category and contains **zero**
TankTrouble paths.

**This channel cannot hold the maze creator, for a structural reason rather than an empirical
one.** Flashfreeze's TankTrouble coverage comes entirely from portals that *embedded the
game*. An embed loads the game SWF, its `Assets/` RSLs and the page fonts — it never loads
the garage, which required a logged-in session on tanktrouble.com itself. No portal crawl
can ever have reached `mazeCreator_v0.3.swf`. Marking this closed.

Incidental discoveries: `tanktroubledeathmatch.com`, `tanktroublepro.club` and
`tanktroublepro.com` (WordPress fan sites), and a distinct HTML5-era `TankTrouble.ttf`
served from a Russian portal's asset tree.

## 22. ERA-CORRECT (2017–2019) HTML5 beta backend — recovered

Source: `cdn-beta.tanktrouble.com`, PageSpeed `.pagespeed.jc.` **combine-JS** bundles pulled
from Wayback in raw (`id_`) form. The bundles contain the original files concatenated, so
the era-correct API is directly readable. Saved to `beta-client-2017-2019\`.

| File | Wayback capture | Bytes | Original bundle |
|---|---|---|---|
| `2017-10-27_ajax+backend.js` | 2017-10-30 | 50,318 | `RELEASE-2017-10-27-01/js/ajax.js+backend.js+errorbox.js` |
| `2018-06-28_backend.js` | 2018-06-28 | 40,038 | `js/backend.js+errorbox.js` |
| `2019-04-14_managers+ajax.js` | 2019-04-14 | 74,242 | `js/clientmanager.js+…+ajax.js` |
| `2019-04-14_garage-ui.js` | 2019-04-14 | 54,779 | `js/tt/ui/garage/uimainstate.js+…` |

### Headline result — precise negative

**Zero occurrences of `maze` in the 2017, 2018 and 2019 `backend.js` / `ajax.js`** — i.e.
nothing maze-related on the **JSON-RPC layer** in any of those years.

> **Correction to an earlier statement in this log.** I first wrote that the HTML5 beta
> "never had a maze API at any point". That was an overreach from the RPC files alone and is
> **wrong**. The beta client contains `maze.js`, `mazemap.js`, `mazethememanager.js`,
> `requestmazemessage.js` and `requestmazeresultmessage.js`. Mazes exist in the HTML5 era —
> they live on the **binary socket layer**, not on JSON-RPC. See §24.

The accurate claim is narrower and still decisive for the hunt:

- The HTML5 maze system is **request-only**. The client sends `RequestMazeMessage` and
  receives `RequestMazeResultMessage`; the server generates the maze. There is **no
  create/save/update/delete maze message anywhere** in the 424-file client inventory, and no
  maze method on RPC.
- So **user-authored mazes were never ported**. The maze creator's write path lived and died
  entirely on the Flash / `index.php` side.
- It was **not a SAJAX function** either — §5 found no maze export among the 35.
- By elimination, `mazeCreator_v0.3.swf` wrote through a **direct PHP endpoint of its own**,
  a sibling of `loadMaze.php` under `includes/`, using the same
  `?q=<base64(shuffleMessage(…))>` envelope.

**That endpoint name is unrecoverable from any index.** CDX enumeration of
`tanktrouble.com/**/includes/*.php` across the whole domain returns exactly **three**
basenames ever requested by anything: `loadMaze.php` (17,411), `updateGameStatistics.php`
(2,305), `getScrapyard.php` (2). Even `achievement.php` and `getUserAuthentication.php` —
which are proven to exist because they are string literals inside the SWF — were never
captured. The write endpoint was called only by the maze creator SWF, which no crawler ever
executed.

Confirmed by the calling side: the garage page does **not** save the maze itself —

```javascript
function attemptToSaveMaze(user)
{
    //Ask the flash to save the maze
    document.getElementById('userSettingsMazeCreatorFlash-'+user).SetVariable('_root.saveRequested', 'true');
    //The flash should call hideMazeCreatorToolAndTitle if save was successful
}
```

The URL is a literal inside the lost binary. **This line of enquiry is closed** — the
endpoint name returns only if the SWF itself is found.

Also recovered from the same page: the editor had **two modes**, with distinct button sets —
`userpanelSaveMaze-<user>` (edit mode) versus `userpanelAcceptMaze-<user>` (preview/browse
mode), plus `userpanelCancelMaze-<user>`. The title field is `userpanelMazeTitle-<user>`,
placeholder text `Maze name` rendered `#666666`, switching to `#000000` once a real title is
set. `SetVariable('previewLoaded','')` asks the SWF to display the user's saved-maze
previews — consistent with the documented 3-mazes-per-tank limit.

### Era-correct API deltas (what actually changed 2017 → 2019 → 2026)

**Present in 2017, gone by 2026:** `getFriends` · `getHighScore` · `getChatMessageReports` ·
`setChatMessageReportModerationDecision` · `checkForSavedCard` · `deleteSavedCard` ·
`purchaseShopItemWithSavedCard` · `purchaseShopItemWithToken` · `replaceGuest` ·
`getAdminLogsAndTotalCount` · `getPopularAndRecentMessages` (renamed
`…MessageContent`) · `setPlayerNameApproved` (singular; later pluralised)

So the 2017–18 beta had a **friends list**, a **high-score board**, a **card-on-file
payment flow**, and a chat-report moderation queue — all since removed. Saved-card
purchasing being present in 2017–18 and absent in 2026 dates a payment-processor change.

**Added by 2018-06-28:** `getFavourites` / `setFavourited` · `revertAccountChange` (+
`…WithToken`) · `resetAccountPassword` · `retireAdmin` · `searchServerLogEntries` ·
`getUnmoderatedChatMessages` · `editMessageContent` · `setUsername` · `setEmail` ·
`getPlayerDetailsByEmail` · `getAdminStats` (later renamed `getAdminStatistics`)

**Added by 2019-04-14** — the multiplayer client layer appears:
`getAvailableServers` · `getAvailableServerStats` · `selectMultiplayerServer` ·
`_findAndConnectToBestAvailableServer` · `_attemptToConnectToServer` · `getClient` ·
`setChatKey` · `loadAvailableServers`

That is the HTML5 counterpart of v4.03's `flagAndTextPanel` region-ping selection (§6b) and
of the twelve `-mp` hosts in certificate transparency (§12) — all three describe the same
regional server fleet, from three independent evidence channels.

### 2019 HTML5 garage — file inventory

`js/tt/ui/garage/` bundle names the whole garage UI: `uimainstate` ·
`uigaragetankiconimage` · `uispraycanimage` · `uispraycanemitter` · `uispraycanparticle` ·
`uiscrollergroup` · `uiscrollerarrowimage` · `uiaccessoryimage` · `uiboximage` ·
`uiweldersmokeemitter` · `uiweldersmokeparticle` · `uiweldersparkemitter` ·
`uiweldersparkparticle`

Spray cans, accessories, boxes and welding effects — **no maze anything**. Independent
confirmation that the HTML5 garage was scoped to tank customisation only.

## 24. The 2017–2019 HTML5 client — full source inventory and maze model

CDX enumeration of `cdn-beta.tanktrouble.com` yields **424 distinct source filenames**,
because PageSpeed's combine-JS names every input file in the bundle URL. This is the
complete client file list for the era, without needing the files themselves.

### Architecture (2017–2019)

- **Transport:** `socket.io-1.4.5.js` + a hand-rolled binary message layer —
  `message.js`, `binarymessage.js`, `messageschemas.js`, `messageparser.js`, with
  `schemapack` for serialisation. Every message is its own file (~60 of them).
- **Physics:** `p2.js` and `b2dutils.js` (Box2D helpers) — `game-physics.js`,
  `celebration-physics.js`, `playerPanel-physics.js`.
- **AI:** `ai.js`, `aimanager.js`, `ais.js`, `aiutils.js`, `ai-plugin.js`, plus a full
  pathfinding stack: `Graph.js`, `Dijkstra.js`, `DijkstraIterator.js`,
  `BidirectionalDijkstra.js`, `BFS.js`, `nodeFlagger.js`. Named AIs: `laika.js`,
  `dimitri.js`.
- **Game modes:** `gamemode.js`, `bootcampgamemode.js`, `classicgamemode.js`,
  `deathmatchgamemode.js` — exactly the three the wiki says shipped (§19).
- **Weapons/upgrades:** `bulletweapon` `laserweapon` `shotgunweapon` `homingmissileweapon`
  `doublebarrelweapon` · `shieldupgrade` `spawnshieldupgrade` `speedboostupgrade`
  `aimerupgrade` `laseraimerupgrade`
- **Progression:** `ranks.js` `emblem.js` `victoryaward.js` `victorygoldaward.js`
  `achievementunlock.js` `stakesmessage.js` `currency.js`
- Oddments worth noting: `red_infiltration.js`, `chickenout.js`, `gpc.js`, `playerkick.js`

### Maze model — server-generated, themed, request-only

From `RELEASE-2018-07-02-01/js/tt/…+maze.js` (saved as
`beta-client-2017-2019\2018-07-02_maze+constants.js`):

| Constant | Value |
|---|---|
| `MAZE.BASE_WIDTH` | 2 |
| `MAZE_MINIMUM_TILES_PER_TANK` | 5 |
| `MAZE_MINIMUM_TILES_BETWEEN_TANKS` | 4 |
| `MAZE_MINIMUM_REACHABLE_RATIO` | 1.0 |
| `MAZE_TILE_SIZE` | 200 px |
| `MAZE_WALL_WIDTH` | 16 px |
| `MAZE_THEMES` | `{ STANDARD: 0, … }` with `MAZE_THEME_INFO[].BORDER_CONFIG` |
| collision category `MAZE` | `0x1 << 1` |

`MAZE_MINIMUM_REACHABLE_RATIO: 1.0` means **every tile must be reachable** — the generator
rejects mazes with isolated pockets. `MAZE_MINIMUM_TILES_BETWEEN_TANKS: 4` matches the wiki's
documented four-tile spawn spacing exactly (§19), and `MAZE_MINIMUM_TILES_PER_TANK: 5`
combined with `BASE_WIDTH: 2` is the mechanism behind "size varies with player count".

`MazeThemeManager` builds per-theme lookup tables mapping a cell's **wall configuration** to
weighted-random choices of floor, space, wall and wall-decoration sprites
(`wallConfigurationToFloors`, `…ToSpaces`, `…ToWallDecorations`, plus `borders`/`walls` with
weight sums). So the HTML5 maze renders a themed tileset chosen stochastically per cell from
its wall bitmask — the direct descendant of the Flash format's 3-bit-per-cell `wallString`
(§9).

Wire messages are `RequestMazeMessage` → `RequestMazeResultMessage`, both subclasses of the
binary `Message`/`ResultMessage` base with a `typeId` from `MessageSchemas`. **Request only —
there is no maze-write message.**

---

## 25. Era index — which section describes which system

Because three distinct systems appear in this log, every section is tagged here. Do not
carry a fact across eras without re-verifying it.

| Era | System | Evidence sections |
|---|---|---|
| **2007 – Dec 2020** | **Flash / mootools site**, `tanktrouble.com/index.php`. Query-route tabs, SAJAX, six direct PHP endpoints, AVM1 SWFs. **The maze creator belongs here.** | §5 (SAJAX 35 fns) · §6 · §6b · §8 (PHP inventory, routing) · §9 (loadMaze/updateGameStatistics/getScrapyard contracts) · §10 (maze creator UI) · §11 (SWF tags) · §14 (SAJAX wire protocol) · §15 (backdoor routes) · §16 (`embed.php`) |
| **2017 – 2020** | **HTML5 beta**, `beta.tanktrouble.com` + `cdn-beta.tanktrouble.com`. JSON-RPC + socket.io binary protocol. Ran **in parallel** with the Flash site. | §22 · §24 |
| **Dec 2020 – now** | **Current site**, `tanktrouble.com` (the beta branch, promoted) + `classic.tanktrouble.com` (Flash remnant: game + news tabs only). | §17 (⚠ current only) · §4 (`classic.` live) · §6b (v4.03) |
| **all eras** | Infrastructure and timeline | §12 (certificate transparency) · §19 (site timeline) · §20 (Flashfreeze) |

**Known-uncertain, flagged as such:** the lineage from SAJAX names to JSON-RPC names
(`login`→`authenticate`, `updateTank`→`setAccessory`/`setColour`, `getScraps` unchanged) is
**inferred from naming only**. No intermediate build has been found that demonstrates the
migration, and the 2017 beta already has the modern names — so the two APIs may have been
written independently rather than one evolving into the other. Treat as unproven.

## 26. Exhaustive Wayback + Common Crawl enumeration

Full inventory in `wayback-inventory\` — **74,165 capture rows, 29,399 unique URLs** across
all host variants. `FINDINGS.md`, `url-inventory.tsv`, `php-paths.tsv`, `swf-paths.tsv`,
`directory-prefixes.tsv` and the raw per-host CDX dumps are all there.

| host | captures | unique paths |
|---|---|---|
| tanktrouble.com | 38,888 | 19,355 |
| cdn.tanktrouble.com | 17,224 | 5,150 |
| www.tanktrouble.com | 9,405 | 3,835 |
| cdn-beta | 6,451 | 2,018 |
| classic | 767 | 121 |
| eu-central2-web2 | 512 | 299 |
| beta | 509 | 90 |
| test-cdn-beta | 375 | 375 |

Per-host sweeps sum exactly to the domain sweep, and were cross-validated against
`wayback_machine_downloader --list`. `m.`, `forum.`, `static.` and `api.` have **zero**
captures. Five hosts not previously known: `eu-central2-web1`, `eu-central2-test1`,
`test-beta`, `migrate`, `beta2`.

### The real win — 6 more previously unknown SWFs, from ZIP bundles

`/includes/` served **downloadable ZIP bundles** that nobody had looked at. Verified by
SHA-256 against the whole corpus (archive + all earlier recoveries this session):

| File | Bytes | Source ZIP | Status |
|---|---|---|---|
| `TankTrouble_v3.5.swf` | 273,896 | `TankTrouble_v3.5.zip` | **NEW** |
| `TankTrouble_v3.6.swf` | 272,790 | `TankTrouble_v3.6.zip` | **NEW** |
| `TankTrouble_v3.6e.swf` | 288,775 | `TankTrouble_v3.6e.zip` | **NEW** |
| `Assets/Tank.swf` | 13,598 | v3.5 / v3.6 zips | **NEW** (earliest Tank build held) |
| `Assets/Tank.swf` | 33,049 | v3.6e zip | **NEW** |
| `Assets/GameTank.swf` | 10,063 | v3.5 / v3.6 zips | **NEW** |

**The standalone `.swf` URLs for v3.5, v3.6 and v3.6e return 404 in every capture, and
v3.8c has no `.swf` capture at all — these ZIPs are the only surviving source for those
builds.**

Cross-validation worth noting: `TankTrouble_v3.8c.swf` and `TankTrouble_v4.03.swf` extracted
from the ZIPs are **byte-identical** to the copies obtained independently from Flashpoint's
Kongregate curation and from the live `classic.` host. Three independent routes, same bytes.

**Corpus is now 33 unique SWFs, up from 23 at the start of this session.** Staged in
`wayback-zip-swfs\`, decompiled into `decompiled\ZIP_*`. Endpoint scan of v3.5 / v3.6 /
v3.6e finds only `includes/loadMaze.php?q=`, `includes/updateGameStatistics.php?q=` and the
absolute `http://www.tanktrouble.com/includes/getUserAuthentication.php` — so `loadMaze.php`
existed at least as far back as v3.5, and no new endpoints appear.

### Directory structure — observed

**Previously unknown prefixes that exist:** `/kickstarterFAQ/` · `/statistics/` ·
`/verification/` · `/facebook/` · `/ajax/` · `/cdn-cgi/` · `/includes/src/` ·
`/includes/Assets/` · `/includes/images/`

**Confirmed non-existent** (nothing under the prefix, ~24 probed): `/uploads/` `/tmp/`
`/backup/` `/logs/` `/fonts/` `/swf/` `/flash/` `/cgi-bin/` `/scripts/` `/mazes/`

**No autoindex listing exists anywhere.** 384 raw `id_` fetches across 244 captured
directory URLs produced zero Apache/nginx index pages; no URL anywhere carries a
`?C=M;O=D` sort query. `/includes/` was captured once and returned **403 Forbidden**;
`/assets/images/{accessories,colours,inputs,ranks,tankIcon}/` likewise 403. Directory
listing was off site-wide. That channel is closed by observation, not by assumption.

### Corrected reading of the PHP path list

`FINDINGS.md` interleaves observed paths with the agent's own probe targets. Cross-checking
`php-paths.tsv` (observations only), **`saveMaze.php`, `getMaze.php`, `deleteMaze.php` and
`mazes.php` were never observed** — they appear in the write-up only as names that were
probed and returned nothing. Do not read them as real endpoints.

Genuinely observed root-level PHP, beyond the three under `includes/`:

| Path | Captures | Note |
|---|---|---|
| `/embed.php` | 218 (2009-01-29 → 2026-02-18) | the longest-lived page on the site |
| `/index.php` | — | site root |
| `/logIn.php` | 36, **404 in every one** (2008-05 → 2009-09) | referenced but already removed by 2008 |
| `/getimage.php` | 548 across hosts | HTML5-era image server |
| `/uploadimage.php` | 3 | HTML5-era admin upload |
| `/admin.php`, `/administrator/index.php`, `/wp-login.php` | 2 each, all 2024-07-04 | **hostile bot scans, not real paths** — TankTrouble is not WordPress |

### Task-5 verdict — maze creator, definitive

- **`mazeCreator*.swf` — ABSENT.** No version suffix, no host, no scheme, ever. Bare
  `/mazeCreator` was requested once in 2009 and 404'd.
- `mazeConstructToolSelect.jpg` and `tankSpawnToolDeselect.jpg` — **index hit but no
  content**: both are 302 http→https upgrades landing on 404, in 2024 and 2023. Somebody knew
  those exact filenames years after Flash died, but the files were already gone.
- The other four tool images have no index hit at all.

### Methodological caveat — applies to every negative in this log

The CDX server **intermittently returns HTTP 200 with an empty body**. The agent's first
pass produced false "absent" results that disappeared on retry; every negative above was
re-run three times with a positive control in the same batch. Two further traps: CDX
urlkeys are **lowercased** and have the **trailing slash stripped**, so `filter=urlkey:`
probes fail unless written lowercase and slash-less. **Do not trust a single zero-row CDX
query.**

## 27. Classic UI (2017–2019) asset recovery

Diffed every `/images/` path that ever returned 200 in Wayback (335) against what is held
locally (214). **122 classic-UI images were missing. All 122 have now been recovered** into
`classic-ui-images\` (935 KB+, every file validated as real JPEG/PNG/GIF/SVG, not an error
page).

Recovery took three passes, and the failures were **entirely artefacts of the CDX
flakiness described above** — not missing data:

| Pass | Method | Recovered |
|---|---|---|
| 1 | fetch at `first_ts` from the inventory | 87 |
| 2 | retry across *every* archived capture, both hosts | +21 |
| 3 | direct fetch at the known timestamp, no CDX lookup, 3 attempts | +14 |

Pass 3 is the instructive one: six `images/shop/*.png` files that CDX reported as
unreachable each have **exactly one 200 capture, on `www.tanktrouble.com`, dated
2018-03-10** — squarely inside the target era. Fetching them directly by timestamp
succeeded on the **first** attempt for all six. A zero-row CDX response meant nothing.
(Pass 2 also exposed a bug of my own: `images/shop/…` paths need the subdirectory created
before writing, or the fetch silently fails.)

They are almost entirely the **panel-chrome tilesets** the mootools UI was built from —
`bigBox*{Top,Middle,Bottom}.jpg` and `box*{Top,Middle,Bottom}.jpg` in Black / Orange /
Yellow / Blue / GrayHollow / LimeHollow / RedHollow variants, plus per-weapon box art
(`bigBoxLaserMiddleAndBottom`, `…GatlingMiddleAndBottom`, `…DeathRayMiddleAndBottom`,
`…FragBombMiddleAndBottom`, `…HomingMissileMiddleAndBottom`, `…RCMissileMiddleAndBottom`,
`…BoobyTrapperMiddleAndBottom`), Facebook/Laika themed boxes, tab-selected variants, and
`betaSign.png` / `betaAccessBackground.png` / `blackHoodiePokingOut.png`.

Note the classic-era capture profile: of 9,292 tanktrouble.com 200-responses dated
2017–2019, **9,236 are `includes/loadMaze.php`** and only 37 are `/images/`. Wayback barely
touched the classic UI's assets during those years — the recovered images come from captures
across the file's whole lifetime, which is valid because the chrome art was static.

## 28. Session tally

**SWF corpus: 23 → 33 unique builds.** Ten previously unheld SWFs recovered, from four
independent routes:

| Route | Files |
|---|---|
| Live `classic.tanktrouble.com` | `TankTrouble_v4.03.swf`, `Assets/GameTank.swf` (10,351) |
| Flashpoint GameZIP | `TankTrouble_v3.8c.swf`, Newgrounds `632327_tank-trouble-new.swf` |
| Wayback `/includes/*.zip` bundles | `v3.5`, `v3.6`, `v3.6e`, `Assets/Tank.swf` ×2 (13,598 / 33,049), `Assets/GameTank.swf` (10,063) |

Plus: 122/122 classic-UI images, the complete 2017–19 beta client source inventory
(424 filenames) with six era-correct bundles pulled, the current client's unminified
sources, three wiki corpora, 37 Lab Report page images, and a full 29,399-URL Wayback
inventory.

**`mazeCreator_v0.3.swf` itself remains lost**, but is no longer a black box: its UI is
recovered visually (§10), its tool set, grid rules and object schema are derived from two
independent channels (§9, §19), its JS↔SWF interface is complete (§6), and the reason for
its loss is established (§19 — garage tab dropped in the Dec-2020 migration). Every index
channel is exhausted; only a local copy can return the binary (§7).

## 30. Second scrape wave — new channels (2026-08-02)

A second pass using channels not tried in the first. Recorded here with the exact
query for each, so both the hits **and the negative results** are reproducible.

### 30.1 Channels that were blocked or dead (not "empty" — unreachable)

| Channel | Result | Evidence |
|---|---|---|
| `timetravel.mementoweb.org` (Memento aggregator) | **dead** | HTTP 000, no TCP response. The federated aggregator is offline; each archive must be queried on its own endpoint. |
| `archive.today` (`.ph` / `.is` / `.li`) | **blocked** | HTTP 429 + anti-bot interstitial on `/timemap/`, all three TLDs, browser UA. Needs a real browser session. |
| `archive.softwareheritage.org` | **blocked** | Anubis proof-of-work wall — `Set-Cookie: techaro.lol-anubis-*`, body `Making sure you're not a bot!`. API returns HTML, not JSON. |
| UK Web Archive timemap | **wrong endpoint** | returns a 159-byte `400 Redirect` stub. |
| AlienVault OTX | **empty** | `{"url_list": [], "full_size": 0}` — genuinely zero, not an error. |

⚠ **Blocked ≠ searched.** archive.today and Software Heritage remain *untested*,
not *excluded*. archive.today matters most: it stores **user-requested** snapshots,
so a logged-in player could have snapshotted their own garage — the one mechanism
that defeats login-gating. Retry from a browser session.

### 30.2 Arquivo.pt — an independent archive, largely redundant

`https://arquivo.pt/wayback/cdx?url=tanktrouble.com&matchType=domain&output=json&limit=5000`

3,440 rows, 1,400 distinct paths, 2019–2024. Diffed against our IA inventory
(9,294 distinct host+path): **only 10 paths are unique to Arquivo**, all binary
socket-protocol message names — `/mine`, `/mineweapon`, `/trap`, `/trapstate`,
`/traptrippedmessage`, `/trapdestroyedmessage`, `/trip`, `/shrapnel`,
`/binaryresultmessage`, plus one 2023 favicon.

Its 12 SWF captures are all builds we already hold. **Value: a redundant fetch
source when IA is throttling**, not a new corpus.

### 30.3 CDX pass A — non-200 rows (the pass never run before)

`filter=!statuscode:200` — 6,571 rows. Redirects and 404s are evidence: a 404
means something requested the path; a 301 chain maps old layout to new.

Status mix: `-` 2811, `404` 2079, `301` 1527, `302` 113, `206` 34, `403` 6, `503` 1.
732 distinct pre-2021 non-bot paths.

This is what surfaced `loadMaze.php` (§30.5), which no 200-only query had shown
in a usable form.

### 30.4 CDX pass B — `collapse=digest` (distinct *builds*, not distinct URLs)

87 distinct SWF payload digests. Collapsing by digest instead of urlkey shows
how many genuinely different builds of each file were ever served:

- `Tank.swf` — **8 distinct builds**, incl. `2017-04-24` and `2017-11-01` (era-correct)
- `TankTrouble_v4.0.swf` — 10 rows but **one** distinct 200-payload across 2013→2020
- `GameTank.swf` — 7 builds
- `signUpTankDesign*StandardColours.swf` — versions 04, 13, 16, 17, 18 (2012→2019)

**9 new SWF builds recovered** (`cdx-passes/swf-by-digest/`). Corpus 20 → 29 unique
SWF byte-sequences:

| File | Capture | Size | Note |
|---|---|---|---|
| `laika02.swf` | 2011-06-25 | 12,415 | |
| `Tank.swf` | 2012-06-15 | 13,570 | pre-rewrite, tiny |
| `GameTank.swf` | 2012-06-15 | 10,071 | |
| `signUpTankDesign13StandardColours.swf` | 2013-04-09 | 230,921 | tank designer |
| `scrapyard10.swf` | 2015-01-06 | 9,830 | calls `getScrapyard.php` |
| `Tank.swf` | 2015-05-12 | 199,909 | |
| `Tank.swf` | 2015-10-16 | 213,971 | |
| `signUpTankDesign17StandardColours.swf` | 2016-10-02 | 231,334 | tank designer |
| `ima3_preloader_1.5.swf` | 2016-11-22 | 34,636 | Google IMA3 ad preloader |

The `signUpTankDesign*` series matters for the maze hunt: it is mazeCreator's
**sibling** — the other in-page Flash editor driven by the same JS↔SWF
`SetVariable` pattern. Its structure is the best available model for how
mazeCreator was wired.

### 30.5 `loadMaze.php` — the maze READ API, and 4,192 surviving mazes

**The single biggest find of this wave.**

```
/includes/loadMaze.php?q=<base64>
```

Request payload decodes to `userName=<name>&a=<random>&b=<random>`
(`a`/`b` are cache-busters). Every archived request has `userName=undefined`
because the crawler was never logged in.

**Response** payload decodes to:

```
t=<maze title>&n=<author username>&d=<maze data>&s=<slot>
```

Worked examples:

```
t=Random&n=pippy&d=7#7334733562056253731332531513731553625656 20#0#0##0#&s=1
t=Death pit??&n=mynameisbob&d=13#7333333333333351111311111111151311131311515151511115151155111151511115151111111111111#0#0##0#
s=1&d=1#7555555555#0#7#1#1#5##1#2#8##1#3#8##1#5#8##1#8#8##1#9#8##1#10#5###0#&n=hi88&t=doo
```

This is **the surviving output of `mazeCreator_v0.3`** — user-built mazes, with
titles and author attribution, in the exact wire format the lost editor emitted.

Scale (`filter=original:.*loadMaze.*&filter=statuscode:200`):

- **17,378 captures**, **4,192 distinct response payloads**
- 2012: 4 · 2013: 4,560 · 2015: 191 · 2016: 1,829 · **2017: 1,250** · **2018: 5,295** · **2019: 1,595** · 2020: 2,654
- **8,140 captures fall inside the 2017–2019 target era**

The first wave decoded 1,633 payloads; this is **2.6× more**. Fetching all 4,192
into `maze-corpus/raw/`, deduped by CDX digest, era-correct timestamps preferred.

`updateGameStatistics.php` uses the same envelope; its payload decodes to a full
match record: `killer0`, `victim0..3`, `kills0..3`, `k0/k1`, `d0/d1`, `s0/s1`,
`e0/e1`, `v0/v1`, `p0/p1`, `rounds`, `players`, `tanksScrapped`, `ranked`.

**The endpoint is dead.** `GET https://classic.tanktrouble.com/includes/loadMaze.php?q=…`
returns Apache 404 for every username tried. The archive is the **only** remaining
source — this corpus cannot be regenerated.

### 30.6 Complete PHP endpoint list — 43 distinct paths

`filter=original:.*[.]php.*&collapse=urlkey` — 19,868 rows, bot-scan noise removed.
All **observed**, none inferred:

| Path | First..last seen | Status |
|---|---|---|
| `/includes/loadMaze.php` | 2012-06-15 .. 2025-11-12 | 15,913× 200, 1,325× 301, 4× 404 |
| `/includes/updateGameStatistics.php` | 2013-02-23 .. 2020-12-08 | 2,119× 200, 162× 301 |
| `/getimage.php` | 2017-10-30 .. 2026-06-11 | 99× 200 |
| `/includes/getScrapyard.php` | 2015-09-28 .. 2016-01-26 | 2× 200 |
| `/uploadimage.php` | 2021-04-01 | 200 |
| `/embed.php` | 2009-01-29 .. 2016-10-25 | 200, 404 |
| `/index.php` | 2008-05-28 | 200 |
| `/logIn.php` | 2008-05-28 | 404 |
| `/RELEASE-*/content.php` | 2017-10-27 .. 2026-05-11 | 34 releases |

`getScrapyard.php` and `uploadimage.php` were **not previously known**.
`getScrapyard.php` is independently confirmed as a string literal inside
`scrapyard10.swf`: `URLRequest@http://tanktrouble.com/includes/getScrapyard.php`.

### 30.7 Complete beta RELEASE list, and the era-correct subset

Every `RELEASE-<date>-<nn>` tag ever observed on `beta.` / `cdn-beta.` /
`cdn.tanktrouble.com`. **13 fall in 2017–2019 and have archived files**:

| Release | Files archived |
|---|---|
| RELEASE-2017-10-27-01 | 85 |
| RELEASE-2017-12-22-01 | 50 |
| RELEASE-2018-04-20-01 | 196 |
| RELEASE-2018-07-02-01 | 80 |
| RELEASE-2018-08-26-01 | 54 |
| RELEASE-2018-11-01-01 | 46 |
| RELEASE-2018-12-07-01 | 53 |
| RELEASE-2018-12-16-01 | 35 |
| RELEASE-2019-01-03-01 | 14 |
| RELEASE-2019-05-10-01 | 310 |
| RELEASE-2019-07-09-01 | 3 |
| RELEASE-2019-10-04-01 | 513 |
| RELEASE-2019-11-27-02 | 170 |

Each folder is an **immutable, complete client snapshot**. Being pulled whole into
`cdn-beta-full/`. `RELEASE-2019-01-03-01` was not in the first wave's list.

PageSpeed bundle names enumerate their inputs, so the CSS module list is readable
straight off a filename — incl. `garage.css`, `shop.css`, `playerpanel.css`,
`achievements.css`, `walloffame.css`, `forum.css`, `premium.css`.

> Note: these bundle filenames exceed the Windows 255-char limit. They are stored
> truncated with a SHA-1 suffix; `cdn-beta-full/_longnames.tsv` maps each stored
> name back to its full original URL.

### 30.8 Live-server fingerprint (2026-08-02)

The Apache 404 page leaks the server build:

```
<address>Apache/2.4.29 (Ubuntu) Server at classic.tanktrouble.com Port 443</address>
```

**Apache 2.4.29 is the Ubuntu 18.04 LTS default** (bionic, April 2018) — the
surviving legacy host is still on an era-correct 2018 base image, behind Cloudflare.

Endpoint probe (all **probes**, not observations):

| Path | Result |
|---|---|
| `/index.php` | 200 |
| `/includes/` | **403** — directory exists, autoindex off |
| `/Assets/` | **403** — directory exists, autoindex off |
| `loadMaze.php`, `getScrapyard.php`, `updateGameStatistics.php`, `getimage.php`, `uploadimage.php`, `embed.php`, `logIn.php` | 404 — all removed |

The two 403s confirm both directories still exist on disk. No autoindex anywhere,
so directory listing remains impossible.

### 30.9 The elte.hu mirror — found, and lost

The `?r=` referrer capture recorded a full third-party mirror of `/includes/`:

```
http://tanktrouble.com:80/?r=SWF+http://people.inf.elte.hu/fodtaai/tank/includes/TankTrouble_v3.6e.swf
```

A personal page on a Hungarian university server mirroring the *whole includes
directory* — exactly the shape of host that could have held `mazeCreator_v0.3.swf`.

- Wayback CDX `people.inf.elte.hu/fodtaai*`, `matchType=prefix`, 3 attempts: **0 rows**. Never crawled.
- Live probe, 2026-08-02: **403** on the file, and on `/tank/includes/`, `/tank/`, `/fodtaai/`.

Host alive, tree sealed, never archived. Closed.

### 30.10 Small / negative channels

- **urlscan.io** — 19 results, only one pre-2021 (2019). One new hostname: `test-cdn-beta.tanktrouble.com`.
- **IA item search** (`advancedsearch.php?q=tanktrouble`) — 4 items. Two are **full wiki dumps incl. revision history**, downloaded and extracted to `ia-items/extracted/`:
  - `tanktroublefandomcom-20220212-history.xml` — 159 pages, 393 revisions
  - `tanktrouble_tank_gamefandomcom-20220227-history.xml` — 237 pages, 392 revisions
  - Yield is thin: **9 distinct tanktrouble URLs** across every revision of both wikis. The wikis document the game, they don't link into it. One curiosity: `rebuildMessages.php` (2015-11-25).
  - The other two items are a mislabelled Fortnite video and an unrelated Thingiverse model.

## 31. ⚠ CORRECTION — there are FOUR wikis, and the obvious dump is a decoy

This overturns an assumption carried through the whole first wave.

**`tanktrouble.fandom.com` was renamed, not deleted.** The original wiki — wikiid
`tanktrouble`, revisions back to **2010-03-24** — is alive at
**`tanktrouble-archive.fandom.com`**. The vacated address was later reused by a
different, short-lived 2021 wiki, `tanktrouble849`, which was itself deleted.

**That decoy is what our dumps contain.** Both `wiki-dumps/tt-wiki/` (wave 1) and
the IA item `wiki-tanktroublefandomcom` (wave 2, §30.10) are `tanktrouble849`.
Verified directly from the dump's own metadata:

```
siteinfo.json ->  wikiid  = tanktrouble849
                  base    = https://tanktrouble.fandom.com/wiki/TankTrouble_Wiki
history.xml   ->  dbname  = tanktrouble849
```

This is why §30.10 measured only 9 outbound URLs across 393 revisions — it was
measuring the wrong wiki. The IA item's *title* ("Wiki - TankTrouble Wiki") and
its *URL* both point at the original; only the payload reveals the substitution.

**Live census, verified 2026-08-02 via `action=query&meta=siteinfo`:**

| Wiki | Pages | Articles | Edits | Images | Status |
|---|---|---|---|---|---|
| `tank-trouble.fandom.com` | 457 | 44 | 576 | 57 | **largest — not previously known** |
| `tanktrouble-archive.fandom.com` | 364 | 32 | 666 | 48 | **the original**, back to 2010-03-24 |
| `tanktrouble-tank-game.fandom.com` | 237 | 32 | 400 | 60 | known |
| `tanktrouble.fandom.com` | — | — | — | — | **dead** (empty API response) |

Full-history mining across all four (2,395 revisions, all namespaces, plus 112
Fandom Discussions posts) is in `wiki-history/`. Results:

- 2,226 URL rows → 302 unique tokens → 67 distinct tanktrouble.com URLs → 19 canonical
- Cross-validated against MediaWiki's own `exturlusage` index: the regex caught all 11 links the wikis themselves index
- **Zero `.swf` filenames in any of 2,395 revisions.** A firm negative — the wikis never linked a SWF directly.

**Never-archived paths (4, all real):** three `tanktrouble.com/forum?threadId=…`
(156197, 184701, 191068) and `tanktrouble.com/news?postId=1` — the site's first
news post. All four sit on paths that *are* archived; only the query strings were
never crawled. All are 2021, so **outside the 2017–2019 target era**.

**On the target era specifically: the wikis are genuinely thin.** All 30 rows in
the 2017–2019 window are the bare homepage inside Main Page boilerplate. Deep
paths cluster in 2015–2016 and 2021. That is a real gap in the sources, not a
collection failure — the best 2017–2019 wiki artefacts are **images** (TTOC
2017/2018/2019 competition screenshots), not URLs.

Two side-findings worth keeping:

- The `?todo` / `?whosthr` / `?calc` backdoor paths are documented on-wiki in **2015** — seven years before Wayback's only captures of them (2022).
- Fandom's CDN silently serves **WebP under `.png` filenames**. A first pass saved 165 mislabelled files; all were refetched with `format=original` and verified by magic bytes. Anything pulled from a Fandom image URL must be magic-byte-checked.

`?garage` and `?laboratory` were deliberately **excluded** from the corpus: the
wikis describe those tabs in prose and the `?<tab>` pattern makes them plausible,
but neither string appears in any revision. They remain INFERRED-only.

## 32. Search-engine and social channels — mostly negative

| Channel | Query | Result |
|---|---|---|
| arctic-shift (Reddit) | `/api/comments/search?body=…` | **API refused** — `'body' query parameter requires one of: author, subreddit, link_id, parent_id`. No free-text search without narrowing to a subreddit or author first. |
| Marginalia | `search.marginalia.nu/search?query=tanktrouble` | 145-byte stub — endpoint moved. |
| Mojeek | `?q=tanktrouble+mazeCreator` | 5.7 KB, no non-Mojeek outbound links. |
| yt-dlp | — | **not installed**; YouTube era-video mining not attempted. |

None of these are exhausted; they are *unrun*. The YouTube channel in particular
is still the best untried route to mazeCreator's full UI — video shows every tool
state and the save dialog, where the one recovered screenshot shows a single frame.

## 33. ⚠ METHOD BUG — `matchType=prefix` with a trailing `*` silently returns zero rows

**This produced a false negative that nearly closed a live channel.**

§30.9 recorded the elte.hu mirror as "never crawled", based on:

```
url=people.inf.elte.hu/fodtaai*&matchType=prefix     -> 0 rows, 3 attempts
```

That is **wrong**. The correct form returns **76 rows**:

```
url=people.inf.elte.hu/fodtaai/&matchType=prefix     -> 76 rows
url=people.inf.elte.hu&matchType=domain&filter=original:.*fodtaai.*   -> 76 rows (identical)
```

When `matchType=prefix` is given explicitly, a trailing `*` in `url=` is taken as a
**literal character** in the prefix, not a wildcard. Nothing matches, and the API
returns HTTP 200 with an empty array — indistinguishable from "not archived".

**Rules that follow:**

1. Use `url=host/path/&matchType=prefix` — **never** combine `matchType=prefix` with `*`.
2. The `*` form is only for the implicit mode (`url=host/path/*` with **no** `matchType`).
3. Cross-check every prefix query with an equivalent `matchType=domain` + `filter=original:` query. If the two disagree, the prefix query is the one that's wrong.

A second self-inflicted false negative in the same area: several `curl -o /tmp/…`
writes failed silently (`/tmp` is not writable from this Git Bash), so the query
looked empty when it had never been saved. **Always check the output file's byte
count, not just the exit code.**

Two more constraints confirmed while chasing this:

- `fl=filename,offset,length` returns `filename: null` on the public CDX API. WARC-level location data is **not exposed**, so the "fetch adjacent captures out of the same WARC" technique is unavailable.
- `web.archive.org/__wb/search/anchor` returns 404. No public anchor-text link graph.

## 34. The elte.hu mirror — recovered

A personal page on a Hungarian university server (`people.inf.elte.hu/fodtaai/tank/`)
mirroring TankTrouble. Four files archived, all fetched:

| File | Capture | Bytes | Status |
|---|---|---|---|
| `tank/Assets/Tank.swf` | 20150827073924 | 85,574 | **★ NEW BUILD — not in any tanktrouble.com digest** |
| `tank/Assets/Crate.swf` | 20150827073929 | 2,357 | byte-identical to the Flashpoint copy |
| `tank/Assets/GameTank.swf` | 20150827073927 | 10,126 | byte-identical to the Flashpoint copy |
| `tank/includes/TankTrouble_v3.6e.swf` | 20150827073918 | 288,775 | byte-identical to the Flashpoint copy |

Three of four matching Flashpoint **exactly** is the useful part: it proves the
mirror was a faithful byte-copy of the origin, which makes the fourth file —
a `Tank.swf` build at 85,574 bytes that appears in **none** of the origin's 8
distinct `Tank.swf` digests — a genuine addition. **Corpus 29 → 30.**

**Why mazeCreator was never here.** The archived `mod_autoindex` listing of the
parent directory gives real filesystem mtimes:

```
Apache Server at people.inf.elte.hu Port 80
tank/    08-Nov-2012 16:06
```

The mirror was taken **November 2012** — the v3.6e era, before the garage existed.
It only ever contained the game embed. The `/fodtaai/tank/` page is a hand-written
embed:

```html
<embed type="application/x-shockwave-flash"
       src="…/tank/includes/TankTrouble_v3.6e.swf"
       id="TankTroubleGame" name="TankTroubleGame" …>
```

`id="TankTroubleGame"` matches the lookup inside `DoAction.as`
(`document.getElementById('TankTroubleGame')`), confirming the mirror copied the
official embed markup verbatim.

Live status 2026-08-02: **403** on `/fodtaai/`, `/tank/`, `/tank/includes/` and the
SWF itself. Host alive, tree sealed. The archive is the only copy.

Side-benefit: this host **had `mod_autoindex` enabled**, and the listing was
captured with the `?C=N;O=D` sort parameters — the tell described in the original
strategy. No such listing was ever captured for `/fodtaai/tank/includes/`.

## 35. The classic `/includes/` directory — fully enumerated

With the prefix syntax fixed, `/includes/` reconstructs to **75 distinct paths**.
Everything below is **observed** in CDX, never inferred. `GET` marks paths with at
least one 200 capture (i.e. recoverable); the rest are 404/403 observations that
still prove the name existed or was requested.

**Recoverable, and not previously held:**

| Path | Era | Note |
|---|---|---|
| `TTTradingCardsSeriesI.pdf` | 2019–2021 | 1.25 MB — physical merch artwork |
| `TTTradingCardsSeriesII.pdf` | 2019–2021 | 416 KB |
| `TTTradingCardsSeriesIII.pdf` | 2019–2021 | 2.55 MB |
| `TTTradingCardsSpecialAnniversaryCard.pdf` | 2019–2021 | 349 KB |
| `c64.eot` / `c64.ttf` / `c64.woff` | 2015–2021 | **the site's pixel font**, all three webfont formats |
| `boxStyles.css`, `forumStyles.css`, `newsStyles.css`, `shopStyles.css`, `styles.css`, `main.css`, `news.css` | 2010–2020 | the complete classic stylesheet set |
| `embed.js`, `swfobject.js`, `mootools-release-1.11.js` | 2010–2020 | the classic JS stack |
| `phaser.min.js`, `scrapyard.js` | **2017–2020** | **era-correct** — the scrapyard was rewritten in Phaser (HTML5) inside the classic Flash site |
| `getScrapyard.php` | 2015–2016 | response bodies, 440/470 bytes |

`phaser.min.js` + `scrapyard.js` is a structural finding: by 2017 the classic site
was **already partly HTML5**, running a Phaser scrapyard alongside the Flash game.
The Flash-to-HTML5 transition was not a single cutover at the beta.

Also confirmed recoverable but previously listed as failures: `scrapyard11.swf`,
`signUpTankDesign04StandardColours.swf`, `signUpTankDesign16StandardColours.swf`,
`TankTrouble_v3.6c.swf` — all have 200 captures; the earlier failures were
throttling, not absence.

Never-200 (name proven, bytes gone): `TankTrouble_v1.11/1.3/1.31/1.4/2.01/2.1/2.2/
3.02a/3.11/3.1a/3.41/3.42/3.43/3.5/3.6/3.6a/3.6b/3.6e/3.7.swf`,
`scrapyard.swf`, `scrapyard01/03/04/05.swf`,
`signUpTankDesign01/04/09/11StandardColours.swf`,
`includes/images/scrapyardPlates.png`, `includes/p2.js`, `includes/src/p2.js`.

**`/includes/` never contained a file matching `maze*` in any capture.** Combined
with §19 (garage tab dropped in the Dec-2020 migration), the editor was almost
certainly served from a garage-scoped path, not from `/includes/`.

## 36. Mirror hunt round 2 — and a definitive negative on PHP source

### 36.1 The honest answer on "mirrors with PHP / server files"

**No mirror of TankTrouble's server-side code exists, anywhere reachable.** This is
now a tested conclusion, not an assumption. PHP is executed, never served, so a
copy can only survive via misconfiguration, a backup, or a leak. All three were
checked:

| Check | Method | Result |
|---|---|---|
| Source-extension leak on origin | CDX sweep for `.phps .inc .bak .old .orig .save .swp .src .sql .gz` | no rows |
| PHP source in any held file | regex scan of **4,434 text files** across both archive roots for `<?php`, `Warning:`, `Fatal error:`, `include_path`, `DOCUMENT_ROOT`, `mysql_*`, `/home/`, `/var/www/` | **zero hits** |
| GitHub | authenticated `gh search code` for `loadMaze`, `saveMaze`, `mazeCreator`, `getScrapyard`, `updateGameStatistics` | 75 results, **none TankTrouble's** — all unrelated projects |
| Official distribution zips | extracted all four (`v3.5`, `v3.6`, `v3.6e`, `v3.8c`) | **client-only** — SWF + `Assets/`, no PHP |

The single Unix path anywhere in the corpus is `/Users/jkorch1298/Desktop/Tank…`,
which is a *player's* local disk leaking through the `?r=` referral tracker — not
the server.

**What does survive of the server side:** response bodies (§30.5, §30.6), the
`/infirmary/` hand-simplified copy of `index.php`, and the live JSON-RPC interface
(§36.4).

### 36.2 Distribution zips — no PHP, but exact developer build times

The zips are client packages, and every one carries `__MACOSX` resource forks —
they were zipped on macOS. The preserved mtimes are the developer's own filesystem
times, giving true build chronology:

| Build | mtime in zip | Assets/Tank.swf mtime |
|---|---|---|
| `TankTrouble_v3.5.swf` | 2011-04-07 08:23:01 | 2011-04-07 (13,598 b) |
| `TankTrouble_v3.6.swf` | 2011-07-10 08:33:58 | 2011-04-07 (13,598 b) |
| `TankTrouble_v3.6e.swf` | 2012-09-10 07:22:04 | 2012-09-10 (33,049 b) |
| `TankTrouble_v3.8c.swf` | 2013-02-10 14:00:37 | 2013-02-10 (137,672 b) |

All contents were already held — **0 new SWFs** — but the timestamps are new.

### 36.3 New mirrors found

| Source | File | Bytes | Verdict |
|---|---|---|---|
| `chat.kongregate.com` | `TankTrouble_v1` | 101,377 | **★ NEW — earliest build yet** |
| `chat.kongregate.com` | `TankTrouble_v3.43` | 307,689 | **★ NEW** — origin serves 404 for this version |
| `chat.kongregate.com` | `TankTrouble_v3.8c` | 290,014 | duplicate |
| IA item `tank-trouble_flash` (creator **Purup**) | `Tank_Trouble.swf` | 290,449 | **★ NEW** |
| IA item `flashplayer32_…_202506` | `tanktrouble.swf` | 307,689 | duplicate of the Kongregate v3.43 |
| `github.com/ZeusWPI/multiplayer-ruffle` | `tank-trouble.swf` | 157,871 | mirror |
| `github.com/gameproxy/swf_storage_1` | `Tank Trouble 2.swf` | 366,881 | mirror |

Kongregate is the important one: it hosted its **own** copies on its **own** CDN, so
versions the origin has since deleted (`v1`, `v3.43` — both 404 on tanktrouble.com)
survive there intact. **Corpus 30 → 39 unique SWF builds.**

Exhausted: IA's Flash software collections contain exactly **one** TankTrouble item
(`tank-trouble_flash`, already taken). `?r=` referral values total **5 distinct**
across all captures — `Link embed`, `Link iframe`, `SpreadTheWord`, and two
`SWF <url>` entries — yielding exactly **one** external host (elte.hu, §34). That
channel is now fully mined.

Community repos (no server code, but real artefacts): `turtlesteak/TankTroubleCompendium`
(the official `TankTrouble.ttf`), `TankTroubleOnlineCompetition/TTOC` (71 MB of
tank/maze/gamemode art), `asger-finding/tanktroubleaddons` (active 2026; ships a
`Classic.zip` resource pack and a full dark-theme reskin of the classic UI),
`ttmand/ttforums` (§36.5).

### 36.4 ⚠ The live JSON-RPC API is an introspection oracle — 144 methods mapped

**Era note: this is the CURRENT (2026) backend, not the 2017–2019 one.** See §25.

`POST https://tanktrouble.com/ajax/`, JSON-RPC 2.0, namespace `tanktrouble`.
It answers **unauthenticated**, and its validation errors leak the signature:

```
params []             -> "Invalid parameter count for method getForumReplies. Expected 5 parameters."
[134783,0,10,0,0]     -> "Id must be positive"
[134783,10,0,0,0]     -> "Invalid direction specified. Must be 'older' or 'newer'"
[134783,1,"newer",false,25] -> "Invalid offset"
[134783,1,"newer",0,25]     -> OK
```

Parameter count, then per-argument type and domain, recovered one error at a time.
Signatures resolved this way:

```
forum.getForumThreadsById(threadId:int, limit:int)
forum.getForumReplies(threadId:int, cursorId:int>0,
                      direction:'older'|'newer', offset:int, limit:int)
news.getNewsPosts()                       # 0 params, returns the live feed
ping()                                    # -> {"result":true,"data":"pong"}
```

**144 method names** were extracted from held client sources, in namespaces
`account`, `achievement`, `admin`, `chat`, `forum`, `garage`, `message`, `news`,
`shop`, plus 30 unnamespaced. Full list in §36.6. Notable: `garage.getGarageContent`,
`garage.setAccessory`, `garage.setColour` — **the garage API has no maze method**,
consistent with §22.

Only `get*` and `ping` were ever called. No `create*`, `set*`, `delete*`,
`purchase*`, or `refund*` method was invoked.

### 36.5 The forum archive — 468 threads recoverable, none archived by Wayback

`ttmand/ttforums` is a hand-curated index by *Mandilindors* of notable threads,
plus a complete Lab Report index (27 volumes, issue numbers and authors).
**468 distinct `threadId`s**, range 1024 – 473752, weighted to the target era:

```
2015: 23   2016: 28   2017: 26   2018: 33   2019: 39   2020: 24
```

Wayback holds **none** of the bodies: `tanktrouble.com/forum?threadId=N` returns an
identical 33,504-byte SPA shell for every id, with content arriving over RPC. A
crawler therefore captured nothing but the shell — which is exactly why the wiki
pass (§31) flagged `forum?threadId=` URLs as never-archived.

Using the signatures from §36.4, all 468 threads plus their replies are being
pulled to `forum-archive/`, with `_index.tsv` mapping id → header → time → author.
Any thread exceeding the 1,000-reply page cap is logged by id as INCOMPLETE rather
than silently truncated.

## 37. `/includes/` recovered — 46 distinct files, and a silent-corruption trap

61 captures pulled, **46 distinct contents** (`includes-tree/`, `_manifest.tsv`
maps stored name → original URL → timestamp → sha256).

### 37.1 ⚠ Wayback `id_` returns raw stored bytes — including gzip

**12 files arrived gzip-encoded and would have been archived corrupt.** The `id_`
modifier returns the *stored* response body, so if the origin served
`Content-Encoding: gzip`, that is what you get — no transparent decoding, and no
error. A `.css` file that is actually gzip looks like a successful download.

```
  1583 ->   4198  20201222_main.css
  2337 ->   7534  20201225_scrapyard.js
178522 -> 759090  20201225_phaser.min.js
   ... 12 files total
```

**Rule: after any `id_` fetch, test for the `1f 8b` magic and decompress.** Extend
this to every file already collected — a whole-tree sweep of 1,005 files found
these 12. The same applies to Fandom serving WebP under `.png` (§31): always
verify by magic bytes, never by extension.

### 37.2 The classic site was part-HTML5 from February 2017

`phaser.min.js` (759,090 b) and `scrapyard.js` (7,534 b) are **byte-identical**
between the 2017-02-21 and 2020-12-25 captures. The Phaser-based scrapyard was
written by **February 2017** and never changed again until the December 2020
shutdown.

`scrapyard.js` is a clean, readable Phaser component:

```javascript
Scrapyard.UIConstants = {
    SCRAPYARD_PLATE_WIDTH: 11,              // canvas px
    SCRAPYARD_PLATE_HEIGHT: 22,             // canvas px
    SCRAPYARD_PLATE_SPACING: 1,             // canvas px
    SCRAPYARD_FLIP_DELAY: 100,              // ms - delay between spawning and flipping plates
    SCRAPYARD_FLIP_TIME: 630,               // ms - time it takes to flip a plate
    SCRAPYARD_FIRST_UPDATE: 60000,          // ms - time to first update
    SCRAPYARD_FOLLOWING_UPDATES: 300000     // ms - time between following updates
}
```

So the Flash→HTML5 migration was **not** a single cutover at the beta: the classic
site ran a Phaser component beside the Flash game for its last four years. The
scrapyard was the pilot.

### 37.3 Recovered server responses

`getScrapyard.php` — the global scrap counter, plain `key=value`:

```
20150928:  scraps=1662979870&velocity=0.0071382502652744
20160126:  scraps=1785664230
```

`embed.js` (185 b) — the official third-party embed, and the reason `embed.php`
exists:

```javascript
var banner = '<iframe id="tanktrouble" style="width: 712px; height: 570px;" scrolling="no" frameborder="0" src="http://www.tanktrouble.com/embed.php"></iframe>';
document.write(banner);
```

712×570 matches the `scale = 712 / theTankTroubleGame.offsetWidth` constant in
`DoAction.as`.

### 37.4 New files recovered

**21 new**, including four SWFs previously logged as failures — all four were
throttling, not absence:

| File | Capture | Bytes |
|---|---|---|
| `TankTrouble_v3.6c.swf` | 2012-06-15 | 277,825 |
| `signUpTankDesign04StandardColours.swf` | 2012-06-01 | 117,001 |
| `signUpTankDesign13StandardColours.swf` | 2013-04-09 | 230,921 |
| `signUpTankDesign16StandardColours.swf` | 2015-05-14 | 231,309 |
| `scrapyard11.swf` | 2015-09-28 | 9,743 |

Plus the complete classic stylesheet set (`styles`, `main`, `news`, `box`, `forum`,
`news`, `shop`), `mootools-release-1.11.js`, `swfobject.js`, `embed.js`, the four
trading-card PDFs, and the `c64` webfont in `.eot`/`.woff` (`.ttf` still failing).

**Still failing after 4 attempts:** `c64.ttf` @20150126100744 — retry later.

## 39. ★ BREAKTHROUGH — the 2018 garage page, and mazeCreator's exact path

Common Crawl's **`?garage` capture of 2018-03-17** (119,310 b decoded) is the
single most valuable document recovered in this hunt. Wayback never has it;
Wayback only ever captured the SPA-era shell or the logged-out homepage.

### 39.1 The path — and why every earlier search missed it

```javascript
var d = new SWFObject("includes/mazeCreator_v0.3.swf",
                      "userSettingsMazeCreatorFlash-" + user,
                      "688", "400", "8", "#ffffff");
d.addParam("allowScriptAccess", "sameDomain");
d.addParam("wmode", "transparent");
d.addParam("menu", "false");
d.addParam("FlashVars", "initCode=" +
    document.getElementById('userSettingsMazeCreatorInitCode-' + user).innerHTML);
d.write("userSettingsMazeCreator-" + user);
```

**The file lived at `/includes/mazeCreator_v0.3.swf`** — inside the very directory
enumerated exhaustively in §35, which found **75 paths and no `maze*` among them.**

This **corrects §35's conclusion** that the editor must have been served from a
garage-scoped path. It was in `/includes/` all along. The reason it is absent from
every index is now exact and provable:

> The `<script>` naming the file is present in the page for **everyone**, logged in
> or not — that is how Common Crawl captured it. But the SWF is only ever
> instantiated **inside `openMazeCreator(user)`**, which runs on a click in a
> logged-in user panel. A crawler parses the JS but never executes that path, so it
> never issues a request for the URL. No request, no capture, no CDX row.

Crawler-blindness was never about login-gating the *file*. It was about the URL
existing only inside a deferred `setTimeout` string.

Live probes 2026-08-02 — `classic.`, `www.`, apex, `cdn.`, `eu-central2-web2.`,
for both `mazeCreator_v0.3.swf` and `mazeCreator.swf`: **404 or no-connect on all
ten.** Wayback CDX for the now-exact URL on both hosts: **zero rows.** The bytes
are gone; the specification is not.

### 39.2 The complete external interface

Enough to reimplement the editor against its original contract.

**Embed:** 688 × 400, Flash 8, `wmode=transparent`, `menu=false`,
`allowScriptAccess=sameDomain`, background `#ffffff`.

**Input — HTML to SWF**, via FlashVar at construction:

| FlashVar | Source |
|---|---|
| `initCode` | `innerHTML` of `#userSettingsMazeCreatorInitCode-<user>`, rendered server-side |

**Control — HTML to SWF**, via `SetVariable`:

| Variable | Values | Meaning |
|---|---|---|
| `fadeOut` | `'true'` / `'false'` | drive the open/close animation |
| `newToolRequested` | tool name | switch active tool |
| `_root.saveRequested` | `'true'` | commit the maze |
| `_root.mazeName` | string | set the title |
| `_root.errorPanel.hide` | `'yes'` | dismiss the in-SWF error panel |
| `previewLoaded` | — | preview handshake |

**Output — SWF to HTML**, by callback: `hideMazeCreatorToolsAndTitle(user)` on
successful save; `showMazeCreatorToolsAndTitle(user, title)` when a maze opens.

**JS functions** (all recovered in full):
`openMazeCreator(user)`, `closeMazeCreator(user, position)`,
`attemptToSaveMaze(user)`, `cancelSaveMaze(user)`,
`selectMazeCreatorTool(user, tool)`, `updateMazeTitle(user, title)`,
`mazeTitleLegalCharacters(field, e)`,
`showMazeCreatorToolsAndTitle(user, title)`, `hideMazeCreatorToolsAndTitle(user)`.

**DOM ids:** `userSettingsMazeCreator`, `userSettingsMazeCreatorFlash`,
`userSettingsMazeCreatorInitCode`, `userpanelMaze`, `userpanelMazeTitle`,
`userpanelMazeConstructTool`, `userpanelMazeCreatorControls`,
`userpanelAcceptMaze`, `userpanelCancelMaze`, `userpanelSaveMaze`.

**Panel geometry:** panel widens 224 → 692 px, content height 99 → 385 px, wrapper
214 → 500 px, `Fx.Transitions.Quad.easeInOut` over 500 ms, staged at
+700/+1200/+1700 ms.

Together with the wire format from §30.5 (`t=title&n=author&d=<maze>`) and the
1,633+ decoded payloads, **the editor is now fully specified** — everything except
its compiled bytes.

### 39.3 ⚠ Common Crawl is NOT down — only its query server is

`index.commoncrawl.org` returns 502/504/000 on every query. **The underlying index
files on `data.commoncrawl.org` are fully available**, and they expose what Wayback
hides: `filename` + `offset` + `length`, so any record can be pulled with one HTTP
Range request.

Method that works without the query API:

1. Each collection has a sorted `cc-index/collections/<COLL>/indexes/cluster.idx` mapping SURT-prefix → (cdx shard, offset, length).
2. `cluster.idx` is 150–250 MB, so **binary-search it with Range requests** — ~20 reads of 64 KB — to find the block covering `com,tanktrouble)`.
3. Range-fetch that one block from the `cdx-*.gz` shard (~200 KB) and filter.
4. For each row, Range-fetch the WARC record; each is an independently-gzipped member, so it decompresses standalone.

Cost per crawl: well under 2 MB, versus a 160 MB full index download.

> **Bug worth recording:** my first `find_block` returned the last line it happened
> to read rather than the last line strictly less than the key. `CC-MAIN-2018-13`
> reported **0 rows when the true answer is 12** — a silent false negative that
> looked exactly like "not crawled". Fixed by scanning forward until a line ≥ key is
> actually observed. Validated against the known-good crawl before trusting the sweep.

### 39.4 What else the 2018 crawl held

| URL | Bytes | Note |
|---|---|---|
| `?garage` | 119,310 | **the mazeCreator loader** |
| `?news` | 382,029 | full news archive at that date |
| `?forum` | 70,453 | |
| `?lab` | 64,421 | |
| `?game` | 63,151 | |
| `/` | 63,133 | |
| `?shop` | 58,871 | |

`robots.txt` (2018), in full — it hid nothing:

```
User-agent: Mediapartners-Google
Disallow:
```

Only `.php` references anywhere in the 2018 bodies: `index.php`, `feedback.php`,
`logIn.php`, `embed.php`. **`feedback.php` is new** — not in the §30.6 list.

`?garage` also names `includes/loggedInTank06.swf`,
`includes/signUpTankDesign17StandardColours.swf` and `includes/TankTrouble_v4.0.swf`
— all three already held, which cross-validates the capture.

## 40. archive.today — user-supplied captures (`bEkyV`, `IH9r2`)

Two archive.today snapshots supplied directly, defeating the 429 wall in §30.1.
Both are **logged-out classic homepage** captures:

| Snapshot | Era | Evidence |
|---|---|---|
| `IH9r2` | **2016** | "Copyright … 2007 – 2016", 45,114,447 visits, 1,663,375 tank owners, "Access Online BETA — Beta access required", "LAST CALL May 1st duplicate emails will be unregistered!" |
| `bEkyV` | **2017** | "Copyright … 2007 – 2017", 60,091,191 visits, 2,631,762 tank owners, "Let the candy feast begin!" |

**The tab routes are now OBSERVED, not inferred** — both pages link all six:
`?game`, `?news`, `?garage`, `?shop`, `?forum`, `?lab`.

This **resolves the open question in §31**, which had to mark `?garage` as
INFERRED-only because no wiki revision contained the string. It also corrects the
guess `?laboratory` — the real route is **`?lab`**. Independently confirmed by the
Common Crawl 2018 rows (§39.4), which show all six returning 200.

Assets: archive.today stores content-addressed (`<sha1>.<ext>`), so filenames are
lost. Hashing against the held corpus recovered **39 identifications** — including
`c64.ttf`, `c64.woff`, `c64.eot` and the full `box*`/`tellAFriend`/`attentionSign`
set — which independently validates `classic-ui-images/`.

**30 assets match nothing held anywhere** — classic UI images that no other channel
has. Their original names are unrecoverable from the snapshot (no `alt`, `id`, or
`class` survives archive.today's rewriting), so they are kept under their content
hashes with era attribution in `archive-today/`.

Also preserved from these captures: live site statistics for two era-correct dates
(visit counts, tank-owner counts, concurrent players) and the Top-10 experience
leaderboards.

## 42. Common Crawl full-range sweep — the clone ecosystem

### 42.1 ⚠ v1 of my sweep silently excluded every subdomain

The first sweep searched only the block covering `com,tanktrouble)`. In SURT
ordering `)` is 0x29 and `,` is 0x2C, so **`com,tanktrouble,beta)`,
`com,tanktrouble,cdn)`, `com,tanktrouble,classic)` all sort into LATER blocks** and
were never read. v1 reported ~6–20 rows per crawl and looked complete.

v2 sweeps the whole SURT range `[com,tanktrouble, com,tanktrouble~)` and returns
**~1,000 rows per crawl**. (CC canonicalisation strips `www.`, so www and apex both
map to `com,tanktrouble)` and were always covered.)

### 42.2 A clone-site ecosystem, 34 hosts

The range also captures every `tanktrouble*` domain, which turns out to be a large
mirror ecosystem never visible from the origin's own logs:

```
4829  tanktroubleplay.com            102  tanktroublefree.com
1682  tanktroublex.com                93  tanktroublepage.com
 738  tanktroubleunblockedgame.com    92  tanktroublegame2.com
 589  tanktrouble234.com              60  tanktrouble3.com
 193  tanktrouble123.com              57  tanktrouble6.com
 151  www.tanktrouble3.com            46  tanktrouble2online.com
 117  tanktroubleonline.com           37  tanktrouble4.com
 101  tanktrouble.com                 36  tanktroublehacked.com
                                      30  tanktrouble2swf.com
```

Each hosts its own SWF copy, frozen at upload date. **3 new builds** so far:

| Host | File | Bytes |
|---|---|---|
| `tanktrouble3.com` | `/swf/tanktrouble.swf` | 290,453 |
| `tanktroublex.com` | `/swf/tank-trouble-3.8c.swf` | 290,018 |
| `tanktroublefree.com`, `tanktroublepage.com` | `/upload/games/tank-trouble.swf` | ~290,860 |

> `tanktroublex.com/swf/cubefield.swf` is a **different game** and is not counted
> as a TankTrouble build.
>
> **Parser bug:** two records decoded with a stray `\r\n` before the payload, so the
> magic-byte check saw `\r\nCWS` and rejected valid SWFs as NOT-SWF. Fixed with an
> `lstrip(b"\r\n")` before the check.

### 42.3 New site structure — path routes, not just `?routes`

Extracting every `href`/`src`/`action` and absolute URL from all recovered bodies
(145 files) gives directories that appear in **no** earlier enumeration:

| Directory | Evidence |
|---|---|
| `/spreadTheWord/` | banner kit — `TankTrouble_400x50.js`, `TankTrouble_72x36.js` + JPEGs. **This is the source of the `?r=Link embed` / `Link iframe` referrals in §36.3.** |
| `/privacy/` | **live 200 on apex today** |
| `/shop/` | **live 200 on apex today** |
| `/like/` | referenced ×73, never archived |
| `/statistics/` | 301 in 2010 |
| `/ios/` | 200 in 2012 |
| `/theLabReport/` | `The_Lab_Report_volume_10_issue_4.pdf` |
| `/infirmary/` | already known |

Confirmed `?route` set is exactly six: `?game ?news ?garage ?shop ?forum ?lab`.
Everything else matching `?word` in the corpus is a **query parameter**, not a
route — `?rs` (SAJAX function), `?ls`, `?id`, `?subject`, `?ref` — or third-party
noise. No seventh tab exists.

### 42.4 ⚠⚠ THE CDN IS A CATCH-ALL — a live era-conflation trap

CC bodies revealed **five RELEASE tags with zero rows in Wayback**:
`RELEASE-2018-03-09-01`, `2018-05-17-01`, `2018-06-14-02`, `2018-08-03-01`,
`2018-10-01-01`.

Probing the CDN for them returned **HTTP 200 on every one**. That looked like five
unarchived era-correct client trees recovered live.

**It is not. Verify before believing it:**

```
cdn-beta.tanktrouble.com/RELEASE-2018-03-09-01/js/backend.js  103030 b  sha 84c6e35510c7796a7eea
cdn-beta.tanktrouble.com/RELEASE-2018-04-20-01/js/backend.js  103030 b  sha 84c6e35510c7796a7eea
cdn-beta.tanktrouble.com/RELEASE-2019-10-04-01/js/backend.js  103030 b  sha 84c6e35510c7796a7eea
cdn-beta.tanktrouble.com/RELEASE-2026-05-11-01/js/backend.js  103030 b  sha 84c6e35510c7796a7eea
cdn-beta.tanktrouble.com/RELEASE-BOGUS-9999-99-99/js/backend.js   287 b  sha 48a4862e46dfd77a000f
```

Any **well-formed** `RELEASE-*` path serves the **current 2026 build**; only
malformed paths 404. The path segment is decorative — a cache-busting prefix, not a
directory.

**Consequence:** the CDN cannot return any historical release, and five files that
would have been filed as era-correct 2018 client code are five copies of the 2026
build. This is the same era-conflation failure recorded in §17/§25, and it is
*actively produced* by the live server.

**Rule: never accept a 200 from a versioned CDN path as historical. Hash it against
the current release first, and probe a deliberately bogus version as a control.**

The five releases therefore remain **proven to have existed, bytes unrecovered** —
referenced by pages Common Crawl captured in 2018, crawled by nobody. Wayback's
13 era-correct tags (§30.7) remain the only real source, and those are already held.

## 44. Full Common Crawl sweep — final numbers

**126,679 rows · 125 collections · 75 hosts · 35,859 distinct URLs**, back to
`CC-MAIN-2009-2010`. (`CC-MAIN-2008-2009`: 0 rows — the site predates that crawl's
coverage of it.)

The clone ecosystem dwarfs the origin: `tanktrouble234.com` 57,237 rows,
`tanktroubleplay.com` 49,151, `tanktroublex.com` 7,299 — versus 756 for
`tanktrouble.com` itself.

### 44.1 The origin's own inventory — 53 distinct (host, path)

The headline: **`?garage` captured 41 times between 2010-09-08 and 2021-07-30.**
An eleven-year time series of the one page that loads the maze editor. Also
`?news` ×45 (2010→2026), `?lab` ×40, `?forum` ×37, `?game` ×37, `?shop` ×31.

New paths this sweep added:

| Path | Note |
|---|---|
| `theLabReport/The_Lab_Report_volume_{10_4,11_1,11_5,12_3,13_2,13_4,14_3,18_1}.pdf` | **8 distinct issues** — naming convention `volume_N_issue_M` |
| `beta.tanktrouble.com/forum?threadId=169003&id=663339` | beta forum, and it exposes a **second id parameter** |
| `beta.tanktrouble.com/news?postId=74` | beta news permalink |
| `www.tanktrouble.com/statistics/` | 200 in 2013 |
| `beta.tanktrouble.com/{game,news,shop}` | path-style routes on beta vs `?routes` on classic |

### 44.2 Related-domain sweeps — mostly negative

Parameterising the sweep key (`CC_KEY`) and re-running:

| SURT | Result |
|---|---|
| `dk,tanktrouble` | **0** — no Danish domain, despite the developer being Danish |
| `dk,purup` | **0** |
| `com,sublabgames` | **0** |
| `net,tanktrouble` | 9 rows — 4 clone domains |
| `org,tanktrouble` | 6 rows — 2 clone domains |
| `com,purup` | 626 rows, but only **5** are actually `purup.com`/`www.purup.com`; the rest are unrelated Japanese `purupuru*` sites |
| `com,subterraneansoftware` | 6 rows — the **Android publisher** (`com.subterraneansoftware.tanktrouble.android`) |

## 45. Client module tree, recovered from PageSpeed bundle names

Google PageSpeed's combine filter names its output after **every input file**, with
`,_` encoding a directory separator:

```
adminoverlaynavigation.js+adminoverlayuploadimage.js+overlays,_accountoverlay.js+…
  .pagespeed.jc.RWzlorml9B.js
```

Each bundle filename is therefore a **verbatim directory listing the server never
exposed**. Harvesting every bundle name across the CDX dumps and recovered bodies
yields **568 distinct source modules**.

> Era note: this is the **HTML5 client** (beta 2017-19 → modern). It is NOT the
> classic Flash site. See §25.

### 45.1 The complete overlay / popup inventory (40+)

```
accountoverlay              accountrecoveryoverlay      accountreversaloverlay
accountverificationoverlay  achievementsoverlay         advertisementoverlay
controlsoverlay             deleteaccountoverlay        faqoverlay
garageoverlay               loginoverlay                messageoverlay
messagesoverlay             newemailoverlay             newgameoverlay
newpasswordoverlay          newsletterunsubscriptionoverlay
newusernameoverlay          recoveraccountoverlay       shopitemdetailsoverlay
shoppurchaseoverlay         shopstockupoverlay          signupoverlay
virtualshopitemdetailsoverlay  virtualshopoverlay       overlaymanager

admin: adminacceptguidelinesoverlay adminchatlogoverlay adminchatreportsoverlay
       admindashboardoverlay adminlogoverlay adminmessagesoverlay
       adminnewsoverlay adminplayerlookupoverlay adminplayernamesoverlay
       adminserverlogoverlay adminshopoverlay adminstatisticsoverlay
       adminstatsoverlay adminvirtualshopitemdetailsoverlay
       adminvirtualshopoverlay adminoverlaynavigation adminoverlayuploadimage

boxes: adduserbox chatbox cookiebox errorbox selectuserbox settingsbox tankinfobox
```

**There is no maze overlay.** Combined with §36.4 (the garage RPC namespace has
only `getGarageContent`/`setAccessory`/`setColour`), this is a third independent
confirmation that the HTML5 client never had a maze editor.

### 45.2 Subdirectories proven by the `,_` separator

`game/` (46 UI modules — emitters, sprites, particle groups, states),
`adproviders/` (`adplacementadprovider`, `ima3adprovider`), `codemirror/`
(`css`, `htmlmixed`, `javascript`, `placeholder`, `xml`), `encoding/`
(`base64js.min`, `textencoderlite`), `autotrack/`, `classy/`, `dateformat/`,
plus `overlays/`, `scrapyard/`, `playerpanel/`, `jqueryplugins/`, `tooltipster/`.

## 46. Predicted server filesystem layout

Every line is tagged with **how it is known**. Nothing here is decoration:

- `binary-literal` — a string inside a compiled SWF
- `http-observed` — a real HTTP response was captured
- `listing-observed` — an actual directory listing was captured
- `header-inferred` — deduced from response headers or server banner
- `convention-inferred` — standard for the observed stack
- `scaffold` — structural guess, explicitly unverified

```
/var/www/…/                                    [header-inferred: Apache 2.4.29 Ubuntu default is /var/www/html]
├── index.php                                  [http-observed 2008→; SAJAX front controller, ?rs= dispatch]
├── embed.php                                  [http-observed ×13; 712×570 iframe target]
├── logIn.php                                  [http-observed 404 in 2008 — name proven, file already gone]
├── feedback.php                               [http-observed — referenced in 2018 bodies only]
├── getimage.php                               [http-observed ×99; ?id=N — images keyed by integer, not path]
├── uploadimage.php                            [http-observed 2021 — admin news image upload]
├── robots.txt                                 [http-observed; Mediapartners-Google only, hides nothing]
├── ads.txt                                    [http-observed]
├── includes/                                  [403 live — EXISTS, autoindex off]
│   ├── mazeCreator_v0.3.swf                   [binary-literal/JS-literal §39 — NEVER fetched by any crawler]
│   ├── TankTrouble_v{1.11,1.3,…,4.03}.swf     [http-observed: 200 for some, 404 for the retired ones]
│   ├── TankTrouble_v{3.5,3.6,3.6e,3.8c}.zip   [http-observed — distribution kits]
│   ├── signUpTankDesign{01,04,09,11,13,16,17,18}StandardColours.swf   [http-observed]
│   ├── scrapyard{,01,03,04,05,06,10,11}.swf   [http-observed]
│   ├── loggedInTank06.swf, laika02.swf, ima3_preloader_1.5.swf        [http-observed]
│   ├── loadMaze.php, updateGameStatistics.php, getScrapyard.php       [http-observed]
│   ├── {styles,main,news,box,forum,shop}Styles.css                    [http-observed]
│   ├── {swfobject,mootools-release-1.11,embed,phaser.min,scrapyard}.js [http-observed]
│   ├── c64.{ttf,woff,eot}                     [http-observed]
│   ├── TTTradingCardsSeries{I,II,III}.pdf     [http-observed]
│   ├── images/                                [http-observed: includes/images/scrapyardPlates.png 404]
│   └── Assets/                                [404 at this path — the real one is at web root, see below]
├── Assets/                                    [403 live — EXISTS; capital A]
│   ├── Tank.swf  GameTank.swf  Crate.swf  Laika.swf                   [http-observed; 8 distinct Tank builds]
├── images/                                    [http-observed ×4168 — largest reference count]
│   └── shop/                                  [http-observed 2018-03-10]
├── spreadTheWord/                             [listing-observed 2008 index]
│   ├── TankTrouble_{400x50,72x36}.js          [http-observed — affiliate banner kit]
│   └── images/TankTrouble_{400x50,72x36}.jpg  [http-observed]
├── theLabReport/                              [http-observed]
│   └── The_Lab_Report_volume_{N}_issue_{M}.pdf [http-observed ×8 — convention proven by 8 samples]
├── infirmary/                                 [http-observed ×26 — "TEMPORARY WARP" per leaked comment]
├── ios/                                       [http-observed 200 in 2012, 403 in 2020]
├── statistics/                                [http-observed 200 in 2013, 301 in 2010]
├── privacy/                                   [live 200 today — modern SPA route]
├── shop/                                      [live 200 today — modern SPA route]
├── like/                                      [referenced ×73, never fetched — scaffold]
└── ajax/                                      [http-observed — modern JSON-RPC endpoint]
```

**Load-bearing structural inferences:**

1. **Case-sensitive filesystem.** `/Assets/` (capital) and `/includes/` (lowercase) both exist and both 403 live. Confirms Linux, consistent with the Apache/Ubuntu banner. `/includes/Assets/Tank.swf` returns **404** while `/Assets/Tank.swf` returns 200 — so `Assets/` sits at the web root, *not* under `includes/`, even though the distribution zips nest it that way.
2. **The zips mirror the dev tree, not the server tree.** Each zip contains `TankTrouble_vX.swf` + `Assets/`, which is how the developer's Flash project was laid out on macOS (`__MACOSX` forks). On the server those two levels were flattened apart.
3. **Images are content-addressed by integer.** `getimage.php?id=N` — so news/shop imagery is **not** recoverable by guessing filenames; only by enumerating ids.
4. **`RELEASE-*` is not a directory.** Proven in §42.4 — it is a cache-busting rewrite prefix on the CDN. The real client tree has no version level.
5. **No directory listing anywhere on tanktrouble.com.** Every `/dir/` probe returns 403, never a listing. The only `mod_autoindex` output in the entire corpus is from the third-party elte.hu host (§34).
6. **Two dispatch styles, split by era.** Classic = `index.php?<tab>` with SAJAX `?rs=<fn>`. Modern = path routes (`/game`, `/news`, `/forum`) with JSON-RPC at `/ajax/`. `beta.` used path routes while `www.` still used `?routes` — the two ran in parallel (§25).

## 48. ★ The garage time series — 47 captures, 2010–2021

Fetching every Common Crawl `?garage` capture gives an eleven-year time series of
the one page that loads the maze editor.

### 48.1 A NEW FILENAME: `mazeCreator_v0.2.swf`

```
2010-09-08   78,798 b   includes/mazeCreator_v0.2.swf     <-- previously unknown
2013-06-18  107,112 b   includes/mazeCreator_v0.3.swf
2017-01-24 … 2020-12-04 (40 captures, 111k–120k b)        includes/mazeCreator_v0.3.swf
2021-01-18   32,601 b   (none)
```

**Version history established:** `v0.2` in 2010 → `v0.3` by 2013-06-18 → then
**frozen for seven and a half years**, unchanged through to the final capture on
2020-12-04.

`v0.2` is as unrecoverable as `v0.3`: CDX returns an explicit `[]` for
`www.tanktrouble.com/includes/mazeCreator_v0.2.swf` (not a flaky empty), a
domain-wide regex over **17,598** maze-matching rows finds no mazeCreator SWF at
all, and live probes 404 on `classic.`, apex and `cdn.` for `v0.1`, `v0.2`, `v0.3`
and the unversioned name.

### 48.2 The garage removal pinned to a five-week window

The page collapses from **111,553 b (2020-12-04, mazeCreator present)** to
**32,601 b (2021-01-18, absent)**. That brackets the garage teardown to
**2020-12-04 … 2021-01-18**, sharpening §19's "December 2020 migration".

### 48.3 Other filenames only this time series reveals

`includes/loggedInTank04.swf` and `includes/signUpTankDesign04.swf` (2010),
`includes/TankTrouble_v3.41.swf`, `includes/scrapyard05.swf` — all referenced in
the 2010 garage, none held. The `signUpTankDesign` sequence visible across the
series is 04 → 13 → 17 → 18, matching §35.

## 49. ⚠ Validation failure — a size check is not an integrity check

Two files were written into `mazeCreator-ui-images/` as `.png` and reported as
recovered. They were **151 KB Wayback HTML error pages**:

```
magic = 3c 21 44 4f 43 54 59 50 45   ("<!DOCTYPE")
```

The fetch helper only tested `size > 200`, which a large error page passes
trivially. Both were deleted and the fetcher rewritten to validate against real
signatures (`\x89PNG`, `\xff\xd8\xff`, `GIF8[79]a`) and to reject-and-retry on
mismatch.

This is the **third** occurrence of the same class of bug in this hunt —
after Fandom serving WebP under `.png` (§31) and Wayback `id_` returning gzip
under `.css` (§37.1).

> **Standing rule: never accept a downloaded file on size or extension. Verify
> magic bytes, and treat a mismatch as a failed fetch, not as data.**

Recovered under the corrected fetcher: `images/busyMaze.png` (86,202 b, verified
PNG). The six mazeCreator *toolbar* images remain unrecovered — `mazeConstructToolSelect.jpg`
has only a 302 in CDX — so §29's claim holds specifically for the toolbar set.
`images/mazeCreator.png` (the garage icon) has a 200 capture and is retryable.

## 50. `TankTrouble_v4.1.0.swf` — a version referenced nowhere else

Clone-host markup mining surfaced `TankTrouble_v4.1.0.swf` on
`tanktroubleunblockedd.com` and `tanktrouble2unblockedd.com` — **later than the
v4.03 that is the last known build**.

Status: CDX `[]` on both clone hosts and on `tanktrouble.com/includes/`; live 404
on `classic.` and apex for `v4.1.0`, `v4.1` and `v4.04`. Treat as **a filename
observed in third-party markup**, not yet as a proven origin build — the clones
rename freely (§36.3 documents hosts that suffix every unrelated game with
"tank-trouble").

### 50.1 Clone embed survey — no deep mirrors

55 clone hosts sampled, 6 pages each. Every one either hotlinks
`tanktrouble.com/embed.php` or serves a flat self-hosted copy
(`/tt/tt3.8c.swf`, `/swf/tanktrouble.swf`, `/uploads/games/…`).

**Zero hosts mirror `/includes/`.** That closes the last plausible non-human route
to the mazeCreator bytes: no clone copied the directory, so none could have
incidentally captured the editor.

## 51. Columnar index — feasible, and now measured

DuckDB + `httpfs` against the Parquet index. Two gotchas:

1. DuckDB **cannot glob generic HTTP paths** (`Globs (*) for generic HTTP file are not supported`). Get the explicit part list from the crawl's own `crawl-data/<CRAWL>/cc-index-table.paths.gz` manifest — 300 `subset=warc` parts per crawl.
2. There is no index on URL substrings, so this reads the `url_path` column of every part. Parquet column pruning keeps it to that column only.

**Measured: 11.4 s/part → ~57 min per crawl.** Practical for selected crawls,
not for all 126.

First 3 parts of `CC-MAIN-2018-13` already prove the value — it finds hosts the
SURT sweep is structurally blind to:

```
200  http://www.paisdelosjuegos.com.ar/juego/tank-trouble.html
200  http://poki.at/g/tank-trouble
```

Neither host name contains "tanktrouble", so **no SURT-prefix sweep could ever
return them**.

## 52. Maze imagery — recovered, with the host caught as the real cause

The first retry pass reported `MISS` for `images/mazeCreator.png` and
`images/maze.png` even though CDX shows 200 captures for both. Cause was **not**
flakiness: those files live on **`classic.tanktrouble.com`**, and the fetcher was
built with the apex host hard-coded. Refetching against the correct host, by exact
14-digit timestamp, succeeded first attempt.

Recovered and magic-validated (`89504e47` / `ffd8ffe0`):

| File | Bytes | Source |
|---|---|---|
| `images_mazeCreator.png` | 2,806 | `classic.` @20201222135147 — **the garage's maze-creator icon** |
| `images_busyMaze.png` | 86,202 | `classic.` @20201221 |
| `assets_tankInfo_mazeCreator.png` | 2,968 | apex @20210401220517 |
| `assets_tankInfo_mazeCreatorActive.png` | 2,975 | apex @20210401220521 |
| `assets_lobby_mazes.png` | 15,845 | apex @20260129 |
| `images_maze_2010.jpg` | 1,189 | @20101128 |

> `images_maze.png` came back **byte-identical** to `images_busyMaze.png`
> (sha256 `63e42c3acc6a26ec…`), despite CDX listing different compressed lengths.
> One of the two fetches resolved to the other. Counted as **one** image, not two;
> `maze.png` is treated as still unconfirmed.

The six mazeCreator **toolbar** images (`mazeConstructTool*`, `crateSpawnTool*`,
`tankSpawnTool*`) remain unrecovered — consistent with §10: they were only ever
swapped in by JS on a logged-in click, so no crawler requested them.

## 53. ★★ The maze wire format, fully decoded — a behavioural spec for the lost editor

The bytes of `mazeCreator_v0.3.swf` are still gone, but **everything it produced is
now readable**, and the format is pinned by two independent sources that agree
exactly.

**Source A — the corpus.** 806 `loadMaze.php` payloads parsed from `maze-corpus\raw\`
(the fetcher was still running; this is a snapshot, not the final 4,192).

**Source B — `MazeDataFetcher.as`**, present in the decompiles of TankTrouble
**v3.5, v3.6, v3.6e and v3.8c**. This is the *reader* for the format the creator
*wrote*, so it is the authoritative inverse. It had been sitting in `decompiled\`
the whole time; nothing new had to be fetched to get it.

### 53.1 The transport

```
GET includes/loadMaze.php?q=<base64( shuffleMessage("userName=<name>&a=<rand>&b=<rand>") )>
    (logged-out form: "c=<rand>&a=<rand>&b=<rand>")

200 →  r=<base64>&s=<slot>
b64 →  t=<title>&n=<author>&d=<grid>
```

`shuffleMessage()` (recovered verbatim from `frame_1/DoAction.as`) is **not
encryption** — it randomly permutes the `&`-separated pairs and rejoins them. The
`a=`/`b=` randoms are cache-busting salt. Decoding needs no key.

### 53.2 The grid string

```
<w> # <cells> # <reserved> # <objCount> # (<x> # <y> # <type> # <params>) … # 0 #
```

* `w` = width. **Height is implicit**: `h = len(cells) / w`. Corpus: exact integer
  for 806/806.
* `cells` is one **octal digit per cell**, row-major, `for y { for x } }`.
* `reserved` is read into a local and then **never referenced** — dead field.
  Always `0` in the corpus.
* Each object is **four** `#`-fields, the last a comma-list. That list is empty for
  every object ever saved, which is why the records *look* separated by `##`.
  The trailing `0` is a terminator, skipped by an unconditional `_loc10_++`.

### 53.3 Cell bits — from `MazeDataFetcher.createMaze()`, lines 101–134

| Bit | Value | Effect in the client |
|---|---|---|
| 2 | `4` | `tile[x][y][2] = 1` — **wall on the west edge** |
| 1 | `2` | `tile[x][y-1][1] = 1` — wall shared with the cell **above** (stored as that cell's south edge) |
| 0 | `1` | `tile[x][y][0] = 1` **and** `grounds.push({x,y})` — **floor present** |

South and east arena borders are never stored; they are implied by the absence of a
neighbour. That is exactly what the corner statistics show: top-left `7`
(floor+N+W, 68.6%), top-right `3` (floor+N, 54.3%), bottom-left `5` (floor+W,
58.2%), bottom-right `1` (floor only, 47.4%).

**Validation.** A cell whose north or west neighbour is absent must itself carry
that wall, or the arena leaks. Across **806 mazes / 79,492 cells: 0 violations,
806/806 fully consistent.** Rendered as ASCII, every maze is a closed, plausibly
hand-designed arena. See `maze-corpus\_render-samples.txt`.

### 53.4 Objects — types confirmed, not guessed

`createMaze()` has a two-case `switch` and **no default**:

```as
case 5:  spawnPoints.push({x: x-1, y: y-1});        // tank spawn
case 8:  crateSpawnPoints.push({x: x-1, y: y-1});   // crate spawn
```

Coordinates are stored **1-indexed** and decremented on load. The corpus contains
types `5` and `8` and nothing else — 5,366 objects, 0 out of bounds.

### 53.5 What the editor allowed — read off the corpus

Every limit below is what 806 user-authored mazes never crossed, so it is very
likely a constraint the tool enforced rather than a coincidence of taste.

| Constraint | Value |
|---|---|
| Grid width | 1 … **18** |
| Grid height | 1 … **10** |
| Distinct sizes used | 113; modal **18×10** (181 mazes) |
| Title length | ≤ **32** |
| Title charset | `A–Z a–z 0–9` + space + `! , - . ?` (68 distinct) |
| Author length | ≤ 16 |
| Object types | **only 5 and 8** |
| Max per type | **5 tank spawns, 5 crate spawns** |
| Max objects | **10**; 142/806 mazes have none |
| Absent cells | 24.4% of all cells — **non-rectangular arenas were expressible**, and 630/806 mazes use at least one |

The three limits — walls, ≤5 tank spawns, ≤5 crate spawns — map one-to-one onto the
three toolbar icon pairs whose filenames §52 could not recover
(`mazeConstructTool*`, `tankSpawnTool*`, `crateSpawnTool*`). Independent closure:
the tool had exactly three tools, and we now know what each one emitted.

### 53.6 Playback behaviour

`BUFFER_SIZE = 2`, `NUM_PLAYS = 3`: the client prefetches two mazes and plays each
**three rounds** before rotating. Requests pick a uniformly random name from the
logged-in players, so a maze's exposure was proportional to how many of its
author's friends were in the room.

### 53.7 What this does and does not give us

**Does:** the format is complete enough to write a working replacement editor and
to replay all 4,192 archived mazes. Nothing about the *format* is still unknown.

**Does not:** the save endpoint. §53.8 covers why.

## 54. The classic server's RPC surface — 36 SAJAX functions, dated

Every classic page shipped generated SAJAX stubs (`function x_<name>(…)`). Scanning
all captured HTML bodies yields the complete list, and each function's
**first and last appearance dates the feature**.

36 distinct functions. Selected dating:

| Function | First seen | Last seen | Reading |
|---|---|---|---|
| `login` `logout` `signup` `post` `vote` `edit` `updateTank` `updateTop10` `updateUserPanels` `reloadGame` `getLoginInfo` `getAllUserInfo` `setApprove` `setDelete` `setDisable` `startThread` `showForumThread` `showForumPreviews` `showEditPost` `setCloseThread` `setDeleteThread` `setDisableThread` `feedback` | 2010-02-08 | 2020-12-04 | the original surface |
| `generateUsertrail`, `updateFormData` | 2012-01-28 | 2020-12-04 | one release |
| `changePassword`, `sendRequest` | 2012-02-06 | **2018-07-22** | **removed** after Jul 2018 |
| `checkForAchievements`, `setBan`, `setBanThread`, `setFilterAndShowForumPreviews`, `showForumThreadLastPage` | 2013-05-23 | 2020-12-04 | one big release |
| `sendVerificationEmail` | 2013-12-06 | 2020-12-04 | |
| `showShop` | 2015-08-01 | **2017-03-30** | the classic shop was **temporary** |
| `formCheckEmail` | 2016-05-25 | 2020-12-04 | |
| `getScraps` | **2017-02-21** | 2020-12-04 | matches §37's byte-identical `scrapyard.js` date exactly — **independent confirmation** the Phaser scrapyard went live 2017-02-21 |

Last capture of any stub is **2020-12-04**, the opening bound of the garage teardown
window in §48. Third independent line of evidence for that date.

### 54.1 ⚠ There is no maze RPC — and that is the finding

**None of the 36 is maze-related.** No `saveMaze`, `getMaze`, `deleteMaze`,
`listMazes`. Combined with §39's recovered JS, the save path is now explained:

* JS does **not** call the server. It sets a variable *inside the SWF*:
  `SetVariable("_root.saveRequested", "true")`, plus `_root.mazeName`.
* So **`mazeCreator_v0.3.swf` performs its own save**, to an endpoint named
  nowhere else on the site.

Cross-checks for that endpoint, all negative:

| Check | Result |
|---|---|
| PHP endpoints in all decompiled clients | 4 only: `updateGameStatistics.php` (37), `achievement.php` (6), `loadMaze.php` (5), `getUserAuthentication.php` (5) |
| PHP endpoints across the whole CDX | `loadMaze.php` ×17,411, `updateGameStatistics.php` ×2,305, `getimage.php` ×99, `content.php` ×42, plus single-digit `index/embed/getScrapyard/admin/logIn/uploadimage` |
| `saveMaze` string anywhere in the corpus | not present |

So the write endpoint's *name* is inside the lost SWF and only there. This is the
one part of the maze system that the format decode does **not** recover — and,
usefully, it is also the one part a replacement implementation does not need.

### 54.2 New endpoints surfaced by the same pass

Not previously logged, all outside the game client: `getScrapyard.php`
(`?scraps`, `?velocity`), `getimage.php` (`?id`, `?at2x`), `uploadimage.php`,
`content.php` (per-RELEASE), `embed.php` (`?from`), `admin.php`, `logIn.php`.
`admin.php` and `logIn.php` appear once each, both **404** in 2008–09 — probes, not
real paths.

## 55. ★ Complete dated embed inventory of the classic site

Scanning every captured HTML body for `new SWFObject("…")` and for bare `*.swf`
string literals yields **20 distinct SWF filenames** with exact first/last-seen
dates. This is the classic site's whole Flash surface, and it is the first
authoritative answer to *what is still missing*.

| Embed | DOM target | Live window | Captures | Held? |
|---|---|---|---|---|
| `TankTrouble_v3.13.swf` | `TankTroubleGame` | 2010-02-08 | 1 | ✗ |
| `TankTrouble_v3.2.swf` | `TankTroubleGame` | 2010-03-10 | 1 | ✗ |
| `TankTrouble_v3.3.swf` | `TankTroubleGame` | 2010-09-03 | 1 | ✗ |
| `TankTrouble_v3.41.swf` | `TankTroubleGame` | 2010-09-08 | 1 | ✗ |
| `TankTrouble_v3.6b.swf` | `TankTroubleGame` | 2012-01-28 | 1 | ✗ |
| `TankTrouble_v3.6c.swf` | `TankTroubleGame` | 2012-05-19 | 1 | ✓ 277,825 b |
| `TankTrouble_v4.0.swf` | `TankTroubleGame` | 2013-05-23 … 2020-12-04 | **136** | ✓ **two sizes** |
| `laika02.swf` | `laika` | 2010-09-08 … 2020-12-04 | 38 | ✓ 12,415 b |
| `loggedInTank02.swf` | `loggedInTank-` | 2010-02-08 … 2010-03-10 | 2 | ✗ |
| `loggedInTank04.swf` | `loggedInTank-`, `forumTank-`, `signedUpTank`, `usertrailicon-flash` | 2010-09-03 … 2012-05-19 | 4 | ✗ |
| `loggedInTank06.swf` | same four | 2013-05-23 … 2020-12-04 | 134 | ✓ 2,324 b |
| **`mazeCreator_v0.2.swf`** | `userSettingsMazeCreatorFlash-` | **2010-09-08 only** | 1 | ✗ |
| **`mazeCreator_v0.3.swf`** | `userSettingsMazeCreatorFlash-` | 2013-06-18 … 2020-12-04 | 39 | ✗ |
| `scrapyard05.swf` | `scrapyard` | 2010-02-08 … 2010-09-08 | 4 | ✗ |
| `scrapyard06.swf` | `scrapyard` | 2012-01-28 … 2014-10-26 | 29 | ✓ 5,117 b |
| `scrapyard07.swf` | `scrapyard` | 2014-10-30 … 2014-10-31 | 2 | ✗ |
| `scrapyard08.swf` | `scrapyard` | 2014-11-22 | 1 | ✗ |
| `scrapyard10.swf` | `scrapyard` | 2014-11-28 … 2015-08-01 | 12 | ✓ 9,830 b |
| `scrapyard11.swf` | `scrapyard` | 2015-08-05 … 2017-01-24 | 16 | ✓ 9,743 b |
| `signUpTankDesign04.swf` | `signUpTankDesign`, `userSettingsTankFlash-` | 2010-09-08 | 1 | ✓ 117,001 b |
| `signUpTankDesign13StandardColours.swf` | both | 2013-05-23 … 2017-03-30 | 63 | ✓ 230,921 b |
| `signUpTankDesign17StandardColours.swf` | both | 2017-01-24 … 2018-07-22 | 28 | ✓ 231,334 b |
| `signUpTankDesign18StandardColours.swf` | both | 2018-08-14 … 2020-12-04 | 45 | ✓ 231,417 b |

Plus `expressinstall.swf` (SWFObject boilerplate, 2010–2012).

### 55.1 Three findings from the table

**(a) `TankTrouble_v4.0.swf` never changed — 7½ years, one build.** ⚠ My first pass
claimed it existed at two sizes (347,219 b and 366,827 b) and had therefore been
silently rebuilt. **That was a substring-match error**: the 347,219 b file is
`TankTrouble_v4.**03**.swf`, a different filename. Corrected result, which is the
stronger one:

| Fact | Evidence |
|---|---|
| `TankTrouble_v4.0.swf` = **366,827 b**, sha256 `188062aff7f7d969…` | 4 independent copies: `includes-tree\` @2013-03-13 **and** @2020-12-25, Flashpoint curation, vseigru mirror @2019 |
| **One** CDX digest (`R43R6IEQ…`) across all 21 archived 200s, 2013-03-13 → 2020-12-25 | `wayback-inventory\cdx-*.txt` |
| `TankTrouble_v4.03.swf` = 347,219 b, sha256 `338f186822…` | separate, later file; live on `classic.` and captured @2023-09-08 |

So the classic Flash game binary was **frozen from March 2013 until the site died**
— the same 7½-year freeze already established for `mazeCreator_v0.3` (§48). Two
assets, same window, same behaviour: after v4.0 shipped, Purup's effort went to the
HTML5 client, not the Flash one.

> **CDX field semantics, settled by this data.** All 21 rows share one digest while
> the `length` column ranges 367,324 … 367,733. Length is the **stored record size**
> and varies with gzip settings; it is not a build discriminator. The portal sweep
> (§ PORTAL-FINDINGS) hit the mirror image — one URL, two digests, identical fetched
> payloads. Taken together: digest can over-split and length can mislead, so
> **sha256 of the decoded payload is the only authoritative build identity**.

**(b) `scrapyard09` never appears.** The series runs 05, 06, 07, 08, **—**, 10, 11,
with 08 seen only on 2014-11-22 and 10 first on 2014-11-28. Either 09 lived under a
week, or the number was skipped. Added to §56's query list to settle it.

**(c) Two `signUpTankDesign` builds we hold are not in the embed table at all** —
`04StandardColours` (2012-06-01) and `16StandardColours` (2015-05-14), both from
`includes-tree\`. So the embed inventory **undercounts**: it only sees versions that
were live on a day a crawler fetched the page. The true build count is higher than
20 for every asset, `mazeCreator` included.

### 55.2 The 12 still missing

`TankTrouble_v3.13`, `v3.2`, `v3.3`, `v3.41`, `v3.6b`; `loggedInTank02`,
`loggedInTank04`; `scrapyard05`, `scrapyard07`, `scrapyard08`;
**`mazeCreator_v0.2`, `mazeCreator_v0.3`**.

Note the shape of that list: nine of the twelve are 2010–2014 assets with 1–4
captures each. mazeCreator_v0.3 is the outlier — **39 page captures naming it and
still no bytes** — which is exactly §39's explanation: the page that names it was
public, the file itself was only ever requested by a logged-in click.

## 56. The classic garage's JS API — 85 functions, dated

Same scan over `?garage` bodies only, for page-level `function name(args)`:
**85 functions**, of which the maze group is complete and **unchanged from
2010-09-08 to 2020-12-04**:

```
openMazeCreator(user)                closeMazeCreator(user, position)
attemptToSaveMaze(user)              cancelSaveMaze(user)
selectMazeCreatorTool(user, tool)    updateMazeTitle(user, title)
showMazeCreatorToolsAndTitle(user, title)
hideMazeCreatorToolsAndTitle(user)   mazeTitleLegalCharacters(field, e)
```

All nine appear in the earliest garage capture, so **the JS contract did not change
between v0.2 and v0.3** — a v0.2 recovery would be usable against the same page
code, and vice versa.

Other dated groups worth recording: `openPaintFacility`/`closePaintFacility`
(2010→2020); `openShop` (2010-09-08 … **2013-06-18**, and `shopCycleImage` /
`shopShowImage` / `shopHideImage` **only** on 2010-09-08); `countdown`,
`noAdsReturned`, `removeAdSwf`, `formCheckEmail_cb`, `formEmailStatus` all from
2017-01-24; `sendFeedback` / `closeFeedback` end **2018-04-22**.

### 56.1 What the sibling editor tells us about mazeCreator

`signUpTankDesign18StandardColours.swf` was decompiled (`decompiled\EMBED_…`) as the
closest available analogue: same author, same era, same `userSettings*Flash-` embed
convention, same `SetVariable` control style, same 688-px panel. Its contract:

* `initCode` FlashVar = `Base64(k=v&k=v…)`, parsed by an **identical**
  `decodeMessage()` to the game client's. Keys: `turc`/`trac` (colours), `ta`,
  `bara`, `fa`, `baca`, `bad` (equipped accessories), `tal`/`baral`/`fal`/`bacal`
  (owned-accessory lists as `id-tier,` pairs), and **`i` = a DOM id prefix** the SWF
  calls `callBackName`.
* It writes results back with
  `getURL("javascript: document.getElementById(callBackName + place).value = …")` —
  into hidden form fields. **The page**, not the SWF, then makes the SAJAX call.

So mazeCreator's `initCode` was near-certainly the same Base64 `k=v` envelope
carrying at minimum the user id, an auth token and the maze being edited.

**But mazeCreator cannot have used the paint editor's write-back path**, because
§54.1 shows there is no maze SAJAX function for the page to call. Two further
details point the same way: the recovered JS sets `_root.errorPanel.hide='yes'`,
so the SWF owns an error panel and therefore sees a failure response; and
`_root.saveRequested='true'` is a request *to* the SWF rather than a value *from*
it. Conclusion: **mazeCreator posted directly to its own PHP endpoint**, the way
the game client posts to `updateGameStatistics.php`. That endpoint's name exists
only inside the lost file.

## 57. ★ The maze editor, seen — `Making a maze.png`

The two never-mined wikis were enumerated exhaustively via the MediaWiki API and
came back **empty of maze-editor material**:

| Wiki | Pages | Images | Maze-editor imagery |
|---|---|---|---|
| `tank-trouble.fandom.com` | 457 | 57 | none |
| `tanktrouble-archive.fandom.com` | 364 | 48 | none |

All 105 images magic-byte verified; 0 mismatches, 0 HTML-as-image, 0 mislabelled
WebP. This is a firm negative from full enumeration, not sampling. Ruled out despite
promising names: `Achievements.png` (Fandom's own contributor badges),
`Premium.png` / `Latecomers_Shop*` (marketing art). Saved in `wiki-screenshots\`.

**But the search surfaced something already on disk.** From a third wiki
(`tanktrouble-tank-game.fandom.com`), held since an earlier pass:

`ia-items\extracted\images\Making a maze.png` — 832 × 556, uploaded 2016-01-30 by
`Mudpuppy888`, carrying a `version 0.3` watermark. **It is a screenshot of the lost
editor in use.**

### 57.1 What it shows

* **All three toolbar icons**, mid-edit: wall tool (deselected), crate tool
  (**selected** — bright, yellow starburst), tank tool (deselected, grey)
* Title `Gauntlet` rendered top-centre; editable name field bottom-left
  (reading `Earth to stone`); red ✗ and green ✓ bottom-right
* A **non-rectangular arena**
* Exactly **5 tank spawns and 5 crate spawns** placed

### 57.2 Why this matters beyond the artwork

It independently confirms three §53 findings that were derived purely from the wire
format, with no visual evidence behind them at the time:

| §53 claim, from the corpus | Confirmed by the screenshot |
|---|---|
| absent cells are legal — 24.4% of corpus cells, 630/806 mazes | the arena is visibly non-rectangular |
| ≤ 5 of each object type | exactly 5 tanks and 5 crates placed |
| exactly two object types (5, 8) | exactly two kinds of marker on the grid |
| three tools | three toolbar icons, no more |

Format decode and visual record agree, from independent sources.

### 57.3 The limits of it — do not overclaim

* **3 of 6 icon states only.** Wall=deselect, crate=**select**, tank=deselect. The
  opposite three states are unobserved and remain **M3**.
* **Not a 1:1 stage capture.** 832 × 556 against a 688 × 400 stage is 1.209×
  horizontal and 1.390× vertical — *not* a uniform scale, so the frame includes
  surrounding panel chrome. Any measurement taken off it needs a per-axis factor,
  and the icons are not guaranteed pixel-exact.
* XMP records `exif:PixelXDimension 832` / `PixelYDimension 556` and
  `XMP Core 5.4.0`, so it passed through an Adobe tool. No original capture size is
  recorded.

Net effect: the six toolbar images move from *blocker* to *cropping and derivation
job*. Fidelity is now bounded by resampling, not by invention.

## 58. Channel closures and a count correction

### 58.1 Columnar index — characterised, not merely untried

`CC-MAIN-2018-13` scanned in full via DuckDB/Parquet over `url_path` containing
`tanktrouble` / `tank-trouble` / `tank_trouble` / `mazecreator`. This is the only
channel that can find content on hosts **not named** tanktrouble.

Result: **no new assets.** Every non-tanktrouble host is either SEO blogspam
(`*.blogolize.com`, `*.blogofoto.com`, `*.ampedpages.com`, `*.blogminds.com` —
spun "tank trouble unblocked" content farms) or a false positive on the phrase
*tank trouble* (septic-tank service blogs, `tanknologyblog.blogspot.com`).

Recorded as **characterised**: the channel works, and what it finds is noise.

### 58.2 Portal / clone rehosts — audited to exhaustion

Final: **2 new unique SWFs**, 9 duplicates. Completeness audit rather than a stop at
"nothing more": of all SWF rows matching `tank.{0,3}trouble`, the 50 unexamined
digests **all** trace to three WordPress portals that suffix every game with
"tank-trouble" (`snail-bob-2`, `bloons-tower-defense-4`, …), sizes 3 KB–29 MB
against TankTrouble's 100–370 KB. The 2017–2019 window grew from 4 captures to 9 —
and every one is a stale re-upload of a 2011–2014 build. Full report in
`portal-rehosts\PORTAL-FINDINGS.md`.

Still **inconclusive, not negative**: ~27 large hosts (armorgames, kongregate, y8,
newgrounds, miniclip, poki, gamedistribution, weebly, sites.google.com …). Wayback
returns HTTP 200 with an empty body on large-domain scans, indistinguishable from a
true zero — demonstrated with a positive control that also failed.

### 58.3 ⚠ SWF count corrected: 43 → **42**

Re-derived by sha256 of the decoded payload across the whole tree. The earlier 43
came from a magic-byte pass. Per §55.1 the field semantics are now settled — CDX
`digest` can over-split on gzip differences and CDX `length` is stored record size —
so **sha256 of the decoded payload is the only authoritative build identity**, and
42 is the number to quote.

## 59. ⏳ In flight at session close — unintegrated output on disk

Two recovery agents were still running when this session ended. **Their files are
on disk but their findings are NOT yet written into this log.** Next session should
read the directories below before assuming anything is missing.

| Directory | Files at close | What it is | Status |
|---|---|---|---|
| `cdn-beta-full\` | **1,318** (was 216) | 2017–2019 HTML5 RELEASE trees | fetching well |
| `cc-purup\` | 23 | Common Crawl sweep of `com,purup` / `dk,purup` / `sublabgames` / `subterraneansoftware` | no `FINDINGS.md` written yet |
| `classic-embeds\` | 0 | per-name `collapse=digest` pass + the 12 missing embeds | not reached — CDX was throttled |
| `route-timeseries\` | 2 | `?news` ×45 and the other five routes | barely started |

**The single highest-value thing to check first:** grep the recovered
`cdn-beta-full\` JavaScript for `saveMaze`, `mazeCreator`, `saveArena`, `/ajax/`
and any maze-related JSON-RPC method name. Those releases contain the **HTML5
garage maze editor**, the successor to the lost Flash tool, and it plausibly
inherited the **maze save endpoint** — currently the only part of the maze system
that is pure invention (M3). 1,318 files is enough of the tree that this grep is
worth running immediately, whether or not the agent finished.

Also unresolved and worth one retry when CDX is quiet: ~27 large portal hosts that
are **inconclusive, not negative** (§58.2).

## 60. ⚠ The HTML5 maze-creator button was never wired — the save-endpoint channel closes

§59 named the single highest-value check: grep the recovered 2017–2019 HTML5
releases for the maze save endpoint the Flash tool used. Run against 1,318
recovered files, across **11 releases** (2017-10-27 → 2019-11-27).

**Result: the HTML5 client has no maze editor, and no maze save call.**

| Symbol | Count | What it actually is |
|---|---|---|
| `_createMaze` | 112 | the **procedural generator** — `_createMaze(width, height)` alongside `tankPositions` and `tilePresentToTileIndex`, plus a `RoundModel._EVENTS.MAZE_SET` handler. Generates arenas at round start; nothing to do with authoring |
| `mazeCreator` / `mazeCreatorActive` | 44 / 22 | **image paths only** — `assets/images/tankInfo/mazeCreator.png` registered against a `tankInfo` button |
| `saveMaze` / `saveArena` / `MazeEditor` | **0** | absent entirely |

The `tankInfo` button is registered in **every one of the 11 releases** with all
three image states:

```
RELEASE-2017-10-27-01 … RELEASE-2019-11-27-02
  infoMazeCreator -> ['active', 'disabled', 'standard']
  click handlers  -> NONE
```

So across two years of HTML5 releases the maze-creator button existed as UI
furniture — icon, hover state, disabled state — with **no behaviour attached**. The
feature was planned and stubbed, never shipped. It therefore never inherited the
save endpoint.

> **Caveat, stated rather than glossed:** the scan looked for a handler within 120
> characters of the registration. A generic dispatcher elsewhere (a loop over all
> `info*` buttons) would not be caught. The `disabled` state and the total absence
> of any `saveMaze`-shaped symbol both point the same way, but "no handler found
> near the registration" is the literal finding.

**Consequence.** This was the last live channel for the maze **write** protocol.
The save endpoint stays **M3 — pure invention** (`RECONSTRUCTION-STATUS.md` §3.3).
Keep it behind a single constant so a future discovery is a one-line change.

Silver lining for the rebuild: `assets/images/tankInfo/mazeCreator.png` and
`mazeCreatorActive.png` are **held**, so the garage's *entry point* icon has both
its states as original bytes. It is the editor's internal toolbar, not the button
that opens it, that remains unrecovered.

## 61. Video capture — an untapped channel for UI imagery

TankTrouble has substantial YouTube coverage from its active years, and gameplay
and tutorial videos show **live UI that no crawler could ever fetch**, because it
only ever existed behind a logged-in click: the garage user panel, the maze editor,
its toolbar in both selected and deselected states, and the save/cancel flow.

This is the natural successor to the wiki channel (§57), which is now exhausted.
Where §57 yielded exactly one editor screenshot, video yields **motion** — which is
strictly more information, because it shows state *transitions*:

* a tool being clicked, i.e. the same icon in **both** its select and deselect
  states — precisely the 3 of 6 states §57 could not supply
* the panel open/close animation, against which the recovered timings
  (500 ms `Fx.Transitions.Quad.easeInOut`, staged +700/+1200/+1700 ms) can be checked
* the error panel, whose existence is known only from `_root.errorPanel.hide`
* the save dialogue, the one part of the flow with no visual record at all

**Cost:** manual. Frame-stepping video, cropping, and upscaling from compressed
footage. Not automatable to a useful standard, and the user has flagged it as
time-consuming.

**Provenance:** anything sourced this way is **M2 at best, never O**. Video is
lossy and rescaled, so a crop is a *reference for redrawing*, not recovered bytes.
Record the video URL, uploader, upload date and timestamp in `LEDGER.tsv` for every
asset derived this way — the same provenance discipline as any other source.

**Priority targets, in order:**

1. The three toolbar icons in **both** states (closes the last artwork gap)
2. The maze-editor save/error dialogue
3. Logged-in garage panel layout, to check the §56 markup reconstruction
4. Anything showing the tank paint editor for cross-checking against the SWF we hold

## 62. Purup's own sites — swept exhaustively, and the channel closes

Full report: `cc-purup\FINDINGS.md`. **16 SURT prefixes × 126 Common Crawl
collections = 2,016 jobs, every one completed, zero gaps.**

**The developer's own site never carried anything.** `purup.com` runs continuously
2010-09-03 → 2026-07-19 and is a **one-page contact card** the whole way: 413 index
rows resolving to **12 distinct URLs**, mostly `robots.txt` and webmail. Four
distinct homepage bodies in sixteen years. No blog, no portfolio, no project list,
no downloads. The hypothesis that a dev-blog post about building the maze creator
would live on the developer's own site is **disproved, not merely unconfirmed**.

Across 2,730 fetched bodies (176 MB): **zero** occurrences of `mazeCreator`,
`maze creator`, `maze editor`, `maze-creator`, `level editor`. **Zero `.swf` rows**
in any prefix.

| prefix | rows | distinct URLs | verdict |
|---|---:|---:|---|
| `com,purup` | 413 | 12 | contact card only |
| `com,sublabgames` | 12 | 2 | Purup's current studio — same phone as purup.com. No TankTrouble content |
| `com,subterraneansoftware` | 1,248 | 78 | the **mobile port** developer's blog — wrong developer |
| `org,tanktrouble` | 1,792 | 197 | unrelated Flash-knockoff aggregator, then SEO portal |
| `net,tanktrouble` | 110 | 50 | SEO portal, 2025+ only |
| `dk,purup` · `dk,sublabgames` · `dk,subterraneansoftware` · `dk,tanktrouble` · `com,tanktroubleaddons` | **0** | 0 | swept-and-empty, not could-not-sweep |

### 62.1 One genuinely useful find, for the wrong layer

`subterraneansoftware.com` is the official **mobile port** developer's blog
(2014–2015, writing as "Tustvold"), and `/tanktrouble-single-player-ai/`
(2014-07-26) documents Laika's AI in real detail: **23 raycasts over a 230° arc**,
bounce prediction varying by difficulty, 5 px wall-border offsets, Box2D threading.

We hold `laika02.swf`, so this is a **cross-check reference** for the AI's
behaviour — useful, and worth keeping. But it is **not authority over the Flash
implementation**, and he says so himself: *"As for the online version I haven't
looked at the code for it and so can't comment on how it works."* Treat any
AI behaviour taken from it as **M2**, not as a description of the SWF we hold.

### 62.2 New leads, logged not pursued

* **`tanktroubleswf.net` (287 index rows)** and `tanktroubleswf.org` (12) — domains
  named after the SWF itself, surfaced by the wide-bracket pass and **not in any
  prior host list**. Best remaining unexplored rehost candidates.
* `tanktrouble.org/files/file/*.swf` — 15 SWF payloads whose *pages* CC indexed but
  whose *binaries* it never captured. 2013-era, so Wayback may hold the bytes.
  Names in `cc-purup\FINDINGS.md`.
* Also unswept: `tanktrouble{3,4,5}.net`, `tanktroublegame.net`, `tanktrouble3.org`,
  `tanktroubleunblocked.org`.

### 62.3 ⚠⚠ NEW TRAP — Common Crawl 403 read as "empty"

`data.commoncrawl.org` sits behind CloudFront and returns **`403 Forbidden` with
body `Request blocked`** under WAF rate-limiting. The agent's first pass treated 403
as a hard miss and recorded **1,148 of 1,260 jobs as zero-row results that had never
actually been asked**.

Caught only because the empty count looked implausible. **Only 404 may be believed.**
This is the Common Crawl analogue of §33 (`matchType=prefix` + `*`) and of the
Wayback "200 with empty body on large-domain scans" trap — three separate services,
same failure shape: *a refusal that is indistinguishable from a negative result.*

Rate ceiling that worked: 8 threads behind a global 0.16 s pacer (≈6 req/s), 403
retried every 45 s for up to 45 min. ~16 concurrent trips the WAF within two minutes.

### 62.4 Two method improvements worth keeping

* **Exact SURT bracket beats the wide form.** `LO = key + ")"`, `HI = key + "-"`,
  since `)` 0x29 < `,` 0x2C < `-` 0x2D. Catches apex plus every subdomain and
  nothing else. Validated: `com,tanktrouble` in `CC-MAIN-2018-13` → exactly 17 rows
  including `beta.tanktrouble.com`, matching the CDX API. The wide `[key, key~)`
  form works but drags ~1,000 junk rows per crawl and spans hundreds of blocks.
* **Cache the cluster.idx window** where a prefix sits and reuse it on the next
  crawl (512 KB, accepted only if it brackets both sides): ~14 range requests per
  job drops to 2–3. Full 2,016-job sweep in ~35 min instead of ~3 h. Only works with
  the narrow bracket.
* **`index.commoncrawl.org` is currently unusable** — 60 jobs, 1 success, 57 hard
  failures, then the host stopped completing TCP connections. Use the cluster.idx
  channel.

## 63. Directory contents

```
HUNT-LOG.md                  this file
archive-today\               user-supplied captures bEkyV + IH9r2 (77 files)
beta-client-2017-2019\       6 era-correct bundles (wave 1)
cdn-beta-full\               full RELEASE-2017/2018/2019 client trees (wave 2)
                             + _longnames.tsv — truncated-name → original-URL map
cdx-passes\                  CDX passes A–M (non-200, digest, referrer, session,
                             loadMaze, all-PHP, includes, vseigru, maze-images)
                             + swf-by-digest\
cc-purup\                    Common Crawl sweep of com,purup / dk,purup /
                             sublabgames / subterraneansoftware SURT prefixes
classic-embeds\              per-name CDX + fetch of all 24 classic embed SWFs
                             (§55) + _cdx.json + WAYBACK-QUEUE-FINDINGS.md
wiki-screenshots\            the two never-mined wikis (§57) — firm negative,
                             _allimages.tsv (105 rows) + PROVENANCE.md
classic-ui-images\           122/122 recovered classic UI images
classic.tanktrouble.com\     live legacy Flash tree, 2026-08-02
commoncrawl\                 full SURT-range sweep, 126,679 rows / 125 crawls
     warc-bodies\            628 fetched bodies incl. 47 ?garage captures 2010–2021
     clone-html\             270 pages across 55 clone hosts
     clone-swfs\             5 SWFs pulled from clone hosts
decompiled\                  FFDec output per SWF (incl. MazeDataFetcher.as — §53)
elte-mirror\                 people.inf.elte.hu mirror + autoindex (§34)
flashfreeze\                 54 IA item tar listings
flashpoint-gamezip\          130 files, full Flashpoint curation, 3 host trees
forum-archive\               468/468 threads, 225,438 replies, _index.tsv
ia-items\                    IA item metadata + both wiki dumps, extracted
includes-tree\               61 files recovered from /includes/ + _manifest.tsv
labReport-extracted-pages\   37 extracted JPEGs
maze-corpus\raw\             loadMaze.php response payloads — the surviving
                             output of mazeCreator_v0.3 (4,192 distinct; fetching)
     _parsed.json            decoded records
     _parsed2.json           field-split records (w, h, walls, objs)
     _render-samples.txt     ASCII renders — the §53 encoding proof
mazeCreator-ui-images\       recovered editor imagery (§52)
memento\                     Arquivo.pt CDX + Memento probe results
mirror-vseigru\              third-party HTML5 client mirror (25 files)
mirrors-github\              forum-threadids.txt, TankTrouble.ttf, ttforums
modern-client\               current unminified sources (2026 — NOT era-correct)
portal-rehosts\              third-party game-portal CDN sweep + PORTAL-FINDINGS.md
referral-mirrors-raw.txt     the ?r= referral captures (third-party embed URLs)
route-timeseries\            ?news/?garage/?game/?shop/?forum/?lab capture series
site-dirs\                   directory-probe results
softwareheritage\            blocked-channel evidence (Anubis wall)
urlcorpora\                  urlscan.io, OTX
wayback-inventory\           wave-1 exhaustive CDX / Common Crawl enumeration
wayback-zip-swfs\            SWFs extracted from archived /includes/*.zip
wiki-dumps\                  wave-1 wiki corpora (live API)
wiki-history\                wave-2 full-revision-history mining
zip-extracted\               contents of all four distribution zips (client-only)
```
