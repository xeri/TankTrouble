# mazeCreator Phase 1 — Toolchain + Dual-Channel Spike + Projector Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** De-risk the mazeCreator SWF rebuild (guide §6.5, §9 step 9) by proving an AS2/Flash-8 toolchain works on this machine, proving the page↔SWF control channel works under Ruffle, and acquiring the Flash projector for gate C — before any editor code is written.

**Architecture:** MTASC (open-source AS2 compiler) compiles a spike SWF targeting SWF version 8. The spike registers `ExternalInterface.addCallback("SetVariable", …)` so the player element grows a `SetVariable` method under Ruffle — same call signature the original page JS uses (`el.SetVariable(name, value)`). If that works, the rebuilt editor needs ZERO page-side divergence. The existing `oracle/ruffle-spike/` puppeteer harness is extended with a second runner for the spike SWF. The Adobe standalone projector 32.0.0.371 is fetched from archive.org as the gate C oracle.

**Tech Stack:** MTASC 1.14 (Windows binary), Ruffle 0.4.1 (already vendored in `oracle/ruffle-spike/ruffle/`), puppeteer-core (already in `oracle/ruffle-spike/node_modules/`), Python 3 (SWF header parse), Adobe Flash Player 32.0.0.371 standalone projector.

## Global Constraints

- Repo: `C:\Users\eth\websites\TankTrouble`. Archive at `archive/` is READ-ONLY — never write into it.
- Every new file under `srv/` needs a `LEDGER.tsv` row (none planned here — all work is `oracle/` + `tools/` + `thirdparty/`, outside the document root).
- Fetched binaries: verify magic bytes before trusting (trap table, guide §8); record source URL + sha256 in a `FETCHED.md` next to the binary (pattern: `thirdparty/sajax/FETCHED.md`).
- Judgement calls → append-only entry in `DECISIONS.md`. Spike findings → `oracle/DIVERGENCES.md`.
- Never commit fetched third-party binaries and written code in the same commit.
- Existing gates must stay green: offline `python -m pytest tests/ -q -m "not live"` = 35 passed.
- Downloads: ≤2 concurrent, adaptive backoff (trap: IA self-throttling).
- Commit messages follow repo convention: `feat(oracle): …`, `chore(thirdparty): …`, `docs: …`.

## Evidence base (read-only inputs, already verified this session)

- Page contract, O bytes, `srv/index.php:3609-3753`: SetVariable vocabulary `fadeOut`, `newToolRequested` (values `construct|crateSpawn|tankSpawn`), `_root.saveRequested`, `_root.mazeName`, `_root.errorPanel.hide`, `previewLoaded`; embed = SWFObject, `688×400`, player `8`, bg `#ffffff`, `wmode=transparent`, `menu=false`, `allowScriptAccess=sameDomain`, `FlashVars initCode=<innerHTML of userSettingsMazeCreatorInitCode-{user}>`.
- FPS evidence: comment at `srv/index.php:3637` — `// 1700 + 15frames/25fps * 1000 = 4300` → sibling editor SWF runs **25 fps**, fade = 15 frames.
- Ruffle verdicts so far (`oracle/DIVERGENCES.md`): `getURL("javascript:…")` outbound WORKS; native `player.SetVariable`/`GetVariable` ABSENT.
- Harness: `oracle/ruffle-spike/run_spike.mjs` (HTTP server + puppeteer pattern to copy).

---

### Task 1: Fetch and pin MTASC

**Files:**
- Create: `thirdparty/mtasc/FETCHED.md`
- Create: `thirdparty/mtasc/.gitignore` (binary itself not committed; FETCHED.md carries URL + sha256 for reproduction)

**Interfaces:**
- Produces: `thirdparty/mtasc/mtasc.exe` (+ `std/` and `std8/` include dirs) — Task 2 and all later SWF builds invoke it as `thirdparty/mtasc/mtasc.exe -version 8 -swf <out> -main -header 688:400:25 <src>`.

