<?php
/* @provenance M3
 * @caveat     DELIBERATE DIVERGENCE. The original used SAJAX over GET, which is
 *             why real credentials are still in the public Wayback CDX index.
 *             This file does NOT reconstruct that. POST + TLS + password_hash.
 * @evidence   5 client call sites in decompiled AS2; original behaviour unknown
 * @verified   tests/test_auth_divergence.py
 * @written    2026-08-03
 * @caveat     Response format is invention (no original response was ever
 *             archived): POST username+password -> 200 "ok" with a minimal
 *             PHP session on success, 401 "denied" on failure, 405 for any
 *             other method, 400 for missing fields. Verifies ONLY the
 *             synthetic testuser accounts (guide 5.1). Logged-in page
 *             rendering is NOT reconstructed (near-zero logged-in captures,
 *             DECISIONS 2026-08-03) - the session is set and nothing in
 *             milestone 3 consumes it.
 * @caveat     TLS termination is out of scope for the localhost-only stack
 *             (binds 127.0.0.1, never internet-facing - SECURITY.md).
 */
require_once dirname(__FILE__) . '/rebuild-db.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('HTTP/1.1 405 Method Not Allowed');
    header('Allow: POST');
    header('Content-Type: text/plain');
    die('RECONSTRUCTION: auth is POST-only by design (guide 6.4). The '
        . "original's GET auth is why real credentials sit in the public "
        . 'CDX; it is deliberately not reconstructed.');
}

$tt_user = isset($_POST['username']) ? $_POST['username'] : '';
$tt_pass = isset($_POST['password']) ? $_POST['password'] : '';
if ($tt_user === '' || $tt_pass === '') {
    header('HTTP/1.1 400 Bad Request');
    die('RECONSTRUCTION: username and password fields are required');
}

$tt_res = mysql_query("SELECT password_hash FROM users WHERE username = '"
    . tt_db_escape($tt_user) . "'");
$tt_row = $tt_res ? mysql_fetch_assoc($tt_res) : null;
if (!$tt_row || !password_verify($tt_pass, $tt_row['password_hash'])) {
    header('HTTP/1.1 401 Unauthorized');
    die('denied');
}

session_start();
$_SESSION['tt_user'] = $tt_user;
die('ok');
