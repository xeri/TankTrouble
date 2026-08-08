# Shared helpers for the TankTrouble guard hooks.
# Loaded by every hook script; contains no side effects.

$ErrorActionPreference = 'Stop'

function Read-HookInput($raw) {
    <#  The hook payload arrives as one JSON object on stdin - but WHERE
        depends on how powershell.exe was invoked: `-File` delivers it through
        the script's $input pipeline, `-Command` through [Console]::In. Callers
        pass their own $input; this falls back to the console stream. Returns
        $null when there is nothing to read, so a hook invoked by hand degrades
        to a no-op instead of throwing. #>
    if ([string]::IsNullOrWhiteSpace($raw)) {
        $raw = [Console]::In.ReadToEnd()
    }
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    try { return $raw | ConvertFrom-Json } catch { return $null }
}

function Get-RepoRoot {
    # The hooks live in <repo>/.claude/hooks/.
    return (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
}

function Get-TargetPaths($payload) {
    <#  Every path a write-shaped tool call would touch. Edit/Write carry
        file_path; MultiEdit carries edits[].file_path in some versions. #>
    $out = @()
    if ($null -eq $payload) { return $out }
    $ti = $payload.tool_input
    if ($null -eq $ti) { return $out }
    if ($ti.file_path)   { $out += $ti.file_path }
    if ($ti.notebook_path) { $out += $ti.notebook_path }
    if ($ti.edits) { foreach ($e in $ti.edits) { if ($e.file_path) { $out += $e.file_path } } }
    return $out | Where-Object { $_ } | Select-Object -Unique
}

function To-RepoRelative($absolute, $repo) {
    <#  Repo-relative POSIX path, or $null when the target is outside the
        repository. Comparison is case-insensitive: Windows folds case and a
        guard that can be bypassed by capitalisation is not a guard. #>
    try { $full = [System.IO.Path]::GetFullPath($absolute) } catch { return $null }
    $prefix = $repo.TrimEnd('\') + '\'
    if (-not $full.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) { return $null }
    return $full.Substring($prefix.Length).Replace('\', '/')
}

function Get-LedgerTier($repoRelative, $repo) {
    <#  The tier recorded for a path, or $null when it has no row. #>
    $ledger = Join-Path $repo 'LEDGER.tsv'
    if (-not (Test-Path $ledger)) { return $null }
    foreach ($line in [System.IO.File]::ReadLines($ledger)) {
        $cells = $line -split "`t"
        if ($cells.Count -ge 2 -and $cells[0] -eq $repoRelative) { return $cells[1] }
    }
    return $null
}

function Deny($message) {
    # Exit 2 is the blocking code: stderr is fed back to Claude as the reason.
    [Console]::Error.WriteLine($message)
    exit 2
}

function Advise($message) {
    # Non-blocking: surfaced to Claude as extra context for the next turn.
    $payload = @{
        hookSpecificOutput = @{
            hookEventName    = 'PostToolUse'
            additionalContext = $message
        }
    }
    $payload | ConvertTo-Json -Depth 5 -Compress | Write-Output
    exit 0
}
