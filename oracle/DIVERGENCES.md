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

### Projector half — NOT yet run

No Flash projector binary exists in the archive or on this machine, so the
Ruffle-vs-projector diff (gate C proper) has only its Ruffle half. Obtain an
Adobe Flash projector (archive.org holds the last 32.0.0.371 standalone
builds) before gate C rendering comparisons. Until then every Ruffle
behaviour above is verified against the DECOMPILE's expectations, not
against a running original player.
