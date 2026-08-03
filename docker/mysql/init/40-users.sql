-- @provenance data M3 / schema M3
-- @evidence   none -- synthetic accounts; original user table never observable
-- @written    2026-08-03 by seed/seed_users.py
-- @caveat     Regenerate with `python seed/seed_users.py`; do not hand-edit.
-- @caveat     Hash format is a placeholder; milestone-3 auth (deliberate divergence, guide 6.4) owns the real decision.

SET NAMES utf8;
USE tanktrouble;

INSERT INTO users (username, password_sha256) VALUES
('testuser01', 'b11a293cc4b3b4b49809ce9b4fcc4d665d493eedb70c598777ec7e90fe6fcf6c'),
('testuser02', '28ac221db45b0b451d9d0a49c75a9a38b9225d67ac2902e109ccf892ff11a365'),
('testuser03', '4adfd7ca583bad4ec70342235545f71ea7608bdc60b5e6d88d9492322c3ee08d'),
('testuser04', '6f00b7f180b1e2f22a17381fe5f935024c3ff5cc80d898717dc2e02a17f1e3eb'),
('testuser05', '47e5568ac6ae2d170209e02194b640ec116ee0440a476134049585b829aae515'),
('testuser06', '8e9f1d260ae2ac0eb45fadada48164d721bbb6a8b09485476f380276a6d524fd'),
('testuser07', '89dbb01d4a02f0f128b31a80eae4fa2774681308e2411ace79c61ac883613a2e'),
('testuser08', 'fe553f2b2e8b26048279923d7051fe4050e73d33a9b117028263941205c0762d'),
('testuser09', 'fad8f80fe6c94d3e5fc49a509eea8c5a9b8bf2e1d4e288e4e330b42b0237bbca'),
('testuser10', 'acecc6dc8face5a8a25f3e53d15f1f0a0b2844bb456300e8542d6da7d3324c5e');
