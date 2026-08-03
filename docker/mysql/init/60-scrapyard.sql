-- @provenance data M2 / schema M3
-- @evidence   archive/includes-tree/20160126_getScrapyard.php (scraps),
--             archive/includes-tree/20150928_getScrapyard.php (velocity)
-- @written    2026-08-03 (hand-written, two archived values)
-- @caveat     Seed = latest archived scraps + only archived velocity,
--             labelled ARBITRARY as live state (guide 5.1); the replay gate
--             injects each archived state explicitly and restores this row.

SET NAMES utf8;
USE tanktrouble;

INSERT INTO scrapyard_state (id, scraps, velocity) VALUES
(1, 1785664230, '0.0071382502652744');
