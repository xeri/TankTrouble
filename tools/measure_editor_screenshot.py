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
import json
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

# --- 3. transcribe cells: sample tones at 4 off-centre points (object
# icons cover cell centres; walls hug the edges) ---
def cell_center(cx, cy):
    return (bx0 + (cx + 0.5) * (bx1 - bx0) / gw,
            by0 + (cy + 0.5) * (by1 - by0) / gh)
def cell_corners(cx, cy):
    for fx, fy in ((0.25, 0.25), (0.75, 0.25), (0.25, 0.75), (0.75, 0.75)):
        yield (int(bx0 + (cx + fx) * (bx1 - bx0) / gw),
               int(by0 + (cy + fy) * (by1 - by0) / gh))
def is_objcol(p):
    r, g, b = p
    return (b > r + 30 and b > 120) or (r > b + 50 and g > b + 10 and r > 150)
floor = [[0] * gh for _ in range(gw)]
tones = {}
for cx in range(gw):
    for cy in range(gh):
        pts = [im.getpixel(pt) for pt in cell_corners(cx, cy)]
        fl = [p for p in pts if is_floor(p)]
        if len(fl) >= 2 or (len(fl) >= 1 and any(is_objcol(p) for p in pts)):
            floor[cx][cy] = 1
            tones[(cx, cy)] = fl[0]

# floor tone pattern: NOT a parity checkerboard (measured) -- report the
# light:dark cell ratio instead (per-cell pseudo-random in the original)
ratio = Counter("L" if p[0] >= 230 else "D" for p in tones.values())
print("floor tone cells:", dict(ratio))

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

# --- 5. objects: blue (tank) / orange (crate) blob per cell -- scan the
# whole cell interior, icons are ~20px in a ~39px cell ---
objs = []
for cx in range(gw):
    for cy in range(gh):
        if not floor[cx][cy]:
            continue
        x0, y0 = cell_center(cx, cy)
        blue = orange = 0
        for dx in range(-16, 17, 2):
            for dy in range(-16, 17, 2):
                r, g, b = im.getpixel((int(x0 + dx), int(y0 + dy)))
                if b > r + 30 and b > 120: blue += 1
                if r > b + 50 and g > b + 10 and r > 150: orange += 1
        if blue > 8:   objs.append((cx + 1, cy + 1, 5))
        elif orange > 8: objs.append((cx + 1, cy + 1, 8))
print("objects (1-indexed x,y,type):", objs)

# sample object colours for the renderer
for name, cond in [("tank-blue", lambda r, g, b: b > r + 30 and b > 120),
                   ("crate-orange", lambda r, g, b: r > b + 50 and r > 150)]:
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
