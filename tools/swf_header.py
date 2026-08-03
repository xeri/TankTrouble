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
