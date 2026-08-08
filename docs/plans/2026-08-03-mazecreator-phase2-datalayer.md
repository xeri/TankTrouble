# mazeCreator Phase 2 — Maze Data Layer + Round-Trip Gate + saveMaze.php Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the rebuilt editor's maze data model (AS2 parse/emit of the `d=` grid format) proven byte-identical against all 672 seeded corpus grids under Ruffle, and land `srv/includes/saveMaze.php` (M3) so the editor has a save target.

**Architecture:** `MazeData.as` is a standalone AS2 class (no UI) ported from the O reader `archive/decompiled/CLASSIC_TankTrouble_v4.0/scripts/__Packages/MazeDataFetcher.as` — parse keeps every field (including `reserved` and per-object `params`) so emit reproduces the input verbatim. A test-only harness SWF exposes `roundTrip(d)` via ExternalInterface; a node runner (same rig as phase 1) feeds every corpus grid through it and asserts byte-identity. `saveMaze.php` mirrors `loadMaze.php`'s wire conventions (M3 — every name and format choice is invention, recorded as such) and validates against the constraint set measured from the corpus.

**Tech Stack:** MTASC 1.14 (`thirdparty/mtasc/`), Ruffle 0.4.1 + puppeteer (`oracle/ruffle-spike/` rig), Python 3, PHP 5.6 in the docker stack (127.0.0.1:8056).

## Global Constraints

- Repo: `C:\Users\eth\websites\TankTrouble`. `archive/` is READ-ONLY.
- Every new file in `srv/` needs a `LEDGER.tsv` row + parseable `@provenance` header (gate D enforces both). `saveMaze.php` already has a `pending` row — update it, do not duplicate.
- Never present invented names/formats as recovered: `saveMaze.php` is **M3 BY CHOICE**, loud in its header, decision logged in `DECISIONS.md`.
- Existing gates stay green: offline `python -m pytest tests/ -q -m "not live"` = 35 passed; full live suite = 61 + whatever this plan adds.
- The 843-payload corpus at `archive/maze-corpus/raw/` is the ground truth; 672 distinct `(author, slot)` states are seeded in `mazes`.
- Editor constraints (verified against 843 mazes, 0 violations — guide §6.5): grid ≤ 18×10, title ≤ 32 chars over `A–Za–z0–9 !,-.? ` + space, author ≤ 16, ≤ 5 tank spawns (type 5), ≤ 5 crate spawns (type 8), ≤ 10 objects.
- Commit style: `feat(M3): …`, `feat(oracle): …`, `data: …`; never mix archive bytes and written code in one commit.

## Evidence base

- O reader semantics (`MazeDataFetcher.as:67-162`): `d.split("#")`; field0 = w; field1 = cells, `h = len/w`; loop **y outer, x inner** reading digits sequentially; digit bit-peel in this order: `>=4` → **west wall** at `[x][y][2]`, `%4`; `>=2` → **wall shared with the cell above** stored at `[x][y-1][1]`, `%2`; `>=1` → **floor** at `[x][y][0]`; field2 = reserved (read, discarded); field3 = objCount; per object 4 fields `x, y, type, params.split(",")`, coords 1-indexed (`x-1,y-1` stored), type 5 = tank spawn, 8 = crate spawn; then ONE further field skipped (the `0` terminator).
- Corpus emit shape, 0 objects: `7#<42 cells>#0#0##0#`. 5 objects: `4#<32 cells>#0#5#3#1#8##4#1#5##1#5#5##3#8#8##4#8#5###0#` (objects contribute `x#y#type#params#`; tail is `#0#`).
- `decodeMessage` (`MazeDataLoader.as`): base64 → split `&` → split `=` — pair order irrelevant.
- Phase 1 verdicts (`oracle/DIVERGENCES.md` 2026-08-03): EI-exposed callbacks answer `el.<name>(…)` under Ruffle; FlashVars via SWF query string work.
- DB: `mazes(author VARBINARY(16), slot TINYINT UNSIGNED, title VARCHAR(32), data TEXT, PRIMARY KEY(author, slot))` (`docker/mysql/init/00-schema.sql:31`).
- loadMaze wire conventions to mirror (`srv/includes/loadMaze.php`): `q=<base64(shuffle(pairs))>` in, `r=<base64(shuffle(pairs))>` out, naive swap-shuffle, raw QUERY_STRING parsing for base64 `+` safety.

