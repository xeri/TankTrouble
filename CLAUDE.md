<!-- Operating manual. Budget ~200 lines; it loads every session. Situational
     detail belongs in .claude/rules/ (path-scoped), .claude/skills/
     (procedures) or docs/ (reference). Maintenance rules at the bottom.
     Last audited 2026-08-08 against commit e8ac581. -->

# TankTrouble classic — operating manual

Byte-faithful reconstruction of tanktrouble.com as it ran in **2017–2018**:
PHP 5.6 + MySQL 5.5 in Docker, Python tooling, AS2/Ruffle for the maze editor.
Milestones 1–3 are done and tagged; current work is UI reconstruction from
image evidence, where the risk of invention is highest.

> A reconstruction that cannot be told apart from the original is a forgery,
> not a preservation.

## Routing table

```
docs/NOW.md ................. the current target — start here
docs/BACKLOG.md ............. parked ideas — write it down, keep going
docs/PROGRESS.md ............ work state; the plans themselves in docs/plans/
docs/REBUILD-GUIDE.md ....... the constitution — read its superseded table first
docs/FOUNDATIONS.md ......... structural commitments — before building on a deduction
docs/standards/ ............. the standing disciplines: assets, backend contracts,
                              UI from images, divergences, evidence wanted
docs/reference/ ............. ARCHITECTURE (every constant) · COMMANDS (gate matrix)
                              REASONING (how to think, how to debug) · GLOSSARY
docs/evidence/ .............. published analyses and the raw hunt log
.claude/rules/ .............. conventions per file type — auto-load by path
.claude/skills/ ............. procedures — invoke by name
DECISIONS.md · DEDUCE.md .... the append-only log, and how each claim was deduced
LEDGER.tsv .................. per-file provenance, the spine
```

## Working mode

**One target at a time, and it is written down.** `docs/NOW.md` says what it is
and what done looks like. Start there instead of re-deriving it; the SessionStart
hook prints it for you.

**Triage before ceremony.** Most changes are routine and should just be made:

| | Routine — do it, run the gates it touches, done | Structural — the full ceremony applies |
|---|---|---|
| What it is | fixing a bug in a tool, tightening a test, editing prose, a mechanical rename, resolving a defect the gate already named | anything that makes a new claim about the original site |
| Tells | no new `srv/` path, no tier change, no new constant, no wire or schema change, no invented behaviour | a `FOUNDATIONS` row, a `DECISIONS` entry, a divergence, a promotion, or a new invention |

If it is routine, do not open `FOUNDATIONS.md`, do not write a decision entry,
do not ask which milestone it belongs to. Do the work.

**Read narrow.** The rule file for the path you are editing loads itself. Read a
second document only when the change is structural or the first one sent you
there.

**Run the gates the change affects**, not the whole suite. Gate A rehashes the
archive and takes minutes; `docs/reference/COMMANDS.md` has the matrix. The full run
belongs at the end of a piece of work, not after every edit.

**Park, do not detour.** Something noticed that is not the target and not a
two-minute fix goes into `docs/BACKLOG.md` in one line, and the session carries
on. Scope creep is the main reason this rebuild moves slowly.

**Say what is blocking.** If the target cannot proceed, say so in one sentence
and either take the next `PROGRESS.md` row or stop — do not substitute
adjacent work and call it progress.

## Invariants — these survive any rewrite

**No invention.** Every file under `srv/` has a `LEDGER.tsv` row naming its
tier. A file with no evidence is `M3` and says so in its own header. *A
plausible file is indistinguishable from a real one six months later.*

**Original bytes are never edited.** `O`/`O?` files are copied, never touched —
their provenance is the ledger row, because injecting a header would edit the
original. Mixed files fence verbatim regions with `@O-begin` / `@O-end`.

**Evidence, then verdict, then bytes.** Nothing is placed because it looks
right. A basename match is not evidence; bytes that exist are not automatically
the right bytes (`flashpoint-gamezip` holds a `menuBackground.jpg` that hashes
to the wrong era — copying it in would have looked like a fix and been a
forgery). Verdict vocabulary: `docs/standards/ASSET-DISCIPLINE.md`.

**Absence needs a mechanism.** "Not captured" means nothing until you can say
*why* it was not captured. `mazeCreator_v0.3.swf` appears nowhere in CDX and is
still provably the real path — nothing ever linked it. `DEDUCE.md` §0.3.

**The page's own references are the work list**, never a directory listing.
Gate E (`tests/test_subresources.py`) walks page → subresource; A, D and F all
walk `srv/` → ledger. *A byte-perfect page serving zero images passed A, D and
F simultaneously — 193 missing assets, no ledger rows, nobody noticed.*

**Foundations are declared before they are built on.** Any structural
commitment — document-root shape, schema, wire format, HTTP surface, visual
geometry, interaction model — gets a `docs/FOUNDATIONS.md` row stating its
evidence grade, **its falsifier**, and its dependents *before* code depends on
it. If you cannot say what observation would overturn it, it is a preference,
not a deduction.

