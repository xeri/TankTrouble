# Ruffle / projector divergence log (gate C, guide 7.3)

## 2026-08-03 — SetVariable spike (guide §9 step 2)

Harness: `ruffle-spike/` — headless Chromium loads Ruffle 0.4.1 (npm
`@ruffle-rs/ruffle`) running the ORIGINAL
`signUpTankDesign13StandardColours.swf` (the era homepage's embed) plus the
era `Assets/*.swf`. Reproduce: see `ruffle-spike/README.md`.

| API | Direction | Verdict under Ruffle |
|---|---|---|
| `getURL("javascript: …")` | SWF → page | **WORKS.** Clicking paint cans wrote `0xff00` / `0x80ff` into the page's `signupturretcolor` / `signuptrackscolor` inputs — original bytes, unmodified page contract (`ruffle-spike/results.json`) |
| `player.SetVariable()` / `player.GetVariable()` | page → SWF | **ABSENT.** Not present on Ruffle's player element (`typeof` = undefined); every probe threw |

### Consequence for the mazeCreator rebuild (guide §6.5, §9 step 9)

The recovered page JS steers the editor exclusively through `SetVariable`
(`fadeOut`, `newToolRequested`, `_root.saveRequested`, `_root.mazeName`,
`_root.errorPanel.hide`, `previewLoaded`). Under Ruffle that channel does
not exist, so **original page JS + rebuilt SWF cannot work as-is in Ruffle**.
Known options, decision deferred to the mazeCreator design step:

1. Ship the rebuilt editor SWF with an `ExternalInterface` shim alongside
   the SetVariable contract (Flash 8 supports ExternalInterface, and Ruffle
   implements it) — page JS then needs a thin adapter, a recorded divergence.
2. Implement the editor as a native HTML5 port (`PORT-FEASIBILITY.md`), where
   no Flash runtime is involved at all.
3. Track Ruffle upstream: if the classic JS API lands later, re-run this
   spike (`node ruffle-spike/run_spike.mjs`) and reconsider.

The paint-editor flow (getURL bridge) needs NO divergence — original SWFs
run against the original page contract.

### Projector half — HELD as of 2026-08-03

Adobe Flash Player **32.0.0.465** standalone (the true final Windows build;
the 32.0.0.371 guess above was superseded by the PE resource) now sits at
`oracle/projector/flashplayer_32_sa.exe` — provenance and smoke-test record
in `oracle/projector/FETCHED.md`. Query-string FlashVars (`file:///…?initCode=`)
reach `_root` in the projector, so gate C can drive SWFs with the site's own
initCode mechanism. Gate C rendering comparisons are now unblocked; the
game SWF needs stack/initCode wiring (phase 2) before it renders standalone.

## 2026-08-03 — editor-spike: EI-exposed SetVariable under Ruffle (phase 1, guide 6.5 pre-work)

Harness: `editor-spike/` — MTASC-built `spike.swf` (SWF v8, 688×400 @ 25fps,
matching the O embed at srv/index.php:3617 and the fps comment at :3637),
loaded by the same headless-Chromium + Ruffle 0.4.1 rig as `ruffle-spike/`.
Reproduce: `sh build.sh && node run_editor_spike.mjs`.

| Probe | Verdict under Ruffle |
|---|---|
| `ExternalInterface.addCallback("SetVariable", …)` then page calls `player.SetVariable(name, value)` | **WORKS.** `typeof player.SetVariable == "function"`; `SetVariable("newToolRequested","crateSpawn")` repainted the stage and `GetVariable("lastSet")` returned `newToolRequested=crateSpawn` |
| `addCallback("GetVariable", …)` | **WORKS** (same run) |
| FlashVars via SWF query string (`spike.swf?initCode=…`) | **DELIVERED** to `_root` — decoded value round-tripped through GetVariable and the boot bridge |
| `getURL("javascript:…")` from MTASC-built bytes | **WORKS** both at boot and from the save path |
| `_root.`-prefixed names through the EI callback | Arrive as the literal string `"_root.saveRequested"` — OUR code must strip the prefix (native plugin resolved it as a path; the rebuilt editor reproduces that) |

results.json 2026-08-03: all four verdicts true
(`flashvars_delivered`, `geturl_boot_fired`, `ei_setvariable_works`,
`geturl_save_fired`).

### Consequence

The 2026-08-03 SetVariable gap above is CLOSED for the rebuild case: a
rebuilt editor SWF that registers `SetVariable`/`GetVariable` via
ExternalInterface answers the ORIGINAL page JS call shape
(`el.SetVariable(name, value)`, srv/index.php:3609-3753) under Ruffle with
**zero page-side divergence**. Option 1 of the earlier note is adopted in
its strongest form — no page adapter needed. Decision recorded in
DECISIONS.md (2026-08-03, mazeCreator control channel).

## 2026-08-03 — phase 2 round-trip gate: MazeData vs the corpus

`oracle/editor-roundtrip/`: 670 unique corpus grids (672 seeded states,
latest-wins; `tools/extract_maze_grids.py`) fed through the rebuilt
editor's `MazeData.parse()` -> `emit()` under Ruffle 0.4.1 via an
ExternalInterface `roundTrip` hook — **670/670 byte-identical**
(`node run_roundtrip.mjs`, exit 0).

Findings the gate/audit surfaced:

* **Every corpus grid (670/670) carries bit-2 digits in row 0** — the
  arena's top boundary wall. The O READER re-homes bit 2 onto the upper
  cell and silently drops row 0's bit into `[x][-1]`
  (MazeDataFetcher.as:126), so the game's model never sees the top border;
  the WRITER plainly emitted it. The rebuilt model keeps bit 2 on its own
  cell (`wallNorth[x][y]`) for byte-fidelity and derives the reader's view.
* Emit-shape audit: `reserved` field is `0` in all 670 grids; every object
  `params` field is empty; cell digit alphabet is exactly 0-7. The emitter
  still round-trips `reserved` verbatim rather than hardcoding it.

## 2026-08-04 — gate C: rebuilt mazeCreator, projector vs Ruffle

SWF: srv/includes/mazeCreator_v0.3.swf sha256 2df553765d6abe1c6b319f812eef082087853cad95a747889aa95a86b5bc440c
Runtimes: Flash projector 32.0.0.465 (oracle/projector) vs Ruffle 0.4.1
(oracle/ruffle-spike), same maze both sides (oracle/editor-visual/
gatec_maze.json — a real corpus maze, 4x4, 2 tanks + 2 crates).
Method: oracle/projector/shot_editor.ps1 (topmost + validated
CopyFromScreen; PrintWindow is black for this player) vs
`node run_editor.mjs --screenshot`; diff via tools/diff_render.py.

Numbers: masked (title + watermark device-text bands) mean=0.02
max=239 pct_over_32=0.01 · unmasked mean=0.26 max=239 pct_over_32=0.27.
Verdict: **pass — vector geometry pixel-identical**; all visible
divergence is device-font rasterization (_sans differs per runtime) and
faint icon-glow alpha rounding. Cosmetic only.

Runtime divergences found while wiring the editor (all mitigated):
1. **Ruffle SetVariable("name", "")** delivers null (watch channel
   stringifies to "null"); real Flash keeps "". Editor normalizes
   null/"null"/"undefined" to "" at the vocabulary entry point.
2. **Relative LoadVars URLs**: Flash resolves against the SWF's URL,
   Ruffle against the page URL. The SWF keeps the Flash-faithful sibling
   path ("saveMaze.php"); harnesses (and any future Ruffle embed) must set
   RufflePlayer config.base to the SWF's directory ("includes/").
3. **Projector truncates its command-line URL near MAX_PATH (~260
   chars)** — diagnosed with oracle/editor-visual/Diag.as marker bars
   (initCode arrived 185/300 chars). Only affects the projector-CLI
   harness path, never the real page embed (FlashVars param). Gate C
   uses a short corpus maze; shot_editor.ps1 guards the length.
4. MTASC static field initializers were replaced with an explicit
   MazeRenderer.initConstants() call. Suspected cause of an empty
   projector render — **falsified** (truncation was the cause) — kept as
   defensive hardening.
