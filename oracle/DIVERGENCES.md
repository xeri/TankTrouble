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
