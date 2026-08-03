"""Gate B — loadMaze.php replay against the archived corpus (guide §7.2,
redesigned per DECISIONS 2026-08-03).

Byte-identical replay of the archived bodies is impossible by construction:
the ORIGINAL shuffled response pair order per-request (all 24 permutations
of t/n/d/s occur across the corpus) and 842/843 archived responses answered
anonymous c=<random> requests, i.e. random maze selection. This gate holds
everything that IS invariant:

  * the notFound body, byte-for-byte, for userName-of-unknown-author replays
  * the outer `r=<base64>` format, byte-for-byte in shape
  * decoded content: EVERY sampled response must equal one of the 672 seeded
    (author, slot) states, and sampling must reach ALL 672 (coupon
    collector, expected ≈4.8k requests, hard cap 25k, P(miss) < 1e-12)
"""

import base64
import glob
import random
import re

import pytest

from conftest import STACK_HOST, STACK_PORT
import http.client

pytestmark = pytest.mark.live

NOTFOUND_BODY = b"r=bm90Rm91bmQ9dHJ1ZQ=="   # base64("notFound=true"), archived
ENDPOINT = "/includes/loadMaze.php"
OUTER_RE = re.compile(rb"\Ar=[A-Za-z0-9+/]+={0,2}\Z")
HARD_CAP = 25000

_rng = random.Random(0x7A6B)   # deterministic test inputs


def _corpus_winners(archive_root):
    """(author, slot) -> canonical content, latest capture wins — the same
    rule seed_mazes.py uses, recomputed independently from the raw corpus."""
    winners = {}
    for path in sorted(glob.glob(str(archive_root / "maze-corpus" / "raw" / "*.txt"))):
        name = path.replace("\\", "/").rsplit("/", 1)[-1]
        fetchts = name.split("_")[0]
        body = open(path, encoding="ascii").read().strip()
        inner = base64.b64decode(body[2:]).decode("utf-8")
        if inner == "notFound=true":
            continue
        fields = dict(p.split("=", 1) for p in inner.split("&"))
        key = (fields["n"], fields["s"])
        if key not in winners or fetchts > winners[key][0]:
            winners[key] = (fetchts, tuple(sorted(inner.split("&"))))
    return {k: v[1] for k, v in winners.items()}


@pytest.fixture(scope="module")
def winners(archive_root):
    w = _corpus_winners(archive_root)
    assert len(w) == 672, "corpus changed — re-audit the latest-wins model"
    return w


@pytest.fixture()
def conn(stack):
    c = http.client.HTTPConnection(STACK_HOST, STACK_PORT, timeout=30)
    yield c
    c.close()


def _q(inner):
    return base64.b64encode(inner.encode("utf-8")).decode("ascii")


def _request_inner(pairs):
    pairs = list(pairs)
    _rng.shuffle(pairs)   # the client shuffled the request too
    return "&".join(pairs)


def _rand():
    return "0.%015d" % _rng.randrange(10 ** 15)


def _fetch(conn, inner):
    conn.request("GET", ENDPOINT + "?q=" + _q(inner))
    resp = conn.getresponse()
    return resp.status, resp.read()


def _decode_body(body):
    assert OUTER_RE.match(body), "outer format violated: %r" % body[:80]
    inner = base64.b64decode(body[2:]).decode("utf-8")
    return tuple(sorted(inner.split("&")))


def test_notfound_byte_identical(conn):
    """The one archived body with no random parts must replay byte-exactly.
    userName="undefined" is what the client actually sent in 12,901 archived
    requests (F_loadmaze200.json)."""
    for _ in range(20):
        inner = _request_inner(["userName=undefined",
                                "a=" + _rand(), "b=" + _rand()])
        status, body = _fetch(conn, inner)
        assert status == 200, "expected 200, got %d: %r" % (status, body[:200])
        assert body == NOTFOUND_BODY, (
            "notFound body not byte-identical: %r" % body[:80])


def test_outer_format(conn):
    """r=<base64>, single line, canonical padding, nothing else."""
    for _ in range(50):
        inner = _request_inner(["c=" + _rand(), "a=" + _rand(), "b=" + _rand()])
        status, body = _fetch(conn, inner)
        assert status == 200
        assert OUTER_RE.match(body), "outer format violated: %r" % body[:80]
        payload = body[2:]
        assert base64.b64encode(base64.b64decode(payload)) == payload, (
            "base64 does not round-trip canonically: %r" % payload[:80])


def test_response_key_set(conn):
    """Every maze response carries exactly the observed fields t/n/d/s."""
    for _ in range(100):
        inner = _request_inner(["c=" + _rand(), "a=" + _rand(), "b=" + _rand()])
        _, body = _fetch(conn, inner)
        content = _decode_body(body)
        keys = sorted(p.split("=", 1)[0] for p in content)
        assert keys == ["d", "n", "s", "t"], "unexpected keys: %s" % keys


def test_c_coverage_and_membership(conn, winners):
    """Coupon collector over the c=<random> path: every response must be a
    seeded winner state, and every winner state must eventually be served."""
    want = set(winners.values())
    seen = set()
    n = 0
    while len(seen) < len(want) and n < HARD_CAP:
        inner = _request_inner(["c=" + _rand(), "a=" + _rand(), "b=" + _rand()])
        status, body = _fetch(conn, inner)
        assert status == 200
        content = _decode_body(body)
        assert content in want, (
            "response is not an archived winner state (stale DB? reseed with "
            "`docker compose down -v && up -d`): %r" % (content,))
        seen.add(content)
        n += 1
    missing = want - seen
    assert not missing, (
        "%d requests never surfaced %d states, e.g. %s" % (
            n, len(missing),
            sorted(w for w in list(missing)[:3])))


def test_deduced_username_lookup(conn, winners):
    """NON-GATE sanity check, clearly labelled: the userName->author lookup
    is DEDUCED from MazeDataFetcher.as (no archived response ever answered a
    real userName). Exercises byte-exact matching incl. a trailing-space and
    a case-pair author."""
    for author in ["b11", "b11 ", "Cheesed", "cheesed"]:
        expect = winners[(author, "1")]
        inner = _request_inner(["userName=" + author,
                                "a=" + _rand(), "b=" + _rand()])
        status, body = _fetch(conn, inner)
        assert status == 200
        assert _decode_body(body) == expect, (
            "userName=%r did not return that author's maze" % author)


def test_malformed_input_rejected_loudly(conn):
    """The reconstruction REJECTS what it cannot evidence (guide 6.2 rule 3):
    unknown key sets and undecodable q must be 400, never plausible data."""
    bad_inners = [
        "c=0.5&a=0.5",                       # missing b
        "userName=x&c=0.5&a=0.5&b=0.5",      # both key sets at once
        "x=1&a=0.5&b=0.5",                   # unknown key
    ]
    for inner in bad_inners:
        status, body = _fetch(conn, inner)
        assert status == 400 and b"RECONSTRUCTION" in body, (
            "expected loud 400 for %r, got %d %r" % (inner, status, body[:100]))
    conn.request("GET", ENDPOINT)            # no q at all
    resp = conn.getresponse()
    assert resp.status == 400 and b"RECONSTRUCTION" in resp.read()
