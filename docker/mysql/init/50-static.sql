-- @provenance data M2 / schema M2
-- @evidence   accessories: initCode tal/baral/fal/bacal DEBUG catalogue in archive/decompiled/EMBED_signUpTankDesign18StandardColours_20201225; achievements: literal ids at v4.0 client call sites
-- @written    2026-08-03 by seed/seed_static.py
-- @caveat     Regenerate with `python seed/seed_static.py`; do not hand-edit.
-- @caveat     The live accessory catalogue was never captured; these rows are the developer's debug set. Achievement ids 1-27 and 33 existed (the numbering proves it) but were never observed -- no rows.

USE tanktrouble;

INSERT INTO accessories (slot, accessory_id, toolbox) VALUES
('turret', 1, 1),
('turret', 2, 1),
('turret', 3, 1),
('turret', 4, 1),
('turret', 5, 2),
('turret', 13, 3),
('turret', 20, 4),
('turret', 27, 5),
('turret', 33, 6),
('barrel', 1, 1),
('barrel', 2, 1),
('barrel', 3, 1),
('barrel', 4, 1),
('front', 1, 1),
('front', 2, 1),
('front', 3, 1),
('front', 4, 1),
('back', 1, 1),
('back', 2, 1),
('back', 3, 1),
('back', 4, 1);

INSERT INTO achievements (id) VALUES
(28),
(29),
(30),
(31),
(32),
(34),
(35),
(36);