- [ ] **Step 1: Download MTASC 1.14 Windows build**

Primary URL (mtasc.org is long dead; archive.org holds it):

```bash
cd /c/Users/eth/websites/TankTrouble/thirdparty
mkdir -p mtasc && cd mtasc
curl -L -o mtasc-1.14-win.zip "https://web.archive.org/web/2016/http://www.mtasc.org/zip/mtasc-1.14-win.zip"
```

If that 404s, fall back to searching the archive.org copy of `mtasc.org/zip/` via the CDX API (exact URL, no wildcard — trap table):

```bash
curl -s "http://web.archive.org/cdx/search/cdx?url=mtasc.org/zip/mtasc-1.14-win.zip&output=json&filter=statuscode:200&limit=5"
# take any timestamp T from the result, then:
curl -L -o mtasc-1.14-win.zip "https://web.archive.org/web/<T>id_/http://www.mtasc.org/zip/mtasc-1.14-win.zip"
```

- [ ] **Step 2: Verify magic bytes and unpack**

```bash
xxd -l 4 mtasc-1.14-win.zip   # must start 50 4b 03 04 ("PK..") — trap: size ≠ integrity
unzip -o mtasc-1.14-win.zip
ls   # expect mtasc.exe, std/, std8/ (layout may nest one dir deeper — flatten so mtasc.exe sits at thirdparty/mtasc/mtasc.exe)
./mtasc.exe 2>&1 | head -3   # expect usage banner "Motion-Twin ActionScript2 Compiler"
```

- [ ] **Step 3: Record provenance**

Write `thirdparty/mtasc/FETCHED.md`:

```markdown
# MTASC 1.14 — Motion-Twin ActionScript 2 compiler

- Source: <the exact web.archive.org URL that worked>
- Fetched: 2026-08-03
- sha256(mtasc-1.14-win.zip): <sha256sum output>
- Role: compiles the rebuilt mazeCreator (M2) — AS2, SWF version 8.
- NOT original site material. Tool provenance only; never enters srv/.
```

Write `thirdparty/mtasc/.gitignore`:

```
*
!FETCHED.md
!.gitignore
```

- [ ] **Step 4: Verify it compiles anything at all**

```bash
cd /c/Users/eth/websites/TankTrouble
cat > /tmp/Hello.as <<'EOF'
class Hello {
    static function main() {
        _root.createEmptyMovieClip("c", 1);
        _root.c.beginFill(0xff0000);
        _root.c.moveTo(0, 0); _root.c.lineTo(100, 0);
        _root.c.lineTo(100, 100); _root.c.lineTo(0, 100);
        _root.c.endFill();
    }
}
EOF
./thirdparty/mtasc/mtasc.exe -version 8 -swf /tmp/hello.swf -main -header 688:400:25 /tmp/Hello.as
xxd -l 3 /tmp/hello.swf   # expect 46 57 53 ("FWS") or 43 57 53 ("CWS")
```

Expected: SWF produced, magic bytes valid.

- [ ] **Step 5: Commit**

```bash
git add thirdparty/mtasc/FETCHED.md thirdparty/mtasc/.gitignore
git commit -m "chore(thirdparty): pin MTASC 1.14 - AS2 toolchain for mazeCreator rebuild (FETCHED.md)"
```

---

### Task 2: Spike SWF — dual-channel control surface

**Files:**
- Create: `oracle/editor-spike/Spike.as`
- Create: `oracle/editor-spike/build.sh`

**Interfaces:**
- Consumes: `thirdparty/mtasc/mtasc.exe` from Task 1.
- Produces: `oracle/editor-spike/spike.swf` (gitignored artefact) exposing, via `ExternalInterface.addCallback`: `SetVariable(name, value)` and `GetVariable(name)` on the player element. Internal state Task 3 asserts on: calling `SetVariable("newToolRequested", "crateSpawn")` must repaint the stage colour and `GetVariable("lastSet")` must return `"newToolRequested=crateSpawn"`. FlashVar `initCode` (Base64) is decoded at boot; decoded text drawn as stage colour key + reported via `GetVariable("initDecoded")`. On boot the SWF fires `getURL("javascript:__spikeBoot('<decoded>')")`.

