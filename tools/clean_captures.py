"""Guide 6.1a steps 1-2 / 9 step 3: captured route bodies -> archive-cleaned/

Layer 1, `served` (tier O): the bytes the server actually sent. Common Crawl
bodies are already raw (no Wayback toolbar, no URL rewriting), verified here
by marker scan + gzip magic check. Raw sources are NOT copied -- the
manifest sha256-locks each one in place in the archive; a physical file
appears under archive-cleaned/served/ only if a byte transform (gunzip,
toolbar strip) was needed. So far: none.

Layer 2, `depagespeed` (derived, mechanical): PageSpeed's transforms undone
where the inversion is exact:
  * `a.js+b.js+dir,_c.js.pagespeed.jc.HASH.js` bundles -> the original
    separate <script> tags (the bundle filename enumerates its inputs;
    `,_` encodes `/`)
  * single-resource cache-extended URLs `x.ext.pagespeed.<filter>.HASH.ext`
    -> `x.ext`
Whitespace collapse is NOT undone (the original whitespace is unknowable
from a collapsed capture); cross-capture diffing must normalise whitespace
instead. Inlined-resource reversal (.ic.) is left to milestone 3 if any
route actually needs it -- occurrences are counted in the manifest.

Scope: classic-era (ts <= 20201204) tanktrouble.com captures of the de-render
targets: the 6 ?query routes, the bare dispatcher /, embed.php, /infirmary/,
/statistics/. Modern-era and foreign-host files are out of scope (grade D).

Deterministic: same archive -> byte-identical outputs + manifest.
"""

import glob
import hashlib
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get("TT_CLEANED_OUT_DIR",
                     os.path.join(REPO, "archive-cleaned"))
CLASSIC_END = "20201204"

ROUTES = {
    "": "root", "_game": "game", "_garage": "garage", "_news": "news",
    "_forum": "forum", "_lab": "lab", "_shop": "shop",
    "embed.php": "embed", "infirmary_": "infirmary", "statistics_": "statistics",
}
FNAME = re.compile(
    r"^(\d{8,14})(?:_(\d{3}))?_(www\.|beta\.)?(tanktrouble\.com)_?(.*)\.txt$")
# normalise the two observed spellings of a query route: `_game` and `@game`
QUERY_ALIAS = {"@%s" % r[1:]: r for r in ROUTES if r.startswith("_")}

PS_BUNDLE = re.compile(
    r"""(['"])([^'"]*?)\.pagespeed\.jc\.([A-Za-z0-9_-]+)\.js\1""")
PS_SINGLE = re.compile(
    r"([\w./%-]+?)\.pagespeed\.(?:ce|cf|jm|ic)\.[A-Za-z0-9_-]+(\.\w+)")


def archive_root():
    root = os.environ.get("TT_ARCHIVE_ROOT", os.path.join(REPO, "archive"))
    if not os.path.isdir(root):
        sys.exit("archive root not found: %s" % root)
    return root


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def split_bundle(prefix, bundle_name):
    """`a.js+b.js+dir,_c.js` -> script tags for a.js, b.js, dir/c.js."""
    parts = bundle_name.split("+")
    tags = []
    for p in parts:
        p = p.replace(",_", "/")
        tags.append('<script type="text/javascript" src="%s%s"></script>'
                    % (prefix, p))
    return "\n".join(tags)


