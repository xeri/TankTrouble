"""Gate D — structural. Every srv/ file has a ledger row; every M* file
announces itself; no unverified stub returns 200; no credential-shaped
strings. See REBUILD-GUIDE.md 7.4."""

import re

from conftest import DASH, REPO, TEXT_EXTS, srv_files

PROV_RE = re.compile(r"@provenance\s+(M1|M2|M3)")
CRED_PATTERNS = [
    re.compile(r"(?i)passw(or)?d\s*[=:]\s*\S{4,}"),
    re.compile(r"mysql:" + r"//"),  # split so the scanner never matches itself
    re.compile(r"(?i)authorization:\s*basic"),
]
SCAN_DIRS = ["srv", "tools", "tests", "docker"]
ALLOWLIST = REPO / "tests" / "credscan_allowlist.txt"


def mstar_file_rows(ledger):
    return [r for r in ledger
            if r["tier"] in ("M1", "M2", "M3") and (REPO / r["path"]).is_file()]


def test_every_file_has_row(ledger):
    row_paths = {r["path"] for r in ledger}
    unlabelled = [f for f in srv_files() if f not in row_paths]
    assert not unlabelled, f"unlabelled files in srv/: {unlabelled}"


def test_mstar_headers(ledger):
    bad = []
    for r in mstar_file_rows(ledger):
        f = REPO / r["path"]
        if f.suffix.lower() not in TEXT_EXTS:
            continue
        head = f.read_text(encoding="utf-8", errors="replace")[:2048]
        m = PROV_RE.search(head)
        if not m:
            bad.append(f"{r['path']}: no parseable @provenance header")
            continue
        if m.group(1) != r["tier"]:
            bad.append(f"{r['path']}: header says {m.group(1)}, ledger says {r['tier']}")
        for field in ("@evidence", "@written"):
            if field not in head:
                bad.append(f"{r['path']}: header missing {field}")
    assert not bad, "\n".join(bad)


def test_stubs_never_200(ledger):
    """A stub that returns plausible data is the most dangerous thing in this
    project. Exemption: verified_by names an existing test file (validated in
    Gate A) — at milestone 1, nothing is exempt."""
    bad = []
    for r in mstar_file_rows(ledger):
        if not r["path"].endswith(".php") or r["verified_by"] != DASH:
            continue
        body = (REPO / r["path"]).read_text(encoding="utf-8", errors="replace")
        if "HTTP/1.1 501 Not Implemented" not in body:
            bad.append(f"{r['path']}: unverified stub without 501 header")
        if "die(" not in body or "STUB" not in body:
            bad.append(f"{r['path']}: unverified stub must die loudly")
        if "HTTP/1.1 200" in body:
            bad.append(f"{r['path']}: unverified stub emits 200")
    assert not bad, "\n".join(bad)


def test_mstar_binaries_have_sidecar(ledger):
    """M* binaries need <name>.provenance. Vacuous at milestone 1 (no M*
    binaries exist); O binaries deliberately need no sidecar — their
    provenance is the ledger row (DECISIONS.md)."""
    bad = []
    for r in mstar_file_rows(ledger):
        f = REPO / r["path"]
        if f.suffix.lower() in TEXT_EXTS:
            continue
        side = f.with_name(f.name + ".provenance")
        if not side.is_file() or "@provenance" not in side.read_text(
                encoding="utf-8", errors="replace"):
            bad.append(f"{r['path']}: M* binary without parseable sidecar")
    assert not bad, "\n".join(bad)


def test_no_credential_shaped_strings():
    allow = set()
    if ALLOWLIST.is_file():
        for line in ALLOWLIST.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                allow.add(line)
    bad = []
    for d in SCAN_DIRS:
        base = REPO / d
        if not base.is_dir():
            continue
        for f in base.rglob("*"):
            if not f.is_file() or f.suffix.lower() not in TEXT_EXTS:
                continue
            rel = f.relative_to(REPO).as_posix()
            if rel in allow:
                continue
            text = f.read_text(encoding="utf-8", errors="replace")
            for pat in CRED_PATTERNS:
                m = pat.search(text)
                if m:
                    bad.append(f"{rel}: credential-shaped string {m.group(0)!r}")
                    break
    assert not bad, ("\n".join(bad) +
                     "\nIf legitimate, add the path to tests/credscan_allowlist.txt")
