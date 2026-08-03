"""Gate F, live half — render byte-diff (guide 7.4a, GATE_F_SPEC).

The offline half (test_masks.py) proves the annotated masks hold against
every era capture. This half proves the RECONSTRUCTION renders the same
static bytes: fetch each active route from the docker stack and compare
against the era-final reference capture with render-side modes (template
edits gated, per-request/loop/ad regions masked, echo regexes enforced).
Transitivity closes the loop: ref==capture (offline) + ref==render (here)
=> render==capture on every gated line, per capture.

A route is ACTIVE iff the ledger row of its serving file names this test in
verified_by — the same ledger-driven mechanics gate D uses for 501 stubs.
Routes not yet claimed are not fetched (their PHP does not exist; gate D
keeps them loud 501s). A claimed route with a blocking mask FAILS before
any fetch. Era hosts vary (www/apex): the render is fetched once per
distinct host and must match the reference under all of them.

Routes with ZERO dynamic regions (infirmary) additionally byte-compare the
raw response body against the era-final capture file — the strongest
possible claim, no masking involved.
"""

import http.client

import pytest

import maskcheck
from conftest import REPO, STACK_HOST, STACK_PORT, parse_ledger

pytestmark = pytest.mark.live

THIS = "tests/test_render_diff.py"

# route -> (request path, serving file's ledger row)
ROUTES = {
    "root": ("/", "srv/index.php"),
    "game": ("/?game", "srv/index.php"),
    "garage": ("/?garage", "srv/index.php"),
    "news": ("/?news", "srv/index.php"),
    "forum": ("/?forum", "srv/index.php"),
    "lab": ("/?lab", "srv/index.php"),
    "shop": ("/?shop", "srv/index.php"),
    "embed": ("/embed.php", "srv/embed.php"),
    "infirmary": ("/infirmary/", "srv/infirmary/index.html"),
}


def active_routes():
    claimed = {r["path"] for r in parse_ledger() if r["verified_by"] == THIS}
    return [route for route, (_, serving) in ROUTES.items()
            if serving in claimed]


def pytest_generate_tests(metafunc):
    if "route" in metafunc.fixturenames:
        metafunc.parametrize("route", active_routes())


def test_gate_scope():
    """The bring-up route must stay active; an empty active set would make
    this file vacuously green (fail-not-skip philosophy)."""
    active = active_routes()
    assert "infirmary" in active, (
        "infirmary must remain gate F's bring-up route (ledger verified_by)")


def _fetch(host, path):
    conn = http.client.HTTPConnection(STACK_HOST, STACK_PORT, timeout=30)
    try:
        conn.putrequest("GET", path, skip_host=True)
        conn.putheader("Host", host)
        conn.endheaders()
        resp = conn.getresponse()
        return resp.status, resp.read()
    finally:
        conn.close()


def test_route_renders(route, stack, archive_root):
    path, serving = ROUTES[route]
    mask = maskcheck.load_mask(route)
    blocking = maskcheck.blocking_regions(mask)
    assert not blocking, (
        "%s: gate blocked by unannotated/needs-split regions %s "
        "(annotate in archive-cleaned/classification/%s.tsv first)"
        % (route, blocking, route))

    caps, bodies = maskcheck.era_route_bodies(archive_root, route)
    ref_cap, ref = caps[-1], bodies[-1]
    modes, regexes = maskcheck.line_modes(mask, side="render")
    zero_dynamic = all(status == "static" for _, _, _, status, _ in mask)

    for host in sorted({c["host"] for c in caps}):
        status, body = _fetch(host, path)
        assert status == 200, (
            "%s (Host: %s): expected 200, got %d — is the route "
            "implemented and its ledger row honest?" % (route, host, status))
        if zero_dynamic:
            src = archive_root / ref_cap["source"].replace("archive/", "", 1)
            assert body == src.read_bytes(), (
                "%s (Host: %s): zero-dynamic route must serve the era-final "
                "capture byte-identically (%s)" % (route, host,
                                                   ref_cap["source"]))
        render = body.decode("utf-8", errors="replace").splitlines()
        div = maskcheck.check_side(ref, render, modes, regexes,
                                   "%s render (Host: %s)" % (route, host))
        assert not div, (
            "render diverges from era-final reference "
            "(%d divergence(s)):\n" % len(div) + "\n".join(div[:12]))
