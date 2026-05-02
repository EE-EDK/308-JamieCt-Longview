# @file run_tests.ps1
# @brief Run lease API and config unit tests locally (no network). Optional pre-commit hook.
# @note Install deps: pip install -r requirements-dev.txt
$ErrorActionPreference = "Stop"
Set-Location (Split-Path $PSScriptRoot -Parent)
python -m pytest test -q @args
exit $LASTEXITCODE
