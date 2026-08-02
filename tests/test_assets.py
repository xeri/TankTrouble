"""Gate A — asset integrity. Every O/O? row's sha256 recomputed against BOTH
srv/ and the archive source (three-way lock: ledger == srv == archive).
Blocks every commit. See REBUILD-GUIDE.md 7.1."""

import hashlib

from conftest import DASH, REPO, TIERS, srv_files

MAGIC = {
    ".swf": (b"FWS", b"CWS", b"ZWS"),
    ".png": (b"\x89PNG",),
    ".jpg": (b"\xff\xd8\xff",),
    ".jpeg": (b"\xff\xd8\xff",),
    ".gif": (b"GIF87a", b"GIF89a"),
    ".pdf": (b"%PDF",),
    ".zip": (b"PK",),
    ".woff": (b"wOFF",),
    ".ttf": (b"\x00\x01\x00\x00",),
}


def sha256_of(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def o_rows(ledger):
    return [r for r in ledger if r["tier"] in ("O", "O?")]


def test_ledger_well_formed(ledger):
    seen = set()
    for r in ledger:
        assert r["tier"] in TIERS, f"{r['path']}: bad tier {r['tier']!r}"
        assert r["path"] not in seen, f"duplicate row: {r['path']}"
        seen.add(r["path"])
        if r["tier"] in ("O", "O?"):
            assert len(r["sha256"]) == 64, f"{r['path']}: O row without sha256"
            assert r["source"].startswith("archive/"), \
                f"{r['path']}: O source must live under archive/"
        if r["tier"].startswith("M"):
            assert r["evidence"] and r["evidence"] != DASH or r["tier"] == "M3", \
                f"{r['path']}: M* row must name its evidence"
        vb = r["verified_by"]
        assert vb == DASH or (REPO / vb).is_file(), \
            f"{r['path']}: verified_by names missing file {vb!r}"


def test_o_rows_match_srv(ledger):
    bad = []
    for r in o_rows(ledger):
        f = REPO / r["path"]
        if not f.is_file():
            bad.append(f"{r['path']}: file missing")
        elif sha256_of(f) != r["sha256"]:
            bad.append(f"{r['path']}: srv/ bytes drifted from ledger")
    assert not bad, "\n".join(bad)


def test_o_rows_match_archive(ledger, archive_root):
    bad = []
    for r in o_rows(ledger):
        src = archive_root / r["source"].removeprefix("archive/")
        if not src.is_file():
            bad.append(f"{r['path']}: archive source missing {r['source']}")
        elif sha256_of(src) != r["sha256"]:
            bad.append(f"{r['path']}: archive source sha256 != ledger")
    assert not bad, "\n".join(bad)


def test_file_set_equality(ledger):
    """Refined guide-4 exit criterion: rows-with-files == files, both ways."""
    row_paths = {r["path"] for r in ledger
                 if r["tier"] not in ("known-lost", "pending")}
    files = set(srv_files())
    missing_rows = files - row_paths
    missing_files = row_paths - files
    assert not missing_rows, f"srv/ files without ledger row: {sorted(missing_rows)}"
    assert not missing_files, f"ledger rows without file: {sorted(missing_files)}"


def test_magic_bytes(ledger):
    """Trap #1 guard: size is not integrity; validate magic on originals."""
    bad = []
    for r in o_rows(ledger):
        f = REPO / r["path"]
        magics = MAGIC.get(f.suffix.lower())
        if not magics or not f.is_file():
            continue
        head = f.read_bytes()[:8]
        if not any(head.startswith(m) for m in magics):
            bad.append(f"{r['path']}: magic {head[:4]!r} not in {magics}")
    assert not bad, "\n".join(bad)
