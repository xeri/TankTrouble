# Security posture

**This stack is intentionally obsolete and must never be internet-facing.**

* PHP 5.6 and MySQL 5.5 are period-correct for the site being reconstructed
  and are years past end-of-life. They are run for structural fidelity only.
* `docker/docker-compose.yml` binds `127.0.0.1` only and publishes no MySQL
  host port. Do not change either. DB credentials reach PHP only through the
  `TT_DB_*` container environment (`docker/.env`, never committed).
* Authentication is deliberately NOT reconstructed period-correct. The
  original ran SAJAX auth over GET, which is why real credentials are
  permanently in the public Wayback CDX index. This rebuild uses POST +
  `password_hash` (guide §6.4) — implemented in
  `srv/includes/getUserAuthentication.php`, demonstrated POST-only by
  `tests/test_auth_divergence.py` — and never reintroduces leaked
  credentials. TLS termination is out of scope for the localhost-only
  stack. Logged-in rendering is not reconstructed; nothing consumes the
  session.
* No real credentials anywhere in this repo. Seeded users are synthetic
  (`testuser01`…). Real usernames from the maze/forum corpora are display
  metadata only, never login accounts.
* CI greps the tree for credential-shaped strings before every push
  (`tests/test_no_unlabelled.py`).
