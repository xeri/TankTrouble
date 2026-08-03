"""De-render generator (guide 6.1a): emit srv/index.php from era-final
reference captures + gate-F masks.

Strategy (DECISIONS 2026-08-03): each route's page is its era-final capture
emitted VERBATIM inside @O fences — zero invented markup — split only where
behaviour is reconstructed:

  * echo:$initCode regions  -> tt_init_code_line(): random k=<int> pair,
    naive swap-shuffle (mirrors the loadMaze port), base64 — the only
    mechanism consistent with the two observed permutations k=X& / &k=X.
  * per-request:random-tagline regions -> tt_tagline_line(): uniform pick
    from the pool observed across all era captures of root+game.

Every other dynamic region (live-player-stats, top10-rankings,
latest-posters, seasonal-promo, news items, template edits) is FROZEN at
its era-final bytes inside the fences; gate F masks or gates them
accordingly. SAJAX: version pinned 0.12 (in-page common JS byte-matches
stock modulo 4 site-inserted debug lines + uri="/"); the dispatcher
functions are stock 0.12 verbatim (thirdparty/sajax/Sajax-0.12-stock.php);
the export list is empty until an endpoint is reconstructed, so every rs=
call answers the sajax-native "-:<func> not callable".

Deterministic: same archive + masks -> byte-identical index.php.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import classify_regions as cls
import annotate_regions as ann

REPO = cls.REPO
OUT_PHP = os.path.join(REPO, "srv", "index.php")

ROUTE_ORDER = ["root", "game", "garage", "news", "forum", "lab", "shop"]


def era_final(route):
    rows = cls.manifest_rows()
    caps = cls.era_captures(rows, route)
    return caps[-1]


def read_raw(source):
    p = os.path.join(REPO, source)
    with open(p, "rb") as f:
        return f.read()


def mask_regions(route):
    _, rows = ann.read_tsv(route)
    out = []
    for r in rows:
        lo, hi = r["ref_lines"].split("-")
        out.append((r["region_id"], int(lo), int(hi), r["status"],
                    r["annotation"]))
    return out


def emitter_for(cell):
    if cell.startswith("echo:$initCode"):
        return "initcode"
    if cell.startswith("per-request:random-tagline"):
        return "tagline"
    return None


def tagline_pool():
    """Union of tagline texts across every era capture of root+game."""
    pool = set()
    for route in ("root", "game"):
        caps, bodies, ref, survives = ann.route_context(route)
        ops_by_cap = [ann.opcodes(ref, b) for b in bodies]
        for rid, a, b, status in cls.region_runs(survives):
            if status != "dynamic":
                continue
            cell = dict((r[0], r[4]) for r in mask_regions(route))[rid]
            if emitter_for(cell) != "tagline":
                continue
            for body, ops in zip(bodies, ops_by_cap):
                for line in ann.project(ops, body, a, b):
                    assert line.startswith("\t\t") and \
                        line.endswith("\t</span>"), repr(line)
                    pool.add(line[2:-len("\t</span>")])
    return sorted(pool)


def php_sq(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"


def fence(source, a, b, lines_keepends):
    """Fenced verbatim chunk for source lines a..b (1-based inclusive).
    PHP eats exactly one newline after ?>, and the closing newline before
    <?php re-supplies the final line's LF — emitted bytes == source bytes."""
    body = b"".join(lines_keepends[a - 1:b])
    assert body.endswith(b"\n")
    body = body[:-1]
    head = "/* @O-begin source=%s lines=%d-%d */ ?>\n" % (source, a, b)
    return head.encode("ascii") + body + b"\n<?php /* @O-end */\n"


def route_function(route, contains):
    cap = era_final(route)
    source = cap["source"]
    raw = read_raw(source)
    lines = raw.splitlines(keepends=True)
    regions = mask_regions(route)
    n_lines = regions[-1][2]
    assert len(lines) == n_lines, (route, len(lines), n_lines)
    assert raw.endswith(b"\n"), route

    chunks = [("code", "function tt_page_%s() {\n" % route)]
    pos = 1
    for rid, lo, hi, status, cell in regions:
        em = emitter_for(cell) if status == "dynamic" else None
        if not em:
            continue
        assert hi == lo, (route, rid, "emitter regions must be single-line")
        if pos <= lo - 1:
            contains.append("%s lines=%d-%d" % (source, pos, lo - 1))
            chunks.append(("fence", (source, pos, lo - 1, lines)))
        chunks.append(("code", "\techo tt_%s_line();\n" %
                       ("init_code" if em == "initcode" else "tagline")))
        pos = hi + 1
    contains.append("%s lines=%d-%d" % (source, pos, n_lines))
    chunks.append(("fence", (source, pos, n_lines, lines)))
    chunks.append(("code", "}\n\n"))

    out = b""
    for kind, data in chunks:
        if kind == "code":
            out += data.encode("ascii")
        else:
            out += fence(*data)
    return out


