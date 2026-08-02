<?php
/* @provenance M3
 * @evidence   5 client call sites in decompiled AS2; behaviour unknown
 * @verified   none
 * @written    2026-08-02
 * @caveat     Milestone-1 skeleton stub. Behaviour not reconstructed. Must
 *             never return 200 or plausible data.
 *             DELIBERATE DIVERGENCE. The original used SAJAX over GET, which
 *             is why real credentials are still in the public Wayback CDX
 *             index. This file does NOT reconstruct that. POST + TLS +
 *             password_hash.
 */
header('HTTP/1.1 501 Not Implemented');
die("STUB includes/getUserAuthentication.php [M3] - behaviour not yet reconstructed\n");
