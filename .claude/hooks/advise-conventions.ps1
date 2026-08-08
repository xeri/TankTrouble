# PostToolUse - WARN. Never blocks; surfaces the paperwork an edit just
# incurred, while the reason is still in context.
#
# These are judgement calls, not violations: a missing @caveat might be a
# forthcoming commit, and a ledger change might get its DECISIONS entry in the
# next edit. Blocking would be wrong. Silence would be worse.

. (Join-Path $PSScriptRoot 'lib.ps1')

$payload = Read-HookInput (@($input) -join "`n")
if ($null -eq $payload) { exit 0 }

$repo = Get-RepoRoot
$notes = @()

foreach ($target in (Get-TargetPaths $payload)) {
    $rel = To-RepoRelative $target $repo
    if (-not $rel) { continue }

    # An M2/M3 file must name what was chosen where the evidence ran out.
    $tier = Get-LedgerTier $rel $repo
    if (($tier -eq 'M2' -or $tier -eq 'M3') -and (Test-Path $target)) {
        $head = Get-Content $target -TotalCount 40 -ErrorAction SilentlyContinue
        if ($head -and -not ($head -match '@caveat')) {
            $notes += "$rel is tier $tier but its header has no @caveat. Name the choices the evidence did not force - an uncaveated invention is indistinguishable from a finding. (gate D checks this)"
        }
    }

    if ($rel -eq 'LEDGER.tsv') {
        $notes += "LEDGER.tsv changed. If a tier, verified_by or placement decision moved, it needs a DECISIONS.md entry naming what was rejected and whether it is reversible. Promotions need a citation: the gate that proves it, plus the capture list."
    }

    if ($rel -like 'docs/plans/*') {
        $notes += "docs/plans/ changed. Every plan needs a docs/PROGRESS.md row (id, kind, status, gate, tag) - tests/test_progress_register.py checks both directions."
    }

    if ($rel -eq 'docs/FOUNDATIONS.md') {
        $notes += "docs/FOUNDATIONS.md changed. If a row moved to falsified, open the overhaul row in docs/PROGRESS.md with its blast radius and rewrite the piece wholesale - patching it closed is the failure THE OVERHAUL RULE exists to prevent."
    }

    if ($rel -like 'srv/*' -and $rel -notlike '*.provenance') {
        $notes += "$rel is served output. If anything a user would see now differs from what the original served, it is a divergence: record it in docs/standards/DIVERGENCES-SERVED.md BEFORE it ships, not after someone notices."
    }

    if ($rel -like 'src/mazecreator/*' -or $rel -like 'oracle/*') {
        $notes += "$rel affects rendered pixels. Re-run the gate C oracle, and check docs/FOUNDATIONS.md F-08/F-09/F-10 - those constants are provisional or already falsified."
    }
}

if (-not $notes) { exit 0 }
$body = ($notes | Select-Object -Unique | ForEach-Object { "- $_" }) -join "`n"
Advise $body
