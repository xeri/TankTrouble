"""mazes: archive/maze-corpus/raw/ -> docker/mysql/init/10-mazes.sql

Data tier O: each row is the decoded content of one archived loadMaze.php
response (`r=<base64>` of `t=<title>&n=<author>&d=<grid>`). notFound=true
payloads are NOT rows -- they prove the slot was empty, and gate B replay
must reproduce that by the row's absence.

Row key: the userName request code, recoverable only from the corpus
filename `<fetchts>_<CODE>.txt` (the archived body holds just `r=`).
MazeDataFetcher.as shows loadMaze is queried by userName, one maze per user.
"""

import base64
import glob
import os
import re
import urllib.parse

from common import archive_root, provenance_header, sql_str, write_out

FNAME = re.compile(r"^(\d{14})_([A-Z0-9]+)\.txt$")


def decode_payload(raw):
    pairs = dict(p.split("=", 1) for p in raw.strip().split("&"))
    inner = base64.b64decode(pairs["r"]).decode("utf-8")
    if inner == "notFound=true":
        return None
    fields = dict(p.split("=", 1) for p in inner.split("&"))
    return {
        "title": urllib.parse.unquote_plus(fields["t"]),
        "author": urllib.parse.unquote_plus(fields["n"]),
        "data": fields["d"],
    }


def validate_grid(d):
    seg = d.split("#")
    w = int(seg[0])
    cells = seg[1]
    if len(cells) % w != 0:
        raise ValueError("cells not divisible by width")
    h = len(cells) // w
    if not (1 <= w <= 18 and 1 <= h <= 10):
        raise ValueError("grid %dx%d outside observed 18x10" % (w, h))


def main():
    raw_dir = os.path.join(archive_root(), "maze-corpus", "raw")
    rows = {}          # user_code -> (fetchts, maze dict)
    notfound = []
    for path in sorted(glob.glob(os.path.join(raw_dir, "*.txt"))):
        m = FNAME.match(os.path.basename(path))
        if not m:
            raise SystemExit("unexpected corpus filename: %s" % path)
        fetchts, code = m.groups()
        maze = decode_payload(open(path, encoding="ascii").read())
        if maze is None:
            notfound.append(code)
            continue
        validate_grid(maze["data"])
        prev = rows.get(code)
        if prev and prev[1] != maze:
            raise SystemExit("conflicting captures for %s" % code)
        if not prev or fetchts > prev[0]:
            rows[code] = (fetchts, maze)

    out = provenance_header(
        "seed_mazes.py", "O", "M1",
        "%d decoded loadMaze.php responses in archive/maze-corpus/raw/; "
        "wire format from MazeDataFetcher.as (DEDUCE.md 3.1)" % (len(rows) + len(notfound)),
        "Column names t/n/d and the userName key are observed; table and "
        "column NAMES in SQL are M3 (never observable through HTTP).")
    out += "INSERT INTO mazes (user_code, title, author, data) VALUES\n"
    vals = []
    for code in sorted(rows):
        maze = rows[code][1]
        vals.append("(%s, %s, %s, %s)" % (
            sql_str(code), sql_str(maze["title"]),
            sql_str(maze["author"]), sql_str(maze["data"])))
    out += ",\n".join(vals) + ";\n"
    out += "\n-- notFound (slot empty at capture time; deliberately no row): %s\n" % (
        ", ".join(sorted(notfound)) or "none")
    write_out("10-mazes.sql", out)
    print("mazes: %d rows, %d notFound" % (len(rows), len(notfound)))


if __name__ == "__main__":
    main()
