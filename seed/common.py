"""Shared helpers for seed importers.

Every importer reads ONLY from the archive (never writes there), emits
deterministic SQL into docker/mysql/init/, and stamps a provenance header.
Determinism rule: same archive state -> byte-identical output. No wall-clock
timestamps, no unseeded randomness, sorted iteration everywhere.
"""

import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "docker", "mysql", "init")


def archive_root():
    root = os.environ.get("TT_ARCHIVE_ROOT", os.path.join(REPO, "archive"))
    if not os.path.isdir(root):
        sys.exit("archive root not found: %s (set TT_ARCHIVE_ROOT)" % root)
    return root


def sql_str(s):
    """Escape a python str as a single-quoted MySQL literal (UTF-8 file)."""
    if s is None:
        return "NULL"
    out = (s.replace("\\", "\\\\")
            .replace("'", "\\'")
            .replace("\0", "\\0")
            .replace("\n", "\\n")
            .replace("\r", "\\r")
            .replace("\x1a", "\\Z"))
    return "'" + out + "'"


def sql_int(v):
    if v is None:
        return "NULL"
    return str(int(v))


def sql_bool(v):
    if v is None:
        return "NULL"
    return "1" if v else "0"


def provenance_header(name, tier_data, tier_schema, evidence, caveat=None):
    lines = [
        "-- @provenance data %s / schema %s" % (tier_data, tier_schema),
        "-- @evidence   %s" % evidence,
        "-- @written    2026-08-03 by seed/%s" % name,
        "-- @caveat     Regenerate with `python seed/%s`; do not hand-edit." % name,
    ]
    if caveat:
        lines.append("-- @caveat     %s" % caveat)
    return "\n".join(lines) + "\n\nUSE tanktrouble;\n\n"


def write_out(filename, text):
    out_dir = os.environ.get("TT_SEED_OUT_DIR", OUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s (%d bytes)" % (os.path.relpath(path, REPO), len(text)))
    return path