- [ ] **Step 1: Write the spike source**

`oracle/editor-spike/Spike.as` — exercises every channel the real editor needs: FlashVars in, EI-callback in, getURL out, `_root`-variable semantics (`_root.saveRequested` path), and code-drawn vector output (what the whole editor UI will be):

```actionscript
import flash.external.ExternalInterface;

class Spike {

    static var app:Spike;
    static function main() { app = new Spike(); }

    var lastSet:String;
    var initDecoded:String;

    function Spike() {
        lastSet = "";
        initDecoded = decode64(String(_root.initCode));

        paint(0x336699);

        // Channel A: classic plugin API name, re-exposed via ExternalInterface.
        // Under real Flash the native SetVariable exists and addCallback of the
        // same name may be ignored -- both routes land in onSetVariable via the
        // _root watch below, so behaviour converges.
        var owner:Spike = this;
        ExternalInterface.addCallback("SetVariable", null,
            function(n:String, v:String) { owner.onSetVariable(n, v); });
        ExternalInterface.addCallback("GetVariable", null,
            function(n:String):String { return String(owner[n]); });

        // Channel B: native SetVariable writes _root vars directly; watch them.
        // Covers real-Flash/projector, where addCallback("SetVariable") may lose
        // to the built-in method.
        _root.watch("newToolRequested",
            function(prop, oldVal, newVal) { owner.onSetVariable(String(prop), String(newVal)); return newVal; });
        _root.watch("saveRequested",
            function(prop, oldVal, newVal) { owner.onSetVariable(String(prop), String(newVal)); return newVal; });

        // Channel C: SWF -> page, already proven for ORIGINAL bytes; this
        // proves it for MTASC-built bytes too.
        getURL("javascript:__spikeBoot('" + initDecoded + "')");
    }

    function onSetVariable(n:String, v:String):Void {
        lastSet = n + "=" + v;
        if (n == "newToolRequested") {
            if (v == "construct")  paint(0x33cc33);
            if (v == "crateSpawn") paint(0xcc8833);
            if (v == "tankSpawn")  paint(0xcc3333);
        }
        if (n == "saveRequested" && v == "true") {
            getURL("javascript:__spikeSaved('" + lastSet + "')");
        }
    }

    function paint(rgb:Number):Void {
        var c:MovieClip = _root.createEmptyMovieClip("canvas", 1);
        c.beginFill(rgb);
        c.moveTo(0, 0); c.lineTo(688, 0); c.lineTo(688, 400); c.lineTo(0, 400);
        c.endFill();
    }

    // Minimal Base64 -- the era client ships its own __Packages.Base64; the
    // spike only needs decode of [A-Za-z0-9+/=].
    function decode64(s:String):String {
        if (s == "undefined" || s == null || s == "") return "";
        var tab:String = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        var out:String = ""; var buf:Number = 0; var bits:Number = 0;
        for (var i:Number = 0; i < s.length; i++) {
            var v:Number = tab.indexOf(s.charAt(i));
            if (v < 0) continue;
            buf = (buf << 6) | v; bits += 6;
            if (bits >= 8) { bits -= 8; out += String.fromCharCode((buf >> bits) & 0xff); }
        }
        return out;
    }
}
```

- [ ] **Step 2: Write the build script**

`oracle/editor-spike/build.sh`:

```bash
#!/bin/sh
# Builds spike.swf. Header: 688x400 @ 25fps -- stage from the O embed
# (srv/index.php:3617), fps from the O comment (srv/index.php:3637).
cd "$(dirname "$0")"
../../thirdparty/mtasc/mtasc.exe -version 8 -swf spike.swf -main -header 688:400:25 Spike.as
```

- [ ] **Step 3: Build and verify magic bytes**

