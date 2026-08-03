"""mazes: archive/maze-corpus/raw/ -> docker/mysql/init/10-mazes.sql

Data tier O: each row is the decoded content of one archived loadMaze.php
response body `r=<base64(shuffled "t=<title>&n=<author>&d=<grid>&s=<slot>")>`.
The pair ORDER inside the base64 is a per-request server-side shuffle (all
24 permutations occur across the corpus) and is deliberately not preserved;
the canonical fields are.

Corpus filename is `<fetchts>_<CODE>.txt` where CODE is the first 12 chars
of the Wayback sha1-base32 digest of the response body (verified 843/843) --
a CAPTURE identity, not a user code. 842/843 responses answered anonymous
`c=<random>` requests (archive/cdx-passes/F_loadmaze200.json).

The corpus is a TIME SERIES of one live table (fetches 2017-01..2019-04):
842 bodies -> 744 distinct contents -> 672 distinct (author, slot) states;
70 authors were re-captured with a DIFFERENT maze (edited between fetches).
Row model: one row per (author, slot), latest capture wins -- the DB is one
site snapshot, not the corpus (DECISIONS 2026-08-03, supersedes the
2026-08-03 "keyed by corpus filename code" entry). Superseded captures and
per-row witnesses are recorded in the SQL trailer; nothing is lost, the
corpus stays the O record.

notFound=true payloads are NOT rows -- they prove the slot was empty, and
gate B replay must reproduce that by the row's absence.
"""

import base64
import glob
import os
import re

from common import archive_root, provenance_header, sql_str, write_out

FNAME = re.compile(r"^(\d{14})_([A-Z0-9]+)\.txt$")


def decode_payload(raw):
    pairs = dict(p.split("=", 1) for p in raw.strip().split("&"))
    if set(pairs) != {"r"}:
        raise SystemExit("unexpected outer keys %s" % sorted(pairs))
    inner = base64.b64decode(pairs["r"]).decode("utf-8")
    if inner == "notFound=true":
        return None
    fields = dict(p.split("=", 1) for p in inner.split("&"))
    if set(fields) != {"t", "n", "d", "s"}:
        raise SystemExit("unexpected inner keys %s" % sorted(fields))
    for k in ("t", "n"):
        # zero %-escapes and zero '+' across the whole corpus -- fields are
        # raw bytes, NOT urlencoded; a hit here means the encoding question
        # must be reopened, not silently decoded (DECISIONS 2026-08-03)
        if "%" in fields[k] or "+" in fields[k]:
            raise SystemExit("possible urlencoding in %s=%r -- corpus "
                             "assumption broken" % (k, fields[k]))
    return {"title": fields["t"], "author": fields["n"],
            "data": fields["d"], "slot": fields["s"]}


def validate_grid(d):
    seg = d.split("#")
    w = int(seg[0])
    cells = seg[1]
    if len(cells) % w != 0:
        raise ValueError("cells not divisible by width")
    h = len(cells) // w
    if not (1 <= w <= 18 and 1 <= h <= 10):
        raise ValueError("grid %dx%d outside observed 18x10" % (w, h))


def content_key(maze):
    return (maze["title"], maze["author"], maze["data"], maze["slot"])


def main():
    raw_dir = os.path.join(archive_root(), "maze-corpus", "raw")
    captures = []      # (fetchts, code, maze)
    notfound = []
    for path in sorted(glob.glob(os.path.join(raw_dir, "*.txt"))):
        m = FNAME.match(os.path.basename(path))
        if not m:
            raise SystemExit("unexpected corpus filename: %s" % path)
        fetchts, code = m.groups()
        maze = decode_payload(open(path, encoding="ascii").read())
        if maze is None:
            notfound.append("%s_%s" % (fetchts, code))
            continue
        validate_grid(maze["data"])
        int(maze["slot"])          # slot must be numeric
        if not maze["author"]:
            raise SystemExit("empty author in %s -- cannot key row" % code)
        captures.append((fetchts, code, maze))

    winners = {}       # (author, slot) -> (fetchts, code, maze)
    for fetchts, code, maze in captures:
        key = (maze["author"], maze["slot"])
        prev = winners.get(key)
        if prev and prev[0] == fetchts and content_key(prev[2]) != content_key(maze):
            raise SystemExit("same-timestamp conflicting captures for %r" % (key,))
        if not prev or fetchts > prev[0]:
            winners[key] = (fetchts, code, maze)

    superseded = []
    for fetchts, code, maze in captures:
        win = winners[(maze["author"], maze["slot"])]
        if win[1] == code and win[0] == fetchts:
            continue
        rel = ("content-identical" if content_key(maze) == content_key(win[2])
               else "content-differs")
        superseded.append("%s_%s author=%s slot=%s %s" % (
            fetchts, code, maze["author"], maze["slot"], rel))

    out = provenance_header(
        "seed_mazes.py", "O", "M1",
        "%d decoded loadMaze.php responses in archive/maze-corpus/raw/ -> "
        "%d distinct (author, slot) states, latest capture wins; wire format "
        "from MazeDataFetcher.as + corpus (all 24 inner permutations occur)"
        % (len(captures) + len(notfound), len(winners)),
        "Fields t/n/d/s and the userName->author query are observed/deduced; "
        "table and column NAMES in SQL are M3 (never observable through "
        "HTTP). Corpus is a time series; superseded captures in trailer.")
    out += "INSERT INTO mazes (author, slot, title, data) VALUES\n"
    vals = []
    for key in sorted(winners):
        maze = winners[key][2]
        vals.append("(%s, %s, %s, %s)" % (
            sql_str(maze["author"]), maze["slot"],
            sql_str(maze["title"]), sql_str(maze["data"])))
    out += ",\n".join(vals) + ";\n"
    out += "\n-- notFound (slot empty at capture time; deliberately no row): %s\n" % (
        ", ".join(sorted(notfound)) or "none")
    out += "\n-- witness (winning capture per row, <fetchts>_<digest12>):\n"
    for key in sorted(winners):
        fetchts, code, maze = winners[key]
        out += "--   %s_%s author=%s slot=%s\n" % (fetchts, code,
                                                   maze["author"], maze["slot"])
    out += "\n-- superseded (older capture of a re-fetched slot; NOT a row):\n"
    for line in sorted(superseded):
        out += "--   %s\n" % line
    write_out("10-mazes.sql", out)
    print("mazes: %d rows from %d captures, %d superseded, %d notFound" % (
        len(winners), len(captures), len(superseded), len(notfound)))


if __name__ == "__main__":
    main()