---

### Task 1: Corpus grid extraction + emit-shape audit

**Files:**
- Create: `tools/extract_maze_grids.py`
- Create (artefact, gitignored): `oracle/editor-roundtrip/grids.json`

**Interfaces:**
- Produces: `python tools/extract_maze_grids.py` writes `oracle/editor-roundtrip/grids.json` = JSON array of unique `d=` strings from the LATEST capture per `(author, slot)` (same latest-wins rule the seed used), and prints an audit: count, reserved-field value histogram, params-content histogram, digit alphabet. Task 3 feeds this file to the harness; Task 4's validator relies on the audit's "reserved always 0, params always empty, digits 0-7" claims — if the audit shows otherwise, STOP and record the finding in DECISIONS.md before proceeding.

- [ ] **Step 1: Write the extractor**

`tools/extract_maze_grids.py`:

```python
#!/usr/bin/env python3
"""Extract unique maze d= grids from the corpus for the round-trip gate.

Latest capture wins per (author, slot) -- the same rule seed/gen_mazes used,
so grids.json matches what is seeded in MySQL. Also audits the emit shape
the editor must reproduce: reserved field, params contents, digit alphabet.
"""
import base64, collections, json, pathlib, re, sys

RAW = pathlib.Path(__file__).resolve().parent.parent / "archive" / "maze-corpus" / "raw"
OUT = pathlib.Path(__file__).resolve().parent.parent / "oracle" / "editor-roundtrip" / "grids.json"


def decode(path):
    raw = path.read_text()
    if not raw.startswith("r="):
        return None
    pairs = {}
    for pair in base64.b64decode(raw[2:]).decode("latin1").split("&"):
        k, _, v = pair.partition("=")
        pairs[k] = v
    return pairs


def main():
    latest = {}   # (n, s) -> (timestamp, d)
    for p in sorted(RAW.iterdir()):          # names sort by timestamp prefix
        pairs = decode(p)
        if pairs is None or "notFound" in pairs:
            continue
        key = (pairs.get("n", ""), pairs.get("s", ""))
        latest[key] = pairs["d"]             # later file overwrites: latest wins

    grids = sorted(set(latest.values()))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(grids, indent=0))

    reserved = collections.Counter()
    params = collections.Counter()
    digits = collections.Counter()
    for d in grids:
        f = d.split("#")
        w, cells, res, n = int(f[0]), f[1], f[2], int(f[3])
        reserved[res] += 1
        digits.update(cells)
        i = 4
        for _ in range(n):
            params[f[i + 3]] += 1
            i += 4
    print(f"states={len(latest)} unique_grids={len(grids)} -> {OUT}")
    print(f"reserved values: {dict(reserved)}")
    print(f"object params values: {dict(params)}")
    print(f"cell digit alphabet: {sorted(digits)}")


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run it and read the audit**

```bash
cd /c/Users/eth/websites/TankTrouble && python tools/extract_maze_grids.py
```

Expected: `unique_grids` ≈ 600+ (672 states, some share grids); `reserved values: {'0': …}` only; params values `{'': …}` only; digit alphabet ⊆ `['0'..'7']`. **If any of the three shows an unexpected value, stop — the emitter in Task 2 must then preserve that field verbatim rather than assume it, and the deviation gets a DECISIONS.md entry.**

- [ ] **Step 3: Add grids.json to the roundtrip dir's .gitignore (created fully in Task 2), commit the tool**

```bash
git add tools/extract_maze_grids.py
git commit -m "feat(tools): extract_maze_grids.py - corpus d= extraction + emit-shape audit"
```

---

### Task 2: MazeData.as — parse/emit ported from the O reader

**Files:**
- Create: `oracle/editor-roundtrip/MazeData.as`
- Create: `oracle/editor-roundtrip/TestHarness.as`
- Create: `oracle/editor-roundtrip/build.sh`
- Create: `oracle/editor-roundtrip/.gitignore`

**Interfaces:**
- Consumes: MTASC invocation pattern from phase 1 (`thirdparty/mtasc/mtasc.exe -version 8 -swf harness.swf -main -header 688:400:25 TestHarness.as MazeData.as`).
- Produces: class `MazeData` with `parse(d:String):Boolean`, `emit():String`, fields `w:Number`, `h:Number`, `floor/wallAbove/wallWest:Array` (2D `[x][y]` of 0/1), `objects:Array` of `{x, y, type, params}` (1-indexed, params raw string), `reservedField:String`. Harness SWF exposes EI callback `roundTrip(d:String):String` returning `emit()` output (or `"PARSE-FAIL"`). Phase 3's editor imports this exact class file — API is frozen by this task.

- [ ] **Step 1: Write MazeData.as**

Port is line-faithful to `MazeDataFetcher.as:67-162` on the parse side; emit reconstructs the corpus shape audited in Task 1:

```actionscript
// Maze d= grid model for the rebuilt mazeCreator (M2, phase 2).
// Parse is a port of the O reader:
//   archive/decompiled/CLASSIC_TankTrouble_v4.0/scripts/__Packages/
//   MazeDataFetcher.as lines 67-162 (bit peel order 4,2,1; y outer, x inner;
//   objects 1-indexed; one terminator field skipped).
// Emit reproduces the corpus shape byte-for-byte (gate:
//   oracle/editor-roundtrip/run_roundtrip.mjs, all corpus grids).

