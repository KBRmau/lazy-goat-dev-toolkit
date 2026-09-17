# Copy this repo's custom skills, always-on rules, and Graphify sessionEnd hook
# into the current user's Cursor home. Does not touch agency-* or mcp.json.

$ErrorActionPreference = "Stop"
$Repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$Cursor = Join-Path $HOME ".cursor"

$pairs = @(
    @{ Src = Join-Path $Repo "skills\auto-work"; Dst = Join-Path $Cursor "skills\auto-work" }
    @{ Src = Join-Path $Repo "skills\humanizer"; Dst = Join-Path $Cursor "skills\humanizer" }
)

foreach ($p in $pairs) {
    New-Item -ItemType Directory -Force -Path $p.Dst | Out-Null
    Copy-Item -Path (Join-Path $p.Src "*") -Destination $p.Dst -Recurse -Force
}

Copy-Item -Path (Join-Path $Repo "rules\*.mdc") -Destination (Join-Path $Cursor "rules") -Force
$legacyRag = Join-Path $Cursor "rules\reference-codebases-rag.mdc"
if (Test-Path $legacyRag) { Remove-Item $legacyRag -Force }

$hooksDir = Join-Path $Cursor "hooks"
New-Item -ItemType Directory -Force -Path $hooksDir | Out-Null
Copy-Item -Path (Join-Path $Repo "hooks\session_end_graphify.py") -Destination $hooksDir -Force

$hookPy = Join-Path $hooksDir "session_end_graphify.py"
Write-Host "Copied skills, rules, and session_end_graphify.py."
Write-Host "Merge sessionEnd into $Cursor\hooks.json. Windows command:"
Write-Host "  python `"$hookPy`""
Write-Host "Optional: set CURSOR_BRAIN_VAULT if the vault is not under Documents or OneDrive."
Write-Host "mcp.json is not copied. Tokens stay local."
