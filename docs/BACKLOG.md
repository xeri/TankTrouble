# Backlog — ideas parked, so they stop costing attention

Anything noticed but not the current target. Write it here in one line and keep
going: noticing is cheap, detouring is not.

This is **not** the work register. When an idea is picked up it becomes a row in
`docs/PROGRESS.md` with a status and a gate, and its line here is struck out.
Ideas may sit here indefinitely; that is the point.

Format: `- [area] one line — why it matters, in a clause.`

## Parked

- [docs] `README.md`'s "What comes next" lists finished milestones as pending — misleads any reader who starts there.
- [docs] `note.txt` is untracked, stale, and reads like a status file; either delete it or mark it scratch in the first line.
- [gates] No CI. The offline suite is CI-ready today; a single workflow would stop every gate depending on someone remembering.
- [gates] Gate A rehashes the whole archive on every run (~4 min). A digest cache keyed by mtime+size would make the suite usable as a pre-commit hook.
- [evidence] `TankTrouble.ttf` is authenticated as first-party but not evidenced as classic-served — decide whether it can ever be used.
- [evidence] The chat system reported in footage appears in no held byte, no ledger row and no want-list entry.
- [backend] `updateGameStatistics.php` — pull the CDX digests. A single constant digest makes the body recoverable and lifts it off 501; it is a cheap, decisive check.
- [backend] `theLabReport/` PDFs are still fetchable and deferred; no ledger rows yet.
- [ui] In-round floor tone is reported flat, not the editor's two-tone mix — a different surface from F-10 and currently unmodelled.
- [ui] Three maze slots per tank is reported in footage; the corpus only ever observed one. Blocks garage work.
- [infra] `docker/mysql/init/20-forum.sql` is 36 MB and in history. Under GitHub's limits, but worth LFS if it grows.

## Rejected, with the reason

Kept so nobody re-proposes them.

- Making the Scrapyard counter climb — would put extrapolated digits on every screenshot. `docs/standards/DIVERGENCES-SERVED.md` §5 records the design that was considered and declined.
- Byte-fidelity for forum SAJAX responses — zero archived bodies. Impossible, not pending.
- Byte-fidelity for the statistics route — zero era captures. Impossible, not pending.
- Per-capture DB snapshots to solve the gate F as-of problem — mutates seed data per test.