def depagespeed(text):
    """Mechanically invert PageSpeed URL transforms. Returns (text, counts)."""
    counts = {"jc_bundles": 0, "single_urls": 0, "ic_left": 0}

    def bundle_repl(m):
        counts["jc_bundles"] += 1
        quote, path = m.group(1), m.group(2)
        prefix, _, bundle = path.rpartition("/")
        if prefix:
            prefix += "/"
        return quote + "\x00BUNDLE\x00" + split_bundle(prefix, bundle) + "\x00" + quote

    # bundles appear as src='...pagespeed.jc....js' inside a script tag; the
    # whole tag must become N tags. Handle the full tag form.
    tag_pat = re.compile(
        r"""<script[^>]*\bsrc=(['"])([^'"]*?\.pagespeed\.jc\.[A-Za-z0-9_-]+\.js)\1[^>]*>\s*</script>""")

    def tag_repl(m):
        counts["jc_bundles"] += 1
        path = m.group(2)
        prefix, _, bundle = path.rpartition("/")
        if prefix:
            prefix += "/"
        bundle = re.sub(r"\.pagespeed\.jc\.[A-Za-z0-9_-]+\.js$", "", bundle)
        return split_bundle(prefix, bundle)

    text = tag_pat.sub(tag_repl, text)

    def single_repl(m):
        counts["single_urls"] += 1
        return m.group(1) + m.group(2)

    text = PS_SINGLE.sub(single_repl, text)
    counts["ic_left"] = text.count(".pagespeed.ic.")
    return text, counts


def main():
    root = archive_root()
    src_dir = os.path.join(root, "commoncrawl", "warc-bodies")
    rows = []
    skipped = {"modern": 0, "foreign": 0, "nonroute": 0}
    for path in sorted(glob.glob(os.path.join(src_dir, "*"))):
        base = os.path.basename(path)
        m = FNAME.match(base)
        if not m or "tanktrouble.com" not in base:
            skipped["foreign"] += 1
            continue
        ts, status, sub, host, tail = m.groups()
        if sub == "beta.":
            skipped["foreign"] += 1
            continue
        tail = QUERY_ALIAS.get(tail, tail)
        if tail not in ROUTES:
            skipped["nonroute"] += 1
            continue
        if ts[:8] > CLASSIC_END:
            skipped["modern"] += 1
            continue
        if status and status != "200":
            skipped["nonroute"] += 1
            continue
        raw = open(path, "rb").read()
        if raw[:2] == b"\x1f\x8b":
            sys.exit("gzip body needs a served/ transform (unimplemented): %s" % base)
        text = raw.decode("utf-8", errors="replace")
        if "wm-ipp" in text or "/web/20" in text:
            sys.exit("wayback artefacts need a served/ transform: %s" % base)

        route = ROUTES[tail]
        cleaned, counts = depagespeed(text)
        out_rel = None
        if cleaned != text:
            out_rel = "depagespeed/%s/%s_%s.html" % (
                route, ts, (sub or "") + host)
            out_path = os.path.join(OUT, out_rel)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8", newline="") as f:
                f.write(cleaned)
        rows.append({
            "route": route, "ts": ts, "host": (sub or "") + host,
            "source": "archive/commoncrawl/warc-bodies/" + base,
            "sha256_served": sha256(raw),
            "depagespeed": out_rel or "—",
            "sha256_depagespeed": sha256(cleaned.encode("utf-8")) if out_rel else "—",
            "jc_bundles": counts["jc_bundles"],
            "single_urls": counts["single_urls"],
            "ic_left": counts["ic_left"],
        })

    os.makedirs(OUT, exist_ok=True)
    cols = ["route", "ts", "host", "source", "sha256_served", "depagespeed",
            "sha256_depagespeed", "jc_bundles", "single_urls", "ic_left"]
    with open(os.path.join(OUT, "MANIFEST.tsv"), "w", encoding="utf-8",
              newline="\n") as f:
        f.write("\t".join(cols) + "\n")
        for r in sorted(rows, key=lambda r: (r["route"], r["ts"], r["host"])):
            f.write("\t".join(str(r[c]) for c in cols) + "\n")

    by_route = {}
    for r in rows:
        by_route.setdefault(r["route"], [0, 0])
        by_route[r["route"]][0] += 1
        by_route[r["route"]][1] += 1 if r["depagespeed"] != "—" else 0
    for route in sorted(by_route):
        n, ps = by_route[route]
        print("%-11s %3d captures, %3d with pagespeed inversions" % (route, n, ps))
    print("total %d rows; skipped %s" % (len(rows), skipped))


if __name__ == "__main__":
    main()
