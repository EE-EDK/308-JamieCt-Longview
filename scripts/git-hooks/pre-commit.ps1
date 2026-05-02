# Opt-in pre-commit: from repo root run:
#   git config core.hooksPath scripts/git-hooks
# Requires: pip install -r requirements-dev.txt
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot ".." "..")).Path
Push-Location $repoRoot
try {
    python -m pytest test -q --tb=short
    exit $LASTEXITCODE
} finally {
    Pop-Location
}
