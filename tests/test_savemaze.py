"""saveMaze.php (M3) — invented wire format, validation vs corpus rules.

Live tests POST to the docker stack. The endpoint is INVENTION mirroring
loadMaze.php conventions (DECISIONS.md 2026-08-03); these tests pin the
invented contract so it cannot drift silently.
"""
import base64
import pathlib
import subprocess
import urllib.error
import urllib.parse
import urllib.request

import pytest

BASE = "http://127.0.0.1:8056"
SRV = pathlib.Path(__file__).resolve().parent.parent / "srv"
MYSQL_CONTAINER = "docker-mysql-1"

VALID_GRID = "4#1111111111111111#0#2#1#1#5##2#2#8###0#"


@pytest.fixture(scope="module", autouse=True)
def clean_test_mazes():
    """Remove rows this module writes, keeping the seeded corpus pristine —
    gate B's coverage test asserts every random-maze response is an archived
    winner state, so test writes must not outlive the module. testuser01 is
    synthetic (seed_users) and owns no corpus maze. Best-effort: offline
    runs write nothing and docker may be absent."""
    yield
    try:
        subprocess.run(
            ["docker", "exec", MYSQL_CONTAINER, "sh", "-c",
             'exec mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" tanktrouble '
             "-e \"DELETE FROM mazes WHERE author='testuser01'\""],
            capture_output=True, text=True, timeout=60)
    except OSError:
        pass


def post_save(inner):
    q = base64.b64encode(inner.encode()).decode()
    body = urllib.parse.urlencode({"q": q}).encode()
    req = urllib.request.Request(BASE + "/includes/saveMaze.php", data=body, method="POST")
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def decode_r(body):
    assert body.startswith("r="), body
    pairs = {}
    for pair in base64.b64decode(body[2:]).decode("latin1").split("&"):
        k, _, v = pair.partition("=")
        pairs[k] = v
    return pairs


def test_header_is_m3_and_loud():
    src = (SRV / "includes" / "saveMaze.php").read_text()
    assert "@provenance M3" in src
    assert "INVENT" in src.upper()
    assert "DO NOT PROMOTE" in src


@pytest.mark.live
def test_get_is_rejected():
    try:
        with urllib.request.urlopen(BASE + "/includes/saveMaze.php") as r:
            status = r.status
    except urllib.error.HTTPError as e:
        status = e.code
    assert status == 405


@pytest.mark.live
def test_valid_save_roundtrips_through_loadmaze():
    inner = "t=Gate Test&n=testuser01&d=" + VALID_GRID + "&s=1"
    status, body = post_save(inner)
    assert status == 200
    pairs = decode_r(body)
    assert pairs.get("saved") == "true"
    assert pairs.get("s") == "1"
    # read it back through the M1 endpoint: content must match exactly
    q = base64.b64encode(b"userName=testuser01&a=0.1&b=0.2").decode()
    with urllib.request.urlopen(BASE + "/includes/loadMaze.php?q=" + q) as r:
        back = decode_r(r.read().decode())
    assert back["d"] == VALID_GRID
    assert back["t"] == "Gate Test"
    assert back["n"] == "testuser01"
    assert back["s"] == "1"


@pytest.mark.live
@pytest.mark.parametrize("inner,code", [
    ("t=" + "x" * 33 + "&n=testuser01&d=" + VALID_GRID + "&s=1", "badTitle"),
    ("t=bad~title&n=testuser01&d=" + VALID_GRID + "&s=1", "badTitle"),
    ("t=ok&n=" + "a" * 17 + "&d=" + VALID_GRID + "&s=1", "badAuthor"),
    ("t=ok&n=testuser01&d=19#" + "1" * 19 + "#0#0##0#&s=1", "badGrid"),
    ("t=ok&n=testuser01&d=nonsense&s=1", "badGrid"),
    ("t=ok&n=testuser01&d=2#1111#0#11#" + "1#1#5##" * 11 + "#0#&s=1", "tooManyObjects"),
    ("t=ok&n=testuser01&d=" + VALID_GRID + "&s=0", "badSlot"),
])
def test_invalid_saves_report_error(inner, code):
    status, body = post_save(inner)
    assert status == 200
    assert decode_r(body).get("error") == code
