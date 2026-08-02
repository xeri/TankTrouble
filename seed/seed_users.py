"""users: synthetic -> docker/mysql/init/40-users.sql

Tier M3, deliberately. Real usernames in the maze corpus and forum archive
are public authorship metadata and stay where they are -- as display strings,
never as login rows (guide 5.1). Real credentials exist in the public
Wayback CDX (the original ran SAJAX auth over GET) and are NEVER seeded.

Usernames are obviously fake (testuser01..). Password column holds the
SHA-256 of a per-user secret drawn from a fixed-seed PRNG; the secrets are
not recorded anywhere, so no seeded account is usable until milestone-3 auth
(itself a deliberate divergence, guide 6.4) decides the real storage format.
"""

import hashlib
import random

from common import provenance_header, sql_str, write_out

N_USERS = 10
SEED = 0x7A6B  # fixed: output must be byte-stable across runs


def main():
    rng = random.Random(SEED)
    out = provenance_header(
        "seed_users.py", "M3", "M3",
        "none -- synthetic accounts; original user table never observable",
        "Hash format is a placeholder; milestone-3 auth (deliberate "
        "divergence, guide 6.4) owns the real decision.")
    out += "INSERT INTO users (username, password_sha256) VALUES\n"
    vals = []
    for i in range(1, N_USERS + 1):
        secret = "%032x" % rng.getrandbits(128)
        digest = hashlib.sha256(secret.encode("ascii")).hexdigest()
        vals.append("(%s, %s)" % (sql_str("testuser%02d" % i), sql_str(digest)))
    out += ",\n".join(vals) + ";\n"
    write_out("40-users.sql", out)
    print("users: %d synthetic rows" % N_USERS)


if __name__ == "__main__":
    main()
