# PreToolUse - BLOCK. Evidence is read-only, everywhere.
#
# A capture that looks wrong is data about the capture. Correcting it destroys
# the only copy of an observation, and no gate can detect the loss afterwards.
# This is the one class of mistake in this project that is genuinely
# irreversible, so it is enforced rather than requested.

. (Join-Path $PSScriptRoot 'lib.ps1')

$payload = Read-HookInput (@($input) -join "`n")
if ($null -eq $payload) { exit 0 }

# Directory names anywhere in the path that mark read-only evidence.
$evidenceSegments = @(
    'archive',
    'evidence',
    'manualevidence',
    'archive-cleaned',
    'pages-recovered',
    'variants',
    'tanktrouble.com',
    'tanktrouble.com-offline'
)

foreach ($target in (Get-TargetPaths $payload)) {
    try { $full = [System.IO.Path]::GetFullPath($target) } catch { continue }
    $segments = $full.Replace('/', '\').Split('\')

    $hit = $null
    foreach ($s in $segments) {
        if ($s -like '_NOT-PART-OF-MAIN-ARCHIVE_*') { $hit = $s; break }
        if ($evidenceSegments -contains $s.ToLowerInvariant()) { $hit = $s; break }
    }
    if (-not $hit) { continue }

    # archive-cleaned/classification/*.tsv are the masks: written material that
    # lives beside the captures. They are reviewable evidence, not captures.
    if ($full -match '[\\/]archive-cleaned[\\/]classification[\\/]') { continue }

    Deny @"
BLOCKED: $target is read-only evidence (matched '$hit').

Evidence is cited, never corrected - a capture that looks wrong is data about
the capture, and editing it destroys the only copy of an observation.

If bytes need to reach the reconstruction, copy them in through the placement
tools, which re-verify sha256 on arrival:
  python tools/place_assets.py --promote
If the observation itself is wrong, that is a finding: record it in
DECISIONS.md, do not rewrite the source.
"@
}

exit 0
