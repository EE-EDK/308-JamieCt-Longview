# 308-Jamie-Ct-3b d-house — Environment Setup
# Usage: powershell -File scripts/setup_env.ps1
# Flags: -Force to rebuild from scratch

param([switch]$Force)

$ErrorActionPreference = "Stop"
$missing = 0

Write-Host "=== 308-Jamie-Ct-3b d-house Environment Setup ===" -ForegroundColor Cyan
Write-Host ""

# --- Toolchain Checks ---

# Check node
try {
    $null = & node --version 2>&1
    Write-Host "[OK] node found" -ForegroundColor Green
} catch {
    Write-Host "[MISSING] node — install from https://nodejs.org/" -ForegroundColor Red
    $missing++
}


# Install Node.js dependencies
if (Test-Path "package.json") {
    if (-Not (Test-Path "node_modules")) {
        Write-Host "Installing Node.js dependencies..." -ForegroundColor Cyan
        npm install
    }
    Write-Host "Node.js dependencies ready." -ForegroundColor Green
}


# --- Summary ---
Write-Host ""
if ($missing -gt 0) {
    Write-Host "WARNING: $missing tool(s) missing. Install before proceeding." -ForegroundColor Yellow
    exit 1
} else {
    Write-Host "Environment ready." -ForegroundColor Green
    exit 0
}
