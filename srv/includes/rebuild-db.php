<?php
/* @provenance M3
 * @evidence   none - both the NAME and the contents of the original's
 *             shared DB include were never observable. DO NOT PROMOTE.
 * @verified   tests/test_loadmaze_replay.py (transitively: every gate-B
 *             response flows through this connection)
 * @written    2026-08-03
 * @caveat     DELIBERATELY MODERN NAME (guide 10.4, DECISIONS 2026-08-03):
 *             the hyphen and the word "rebuild" announce the invention.
 *             Credentials come from the TT_DB_* container environment,
 *             never from code (DECISIONS 2026-08-03). mysql_* API kept for
 *             period fidelity inside the never-exposed container (guide
 *             6.3); every query input must pass tt_db_escape().
 */

$tt_db = mysql_connect(getenv('TT_DB_HOST'), getenv('TT_DB_USER'),
                       getenv('TT_DB_PASSWORD'));
if ($tt_db === false) {
    header('HTTP/1.1 500 Internal Server Error');
    die("RECONSTRUCTION: DB connection failed - is the mysql container up?\n");
}
if (!mysql_select_db(getenv('TT_DB_NAME'), $tt_db)) {
    header('HTTP/1.1 500 Internal Server Error');
    die("RECONSTRUCTION: cannot select database\n");
}
mysql_set_charset('utf8', $tt_db);

function tt_db_escape($s)
{
    return mysql_real_escape_string($s);
}

/* Guide 3.3's own worked example: the maze-save endpoint NAME is pure
 * invention (M3) - the editor SWF that called it is lost (mazeCreator,
 * guide 6.5) and no request for it was ever archived. The constant lives
 * here so every invented name stays findable in one place;
 * srv/includes/saveMaze.php is a `pending` ledger row with NO file until
 * the mazeCreator milestone reconstructs the caller. */
define('TT_SAVE_MAZE_ENDPOINT', 'saveMaze.php');
