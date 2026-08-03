-- @provenance data M3 / schema M3
-- @evidence   none -- synthetic accounts; original user table never observable
-- @written    2026-08-03 by seed/seed_users.py
-- @caveat     Regenerate with `python seed/seed_users.py`; do not hand-edit.
-- @caveat     bcrypt via password_hash (guide 6.4 divergence); secrets derive from the fixed PRNG in seed_users.py, hashes pinned there.

SET NAMES utf8;
USE tanktrouble;

INSERT INTO users (username, password_hash) VALUES
('testuser01', '$2y$10$MzRjM2ViOTgzOGE3YTMyYORMgO.JtPGjD9QaaUAoz..zHzLNxPurS'),
('testuser02', '$2y$10$NDUzMGFmZjZlYmJkZTM3ZOSTGN.3iG3ZwOKKuUAILnT9eqcUwyFQ.'),
('testuser03', '$2y$10$NzNiYzA5ZjhhOTljYjk5ZOBSVFvm0Kj0E.aule/fqzznsldbHJWei'),
('testuser04', '$2y$10$MGY3MDM3MzI0OWY4MjIzYO0kgEBrfQJ5LpRqaGeXhL/XQerw9LPqm'),
('testuser05', '$2y$10$OTc1N2EyMTg3YmZiNDNmM.CNcxUM/EuPwOHrdnqPW0ZTBeBT2oB4m'),
('testuser06', '$2y$10$OGUzMGJjMTUzYjc5ODIwM.NN1R5TuSSUDesD/kQ8/DKAUzEc1hrEi'),
('testuser07', '$2y$10$N2IxOWY2YWViZDliNzY1NOP/jS64z93z0eMZiYKAz1/4hJUDIjNu6'),
('testuser08', '$2y$10$ZjFjMWY4YmYxNGM4Nzk1YOLV2QkLnwNOQHUU0SOlRwCay76h8z3RW'),
('testuser09', '$2y$10$YTMwZGE2NmNmNWJmZWFlZeiDNYHwx7N.9XXP5IvsBWw/fl9rxdyye'),
('testuser10', '$2y$10$ZjM1MmQzOTBiMjAyYTU4YOPcCf9yPztT4LJk8xxjhhyZx/K0Zxga.');
