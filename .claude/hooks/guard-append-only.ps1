# PreToolUse - BLOCK. DECISIONS.md is append-only; LEDGER.tsv rows are never
# deleted.
#
# The append-only log is what lets a reader six months from now tell a
# deduction from a preference, and see which answers were tried and rejected.
# An edited entry destroys that silently - nothing downstream can detect it.

. (Join-Path $PSScriptRoot 'lib.ps1')

$payload = Read-HookInput (@($input) -join "`n")
if ($null -eq $payload) { exit 0 }

$repo = Get-RepoRoot
$ti   = $payload.tool_input
if ($null -eq $ti) { exit 0 }

foreach ($target in (Get-TargetPaths $payload)) {
    $rel = To-RepoRelative $target $repo
    if (-not $rel) { continue }

    # A whole-file Write over either of them replaces content wholesale.
    if ($payload.tool_name -eq 'Write' -and
        ($rel -eq 'DECISIONS.md' -or $rel -eq 'LEDGER.tsv') -and
        (Test-Path $target)) {
        Deny @"
BLOCKED: Write would replace all of $rel.

$rel is append-only in spirit and is edited by insertion, not rewritten. Use
Edit to append; to change an earlier statement, supersede it with a new entry
that names what it replaces.
"@
    }

    if ($payload.tool_name -ne 'Edit') { continue }
    $old = [string]$ti.old_string
    $new = [string]$ti.new_string
    if ([string]::IsNullOrEmpty($old)) { continue }

    if ($rel -eq 'DECISIONS.md' -and -not $new.Contains($old)) {
        Deny @"
BLOCKED: this Edit rewrites existing text in DECISIONS.md.

The log is append-only: an entry is never edited, only superseded. The
replacement text must still contain the text it replaces (i.e. you are
inserting around it, not over it).

To correct an earlier decision, append:
  ## YYYY-MM-DD - <new decision> [SUPERSEDES "<old entry title>", <date>]
  <what it said, what changed the answer, what was rejected>
  Reversible: yes/no - <how>

The history of being wrong is part of the evidence trail.
"@
    }

    if ($rel -eq 'LEDGER.tsv') {
        $oldRows = ($old -split "`n" | Where-Object { $_.Trim() }).Count
        $newRows = ($new -split "`n" | Where-Object { $_.Trim() }).Count
        if ($newRows -lt $oldRows) {
            Deny @"
BLOCKED: this Edit removes $($oldRows - $newRows) row(s) from LEDGER.tsv.

A ledger row is the only record that a byte is real, and for known-lost paths
it is the only record that the loss was investigated. Rows are superseded in
place (tier, evidence, verified_by, notes), never deleted.

If a file genuinely left srv/, its row becomes known-lost or pending WITH the
reason - never nothing.
"@
        }
    }
}

exit 0
