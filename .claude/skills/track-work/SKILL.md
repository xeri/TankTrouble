---
name: track-work
description: Use when starting, pausing, blocking, finishing or superseding a piece of work — writing a plan, opening a milestone or phase, switching target, parking an idea, updating status, or tagging a release. Keeps NOW, BACKLOG, PROGRESS and plans in step.
---

# Track work

Four artefacts, one rule per layer, so a session opens by working rather than by
re-deriving what the work is.

| File | Holds | Changes |
|---|---|---|
| `docs/NOW.md` | **one** target, its definition of done, the next three steps | when the target changes — replaced, not appended |
| `docs/PROGRESS.md` | every unit of work, with status and gate | whenever a row moves |
| `docs/plans/` | the plan documents | written once, then historical |
| `docs/BACKLOG.md` | ideas nobody is working on | constantly, one line at a time |

**Every plan has a register row, and every register row names its evidence of
completion.** `tests/test_progress_register.py` enforces both directions.

## Switching target

Replace the **Target** section of `docs/NOW.md` — do not accumulate history
there; that is what the register is for. The new target is always an existing
`docs/PROGRESS.md` row, and its definition of done must be checkable by someone
who was not in the conversation.

Say what the previous target's state is before switching. A target abandoned
without a status change is how work goes missing.

## Parking

Anything noticed that is not the target and not a two-minute fix goes into
`docs/BACKLOG.md` as one line, and the session carries on. Noticing is cheap;
detouring is not.

When a parked idea is picked up it becomes a `PROGRESS.md` row with a status and
a gate, and its backlog line is struck out. Rejected ideas stay in the backlog's
rejected list **with the reason**, so nobody re-proposes them.

## Opening work

- [ ] Write the plan into `docs/plans/YYYY-MM-DD-<slug>.md`. Phases, exit
      criteria, and the gate that will prove each one. Plans authored in a
      scratch location are copied here the moment the work goes active — a clone
      that cannot read its own roadmap is the problem this fixes.
- [ ] Add the `docs/PROGRESS.md` row:

```
id · title · kind · status · plan · gate · tag · notes
```

  * `kind` — `spec` | `feature` | `gate` | `overhaul` | `evidence`
  * `status` — `proposed` | `active` | `blocked` | `done` | `superseded`
  * `gate` — the test that will prove it. An `active` row must name one. If no
    gate can prove it, say so explicitly and say what will be inspected instead.
  * `tag` — the git tag, once it exists. Required on `done`.
- [ ] Register any structural commitment the work will make in
      `docs/FOUNDATIONS.md` **before** building on it — grade, falsifier,
      dependents, blast radius.

## While working

- [ ] `blocked` rows name what unblocks them and who or what supplies it. A
      blocker that is really "impossible" is not blocked — mark it `superseded`
      or close it with the reason, so nobody re-opens it every quarter.
- [ ] A discovery that changes the plan goes in `DECISIONS.md`, and the plan body
      is **not** rewritten. The plan records what was intended; `DECISIONS.md`
      records what shipped. Where they differ, `DECISIONS.md` wins.

## Closing work

- [ ] Verify **every** exit criterion, freshly, on a clean run. Not from memory,
      not from an earlier session.
- [ ] Run the full offline suite, and the live suite if the stack is up.
- [ ] Write the `DECISIONS.md` entries the phase owes. A phase that made choices
      and recorded none has not finished.
- [ ] Tag, then flip the register row to `done` with the tag in it.
- [ ] Add the follow-ups the work exposed as new `proposed` rows, with enough
      context to act on cold.

## Superseding

Set `status: superseded` and name the successor row. Never delete a row — the
register is also the record of what was tried.

## Overhaul items

New evidence that falsifies something already shipped opens an `overhaul` row
naming the falsified `FOUNDATIONS` id and the blast radius. It stays open until
the piece is rewritten wholesale — patching it closed is exactly the failure
THE OVERHAUL RULE exists to prevent.
