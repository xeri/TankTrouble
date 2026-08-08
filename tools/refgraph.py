#!/usr/bin/env python3
"""Subresource reference graph for srv/ — the page-side half of the ledger.

The ledger answers "what is this file and where did it come from". It cannot
answer "what does the site ASK the browser for", because it is built from what
was FOUND, not from what is REFERENCED. Milestone-3 review found the gap: the
2018 front page requests 182 local assets that srv/ does not hold, every gate
green, because gates A/D walk srv -> ledger and gate F byte-diffs HTML only.
A byte-perfect page serving zero images passed all three.

This module walks the other direction: entry point -> subresource. Gate E
(tests/test_subresources.py) and tools/resolve_assets.py both import it, so
the gate and the recovery tool can never disagree about what "referenced"
means.

Extraction is deliberately STATIC and conservative:

  * markup   src=/href=/action=, <param name="movie" value=...>, inline
             style="... url(...)"
  * css      url(...)  (relative to the stylesheet's own directory)
  * js       whole string literals that end in an asset extension

Runtime-assembled names ('images/tool' + x + 'Select.jpg') are NOT resolvable
statically. They are collected separately as `dynamic` so they show up in
reports instead of silently counting as "no reference" — see
docs/standards/ASSET-DISCIPLINE.md.

Reachability starts at every .php/.htm(l) under srv/ (each is a route or an
endpoint) and follows referenced stylesheets AND scripts. Assets referenced
only by an UNREFERENCED file are not the site's dependencies and are reported
as `unreachable`, not as defects.

Base directories differ by referrer type and this matters:

  * a CSS url() resolves against the STYLESHEET's directory
  * a URL in a JS string resolves against the DOCUMENT that loaded the script

Getting the second one wrong is not academic. srv/includes/scrapyard.js:104
loads 'images/scrapyardPlates.png'; resolved script-relative that reads as
/includes/images/scrapyardPlates.png, which is how it came to sit in the
ledger as known-lost ("obs in CDX, 404 only"). The browser asks for
/images/scrapyardPlates.png, which the era captured with status 200. The file
was never lost — it was looked for in a place the site never used.
"""

import posixpath
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRV = REPO / "srv"

MARKUP_EXTS = {".php", ".html", ".htm"}
CSS_EXTS = {".css"}
JS_EXTS = {".js"}
ASSET_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".ico", ".css", ".js",
              ".swf", ".pdf", ".zip", ".woff", ".woff2", ".ttf", ".eot",
              ".mp3", ".wav", ".xml", ".txt"}

# an href/src value we must never treat as a local file reference
EXTERNAL_PREFIXES = ("http://", "https://", "//", "mailto:", "tel:",
                     "javascript:", "data:", "#", "?", "{")

ATTR_RE = re.compile(r'(?:src|href|action)\s*=\s*"([^"]*)"', re.I)
ATTR_SQ_RE = re.compile(r"(?:src|href|action)\s*=\s*'([^']*)'", re.I)
PARAM_MOVIE_RE = re.compile(
    r'<param\s+name\s*=\s*"movie"\s+value\s*=\s*"([^"]*)"', re.I)
CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)([^)'\"]+)\1\s*\)", re.I)
JS_LITERAL_RE = re.compile(r"""(['"])([^'"\n]*?\.(?:jpg|jpeg|png|gif|svg|swf|css|js|mp3|wav|ico))\1""", re.I)
# a literal glued to a `+` on either side is a FRAGMENT of a runtime-assembled
# name ('images/x' + tool + 'Select.jpg'), never a whole reference
CONCAT_EDGE_RE = re.compile(r"\+\s*$")
# 'images/foo' + expr + 'Select.jpg' — a name the browser gets but we cannot
CONCAT_RE = re.compile(
    r"""(['"])([A-Za-z0-9_./-]*/[A-Za-z0-9_.-]*)\1\s*\+[^;\n]*?\+\s*(['"])([A-Za-z0-9_.-]*\.(?:jpg|jpeg|png|gif|svg|swf))\3""",
    re.I)


class Ref:
    """One extracted reference.

    kind:
      ok       resolves to an existing file under srv/
      missing  resolves under srv/ but no such file

    `clamped` marks a reference whose ../ segments would walk above the
    document root. RFC 3986 5.2.4 remove_dot_segments drops those, and every
    browser follows it, so `/?news` asking for `../images/x.jpg` really did
    fetch `/images/x.jpg`. Recorded because it makes the reference look
    broken when it is not.
    """

    __slots__ = ("raw", "src_file", "target", "kind", "clamped")

    def __init__(self, raw, src_file, target, kind, clamped=False):
        self.raw = raw
        self.src_file = src_file      # repo-relative posix, e.g. srv/index.php
        self.target = target          # docroot-relative posix, e.g. images/x.jpg
        self.kind = kind
        self.clamped = clamped

    def __repr__(self):
        return f"Ref({self.target!r} <- {self.src_file}, {self.kind})"

    @property
    def srv_path(self):
        """Repo-relative path the target WOULD have. Meaningless if it escapes."""
        return f"srv/{self.target}"


def _read(p):
    return p.read_text(encoding="utf-8", errors="replace")


def _whole_js_literals(text):
    """String literals that are a complete asset name, not a concat fragment."""
    out = []
    for m in JS_LITERAL_RE.finditer(text):
        before = text[max(0, m.start() - 40):m.start()].rstrip()
        after = text[m.end():m.end() + 40].lstrip()
        if before.endswith("+") or after.startswith("+"):
            continue
        out.append(m.group(2))
    return out


def _raw_refs(path):
    """(raw value, is_css_context) pairs extracted from one file."""
    text = _read(path)
    ext = path.suffix.lower()
    out = []
    if ext in MARKUP_EXTS:
        for m in ATTR_RE.finditer(text):
            out.append(m.group(1))
        for m in ATTR_SQ_RE.finditer(text):
            out.append(m.group(1))
        for m in PARAM_MOVIE_RE.finditer(text):
            out.append(m.group(1))
        for m in CSS_URL_RE.finditer(text):     # inline style="... url(x)"
            out.append(m.group(2))
        out.extend(_whole_js_literals(text))    # inline <script>
    elif ext in CSS_EXTS:
        for m in CSS_URL_RE.finditer(text):
            out.append(m.group(2))
    elif ext in JS_EXTS:
        out.extend(_whole_js_literals(text))
    return out


def _dynamic_refs(path):
    """Runtime-assembled asset names, as '<prefix>*<suffix>' shapes."""
    if path.suffix.lower() not in MARKUP_EXTS | JS_EXTS:
        return []
    return sorted({f"{m.group(2)}*{m.group(4)}"
                   for m in CONCAT_RE.finditer(_read(path))})


def _classify(raw, src_file, base):
    """raw href/url value + referring file + resolution base -> Ref, or None
    if the value is external / not a file reference."""
    value = raw.strip()
    if not value or value.startswith(EXTERNAL_PREFIXES):
        return None
    if "://" in value:
        return None
    clean = value.split("?", 1)[0].split("#", 1)[0]
    if not clean:
        return None
    joined = posixpath.normpath(posixpath.join(base, clean))
    clamped = False
    if joined == "srv" or not (joined + "/").startswith("srv/"):
        # RFC 3986 5.2.4: leading ../ that would pass the root is discarded
        clamped = True
        joined = "srv/" + posixpath.normpath(clean).lstrip("./")
        while joined.startswith("srv/../"):
            joined = "srv/" + joined[len("srv/../"):]
    target = joined[len("srv/"):]
    if not target or not posixpath.splitext(target)[1]:
        return None                                  # a route, not a file
    kind = "ok" if (REPO / joined).is_file() else "missing"
    return Ref(value, src_file, target, kind, clamped)


def entry_points():
    """Route/endpoint files: every markup file under srv/."""
    return sorted(p for p in SRV.rglob("*")
                  if p.is_file() and p.suffix.lower() in MARKUP_EXTS)


def build(follow_css=True):
    """Walk srv/ from its entry points.

    Returns (refs, dynamic, unreachable_refs):
      refs             list[Ref] reachable from an entry point
      dynamic          {referring file: ['images/foo*Select.jpg', ...]}
      unreachable_refs list[Ref] found only in files nothing references
    """
    reached = []
    dynamic = {}
    seen_files = set()
    # (file, base directory its own references resolve against)
    queue = [(p, p.relative_to(REPO).as_posix().rsplit("/", 1)[0])
             for p in entry_points()]

    while queue:
        path, base = queue.pop()
        rel = path.relative_to(REPO).as_posix()
        if (rel, base) in seen_files:
            continue
        seen_files.add((rel, base))
        dyn = _dynamic_refs(path)
        if dyn:
            dynamic[rel] = dyn
        for raw in _raw_refs(path):
            ref = _classify(raw, rel, base)
            if ref is None or ref.kind != "ok":
                if ref is not None:
                    reached.append(ref)
                continue
            reached.append(ref)
            ext = posixpath.splitext(ref.target)[1].lower()
            if follow_css and ext in CSS_EXTS:
                # url() is stylesheet-relative
                queue.append((REPO / ref.srv_path,
                              posixpath.dirname(ref.srv_path)))
            elif ext in JS_EXTS:
                # a URL in a script string is document-relative
                queue.append((REPO / ref.srv_path, base))

    walked = {rel for rel, _base in seen_files}
    unreachable = []
    for path in SRV.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(REPO).as_posix()
        if rel in walked or path.suffix.lower() not in CSS_EXTS | JS_EXTS:
            continue
        for raw in _raw_refs(path):
            ref = _classify(raw, rel, posixpath.dirname(rel))
            if ref is not None:
                unreachable.append(ref)
    return reached, dynamic, unreachable


def defects(refs):
    """Distinct docroot-relative targets that are referenced but absent."""
    return sorted({r.target for r in refs if r.kind == "missing"})


def clamped(refs):
    """Distinct (referring file, target) whose ../ was clamped at the root."""
    return sorted({(r.src_file, r.target) for r in refs if r.clamped})


def _main():
    refs, dynamic, unreachable = build()
    kinds = {}
    for r in refs:
        kinds[r.kind] = kinds.get(r.kind, 0) + 1
    print("reachable references:", len(refs), kinds)
    print("distinct missing targets:", len(defects(refs)))
    for t in defects(refs):
        print("   MISSING", t)
    print("\nroot-clamped (../ above docroot, browser drops it):",
          len(clamped(refs)))
    for src, t in clamped(refs):
        print(f"   {t}   <- {src}")
    print("\nruntime-assembled names:")
    for src, names in sorted(dynamic.items()):
        for n in names:
            print(f"   {n}   <- {src}")
    print("\nrefs reachable only from unreferenced files:",
          len({r.target for r in unreachable}))


if __name__ == "__main__":
    _main()
