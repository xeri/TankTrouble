<!-- Machine-parsed by tests/test_progress_register.py: the table columns and the
     status/kind vocabularies are fixed. Add rows, never renumber them. -->

# Progress register

One row per unit of work. Every file in `docs/plans/` has a row here, and every
row that names a plan names a file that exists. `done` rows name their evidence
of completion — a git tag, or `commit:<sha>`.

**Exactly one row at a time is the target**, and that target is written out in
[`NOW.md`](./NOW.md). Ideas that are not work yet live in
[`BACKLOG.md`](./BACKLOG.md). Procedure for all three: the `track-work` skill.

**Right now, before anything else:** the `archive/` junction does not exist on
this machine and `TT_ARCHIVE_ROOT` is unset, so gates A, C1 and the seeds fail
rather than skip. Create it per `README.md` Setup.

`kind` — `spec` `feature` `gate` `overhaul` `evidence`
`status` — `proposed` `active` `blocked` `done` `superseded`

| id | title | kind | status | plan | gate | tag | notes |
|---|---|---|---|---|---|---|---|
| P-01 | Milestone 1 — skeleton, LEDGER, gates A and D | feature | done | — | `tests/test_assets.py` | `skeleton-complete` | 327 files under `srv/`, every one labelled |
| P-02 | Milestone 2 — seed the DB from the archive corpora | feature | done | — | `tests/test_seed.py` | `seed-complete` | live-imported and verified |
| P-03 | mazeCreator phase 1 — Ruffle / projector control-channel spike | spec | done | `docs/plans/2026-08-03-mazecreator-phase1-spike.md` | `oracle/editor-spike` | `mazecreator-spike-complete` | `SetVariable` absent under Ruffle; dual-channel chosen |
| P-04 | mazeCreator phase 2 — data layer, `MazeData` round-trip | feature | done | `docs/plans/2026-08-03-mazecreator-phase2-datalayer.md` | `oracle/editor-roundtrip` | `mazecreator-datalayer-complete` | 670/670 grids byte-identical |
| P-05 | mazeCreator phase 3 — editor SWF rebuild | feature | done | `docs/plans/2026-08-03-mazecreator-phase3-editor.md` | `tests/test_mazecreator_asset.py` | `mazecreator-editor-complete` | ships M2; the M3 inventions inside it are F-08/F-09/F-10 |
| P-06 | Milestone 3 — reconstruct the PHP | feature | done | `docs/plans/2026-08-03-milestone-3.md` | `tests/test_loadmaze_replay.py` | `m3-complete` | phases A–E; gate B redefined as content replay |
| P-07 | Gate F harness and the 217-region annotation pass | gate | done | — | `tests/test_render_diff.py` | `gatef-harness-ready` | an unannotated region blocks its route |
| P-08 | Gate E — reference-derived subresource inventory | gate | done | — | `tests/test_subresources.py` | `commit:af48c8b` | 134 assets placed; the rest carry `known-lost` rows |
| P-09 | Agent operating system — instructions, rules, skills, hooks, registers | spec | active | `docs/plans/2026-08-08-agent-operating-system.md` | `tests/test_citations.py` | — | this change |
| P-10 | Restore the archive junction on this machine | evidence | blocked | — | `tests/test_assets.py` | — | blocks P-01/P-02 gates and every live run; one `New-Item -ItemType Junction` |
| P-11 | Adopt the manualevidence analyses | evidence | blocked | — | — | — | blocked on step 1 of `adopt-visual-evidence`: the source video URLs have never been supplied, so no finding can carry a citable LEDGER row |
| P-12 | Overhaul F-08 — editor lattice re-fits and re-centres live | overhaul | blocked | — | `oracle/editor-visual` | — | blocked on P-11. Blast radius: `MazeRenderer` geometry, `gauntlet.json`, gate C baseline |
| P-13 | Overhaul F-09 — editor interaction model (drag-paint, hover preview, cursor ghost) | overhaul | blocked | — | `oracle/editor-visual` | — | blocked on P-11. Behaviour only; no wire format moves |
| P-14 | Resolve F-10 — is the floor tone deterministic or random? | overhaul | proposed | — | — | — | settled by two frames of the same maze; see `docs/standards/VISUAL-EVIDENCE-WANTED.md` #8a |
| P-15 | Garage and userpanel reconstruction | feature | proposed | — | — | — | the largest hole in the rebuild. Do not start before P-11: the interaction and layout evidence exists but is uncited |
| P-16 | Continuous integration | gate | proposed | — | — | — | no CI exists; every gate is run by hand. Offline suite is CI-ready today |
| P-17 | Freeze and publish the evidence set alongside the reconstruction | spec | proposed | — | — | — | when the rebuild is substantially complete; unchanged thereafter. See `../../CLAUDE.md` |

## How to read a blocked row

A blocker names what unblocks it and who supplies it. If the real answer is
"impossible", the row is not blocked — close it as `superseded` with the reason,
so nobody re-opens it every quarter. Two things in this project are permanently
impossible and are recorded as such rather than as work: byte-fidelity for forum
SAJAX bodies (zero archived responses) and for the statistics route (zero era
captures).
