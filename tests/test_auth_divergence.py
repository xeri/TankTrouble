"""Auth divergence gate (guide 6.4): the login path must be POST-only,
verify bcrypt against synthetic users ONLY, and never behave like the
original GET scheme. Demonstrable, not just asserted in a header.

The synthetic secret is re-derived from seed_users.secrets() (fixed-seed
PRNG) — no plaintext secret is stored anywhere in the repo.
"""

import http.client
import sys
import urllib.parse

import pytest

from conftest import REPO, STACK_HOST, STACK_PORT

sys.path.insert(0, str(REPO / "seed"))
import seed_users  # noqa: E402

pytestmark = pytest.mark.live

ENDPOINT = "/includes/getUserAuthentication.php"


def _request(method, params=None):
    conn = http.client.HTTPConnection(STACK_HOST, STACK_PORT, timeout=30)
    try:
        body = urllib.parse.urlencode(params) if params else None
        headers = ({"Content-Type": "application/x-www-form-urlencoded"}
                   if body else {})
        conn.request(method, ENDPOINT, body, headers)
        resp = conn.getresponse()
        return resp.status, resp.read(), dict(resp.getheaders())
    finally:
        conn.close()


def _creds(i=0):
    secret, _salt = seed_users.secrets()[i]
    return seed_users.HASHES[i][0], secret


def test_get_is_refused(stack):
    """The original's GET auth leaked real credentials; the reconstruction
    must refuse the method outright."""
    status, body, headers = _request("GET")
    assert status == 405 and b"RECONSTRUCTION" in body
    assert headers.get("Allow") == "POST"


def test_wrong_password_denied(stack):
    user, _ = _creds()
    status, body, _ = _request("POST", {"username": user,
                                        "password": "not-the-secret"})
    assert status == 401 and body == b"denied"


def test_unknown_user_denied(stack):
    status, body, _ = _request("POST", {"username": "purup",
                                        "password": "anything"})
    assert status == 401 and body == b"denied"


def test_synthetic_user_logs_in(stack):
    user, secret = _creds()
    status, body, headers = _request("POST", {"username": user,
                                              "password": secret})
    assert status == 200 and body == b"ok"
    assert "PHPSESSID" in headers.get("Set-Cookie", ""), (
        "minimal session expected on success")


def test_missing_fields_rejected(stack):
    status, body, _ = _request("POST", {"username": "x"})
    assert status == 400 and b"RECONSTRUCTION" in body
