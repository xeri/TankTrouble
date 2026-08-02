"""news: captured ?news pages -> docker/mysql/init/30-news.sql

VERBATIM-BLOB MODEL. The captured news page mixes several markup generations
in a single body (`news4 standard` collapsed items above `news standard` +
header/content pretty-printed items, with drifting indentation). One template
looping over clean field data cannot emit that; the page was hand-maintained
HTML or stored per-item HTML blobs -- which of the two is NOT observable.
So the importer does not invent field structure: each row's `body` is the
byte-verbatim slice of the capture, from `<a name=...>` through the item's
closing </div>. Convenience columns (posted/seq/css_class/title) are parsed
out for indexing only; the blob is the data.

Key: (posted, seq-in-document-order). Anchor dates collide (03-10-2016 has
two posts), so the site's own permalink anchor is not unique.

Canonical blob per item: the LATEST classic anchored capture, upgraded to an
earlier capture's blob only when that one is whitespace-normalised-equal and
longer (less PageSpeed collapse). Normalised-unequal bodies (live poll
widgets, template evolution such as the social-share block) keep the latest
capture's view; the count is recorded in the SQL trailer.

Scope: classic-era captures that use the anchor convention. Pre-anchor
classic captures (2010/2013) and modern-SPA captures (2021+, beta host) are
excluded -- the latter are grade D for the classic site.
"""

import glob
import os
import re

from common import archive_root, provenance_header, sql_str, write_out

ANCHOR = re.compile(r'<a name="(\d{2}-\d{2}-\d{4})" id="\1"></a>')
# item class is DATA, not structure: three generations observed so far
# ("news4 standard" collapsed, "news standard"+header/content pretty,
# "text medium" boxed) -- accept any class, record it
ITEM_OPEN = re.compile(r'\s*<div class="([^"]+)"[^>]*>')
DIV = re.compile(r"<div\b[^>]*>|</div>")
HEADER_OPEN = re.compile(r"\s*<div[^>]*>")


def iso(ddmmyyyy):
    d, m, y = ddmmyyyy.split("-")
    return "%s-%s-%s" % (y, m, d)


def matching_close(text, open_start):
    depth = 0
    for m in DIV.finditer(text, open_start):
        depth += 1 if m.group(0) != "</div>" else -1
        if depth == 0:
            return m.end()
    raise SystemExit("unbalanced divs after offset %d" % open_start)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def parse_capture(body):
    """Yield (date, css_class, title, verbatim_blob) in document order."""
    for a in ANCHOR.finditer(body):
        if ANCHOR.match(body, a.end()) or ANCHOR.match(body, a.end() + 1):
            # duplicated back-to-back anchor (hand-edit artefact, e.g.
            # 26-01-2009): the inner one owns the item
            continue
        m = ITEM_OPEN.match(body, a.end())
        if not m:
            raise SystemExit("anchor %s not followed by an item div: %r" % (
                a.group(1), body[a.end():a.end() + 120]))
        div_start = body.index("<div", m.start())
        end = matching_close(body, div_start)
        blob = body[a.start():end]
        inner = body[m.end():end - len("</div>")]

        h = HEADER_OPEN.match(inner)
        if not h:
            raise SystemExit("item %s: no header div: %r" % (
                a.group(1), inner[:120]))
        header_div_start = inner.index("<div", 0)
        header_end = matching_close(inner, header_div_start)
        header = inner[h.end():header_end - len("</div>")]
        date_div = re.search(r"<div[^>]*>\s*%s\s*</div>\s*$" % a.group(1), header)
        if not date_div:
            raise SystemExit("item %s: header lacks trailing date div: %r" % (
                a.group(1), header[-160:]))
        title = norm(re.sub(r"<[^>]+>", " ", header[:date_div.start()]))
        yield a.group(1), m.group(1), title, blob


def main():
    pat = os.path.join(archive_root(), "commoncrawl", "warc-bodies", "*news*")
    files = sorted(p for p in glob.glob(pat)
                   if re.search(r"_@?news\.txt$|__news\.txt$", p))
    items = {}       # (date, seq) -> dict
    used, skipped = [], []
    for path in files:
        body = open(path, encoding="utf-8", errors="replace").read()
        if not ANCHOR.search(body):
            skipped.append(os.path.basename(path))
            continue
        used.append(os.path.basename(path))
        seq_per_date = {}
        for date, cls, title, blob in parse_capture(body):
            seq = seq_per_date.get(date, 0)
            seq_per_date[date] = seq + 1
            key = (date, seq)
            cur = items.get(key)
            rec = {"cls": cls, "title": title, "blob": blob, "conflict": False,
                   "old_titles": set()}
            if cur is None:
                items[key] = rec
                continue
            if cur["title"] != title:
                # the page was live-edited (e.g. 28-04-2017 lost "- 7 Days
                # Left to Vote" once voting closed): keep the end state,
                # record the earlier one
                cur["old_titles"].add(cur["title"])
                cur["title"] = title
                cur.update({"cls": cls, "blob": blob, "conflict": True})
            elif norm(cur["blob"]) == norm(blob):
                if len(blob) > len(cur["blob"]):
                    cur["blob"], cur["cls"] = blob, cls
            else:
                # later capture wins; remember that captures disagreed
                cur.update({"cls": cls, "blob": blob, "conflict": True})

    conflicts = sorted(k for k, v in items.items() if v["conflict"])
    out = provenance_header(
        "seed_news.py", "O", "M2",
        "%d dated items sliced verbatim from %d anchored classic ?news "
        "captures in archive/commoncrawl/warc-bodies/" % (len(items), len(used)),
        "body is the byte-verbatim capture slice; whether the original kept "
        "these blobs in a DB or a hand-edited file is NOT observable (see "
        "module docstring), hence schema M2 not M1.")
    out += "INSERT INTO news (posted, seq, css_class, title, body) VALUES\n"
    vals = []
    for date, seq in sorted(items, key=lambda k: (iso(k[0]), k[1])):
        it = items[(date, seq)]
        vals.append("(%s, %d, %s, %s, %s)" % (
            sql_str(iso(date)), seq, sql_str(it["cls"]),
            sql_str(it["title"]), sql_str(it["blob"])))
    out += ",\n".join(vals) + ";\n"
    out += "\n-- captures used: %s\n" % ", ".join(used)
    out += "-- captures skipped (pre-anchor classic or modern-SPA): %s\n" % \
           ", ".join(skipped)
    out += "-- items live-edited across captures (latest kept): %s\n" % (
        ", ".join("%s#%d" % k for k in conflicts) or "none")
    edited = {k: v["old_titles"] for k, v in items.items() if v["old_titles"]}
    for k in sorted(edited):
        out += "--   earlier title of %s#%d: %s\n" % (
            k[0], k[1], " | ".join(sorted(edited[k])))
    write_out("30-news.sql", out)
    print("news: %d items, %d cross-capture divergent, %d captures used, "
          "%d skipped" % (len(items), len(conflicts), len(used), len(skipped)))


if __name__ == "__main__":
    main()