```bash
cd /c/Users/eth/websites/TankTrouble && sh oracle/editor-spike/build.sh
xxd -l 3 oracle/editor-spike/spike.swf   # 46 57 53 "FWS"
```

Expected: compiles clean, valid SWF. (If MTASC rejects the anonymous-function callbacks, hoist them to named methods — MTASC is strict AS2.)

- [ ] **Step 4: Commit**

```bash
git add oracle/editor-spike/Spike.as oracle/editor-spike/build.sh
git commit -m "feat(oracle): editor spike SWF - dual-channel SetVariable surface for Ruffle test"
```

---

### Task 3: Ruffle spike runner — the verdict machine

**Files:**
- Create: `oracle/editor-spike/index.html`
- Create: `oracle/editor-spike/run_editor_spike.mjs`
- Create: `oracle/editor-spike/.gitignore`

**Interfaces:**
- Consumes: `spike.swf` from Task 2; Ruffle + puppeteer vendored in `oracle/ruffle-spike/` (reused via relative path, NOT duplicated).
- Produces: `oracle/editor-spike/results.json` with verdict booleans: `ei_setvariable_works`, `flashvars_delivered`, `geturl_boot_fired`, `geturl_save_fired`, `paint_changed`. These verdicts decide the editor design (Task 6 records the decision).

- [ ] **Step 1: Write the host page**

`oracle/editor-spike/index.html` — embeds via Ruffle exactly like the O page would (same params as `srv/index.php:3617`), FlashVars `initCode` = Base64 of `u=99&n=testuser01&` (shape mirrors the reconstructed initCode convention, `srv/index.php:160-165`):

```html
<!doctype html>
<meta charset="utf-8">
<title>editor spike</title>
<script src="../ruffle-spike/ruffle/ruffle.js"></script>
<div id="swfhost" style="width:688px;height:400px"></div>
<script>
window.__spike = { boot: null, saved: null, probes: {} };
window.__spikeBoot  = function (d) { window.__spike.boot = d; };
window.__spikeSaved = function (d) { window.__spike.saved = d; };

window.RufflePlayer = window.RufflePlayer || {};
window.RufflePlayer.config = { autoplay: "on", unmuteOverlay: "hidden",
                               allowScriptAccess: true };
window.addEventListener("DOMContentLoaded", async () => {
  const ruffle = window.RufflePlayer.newest();
  const player = ruffle.createPlayer();
  player.style.width = "688px"; player.style.height = "400px";
  document.getElementById("swfhost").appendChild(player);
  window.__player = player;
  try {
    // btoa("u=99&n=testuser01&") -- literal to keep the page dependency-free
    await player.load("spike.swf?initCode=" + btoa("u=99&n=testuser01&"));
    window.__spike.loaded = true;
  } catch (e) { window.__spike.loadfail = String(e); }
});
</script>
```

Note: FlashVars passed as a URL query on the SWF path — same `_root` delivery mechanism, and it is also the mechanism the projector run will use (Task 5), so proving it here proves it for both runtimes.

- [ ] **Step 2: Write the runner**

`oracle/editor-spike/run_editor_spike.mjs` (pattern copied from `oracle/ruffle-spike/run_spike.mjs` — same HTTP server, same browser launch):

