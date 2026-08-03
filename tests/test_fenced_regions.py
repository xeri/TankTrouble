"""Mixed-provenance fence verifier (DECISIONS 2026-08-02 obligation).

De-rendered files are written PHP wrapping verbatim original HTML. Each
verbatim region is fenced:

    /* @O-begin source=<repo-rel-path> lines=<a>-<b> */ ?>
    ...verbatim bytes...
    <?php /* @O-end */

Grammar refinement over README (recorded in DECISIONS 2026-08-03): the
fence names its source SPAN (lines=<a>-<b>, 1-based inclusive) — a bare
path cannot be byte-verified. The fenced body is the file text between the
newline after `?>` and the newline before `<?php /* @O-end */` — PHP eats
exactly one newline after `?>`, so emitted output equals the fenced bytes.

Checks, for every M* text file under srv/:
  1. every fence parses and its source span exists;
  2. the fenced body byte-matches the source span;
  3. every fence is declared in the header's @contains line;
  4. begin/end markers balance.
Vacuously green until the first de-rendered file lands; a self-test keeps
the parser honest meanwhile.
"""

import re

from conftest import REPO, TEXT_EXTS, parse_ledger

FENCE_RE = re.compile(
    r"/\* @O-begin source=(?P<src>[^ ]+) lines=(?P<a>\d+)-(?P<b>\d+) \*/ "
    r"\?>\n(?P<body>.*?)\n<\?php /\* @O-end \*/",
    re.DOTALL)


def fences_in(text):
    return list(FENCE_RE.finditer(text))


def raw_read(path):
    """No newline translation — fenced bytes may carry \\r\\n verbatim."""
    with open(path, encoding="utf-8", errors="replace", newline="") as f:
        return f.read()


def mstar_texts():
    for r in parse_ledger():
        if r["tier"] not in ("M1", "M2", "M3"):
            continue
        f = REPO / r["path"]
        if f.is_file() and f.suffix.lower() in TEXT_EXTS:
            yield r["path"], raw_read(f)


def test_fenced_regions_byte_match():
    bad = []
    for path, text in mstar_texts():
        n_begin = text.count("@O-begin")
        fences = fences_in(text)
        if n_begin != len(fences) or text.count("@O-end") != n_begin:
            bad.append("%s: %d @O-begin markers but %d parseable fences "
                       "(malformed fence?)" % (path, n_begin, len(fences)))
            continue
        for m in fences:
            src = REPO / m.group("src")
            a, b = int(m.group("a")), int(m.group("b"))
            if not src.is_file():
                bad.append("%s: fence source missing %s" % (path,
                                                            m.group("src")))
                continue
            span = "".join(raw_read(src).splitlines(keepends=True)[a - 1:b])
            if span.endswith("\n"):
                span = span[:-1]
            if m.group("body") != span:
                bad.append("%s: fence %s lines %d-%d does not byte-match"
                           % (path, m.group("src"), a, b))
            token = "%s lines=%d-%d" % (m.group("src"), a, b)
            head = text[:4096]
            if "@contains" not in head or token not in head:
                bad.append("%s: fence %s not declared in @contains"
                           % (path, token))
    assert not bad, "\n".join(bad)


def test_fence_parser_self_test(tmp_path):
    """Guards the regex against rot while zero real fences exist."""
    src = tmp_path / "cap.txt"
    src.write_text("l1\nl2\nl3\nl4\n", encoding="utf-8", newline="\n")
    doc = ("<?php\n/* @O-begin source=%s lines=2-3 */ ?>\nl2\nl3\n"
           "<?php /* @O-end */\n" % src.as_posix())
    m = fences_in(doc)
    assert len(m) == 1 and m[0].group("body") == "l2\nl3"
    span = "\n".join(src.read_text(encoding="utf-8").splitlines()[1:3])
    assert m[0].group("body") == span
