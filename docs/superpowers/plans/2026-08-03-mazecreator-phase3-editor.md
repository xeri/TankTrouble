# mazeCreator Phase 3 — Editor SWF (rendering + tools + interaction) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the lost `mazeCreator_v0.3.swf` as an AS2/Flash-8 SWF that renders mazes, implements the three editing tools, speaks the full page SetVariable contract, and saves through `saveMaze.php` — shipped into `srv/includes/` with M2 provenance and a gate C projector-vs-Ruffle screenshot diff.

**Architecture:** New `src/mazecreator/` holds the shipping AS2 source (MazeData moved there from the phase 2 oracle, Base64 adapted from the O decompile, new MazeRenderer + Editor classes). A new `oracle/editor-visual/` harness drives the SWF under Ruffle via puppeteer for render, interaction, and save-flow assertions; the phase 1 projector supplies the gate C ground truth. MTASC 1.14 compiles everything (`thirdparty/mtasc/mtasc.exe -version 8 … -header 688:400:25`).

**Tech Stack:** MTASC 1.14 (AS2 → SWF8), Ruffle 0.4.1 + puppeteer-core (Brave headless, `TT_BROWSER` override), Flash projector 32.0.0.465, Python 3 + Pillow for measurement/diff, docker stack at 127.0.0.1:8056 for save-flow tests.

## Global Constraints

- Provenance discipline: `archive/` is READ-ONLY. Never mix archive bytes and written code in one commit. Every `srv/` file needs a LEDGER.tsv row; every M\* file a parseable `@provenance` header. The shipped SWF is **M2** (logic evidence-constrained, pixels redrawn) — never claim O.
- Contract is frozen O evidence (`srv/index.php:3609-3753`): inbound SetVariable `fadeOut`, `newToolRequested` (construct|crateSpawn|tankSpawn), `_root.saveRequested`, `_root.mazeName`, `_root.errorPanel.hide`, `previewLoaded`; SWF-outbound `getURL("javascript:showMazeCreatorToolsAndTitle(user,title)")` and `…hideMazeCreatorToolsAndTitle(user)`. Page JS is NEVER modified.
- Editor limits (corpus, 0 violations): grid ≤ 18×10, title ≤ 32 chars over `[0-9A-Za-z !,\-.?]`, ≤ 5 tank + ≤ 5 crate spawns, ≤ 10 objects, objects only on floor cells.
- Corpus invariants measured 2026-08-03 (670/670 grids, 0 violations — cite in DECISIONS):
  - Grids are tight floor bounding boxes (floor present in row 0, col 0, last row, last col of every grid).
  - Boundary wall bits are fully derived: for any edge with exactly one floor cell on its two sides, the storing cell's bit is 1; for floor-floor edges the bit is free user data (18,148 interior walls); for nonfloor-nonfloor edges the bit is 0. South edge of bottom-row floor and east edge of last-column floor are unstorable — renderer closes them implicitly.
- MazeData API frozen: `parse(d):Boolean`, `emit():String`, `clear(w,h)`, fields `w,h,floor,wallNorth,wallWest,objects,reservedField`. Additions allowed only if `run_roundtrip.mjs` stays 670/670.
- Dual-channel control (phase 1 verdicts): `ExternalInterface.addCallback("SetVariable"/"GetVariable")` for Ruffle; `_root.watch` + a real `_root.errorPanel` object with `watch("hide")` for native SetVariable under projector. EI delivers `_root.`-prefixed names literally — strip the prefix.
- Repo conventions: direct commits to main, milestone tags. Bash tool: prefix `cd /c/Users/eth/websites/TankTrouble` on every command (working dir drifts). Never write cp1252 bytes into tracked text files — heredocs writing files must set UTF-8 explicitly.
- Security: synthetic users only (`testuser01`); grep for credential-shaped strings before push; stack stays 127.0.0.1.

---

### Task 1: Visual spec pinned from the screenshot (M2 evidence)

**Files:**
- Create: `tools/measure_editor_screenshot.py`
- Create: `oracle/editor-visual/gauntlet.json`
- Create: `docs/mazecreator-visual-spec.md`
- Modify: `DECISIONS.md` (append)

**Interfaces:**
- Produces: pinned visual constants (CELL, LATTICE_X/Y, WALL_T, COLOR_\*) consumed verbatim by Task 3's `MazeRenderer` statics; `gauntlet.json` = `{"d": "<wire string>", "title": "Gauntlet"}` consumed by Tasks 3 and 7 as the render test vector.