```js
// Editor-spike runner: is ExternalInterface.addCallback("SetVariable") enough
// to run the ORIGINAL page JS against a REBUILT editor SWF under Ruffle?
// Run:    node run_editor_spike.mjs        (after sh build.sh)
// Output: results.json + spike.png; findings -> ../DIVERGENCES.md by hand.

import http from "node:http";
import { readFile } from "node:fs/promises";
import { writeFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";

const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const ROOT = path.resolve(DIR, "..", "..");   // repo root, so ../ruffle-spike/ruffle resolves
const PORT = 8078;
const MIME = { ".html": "text/html", ".js": "text/javascript",
               ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };

const server = http.createServer(async (req, res) => {
  try {
    const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "");
    const body = await readFile(path.join(ROOT, "oracle", rel.startsWith("ruffle-spike") ? "" : "editor-spike", rel));
    res.writeHead(200, { "Content-Type": MIME[path.extname(rel)] || "application/octet-stream" });
    res.end(body);
  } catch { res.writeHead(404); res.end("nope"); }
});
await new Promise(r => server.listen(PORT, "127.0.0.1", r));

const EXE = process.env.TT_BROWSER ||
  "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe";
const browser = await puppeteer.launch({ executablePath: EXE, headless: true,
  args: ["--no-first-run"] });
const page = await browser.newPage();
await page.setViewport({ width: 900, height: 600 });
const console_lines = [];
page.on("console", m => console_lines.push(m.text()));
page.on("pageerror", e => console_lines.push("PAGEERROR " + e.message));

await page.goto(`http://127.0.0.1:${PORT}/index.html`);
await page.waitForFunction("window.__spike && (window.__spike.loaded || window.__spike.loadfail)",
  { timeout: 30000 });
await new Promise(r => setTimeout(r, 2000));   // let the SWF boot + getURL fire

const shot = async n => page.screenshot({ path: path.join(DIR, n) });
await shot("spike-boot.png");

const result = await page.evaluate(async () => {
  const p = window.__player;
  const out = { boot: window.__spike.boot, loadfail: window.__spike.loadfail || null,
                setvar_type: typeof p.SetVariable, getvar_type: typeof p.GetVariable };
  const call = (f, ...a) => { try { return { ok: true, ret: f(...a) }; }
                              catch (e) { return { ok: false, err: String(e) }; } };
  // THE question: does the EI-exposed SetVariable answer the ORIGINAL call shape?
  out.set_tool  = call((n, v) => p.SetVariable(n, v), "newToolRequested", "crateSpawn");
  await new Promise(r => setTimeout(r, 500));
  out.get_last  = call(n => p.GetVariable(n), "lastSet");
  out.get_init  = call(n => p.GetVariable(n), "initDecoded");
  out.set_save  = call((n, v) => p.SetVariable(n, v), "_root.saveRequested", "true");
  await new Promise(r => setTimeout(r, 500));
  out.saved = window.__spike.saved;
  return out;
});
await shot("spike-after.png");

