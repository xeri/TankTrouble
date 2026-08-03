"""Guide 6.1a step 3 prep: separate static template from dynamic output.

For each de-render route, diff every era-window (2017-2018) capture against
a reference capture (the latest era one). A reference line that survives
byte-identical in EVERY era capture is literal template text; contiguous
runs of non-surviving lines are dynamic regions the PHP echoed.

Output per route: archive-cleaned/classification/<route>.tsv
  region_id  ref_lines  status  survivors  sample
plus a summary in classification/REPORT.md. This is the DRAFT input to the
gate-F mask files -- milestone 3 annotates each dynamic region with what
variable produced it; a region that cannot be annotated is a region not yet
understood (guide 6.1a step 3), and the mask must not grow to hide it.

Line-level granularity is deliberate: PageSpeed never touched these bodies
(classic captures are artifact-free, see DECISIONS) and the originals keep
one statement per line almost everywhere, so lines approximate PHP
echo-boundaries well. Byte-level refinement belongs to milestone 3.

Deterministic: same archive -> byte-identical outputs.

Milestone 3: annotate_regions.py imports this module's loading/alignment
functions and OWNS the TSVs from then on (adds annotation + region_sha
columns, merges annotations across regenerations). Do not run this file's
main() once annotations exist -- it writes the draft 4-column format and
would drop them; use `python tools/annotate_regions.py --regen` instead.
"""

import difflib
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get("TT_CLASSIFY_OUT_DIR",
                     os.path.join(REPO, "archive-cleaned", "classification"))
ERA = ("20170101", "20181231")
ROUTES = ["root", "game", "garage", "news", "forum", "lab", "shop",
          "embed", "infirmary", "statistics"]


def archive_root():
    root = os.environ.get("TT_ARCHIVE_ROOT", os.path.join(REPO, "archive"))
    if not os.path.isdir(root):
        sys.exit("archive root not found: %s" % root)
    return root


def manifest_rows():
    path = os.path.join(REPO, "archive-cleaned", "MANIFEST.tsv")
    lines = open(path, encoding="utf-8").read().splitlines()
    cols = lines[0].split("\t")
    return [dict(zip(cols, l.split("\t"))) for l in lines[1:] if l.strip()]


def era_captures(rows, route):
    picked = []
    for r in rows:
        if r["route"] != route:
            continue
        if not (ERA[0] <= r["ts"][:8] <= ERA[1]):
            continue
        picked.append(r)
    return sorted(picked, key=lambda r: r["ts"])


def load_bodies(root, caps):
    """splitlines() bodies for manifest rows, archive order preserved."""
    bodies = []
    for r in caps:
        src = os.path.join(root, r["source"].replace("archive/", "", 1))
        bodies.append(open(src, encoding="utf-8",
                           errors="replace").read().splitlines())
    return bodies


def compute_survives(bodies):
    """(ref, survives): ref = latest era capture, survives[i] True iff ref
    line i is byte-matched in EVERY other era capture."""
    ref = bodies[-1]
    survives = [True] * len(ref)
    for other in bodies[:-1]:
        matched = [False] * len(ref)
        for op in difflib.SequenceMatcher(
                a=ref, b=other, autojunk=False).get_matching_blocks():
            for i in range(op.a, op.a + op.size):
                matched[i] = True
        survives = [s and m for s, m in zip(survives, matched)]
    return ref, survives


def region_runs(survives):
    """Contiguous (region_id, start0, end0_excl, status) runs, the exact
    numbering the draft TSVs used."""
    runs = []
    rid = 0
    i = 0
    n = len(survives)
    while i < n:
        j = i
        while j < n and survives[j] == survives[i]:
            j += 1
        runs.append(("%s%03d" % ("S" if survives[i] else "D", rid), i, j,
                     "static" if survives[i] else "dynamic"))
        rid += 1
        i = j
    return runs


def main():
    root = archive_root()
    rows = manifest_rows()
    os.makedirs(OUT, exist_ok=True)
    report = ["# Region classification draft (guide 6.1a step 3)", "",
              "Era window %s..%s. Reference = latest era capture per route." %
              ERA, ""]
    report.append("| route | era captures | ref lines | static lines | "
                  "dynamic regions |")
    report.append("|---|---|---|---|---|")

    for route in ROUTES:
        caps = era_captures(rows, route)
        if len(caps) < 2:
            report.append("| %s | %d | — | — | too few era captures |"
                          % (route, len(caps)))
            continue
        bodies = load_bodies(root, caps)
        ref, survives = compute_survives(bodies)
        regions = [(a, b) for _, a, b, st in region_runs(survives)
                   if st == "dynamic"]

        out_path = os.path.join(OUT, "%s.tsv" % route)
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write("region_id\tref_lines\tstatus\tsample\n")
            for rid_s, i, j, status in region_runs(survives):
                f.write("%s\t%d-%d\t%s\t%s\n" % (
                    rid_s, i + 1, j, status, sample(ref[i])))
        n_static = sum(survives)
        report.append("| %s | %d | %d | %d (%.0f%%) | %d |" % (
            route, len(caps), len(ref), n_static,
            100.0 * n_static / max(1, len(ref)), len(regions)))
        print("%-11s %2d caps, %5d ref lines, %5d static, %3d dynamic regions"
              % (route, len(caps), len(ref), n_static, len(regions)))

    report += ["",
               "Every dynamic region needs a milestone-3 annotation naming the",
               "variable/loop that produced it before route PHP is written.", ""]
    with open(os.path.join(OUT, "REPORT.md"), "w", encoding="utf-8",
              newline="\n") as f:
        f.write("\n".join(report))


def sample(line, limit=80):
    s = re.sub(r"\s+", " ", line).strip()
    return s[:limit]


if __name__ == "__main__":
    main()
