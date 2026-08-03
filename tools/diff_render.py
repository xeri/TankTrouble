#!/usr/bin/env python3
"""Tolerance diff between two renders. Usage:
   python tools/diff_render.py a.png b.png out.png [--mask=x,y,w,h]...
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