class MazeData {

    var w:Number;
    var h:Number;
    var floor:Array;       // [x][y] 0/1
    var wallAbove:Array;   // [x][y] 0/1 -- wall between (x,y) and (x,y+1); the
                           // WIRE encodes it on the LOWER cell (y+1) as bit 2,
                           // and the O reader stores it on the upper cell.
    var wallWest:Array;    // [x][y] 0/1 -- bit 4 on the cell itself
    var objects:Array;     // {x, y, type, params} -- 1-indexed, params raw
    var reservedField:String;

    function MazeData() { clear(1, 1); }

    function clear(width:Number, height:Number):Void {
        w = width; h = height;
        reservedField = "0";
        objects = [];
        floor = []; wallAbove = []; wallWest = [];
        for (var x:Number = 0; x < w; x++) {
            floor[x] = []; wallAbove[x] = []; wallWest[x] = [];
            for (var y:Number = 0; y < h; y++) {
                floor[x][y] = 0; wallAbove[x][y] = 0; wallWest[x][y] = 0;
            }
        }
    }

    function parse(d:String):Boolean {
        var f:Array = d.split("#");
        var i:Number = 0;
        var width:Number = Number(f[i++]);
        var cells:String = f[i++];
        if (!(width >= 1) || cells.length % width != 0) return false;
        clear(width, cells.length / width);
        reservedField = f[i++];
        var k:Number = 0;
        for (var y:Number = 0; y < h; y++) {
            for (var x:Number = 0; x < w; x++) {
                var v:Number = Number(cells.charAt(k++));
                if (isNaN(v) || v > 7) return false;
                if (v / 4 >= 1) { wallWest[x][y] = 1; v %= 4; }
                if (v / 2 >= 1) { if (y > 0) wallAbove[x][y - 1] = 1; v %= 2; }
                if (v >= 1)     { floor[x][y] = 1; }
            }
        }
        var count:Number = Number(f[i++]);
        if (isNaN(count)) return false;
        objects = [];
        for (var o:Number = 0; o < count; o++) {
            objects.push({ x: Number(f[i++]), y: Number(f[i++]),
                           type: Number(f[i++]), params: String(f[i++]) });
        }
        // O reader: _loc10_ = _loc10_ + 1  -- skips one terminator field
        i++;
        return true;
    }

    function emit():String {
        var cells:String = "";
        for (var y:Number = 0; y < h; y++) {
            for (var x:Number = 0; x < w; x++) {
                var v:Number = 0;
                if (floor[x][y] == 1) v += 1;
                if (y > 0 && wallAbove[x][y - 1] == 1) v += 2;
                if (wallWest[x][y] == 1) v += 4;
                cells += String(v);
            }
        }
        var out:String = w + "#" + cells + "#" + reservedField + "#" + objects.length + "#";
        for (var o:Number = 0; o < objects.length; o++) {
            var ob:Object = objects[o];
            out += ob.x + "#" + ob.y + "#" + ob.type + "#" + ob.params + "#";
        }
        return out + "#0#";
    }
}
```

**Known subtlety the gate must decide:** the parse of bit 2 at `y == 0` — the O reader writes `[x][-1][1]` into a nonexistent slot (AS2 tolerates it silently); the port guards `y > 0`, and emit therefore CANNOT reproduce a `2`/`3`/`6`/`7` digit in row 0. If any corpus grid has bit-2 digits in its first row, round-trip will fail there — that failure is a FINDING (the wire really does carry a dead bit the reader discards), and the fix is to keep a `row0Bit2:Array` verbatim-preservation field. Do not pre-emptively add it; let the gate tell you.

- [ ] **Step 2: Write TestHarness.as + build.sh + .gitignore**

`oracle/editor-roundtrip/TestHarness.as`:

```actionscript
// Round-trip gate harness (phase 2). Exposes MazeData.parse->emit via
// ExternalInterface for run_roundtrip.mjs. Test scaffolding only -- this
// class never ships in the editor SWF.
import flash.external.ExternalInterface;

