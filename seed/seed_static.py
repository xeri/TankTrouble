"""accessories + achievements: decompile constants -> 50-static.sql

accessories -- tier M2. The paint/signup editor receives its catalogue via
FlashVar initCode fields tal/baral/fal/bacal as "id-toolbox," pairs
(EMBED_signUpTankDesign18StandardColours_20201225 frame_1). The LIVE
catalogue flowed only to logged-in garages and was never captured; the one
recoverable listing is the editor's own DEBUG block, which the developer
kept plausible enough to exercise every toolbox tier. Seeded AS the debug
catalogue, labelled as such -- do not mistake these ids for the shop's real
inventory.

achievements -- tier M2. The v4.0 client calls unlockAchievement /
achievementProgress / multipleAchievementProgress with literal ids
{28,29,30,31,32,34,35,36}. Nothing else about an achievement (name, art,
threshold) is client-visible, and the id numbering implies 1..27 and 33
existed with owners unknown -- rows only for the observed ids.
"""

from common import provenance_header, write_out

# id-toolbox pairs, verbatim from the DEBUG block
DEBUG_CATALOGUE = {
    "turret": "1-1,2-1,3-1,4-1,5-2,13-3,20-4,27-5,33-6,",
    "barrel": "1-1,2-1,3-1,4-1,",
    "front":  "1-1,2-1,3-1,4-1,",
    "back":   "1-1,2-1,3-1,4-1,",
}
ACHIEVEMENT_IDS = [28, 29, 30, 31, 32, 34, 35, 36]


def main():
    out = provenance_header(
        "seed_static.py", "M2", "M2",
        "accessories: initCode tal/baral/fal/bacal DEBUG catalogue in "
        "archive/decompiled/EMBED_signUpTankDesign18StandardColours_20201225; "
        "achievements: literal ids at v4.0 client call sites",
        "The live accessory catalogue was never captured; these rows are the "
        "developer's debug set. Achievement ids 1-27 and 33 existed (the "
        "numbering proves it) but were never observed -- no rows.")
    out += "INSERT INTO accessories (slot, accessory_id, toolbox) VALUES\n"
    vals = []
    for slot in ("turret", "barrel", "front", "back"):
        for pair in DEBUG_CATALOGUE[slot].split(",")[:-1]:
            aid, box = pair.split("-")
            vals.append("('%s', %d, %d)" % (slot, int(aid), int(box)))
    out += ",\n".join(vals) + ";\n\n"
    out += "INSERT INTO achievements (id) VALUES\n"
    out += ",\n".join("(%d)" % i for i in ACHIEVEMENT_IDS) + ";\n"
    write_out("50-static.sql", out)
    print("accessories: %d rows; achievements: %d rows" % (
        len(vals), len(ACHIEVEMENT_IDS)))


if __name__ == "__main__":
    main()
