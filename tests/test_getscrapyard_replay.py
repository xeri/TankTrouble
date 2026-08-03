"""getScrapyard.php replay + era getScraps shape (guide 7.2).

Replay: the only two archived request/response pairs (both PRE-ERA) must
reproduce byte-exactly once their state is injected into scrapyard_state.
State injection goes through `docker exec` into the mysql container (the
credentials never leave it) and the seed row is restored afterwards.

getScraps: the era pages call the SAJAX function instead; ZERO era bodies
are archived, so those checks are SHAPE-ONLY (deduced from the
srv/includes/scrapyard.js parse: sajax string result -> JSON.parse ->
scraps + optional velocity) and clearly labelled non-byte-gate.
"""

import http.client
import json
import re
import subprocess
import urllib.parse

import pytest

from conftest import REPO, STACK_HOST, STACK_PORT

pytestmark = pytest.mark.live

MYSQL_CONTAINER = "docker-mysql-1"
SEED_SQL = ("UPDATE scrapyard_state SET scraps=1785664230, "
            "velocity='0.0071382502652744' WHERE id=1")

# (query string, injection SQL, archived body, archive source)
REPLAYS = [
    ("scraps&velocity",
     "UPDATE scrapyard_state SET scraps=1662979870, "
     "velocity='0.0071382502652744' WHERE id=1",
     b"scraps=1662979870&velocity=0.0071382502652744",
     "archive/includes-tree/20150928_getScrapyard.php"),
    ("scraps",
     "UPDATE scrapyard_state SET scraps=1785664230, velocity=NULL WHERE id=1",
     b"scraps=1785664230",
     "archive/includes-tree/20160126_getScrapyard.php"),
]


def _mysql(sql):
    cp = subprocess.run(
        ["docker", "exec", MYSQL_CONTAINER, "sh", "-c",
         'exec mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" tanktrouble '
         "-e '%s'" % sql],
        capture_output=True, text=True, timeout=60)
    assert cp.returncode == 0, "mysql exec failed: %s" % cp.stderr[-300:]


def _get(path):
    conn = http.client.HTTPConnection(STACK_HOST, STACK_PORT, timeout=30)
    try:
        conn.request("GET", path)
        resp = conn.getresponse()
        return resp.status, resp.read()
    finally:
        conn.close()


def _post(path, params):
    conn = http.client.HTTPConnection(STACK_HOST, STACK_PORT, timeout=30)
    try:
        body = urllib.parse.urlencode(params)
        conn.request("POST", path, body,
                     {"Content-Type": "application/x-www-form-urlencoded"})
        resp = conn.getresponse()
        return resp.status, resp.read()
    finally:
        conn.close()


def test_archived_bodies_replay_byte_exact(stack, archive_root):
    try:
        for qs, inject, body, source in REPLAYS:
            src = archive_root / source.replace("archive/", "", 1)
            assert src.read_bytes() == body, (
                "archived body drifted from the constant this test locks: %s"
                % source)
            _mysql(inject)
            status, got = _get("/includes/getScrapyard.php?" + qs)
            assert status == 200
            assert got == body, (
                "replay of ?%s not byte-identical:\n  want %r\n  got  %r"
                % (qs, body, got[:100]))
    finally:
        _mysql(SEED_SQL)


def test_unarchived_inputs_rejected(stack):
    for qs in ["", "?velocity", "?velocity&scraps", "?scraps&x", "?foo"]:
        status, body = _get("/includes/getScrapyard.php" + qs)
        assert status == 400 and b"RECONSTRUCTION" in body, (
            "expected loud 400 for %r, got %d %r" % (qs, status, body[:100]))


def _sajax_string_result(body):
    """'+:var res = '<js-escaped string>'; res;' -> the decoded string."""
    m = re.match(rb"\+:var res = '(.*)'; res;\Z", body, re.S)
    assert m, "not a sajax string success frame: %r" % body[:120]
    s = m.group(1).decode("ascii")
    return (s.replace("\\\\", "\x00").replace("\\'", "'")
            .replace('\\"', '"').replace("\\r", "\r").replace("\\n", "\n")
            .replace("\x00", "\\"))


def test_getscraps_shape_with_velocity(stack):
    """NON-BYTE-GATE (deduced shape): x_getScraps(true, cb) path."""
    status, body = _post("/", {"rs": "getScraps", "rsargs[]": "true"})
    assert status == 200
    obj = json.loads(_sajax_string_result(body))
    assert set(obj) == {"scraps", "velocity"} and isinstance(obj["scraps"], int)


def test_getscraps_shape_without_velocity(stack):
    status, body = _post("/", {"rs": "getScraps", "rsargs[]": "undefined"})
    assert status == 200
    obj = json.loads(_sajax_string_result(body))
    assert set(obj) == {"scraps"}


def test_unreconstructed_sajax_functions_stay_native_errors(stack):
    for func in ["login", "vote", "showForumPreviews"]:
        status, body = _post("/", {"rs": func})
        assert status == 200 and body == b"-:%s not callable" % func.encode()