class TestHarness {
    static function main() {
        ExternalInterface.addCallback("roundTrip", null, function(d:String):String {
            var m:MazeData = new MazeData();
            if (!m.parse(d)) return "PARSE-FAIL";
            return m.emit();
        });
        // visible liveness marker
        var c:MovieClip = _root.createEmptyMovieClip("bg", 1);
        c.beginFill(0x224422);
        c.moveTo(0, 0); c.lineTo(688, 0); c.lineTo(688, 400); c.lineTo(0, 400);
        c.endFill();
    }
}
```

`oracle/editor-roundtrip/build.sh`:

```bash
#!/bin/sh
cd "$(dirname "$0")"
../../thirdparty/mtasc/mtasc.exe -version 8 -swf harness.swf -main -header 688:400:25 TestHarness.as MazeData.as
```

`oracle/editor-roundtrip/.gitignore`:

```
harness.swf
grids.json
results.json
node_modules
```

- [ ] **Step 3: Build**

```bash
cd /c/Users/eth/websites/TankTrouble && sh oracle/editor-roundtrip/build.sh
python tools/swf_header.py oracle/editor-roundtrip/harness.swf   # version=8 stage=688x400px fps=25
```

- [ ] **Step 4: Commit**

```bash
git add oracle/editor-roundtrip/MazeData.as oracle/editor-roundtrip/TestHarness.as oracle/editor-roundtrip/build.sh oracle/editor-roundtrip/.gitignore
git commit -m "feat(oracle): MazeData.as parse/emit ported from O reader + roundtrip harness"
```

---

### Task 3: Round-trip gate under Ruffle — every corpus grid, byte-identical

**Files:**
- Create: `oracle/editor-roundtrip/index.html`
- Create: `oracle/editor-roundtrip/run_roundtrip.mjs`

**Interfaces:**
- Consumes: `harness.swf` (Task 2), `grids.json` (Task 1), the `oracle/ruffle-spike/` rig (Ruffle + puppeteer via junction, phase 1 pattern).
- Produces: `results.json` `{total, pass, fail, failures:[{d, got}]}`; exit code 0 only on `fail == 0`. This is the phase 2 exit gate for the data layer.

- [ ] **Step 1: Write the host page**

`oracle/editor-roundtrip/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>maze roundtrip gate</title>
<script src="../ruffle-spike/ruffle/ruffle.js"></script>
</head>
<body>
<div id="swfhost" style="width:688px;height:400px"></div>
<script>
window.__gate = {};
window.RufflePlayer = window.RufflePlayer || {};
window.RufflePlayer.config = { autoplay: 'on', unmuteOverlay: 'hidden',
                               allowScriptAccess: true, logLevel: 'warn' };
window.addEventListener('load', function () {
  var player = window.RufflePlayer.newest().createPlayer();
  window.__player = player;
  player.style.width = '688px'; player.style.height = '400px';
  document.getElementById('swfhost').appendChild(player);
  player.load('harness.swf')
    .then(function () { window.__gate.loaded = true; })
    .catch(function (e) { window.__gate.loadfail = String(e); });
});
</script>
</body>
</html>
```

- [ ] **Step 2: Write the runner**

`oracle/editor-roundtrip/run_roundtrip.mjs`:

```js
// Phase 2 exit gate: MazeData.parse->emit must reproduce every corpus grid
// byte-for-byte under Ruffle. Run: node run_roundtrip.mjs  (exit 0 = green)

import http from "node:http";
import { readFile } from "node:fs/promises";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";

const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const ORACLE = path.resolve(DIR, "..");
const PORT = 8079;
const MIME = { ".html": "text/html", ".js": "text/javascript",
               ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };

