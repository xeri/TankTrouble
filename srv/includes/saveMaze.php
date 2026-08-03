<?php
/* @provenance M3
 * @evidence   NONE for the name, method, or wire format - ALL INVENTED.
 *             Deduction chain (DEDUCE.md 3.3): no maze SAJAX function among
 *             the 36 -> the page did not save; recovered JS sets
 *             _root.errorPanel.hide -> the SWF saw the response -> the SWF
 *             posted to a URL that lived only inside the lost
 *             mazeCreator_v0.3.swf. Every fetch channel exhausted.
 * @verified   tests/test_savemaze.py (pins the INVENTED contract only)
 * @written    2026-08-03
 * @caveat     DO NOT PROMOTE. Wire format mirrors loadMaze.php conventions
 *             (q=/r= base64 pair messages, naive swap-shuffle) as the least
 *             inventive choice; the original format is unknowable without
 *             the lost SWF. Validation limits are the corpus-measured
 *             editor constraints (guide 6.5): grid <= 18x10, title <= 32
 *             legal chars, author <= 16, <= 5 tank + <= 5 crate spawns,
 *             <= 10 objects. POST-only is a rebuild-era choice.
 */

require_once dirname(__FILE__) . '/rebuild-db.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('HTTP/1.1 405 Method Not Allowed');
    header('Allow: POST');
    die("RECONSTRUCTION: saveMaze.php accepts POST only (M3 - see header)\n");
}

// mirror loadMaze.php: shuffle pair order, base64, r= envelope
function tt_save_reply($pairs)
{
    $n = count($pairs);
    for ($i = 0; $i < $n; $i++) {
        $j = mt_rand(0, $n - 1);
        $tmp = $pairs[$i]; $pairs[$i] = $pairs[$j]; $pairs[$j] = $tmp;
    }
    echo 'r=' . base64_encode(implode('&', $pairs));
    exit;
}

function tt_save_error($code)
{
    echo 'r=' . base64_encode('error=' . $code);
    exit;
}

$q = isset($_POST['q']) ? $_POST['q'] : null;
if ($q === null || $q === '') {
    tt_save_error('badGrid');
}
$decoded = base64_decode(str_replace(' ', '+', $q), true);
if ($decoded === false) {
    tt_save_error('badGrid');
}

$fields = array();
foreach (explode('&', $decoded) as $pair) {
    $kv = explode('=', $pair, 2);
    $fields[$kv[0]] = isset($kv[1]) ? $kv[1] : '';
}

$title  = isset($fields['t']) ? $fields['t'] : '';
$author = isset($fields['n']) ? $fields['n'] : '';
$grid   = isset($fields['d']) ? $fields['d'] : '';
$slot   = isset($fields['s']) ? $fields['s'] : '';

// title: <= 32 chars over the editor's legal set (mazeTitleLegalCharacters,
// srv/index.php - O evidence for the CHARSET)
if ($title === '' || strlen($title) > 32
        || !preg_match('/^[0-9A-Za-z !,\\-.?]+$/', $title)) {
    tt_save_error('badTitle');
}
// author: <= 16 bytes (schema VARBINARY(16); corpus max 16)
if ($author === '' || strlen($author) > 16) {
    tt_save_error('badAuthor');
}
// slot: positive small int (corpus observed only 1; schema TINYINT UNSIGNED)
if (!preg_match('/^[1-9][0-9]?$/', $slot)) {
    tt_save_error('badSlot');
}

// grid: same field walk as the O reader (MazeDataFetcher.as)
$f = explode('#', $grid);
if (count($f) < 6) { tt_save_error('badGrid'); }
$w = (int) $f[0];
$cells = $f[1];
if ($w < 1 || $w > 18 || $cells === '' || strlen($cells) % $w !== 0) {
    tt_save_error('badGrid');
}
$h = strlen($cells) / $w;
if ($h < 1 || $h > 10 || !preg_match('/^[0-7]+$/', $cells)) {
    tt_save_error('badGrid');
}
$objCount = (int) $f[3];
if ($objCount > 10) { tt_save_error('tooManyObjects'); }
$idx = 4;
$tanks = 0; $crates = 0;
for ($i = 0; $i < $objCount; $i++) {
    if (!isset($f[$idx + 3])) { tt_save_error('badGrid'); }
    $ox = (int) $f[$idx]; $oy = (int) $f[$idx + 1]; $type = (int) $f[$idx + 2];
    if ($ox < 1 || $ox > $w || $oy < 1 || $oy > $h) { tt_save_error('badGrid'); }
    if ($type === 5) { $tanks++; }
    elseif ($type === 8) { $crates++; }
    else { tt_save_error('badGrid'); }
    $idx += 4;
}
if ($tanks > 5 || $crates > 5) { tt_save_error('tooManyObjects'); }

$sql = sprintf(
    "INSERT INTO mazes (author, slot, title, data) VALUES ('%s', %d, '%s', '%s')"
    . " ON DUPLICATE KEY UPDATE title = VALUES(title), data = VALUES(data)",
    tt_db_escape($author),
    (int) $slot,
    tt_db_escape($title),
    tt_db_escape($grid)
);
if (!mysql_query($sql)) {
    header('HTTP/1.1 500 Internal Server Error');
    die("RECONSTRUCTION: maze insert failed\n");
}

tt_save_reply(array('saved=true', 's=' . (int) $slot));
