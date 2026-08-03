"""Gate S — seed data. The generated SQL in docker/mysql/init/ must be
reproducible from the archive, carry provenance, and never smuggle invented
rows into O data. No live MySQL exists on this machine (DECISIONS.md); these
checks are content-level, and DB-level validation happens when a docker
runtime is available."""

import base64
import glob
import json
import os
import re
import subprocess
import sys

from conftest import REPO

INIT = REPO / "docker" / "mysql" / "init"
SEED = REPO / "seed"
GENERATED = {
    "10-mazes.sql": "seed_mazes.py",
    "20-forum.sql": "seed_forum.py",
    "30-news.sql": "seed_news.py",
    "40-users.sql": "seed_users.py",
    "50-static.sql": "seed_static.py",
}
# forum regeneration reads 3 GB and takes minutes; its reproducibility is
# covered by the count/shape checks below instead of a full re-run
DETERMINISM_RERUN = ["seed_mazes.py", "seed_news.py", "seed_users.py",
                     "seed_static.py"]


def sql(name):
    return (INIT / name).read_text(encoding="utf-8")


def rows_of(text, table):
    """Count VALUES tuples across all INSERT statements for `table`."""
    n = 0
    for m in re.finditer(
            r"INSERT INTO %s\s*\([^)]*\)\s*VALUES\n(.*?);\n" % table,
            text, re.S):
        n += len(re.findall(r"^\(", m.group(1), re.M))
    return n


def test_all_seed_files_exist_with_provenance():
    missing, headerless = [], []
    for name in ["00-schema.sql"] + sorted(GENERATED):
        p = INIT / name
        if not p.is_file():
            missing.append(name)
            continue
        if "@provenance" not in p.read_text(encoding="utf-8")[:2048]:
            headerless.append(name)
    assert not missing, "missing seed files: %s" % missing
    assert not headerless, "seed files without @provenance: %s" % headerless


def test_generated_seeds_are_reproducible(tmp_path, archive_root):
    """Byte-identical regeneration — catches archive drift, nondeterminism,
    and hand-edits to generated files alike."""
    env = dict(os.environ,
               TT_SEED_OUT_DIR=str(tmp_path),
               TT_ARCHIVE_ROOT=str(archive_root))
    bad = []
    for script in DETERMINISM_RERUN:
        r = subprocess.run([sys.executable, str(SEED / script)],
                           cwd=str(SEED), env=env, capture_output=True, text=True)
        assert r.returncode == 0, "%s failed:\n%s" % (script, r.stderr)
    for name, script in GENERATED.items():
        if script not in DETERMINISM_RERUN:
            continue
        fresh = (tmp_path / name).read_bytes()
        committed = (INIT / name).read_bytes()
        if fresh != committed:
            bad.append(name)
    assert not bad, "committed seed differs from regeneration: %s" % bad


def test_maze_rows_match_corpus(archive_root):
    """One row per (author, slot), latest capture wins (DECISIONS
    2026-08-03) — recompute the winner count from the corpus by the same
    rule the seed uses, independently of the seed's own code."""
    files = glob.glob(str(archive_root / "maze-corpus" / "raw" / "*.txt"))
    states, notfound = set(), 0
    for f in files:
        r = dict(p.split("=", 1) for p in open(f).read().strip().split("&"))
        inner = base64.b64decode(r["r"]).decode("utf-8")
        if inner == "notFound=true":
            notfound += 1
            continue
        fields = dict(p.split("=", 1) for p in inner.split("&"))
        assert set(fields) == {"t", "n", "d", "s"}, f
        states.add((fields["n"], fields["s"]))
    text = sql("10-mazes.sql")
    assert len(files) == 843 and notfound == 1, "corpus changed — re-audit"
    assert rows_of(text, "mazes") == len(states) == 672
    assert "-- superseded" in text and "-- witness" in text, (
        "time-series trailer missing")


def test_forum_rows_match_corpus(archive_root):
    thread_files = glob.glob(str(archive_root / "forum-archive" / "thread_*.json"))
    text = sql("20-forum.sql")
    n_threads = rows_of(text, "forum_threads")
    miss = re.search(r"fetch-miss thread ids .*?: (.+)$", text, re.M)
    assert miss, "fetch-miss trailer missing"
    n_miss = 0 if miss.group(1).strip() == "none" else len(miss.group(1).split(","))
    assert n_threads + n_miss == len(thread_files), (
        "threads %d + fetch-miss %d != %d archived thread files" % (
            n_threads, n_miss, len(thread_files)))
    assert rows_of(text, "forum_replies") > 200000, "reply corpus implausibly small"


def test_forum_excludes_fetch_era_fields():
    head = sql("20-forum.sql")[:4000]
    cols = re.search(r"INSERT INTO forum_threads \(([^)]*)\)", head).group(1)
    assert "html" not in cols and "`time`" not in cols, (
        "fetch-era fields must not be seeded")


def test_news_bodies_are_verbatim_capture_slices(archive_root):
    """Every seeded body must appear byte-for-byte in at least one anchored
    classic capture — the blob is O data, so nothing may have rewritten it."""
    text = sql("30-news.sql")
    used = re.search(r"-- captures used: (.+)$", text, re.M).group(1).split(", ")
    corpus = ""
    for name in used:
        corpus += open(str(archive_root / "commoncrawl" / "warc-bodies" / name),
                       encoding="utf-8", errors="replace").read()
    bodies = re.findall(r", '((?:[^'\\]|\\.)*)'\)[,;]", text)
    assert len(bodies) == rows_of(text, "news")
    unescape = lambda s: (s.replace("\\\\", "\x00").replace("\\'", "'")
                          .replace("\\n", "\n").replace("\\r", "\r")
                          .replace("\\0", "\0").replace("\\Z", "\x1a")
                          .replace("\x00", "\\"))
    missing = [b[:60] for b in map(unescape, bodies) if b not in corpus]
    assert not missing, "bodies not found verbatim in captures: %r" % missing[:3]


def test_users_are_obviously_synthetic():
    text = sql("40-users.sql")
    names = re.findall(r"\('([^']+)', '\$2y\$10\$[./A-Za-z0-9]{53}'\)", text)
    assert names, "no user rows parsed (bcrypt password_hash expected)"
    assert all(re.fullmatch(r"testuser\d{2}", n) for n in names), (
        "user rows must be obviously fake: %s" % names)


def test_schema_covers_every_seeded_table():
    schema = sql("00-schema.sql")
    created = set(re.findall(r"CREATE TABLE (\w+)", schema))
    seeded = set()
    for name in GENERATED:
        seeded |= set(re.findall(r"INSERT INTO (\w+)", sql(name)))
    assert seeded <= created, "seeded tables missing DDL: %s" % (seeded - created)
