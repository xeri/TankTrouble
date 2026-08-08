# PostToolUse - AUTO-GATE. Run the cheap offline gates whose subject just
# changed, and feed any failure straight back.
#
# Gate D and gate E are seconds long and catch the two mistakes that are
# expensive to find later: an unlabelled file, and a page asking for something
# that does not exist. Running them here means a broken state never survives
# past the edit that caused it.

. (Join-Path $PSScriptRoot 'lib.ps1')

$payload = Read-HookInput (@($input) -join "`n")
if ($null -eq $payload) { exit 0 }

$repo = Get-RepoRoot
$touched = @()
foreach ($target in (Get-TargetPaths $payload)) {
    $rel = To-RepoRelative $target $repo
    if ($rel) { $touched += $rel }
}
if (-not $touched) { exit 0 }

$gates = @()
if ($touched | Where-Object { $_ -like 'srv/*' -or $_ -eq 'LEDGER.tsv' }) {
    $gates += 'tests/test_no_unlabelled.py'
    $gates += 'tests/test_subresources.py'
}
if ($touched | Where-Object { $_ -like '*.md' -or $_ -like '.claude/*' }) {
    $gates += 'tests/test_citations.py'
    $gates += 'tests/test_docs_single_source.py'
    $gates += 'tests/test_progress_register.py'
    $gates += 'tests/test_foundations.py'
}
$gates = $gates | Select-Object -Unique
if (-not $gates) { exit 0 }

Push-Location $repo
try {
    $out = & python -m pytest @gates -m "not live" -q --no-header 2>&1 | Out-String
    $code = $LASTEXITCODE
} catch {
    # No python on PATH is a developer-environment problem, not a finding.
    Pop-Location; exit 0
}
Pop-Location

if ($code -ne 0) {
    [Console]::Error.WriteLine(@"
GATE FAILED after this edit - fix it now, not later.

$out
A red gate is a to-do list. Do not delete a row, widen a mask, or copy a
plausible file into place to make it green.
"@)
    exit 2
}

exit 0
