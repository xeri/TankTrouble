# SessionStart - point the session at ONE target, and surface the environment
# fault that makes several gates fail rather than skip.
#
# Pure ASCII on purpose: PowerShell writes in the console codepage, and
# non-ASCII reaches the agent as mojibake.

$ErrorActionPreference = 'SilentlyContinue'
# The docs are UTF-8; without this the console codepage mangles every dash.
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$lines = @()

# --- the target, first, because it is what the session is for ---------------
$now = Join-Path $repo 'docs\NOW.md'
if (Test-Path $now) {
    $take = @()
    $on = $false
    foreach ($l in (Get-Content $now -Encoding UTF8)) {
        if ($l -match '^---\s*$') { if ($on) { break } ; continue }
        if ($l -match '^##\s')    { if ($on) { break } ; $on = $true; continue }
        if ($on) { $take += $l }
    }
    $body = ($take -join "`n").Trim()
    if ($body) { $lines += "TARGET (docs/NOW.md):"; $lines += $body }
}

# --- environment ------------------------------------------------------------
if (-not (Test-Path (Join-Path $repo 'archive\includes-tree')) -and
    -not $env:TT_ARCHIVE_ROOT) {
    $lines += ''
    $lines += 'ARCHIVE MISSING - gates A, C1 and S will FAIL (never skip). Create the junction (no admin needed):'
    $lines += '  New-Item -ItemType Junction -Path "' + $repo + '\archive" -Target "C:\Users\eth\websites\_NOT-PART-OF-MAIN-ARCHIVE_swf-recovered-2026-08-02"'
    $lines += '  or set TT_ARCHIVE_ROOT. Offline-only runs must say so: pytest -m "not live"'
}

# --- do not build on these --------------------------------------------------
$f = Join-Path $repo 'docs\FOUNDATIONS.md'
if (Test-Path $f) {
    $text = Get-Content $f -Raw
    $bad = @()
    foreach ($m in [regex]::Matches($text, '(?m)^### (F-\d{2}) \u2014 (.+)$')) {
        $tail = $text.Substring($m.Index, [Math]::Min(1500, $text.Length - $m.Index))
        if ($tail -match '\*\*Status:\*\* falsified') {
            $bad += "  $($m.Groups[1].Value)  $($m.Groups[2].Value)"
        }
    }
    if ($bad) {
        $lines += ''
        $lines += 'FALSIFIED foundations - do not build on these, and do not patch them:'
        $lines += $bad
    }
}

if ($lines) { ($lines -join "`n") | Write-Output }
exit 0
