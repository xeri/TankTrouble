"""users: synthetic -> docker/mysql/init/40-users.sql

Tier M3, deliberately. Real usernames in the maze corpus and forum archive
are public authorship metadata and stay where they are -- as display strings,
never as login rows (guide 5.1). Real credentials exist in the public
Wayback CDX (the original ran SAJAX auth over GET) and are NEVER seeded.

Usernames are obviously fake (testuser01..). The password column holds PHP
password_hash() bcrypt strings (guide 6.4 divergence: POST + TLS +
password_hash). Per-user secret AND bcrypt salt are drawn from a fixed-seed
PRNG, so the whole chain is reproducible: the auth gate
(tests/test_auth_divergence.py) re-derives testuser01's secret from the
same PRNG and logs in with it. The bcrypt strings below were produced ONCE
inside the stack's own php:5.6 container:

    php -r "password_hash($secret, PASSWORD_BCRYPT,
                          array('cost'=>10, 'salt'=>$salt));"

with salt = first 22 hex chars of the user's second PRNG draw -- fixed salt
=> deterministic output => this file stays byte-stable without needing
docker at regen time.
"""

from common import provenance_header, sql_str, write_out

N_USERS = 10
SEED = 0x7A6B  # fixed: secrets derive from random.Random(SEED), see HASHES

# (username, bcrypt of PRNG secret) -- see module docstring for derivation
HASHES = [
    ("testuser01", "$2y$10$MzRjM2ViOTgzOGE3YTMyYORMgO.JtPGjD9QaaUAoz..zHzLNxPurS"),
    ("testuser02", "$2y$10$NDUzMGFmZjZlYmJkZTM3ZOSTGN.3iG3ZwOKKuUAILnT9eqcUwyFQ."),
    ("testuser03", "$2y$10$NzNiYzA5ZjhhOTljYjk5ZOBSVFvm0Kj0E.aule/fqzznsldbHJWei"),
    ("testuser04", "$2y$10$MGY3MDM3MzI0OWY4MjIzYO0kgEBrfQJ5LpRqaGeXhL/XQerw9LPqm"),
    ("testuser05", "$2y$10$OTc1N2EyMTg3YmZiNDNmM.CNcxUM/EuPwOHrdnqPW0ZTBeBT2oB4m"),
    ("testuser06", "$2y$10$OGUzMGJjMTUzYjc5ODIwM.NN1R5TuSSUDesD/kQ8/DKAUzEc1hrEi"),
    ("testuser07", "$2y$10$N2IxOWY2YWViZDliNzY1NOP/jS64z93z0eMZiYKAz1/4hJUDIjNu6"),
    ("testuser08", "$2y$10$ZjFjMWY4YmYxNGM4Nzk1YOLV2QkLnwNOQHUU0SOlRwCay76h8z3RW"),
    ("testuser09", "$2y$10$YTMwZGE2NmNmNWJmZWFlZeiDNYHwx7N.9XXP5IvsBWw/fl9rxdyye"),
    ("testuser10", "$2y$10$ZjM1MmQzOTBiMjAyYTU4YOPcCf9yPztT4LJk8xxjhhyZx/K0Zxga."),
]


def secrets():
    """The reproducible per-user (secret, salt) chain; imported by the auth
    gate to log in as a synthetic user."""
    import random
    rng = random.Random(SEED)
    out = []
    for _ in range(N_USERS):
        secret = "%032x" % rng.getrandbits(128)
        salt = ("%032x" % rng.getrandbits(128))[:22]
        out.append((secret, salt))
    return out


def main():
    out = provenance_header(
        "seed_users.py", "M3", "M3",
        "none -- synthetic accounts; original user table never observable",
        "bcrypt via password_hash (guide 6.4 divergence); secrets derive "
        "from the fixed PRNG in seed_users.py, hashes pinned there.")
    out += "INSERT INTO users (username, password_hash) VALUES\n"
    vals = ["(%s, %s)" % (sql_str(u), sql_str(h)) for u, h in HASHES]
    out += ",\n".join(vals) + ";\n"
    write_out("40-users.sql", out)
    print("users: %d synthetic rows (bcrypt)" % len(HASHES))


if __name__ == "__main__":
    main()
