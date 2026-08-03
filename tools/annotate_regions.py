"""Milestone 3 mask maintenance for gate F (guide 6.1a step 3, 7.4a).

Owns archive-cleaned/classification/<route>.tsv from milestone 3 on.
Extends the draft 4-column format with two columns:

  region_id  ref_lines  status  sample  annotation  region_sha

* annotation — WHY the region's bytes vary (dynamic rows only; static rows
  carry an em dash). Empty annotation on a dynamic region BLOCKS gate F for
  that route (GATE_F_SPEC). Vocabulary (DECISIONS 2026-08-03):

    echo:$<name> [re=<regex>]   one server-side value echoed; optional regex
                                with EXACTLY one capture group locates it
                                within the line (single-line regions only) --
                                the static remainder of the line then stays
                                gated instead of masked
    loop:<name>                 variable-height DB-driven block; line-mode
                                masks it, anchor-mode (phase C) gates its
                                item template
    template-edit:<from>[..<to>]  literal template text with validity window
                                (YYYYMMDD bounds, inclusive); byte-exact
                                inside window, masked outside; reference text
                                defines the in-window form
    per-request:<what>          varies every request (nonces, clocks,
                                cache-busters); always masked -- never fake
                                the clock to chase it
    ad-block                    third-party ad markup; always masked
    needs-split:<why>           region mixes causes at line granularity;
                                blocks the gate exactly like an empty cell

  Multiple annotations for one region: '; '-separated. A cell containing
  ' re=' must be a single annotation (regexes may contain ';').

* region_sha — sha256 of the region's reference lines ('\n'-joined), first
  12 hex chars. Annotations are keyed by (route, region_sha) so re-running
  classification (new captures, algorithm fixes) re-attaches them to
  unchanged regions instead of losing them; changed regions come back
  UNANNOTATED and must be re-examined -- that is the safety property.

Commands:
  --check                      coverage table (default)
  --variants ROUTE [REGION_ID] every distinct byte-form of dynamic region(s)
                               across era captures, with timestamps
  --set ROUTE REGION_ID ANNOT  validate + write one annotation
  --regen                      re-classify, merge annotations by region_sha,
                               rewrite TSVs + REPORT.md

Deterministic: same archive + same annotations -> byte-identical outputs.
"""

import difflib
import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import classify_regions as cls

OUT = cls.OUT
HEADER = ["region_id", "ref_lines", "status", "sample", "annotation",
          "region_sha"]
DASH = "—"
TS_RE = re.compile(r"\A\d{8}\Z")


# ---------------------------------------------------------------- vocabulary

def parse_annotation_cell(cell):
    """Return list of (kind, detail) or raise ValueError. Empty cell -> []."""
    cell = cell.strip()
    if not cell:
        return []
    if " re=" in cell:
        parts = [cell]          # regex may contain ';' -- no splitting
    else:
        parts = [p.strip() for p in cell.split(";") if p.strip()]
    out = []
    for p in parts:
        if p == "ad-block":
            out.append(("ad-block", ""))
            continue
        if ":" not in p:
            raise ValueError("unknown annotation %r" % p)
        kind, detail = p.split(":", 1)
        if kind == "echo":
            m = re.match(r"\A\$[A-Za-z_][A-Za-z0-9_.-]*", detail)
            if not m:
                raise ValueError("echo needs $<name>: %r" % p)
            rest = detail[m.end():]
            rx = None
            if rest:
                if not rest.startswith(" re="):
                    raise ValueError("echo tail must be ' re=<regex>': %r" % p)
                rx = rest[4:]
                try:
                    if re.compile(rx).groups != 1:
                        raise ValueError(
                            "echo regex needs EXACTLY one capture group: %r" % p)
                except re.error as e:
                    raise ValueError("echo regex does not compile (%s): %r"
                                     % (e, p))
            out.append(("echo", (m.group(0), rx)))
        elif kind == "loop":
            if not detail:
                raise ValueError("loop needs a name: %r" % p)
            out.append(("loop", detail))
        elif kind == "template-edit":
            b = detail.split("..")
            if not (1 <= len(b) <= 2 and all(TS_RE.match(x) for x in b)):
                raise ValueError(
                    "template-edit needs YYYYMMDD[..YYYYMMDD]: %r" % p)
            out.append(("template-edit",
                        (b[0], b[1] if len(b) == 2 else "99999999")))
        elif kind == "per-request":
            if not detail:
                raise ValueError("per-request needs <what>: %r" % p)
            out.append(("per-request", detail))
        elif kind == "needs-split":
            if not detail:
                raise ValueError("needs-split needs <why>: %r" % p)
            out.append(("needs-split", detail))
        else:
            raise ValueError("unknown annotation kind %r" % p)
    return out


