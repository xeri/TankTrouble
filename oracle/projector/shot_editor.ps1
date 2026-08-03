# Gate C: projector ground-truth screenshot of the shipped editor.
# Technique notes (2026-08-04):
#  - PrintWindow is BLACK for Flash Player 32 (direct-to-screen GDI) --
#    only CopyFromScreen works, so the window is pinned TOPMOST and each
#    capture is validated (stage corner must be white) with retries, which
#    survives a busy desktop.
#  - The projector truncates its command-line URL around MAX_PATH (~260
#    chars): initCode must stay short. gatec_maze.json holds a small REAL
#    corpus maze (2 tanks + 2 crates) chosen to fit; the full Gauntlet
#    initCode (300 b64 chars) arrives truncated and must not be used here.
Add-Type -AssemblyName System.Drawing
Add-Type -Namespace GC1 -Name U -MemberDefinition '[DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int cmd); [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h, IntPtr after, int x, int y, int cx, int cy, uint flags); [DllImport("user32.dll")] public static extern bool GetClientRect(IntPtr h, out RECT r); [DllImport("user32.dll")] public static extern bool ClientToScreen(IntPtr h, ref POINT p); public struct RECT { public int L, T, R, B; } public struct POINT { public int X, Y; }'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$init = Get-Content "$root\oracle\editor-visual\gatec_maze.json" | ConvertFrom-Json
$inner = "u=7&n=testuser01&t=$($init.title)&d=$($init.d)&s=1"
$b64 = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes($inner))
$swf = "$root\srv\includes\mazeCreator_v0.3.swf"
$arg = "`"$swf`?initCode=$b64`""
if (($swf.Length + 10 + $b64.Length) -gt 255) { Write-Error "URL too long for the projector (MAX_PATH truncation)"; exit 1 }
$proc = Start-Process -FilePath "$PSScriptRoot\flashplayer_32_sa.exe" -ArgumentList $arg -PassThru
Start-Sleep -Seconds 6
$h = (Get-Process -Id $proc.Id).MainWindowHandle
[GC1.U]::ShowWindow($h, 1) | Out-Null
[GC1.U]::SetWindowPos($h, [IntPtr](-1), 1180, 620, 0, 0, 0x0051) | Out-Null
Start-Sleep -Milliseconds 1200
$cr = New-Object GC1.U+RECT; [GC1.U]::GetClientRect($h, [ref]$cr) | Out-Null
$cp = New-Object GC1.U+POINT; [GC1.U]::ClientToScreen($h, [ref]$cp) | Out-Null
$cw = $cr.R - $cr.L; $ch = $cr.B - $cr.T
$saved = $false
for ($i = 0; $i -lt 25 -and -not $saved; $i++) {
    $bmp = New-Object System.Drawing.Bitmap $cw, $ch
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.CopyFromScreen((New-Object System.Drawing.Point($cp.X, $cp.Y)), [System.Drawing.Point]::Empty, (New-Object System.Drawing.Size($cw, $ch)))
    $corner = $bmp.GetPixel(660, 380)
    if ($corner.R -gt 240 -and $corner.G -gt 240 -and $corner.B -gt 240) {
        $bmp.Save("$PSScriptRoot\projector_editor.png")
        Write-Output "attempt $i valid -- saved projector_editor.png (${cw}x${ch})"
        $saved = $true
    } else { Start-Sleep -Milliseconds 400 }
}
Stop-Process $proc -Force
if (-not $saved) { Write-Error "no valid capture (desktop contention?)"; exit 1 }
