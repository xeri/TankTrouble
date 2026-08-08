---
name: record-decision
description: Use when a judgement call has been made that the evidence did not force — a chosen name, format, type, threshold, or scope boundary — or when new evidence supersedes an earlier decision. Writes the DECISIONS.md entry and checks what else must move.
---

# Record a decision

`DECISIONS.md` is append-only and is the reason a reader six months from now can
tell a deduction from a preference. Newest at the bottom. **Never edit an
existing entry.**

## What needs an entry

Anything the evidence did not force:

* a name, a type, a limit, a default, a selection mechanism
* a scope boundary ("this stays 501") — a decision, not an omission
* a deviation from the guide, or from an earlier decision
* accepting a lower tier, or declining to promote
* anything that would make a later reader ask "why is it like this?"

## Format

```
## YYYY-MM-DD — <what was decided> [SUPERSEDES "<old entry title>", <date>]
Tier: <if the entry places or moves a file>
<Why. What the evidence forced, and where it ran out.>
<Mechanism: how the choice is prevented from going wrong silently.>
Rejected: <the real alternatives, each with the reason>
Wanted: <what evidence would let this be revisited> (optional)
Reversible: yes/no — <how to undo it>
```

An entry with no `Rejected:` line usually means no decision was actually made —
go back and find the alternatives.

## Then check what else moves

- [ ] **`docs/FOUNDATIONS.md`** — does this pin or overturn a structural
      commitment? If it pins one, the row needs a grade, a falsifier, its
      dependents and its blast radius before anything builds on it.
- [ ] **`LEDGER.tsv`** — does a tier, `verified_by`, or note change?
- [ ] **`docs/standards/BACKEND-CONTRACTS.md`** — is this a chosen answer to something the
      corpus cannot show?
- [ ] **`docs/standards/DIVERGENCES-SERVED.md` / `oracle/DIVERGENCES.md`** — is anything
      user-visible now different from what the original served? Log it *before*
      it ships.
- [ ] **`docs/standards/VISUAL-EVIDENCE-WANTED.md`** — would evidence overturn this? Add
      the want entry now, while you still know exactly what would settle it.
- [ ] **`docs/PROGRESS.md`** — does a register row change status?

## Superseding

Name the entry you are replacing in the heading, restate what it said, and say
what changed the answer. The old entry stays exactly as written — the history of
being wrong is part of the evidence trail.

## Escalate instead of deciding

Wire format changes, authentication, ledger row deletion, publishing evidence
outside the repo, and overturning a `FOUNDATIONS` row that still has dependents
are not yours to decide alone. Ask.