**One seam per invention.** An invented constant, geometry or interaction is
written in exactly one place and consumed verbatim (`MazeRenderer` statics fed
by `docs/standards/MAZECREATOR-VISUAL-SPEC.md` is the pattern). *THE OVERHAUL RULE demands
wholesale replacement when evidence lands; that is only affordable behind a
seam.*

**Unobservable is not unaccountable.** Backend behaviour the corpus cannot show
— response headers, error bodies for bad input, selection mechanism, case
handling — is chosen deliberately, declared in the file's `@caveat`, and
registered in `docs/standards/BACKEND-CONTRACTS.md`. Invisible to users is not permission
to guess quietly.

**Reproduce the original's faults.** The SWF version string hard-coded in four
files with no shared constant, `infirmary/index.html` being a hand-copy rather
than a template: these are fidelity, not bugs. Refactoring them is a divergence
and needs an entry.

**Stubs die loudly.** An unverified `.php` returns 501 and says `STUB`. *Gate
D's own words: a stub that returns plausible data is the most dangerous thing
in this project.*

**Image evidence is `M2` at best, never `O`.** Frames are *of* the site, not its
bytes. Confidence tags (`[OBSERVED] [MEASURED] [INFERRED] [UNCERTAIN]
[NOT VISIBLE]`) are never promoted when quoted; scale is derived and shown, never
assumed; video-author overlays are not evidence; page chrome and in-stage
content date separately. Procedure: `docs/standards/UI-RECONSTRUCTION.md`.

**THE OVERHAUL RULE.** When evidence shows how something actually looked or
behaved, the invention is replaced wholesale — never patched to be "close
enough". Wire formats stay green through any overhaul.
`docs/standards/VISUAL-EVIDENCE-WANTED.md`.

**Divergences are logged before they ship**, not after someone notices.
Page/server side: `docs/standards/DIVERGENCES-SERVED.md`. Runtime: `oracle/DIVERGENCES.md`.
Anything visibly non-original must announce itself on screen, so no screenshot
of this stack can be mistaken for evidence.

**Gates fail, never skip.** No archive → fail. No stack → fail, or say
`-m "not live"` on the command line. *A silently-skipped gate A is a green lie.*

**`DECISIONS.md` is append-only.** Supersede by reference; never edit an entry.

**Commits** name the tier, carry one file or one tight pair, and never mix
archive bytes with written code.

**Stop and ask a human** before: changing a wire format, touching auth,
deleting a ledger row, publishing evidence outside the repo, or overturning a
`FOUNDATIONS` row that still has dependents.

## Reality check — what exists today, not what is advertised

| Thing | Ground truth |
|---|---|
| Milestones 1–3 | done, tagged `skeleton-complete` / `seed-complete` / `m3-complete` |
| `README.md` "what comes next" | **stale** — it lists finished work as pending |
| `note.txt` | untracked local scratch, stale, not a source of truth |
| Gate E | subresource resolution. **Not** guide §7.5's "visual regression" — that is gate C |
| Gates B, F | exist and pass, but need the live stack (`-m "not live"` skips them) |
| Gate C | passed for the maze editor only; nothing else has a pixel oracle |
| `archive/` junction | **absent on this machine right now** — gates A, C1 and the seeds fail until it is created (`README.md` Setup) |
| CI | none. Every gate is run by hand |
| `manualevidence` findings | published under `docs/evidence/`, **not adopted**; several falsify pinned visual constants |
| Logged-in rendering | deliberately not reconstructed — near-zero logged-in captures |
| SAJAX | only reconstructed names are callable; everything else returns the stock "not callable" error |
| Scrapyard counter | freezes ~60 s after load, by design — frozen seed state, O client zeroes its own velocity |
| Statistics route, forum SAJAX bodies | zero era captures / zero archived bodies — byte-fidelity is impossible, not pending |

## Enforcement — what is a hook, what is a gate, what is prose

*Creates a forgery or destroys evidence → a hook blocks it. Provable by a test →
a gate owns it. Needs judgement → it lives in this file.*

Hooks (`.claude/hooks/`, wired in `.claude/settings.json`) **block** edits to
archive/evidence paths, to any file whose ledger tier is `O`/`O?`, and to new
`srv/` paths with no ledger row; they **auto-run** gates D and E after `srv/`
edits; they **warn** on the rest. Gate list and commands: `docs/reference/COMMANDS.md`.

## Maintaining this file

* **The razor:** for every rule ask *which file enforces this tomorrow?* If the
  answer is "none", either cut it or build the enforcement.
* Add a rule the **second** time something goes wrong, not the first.
* Cite **symbols**, not line numbers — line numbers drift on every insertion.
  `tests/test_citations.py` checks every citation in every tracked doc.
* A number has exactly one home (`docs/reference/ARCHITECTURE.md`). Cite it by
  name; never restate the value here.
* Budget ~200 lines. Test edits in a fresh session: ask *"summarise the rules in
  CLAUDE.md"* — anything missed means this file is too long or too vague.
* Prune quarterly. A stale instruction is worse than none: agents follow it
  literally and cite it as justification.