def build():
    contains = []
    route_bodies = [route_function(r, contains) for r in ROUTE_ORDER]
    pool = tagline_pool()

    header = """<?php
/*
 * @provenance M1 (written reconstruction, promoted via gate F 2026-08-03;
 *   verbatim era-final capture bytes inside @O fences below -- file tier =
 *   authorship tier, DECISIONS 2026-08-02)
 * @written 2026-08-03 (generated by tools/derender.py -- regenerate, do not
 *   hand-edit fenced bytes)
 * @evidence era-final captures per route (archive-cleaned/MANIFEST.tsv);
 *   gate F offline half proves the masks hold against every era capture,
 *   live half proves this file renders the same gated bytes
 *   (tests/test_masks.py, tests/test_render_diff.py). SAJAX pinned 0.12:
 *   in-page common JS byte-matches thirdparty/sajax/Sajax-0.12-stock.php
 *   modulo 4 site-inserted sajax_debug lines and sajax_remote_uri="/";
 *   dispatcher functions below are stock 0.12 verbatim.
 * @caveat route resolution (exact QUERY_STRING match, unknown -> loud 400)
 *   is deduced from archived request URLs only; original behaviour on other
 *   inputs is unarchived and NOT guessed.
 * @caveat initCode mechanism (random k, naive swap-shuffle, base64) is
 *   deduced from the two observed permutations; RNG and range unobservable.
 * @caveat per-request regions are FROZEN at era-final bytes: live-player
 *   stats, top10 rankings, forum latest-posters, seasonal promo (originals
 *   were live values / date-derived). Gate F masks them; DECISIONS records
 *   the freeze.
 * @caveat every SAJAX function except getScraps answers "-:<func> not
 *   callable" (stock error form) until its endpoint is reconstructed; zero
 *   era SAJAX response bodies are archived.
 * @caveat getScraps response SHAPE is deduced from the scrapyard.js parse
 *   (JSON string with scraps and optional velocity); its VALUES come from
 *   the M3 scrapyard_state table seeded with the archived 2015/2016
 *   getScrapyard.php bodies -- labelled arbitrary, no era body archived.
 * @contains
%s
 */

/* ---- Sajax 0.12 dispatcher, stock verbatim ----------------------------
 * source: thirdparty/sajax/Sajax-0.12-stock.php (sajax_esc lines 297-303,
 * sajax_get_js_repr lines 38-76, sajax_handle_client_request lines 78-123).
 * Export list holds only reconstructed endpoints (guide 6.2 rule 3:
 * reject, never fake).
 * -------------------------------------------------------------------- */

$GLOBALS['sajax_export_list'] = array('getScraps');

function sajax_esc($val)
{
	$val = str_replace("\\\\", "\\\\\\\\", $val);
	$val = str_replace("\\r", "\\\\r", $val);
	$val = str_replace("\\n", "\\\\n", $val);
	$val = str_replace("'", "\\\\'", $val);
	return str_replace('"', '\\\\"', $val);
}

function sajax_get_js_repr($value) {
	$type = gettype($value);

	if ($type == "boolean") {
		return ($value) ? "Boolean(true)" : "Boolean(false)";
	}
	elseif ($type == "integer") {
		return "parseInt($value)";
	}
	elseif ($type == "double") {
		return "parseFloat($value)";
	}
	elseif ($type == "array" || $type == "object" ) {
		$s = "{ ";
		if ($type == "object") {
			$value = get_object_vars($value);
		}
		foreach ($value as $k=>$v) {
			$esc_key = sajax_esc($k);
			if (is_numeric($k))
				$s .= "$k: " . sajax_get_js_repr($v) . ", ";
			else
				$s .= "\\"$esc_key\\": " . sajax_get_js_repr($v) . ", ";
		}
		if (count($value))
			$s = substr($s, 0, -2);
		return $s . " }";
	}
	else {
		$esc_val = sajax_esc($value);
		$s = "'$esc_val'";
		return $s;
	}
}

function sajax_handle_client_request() {
	global $sajax_export_list;

	$mode = "";

	if (! empty($_GET["rs"]))
		$mode = "get";

	if (!empty($_POST["rs"]))
		$mode = "post";

	if (empty($mode))
		return;

	if ($mode == "get") {
		// Bust cache in the head
		header ("Expires: Mon, 26 Jul 1997 05:00:00 GMT");    // Date in the past
		header ("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT");
		// always modified
		header ("Cache-Control: no-cache, must-revalidate");  // HTTP/1.1
		header ("Pragma: no-cache");                          // HTTP/1.0
		$func_name = $_GET["rs"];
		if (! empty($_GET["rsargs"]))
			$args = $_GET["rsargs"];
		else
			$args = array();
	}
	else {
		$func_name = $_POST["rs"];
		if (! empty($_POST["rsargs"]))
			$args = $_POST["rsargs"];
		else
			$args = array();
	}

	if (! in_array($func_name, $sajax_export_list))
		echo "-:$func_name not callable";
	else {
		echo "+:";
		$result = call_user_func_array($func_name, $args);
		echo "var res = " . trim(sajax_get_js_repr($result)) . "; res;";
	}
	exit;
}

/* ---- reconstructed behaviour ---------------------------------------- */

/* Mirror of the client shuffleMessage port in includes/loadMaze.php --
 * deliberately the same naive biased swap, NOT Fisher-Yates. */
function tt_shuffle_message($m)
{
	$pairs = explode('&', $m);
	$n = count($pairs);
	for ($i = 0; $i < $n; $i++) {
		$j = mt_rand(0, $n - 1);
		$tmp = $pairs[$i];
		$pairs[$i] = $pairs[$j];
		$pairs[$j] = $tmp;
	}
	return implode('&', $pairs);
}

function tt_init_code_line()
{
	$inner = tt_shuffle_message('k=' . mt_rand(0, 2147483647) . '&');
	return "tt.addParam('FlashVars','initCode=" . base64_encode($inner)
		. "');\\ttt.write(\\"TankTrouble\\");\\n";
}

function tt_tagline_line()
{
	$pool = array(
%s
	);
	return "\\t\\t" . $pool[mt_rand(0, count($pool) - 1)] . "\\t</span>\\n";
}

/* Era scrapyard endpoint: pages call x_getScraps(includeVelocity, cb); the
 * callback JSON.parses the returned STRING (srv/includes/scrapyard.js,
 * O 2017-02-21). State lives in the M3 scrapyard_state table. */
function getScraps($includeVelocity = '')
{
	require_once dirname(__FILE__) . '/includes/rebuild-db.php';
	$res = mysql_query("SELECT scraps, velocity FROM scrapyard_state WHERE id = 1");
	$row = $res ? mysql_fetch_assoc($res) : null;
	if (!$row) {
		header('HTTP/1.1 500 Internal Server Error');
		die('RECONSTRUCTION: scrapyard_state row missing - reseed the stack');
	}
	$json = '{"scraps":' . (int) $row['scraps'];
	if ($includeVelocity === 'true'
			&& $row['velocity'] !== null && $row['velocity'] !== '') {
		$json .= ',"velocity":' . $row['velocity'];
	}
	return $json . '}';
}

"""

    main_block = """
/* ---- front controller ------------------------------------------------ */

sajax_handle_client_request();

$tt_routes = array(
	'' => 'tt_page_root',
	'game' => 'tt_page_game',
	'garage' => 'tt_page_garage',
	'news' => 'tt_page_news',
	'forum' => 'tt_page_forum',
	'lab' => 'tt_page_lab',
	'shop' => 'tt_page_shop',
);

$tt_qs = isset($_SERVER['QUERY_STRING']) ? $_SERVER['QUERY_STRING'] : '';
if (!array_key_exists($tt_qs, $tt_routes)) {
	header('HTTP/1.1 400 Bad Request');
	header('Content-Type: text/plain');
	die("RECONSTRUCTION: unknown query string. The era archive evidences "
		. "exactly ?game ?garage ?news ?forum ?lab ?shop and the bare root; "
		. "original behaviour on other inputs is unarchived and not guessed.");
}
call_user_func($tt_routes[$tt_qs]);
"""

    contains_txt = "\n".join(" *   %s" % c for c in contains)
    pool_txt = "\n".join("\t\t%s," % php_sq(t) for t in pool)
    out = header % (contains_txt, pool_txt)
    out = out.encode("ascii")
    for body in route_bodies:
        out += body
    out += main_block.encode("ascii")
    with open(OUT_PHP, "wb") as f:
        f.write(out)
    print("wrote %s (%d bytes, %d fences, %d taglines)" % (
        OUT_PHP, len(out), len(contains), len(pool)))