const grids = JSON.parse(readFileSync(path.join(DIR, "grids.json"), "utf8"));

const server = http.createServer(async (req, res) => {
  try {
    const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
    const base = rel.startsWith("ruffle-spike/") ? ORACLE : DIR;
    const body = await readFile(path.join(base, rel));
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
await page.goto(`http://127.0.0.1:${PORT}/index.html`);
await page.waitForFunction("window.__gate && (window.__gate.loaded || window.__gate.loadfail)",
  { timeout: 30000 });
await new Promise(r => setTimeout(r, 1500));

const out = { total: grids.length, pass: 0, fail: 0, failures: [] };
for (const d of grids) {
  const got = await page.evaluate(g => window.__player.roundTrip(g), d);
  if (got === d) out.pass++;
  else { out.fail++; if (out.failures.length < 20) out.failures.push({ d, got }); }
}
writeFileSync(path.join(DIR, "results.json"), JSON.stringify(out, null, 2));
console.log(`roundtrip: ${out.pass}/${out.total} byte-identical, ${out.fail} failures`);
if (out.failures.length) console.log("first failure:", JSON.stringify(out.failures[0], null, 2));
await browser.close(); server.close();
process.exit(out.fail === 0 ? 0 : 1);
```

- [ ] **Step 3: Link node_modules (phase 1 pattern) and run the gate**

```bash
cd /c/Users/eth/websites/TankTrouble/oracle/editor-roundtrip
cmd //c "mklink /J node_modules ..\\ruffle-spike\\node_modules"
node run_roundtrip.mjs
```

Expected: `roundtrip: <N>/<N> byte-identical, 0 failures`, exit 0. If failures appear, diagnose from `results.json` (likely candidates: the row-0 bit-2 subtlety flagged in Task 2, or a reserved/params assumption the Task 1 audit already warned about). Fix `MazeData.as`, rebuild, re-run. Do not proceed until 100%.

- [ ] **Step 4: Commit**

```bash
cd /c/Users/eth/websites/TankTrouble
git add oracle/editor-roundtrip/index.html oracle/editor-roundtrip/run_roundtrip.mjs
git commit -m "feat(oracle): roundtrip gate - corpus grids byte-identical through MazeData under Ruffle"
```

---

### Task 4: saveMaze.php — the M3 save endpoint

**Files:**
- Create: `srv/includes/saveMaze.php`
- Create: `tests/test_savemaze.py`
- Modify: `LEDGER.tsv` (the existing `saveMaze.php` `pending` row → real M3 row)
- Modify: `DECISIONS.md` (append wire-format decision)

**Interfaces:**
- Consumes: `TT_SAVE_MAZE_ENDPOINT` constant in `srv/includes/rebuild-db.php` (already lands there, M3 milestone note); `tt_shuffle_message` convention from `loadMaze.php`; `mazes` table.
- Produces: `POST /includes/saveMaze.php` with body `q=<base64(shuffle("t=<title>&n=<author>&d=<grid>&s=<slot>"))>` → `200` body `r=<base64(shuffle("saved=true&s=<slot>"))>` on success, `r=<base64("error=<code>"))>` on validation failure (codes: `badTitle`, `badAuthor`, `badGrid`, `tooManyObjects`, `badSlot`); `GET` → `405`. Phase 3's editor posts exactly this.

- [ ] **Step 1: Write the failing tests**

`tests/test_savemaze.py` — live-marked (needs the stack), plus one offline stub-guard:

```python
"""saveMaze.php (M3) — invented wire format, validation vs corpus rules.

Live tests POST to the docker stack. The endpoint is INVENTION mirroring
loadMaze.php conventions; these tests pin the invented contract so it
cannot drift silently.
"""
import base64
import pathlib
import re
import urllib.parse
import urllib.request

import pytest

BASE = "http://127.0.0.1:8056"
SRV = pathlib.Path(__file__).resolve().parent.parent / "srv"

VALID_GRID = "4#1111111111111111#0#2#1#1#5##2#2#8###0#"


def post_save(inner):
    q = base64.b64encode(inner.encode()).decode()
    body = urllib.parse.urlencode({"q": q}).encode()
    req = urllib.request.Request(BASE + "/includes/saveMaze.php", data=body, method="POST")
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def decode_r(body):
    assert body.startswith("r="), body
    pairs = {}
    for pair in base64.b64decode(body[2:]).decode("latin1").split("&"):
        k, _, v = pair.partition("=")
        pairs[k] = v
    return pairs


def test_header_is_m3_and_loud():
    src = (SRV / "includes" / "saveMaze.php").read_text()
    assert "@provenance M3" in src
    assert "INVENT" in src.upper()


@pytest.mark.live
def test_get_is_rejected():
    import urllib.error
    try:
        with urllib.request.urlopen(BASE + "/includes/saveMaze.php") as r:
            status = r.status
    except urllib.error.HTTPError as e:
        status = e.code
    assert status == 405


@pytest.mark.live
def test_valid_save_roundtrips_through_loadmaze():
    inner = "t=Gate Test&n=testuser01&d=" + VALID_GRID + "&s=1"
    status, body = post_save(inner)
    assert status == 200
    pairs = decode_r(body)
    assert pairs.get("saved") == "true"
    # read it back through the M1 endpoint: content must match exactly
    q = base64.b64encode(b"userName=testuser01&a=0.1&b=0.2").decode()
    with urllib.request.urlopen(BASE + "/includes/loadMaze.php?q=" + q) as r:
        back = decode_r(r.read().decode())
    assert back["d"] == VALID_GRID
    assert back["t"] == "Gate Test"
    assert back["n"] == "testuser01"


@pytest.mark.live
@pytest.mark.parametrize("inner,code", [
    ("t=" + "x" * 33 + "&n=testuser01&d=" + VALID_GRID + "&s=1", "badTitle"),
    ("t=bad\x01title&n=testuser01&d=" + VALID_GRID + "&s=1", "badTitle"),
    ("t=ok&n=" + "a" * 17 + "&d=" + VALID_GRID + "&s=1", "badAuthor"),
    ("t=ok&n=testuser01&d=19#" + "1" * 19 + "#0#0##0#&s=1", "badGrid"),
    ("t=ok&n=testuser01&d=nonsense&s=1", "badGrid"),
    ("t=ok&n=testuser01&d=2#1111#0#11#" + "1#1#5##" * 11 + "#0#&s=1", "tooManyObjects"),
    ("t=ok&n=testuser01&d=" + VALID_GRID + "&s=0", "badSlot"),
])
def test_invalid_saves_report_error(inner, code):
    status, body = post_save(inner)
    assert status == 200
    assert decode_r(body).get("error") == code
```

- [ ] **Step 2: Run tests to verify the live ones fail (endpoint absent → 404/501)**

```bash
python -m pytest tests/test_savemaze.py -q
```

Expected: `test_header_is_m3_and_loud` FAILS (file missing); live tests FAIL against the stub/404.

- [ ] **Step 3: Write saveMaze.php**

`srv/includes/saveMaze.php`:

```php
<?php
/* @provenance M3
 * @evidence   NONE for the name, method, or wire format - ALL INVENTED.
 *             Deduction chain (DEDUCE.md 3.3): no maze SAJAX function among
 *             the 36 -> the page did not save; recovered JS sets
 *             _root.errorPanel.hide -> the SWF saw the response -> the SWF
 *             posted to a URL that lived only inside the lost
 *             mazeCreator_v0.3.swf. Every fetch channel exhausted.
 * @verified   tests/test_savemaze.py (pins the INVENTED contract only)
 * @written    2026-08-03
 * @caveat     DO NOT PROMOTE. Wire format mirrors loadMaze.php conventions
 *             (q=/r= base64 pair messages, naive swap-shuffle) as the least
 *             inventive choice; the original format is unknowable without
 *             the lost SWF. Validation limits are the corpus-measured
 *             editor constraints (guide 6.5): grid <= 18x10, title <= 32
 *             legal chars, author <= 16, <= 5 tank + <= 5 crate spawns,
 *             <= 10 objects. POST-only is a rebuild-era choice.
 */

require_once dirname(__FILE__) . '/rebuild-db.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('HTTP/1.1 405 Method Not Allowed');
    header('Allow: POST');
    die("RECONSTRUCTION: saveMaze.php accepts POST only (M3 - see header)\n");
}

function tt_save_reply($pairs)
{
    // mirror loadMaze.php: shuffle pair order, base64, r= envelope
    $msg = implode('&', $pairs);
    $parts = explode('&', $msg);
    $n = count($parts);
    for ($i = 0; $i < $n; $i++) {
        $j = mt_rand(0, $n - 1);
        $tmp = $parts[$i]; $parts[$i] = $parts[$j]; $parts[$j] = $tmp;
    }
    echo 'r=' . base64_encode(implode('&', $parts));
    exit;
}

function tt_save_error($code)
{
    echo 'r=' . base64_encode('error=' . $code);
    exit;
}

$q = isset($_POST['q']) ? $_POST['q'] : null;
if ($q === null || $q === '') {
    tt_save_error('badGrid');
}
$decoded = base64_decode(str_replace(' ', '+', $q), true);
if ($decoded === false) {
    tt_save_error('badGrid');
}

$fields = array();
foreach (explode('&', $decoded) as $pair) {
    $kv = explode('=', $pair, 2);
    $fields[$kv[0]] = isset($kv[1]) ? $kv[1] : '';
}

$title  = isset($fields['t']) ? $fields['t'] : '';
$author = isset($fields['n']) ? $fields['n'] : '';
$grid   = isset($fields['d']) ? $fields['d'] : '';
$slot   = isset($fields['s']) ? $fields['s'] : '';

// title: <= 32 chars over the editor's legal set (mazeTitleLegalCharacters,
// srv/index.php:3685 - O evidence for the CHARSET)
if ($title === '' || strlen($title) > 32
        || !preg_match('/^[0-9A-Za-z !,\\-.?]+$/', $title)) {
    tt_save_error('badTitle');
}
// author: <= 16 bytes (schema VARBINARY(16); corpus max 16)
if ($author === '' || strlen($author) > 16) {
    tt_save_error('badAuthor');
}
// slot: positive small int (corpus observed only 1; schema TINYINT UNSIGNED)
if (!preg_match('/^[1-9][0-9]?$/', $slot)) {
    tt_save_error('badSlot');
}

// grid: parse with the same field walk as the O reader (MazeDataFetcher.as)
$f = explode('#', $grid);
if (count($f) < 6) { tt_save_error('badGrid'); }
$w = (int) $f[0];
$cells = $f[1];
if ($w < 1 || $w > 18 || $cells === '' || strlen($cells) % $w !== 0) {
    tt_save_error('badGrid');
}
$h = strlen($cells) / $w;
if ($h < 1 || $h > 10 || !preg_match('/^[0-7]+$/', $cells)) {
    tt_save_error('badGrid');
}
$objCount = (int) $f[3];
if ($objCount > 10) { tt_save_error('tooManyObjects'); }
$idx = 4;
$tanks = 0; $crates = 0;
for ($i = 0; $i < $objCount; $i++) {
    if (!isset($f[$idx + 3])) { tt_save_error('badGrid'); }
    $ox = (int) $f[$idx]; $oy = (int) $f[$idx + 1]; $type = (int) $f[$idx + 2];
    if ($ox < 1 || $ox > $w || $oy < 1 || $oy > $h) { tt_save_error('badGrid'); }
    if ($type === 5) { $tanks++; }
    elseif ($type === 8) { $crates++; }
    else { tt_save_error('badGrid'); }
    $idx += 4;
}
if ($tanks > 5 || $crates > 5) { tt_save_error('tooManyObjects'); }

$sql = sprintf(
    "INSERT INTO mazes (author, slot, title, data) VALUES ('%s', %d, '%s', '%s')"
    . " ON DUPLICATE KEY UPDATE title = VALUES(title), data = VALUES(data)",
    mysql_real_escape_string($author),
    (int) $slot,
    mysql_real_escape_string($title),
    mysql_real_escape_string($grid)
);
if (!mysql_query($sql)) {
    header('HTTP/1.1 500 Internal Server Error');
    die("RECONSTRUCTION: maze insert failed\n");
}

tt_save_reply(array('saved=true', 's=' . (int) $slot));
```

- [ ] **Step 4: Run the tests**

```bash
python -m pytest tests/test_savemaze.py -q
```

Expected: all pass (stack must be up). If a validation case disagrees with the endpoint, fix the ENDPOINT to match the test contract — the tests are the specification of this invention.

- [ ] **Step 5: Update LEDGER.tsv + DECISIONS.md**

In `LEDGER.tsv`, replace the existing `saveMaze.php` `pending` row with (tab-separated, matching the file's column layout):

```
srv/includes/saveMaze.php	M3	—	written 2026-08-03	none - name, method and wire format all invented; deduction chain DEDUCE.md 3.3	tests/test_savemaze.py	DO NOT PROMOTE; format mirrors loadMaze conventions
```

Append to `DECISIONS.md`:

```markdown
## 2026-08-03 — saveMaze.php wire format: mirror loadMaze, POST-only (M3)
Tier: M3 — every choice here is invention; the real format lived only in
the lost mazeCreator_v0.3.swf.
Chosen: POST q=<base64(shuffle("t&n&d&s"))>; reply r=<base64(shuffle(
"saved=true&s="))> or r=<base64("error=<code>")>. Rationale: the era SWF
used LoadVars (POST-default) and the site's only fully-observed endpoint
pair message is loadMaze's q=/r= convention — mirroring it is the least
inventive option. Validation = the corpus-measured constraints (guide 6.5).
Errors are in-band (error=<code>) because the SWF owned an error panel, so
the response had to be machine-readable by the SWF.
Rejected: SAJAX (no maze function among the 36 — evidence against);
GET (write over GET is the vulnerability class 6.4 exists to avoid);
HTTP-status-only errors (panel needs a reason).
Reversible: yes — the editor reads the reply through the same decodeMessage
port, so format changes are one function on each side.
Supersedes: the 2026-08-03 "constant + pending row, NO file" boundary entry
(the constant and its name are unchanged).
```

- [ ] **Step 6: Full gate suite**

```bash
python -m pytest tests/ -q
```

Expected: previous 61 + the new savemaze tests, all green (stack up). Offline check: `python -m pytest tests/ -q -m "not live"` = 35 + `test_header_is_m3_and_loud` = 36.

- [ ] **Step 7: Commit (endpoint + tests + ledger + decision together — one tightly-coupled unit)**

```bash
git add srv/includes/saveMaze.php tests/test_savemaze.py LEDGER.tsv DECISIONS.md
git commit -m "feat(M3): includes/saveMaze.php - invented save endpoint, contract pinned by tests"
```

---

### Task 5: Phase close-out — docs + tag

**Files:**
- Modify: `oracle/DIVERGENCES.md` (round-trip gate result appended to the editor-spike section's log)
- Modify: `docs/superpowers/plans/2026-08-03-mazecreator-phase2-datalayer.md` (tick checkboxes)

**Interfaces:**
- Produces: tag `mazecreator-datalayer-complete`; phase 3 (rendering + tools + gate C visuals) plans on top of the frozen `MazeData` API and the pinned saveMaze contract.

- [ ] **Step 1: Append the gate result to oracle/DIVERGENCES.md**

One dated paragraph: N corpus grids, N/N byte-identical through MazeData under Ruffle 0.4.1, runner path, plus any parse findings the gate surfaced (row-0 bit-2, reserved values, params contents — whatever actually happened).

- [ ] **Step 2: Verify gates one final time**

```bash
python -m pytest tests/ -q -m "not live"        # 36 expected
cd oracle/editor-roundtrip && node run_roundtrip.mjs && cd ../..   # exit 0
```

- [ ] **Step 3: Commit + tag**

```bash
git add oracle/DIVERGENCES.md docs/
git commit -m "docs: phase 2 round-trip gate results + plan checkboxes"
git tag mazecreator-datalayer-complete
```

---

## Out of scope (phase 3+)

- Editor rendering (floor/wall/spawn drawing, title text, version watermark), tools, mouse interaction, error panel, fade, previews state
- Gate C screenshot diff (projector vs Ruffle) for editor visuals
- `userSettingsMazeCreatorInitCode-*` markup + logged-in garage UI
- Toolbar icon redraw (M2 art from `Making a maze.png` + video)

## Self-review notes

- Coverage: guide §6.5 editor constraints → Task 4 validator + Task 1 audit; §6.1a "machine-generated regions invert exactly" ethos → round-trip gate (Task 3); §3.1/3.3 ledger + decision discipline → Task 4 step 5; O-reader fidelity → Task 2 port with line references.
- Types/names consistent: `roundTrip` (Tasks 2, 3); `grids.json` (Tasks 1, 3); error codes `badTitle/badAuthor/badGrid/tooManyObjects/badSlot` (Task 4 tests ↔ endpoint); `VALID_GRID` uses 2 objects on a 4×4 all-floor grid — parses under the Task 2 walk.
- Placeholders: none; every step has runnable content. Data-dependent steps (audit reaction, gate findings) state exactly what to record.
