# Visual evidence wanted

Standing request log — covers BOTH already-rebuilt pieces AND future
work not yet built (garage UI, paint editor, sign-up flow, forum, shop,
statistics, sounds…): gathering evidence BEFORE a rebuild starts beats
overhauling after. Rule: when a visual (existing or planned) cannot be
deduced with enough accuracy from held evidence, or it is a vital
user-facing interface, an entry lands here with (a) what is needed,
broadly, (b) specific details/references to hunt for, (c) what it would
replace or confirm.
Sources that work: YouTube footage from the active years (2010-2018 —
frame-step, crop; provenance **M2 at best, never O**), old screenshots,
community archives. Record video URL, uploader, upload date, and timestamp
in LEDGER.tsv for every asset derived this way (guide §6.5).

## THE OVERHAUL RULE

Every manually created (M2/M3) visual, animation, interaction model, or
copy text in this rebuild is a **placeholder pending evidence, not a
finished artifact**. When new evidence arrives — footage, a cleaner
screenshot, a community archive — showing how something actually looked,
moved, or behaved:

1. **Rewrite the affected piece fully against the evidence. Do not patch
   the invention to be "close enough".** The invented version has zero
   authority; it exists only so the site runs end-to-end. If the evidence
   shows different geometry, different animation curves, different copy,
   different interaction — the invented implementation is replaced
   wholesale, and its tests re-pinned to the evidence.
2. This applies to whole files, not just constants: an M2 SWF whose real
   appearance surfaces gets rebuilt against the footage, not tweaked.
   The `.provenance` sidecars carry the same commitment.
3. Archive the evidence first (read-only discipline), LEDGER row with
   URL/uploader/date/timestamp, then overhaul, then record the
   supersession in DECISIONS.md (what the invention was, what the
   evidence showed, what changed).
4. Gates keep the floor: byte-level gates (round-trip, replay, contract
   tests) must stay green through any overhaul — evidence changes pixels
   and behavior, never the wire format.

Status values: `WANTED` / `PARTIAL` (some states held) / `FETCHED` (evidence
in archive, redraw pending) / `DONE`.

---

## mazeCreator (phase 3 rebuild shipped from deduction — every entry below would upgrade it)

### 1. Tool icon states — PARTIAL, high value
Page-side JPGs, never captured: `images/mazeConstructTool{S,Des}elect.jpg`,
`images/crateSpawnTool{S,Des}elect.jpg`, `images/tankSpawnTool{S,Des}elect.jpg`
(srv/index.php:3732-3734). The screenshot
`archive/ia-items/extracted/images/Making a maze.png` holds 3 of 6 states:
wall=Deselect, crate=**Select**, tank=Deselect. Needed: the opposite three.
Video of someone CLICKING a tool gives the same icon in both states in
adjacent frames — ideal shot: any maze-editing footage where the toolbar is
visible while tools change.

### 2. Editor error panel — WANTED, vital user-facing
Known ONLY from `_root.errorPanel.hide` (srv/index.php:3706,3721). No
capture, no screenshot, no copy text. Phase 3 invented a dark rounded box +
copy ("Please give your maze a name." etc — DECISIONS 2026-08-03). Needed:
any frame showing the panel — likely triggers in footage: user hits the
green ✓ with an empty/duplicate name, or server rejects. Also wanted: the
exact wording, font, position, whether it animates.

### 3. Save flow / dialogue after ✓ — WANTED
What the SWF showed between "✓ clicked" and "tools hidden" (page evidence:
SWF calls `hideMazeCreatorToolsAndTitle` only on success). Spinner?
Instant? Confirmation flash? Any footage of a successful maze save.

### 4. Maze preview / garage mode — WANTED, vital user-facing
The SWF's boot state before editing (`previewLoaded` SetVariable, page
comment "display maze previews"). Phase 3 renders the saved maze +
click-anywhere-to-edit as a minimal stand-in. Needed: what the preview
actually looked like — multiple slots? thumbnails? "create new maze"
affordance? Any logged-in garage footage showing the maze panel BEFORE the
user starts editing.

### 5. Editing interaction semantics — WANTED, changes behavior not pixels
Phase 3 invented: click cell = toggle floor, click edge between floor
cells = toggle wall, click with spawn tool = toggle spawn. Unknown: did the
original drag-paint? preview walls on hover? show a cursor ghost? Footage
of someone actually drawing a maze answers all three in seconds.

### 6. Maze placement rule — PARTIAL
Screenshot shows the 13×8 maze centered with HALF-cell precision
(bbox left 137.2 stage px = lattice 56 + 2.5 cells). Phase 3 snaps to
integer cells so the editing lattice stays fixed. Footage of a maze
growing (cells added at the edge) reveals whether the original re-centered
live or kept a fixed lattice.

