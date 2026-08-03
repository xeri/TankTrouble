<?php
/* @provenance M1
 * @evidence   17,411 CDX rows (17,378 decodable ?q= requests in
 *             archive/cdx-passes/F_loadmaze200.json); 843 decoded response
 *             bodies in archive/maze-corpus/raw/; reader source
 *             archive/decompiled/CLASSIC_TankTrouble_v4.0/scripts/
 *             __Packages/MazeDataFetcher.as + MazeDataLoader.as;
 *             shuffleMessage/decodeMessage in scripts/frame_1/DoAction.as
 * @verified   tests/test_loadmaze_replay.py - gate B: notFound byte-exact
 *             vs the archived body, outer format exact, full 672-state
 *             content replay over HTTP (DECISIONS 2026-08-03)
 * @written    2026-08-03
 * @caveat     Response pair ORDER was a per-request shuffle in the ORIGINAL
 *             (all 24 permutations of t/n/d/s occur across the 842 archived
 *             bodies), so byte-identical replay is impossible by
 *             construction; gate B compares canonical field content. The
 *             shuffle below mirrors the CLIENT's naive swap-shuffle
 *             (shared-codebase presumption) - the server's actual algorithm
 *             is unverifiable from output.
 * @caveat     Unknown or malformed input is REJECTED loudly (HTTP 400); the
 *             original's behaviour on bad input was never observed. Response
 *             headers were never archived; PHP defaults apply. Random-maze
 *             selection uses ORDER BY RAND(); the original's mechanism is
 *             unobservable. userName matching is byte-exact (VARBINARY
 *             author, DECISIONS 2026-08-03); the original's case/space
 *             handling is unknown. 13 CDX rows (2018-06-03/04, digest
 *             G7SVMWKCBAA3, body never archived) returned a stable
 *             non-shuffled body this reconstruction does not reproduce.
 */

// WIRE FORMAT - observed; CORRECTS guide 6.2, which shows `r=<b64>&s=<slot>`:
//   GET includes/loadMaze.php?q=<base64( shuffle("userName=<name>&a=<r>&b=<r>") )>
//                       or ...?q=<base64( shuffle("c=<r>&a=<r>&b=<r>") )>
//     a/b/c are client Math.random() cache-busters, read and discarded
//   200 -> r=<base64( shuffle("t=<title>&n=<author>&d=<grid>&s=<slot>") )>
//     `s` sits INSIDE the base64 (842/842 corpus bodies; observed only 1)
//   no maze for the query -> r=<base64("notFound=true")>  (single pair)
//   d (grid) is emitted verbatim from the seeded payload - never re-derived

require_once __DIR__ . '/rebuild-db.php';

// q comes from QUERY_STRING + rawurldecode: archived requests are raw
// base64 or %3D-padded, never '+' - but $_GET would silently turn a base64
// '+' into a space, so the raw query string is the safe source
function tt_query_param_q()
{
    $qs = isset($_SERVER['QUERY_STRING']) ? $_SERVER['QUERY_STRING'] : '';
    foreach (explode('&', $qs) as $part) {
        if (substr($part, 0, 2) === 'q=') {
            return rawurldecode(substr($part, 2));
        }
    }
    return null;
}

function tt_fail_400($why)
{
    header('HTTP/1.1 400 Bad Request');
    die('RECONSTRUCTION: ' . $why
        . " - original behaviour on bad input unknown (see @caveat)\n");
}

// naive swap-shuffle ported from the client's shuffleMessage()
// (frame_1/DoAction.as); deliberately NOT Fisher-Yates
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

$q = tt_query_param_q();
if ($q === null || $q === '') {
    tt_fail_400('missing q parameter');
}
$decoded = base64_decode($q);   // lenient, like the client's Base64.Decode
if ($decoded === false || $decoded === '') {
    tt_fail_400('q does not decode as base64');
}

$params = array();
foreach (explode('&', $decoded) as $pair) {
    $kv = explode('=', $pair, 2);
    if (count($kv) !== 2) {
        tt_fail_400('malformed pair in q');
    }
    $params[$kv[0]] = $kv[1];   // duplicate keys: last wins, like the client
}

$keys = array_keys($params);
sort($keys);
if ($keys === array('a', 'b', 'userName')) {
    $sql = "SELECT title, author, data, slot FROM mazes WHERE author = '"
         . tt_db_escape($params['userName'])
         . "' ORDER BY RAND() LIMIT 1";
} elseif ($keys === array('a', 'b', 'c')) {
    $sql = 'SELECT title, author, data, slot FROM mazes ORDER BY RAND() LIMIT 1';
} else {
    tt_fail_400('unexpected key set {' . implode(',', $keys) . '}');
}

$res = mysql_query($sql);
if ($res === false) {
    header('HTTP/1.1 500 Internal Server Error');
    die("RECONSTRUCTION: query failed\n");
}
$row = mysql_fetch_assoc($res);
if (!$row) {
    $inner = 'notFound=true';
} else {
    $inner = tt_shuffle_message(
        't=' . $row['title'] . '&n=' . $row['author']
        . '&d=' . $row['data'] . '&s=' . $row['slot']);
}
echo 'r=' . base64_encode($inner);
