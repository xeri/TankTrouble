# PreToolUse - BLOCK. Original bytes are never edited, and a new path under
# srv/ is an evidence claim.
#
# Two failure modes, both silent and both forgeries:
#   1. Editing an O/O? file makes the ledger's sha256 a lie. Gate A catches it
#      later; by then the original bytes are gone from the working tree.
#   2. Creating a file under srv/ asserts the original server had that path.
#      Gate D would flag the missing row, but only after the claim exists.

. (Join-Path $PSScriptRoot 'lib.ps1')

$payload = Read-HookInput (@($input) -join "`n")
if ($null -eq $payload) { exit 0 }

$repo = Get-RepoRoot

foreach ($target in (Get-TargetPaths $payload)) {
    $rel = To-RepoRelative $target $repo
    if (-not $rel) { continue }

    $tier = Get-LedgerTier $rel $repo

    if ($tier -eq 'O' -or $tier -eq 'O?') {
        Deny @"
BLOCKED: $rel is tier $tier - original bytes.

O and O? files are copied, never touched. Their provenance IS the ledger row
(injecting a header would itself edit the original), and gate A recomputes
sha256 from both srv/ and the archive source.

If this file is wrong, the finding is about the ledger row or the era
resolution, not the bytes:
  - wrong bytes chosen  -> re-run tools/resolve_era.py, supersede in DECISIONS.md
  - needs modification  -> it is not an O file. That is a de-render: write a
    new M* file with the original spans inside @O-begin/@O-end fences.
"@
    }

    if ($rel -like 'srv/*' -and $null -eq $tier -and -not (Test-Path $target)) {
        Deny @"
BLOCKED: $rel would be a new path under srv/ with no LEDGER.tsv row.

Every file under srv/ is a claim that the original server served that path.
The row comes first, carrying the evidence for the claim.

If this is shared logic rather than a served file, it does not belong under
srv/ at all - index.php holds in-file functions precisely so no new fetchable
path is invented (docs/FOUNDATIONS.md F-03).
"@
    }
}

exit 0