### 7. Title + watermark typography — PARTIAL
"Gauntlet" title (#666666, ~18px) and "version 0.3" watermark measured
from one upscaled screenshot; face unknown (rebuild uses `_sans`).
A cleaner capture or any frame at native scale would pin the actual font
(era site chrome used Verdana/Arial family).

### 8. Fade transitions — PARTIAL
15 frames @ 25fps is O evidence (srv/index.php:3637 comment). Unknown:
linear alpha vs eased. Any open/close footage of the maze creator panel.

### 8a. Floor tone pattern — WANTED
Editor floor is a per-cell mix of #dddddd/#eeeeee, ~1/3 light, no
deterministic rule fits the screenshot (not parity, not rows/columns).
Rebuild uses a fixed hash. Two different frames of the SAME maze would
settle it instantly: identical tones = deterministic function (then
derivable); different tones = runtime random (rebuild hash is then a fair
stand-in). Any footage showing one maze twice (reopen, or before/after an
edit elsewhere).

## Older / other routes

### 9. Tank paint editor icon states — WANTED (same JPG family, phase 4+)
`images/userpanel*Paint*.jpg` states referenced by the paint flow; same
video-frame technique applies when that milestone opens.

### 10. Selected-state nav tabs for news / shop / forum — PARTIAL, era-inferred
`images/tab2Select.jpg` (news), `tab4Select.jpg` (shop), `tab5Select.jpg`
(forum) have a CDX gap 2015-03 to 2019-09 — the 2017-2018 window never
captured them, so all three ship as **O?** on a timeline argument
(`tools/asset_judgements.tsv`; DECISIONS 2026-08-04): the nav strip is
versioned as a set, siblings date the strip-wide change to 20181218, and
tab3/tab6Select prove no further change until Dec 2019. Needed to upgrade to
O: any in-era capture of `/?news`, `/?shop` or `/?forum` — or of those three
image paths — with the tab strip visible. A frame of era footage showing a
raised NEWS/SHOP/FORUM tab would also confirm the artwork by eye.

---

# Full sweep inventory (2026-08-04)

Repo-wide sweep for everything content-recoverable — already-rebuilt AND
not-yet-built. Items S1-S114, own numbering (entries 1-10 above NOT
repeated). Line refs are `srv/index.php` absolute lines; the file repeats
each route's JS, so garage-route copies are cited (3374-5950) where the
code is garage-only.

Recoverability key: **HIGH** = any ordinary gameplay/front-page video;
**MED** = needs logged-in footage; **LOW** = rare moment / rare era / may
not exist.

## Highest-yield single shots, ranked

1. **One logged-in session walking all six tabs** (S113) — collapses ~25
   unknowns at once.
2. **A slow full-page scroll of `?news`, any year 2015-2018** (S78) —
   recovers 30+ known-lost images plus poll bars and the closed stamp.
3. **A garage session: open paint → open maze editor → save** (S24-S48 +
   entries 1-5 above) — the two biggest reconstructed surfaces at once.
4. **A forum thread view with mixed bubble colours** (S57-S63) — the only
   way any forum pixel is ever recovered.
5. **Front-page hover passes: nav tabs, Top-10 names, feedback envelope**
   (S2, S4, S11, S19) — cheap, three are currently pure guesswork.

## A. Game-page chrome (root `/`, `?game`)

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S1 | **Tagline rotation pool completeness** | flow / typography | M1 reconstruction picks uniformly from **10** observed strings; pool completeness unknowable | `srv/index.php:167-182` (`tt_tagline_line`) | Read the grey line under the logo across many videos; an 11th string breaks the pool | HIGH |
| S2 | **`tabNSelect2.jpg` alternate nav strip** | icon-state | `tab2/3/4/6Select2.jpg` held **O** but referenced by nothing; `tab1/5Select2` absent. Second selected-state generation, hover state, or dead art? | `srv/images/` vs zero refs in index.php | A nav tab *moused over but not clicked* — if raised art changes on hover, that is these | MED |
| S3 | **Top-10 "Friends" tab, logged-in** | page-look | Only the logged-out "must log in" string captured; logged-in table (header flips to "Top 10 Exp.") never seen | `srv/index.php:1113-1138`, `updateTop10_cb`:1146 | Logged-in user clicks **Friends** tab under the Victories box | MED |
| S4 | **Usertrail hover card** | interaction / page-look | Hover Top-10 name 1s → spinner → server HTML + 200×99 `loggedInTank06.swf`. Card markup (`x_generateUsertrail`) never captured | `srv/index.php:1301-1362`; `usertrail` div :1235 | Cursor rests on a Top-10 username >1s; frame-step spinner→card | HIGH |
| S5 | **Achievement unlock float — content** | animation / page-look | Box art + glow tween O-exact. Title/description/icon from `x_checkForAchievements` never captured; only ids {28-32,34-36} known, 1-27+33 existed unobserved | `srv/index.php:1218-1261` | Yellow glow flashes top-centre after login/round — freeze the 5s, read title+description+icon | MED |
| S6 | **Logged-in user card in login sidebar** | page-look | `x_login` HTML into `loginmessageswrapper`; 71px row height; 110×55 tank SWF. Score/rank/logout markup never captured | `srv/index.php:598-657`, `doLogout`:943 | Sidebar login on camera — hold the 500ms animation + resulting card | MED |
| S7 | **Multi-user stack (up to 3 logged in)** | page-look / flow | JS caps at 3 (`numUsers == 3` hides login box); stacked layout never captured | `srv/index.php:593-596`, `:666-681`, `:879-905` | Two/three players log in on one page (common in local-multiplayer videos) | MED |
| S8 | **Logout animation + card removal** | animation | Specified in JS (200ms fade, 500ms collapse) but never seen; confirm no confirm-dialog | `srv/index.php:943-1000` | Player clicks logout on a user card | MED |
| S9 | **Login error strip** | page-look | Error HTML classed `text tiny clearRed`; **`.clearRed` not in any held CSS**. Copy unknown except `Username rejected` | `srv/index.php:622-641`, `:790-810` | Wrong password on camera — 110px red strip animates in (300ms), out after 1500ms | HIGH |
| S10 | **`/detention` page** | page-look / flow | **Whole page unknown.** `window.open("detention","_self")` 1700ms after `Username rejected`. No ledger row, no file, no CDX | `srv/index.php:638-639` (+2224,4803,10781,12500,14049,15505) | Banned account login attempt on camera | LOW |
| S11 | **Feedback box — open state** | page-look / flow | `sendFeedback` SAJAX + removed markup block existed until (2018-04-22, 2018-05-23] — in-page form look unknown | `srv/index.php:1183-1210`; removed-block catalogue | 2017/early-2018 video clicking the "Got Feedback?" box — form expands in place | MED |
| S12 | **`ima3_preloader_1.5.swf` pre-roll + `#preloader`** | SWF / flow | Handlers reference `#preloader` which exists in no era page; SWF held O, on-screen behaviour unknown | `srv/index.php:228-240`; `srv/includes/ima3_preloader_1.5.swf` | Pre-2017 footage starting before the game shows an interstitial in the 712×490 stage | LOW |
| S13 | **Game stage slide-up transition** | animation | `#TankTrouble` at `top:60px`; page polls for `-10px`. SWF performs the move; duration/easing unknown | `srv/index.php:324-333`, `:433-443` | Click 1/2/3-PLAYER — frame-step teaser text vanish + 70px slide | HIGH |
| S14 | **Scrapyard counter in motion** | animation | Rebuild freezes after ~60s (declared divergence). Real flip cadence/roll direction unobserved | `docs/standards/DIVERGENCES-SERVED.md` §5; `scrapyard.js:104-251` | Sidebar "Scrapyard" number visible >2min — count plate flips | HIGH |
| S15 | **Pre-2017 scrapyard SWFs** | SWF | `scrapyard06/10/11.swf` held O, referenced by no era page; others known-lost (`09` inferred, may not exist) | LEDGER rows 191-198 | Pre-2017-02 footage of the left sidebar counter | MED |
| S16 | **Seasonal side-box variants never rendered** | page-look | `.box.christmas/.halloween/.glitch/.kickstarter` fully in `boxStyles.css`, used by zero captured page | `srv/includes/boxStyles.css:31-70+` | Halloween/Christmas-week front-page footage — sidebar boxes change skin | MED |
| S17 | **`Commodore` (c64) webfont in the wild** | typography | Declared + used by `.box.glitch` and two news rules; no captured page uses them | `styles.css:86-93`, `boxStyles.css:50,60`, `newsStyles.css:237,243` | Any frame with a blocky pixel-font box or news item | LOW |
| S18 | **Advent-calendar UI** | page-look / flow | 8 day-sprites held, ~16 unheld/unnamed; `AdventCalendarOverview.jpg`, `christmasPresentOpen.jpg`, `christmasDisplay.png` known-lost; commented-out login-box block places `christmasDisplay.png` | LEDGER 232,302,304; `srv/index.php:564-570` | December footage: present sprite for an unheld day; a present clicked/opened; the overview page | MED |
| S19 | **Facebook Like/Share box render** | page-look | Third-party render; `.box.fb` has no held CSS | `srv/index.php:1160-1161` | Any frame of the 120px Facebook button in the right column | HIGH |
| S20 | **`favicon.ico`** | icon-state | **79 CDX 200s, zero ledger rows, no file.** Silently absent | `DEDUCE.md:149` | Any era browser-tab frame (common in tutorials) | HIGH |
| S21 | **`expressinstall.swf` "Flash required" screen** | page-look | known-lost; named in `swfobject.js:40` | LEDGER 428 | Old footage on outdated Flash — upgrade panel in the stage | LOW |
| S22 | **`?r=` referral landing** | flow | `?r=Link%20iframe/embed`, `/spreadTheWord/` source; on-screen effect unknown | `srv/index.php:427`; `DEDUCE.md:152` | Arrival via the banner inside an embedded portal copy | LOW |
| S23 | **AdSense skyscrapers as rendered** | page-look | Two 160×600 slots ship blank by design | `docs/standards/DIVERGENCES-SERVED.md` §2 | Full-window frame — confirm layout never reflowed by ads | HIGH |

## B. Logged-in garage / userpanel — largest single hole

Everything from `x_updateUserPanels` / `x_getAllUserInfo` SAJAX. **Zero
bytes of that HTML archived**; only the JS survives (garage route,
`srv/index.php:3483-4164`).

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S24 | **The userpanel itself** | page-look | Nothing built. IDs proven: `userpanel-<user>` (224px collapsed, 692 expanded), `userpanelContent-` (99px), `userpanelswrapper` (214px). Contents/borders/tank position/name label unknown | `srv/index.php:3483-3575`, `:4117-4162` | Logged-in `?garage`: panel row fades in, grows to 214px | MED |
| S25 | **Userpanel icon strip (5 icons)** | icon-state | `userpanelPaint- / Maze- / SherifStar- / Form- / Stats-`. Filenames unknown, art unknown, each has enabled + faded state (opacity 0↔1) | `srv/index.php:3501-3552`, `:4083,4091` | One click on any icon fades the other four over 200ms — gives all five in BOTH states | MED |
| S26 | **Form icon server-chosen sprite** | icon-state | `updateFormData_cb(r) { formIconToUpdate.src = r; }` — ≥2 states (profile incomplete/complete); neither URL nor art known | `srv/index.php:4036-4040` | User completes account form, clicks accept — icon swaps sprite | LOW |
| S27 | **Sherif-star (moderator) icon + panel** | icon-state / page-look | Moderator-only; what it opens referenced nowhere else. Unknown feature | `srv/index.php:3515-3547` | Moderator opening their garage. Rare | LOW |
| S28 | **Accept "✓" buttons (4 variants)** | icon-state | `userpanelAccept{Paint,Maze,Form,Stats}-`; fades in at t=1700ms. Art/position unknown | `srv/index.php:3563,3622,3771,4055` | 1.7s after opening any garage sub-panel | MED |
| S29 | **Paint facility open sequence** | animation | Timings O-exact (700/1200/1700ms; 99→245px, 214→360px, `showCans`/`showAccessories`). Visual unseen | `srv/index.php:3554-3565` | Click paint icon — frame-step 0→2s | MED |
| S30 | **Era accessory catalogue** | SWF / flow | Only the developer DEBUG catalogue seeded (`1-1,2-1,3-1,4-1,5-2,13-3,20-4,27-5,33-6,`). Real 2017-18 accessory/badge list + toolbox grouping never captured | decompile `DoAction.as:1566-1580` | Paint facility open, accessory toolboxes **scrolled** — enumerate every sprite + box | MED |
| S31 | **Badge picker** | icon-state | `bad`/`oldBadge` field exists; artwork set + chooser unknown | same, `:1308,1347,1596` | Same shot, badge toolbox row | MED |
| S32 | **Locked/unpurchased accessory presentation** | icon-state | Loader skips `_width == 0` clips — empty frames exist. Greyed? hidden? price-tagged? | `DoAction.as:1610-1616` | Free account vs Kickstarter-backer account, same toolbox | LOW |
| S33 | **Personal stats page (`userpanelStatsPage-`)** | page-look | Panel grows to 605/720px. No field list, layout, chart. Unbuilt | `srv/index.php:4042-4056` | Click stats icon in garage | MED |
| S34 | **Account settings form** | page-look / interaction | Field ids + placeholder copy proven (`formname`, `formpassword1/2`, `formemail`, `formbirthyear`, `formcountry`, `formsubscribe`); layout, country list, year range, checkbox style unknown. 350px panel | `srv/index.php:3755-3788` | Click form icon; a shot with country dropdown OPEN | MED |
| S35 | **Email verification status line** | interaction | Strings recovered (`A verification email will be sent…`, `Verified`, `Not verified`), 200ms crossfade. Position/colour unknown | `srv/index.php:3940-3975` | Edit email in garage form, pause | LOW |
| S36 | **Garage form validation errors** | interaction | 10 exact strings recovered; which element turns `text medium red` + placement unverified | `srv/index.php:3802-3900`, `:4008` | Mistype password confirmation, hit accept | LOW |
| S37 | **Garage → maze-creator transition** | animation | Sequence O-exact (700/1200/1700ms, return 2300ms). Visual of tank card giving way to editor unseen | `srv/index.php:3609-3641` | Click maze icon; frame-step 0→2.5s + close | MED |
| S38 | **`userSettingsMazeCreatorInitCode-` fields** | flow | Rebuild invented `u,n,t,d,s`; real fields unknown | `srv/index.php:3617`; DECISIONS 2026-08-04 | Video showing *two saved mazes/slots* proves a slot field | LOW |
| S39 | **Maze-creator toolbar row (page-side)** | page-look | `userpanelMazeCreatorControls-`, title input (placeholder `Maze name`, #666→#000), save/cancel. Partially in the screenshot; chrome/spacing unconfirmed | `srv/index.php:3643-3676`, `:3737-3753` | Strip under the 688×400 stage during editing | MED |
| S40 | **`userSettingsTank-` visibility juggle** | animation | hidden at 700ms, restored on collapse. Pop or crossfade? | `srv/index.php:3617,3633,4085,4091` | Open then cancel any garage sub-panel | MED |

## C. mazeCreator — beyond entries 1-8a above

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S41 | **Editor sound effects** | sound | Rebuilt SWF has NO audio. Sibling paint editor carries 9 named sounds. Maze editor click/place/save sounds unknown | `DoAction.as:1536-1562`; `src/mazecreator/Editor.as` | **Audio:** maze-editing footage with game audio — listen for click/thunk on place + save | MED |
| S42 | **Cursor over the editor stage** | interaction | Rebuild leaves system cursor. Custom cursor / tool ghost possible | VE #5 covers semantics, not cursor art | Editing footage where recorder captures the cursor | MED |
| S43 | **Multiple maze slots** | flow | `s` observed only as 1 across all 842 payloads. Slot picker existence unknown; rebuild invents `badSlot` | DECISIONS "mazes remodel"; `saveMaze.php` | Garage maze area BEFORE editing — count thumbnails/slots | MED |
| S44 | **Deleting / clearing a maze** | flow | No delete path in page JS or wire format. May not have existed | absence in `srv/index.php:3609-3753` | Player replaces an existing maze — lingers? cleared? overwritten? | LOW |
| S45 | **Unsaved-changes warning on ✗** | flow | O source: `//TODO: Ask the flash to check if a warning should be displayed` — shipped build likely had none; confirm | `srv/index.php:3719` | Click ✗ with unsaved edits — confirm nothing appears | MED |
| S46 | **Garage maze-icon art** | icon-state | Held `mazeCreator*.png` files belong to the HTML5 client tree; classic `userpanelMaze-` icon is a different unrecovered asset | `archive/mazeCreator-ui-images/` | Same shot as S25 | MED |
| S47 | **`mazeCreator_v0.2.swf` (2010 editor)** | SWF | known-lost, one CDX sighting 2010-09-08. Look/tools unknown | LEDGER 182; `DEDUCE.md:208-211` | 2010-2011 garage footage — different tool count / no watermark | LOW |
| S48 | **Editor behaviour at limits** | interaction | Limits from corpus stats, not observed UI. How the 6th crate was refused (greyed? shake? panel?) unknown | DECISIONS 2026-08-04 item 1 | Someone tries a 6th tank/crate or 19-wide maze | MED |

## D. Paint / tank editor (`signUpTankDesign*`)

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S49 | **Lost builds 01/09/11** | SWF | known-lost, CDX names only. Held: 04,13,16,17,18 | LEDGER 202,204,205 | Pre-2013 sign-up footage with older editor layout | LOW |
| S50 | **Which build live on which day** | flow | Two held builds appear in no capture; embed inventory undercounts | `DEDUCE.md:369-371` | Any dated video with the sign-up editor — layout dates the build | HIGH |
| S51 | **Spray-can shake/pop/weld animations** | animation | Inside held O bytes; no external reference to verify a Ruffle/projector render against | `DoAction.as:1530-1562` | Sign-up footage with repeated can clicks — gate-C ground truth | HIGH |

## E. Sign-up flow

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S52 | **Sign-up success screen** | page-look / flow | `signupresult` server HTML + `signedupinitcode` element never captured | `srv/index.php:4411-4446` | Completed sign-up on camera — congratulation panel + tank | MED |
| S53 | **`logInToGetStarted.gif` in situ** | animation | Held O; shown when `numUsers < 2` post-sign-up at `top:40px;left:130px`; login box flips to `box important` | `srv/index.php:4439-4445`, `:558-560` | Right after a first sign-up: arrow animates, login box turns orange | MED |
| S54 | **Password-strength bar** | animation | Scoring + 5 colours O; 4px bar, 200ms tweens. Never seen rendered | `srv/index.php:4517-4609`, bar `:4187` | Typing a password in sign-up — coloured sliver grows | HIGH |
| S55 | **Server-side sign-up rejections** | interaction | 13 exact strings recovered; rendering confirmed only for client-side siblings | `srv/index.php:4338-4410` | Someone picks a taken username | MED |
| S56 | **`/verification/` landing** | page-look / flow | Pairs with `sendVerificationEmail`; 4 pre-era CDX 200s; no file, no row | `DEDUCE.md:158` | User clicks verification link from email | LOW |

## F. Forum — second-largest hole (100% SAJAX-rendered)

Era-final `?forum` = `<div id="forumwrapper"></div>` only. No archived
rendered forum HTML exists at all.

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S57 | **Thread-preview list (page 1, 20 items)** | page-look | Nothing. Only call shape `x_showForumPreviews(1, 20, …)` known | `srv/index.php:12044-12048` | Open `?forum` in any video — list fades in ~1s after load | HIGH |
| S58 | **Speech-bubble post rendering** | page-look | 9-slice bubble, left/right pointers alternating, 3 colour variants (default, `.grayBubble` #cccccc, `.yellowBubble`). Meaning of gray/yellow unknown | `srv/includes/forumStyles.css`; `srv/index.php:12303-12307` | Thread view with a greyed + a yellow bubble visible | HIGH |
| S59 | **Per-post tank render + scale** | page-look | `forumTank-<name>` embeds tank SWF at `110×scale` — scale varies per user (rank-linked?) | `srv/index.php:12071-12082` | Thread view — compare tank sizes between posters | HIGH |
| S60 | **Post fade-in stagger** | animation | O-exact: 75ms × index, 200ms linear each | `srv/index.php:12084-12107` | Frame-step first second after forum load | HIGH |
| S61 | **New-thread form** | page-look / interaction | ids + placeholder `Discussion header` + 2 error strings known; look unknown | `srv/index.php:12187-12242` | Starting a thread, ideally submitting empty header first | MED |
| S62 | **Reply form** | page-look / interaction | `forumcommenttextarea`, `forumcommenterror` | `srv/index.php:12244-12264` | Replying in-thread | MED |
| S63 | **Inline edit + bounce** | animation | On save, bubble height animates `Bounce.easeOut` 1500ms — distinctive | `srv/index.php:12136-12165`, `:12266-12286` | User edits own post — bubble springs | MED |
| S64 | **Moderation controls** | icon-state / interaction | 8 endpoints (`setDisable/Delete/Approve/Ban/CloseThread/…`) with zero UI evidence; `forumHideTrail()` implies a hover trail | `srv/index.php:12167-12185` | Moderator footage. Forum-drama videos 2013-2018 | LOW |
| S65 | **Thread filter** | interaction | Literal `'all'` proves a filter with other values; control unrecovered | `srv/index.php:12241,12263` | Dropdown/tab row above the thread list | MED |
| S66 | **Pagination** | interaction | `firstPreview/lastPreview` args prove paging (size 20); control art unknown | same | Bottom of a listing / long thread | MED |
| S67 | **Scroll-to-top after posting** | animation | `Fx.Scroll(window, {duration: 3000}).toTop()` — very slow, easy to spot | `srv/index.php:12050-12055` | Reply posted, page glides up over 3s | MED |
| S68 | **`forumAllUserInfo` hidden block** | flow | Hidden per-user initCode container; never captured | `srv/index.php:12063,12291` | Not visible; inferable from S59 | LOW |

## G. Shop

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S69 | **Live classic shop (`showShop`)** | page-look | Removed (2017-03-30, 2017-04-29]; era `?shop` = closed notice. `shopStyles.css` (O) proves rich card layout (224px items, priceTag dollar/cent, showmore, purchaseOptions). No rendered instance archived | `srv/includes/shopStyles.css`; `srv/index.php:15308-15313` | 2015-early-2017 `?shop` footage — card grid + a "show more" expand | MED |
| S70 | **Shop item photography** | page-look | 9 product PNGs held; `shopCollection00.jpg`, `hoodies.png`, `newStamp.png` known-lost | LEDGER 318,338,392 | Same shot — `newStamp.png` is a per-item "NEW" overlay | MED |
| S71 | **Purchase / PayPal flow** | flow | `payPal.gif` held, referenced by nothing served. Checkout unknown | `srv/images/payPal.gif` | Shop video reaching the purchase options row | LOW |
| S72 | **`/shop/` directory (≠ `?shop`)** | page-look | 501 stub, filename convention-inferred | LEDGER 222 | Address bar reading `tanktrouble.com/shop/` in-era | LOW |

## H. News

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S73 | **Open-poll UI (`poll-N-options`)** | page-look / interaction | Every archived poll is closed. Pre-vote option rows appear in NO archived byte | `srv/index.php:6066-6094` | 2011-2018 news footage during a live poll | MED |
| S74 | **Vote-registered animation** | animation | Exact: options fade 200ms → `Your vote was registered` → `Bounce.easeOut` 1500ms → results fade | `srv/index.php:6075-6103` | Logged-in user clicks a poll option | LOW |
| S75 | **Poll bar sprites (9 files)** | icon-state | `pollBar{Green,Yellow,Red}{Left,Middle,Right}.jpg` all known-lost — results render broken | LEDGER 374-382 | Any poll result frame — 3 colours × 3 slices in one shot | HIGH |
| S76 | **`thisPollIsClosed.png` stamp** | icon-state | known-lost; `top:-10px;left:480px` over the question | LEDGER 420; `srv/index.php:6112` | Same frame as S75 | HIGH |
| S77 | **Poll illustration images** | page-look | known-lost: `pollKickstarterCrates.png`, `sixCrates.jpg`, `fourCrates.jpg`, `nextWeaponSketches.jpg`, `laikaSmall.jpg`, `mouseControl.jpg` | LEDGER 313-394 | News-page scroll — these sit left of each poll's bars | HIGH |
| S78 | **Remaining known-lost news imagery (~30 files)** | page-look | `300000000.jpg`, `androidIngame.jpg`, `anniversaryCake.png`, `busyMaze.png`, `dimitrisDeathRay.jpg`, `greetingsFromTheBahamas.png`, `halloweenSwag.png`, `iPhone1.0.0.jpg`, `kickstarterCrates554x227.png`, `polaroidDonut.png`, `researchFacility.jpg`, `timeMagazine1963.png`, `visits20150107.png`, … (full list: `tools/asset_choices.tsv` 69 unobserved + 5 weak-candidate) | LEDGER 229-424 | **One slow `?news` scroll circa 2015-2018 captures dozens — highest-yield single shot** | HIGH |
| S79 | **Tick/cross sprites** | icon-state | `v.jpg`/`x.jpg` held, `formV.jpg`/`cross.jpg` known-lost; usage sites unconfirmed | LEDGER 307,312 | Any form-completion checkmark on screen | MED |
| S80 | **News social-share widget** | page-look | Appears only in later captures; appearance date unknown | DECISIONS "news is verbatim blobs" | Compare 2016 vs 2018 news items on video | MED |
| S81 | **News markup generations (news/news3/news4)** | page-look | Three generations coexist; which was live when only partly datable | same | Dated news footage across years | MED |

## I. Statistics / Lab / popup subpages — whole pages unknown (all 501 stubs)

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S82 | **`/statistics/`** | page-look | Zero era captures ("never activatable in-era"); 14 CDX 200s 2010-2017 | LEDGER 224 | Video clicking through to stats from `?lab` (link gone by 2017-12-12) | LOW |
| S83 | **`/tankRanks/` popup** | page-look | 460×535 popup w/ scrollbars from `?lab`; 86 CDX 200s 2010-2015 | LEDGER 225; `srv/index.php:13854` | `?lab` ranks link clicked, small popup opens | LOW |
| S84 | **`/theLabReport/` popup** | page-look | 460×535 popup; PDFs known (vol ≤18; vol10 iss4 known-lost); browser page unknown | LEDGER 227,427; `srv/index.php:13795` | `?lab` → "Browse the archive" | LOW |
| S85 | **`/faq/index.html` popup** | page-look | 600×600 popup; **ledger row says `index.php` but page opens `faq/index.html`** — row correction needed; 72 CDX 200s | LEDGER row 10 vs `srv/index.php:1108` | FAQ box clicked in right column | MED |
| S86 | **`/tellAFriendMail/` popup** | page-look | 460×535 no-scrollbar popup; 21 CDX 200s 2008-2018 | LEDGER 226; `srv/index.php:1179` | "Tell a Friend" clicked | LOW |
| S87 | **`/spreadTheWord/`** | page-look | Stub; two banners held; page + `?r=` tracker copy unknown | LEDGER 223; `srv/index.php:13837-13841` | `?lab` banner section or direct visit | LOW |
| S88 | **`/ios/`** | page-look | Stub; 7 CDX 200s 2012-2019 | LEDGER 216 | iOS-app link followed on video | LOW |
| S89 | **`/like/`** | page-look | Stub; purpose entirely unverified | LEDGER 217 | Address bar `/like/` | LOW |
| S90 | **`/privacy/`** | page-look | Stub; text unknown | LEDGER 219 | Screenshot of the policy text | LOW |
| S91 | **`/infirmary/` success/failure states** | interaction | Page O byte-perfect but only initial state; `You will receive an email shortly.` + failure state never captured | `srv/infirmary/index.html` | Password recovery on camera | LOW |
| S92 | **`changePassword.php` landing** | page-look / flow | Stub; named only in infirmary comment which says design moved away from it | LEDGER 7 | "Change password" link from email | LOW |
| S93 | **`sendRequest.php` popup form** | page-look | Stub; infirmary comment says final design was a popup | LEDGER 221 | Password-recovery popup window | LOW |
| S94 | **`content.php`** | page-look / flow | Stub, CDX-observed only, function unknown | LEDGER 8 | Address bar with `content.php` | LOW |
| S95 | **`getimage.php` / `uploadimage.php`** | flow | Both 501; observed 200s wrong-generation; believed admin news-image uploader | LEDGER 12,228 | Dev/admin footage only | LOW |
| S96 | **`feedback.php`** | page-look | Stub; response unknown | LEDGER 11 | See S11 | LOW |
| S97 | **`achievement.php`** | flow | Stub, zero CDX rows; 6 AS2 call sites; user-visible output unknown | LEDGER 165 | See S5 | LOW |
| S98 | **`logIn.php`** | page-look | 404 by 2008; version-bump comment proves it existed as a game host page | LEDGER 218; `srv/index.php:403` | 2008-2009 footage; near-unrecoverable | LOW |
| S99 | **`/facebook/`, `/kickstarterFAQ/`, `/verification/`** | page-look | Not created — captures pre-era; `kickstarterFAQBanner.png` held O so a page rendered | `DEDUCE.md:158-161` | 2015 Kickstarter-period footage/screenshots | LOW |
| S100 | **`/explanation.html`, `/static/`, `/u/`, `/mazeCreator`** | page-look | Grade-C 404 probes — may never have existed | `DEDUCE.md:169-171` | Speculative; record any sighting | LOW |

## J. Sounds / music

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S101 | **Page-level audio (any?)** | sound | No audio API anywhere in index.php. Believed silent — unconfirmed; could hide in `loggedInTank06.swf`/`scrapyard*.swf` | grep → 0 | Audio of a front page with no game running — truly silent on hover/login? | HIGH |
| S102 | **Era game-SWF audio set** | sound | `TankTrouble_v4.0.swf` held O but decompile has scripts only, no sounds extracted. Sound names known only from v3.8c/v4.03/Newgrounds (31 files) | `archive/decompiled/` tree | 2017-2018 gameplay audio — verify era weapon sounds match the v4.03 set | HIGH |
| S103 | **`laika02.swf` behaviour** | SWF | Held O, embedded once at 140×250 in a news item; never verified | `srv/index.php:9826` | Scroll to the Laika news item | MED |
| S104 | **Scrapyard flip sound** | sound | Phaser widget silent; older SWF widgets might not be | `scrapyard.js` | Audio during a flip on a quiet page | LOW |

## K. Misc / cross-cutting

| # | Item | Category | What exists / what's missing | Evidence pointer | FOOTAGE TRIGGER | Rec. |
|---|---|---|---|---|---|---|
| S105 | **Frozen live regions — real ranges + format** | page-look | Player stats, Top-10, forum latest-posters, visit counter frozen at 20181214/18 bytes | `docs/standards/DIVERGENCES-SERVED.md` §3 | Any frame — read counters, confirm formatting stayed constant across years | HIGH |
| S106 | **Seasonal promo box rotation** | page-look | Halloween box byte-identical 2017/2018; full year-round set unknown | DECISIONS "seasonal-promo" | Front-page footage from Feb-Sep (uncaptured months) | HIGH |
| S107 | **Sign-up template swap dates** | flow | 13→17 in (2017-03-30, 2017-04-29]; 17→18 in (2018-07-22, 2018-08-14] — wide windows | DECISIONS "annotation pass" | Dated video inside either window narrows the deploy day | HIGH |
| S108 | **Editor title font: device vs embedded** | typography | Gate C attributes residual divergence to `_sans` — unconfirmed against original pixels | `oracle/DIVERGENCES.md` gate C | Native-resolution frame of editor title — AA pattern distinguishes | LOW |
| S109 | **`p2.js`** | flow | known-lost, "may never have existed" — likely crawler artefact. Listed so nobody chases it | LEDGER 187,210,430,431 | Nothing — do not chase | LOW |
| S110 | **`TankTrouble_v1.x-v3.7` builds (19 SWFs)** | SWF | All known-lost, CDX names only; v3.5/v3.6 inner SWFs sit in held zips (promotion candidates) | LEDGER 139-161 | Old gameplay videos date each build by visible UI — catches mislabelled clone rehosts | HIGH |
| S111 | **`loggedInTank02/04.swf`** | SWF | known-lost; only `06` held | LEDGER 178,179 | Pre-2013 logged-in sidebar footage | LOW |
| S112 | **IE-era layout variants** | page-look | JS full of IE6 pixel fudges (`71+10`, `+25`); whether layout visibly differed unknown | `srv/index.php:655-657,816,828-839` | Era footage recorded in IE | LOW |
| S113 | **Any page rendered logged-in** | page-look | **Project boundary: logged-in rendering not reconstructed anywhere.** Logged-in variants of all six tabs unknown, not just garage | DECISIONS "logged-in rendering is a boundary" | **Most valuable footage class: one logged-in session across all six tabs** | MED |
| S114 | **Unnamed / unknown-existence UI** | speculative | Code hints without names: filter values beyond `'all'`, sherif-star panel, `content.php`, `Select2` tabs, add-friend UI (only `top10Friends` proves friends existed), achievement list page, ranks surfaced outside lab | scattered | Any on-screen control in era footage that maps to nothing in this document = a find; photograph it + its label verbatim | MED |

---

*Add new entries at the bottom of the relevant section. When evidence
arrives: archive it under `archive/` (read-only discipline), add the
LEDGER row (M2, with URL/uploader/date/timestamp), flip the status here,
note the superseded invention in DECISIONS.md — and apply THE OVERHAUL
RULE to whatever the evidence touches.*
