<?php
/* @provenance M2
 * @evidence   two archived request/response pairs: ?scraps ->
 *             "scraps=1785664230" (2016-01-26), ?scraps&velocity ->
 *             "scraps=1662979870&velocity=0.0071382502652744" (2015-09-28);
 *             bodies at archive/includes-tree/20150928_getScrapyard.php and
 *             20160126_getScrapyard.php. The requested query keys select
 *             the emitted fields.
 * @verified   tests/test_getscrapyard_replay.py (both archived bodies
 *             replay byte-exact with their state injected)
 * @written    2026-08-03
 * @caveat     Both observations are PRE-ERA (the era scrapyard moved to the
 *             SAJAX getScraps call in index.php, deploy 2017-02-21); this
 *             file's era behaviour is unarchived. Tier stays M2.
 * @caveat     Exactly the two archived query strings are accepted; original
 *             behaviour on any other input is unarchived and NOT guessed.
 * @caveat     velocity's storage/derivation is unobservable; the state row
 *             keeps the archived decimal string and emits it verbatim.
 */
require_once dirname(__FILE__) . '/rebuild-db.php';

function tt_scrapyard_fail($why)
{
    header('HTTP/1.1 400 Bad Request');
    header('Content-Type: text/plain');
    die('RECONSTRUCTION: ' . $why
        . ' The archive evidences exactly ?scraps and ?scraps&velocity;'
        . ' original behaviour on other inputs is unknown.');
}

$tt_qs = isset($_SERVER['QUERY_STRING']) ? $_SERVER['QUERY_STRING'] : '';
if ($tt_qs !== 'scraps' && $tt_qs !== 'scraps&velocity') {
    tt_scrapyard_fail('unsupported query string.');
}

$tt_res = mysql_query('SELECT scraps, velocity FROM scrapyard_state WHERE id = 1');
$tt_row = $tt_res ? mysql_fetch_assoc($tt_res) : null;
if (!$tt_row) {
    header('HTTP/1.1 500 Internal Server Error');
    die('RECONSTRUCTION: scrapyard_state row missing - reseed the stack');
}

$tt_out = 'scraps=' . (int) $tt_row['scraps'];
if ($tt_qs === 'scraps&velocity') {
    if ($tt_row['velocity'] === null || $tt_row['velocity'] === '') {
        header('HTTP/1.1 500 Internal Server Error');
        die('RECONSTRUCTION: velocity requested but state holds none');
    }
    $tt_out .= '&velocity=' . $tt_row['velocity'];
}
echo $tt_out;