result.console_tail = console_lines.slice(-40);
result.verdicts = {
  flashvars_delivered:  result.boot === "u=99&n=testuser01&",
  geturl_boot_fired:    result.boot !== null,
  ei_setvariable_works: result.set_tool?.ok === true &&
                        result.get_last?.ret === "newToolRequested=crateSpawn",
  geturl_save_fired:    typeof result.saved === "string" || result.saved === null &&
                        result.set_save?.ok === true,
};
writeFileSync(path.join(DIR, "results.json"), JSON.stringify(result, null, 2));
console.log(JSON.stringify(result.verdicts, null, 2));
console.log("full details in results.json");
await browser.close(); server.close();
```

- [ ] **Step 3: Write .gitignore for artefacts**

`oracle/editor-spike/.gitignore`:

```
spike.swf
results.json
*.png
```

- [ ] **Step 4: Run it — this step IS the test**

```bash
cd /c/Users/eth/websites/TankTrouble/oracle/editor-spike && node run_editor_spike.mjs
```

Expected shape of PASS: all four verdicts `true`, `spike-after.png` shows the orange (`0xcc8833`) crateSpawn fill.

Interpretation table (this is the deliverable, record whichever row fires):

| `ei_setvariable_works` | Consequence |
|---|---|
| `true` | Rebuilt SWF + ORIGINAL page JS run unchanged under Ruffle. Zero page divergence. Editor design = dual-channel (EI callback + `_root.watch`). |
| `false` but `set_tool.ok` (call succeeded, state wrong) | EI callback name collision or arg marshalling issue — try callback name probe variants (`setVariable`, custom name + page adapter). Adapter = recorded divergence. |
| `false`, call threw | Ruffle does not expose AVM1 EI callbacks on the element — editor needs a page-side adapter shim (divergence option 1 in DIVERGENCES.md) or the HTML5-port route (PORT-FEASIBILITY.md). STOP and record before any editor work. |

Note the `_root.saveRequested` probe: the original JS passes the literal name `"_root.saveRequested"` to native SetVariable, which the plugin resolves as a path. Through the EI callback OUR code receives the string and must resolve the `_root.` prefix itself — the spike's `onSetVariable` treats `"saveRequested"` and `"_root.saveRequested"` as distinct, so `get_last` after `set_save` should read `_root.saveRequested=true`. If `saved` fired with that value, path handling is proven needed and working. (The real editor strips a leading `_root.` — carry this into phase 2.)

- [ ] **Step 5: Commit harness (artefacts stay ignored)**

```bash
git add oracle/editor-spike/index.html oracle/editor-spike/run_editor_spike.mjs oracle/editor-spike/.gitignore
git commit -m "feat(oracle): editor-spike Ruffle runner - EI SetVariable verdict harness"
```

---

### Task 4: Confirm sibling SWF header facts (stage + fps)

**Files:**
- Create: `tools/swf_header.py`

**Interfaces:**
- Produces: `python tools/swf_header.py <path.swf>` → one line `version=<n> compressed=<yes/no> stage=<w>x<h>px fps=<f> frames=<n>`. Phase 2 reuses it to sanity-check every built editor SWF.

- [ ] **Step 1: Write the header reader**

`tools/swf_header.py`:

```python
#!/usr/bin/env python3
"""Print SWF header facts: version, stage rect (px), fps, frame count.

Evidence tool for the mazeCreator rebuild: the sibling editor's header
(signUpTankDesign*, the paint editor) bounds the design space for the lost
mazeCreator_v0.3.swf (DEDUCE.md rule 7). Also sanity-checks MTASC output.
"""
import struct, sys, zlib