Pre-measured estimates to validate (from `archive/ia-items/extracted/images/Making a maze.png`, 832×556): capture/stage scale uniform ≈ 1.2023 (guide §6.5's per-axis 1.209/1.390 factors are an artifact of chrome inclusion — cell pitch is identical on both axes, so scale is uniform); cell pitch 32 stage px; wall #444444, ~4 px thick; floor checker #dddddd/#eeeeee; title text #666666; maze in shot is 13×8 cells, bbox capture x 165-668, y 99-410.

- [ ] **Step 1: Write the measurement script**

```python
#!/usr/bin/env python3
"""Measure mazeCreator visual constants from 'Making a maze.png' (M2).

The capture (832x556) is the 692px-wide userpanel at a uniform scale of
~1.2023 (832/692); guide 6.5's per-axis factors (1.209/1.390) came from
dividing by the 688x400 stage, which ignores panel chrome. Wall-run pitch
is ~38.4 capture px on BOTH axes => square cells => uniform scale.

Outputs: pinned constants + a transcription of the shot's maze as a d=
wire string (floor from cell tone, walls from dark runs, objects from
blue/orange blobs).
"""
import json, sys
from collections import Counter
from PIL import Image

IMG = "archive/ia-items/extracted/images/Making a maze.png"
SCALE = 832 / 692.0            # capture px per stage px
CELL_CAP = 32 * SCALE          # expected capture-px cell pitch

im = Image.open(IMG).convert("RGB")
W, H = im.size

def is_dark(p):  return sum(p) < 330          # wall #444444 family
def is_floor(p): return 200 <= p[0] <= 245 and abs(p[0]-p[1]) < 6 and abs(p[1]-p[2]) < 6

# --- 1. maze bbox in capture px (dark pixels, excluding page text bands) ---
xs, ys = [], []
for y in range(40, 470):
    for x in range(0, W):
        if is_dark(im.getpixel((x, y))):
            xs.append(x); ys.append(y)
bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
print(f"maze bbox capture: x {bx0}-{bx1}  y {by0}-{by1}")

# --- 2. fit integer cell count + refine pitch ---
def fit(span):
    best = None
    for n in range(3, 19):
        pitch = span / n
        if 36 <= pitch <= 41:
            err = abs(pitch - CELL_CAP)
            if best is None or err < best[1]:
                best = (n, err, pitch)
    return best
fw = fit(bx1 - bx0); fh = fit(by1 - by0)
gw, gh = fw[0], fh[0]
print(f"grid {gw}x{gh}, pitch x={fw[2]:.2f} y={fh[2]:.2f} capture px "
      f"(stage {fw[2]/SCALE:.2f}/{fh[2]/SCALE:.2f})")

# --- 3. transcribe cells: sample tone at each cell centre ---
def cell_center(cx, cy):
    return (bx0 + (cx + 0.5) * (bx1 - bx0) / gw,
            by0 + (cy + 0.5) * (by1 - by0) / gh)
floor = [[0] * gh for _ in range(gw)]
tones = {}
for cx in range(gw):
    for cy in range(gh):
        x, y = cell_center(cx, cy)
        px = im.getpixel((int(x), int(y)))
        if is_floor(px):
            floor[cx][cy] = 1
            tones[(cx, cy)] = px

# checkerboard parity: which (cx+cy)%2 gets the lighter #eeeeee tone
par = Counter()
for (cx, cy), p in tones.items():
    par[((cx + cy) % 2, p[0] >= 230)] += 1
print("checker parity ((cx+cy)%2, is_light):", par.most_common())

# --- 4. transcribe walls: darkness along each interior edge midline ---
def edge_dark(cx, cy, which):
    if which == "west":
        x = bx0 + cx * (bx1 - bx0) / gw
        y = by0 + (cy + 0.5) * (by1 - by0) / gh
    else:
        x = bx0 + (cx + 0.5) * (bx1 - bx0) / gw
        y = by0 + cy * (by1 - by0) / gh
    hits = 0
    for d in range(-2, 3):
        p = im.getpixel((int(x + (d if which == "north" else 0)),
                         int(y + (d if which == "west" else 0))))
        hits += is_dark(p)
    return hits >= 3
wallN = [[0] * gh for _ in range(gw)]
wallW = [[0] * gh for _ in range(gw)]
for cx in range(gw):
    for cy in range(gh):
        if edge_dark(cx, cy, "north"): wallN[cx][cy] = 1
        if edge_dark(cx, cy, "west"):  wallW[cx][cy] = 1

# --- 5. objects: blue (tank) / orange (crate) blob per cell ---
objs = []
for cx in range(gw):
    for cy in range(gh):
        if not floor[cx][cy]:
            continue
        x0, y0 = cell_center(cx, cy)
        blue = orange = 0
        for dx in range(-12, 13, 2):
            for dy in range(-12, 13, 2):
                r, g, b = im.getpixel((int(x0 + dx), int(y0 + dy)))
                if b > r + 30 and b > 120: blue += 1
                if r > b + 50 and g > b + 10 and r > 150: orange += 1
        if blue > 8:   objs.append((cx + 1, cy + 1, 5))
        elif orange > 8: objs.append((cx + 1, cy + 1, 8))
print("objects (1-indexed x,y,type):", objs)

# sample object colours for the renderer
for name, cond in [("tank-blue", lambda r,g,b: b > r + 30 and b > 120),
                   ("crate-orange", lambda r,g,b: r > b + 50 and r > 150)]:
    cnt = Counter()
    for y in range(by0, by1):
        for x in range(bx0, bx1):
            p = im.getpixel((x, y))
            if cond(*p): cnt[p] += 1
    print(name, "top colours:", cnt.most_common(4))

# --- 6. emit d= (normalized: boundary bits per the 670/670 invariant) ---
cells = ""
for cy in range(gh):
    for cx in range(gw):
        f = floor[cx][cy]
        n = wallN[cx][cy]; w = wallW[cx][cy]
        # force the invariant so the transcription is corpus-shaped
        fa = cy > 0 and floor[cx][cy - 1]
        fl = cx > 0 and floor[cx - 1][cy]
        if f != fa: n = 1
        if not f and not fa: n = 0
        if f != fl: w = 1
        if not f and not fl: w = 0
        cells += str(f + 2 * n + 4 * w)
d = f"{gw}#{cells}#0#{len(objs)}#" + "".join(f"{x}#{y}#{t}##" for x, y, t in objs) + "#0#"
print("d=", d)
json.dump({"d": d, "title": "Gauntlet"},
          open("oracle/editor-visual/gauntlet.json", "w"), indent=1)

# --- 7. title / watermark bands (report capture coords; divide by SCALE) ---
for label, y0, y1 in [("title", 5, 40), ("watermark", 465, 500)]:
    pts = [(x, y) for y in range(y0, y1) for x in range(0, W)
           if is_dark(im.getpixel((x, y))) or
              (100 <= im.getpixel((x, y))[0] <= 190 and
               im.getpixel((x, y))[0] == im.getpixel((x, y))[1] == im.getpixel((x, y))[2])]
    if pts:
        xs2 = [p[0] for p in pts]; ys2 = [p[1] for p in pts]
        print(f"{label}: capture x {min(xs2)}-{max(xs2)} y {min(ys2)}-{max(ys2)} "
              f"-> stage x {min(xs2)/SCALE:.0f}-{max(xs2)/SCALE:.0f} "
              f"y {min(ys2)/SCALE:.0f}-{max(ys2)/SCALE:.0f}")
```

- [ ] **Step 2: Run it** — `cd /c/Users/eth/websites/TankTrouble && mkdir -p oracle/editor-visual && python tools/measure_editor_screenshot.py`. Expect grid 13×8, pitch ≈ 38.4/38.4, and a d= string. If pitch differs per axis by > 0.5 px, stop — the uniform-scale premise is wrong; re-derive before proceeding.

- [ ] **Step 3: Sanity the transcription** — run this inline check (invariant + object caps):

```python
import json
d = json.load(open("oracle/editor-visual/gauntlet.json"))["d"]
f = d.split("#"); w = int(f[0]); cells = f[1]; h = len(cells)//w
assert all(int(c) <= 7 for c in cells)
assert any(int(c)&1 for c in cells[:w]) and any(int(c)&1 for c in cells[(h-1)*w:])
n = int(f[3]); assert n <= 10
print("transcription OK:", w, "x", h, n, "objects")
```

- [ ] **Step 4: Write `docs/mazecreator-visual-spec.md`** recording, with the measured numbers (replace the estimates): scale derivation, CELL (expect 32), lattice origin LATTICE_X/LATTICE_Y (derive: `origin = bbox_left/SCALE - offset*CELL` for integer/half-cell offsets; expect ≈ (56, 50)), WALL_T (expect 4), colors (wall #444444, floor #dddddd/#eeeeee + which parity is light, title #666666, tank blue + crate orange as sampled), title band and watermark band stage coordinates, and the placement note: *original centers the maze bbox on the lattice with half-cell precision; rebuild snaps to integer cells for a fixed editing lattice — divergence recorded, revisit with video evidence.*

- [ ] **Step 5: Append DECISIONS.md entry** (follow the file's existing entry format, dated 2026-08-03): boundary-bit invariant (670/670, four directions, 0 violations — bits derived from floor adjacency except free floor-floor interior walls; grids are tight floor bboxes), visual constants source = screenshot at uniform 1.2023 scale (M2), integer-cell lattice snap divergence.

- [ ] **Step 6: Commit**

```bash
cd /c/Users/eth/websites/TankTrouble && git add tools/measure_editor_screenshot.py oracle/editor-visual/gauntlet.json docs/mazecreator-visual-spec.md DECISIONS.md && git commit -m "docs: phase 3 visual spec measured from screenshot; boundary-bit invariant pinned"
```

---

### Task 2: `src/mazecreator/` source layout — MazeData move + normalizeBoundary + Base64

**Files:**
- Create: `src/mazecreator/MazeData.as` (move from `oracle/editor-roundtrip/MazeData.as`, then extend)
- Create: `src/mazecreator/Base64.as` (adapted from `archive/decompiled/CLASSIC_TankTrouble_v4.0/scripts/__Packages/Base64.as`)
- Modify: `oracle/editor-roundtrip/build.sh` (classpath)
- Modify: `oracle/editor-roundtrip/run_roundtrip.mjs` (add normalize pass)
- Modify: `oracle/editor-roundtrip/TestHarness.as` (add normalize hook)

**Interfaces:**
- Consumes: frozen MazeData API.
- Produces: `MazeData.normalizeBoundary():Void` (recomputes boundary bits from floor adjacency, preserves floor-floor bits, zeroes nonfloor-nonfloor bits); `Base64.Encode(str:String):String` / `Base64.Decode(str:String):String` compiled under MTASC. Tasks 4-5 import both.

- [ ] **Step 1: Move MazeData** — `cd /c/Users/eth/websites/TankTrouble && mkdir -p src/mazecreator && git mv oracle/editor-roundtrip/MazeData.as src/mazecreator/MazeData.as`

- [ ] **Step 2: Point the roundtrip build at it** — edit `oracle/editor-roundtrip/build.sh` line 3 to:

```sh
../../thirdparty/mtasc/mtasc.exe -version 8 -cp ../../src/mazecreator -swf harness.swf -main -header 688:400:25 TestHarness.as
```

- [ ] **Step 3: Rebuild + re-run the gate untouched** — `cd /c/Users/eth/websites/TankTrouble/oracle/editor-roundtrip && sh build.sh && node run_roundtrip.mjs`. Expected: `roundtrip: 670/670 byte-identical, 0 failures`.

- [ ] **Step 4: Add the failing normalize pass.** In `TestHarness.as` main, add a second callback after the existing one:

```actionscript
        ExternalInterface.addCallback("roundTripNormalized", null, function(d:String):String {
            var m:MazeData = new MazeData();
            if (!m.parse(d)) return "PARSE-FAIL";
            m.normalizeBoundary();
            return m.emit();
        });
```

In `run_roundtrip.mjs`, after the existing loop add:

```javascript
const norm = { pass: 0, fail: 0, failures: [] };
for (const d of grids) {
  const got = await page.evaluate(g => window.__player.roundTripNormalized(g), d);
  if (got === d) norm.pass++;
  else { norm.fail++; if (norm.failures.length < 5) norm.failures.push({ d, got }); }
}
console.log(`normalize no-op: ${norm.pass}/${grids.length}, ${norm.fail} failures`);
if (norm.failures.length) console.log("first:", JSON.stringify(norm.failures[0]));
```

and change the exit line to `process.exit(out.fail === 0 && norm.fail === 0 ? 0 : 1);`

- [ ] **Step 5: Run to verify it fails** — `sh build.sh` should fail compile with "Unknown variable normalizeBoundary" (method missing).

- [ ] **Step 6: Implement `normalizeBoundary` in `src/mazecreator/MazeData.as`** (append inside the class; comment cites the invariant):

```actionscript
    // Corpus law (670/670 grids, DECISIONS 2026-08-03): a wall bit whose edge
    // borders exactly one floor cell is always 1; between two floors it is
    // free user data; between two non-floors it is always 0. Editing code
    // calls this after floor changes so emit() stays corpus-shaped.
    function normalizeBoundary():Void {
        for (var x:Number = 0; x < w; x++) {
            for (var y:Number = 0; y < h; y++) {
                var f:Number = floor[x][y];
                var fa:Number = (y > 0) ? floor[x][y - 1] : 0;
                var fl:Number = (x > 0) ? floor[x - 1][y] : 0;
                if (f != fa) wallNorth[x][y] = 1;
                else if (f == 0) wallNorth[x][y] = 0;
                if (f != fl) wallWest[x][y] = 1;
                else if (f == 0) wallWest[x][y] = 0;
            }
        }
    }
```

- [ ] **Step 7: Run the gate** — `sh build.sh && node run_roundtrip.mjs`. Expected: `roundtrip: 670/670 … 0 failures` AND `normalize no-op: 670/670, 0 failures` (proves both the invariant and the implementation).

- [ ] **Step 8: Create `src/mazecreator/Base64.as`** — copy `archive/decompiled/CLASSIC_TankTrouble_v4.0/scripts/__Packages/Base64.as` verbatim, then add this header comment ABOVE the class and fix only what MTASC rejects (record each fix in the header):

```actionscript
// @provenance M2 -- decompiled from O bytes (archive/decompiled/CLASSIC_
// TankTrouble_v4.0/scripts/__Packages/Base64.as, JPEXS output). The era
// client ships this exact class; the rebuilt editor reuses it so encode/
// decode behaviour matches the original page<->SWF traffic. MTASC
// compatibility edits (if any) listed here:
//   - (none yet)
```

- [ ] **Step 9: Compile check** — `cd /c/Users/eth/websites/TankTrouble/src/mazecreator && ../../thirdparty/mtasc/mtasc.exe -version 8 -swf /tmp/b64check.swf -header 688:400:25 Base64.as MazeData.as` (note: scratch output; MTASC without `-main` just compiles classes). Expected: exit 0. If MTASC rejects decompiled idioms (untyped statics are usually fine; `var` redeclaration or reserved words are not), make the minimal edit and list it in the header.

- [ ] **Step 10: Commit**

```bash
cd /c/Users/eth/websites/TankTrouble && git add -A src/mazecreator oracle/editor-roundtrip && git commit -m "feat: src/mazecreator layout - MazeData moved + normalizeBoundary (670/670 no-op), Base64 from O decompile"
```

---

### Task 3: MazeRenderer + visual harness

**Files:**
- Create: `src/mazecreator/MazeRenderer.as`
- Create: `oracle/editor-visual/RenderHarness.as`
- Create: `oracle/editor-visual/build.sh`
- Create: `oracle/editor-visual/index.html`
- Create: `oracle/editor-visual/run_visual.mjs`
- Create: `oracle/editor-visual/.gitignore` (`harness.swf`, `editor.swf`, `*.png`, `node_modules`, `results.json`)
- Create: `tools/diff_render.py`

**Interfaces:**
- Consumes: `MazeData` (Task 2), constants from `docs/mazecreator-visual-spec.md` (Task 1 — substitute measured values if they differ from the literals below).
- Produces: `MazeRenderer.CELL/LATTICE_X/LATTICE_Y/LATTICE_W/LATTICE_H/WALL_T` statics; `MazeRenderer.render(mc:MovieClip, data:MazeData, offX:Number, offY:Number):Void` where offX/offY are CELL-multiples added to the lattice origin; `MazeRenderer.cellOffsetFor(data:MazeData):Object` returning `{cx:Number, cy:Number}` integer centering offsets. Task 4 builds on all three. `tools/diff_render.py <a.png> <b.png> <out.png> [--mask x,y,w,h]...` prints `mean=<f> max=<i> pct_over_32=<f>` — reused by gate C in Task 7.

- [ ] **Step 1: Write `src/mazecreator/MazeRenderer.as`** (constants below are Task 1's estimates — use the measured values from docs/mazecreator-visual-spec.md where they differ):

```actionscript
// Maze rendering for the rebuilt mazeCreator (M2). Geometry + palette
// measured from archive/ia-items/extracted/images/"Making a maze.png"
// (docs/mazecreator-visual-spec.md). Wire semantics per MazeData: wall
// bits draw where stored; the unstorable south/east closure edges (floor
// at lattice bottom/right or beside grid end) derive from floor adjacency.
class MazeRenderer {

    static var CELL:Number = 32;
    static var LATTICE_X:Number = 56;
    static var LATTICE_Y:Number = 50;
    static var LATTICE_W:Number = 18;
    static var LATTICE_H:Number = 10;
    static var WALL_T:Number = 4;
    static var COLOR_WALL:Number = 0x444444;
    static var COLOR_FLOOR_A:Number = 0xEEEEEE;  // (cx+cy) even  -- confirm parity vs spec
    static var COLOR_FLOOR_B:Number = 0xDDDDDD;
    static var COLOR_TANK:Number = 0x7777CC;
    static var COLOR_CRATE:Number = 0xDDaa44;
    static var COLOR_CRATE_EDGE:Number = 0xAA7722;

    static function cellOffsetFor(data:MazeData):Object {
        return { cx: Math.floor((LATTICE_W - data.w) / 2),
                 cy: Math.floor((LATTICE_H - data.h) / 2) };
    }

    static function render(mc:MovieClip, data:MazeData, offX:Number, offY:Number):Void {
        mc.clear();
        var ox:Number = LATTICE_X + offX * CELL;
        var oy:Number = LATTICE_Y + offY * CELL;
        var x:Number; var y:Number;
        // floors (checkerboard keyed to LATTICE coords so tiles do not
        // change tone when the maze grows leftward/upward)
        for (x = 0; x < data.w; x++) {
            for (y = 0; y < data.h; y++) {
                if (data.floor[x][y] != 1) continue;
                var tone:Number = (((x + offX) + (y + offY)) % 2 == 0)
                    ? COLOR_FLOOR_A : COLOR_FLOOR_B;
                mc.beginFill(tone);
                boxAt(mc, ox + x * CELL, oy + y * CELL, CELL, CELL);
                mc.endFill();
            }
        }
        // walls: stored bits, then the unstorable south/east closures
        mc.beginFill(COLOR_WALL);
        for (x = 0; x < data.w; x++) {
            for (y = 0; y < data.h; y++) {
                if (data.wallNorth[x][y] == 1)
                    boxAt(mc, ox + x * CELL - WALL_T / 2, oy + y * CELL - WALL_T / 2,
                          CELL + WALL_T, WALL_T);
                if (data.wallWest[x][y] == 1)
                    boxAt(mc, ox + x * CELL - WALL_T / 2, oy + y * CELL - WALL_T / 2,
                          WALL_T, CELL + WALL_T);
                if (data.floor[x][y] == 1 && (y == data.h - 1 || data.floor[x][y + 1] != 1))
                    boxAt(mc, ox + x * CELL - WALL_T / 2, oy + (y + 1) * CELL - WALL_T / 2,
                          CELL + WALL_T, WALL_T);
                if (data.floor[x][y] == 1 && (x == data.w - 1 || data.floor[x + 1][y] != 1))
                    boxAt(mc, ox + (x + 1) * CELL - WALL_T / 2, oy + y * CELL - WALL_T / 2,
                          WALL_T, CELL + WALL_T);
            }
        }
        mc.endFill();
        // objects -- 1-indexed cells; deterministic pseudo-random angle so
        // projector and Ruffle render identically (gate C)
        for (var o:Number = 0; o < data.objects.length; o++) {
            var ob:Object = data.objects[o];
            var cxp:Number = ox + (ob.x - 1) * CELL + CELL / 2;
            var cyp:Number = oy + (ob.y - 1) * CELL + CELL / 2;
            var ang:Number = ((ob.x * 53 + ob.y * 97) % 360) * Math.PI / 180;
            if (ob.type == 8) drawCrate(mc, cxp, cyp, ang);
            else drawTank(mc, cxp, cyp, ang);
        }
    }

    static function boxAt(mc:MovieClip, x:Number, y:Number, w:Number, h:Number):Void {
        mc.moveTo(x, y); mc.lineTo(x + w, y); mc.lineTo(x + w, y + h);
        mc.lineTo(x, y + h); mc.lineTo(x, y);
    }

    // rotated square, 14px half-diagonal footprint like the shot's crates
    static function drawCrate(mc:MovieClip, cx:Number, cy:Number, ang:Number):Void {
        mc.lineStyle(2, COLOR_CRATE_EDGE);
        mc.beginFill(COLOR_CRATE);
        poly(mc, cx, cy, [[-8,-8],[8,-8],[8,8],[-8,8]], ang);
        mc.endFill();
        mc.lineStyle();
    }

    // top-view tank: hull + two tracks + barrel, outline-heavy like the shot
    static function drawTank(mc:MovieClip, cx:Number, cy:Number, ang:Number):Void {
        mc.lineStyle(2, COLOR_TANK);
        mc.beginFill(0xFFFFFF, 60);
        poly(mc, cx, cy, [[-7,-9],[7,-9],[7,9],[-7,9]], ang);   // hull
        mc.endFill();
        poly(mc, cx, cy, [[-10,-9],[-7,-9],[-7,9],[-10,9]], ang); // left track
        poly(mc, cx, cy, [[7,-9],[10,-9],[10,9],[7,9]], ang);     // right track
        poly(mc, cx, cy, [[-1,-14],[1,-14],[1,0],[-1,0]], ang);   // barrel
        mc.lineStyle();
    }

    static function poly(mc:MovieClip, cx:Number, cy:Number, pts:Array, ang:Number):Void {
        var c:Number = Math.cos(ang); var s:Number = Math.sin(ang);
        for (var i:Number = 0; i <= pts.length; i++) {
            var p:Array = pts[i % pts.length];
            var px:Number = cx + p[0] * c - p[1] * s;
            var py:Number = cy + p[0] * s + p[1] * c;
            if (i == 0) mc.moveTo(px, py); else mc.lineTo(px, py);
        }
    }
}
```

- [ ] **Step 2: Write `oracle/editor-visual/RenderHarness.as`**:

```actionscript
// Visual gate harness (phase 3). Renders an arbitrary d= via EI for
// run_visual.mjs screenshots. Never ships.
import flash.external.ExternalInterface;

class RenderHarness {
    static function main() {
        var bg:MovieClip = _root.createEmptyMovieClip("bg", 1);
        bg.beginFill(0xFFFFFF);
        bg.moveTo(0, 0); bg.lineTo(688, 0); bg.lineTo(688, 400); bg.lineTo(0, 400);
        bg.endFill();
        var maze:MovieClip = _root.createEmptyMovieClip("maze", 2);
        ExternalInterface.addCallback("renderMaze", null, function(d:String):String {
            var m:MazeData = new MazeData();
            if (!m.parse(d)) return "PARSE-FAIL";
            var off:Object = MazeRenderer.cellOffsetFor(m);
            MazeRenderer.render(maze, m, off.cx, off.cy);
            return "ok";
        });
    }
}
```

- [ ] **Step 3: Write `oracle/editor-visual/build.sh`**:

```sh
#!/bin/sh
cd "$(dirname "$0")"
../../thirdparty/mtasc/mtasc.exe -version 8 -cp ../../src/mazecreator -swf harness.swf -main -header 688:400:25 RenderHarness.as
```

- [ ] **Step 4: Write `oracle/editor-visual/index.html`** — copy `oracle/editor-roundtrip/index.html` exactly, but add `<style>body{margin:0}</style>` in the head (page coords must equal stage coords for later mouse tests) and keep loading `harness.swf`.

- [ ] **Step 5: Write `oracle/editor-visual/run_visual.mjs`** (same server pattern as run_roundtrip.mjs — port 8081):

```javascript
// Renders gauntlet.json under Ruffle, screenshots to ruffle_render.png.
import http from "node:http";
import { readFile } from "node:fs/promises";
import { readFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";

const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const ORACLE = path.resolve(DIR, "..");
const PORT = 8081;
const MIME = { ".html": "text/html", ".js": "text/javascript",
               ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };

const gauntlet = JSON.parse(readFileSync(path.join(DIR, "gauntlet.json"), "utf8"));

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
  args: ["--no-first-run", "--force-device-scale-factor=1"] });
const page = await browser.newPage();
await page.setViewport({ width: 688, height: 400 });
await page.goto(`http://127.0.0.1:${PORT}/index.html`);
await page.waitForFunction("window.__gate && (window.__gate.loaded || window.__gate.loadfail)",
  { timeout: 30000 });
await new Promise(r => setTimeout(r, 1500));

const verdict = await page.evaluate(d => window.__player.renderMaze(d), gauntlet.d);
console.log("renderMaze:", verdict);
await new Promise(r => setTimeout(r, 500));
await page.screenshot({ path: path.join(DIR, "ruffle_render.png") });
await browser.close(); server.close();
process.exit(verdict === "ok" ? 0 : 1);
```

- [ ] **Step 6: Link node_modules + build + run** — `cd /c/Users/eth/websites/TankTrouble/oracle/editor-visual && cmd //c "mklink /J node_modules ..\\ruffle-spike\\node_modules" && sh build.sh && node run_visual.mjs`. Expected: `renderMaze: ok`, exit 0, `ruffle_render.png` written.

- [ ] **Step 7: Eyeball + measure against the screenshot.** Write `tools/diff_render.py`:

```python
#!/usr/bin/env python3
"""Tolerance diff between two renders. Usage:
   python tools/diff_render.py a.png b.png out.png [--mask x,y,w,h]...
Masked rects are ignored (text antialiasing differs across renderers).
Prints mean/max channel delta and % of pixels with delta > 32."""
import sys
from PIL import Image, ImageChops

args = [a for a in sys.argv[1:] if not a.startswith("--mask")]
masks = [tuple(int(v) for v in a.split("=", 1)[1].split(","))
         for a in sys.argv[1:] if a.startswith("--mask")]
a = Image.open(args[0]).convert("RGB")
b = Image.open(args[1]).convert("RGB").resize(a.size)
for x, y, w, h in masks:
    blk = Image.new("RGB", (w, h))
    a.paste(blk, (x, y)); b.paste(blk, (x, y))
diff = ImageChops.difference(a, b)
px = list(diff.getdata())
deltas = [max(p) for p in px]
mean = sum(deltas) / len(deltas)
over = sum(1 for d in deltas if d > 32) / len(deltas) * 100
diff.save(args[2])
print(f"mean={mean:.2f} max={max(deltas)} pct_over_32={over:.2f}")
```

Then Read `oracle/editor-visual/ruffle_render.png` and compare it visually against the maze region of `Making a maze.png` — cell tones, wall weight, object shapes, checker parity. Style match is the bar here, not pixel identity (the reference is upscaled/compressed and the lattice snap shifts placement). Fix renderer constants if tones/weights are visibly off.

- [ ] **Step 8: Commit**

```bash
cd /c/Users/eth/websites/TankTrouble && git add src/mazecreator/MazeRenderer.as oracle/editor-visual tools/diff_render.py && git commit -m "feat: MazeRenderer + Ruffle visual harness renders corpus-format mazes"
```

---

### Task 4: Editor shell — boot, states, control vocabulary, interaction

**Files:**
- Create: `src/mazecreator/Editor.as`
- Create: `src/mazecreator/build.sh`
- Modify: `oracle/editor-visual/index.html` (load `editor.swf` with initCode)
- Create: `oracle/editor-visual/run_editor.mjs`

**Interfaces:**
- Consumes: `MazeData` + `normalizeBoundary` (Task 2), `Base64.Encode/Decode` (Task 2), `MazeRenderer.render/cellOffsetFor` + statics (Task 3).
- Produces: `Editor` main class with: EI `SetVariable(name,value)` / `GetVariable(name)` where GetVariable answers `mazeD` (cropped, normalized emit), `state` ("preview"|"edit"), `tool`, `titleText`, `errorVisible` ("true"|"false"), `stageAlpha`; states + save hook `doSave()` stub replaced in Task 5. initCode fields (M3, minimal — phase 4 may extend): `u` (panel user id), `n` (author userName), `t` (title), `d` (grid), `s` (slot).

Behavior spec (M3 inventions — DECISIONS entry lands in Task 7):
- Boot: decode `initCode` FlashVar with `Base64.Decode` + the O `decodeMessage` split. No `d` → blank 18×10 lattice, title "". With `d` → parse into an 18×10 lattice at `cellOffsetFor` position (copy parsed cells/objects in at the offset). State = preview. If `ExternalInterface.available` → `_alpha = 0` awaiting `fadeOut=false` (page fades it in at +1200 ms); else (projector) boot visible.
- Preview state: renders maze, plus title text; click anywhere → state=edit, `getURL("javascript:showMazeCreatorToolsAndTitle('<u>','<title>')")`.
- Edit state, construct tool: click within 6 px of an interior gridline between two floor cells toggles that stored wall bit; otherwise click toggles the cell's floor (clearing a floor cell also deletes any object on it); after any floor change call `normalizeBoundary()` on the lattice.
- Edit state, tankSpawn/crateSpawn: click a floor cell → toggle object (type 5/8) at that 1-indexed cell; adding is refused beyond 5 of that type or 10 total.
- `mazeName` → set title (render); `errorPanel.hide` = "yes" → hide panel; `previewLoaded` → state=preview; `fadeOut` "true"/"false" → 15-frame fade (comment evidence `15frames/25fps`, srv/index.php:3637) toward 0/100 alpha via onEnterFrame ±100/15 per frame.
- Watermark: "version 0.3" bottom-right per spec band; title centered top band; both device-font TextFields (`_sans`), colors per spec.
- Native-channel coverage: `_root.watch` on `newToolRequested`, `saveRequested`, `mazeName`, `previewLoaded`, `fadeOut`; `_root.errorPanel` is a plain object `{ hide: "" }` with `watch("hide", …)` so projector-side `SetVariable('_root.errorPanel.hide','yes')` lands. EI names arrive literal (`_root.mazeName`) — strip the `_root.` prefix before routing; route `errorPanel.hide` by exact string.

- [ ] **Step 1: Write `src/mazecreator/Editor.as`**:

```actionscript
// The rebuilt mazeCreator (M2). Contract is O evidence (srv/index.php:
// 3609-3753): inbound SetVariable fadeOut/newToolRequested/_root.
// saveRequested/_root.mazeName/_root.errorPanel.hide/previewLoaded;
// outbound getURL javascript show/hideMazeCreatorToolsAndTitle. Dual
// channel per oracle/editor-spike verdicts. Interaction model + initCode
// fields are M3 (DECISIONS 2026-08-03); visuals M2 per
// docs/mazecreator-visual-spec.md.
import flash.external.ExternalInterface;

class Editor {

    static var app:Editor;
    static function main() { app = new Editor(); }

    static var SAVE_ENDPOINT:String = "saveMaze.php"; // sibling of the SWF in includes/
    static var EDGE_TOL:Number = 6;

    var data:MazeData;          // full 18x10 editing lattice
    var state:String;           // "preview" | "edit"
    var tool:String;            // construct | crateSpawn | tankSpawn
    var title:String;
    var userId:String; var userName:String; var slot:String;
    var errorVisible:Boolean;
    var fadeTarget:Number;

    var mazeMc:MovieClip; var panelMc:MovieClip;
    var titleTf:TextField; var panelTf:TextField;

    function Editor() {
        var init:Object = decodeInit(String(_root.initCode));
        userId = (init.u != undefined) ? String(init.u) : "";
        userName = (init.n != undefined) ? String(init.n) : "";
        title = (init.t != undefined) ? String(init.t) : "";
        slot = (init.s != undefined) ? String(init.s) : "1";

        data = new MazeData();
        data.clear(MazeRenderer.LATTICE_W, MazeRenderer.LATTICE_H);
        if (init.d != undefined && String(init.d) != "") loadIntoLattice(String(init.d));

        state = "preview";
        tool = "construct";
        errorVisible = false;

        buildStage();
        wireChannels();

        // page embeds us hidden and fades us in at +1200ms; standalone
        // projector has no page, so boot visible there.
        if (ExternalInterface.available) { _root._alpha = 0; fadeTarget = 0; }
        else { _root._alpha = 100; fadeTarget = 100; }
        var owner:Editor = this;
        _root.onEnterFrame = function() { owner.fadeStep(); };
        _root.onMouseDown = function() { owner.onClick(_root._xmouse, _root._ymouse); };
        redraw();
    }

    // ---- boot helpers -------------------------------------------------
    function decodeInit(code:String):Object {
        var o:Object = {};
        if (code == "undefined" || code == null || code == "") return o;
        var pairs:Array = Base64.Decode(code).split("&");
        for (var i:Number = 0; i < pairs.length; i++) {
            var kv:Array = pairs[i].split("=");
            o[kv[0]] = kv[1];
        }
        return o;
    }

    function loadIntoLattice(d:String):Void {
        var m:MazeData = new MazeData();
        if (!m.parse(d)) return;
        var off:Object = MazeRenderer.cellOffsetFor(m);
        for (var x:Number = 0; x < m.w; x++) {
            for (var y:Number = 0; y < m.h; y++) {
                data.floor[x + off.cx][y + off.cy] = m.floor[x][y];
                data.wallNorth[x + off.cx][y + off.cy] = m.wallNorth[x][y];
                data.wallWest[x + off.cx][y + off.cy] = m.wallWest[x][y];
            }
        }
        for (var o:Number = 0; o < m.objects.length; o++) {
            var ob:Object = m.objects[o];
            data.objects.push({ x: ob.x + off.cx, y: ob.y + off.cy,
                                type: ob.type, params: ob.params });
        }
        data.reservedField = m.reservedField;
        data.normalizeBoundary();
    }

    // crop the lattice back to the corpus shape: tight floor bbox,
    // boundary bits normalized (670/670 invariant)
    function cropToFloorBbox():MazeData {
        var x0:Number = 999; var x1:Number = -1; var y0:Number = 999; var y1:Number = -1;
        for (var x:Number = 0; x < data.w; x++)
            for (var y:Number = 0; y < data.h; y++)
                if (data.floor[x][y] == 1) {
                    if (x < x0) x0 = x; if (x > x1) x1 = x;
                    if (y < y0) y0 = y; if (y > y1) y1 = y;
                }
        var out:MazeData = new MazeData();
        if (x1 < 0) { out.clear(1, 1); return out; }
        out.clear(x1 - x0 + 1, y1 - y0 + 1);
        for (x = x0; x <= x1; x++)
            for (y = y0; y <= y1; y++) {
                out.floor[x - x0][y - y0] = data.floor[x][y];
                out.wallNorth[x - x0][y - y0] = data.wallNorth[x][y];
                out.wallWest[x - x0][y - y0] = data.wallWest[x][y];
            }
        for (var o:Number = 0; o < data.objects.length; o++) {
            var ob:Object = data.objects[o];
            out.objects.push({ x: ob.x - x0, y: ob.y - y0, type: ob.type, params: ob.params });
        }
        out.normalizeBoundary();
        return out;
    }

    // ---- control channels ---------------------------------------------
    function wireChannels():Void {
        var owner:Editor = this;
        ExternalInterface.addCallback("SetVariable", null,
            function(n:String, v:String) { owner.onSetVariable(n, v); });
        ExternalInterface.addCallback("GetVariable", null,
            function(n:String):String { return owner.getVar(n); });
        var names:Array = ["newToolRequested", "saveRequested", "mazeName",
                           "previewLoaded", "fadeOut"];
        for (var i:Number = 0; i < names.length; i++) {
            _root.watch(names[i], function(prop, oldVal, newVal) {
                owner.onSetVariable(String(prop), String(newVal)); return newVal;
            });
        }
        _root.errorPanel = { hide: "" };
        _root.errorPanel.watch("hide", function(prop, oldVal, newVal) {
            owner.onSetVariable("errorPanel.hide", String(newVal)); return newVal;
        });
    }

    function onSetVariable(name:String, value:String):Void {
        if (name.substr(0, 6) == "_root.") name = name.substr(6);
        if (name == "fadeOut") fadeTarget = (value == "true") ? 0 : 100;
        else if (name == "newToolRequested") {
            if (value == "construct" || value == "crateSpawn" || value == "tankSpawn")
                tool = value;
        }
        else if (name == "mazeName") { title = value; hideError(); redraw(); }
        else if (name == "errorPanel.hide") { if (value == "yes") hideError(); }
        else if (name == "previewLoaded") { state = "preview"; redraw(); }
        else if (name == "saveRequested") { if (value == "true") doSave(); }
    }

    function getVar(name:String):String {
        if (name == "mazeD") return cropToFloorBbox().emit();
        if (name == "state") return state;
        if (name == "tool") return tool;
        if (name == "titleText") return title;
        if (name == "errorVisible") return errorVisible ? "true" : "false";
        if (name == "stageAlpha") return String(Math.round(_root._alpha));
        return "";
    }

    // ---- interaction ---------------------------------------------------
    function onClick(mx:Number, my:Number):Void {
        if (_root._alpha < 50) return;
        if (state == "preview") {
            state = "edit";
            getURL("javascript:showMazeCreatorToolsAndTitle('" + userId + "','"
                   + title + "')");
            redraw();
            return;
        }
        var lx:Number = mx - MazeRenderer.LATTICE_X;
        var ly:Number = my - MazeRenderer.LATTICE_Y;
        var C:Number = MazeRenderer.CELL;
        if (lx < -EDGE_TOL || ly < -EDGE_TOL) return;
        var cx:Number = Math.floor(lx / C);
        var cy:Number = Math.floor(ly / C);
        if (cx >= data.w || cy >= data.h) return;
        if (tool == "construct") {
            var dx:Number = lx - cx * C;   // 0..C within the cell
            var dy:Number = ly - cy * C;
            // near a vertical interior gridline between two floor cells?
            if (dx < EDGE_TOL && cx > 0
                && data.floor[cx][cy] == 1 && data.floor[cx - 1][cy] == 1)
                data.wallWest[cx][cy] = 1 - data.wallWest[cx][cy];
            else if (dx > C - EDGE_TOL && cx < data.w - 1
                && data.floor[cx][cy] == 1 && data.floor[cx + 1][cy] == 1)
                data.wallWest[cx + 1][cy] = 1 - data.wallWest[cx + 1][cy];
            else if (dy < EDGE_TOL && cy > 0
                && data.floor[cx][cy] == 1 && data.floor[cx][cy - 1] == 1)
                data.wallNorth[cx][cy] = 1 - data.wallNorth[cx][cy];
            else if (dy > C - EDGE_TOL && cy < data.h - 1
                && data.floor[cx][cy] == 1 && data.floor[cx][cy + 1] == 1)
                data.wallNorth[cx][cy + 1] = 1 - data.wallNorth[cx][cy + 1];
            else {
                data.floor[cx][cy] = 1 - data.floor[cx][cy];
                if (data.floor[cx][cy] == 0) removeObjectAt(cx + 1, cy + 1);
                data.normalizeBoundary();
            }
        } else {
            if (data.floor[cx][cy] != 1) return;
            var t:Number = (tool == "tankSpawn") ? 5 : 8;
            if (!removeObjectAt(cx + 1, cy + 1)) {
                var tanks:Number = 0; var crates:Number = 0;
                for (var i:Number = 0; i < data.objects.length; i++) {
                    if (data.objects[i].type == 5) tanks++; else crates++;
                }
                if (data.objects.length >= 10) return;
                if (t == 5 && tanks >= 5) return;
                if (t == 8 && crates >= 5) return;
                data.objects.push({ x: cx + 1, y: cy + 1, type: t, params: "" });
            }
        }
        redraw();
    }

    function removeObjectAt(x1:Number, y1:Number):Boolean {
        for (var i:Number = 0; i < data.objects.length; i++) {
            if (data.objects[i].x == x1 && data.objects[i].y == y1) {
                data.objects.splice(i, 1); return true;
            }
        }
        return false;
    }

    // ---- save (completed in Task 5) -------------------------------------
    function doSave():Void { }

    // ---- display ---------------------------------------------------------
    function buildStage():Void {
        var bg:MovieClip = _root.createEmptyMovieClip("bg", 1);
        bg.beginFill(0xFFFFFF);
        bg.moveTo(0, 0); bg.lineTo(688, 0); bg.lineTo(688, 400); bg.lineTo(0, 400);
        bg.endFill();
        mazeMc = _root.createEmptyMovieClip("maze", 2);

        _root.createTextField("titleTf", 3, 0, 6, 688, 28);
        titleTf = _root.titleTf;
        var tfm:TextFormat = new TextFormat();
        tfm.font = "_sans"; tfm.size = 18; tfm.color = 0x666666; tfm.align = "center";
        titleTf.setNewTextFormat(tfm); titleTf.selectable = false;

        _root.createTextField("versionTf", 4, 488, 378, 190, 20);
        var vf:TextFormat = new TextFormat();
        vf.font = "_sans"; vf.size = 12; vf.color = 0x999999; vf.align = "right";
        vf.letterSpacing = 2;
        _root.versionTf.setNewTextFormat(vf);
        _root.versionTf.selectable = false;
        _root.versionTf.text = "version 0.3";

        panelMc = _root.createEmptyMovieClip("panel", 5);
        panelMc.beginFill(0x444444, 90);
        panelMc.moveTo(144, 160); panelMc.lineTo(544, 160);
        panelMc.lineTo(544, 240); panelMc.lineTo(144, 240);
        panelMc.endFill();
        panelMc.createTextField("msg", 1, 154, 185, 380, 40);
        panelTf = panelMc.msg;
        var pf:TextFormat = new TextFormat();
        pf.font = "_sans"; pf.size = 14; pf.color = 0xFFFFFF; pf.align = "center";
        panelTf.setNewTextFormat(pf); panelTf.selectable = false;
        panelMc._visible = false;
    }

    function redraw():Void {
        MazeRenderer.render(mazeMc, data, 0, 0);
        titleTf.text = title;
    }

    function showError(msg:String):Void {
        panelTf.text = msg; panelMc._visible = true; errorVisible = true;
    }
    function hideError():Void { panelMc._visible = false; errorVisible = false; }

    function fadeStep():Void {
        var step:Number = 100 / 15;   // 15 frames @ 25fps (srv/index.php:3637)
        if (_root._alpha < fadeTarget) _root._alpha = Math.min(fadeTarget, _root._alpha + step);
        else if (_root._alpha > fadeTarget) _root._alpha = Math.max(fadeTarget, _root._alpha - step);
    }
}
```

- [ ] **Step 2: Write `src/mazecreator/build.sh`**:

```sh
#!/bin/sh
cd "$(dirname "$0")"
../../thirdparty/mtasc/mtasc.exe -version 8 -swf editor.swf -main -header 688:400:25 Editor.as
```

Add `src/mazecreator/.gitignore` containing `editor.swf`.

- [ ] **Step 3: Compile** — `cd /c/Users/eth/websites/TankTrouble/src/mazecreator && sh build.sh`. Expected: `editor.swf` produced. (Note: rendering only appears at runtime; parse copies from the lattice keep the frozen MazeData API untouched.)

- [ ] **Step 4: Point the harness at the editor.** Edit `oracle/editor-visual/index.html`: change `player.load('harness.swf')` to `player.load('includes/editor.swf?initCode=' + window.__initCode)` and add `window.__initCode = new URLSearchParams(location.search).get('initCode') || '';` before the load call. (FlashVars via SWF query string — proven in both runtimes, phase 1.)

- [ ] **Step 5: Write `oracle/editor-visual/run_editor.mjs`** — the interaction gate. Serve `includes/editor.swf` from `src/mazecreator/editor.swf`, define page spies, drive clicks and SetVariable, assert via GetVariable:

```javascript
// Phase 3 interaction gate: boots the real editor SWF under Ruffle and
// asserts the full page contract + editing semantics. Exit 0 = green.
import http from "node:http";
import { readFile } from "node:fs/promises";
import { readFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";

const DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));
const ORACLE = path.resolve(DIR, "..");
const SRC = path.resolve(DIR, "../../src/mazecreator");
const PORT = 8082;
const MIME = { ".html": "text/html", ".js": "text/javascript",
               ".wasm": "application/wasm", ".swf": "application/x-shockwave-flash" };

const gauntlet = JSON.parse(readFileSync(path.join(DIR, "gauntlet.json"), "utf8"));
const INIT = Buffer.from(
  `u=7&n=testuser01&t=${gauntlet.title}&d=${gauntlet.d}&s=1`).toString("base64");

const server = http.createServer(async (req, res) => {
  try {
    const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
    let file;
    if (rel === "includes/editor.swf") file = path.join(SRC, "editor.swf");
    else if (rel.startsWith("ruffle-spike/")) file = path.join(ORACLE, rel);
    else file = path.join(DIR, rel);
    const body = await readFile(file);
    res.writeHead(200, { "Content-Type": MIME[path.extname(rel)] || "application/octet-stream" });
    res.end(body);
  } catch { res.writeHead(404); res.end("nope"); }
});
await new Promise(r => server.listen(PORT, "127.0.0.1", r));

const EXE = process.env.TT_BROWSER ||
  "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe";
const browser = await puppeteer.launch({ executablePath: EXE, headless: true,
  args: ["--no-first-run", "--force-device-scale-factor=1"] });
const page = await browser.newPage();
await page.setViewport({ width: 688, height: 400 });
await page.evaluateOnNewDocument(() => {
  window.__calls = [];
  window.showMazeCreatorToolsAndTitle = (u, t) => window.__calls.push(["show", u, t]);
  window.hideMazeCreatorToolsAndTitle = (u) => window.__calls.push(["hide", u]);
});
await page.goto(`http://127.0.0.1:${PORT}/index.html?initCode=${encodeURIComponent(INIT)}`);
await page.waitForFunction("window.__gate && (window.__gate.loaded || window.__gate.loadfail)",
  { timeout: 30000 });
await new Promise(r => setTimeout(r, 1500));

const results = [];
const check = (name, cond) => { results.push([name, !!cond]); if (!cond) console.log("FAIL:", name); };
const sv = (n, v) => page.evaluate((a, b) => window.__player.SetVariable(a, b), n, v);
const gv = (n) => page.evaluate(a => window.__player.GetVariable(a), n);
const wait = (ms) => new Promise(r => setTimeout(r, ms));
const CELL = 32, LX = 56, LY = 50;
const cellClick = (cx, cy) =>
  page.mouse.click(LX + cx * CELL + CELL / 2, LY + cy * CELL + CELL / 2);

// boot: hidden until the page fades us in (page contract, +1200ms)
check("boots hidden", (await gv("stageAlpha")) === "0");
await sv("fadeOut", "false");
await wait(1200);
check("fades in over 15 frames", (await gv("stageAlpha")) === "100");
check("boots into preview", (await gv("state")) === "preview");
check("initCode round-trips", (await gv("mazeD")) === gauntlet.d);
check("initCode title", (await gv("titleText")) === gauntlet.title);

// preview click -> edit + outbound showMazeCreatorToolsAndTitle
await cellClick(9, 4); await wait(300);
check("click enters edit", (await gv("state")) === "edit");
const calls1 = await page.evaluate(() => window.__calls);
check("show call fired", calls1.some(c => c[0] === "show" && c[1] === "7" && c[2] === gauntlet.title));
check("default tool construct", (await gv("tool")) === "construct");

// construct: paint a floor cell on, then off (lattice corner 0,0)
const d0 = await gv("mazeD");
await cellClick(0, 0); await wait(200);
const d1 = await gv("mazeD");
check("floor paint changes maze", d1 !== d0);
await cellClick(0, 0); await wait(200);
check("floor unpaint restores", (await gv("mazeD")) === d0);

// construct: toggle an interior wall between two floor cells. Paint two
// adjacent cells far from the boot maze, then click their shared edge.
await cellClick(16, 8); await cellClick(17, 8); await wait(200);
const dPair = await gv("mazeD");
await page.mouse.click(LX + 17 * CELL + 1, LY + 8 * CELL + CELL / 2); // west edge of (17,8)
await wait(200);
const dWall = await gv("mazeD");
check("interior wall toggles", dWall !== dPair);
await page.mouse.click(LX + 17 * CELL + 1, LY + 8 * CELL + CELL / 2);
await wait(200);
check("interior wall toggles back", (await gv("mazeD")) === dPair);

// tankSpawn: place and remove; cap at 5 (gauntlet already has tanks)
await sv("newToolRequested", "tankSpawn");
check("tool switches", (await gv("tool")) === "tankSpawn");
const countType = (d, t) => {
  const f = d.split("#"); let n = +f[3], i = 4, k = 0;
  for (let o = 0; o < n; o++) { if (+f[i + 2] === t) k++; i += 4; }
  return k;
};
const before = countType(await gv("mazeD"), 5);
await cellClick(16, 8); await wait(200);
const after = countType(await gv("mazeD"), 5);
if (before < 5) check("tank place adds", after === before + 1);
else check("tank cap enforced", after === 5);
await cellClick(16, 8); await wait(200);
check("tank toggle removes", countType(await gv("mazeD"), 5) === before);

// title + error panel vocabulary (literal _root.-prefixed names)
await sv("_root.mazeName", "New Name");
check("mazeName literal name", (await gv("titleText")) === "New Name");
check("error hidden initially", (await gv("errorVisible")) === "false");
await sv("_root.mazeName", "");
await sv("_root.saveRequested", "true"); await wait(300);
check("save with empty title shows error", (await gv("errorVisible")) === "true");
await sv("_root.errorPanel.hide", "yes");
check("errorPanel.hide literal name", (await gv("errorVisible")) === "false");

// previewLoaded returns to preview
await sv("previewLoaded", "");
check("previewLoaded -> preview", (await gv("state")) === "preview");

// fadeOut hides
await sv("fadeOut", "true"); await wait(1200);
check("fadeOut fades to 0", (await gv("stageAlpha")) === "0");

// cleanup painted cells not needed -- lattice was only mutated in-session
const failed = results.filter(r => !r[1]);
console.log(`editor interaction: ${results.length - failed.length}/${results.length} checks green`);
await browser.close(); server.close();
process.exit(failed.length === 0 ? 0 : 1);
```

- [ ] **Step 6: Run to verify current failure** — `cd /c/Users/eth/websites/TankTrouble/oracle/editor-visual && node run_editor.mjs`. Expected before the save logic exists: "save with empty title shows error" FAILS (doSave is a stub) — every other check should pass. Debug anything else that fails now (coordinate math and channel routing are the likely suspects; use GetVariable probes, not screenshots, to localize).

- [ ] **Step 7: Make the empty-title check pass with local validation only** (the network half is Task 5). Replace the `doSave` stub in `Editor.as`:

```actionscript
    function doSave():Void {
        if (state != "edit") return;
        if (!validTitle(title)) { showError("Please give your maze a name."); return; }
        // network save lands in Task 5
    }

    function validTitle(t:String):Boolean {
        if (t == null || t.length < 1 || t.length > 32) return false;
        var legal:String = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                         + "abcdefghijklmnopqrstuvwxyz !,-.?";
        for (var i:Number = 0; i < t.length; i++)
            if (legal.indexOf(t.charAt(i)) < 0) return false;
        return true;
    }
```

- [ ] **Step 8: Rebuild + full gate green** — `cd /c/Users/eth/websites/TankTrouble/src/mazecreator && sh build.sh && cd ../../oracle/editor-visual && node run_editor.mjs`. Expected: all checks green, exit 0.

- [ ] **Step 9: Commit**

```bash
cd /c/Users/eth/websites/TankTrouble && git add src/mazecreator oracle/editor-visual && git commit -m "feat: Editor shell - states, full SetVariable vocabulary, tool interaction, fade; Ruffle interaction gate green"
```

---

### Task 5: Save flow through saveMaze.php

**Files:**
- Modify: `src/mazecreator/Editor.as` (complete `doSave`)
- Modify: `oracle/editor-visual/run_editor.mjs` (proxy + save assertions)

**Interfaces:**
- Consumes: `Editor.cropToFloorBbox()`, `Base64.Encode`, invented saveMaze contract (POST `q=b64(t&n&d&s)`, reply `r=b64(saved=true&s=N | error=code)` — pinned by tests/test_savemaze.py).
- Produces: complete save flow; on success `getURL("javascript:hideMazeCreatorToolsAndTitle('<u>')")` + state=preview; on error the panel shows mapped copy.

- [ ] **Step 1: Add the failing save assertions to `run_editor.mjs`.** First add the proxy: inside the http server handler, BEFORE the static-file logic, insert:

```javascript
    if (rel.startsWith("includes/") && rel !== "includes/editor.swf") {
      // proxy PHP endpoints to the docker stack so LoadVars posts land
      const chunks = [];
      for await (const c of req) chunks.push(c);
      const upstream = await fetch("http://127.0.0.1:8056/" + rel, {
        method: req.method,
        headers: { "content-type": req.headers["content-type"] || "application/x-www-form-urlencoded" },
        body: req.method === "POST" ? Buffer.concat(chunks) : undefined,
      });
      const buf = Buffer.from(await upstream.arrayBuffer());
      res.writeHead(upstream.status, { "Content-Type": "text/plain" });
      res.end(buf);
      return;
    }
```

Then, replacing the section from `// previewLoaded returns to preview` to the end of the checks, drive a real save first (keep the previewLoaded and fadeOut checks after it):

```javascript
// real save: rename, request save, expect hide call + preview + DB write
await sv("_root.mazeName", "Phase Three Gate");
await sv("_root.saveRequested", "true");
await wait(2000);
const calls2 = await page.evaluate(() => window.__calls);
check("hide call fired on save", calls2.some(c => c[0] === "hide" && c[1] === "7"));
check("save flips to preview", (await gv("state")) === "preview");
check("no error on good save", (await gv("errorVisible")) === "false");
const savedD = await gv("mazeD");
const q = Buffer.from("userName=testuser01&a=0.1&b=0.2").toString("base64");
const body = await (await fetch(`http://127.0.0.1:8056/includes/loadMaze.php?q=${q}`)).text();
const pairs = Object.fromEntries(Buffer.from(body.slice(2), "base64").toString("latin1")
  .split("&").map(p => p.split("=")));
check("DB round-trip d matches editor", pairs.d === savedD);
check("DB round-trip title", pairs.t === "Phase Three Gate");

// server-side rejection surfaces in the error panel: force badGrid by
// requesting a save in preview state? No -- preview ignores saveRequested;
// instead verify the local empty-title path stays covered (Task 4 check)
// and the previewLoaded/fadeOut vocabulary still works after a save cycle.
```

After the final results tally, add DB cleanup so gate B's corpus coverage stays pristine (same rule as tests/test_savemaze.py):

```javascript
import { execFileSync } from "node:child_process";
try {
  execFileSync("docker", ["exec", "docker-mysql-1", "sh", "-c",
    'exec mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" tanktrouble ' +
    "-e \"DELETE FROM mazes WHERE author='testuser01'\""], { timeout: 60000 });
} catch {}
```

(the import goes at the top of the file; the try block after `server.close()`).

Note the ordering change: the empty-title error test from Task 4 must run AFTER the successful save (a failed save leaves state=edit; the good save flips to preview, so re-enter edit with a stage click before the empty-title case) — OR simpler: run the good save LAST. Arrange: …tank checks → mazeName/error-panel checks (empty title) → restore title → good save → hide/preview/DB checks → previewLoaded + fadeOut checks.

- [ ] **Step 2: Run to verify failure** — `node run_editor.mjs` with the docker stack up. Expected: "hide call fired on save" and the DB checks FAIL (doSave never posts).

- [ ] **Step 3: Complete `doSave` in `Editor.as`** (replace the Task 4 body; keep `validTitle`):

```actionscript
    function doSave():Void {
        if (state != "edit") return;
        if (!validTitle(title)) { showError("Please give your maze a name."); return; }
        var cropped:MazeData = cropToFloorBbox();
        var d:String = cropped.emit();
        var inner:String = "t=" + title + "&n=" + userName + "&d=" + d + "&s=" + slot;
        var post:LoadVars = new LoadVars();
        post.q = Base64.Encode(inner);
        var reply:LoadVars = new LoadVars();
        var owner:Editor = this;
        reply.onLoad = function(ok:Boolean) {
            if (!ok) { owner.showError("Could not reach the server."); return; }
            // body is r=<base64>; LoadVars url-decodes, turning + into space
            var raw:String = Base64.StringReplaceAll(String(this.r), " ", "+");
            var pairs:Array = Base64.Decode(raw).split("&");
            var res:Object = {};
            for (var i:Number = 0; i < pairs.length; i++) {
                var kv:Array = pairs[i].split("=");
                res[kv[0]] = kv[1];
            }
            if (res.saved == "true") {
                owner.hideError();
                owner.state = "preview";
                owner.redraw();
                getURL("javascript:hideMazeCreatorToolsAndTitle('" + owner.userId + "')");
            } else {
                owner.showError(owner.errorCopy(String(res.error)));
            }
        };
        post.sendAndLoad(SAVE_ENDPOINT, reply, "POST");
    }

    // M3 copy -- the original panel text is unrecorded (known only from
    // _root.errorPanel.hide). Codes are the invented saveMaze.php set.
    function errorCopy(code:String):String {
        if (code == "badTitle") return "Please give your maze a name.";
        if (code == "tooManyObjects") return "Too many spawn points.";
        return "Your maze could not be saved.";
    }
```

- [ ] **Step 4: Rebuild + run the full interaction gate** — `cd /c/Users/eth/websites/TankTrouble/src/mazecreator && sh build.sh && cd ../../oracle/editor-visual && node run_editor.mjs`. Expected: all checks green including the DB round-trip, exit 0. If `DB round-trip d matches editor` fails on `+`-vs-space, the LoadVars url-decode note in Step 3 is the first suspect (also check the PHP side already tolerates it: saveMaze.php line 50).

- [ ] **Step 5: Confirm corpus stayed pristine** — `cd /c/Users/eth/websites/TankTrouble && python -m pytest tests/test_getscrapyard_replay.py tests/test_loadmaze_replay.py -q`. Expected: green (cleanup worked).

- [ ] **Step 6: Commit**

```bash
cd /c/Users/eth/websites/TankTrouble && git add src/mazecreator/Editor.as oracle/editor-visual/run_editor.mjs && git commit -m "feat: editor save flow - LoadVars POST to saveMaze.php, error panel copy, hide callback; DB round-trip green"
```

---

### Task 6: Ship `srv/includes/mazeCreator_v0.3.swf` (M2)

**Files:**
- Modify: `src/mazecreator/build.sh` (also emit the shipping SWF)
- Create: `srv/includes/mazeCreator_v0.3.swf` (build output — committed)
- Create: `srv/includes/mazeCreator_v0.3.swf.provenance`
- Modify: `LEDGER.tsv` (the `srv/includes/mazeCreator_v0.3.swf` row: pending → M2)
- Create: `tests/test_mazecreator_asset.py`

**Interfaces:**
- Consumes: `tools/swf_header.py` → `read_header(path)` returns `{"version": int, "compressed": bool, "w": int, "h": int, "fps": float, "frames": int}`.
- Produces: the shipped SWF at the O-evidenced embed path (`includes/mazeCreator_v0.3.swf`, srv/index.php:3617).

- [ ] **Step 1: Write the failing asset test** `tests/test_mazecreator_asset.py`:

```python
"""mazeCreator_v0.3.swf (M2) -- shipped rebuild asset sanity.

The SWF is a rebuild (M2): logic pinned by the oracle gates
(oracle/editor-roundtrip, oracle/editor-visual), pixels redrawn from the
'Making a maze.png' screenshot. This test pins the shipping artifact:
embed-contract header facts + provenance bookkeeping.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from swf_header import read_header

SWF = ROOT / "srv" / "includes" / "mazeCreator_v0.3.swf"


def test_swf_matches_embed_contract():
    # srv/index.php:3617 embeds 688x400 player 8; siblings run 25fps
    h = read_header(SWF)
    assert h["version"] == 8
    assert (h["w"], h["h"]) == (688, 400)
    assert h["fps"] == 25


def test_provenance_sidecar_and_ledger():
    sidecar = SWF.with_suffix(".swf.provenance")
    text = sidecar.read_text()
    assert "M2" in text and "DO NOT PROMOTE" in text
    row = [l for l in (ROOT / "LEDGER.tsv").read_text(encoding="utf-8").splitlines()
           if "srv/includes/mazeCreator_v0.3.swf" in l]
    assert len(row) == 1
    assert "\tM2\t" in row[0]


def test_editor_source_headers():
    src = (ROOT / "src" / "mazecreator" / "Editor.as").read_text()
    assert "M2" in src and "srv/index.php" in src
```

- [ ] **Step 2: Run to verify failure** — `cd /c/Users/eth/websites/TankTrouble && python -m pytest tests/test_mazecreator_asset.py -q`. Expected: FAIL (no SWF, no sidecar).

- [ ] **Step 3: Extend `src/mazecreator/build.sh`** to also produce the shipping copy:

```sh
#!/bin/sh
cd "$(dirname "$0")"
../../thirdparty/mtasc/mtasc.exe -version 8 -swf editor.swf -main -header 688:400:25 Editor.as
cp editor.swf ../../srv/includes/mazeCreator_v0.3.swf
```

Run it. Note: MTASC output is uncompressed FWS — fine for the era player; do not add compression the original may not have had.

- [ ] **Step 4: Write the sidecar** `srv/includes/mazeCreator_v0.3.swf.provenance`:

```
tier: M2
written: 2026-08-03
source: src/mazecreator/ (Editor.as, MazeRenderer.as, MazeData.as, Base64.as)
built-with: MTASC 1.14 (thirdparty/mtasc/FETCHED.md), -version 8 -header 688:400:25
evidence:
  - embed contract + SetVariable vocabulary: srv/index.php:3609-3753 (O)
  - wire format + reader semantics: MazeDataFetcher.as decompile (O);
    round-trip gate 670/670 (oracle/editor-roundtrip)
  - visuals: 'Making a maze.png' screenshot, uniform 1.2023 scale (M2) --
    docs/mazecreator-visual-spec.md
  - constraints: corpus-measured (guide 6.5), boundary-bit invariant
    670/670 (DECISIONS 2026-08-03)
invented (M3 inside an M2 shell, see DECISIONS):
  - interaction model (click semantics), initCode field names (u,n,t,d,s),
    error panel visuals + copy, integer-cell lattice snap, save wire format
    (mirrors loadMaze -- pinned by tests/test_savemaze.py)
caveat: DO NOT PROMOTE. Original pixels, fonts, tweens, and preview mode
  are unrecovered; icon-state art and transitions await video evidence
  (guide 6.5 artwork source 2).
gates: oracle/editor-roundtrip/run_roundtrip.mjs, oracle/editor-visual/
  run_editor.mjs, tests/test_mazecreator_asset.py, gate C entry in
  oracle/DIVERGENCES.md
```

- [ ] **Step 5: Update the LEDGER row.** Find the `srv/includes/mazeCreator_v0.3.swf` row (it exists as pending/known-lost from milestone 1) and set tier M2 with verification pointing at the sidecar + gates. Preserve the TSV column layout exactly (tabs, UTF-8 — use the Edit tool, never a heredoc).

- [ ] **Step 6: Test green + full suite** — `python -m pytest tests/test_mazecreator_asset.py -q` then `python -m pytest tests/ -q`. Expected: 74 passed (71 + 3).

- [ ] **Step 7: Commit** (rebuild output + bookkeeping only — no archive bytes):

```bash
cd /c/Users/eth/websites/TankTrouble && git add src/mazecreator/build.sh srv/includes/mazeCreator_v0.3.swf srv/includes/mazeCreator_v0.3.swf.provenance LEDGER.tsv tests/test_mazecreator_asset.py && git commit -m "feat(M2): ship mazeCreator_v0.3.swf rebuild + provenance sidecar + asset tests"
```

---

### Task 7: Gate C screenshot diff + close-out

**Files:**
- Create: `oracle/projector/shot_editor.ps1`
- Modify: `oracle/DIVERGENCES.md` (append gate C editor section)
- Modify: `DECISIONS.md` (append phase 3 inventions entry)
- Modify: `~/.claude/projects/C--Users-eth-websites/memory/tanktrouble-rebuild.md` + `MEMORY.md`

**Interfaces:**
- Consumes: `tools/diff_render.py` (Task 3), projector at `oracle/projector/flashplayer_32_sa.exe`, `run_visual.mjs` output.

- [ ] **Step 1: Ruffle side** — regenerate with the SHIPPED SWF: temporarily point `run_visual.mjs`'s server at `srv/includes/mazeCreator_v0.3.swf` is wrong (the editor boots to preview and needs initCode) — instead reuse `run_editor.mjs`'s server pattern: add a `--screenshot` mode to `run_editor.mjs` that, after the "fades in" check, saves `ruffle_editor.png` and exits before the interaction checks. Concretely: read `process.argv.includes("--screenshot")`; if set, after the fade-in wait run `await page.screenshot({ path: path.join(DIR, "ruffle_editor.png") })`, close, exit 0. Run: `node run_editor.mjs --screenshot`.

- [ ] **Step 2: Projector side** — `oracle/projector/shot_editor.ps1` (same CopyFromScreen approach as phase 1's smoke test):

```powershell
# Gate C: projector ground-truth screenshot of the shipped editor.
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$init = Get-Content "$root\oracle\editor-visual\gauntlet.json" | ConvertFrom-Json
$inner = "u=7&n=testuser01&t=$($init.title)&d=$($init.d)&s=1"
$b64 = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes($inner))
$swf = "$root\srv\includes\mazeCreator_v0.3.swf"
$proc = Start-Process -FilePath "$PSScriptRoot\flashplayer_32_sa.exe" `
        -ArgumentList "`"$swf`?initCode=$b64`"" -PassThru
Start-Sleep -Seconds 6
Add-Type -AssemblyName System.Windows.Forms, System.Drawing
$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bmp = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
$bmp.Save("$PSScriptRoot\projector_editor_raw.png")
Stop-Process $proc -Force
Write-Output "saved projector_editor_raw.png -- crop the stage before diffing"
```

Run it (needs the desktop unlocked). Then crop the 688×400 stage region out of `projector_editor_raw.png` (locate the white stage rectangle; a short Pillow crop in the scratchpad is fine) → `oracle/projector/projector_editor.png`.

- [ ] **Step 3: Diff** — `python tools/diff_render.py oracle/editor-visual/ruffle_editor.png oracle/projector/projector_editor.png oracle/editor-visual/gatec_diff.png --mask=0,0,688,40 --mask=480,375,208,25` (masks = title + watermark device-text bands; adjust to the spec's measured bands). Record the numbers. Vector geometry should be near-identical; text antialiasing is the expected divergence — that is WHY the bands are masked.

- [ ] **Step 4: Append to `oracle/DIVERGENCES.md`** — gate C editor section: date, SWF sha256 (`sha256sum srv/includes/mazeCreator_v0.3.swf`), both runtime versions (Ruffle 0.4.1, projector 32.0.0.465), diff numbers with and without masks, and any visible divergence with a verdict (cosmetic / behavioral).

- [ ] **Step 5: Append DECISIONS.md phase 3 entry** — the M3 inventions now load-bearing: interaction model (edge-click walls / cell-click floor / spawn toggles), initCode fields `u,n,t,d,s`, integer-cell lattice snap, error copy, `ExternalInterface.available` boot-visibility rule, deterministic object angles (gate C determinism), boot-to-preview + click-to-edit state model. One line each on what evidence would revise them (video, mainly). Cross-check `docs/VISUAL-EVIDENCE-WANTED.md` — every invention listed there must stay current (statuses, trigger scenarios); add entries for anything new this phase invented.

- [ ] **Step 6: Full verification sweep** — 
`cd /c/Users/eth/websites/TankTrouble && python -m pytest tests/ -q` (expect 74 passed), `cd oracle/editor-roundtrip && node run_roundtrip.mjs` (670/670 + normalize no-op), `cd ../editor-visual && node run_editor.mjs` (all checks). Grep for credential-shaped strings: `cd /c/Users/eth/websites/TankTrouble && grep -rInE "(password|passwd|pwd)\s*=\s*['\"][^'\"]{4,}" src oracle tools tests docs --include="*.as" --include="*.mjs" --include="*.py" --include="*.md" | grep -vi "MYSQL_PASSWORD"` (expect empty).

- [ ] **Step 7: Commit + tag + memory**

```bash
cd /c/Users/eth/websites/TankTrouble && git add oracle/DIVERGENCES.md DECISIONS.md oracle/projector/shot_editor.ps1 && git commit -m "docs: gate C editor screenshot diff + phase 3 decisions" && git tag mazecreator-editor-complete
```

Then update `~/.claude/projects/C--Users-eth-websites/memory/tanktrouble-rebuild.md` (phase 3 complete: what shipped, gate results, tag) and the `MEMORY.md` index line (next: phase 4 — initCode markup reconstruction + logged-in garage UI + icon redraw from video).

---

## Self-Review Notes

- Spec coverage: rendering (T1 spec + T3), tools + interaction (T4), full SetVariable vocabulary incl. fadeOut timing + errorPanel dotted-path dual channel (T4), save flow to the live M3 endpoint (T5), ship + provenance (T6), gate C (T7). Preview mode is deliberately minimal (render + click-to-edit) — full garage preview needs initCode markup, phase 4; recorded in the sidecar caveat.
- Ordering hazard flagged in T5 Step 1 (error-path test vs good-save state flip) is resolved by the stated ordering: good save LAST among interaction checks.
- Type consistency: `MazeRenderer.render(mc, data, offX, offY)` + `cellOffsetFor(data)` used identically in T3 harness and T4 Editor; `normalizeBoundary()` defined T2, called T4 (loadIntoLattice, floor toggle) and T5 (via cropToFloorBbox defined T4); `read_header` dict keys match tools/swf_header.py:30-34.
- Constants in T3/T4 code are Task 1 estimates by design — Task 1's measured values are authoritative; T3 Step 1 says so explicitly.