def blocks_gate(cell):
    """True iff this dynamic-region cell blocks gate F for its route."""
    try:
        parsed = parse_annotation_cell(cell)
    except ValueError:
        return True
    return not parsed or any(k == "needs-split" for k, _ in parsed)


# ------------------------------------------------------------------ tsv io

def region_sha(ref, a, b):
    return hashlib.sha256(
        "\n".join(ref[a:b]).encode("utf-8")).hexdigest()[:12]


def tsv_path(route):
    return os.path.join(OUT, "%s.tsv" % route)


def read_tsv(route):
    """rows as dicts; draft 4-column files gain empty annotation/sha cells."""
    lines = open(tsv_path(route), encoding="utf-8").read().splitlines()
    cols = lines[0].split("\t")
    rows = []
    for l in lines[1:]:
        if not l.strip():
            continue
        cells = l.split("\t")
        cells += [""] * (len(HEADER) - len(cells))
        rows.append(dict(zip(HEADER, cells)))
    return cols, rows


def write_tsv(route, rows):
    with open(tsv_path(route), "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(HEADER) + "\n")
        for r in rows:
            f.write("\t".join(r[c] for c in HEADER) + "\n")


def route_context(route):
    root = cls.archive_root()
    caps = cls.era_captures(cls.manifest_rows(), route)
    if len(caps) < 2:
        sys.exit("route %r has too few era captures" % route)
    bodies = cls.load_bodies(root, caps)
    ref, survives = cls.compute_survives(bodies)
    return caps, bodies, ref, survives


# -------------------------------------------------------------- projection

def project(ref, other, a, b):
    """other-capture lines aligned (difflib) to ref[a:b]. Replace blocks are
    attributed whole if they overlap the range; inserts attach at either
    boundary."""
    out = []
    sm = difflib.SequenceMatcher(a=ref, b=other, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            lo, hi = max(i1, a), min(i2, b)
            if lo < hi:
                out.extend(other[j1 + (lo - i1): j1 + (hi - i1)])
        elif tag == "replace":
            if i1 < b and i2 > a:
                out.extend(other[j1:j2])
        elif tag == "insert":
            if a <= i1 <= b:
                out.extend(other[j1:j2])
    return out


# ---------------------------------------------------------------- commands

def cmd_check():
    total = need = 0
    print("%-11s %8s %10s %8s" % ("route", "dynamic", "annotated", "blocked"))
    for route in cls.ROUTES:
        if not os.path.exists(tsv_path(route)):
            continue
        _, rows = read_tsv(route)
        dyn = [r for r in rows if r["status"] == "dynamic"]
        blocked = [r["region_id"] for r in dyn if blocks_gate(r["annotation"])]
        print("%-11s %8d %10d %8d  %s" % (
            route, len(dyn), len(dyn) - len(blocked), len(blocked),
            ",".join(blocked[:8]) + ("..." if len(blocked) > 8 else "")))
        total += len(dyn)
        need += len(blocked)
    print("total dynamic %d, gate-blocking %d" % (total, need))
    return 1 if need else 0


def cmd_variants(route, only_rid=None):
    caps, bodies, ref, survives = route_context(route)
    for rid, a, b, status in cls.region_runs(survives):
        if status != "dynamic" or (only_rid and rid != only_rid):
            continue
        print("== %s %s lines %d-%d sha=%s" % (
            route, rid, a + 1, b, region_sha(ref, a, b)))
        forms = {}
        for cap, body in zip(caps, bodies):
            form = tuple(project(ref, body, a, b))
            forms.setdefault(form, []).append(cap["ts"])
        for form, tss in sorted(forms.items(), key=lambda kv: kv[1][0]):
            print("  -- %d capture(s) %s%s" % (
                len(tss), " ".join(tss[:6]),
                " ..%s" % tss[-1] if len(tss) > 6 else ""))
            if not form:
                print("     (absent)")
            for line in form:
                print("     |%s" % line[:200])
        print()


def cmd_set(route, rid, annot):
    if annot and annot != DASH:
        parse_annotation_cell(annot)      # raises on bad vocabulary
    _, rows = read_tsv(route)
    hit = [r for r in rows if r["region_id"] == rid]
    if not hit:
        sys.exit("no region %s in %s.tsv" % (rid, route))
    if hit[0]["status"] != "dynamic":
        sys.exit("%s %s is static; static rows stay %s" % (route, rid, DASH))
    hit[0]["annotation"] = annot
    write_tsv(route, rows)
    print("%s %s <- %s" % (route, rid, annot or "(cleared)"))


def cmd_regen():
    rows_manifest = cls.manifest_rows()
    root = cls.archive_root()
    report = ["# Region classification (guide 6.1a step 3, annotated for "
              "gate F)", "",
              "Era window %s..%s. Reference = latest era capture per route."
              % cls.ERA,
              "Maintained by tools/annotate_regions.py; annotations keyed by "
              "region_sha survive regeneration.", "",
              "| route | era captures | ref lines | static lines | dynamic "
              "regions | annotated | gate-blocking |",
              "|---|---|---|---|---|---|---|"]
    for route in cls.ROUTES:
        caps = cls.era_captures(rows_manifest, route)
        if len(caps) < 2:
            report.append("| %s | %d | — | — | too few era captures | — | — |"
                          % (route, len(caps)))
            continue
        bodies = cls.load_bodies(root, caps)
        ref, survives = cls.compute_survives(bodies)
        old = {}
        if os.path.exists(tsv_path(route)):
            _, old_rows = read_tsv(route)
            old = {r["region_sha"]: r["annotation"] for r in old_rows
                   if r["region_sha"] and r["annotation"]
                   and r["annotation"] != DASH}
        out_rows = []
        n_dyn = n_ann = n_blk = 0
        for rid, a, b, status in cls.region_runs(survives):
            sha = region_sha(ref, a, b)
            if status == "dynamic":
                annot = old.get(sha, "")
                n_dyn += 1
                if blocks_gate(annot):
                    n_blk += 1
                else:
                    n_ann += 1
            else:
                annot = DASH
            out_rows.append(dict(zip(HEADER, [
                rid, "%d-%d" % (a + 1, b), status, cls.sample(ref[a]),
                annot, sha])))
        write_tsv(route, out_rows)
        n_static = sum(survives)
        report.append("| %s | %d | %d | %d (%.0f%%) | %d | %d | %d |" % (
            route, len(caps), len(ref), n_static,
            100.0 * n_static / max(1, len(ref)), n_dyn, n_ann, n_blk))
        print("%-11s %3d dynamic, %3d annotated, %3d gate-blocking"
              % (route, n_dyn, n_ann, n_blk))
    report += ["",
               "A gate-blocking region (empty annotation or needs-split) "
               "blocks gate F for its whole route (GATE_F_SPEC).", ""]
    with open(os.path.join(OUT, "REPORT.md"), "w", encoding="utf-8",
              newline="\n") as f:
        f.write("\n".join(report))


def main(argv):
    if not argv or argv[0] == "--check":
        sys.exit(cmd_check())
    if argv[0] == "--variants" and len(argv) in (2, 3):
        cmd_variants(argv[1], argv[2] if len(argv) == 3 else None)
    elif argv[0] == "--set" and len(argv) == 4:
        cmd_set(argv[1], argv[2], argv[3])
    elif argv[0] == "--regen":
        cmd_regen()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
