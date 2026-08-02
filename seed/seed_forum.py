"""forum: archive/forum-archive/thread_*.json -> docker/mysql/init/20-forum.sql

Data tier O: original posts, authors and unix timestamps, fetched through the
modern JSON-RPC forum API. Two fields are NOT seeded because they are
fetch-era artefacts, not original data:
  html  -- 2026 client-side rendering of the post
  time  -- the fetch wall-clock, not a post attribute
threadMeta is skipped too: it is a page of thread listings captured alongside
the thread, fully redundant with the thread objects themselves.

creator/coCreator/moderatedBy are modern numeric user-id strings; seeded
verbatim as display metadata, never as foreign keys to logins (guide 5.1).
"""

import glob
import json
import os

from common import archive_root, provenance_header, sql_bool, sql_int, sql_str, write_out

BATCH = 500

THREAD_COLS = ["id", "header", "message", "created", "creator", "coCreator1",
               "coCreator2", "latestEdit", "latestPost", "deleted",
               "moderatedBy", "approved", "banned", "locked", "pinned",
               "hasAnyReplies"]
REPLY_COLS = ["id", "threadId", "message", "created", "creator", "coCreator1",
              "coCreator2", "latestEdit", "deleted", "moderatedBy",
              "approved", "banned"]

INT_COLS = {"id", "threadId", "created", "latestEdit", "latestPost"}
BOOL_COLS = {"deleted", "approved", "locked", "pinned", "hasAnyReplies"}


def render(obj, cols):
    parts = []
    for c in cols:
        v = obj.get(c)
        if c in INT_COLS:
            parts.append(sql_int(v))
        elif c in BOOL_COLS:
            parts.append(sql_bool(v))
        else:
            parts.append(sql_str(v))
    return "(" + ", ".join(parts) + ")"


def batched_insert(table, cols, rendered_rows):
    out = []
    for i in range(0, len(rendered_rows), BATCH):
        out.append("INSERT INTO %s (%s) VALUES\n%s;\n" % (
            table, ", ".join("`%s`" % c for c in cols),
            ",\n".join(rendered_rows[i:i + BATCH])))
    return "".join(out)


def main():
    src = os.path.join(archive_root(), "forum-archive")
    files = sorted(glob.glob(os.path.join(src, "thread_*.json")),
                   key=lambda p: int(os.path.basename(p)[7:-5]))
    threads, replies, missing = [], [], []
    for path in files:
        with open(path, encoding="utf-8") as f:
            doc = json.load(f)
        if "thread" not in doc:
            # the fetch was answered with nothing for this id (thread gone at
            # fetch time). Record the miss; a fabricated row would be M3 data
            # in an O table.
            missing.append(doc["threadId"])
            continue
        t = doc["thread"]
        if t["id"] != doc["threadId"]:
            raise SystemExit("threadId mismatch in %s" % path)
        if doc["replyCount"] != len(doc["replies"]):
            raise SystemExit("replyCount %d != %d replies in %s" % (
                doc["replyCount"], len(doc["replies"]), path))
        threads.append(render(t, THREAD_COLS))
        for r in sorted(doc["replies"], key=lambda r: r["id"]):
            if r["threadId"] != t["id"]:
                raise SystemExit("reply %s in wrong thread file %s" % (r["id"], path))
            replies.append(render(r, REPLY_COLS))

    out = provenance_header(
        "seed_forum.py", "O", "M1",
        "%d threads / %d replies in archive/forum-archive/ (modern JSON-RPC "
        "fetch of original posts); fetch-era fields html/time excluded" % (
            len(threads), len(replies)),
        "Table/column NAMES follow the API field names; the classic-era "
        "schema names were never observable (M3).")
    out += batched_insert("forum_threads", THREAD_COLS, threads)
    out += "\n"
    out += batched_insert("forum_replies", REPLY_COLS, replies)
    out += "\n-- fetch-miss thread ids (archived file, no thread payload; " \
           "deliberately no row): %s\n" % (
               ", ".join(str(i) for i in sorted(missing)) or "none")
    write_out("20-forum.sql", out)
    print("forum: %d threads, %d replies, %d fetch-miss" % (
        len(threads), len(replies), len(missing)))


if __name__ == "__main__":
    main()
