import hashlib
import http.client
import os
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
STACK_HOST, STACK_PORT = "127.0.0.1", 8056


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "live: needs the seeded docker stack on 127.0.0.1:8056 "
        '(gates B/F); run offline gates only with -m "not live"')
SRV = REPO / "srv"
LEDGER = REPO / "LEDGER.tsv"
DASH = "—"  # em dash: honest empty cell
TIERS = {"O", "O?", "M1", "M2", "M3", "known-lost", "pending"}
HEADER = ["path", "tier", "sha256", "source", "evidence", "verified_by", "notes"]
TEXT_EXTS = {".php", ".js", ".css", ".html", ".htm", ".txt", ".md", ".yml",
             ".yaml", ".py", ".tsv", ".ini", ".example", ".json", ".xml",
             ".sql"}


@pytest.fixture(scope="session")
def archive_root():
    """The read-only archive. Gates FAIL (never skip) without it — a
    silently-skipped Gate A is a green lie."""
    root = os.environ.get("TT_ARCHIVE_ROOT") or str(REPO / "archive")
    p = Path(root)
    if not (p / "includes-tree").is_dir():
        pytest.fail(
            "archive root not found. Create the junction:\n"
            '  New-Item -ItemType Junction -Path "<repo>\\archive" '
            '-Target "<...>\\_NOT-PART-OF-MAIN-ARCHIVE_swf-recovered-2026-08-02"\n'
            "or set TT_ARCHIVE_ROOT. See README.md.")
    return p


def parse_ledger():
    assert LEDGER.is_file(), "LEDGER.tsv missing"
    lines = LEDGER.read_text(encoding="utf-8").splitlines()
    assert lines and lines[0].split("\t") == HEADER, "LEDGER.tsv header wrong"
    rows = []
    for i, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        cells = line.split("\t")
        assert len(cells) == len(HEADER), f"LEDGER.tsv line {i}: {len(cells)} cols"
        rows.append(dict(zip(HEADER, cells)))
    return rows


@pytest.fixture(scope="session")
def ledger():
    return parse_ledger()


@pytest.fixture(scope="session")
def stack(ledger):
    """The live docker pair. Live gates FAIL (never silently skip) without
    it — same philosophy as archive_root. Deliberate offline runs must say
    so on the command line: pytest -m "not live"."""
    want = next(r["sha256"] for r in ledger
                if r["path"] == "srv/includes/styles.css")
    try:
        conn = http.client.HTTPConnection(STACK_HOST, STACK_PORT, timeout=10)
        conn.request("GET", "/includes/styles.css")
        body = conn.getresponse().read()
        conn.close()
    except OSError as e:
        pytest.fail(
            "live gates (B/F) need the docker stack:\n"
            "  cd docker && docker compose up -d   (needs docker/.env)\n"
            'or run the offline gates only: pytest -m "not live"\n'
            "(%s)" % e)
    got = hashlib.sha256(body).hexdigest()
    if got != want:
        pytest.fail(
            "stack is up but serves wrong bytes for includes/styles.css — "
            "stale volume or wrong mount? Reseed:\n"
            "  cd docker && docker compose down -v && docker compose up -d")
    return (STACK_HOST, STACK_PORT)


def srv_files():
    """All files under srv/, repo-relative posix paths, sidecars excluded."""
    return sorted(
        p.relative_to(REPO).as_posix()
        for p in SRV.rglob("*")
        if p.is_file() and not p.name.endswith(".provenance"))