def build_embed():
    """srv/embed.php: the era-final embed capture verbatim, one fence. All
    five dynamic regions are template-edit:20170124 (deploy-time constants,
    incl. the page's own constant initCode numUsers=0), so the render side
    is fully gated -- the whole page must byte-match the reference."""
    cap = era_final("embed")
    source = cap["source"]
    raw = read_raw(source)
    lines = raw.splitlines(keepends=True)
    assert raw.endswith(b"\n")
    contains = ["%s lines=1-%d" % (source, len(lines))]
    header = """<?php
/*
 * @provenance M1 (written wrapper, promoted via gate F 2026-08-03; the
 *   whole page is the era-final capture verbatim in one @O fence -- all
 *   five dynamic regions are template-edit:20170124 deploy-time constants,
 *   incl. the page's own constant initCode, so gate F gates every line)
 * @written 2026-08-03 (generated by tools/derender.py)
 * @evidence 9 era captures byte-stable since 20170124 (offline gate,
 *   tests/test_masks.py); render diffed against the era-final reference
 *   (tests/test_render_diff.py)
 * @contains
%s
 */
""" % "\n".join(" *   %s" % c for c in contains)
    out = header.encode("ascii") + fence(source, 1, len(lines), lines)
    path = os.path.join(REPO, "srv", "embed.php")
    with open(path, "wb") as f:
        f.write(out)
    print("wrote %s (%d bytes)" % (path, len(out)))


if __name__ == "__main__":
    build()
    build_embed()
