#!/usr/bin/env python3
"""Extract unique maze d= grids from the corpus for the round-trip gate.

Latest capture wins per (author, slot) -- the same rule seed/gen_mazes used,
so grids.json matches what is seeded in MySQL. Also audits the emit shape
the editor must reproduce: reserved field, params contents, digit alphabet.
"""
import base64, collections, json, pathlib, sys

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
    latest = {}   # (n, s) -> d
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