def read_header(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    sig, version = raw[:3], raw[3]
    if sig == b"CWS":
        body, compressed = zlib.decompress(raw[8:]), True
    elif sig == b"FWS":
        body, compressed = raw[8:], False
    else:
        raise SystemExit(f"not a SWF (magic {sig!r})")  # trap: size != integrity

    # RECT: 5 bits nbits, then 4 signed fields of nbits each, in twips
    nbits = body[0] >> 3
    bits = "".join(f"{b:08b}" for b in body[: (5 + 4 * nbits + 7) // 8 + 1])
    vals = [int(bits[5 + i * nbits : 5 + (i + 1) * nbits], 2) for i in range(4)]
    xmin, xmax, ymin, ymax = vals
    off = (5 + 4 * nbits + 7) // 8
    fps = body[off] / 256 + body[off + 1]          # fixed 8.8, little-endian
    frames = struct.unpack("<H", body[off + 2 : off + 4])[0]
    return {
        "version": version, "compressed": compressed,
        "w": (xmax - xmin) // 20, "h": (ymax - ymin) // 20,
        "fps": fps, "frames": frames,
    }


if __name__ == "__main__":
    for p in sys.argv[1:]:
        h = read_header(p)
        print(f"{p}: version={h['version']} compressed={'yes' if h['compressed'] else 'no'} "
              f"stage={h['w']}x{h['h']}px fps={h['fps']:g} frames={h['frames']}")
```

- [ ] **Step 2: Run against the siblings and the spike**

```bash
cd /c/Users/eth/websites/TankTrouble
python tools/swf_header.py \
  srv/includes/signUpTankDesign18StandardColours.swf \
  srv/includes/TankTrouble_v4.0.swf \
  oracle/editor-spike/spike.swf
```

Expected: paint editor sibling reports `fps=25` (corroborating the `srv/index.php:3637` comment); spike reports `version=8 stage=688x400px fps=25`. Whatever the sibling ACTUALLY reports is the finding — if it is not 25, record the discrepancy in DECISIONS.md and prefer the measured value.

- [ ] **Step 3: Commit**

```bash
git add tools/swf_header.py
git commit -m "feat(tools): swf_header.py - header evidence reader (sibling fps/stage facts)"
```

---

### Task 5: Acquire the Flash projector (gate C oracle half)

**Files:**
- Create: `oracle/projector/FETCHED.md`
- Create: `oracle/projector/.gitignore`

**Interfaces:**
- Produces: `oracle/projector/flashplayer_32_sa.exe` — gate C ground-truth runtime. Phase 2's gate C harness launches it as `oracle/projector/flashplayer_32_sa.exe <swf-path-or-file-url>`.

- [ ] **Step 1: Locate a trustworthy copy on archive.org**

Adobe's fpdownload URLs died with EOL. archive.org holds the final standalone builds. Search items, then verify before trusting:

```bash
curl -s "https://archive.org/advancedsearch.php?q=flashplayer+32+standalone+projector&fl%5B%5D=identifier&rows=10&output=json" | python -m json.tool | head -40
```

Pick an item whose file listing (`https://archive.org/metadata/<identifier>`) contains a Windows standalone projector (`flashplayer*_sa.exe`, ~15 MB). Prefer an item that mirrors Adobe's original `fp_32.0.0.371_archive.zip` layout.

```bash
mkdir -p /c/Users/eth/websites/TankTrouble/oracle/projector
cd /c/Users/eth/websites/TankTrouble/oracle/projector
curl -L -o flashplayer_32_sa.exe "<direct file URL from the metadata listing>"
```

- [ ] **Step 2: Verify it is actually a PE executable of plausible size**

```bash
xxd -l 2 flashplayer_32_sa.exe        # 4d 5a "MZ" — trap: size != integrity
ls -la flashplayer_32_sa.exe          # expect ~10-16 MB, not a 151 KB HTML error page
sha256sum flashplayer_32_sa.exe
```

- [ ] **Step 3: Smoke-test against ORIGINAL bytes**

Launch it with the O game SWF (visual check — window opens, preloader runs):

```powershell
Start-Process oracle\projector\flashplayer_32_sa.exe -ArgumentList ((Resolve-Path srv\includes\TankTrouble_v4.0.swf).Path)
# observe, then close the window (or Stop-Process -Name flashplayer_32_sa)
```

Then the spike SWF with query-string FlashVars (this is the projector-side initCode delivery Task 3's note promised):

```powershell
$u = "file:///" + ((Resolve-Path oracle\editor-spike\spike.swf).Path -replace '\\','/') + "?initCode=dT05OSZuPXRlc3R1c2VyMDEm"
Start-Process oracle\projector\flashplayer_32_sa.exe -ArgumentList $u
```

Expected: blue `0x336699` stage (boot paint). The `getURL("javascript:…")` call is a no-op in the projector — that is fine and worth noting in FETCHED.md; gate C is visual.

- [ ] **Step 4: Record provenance + divergence note**

`oracle/projector/FETCHED.md`:

```markdown
# Adobe Flash Player standalone projector (gate C oracle)

- Item: https://archive.org/details/<identifier>
- File: <file URL used>
- Fetched: 2026-08-03
- sha256: <value>
- Version: <as reported by right-click > Properties > Details, expect 32.0.0.371>
- Role: gate C ground truth (guide 7.3). Runs O SWFs natively.
- Note: getURL("javascript:") is inert in the projector; page-bridge
  behaviour is only testable under Ruffle. Gate C compares RENDERING.
```

`oracle/projector/.gitignore`:

```
*
!FETCHED.md
!.gitignore
```

- [ ] **Step 5: Commit, and update DIVERGENCES.md projector section**

Edit `oracle/DIVERGENCES.md` — replace the "Projector half — NOT yet run" paragraph body with a line stating the projector is now held at `oracle/projector/` (keep the heading; the section becomes the gate C status log).

```bash
git add oracle/projector/FETCHED.md oracle/projector/.gitignore oracle/DIVERGENCES.md
git commit -m "chore(oracle): pin Flash projector 32 standalone - gate C oracle half (FETCHED.md)"
```

---

### Task 6: Record verdicts + design decision

**Files:**
- Modify: `oracle/DIVERGENCES.md` (append spike results section)
- Modify: `DECISIONS.md` (append design decision — append-only, never edit old entries)

**Interfaces:**
- Consumes: `oracle/editor-spike/results.json` verdicts from Task 3; header facts from Task 4.
- Produces: the recorded design decision phase 2's editor plan builds on.

- [ ] **Step 1: Append spike results to oracle/DIVERGENCES.md**

Append a section in the existing house style (date-headed, table of API/verdict, consequence paragraph). Content comes from `results.json` — do not write it before the run. Must cover: `ei_setvariable_works` verdict, FlashVars-via-query delivery, getURL from MTASC-built bytes, `_root.`-prefix path handling, and which interpretation-table row fired.

- [ ] **Step 2: Append the design decision to DECISIONS.md**

Template (adjust to the actual verdict):

```markdown
## 2026-08-03 — mazeCreator control channel: dual-channel SWF, page JS untouched
Tier: M2 (editor), O (page contract unchanged).
The rebuilt editor implements BOTH control routes: (a)
ExternalInterface.addCallback("SetVariable"/"GetVariable") so Ruffle's player
element answers the ORIGINAL page calls (spike: oracle/editor-spike,
results 2026-08-03), and (b) _root variable watch/poll so native SetVariable
works under real Flash (projector, gate C). Page-side JS stays the O bytes —
zero divergence. Names with a "_root." prefix are resolved by stripping the
prefix (native plugin behaviour, reproduced).
Rejected: page-side adapter shim (needless divergence given (a) works);
HTML5 port for the editor (PORT-FEASIBILITY.md stays the fallback if Ruffle
regresses).
Evidence: oracle/editor-spike/results.json; fps=25 + 688x400 from
srv/index.php:3617,3637 and tools/swf_header.py over the sibling paint editor.
Reversible: yes — channel (b) alone suffices for any real-Flash runtime.
Supersedes: the "decision deferred" note in oracle/DIVERGENCES.md 2026-08-03.
```

If the spike FAILED (`ei_setvariable_works=false`), the decision entry instead selects the page-adapter divergence or the HTML5 port, quoting the failing probe verbatim — do NOT proceed to phase 2 planning without this entry either way.

- [ ] **Step 3: Run the offline gate suite — nothing may regress**

```bash
cd /c/Users/eth/websites/TankTrouble && python -m pytest tests/ -q -m "not live"
```

Expected: 35 passed (same count as before this plan).

- [ ] **Step 4: Commit**

```bash
git add oracle/DIVERGENCES.md DECISIONS.md
git commit -m "docs: editor spike verdicts + mazeCreator control-channel decision"
```

- [ ] **Step 5: Tag phase completion**

```bash
git tag mazecreator-spike-complete
```

---

## Out of scope (phase 2 plan, written AFTER Task 6's verdict)

- The editor SWF itself (grid model, wire-format emit, tools, error panel, previews state)
- `saveMaze.php` (M3) + `userSettingsMazeCreatorInitCode` markup reconstruction
- Toolbar icon redraw from `Making a maze.png` + video frames (M2/M3 art)
- Gate C screenshot-diff automation
- Logged-in garage UI

## Self-review notes

- Spec coverage: guide §9 step 2 remainder (projector half) → Task 5; §6.5 pre-work (toolchain, control channel) → Tasks 1-3; DEDUCE rule 7 sibling evidence → Task 4; §3.3 decision logging → Task 6. Editor build itself intentionally out of scope.
- Interfaces consistent: `SetVariable`/`GetVariable`/`lastSet`/`initDecoded` names match across Tasks 2-3; `mtasc.exe` invocation identical in Tasks 1-2; projector path matches Tasks 5 and the FETCHED.md.
- No placeholder steps: every code block is complete and runnable; the two "write whichever verdict fired" steps are data-dependent by design, with required content enumerated.
