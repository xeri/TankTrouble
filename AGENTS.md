# AGENTS.md

Entry point for coding agents that do not read `CLAUDE.md`.

**Read `CLAUDE.md` first.** It is the operating manual for this repository and
the source of truth for everything below. This file exists only so tools that
look for `AGENTS.md` find their way there; it is deliberately not imported by
`CLAUDE.md`, so it costs no context and cannot drift into a second rulebook.

Then, in order:

1. `CLAUDE.md` — invariants, reality check, routing table.
2. `docs/REBUILD-GUIDE.md` — the constitution. Read its "Superseded sections"
   table before following any `§`.
3. `docs/FOUNDATIONS.md` — the structural commitments you must not silently
   build on top of.
4. `.claude/rules/` — conventions per file type. A Claude Code session loads
   these automatically when it touches a matching path; other tools should read
   the one matching the files they are about to change.

The one-line version: **nothing is written without evidence, original bytes are
never edited, and a gate that cannot run fails rather than skips.**
