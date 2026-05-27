# AXF Bootstrap Script for Windows
# Usage: powershell -ExecutionPolicy Bypass -File bootstrap/windows.ps1

Write-Host "🚀 AXF Bootstrap (Windows)" -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan

# 1. Check Prerequisites
Write-Host "🔍 Checking prerequisites..." -ForegroundColor Yellow

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "❌ Python not found. Please install Python 3.12+." -ForegroundColor Red
    exit 1
}

# Check Python Version >= 3.12
try {
    $pythonVersion = python --version 2>&1 | Select-String -Pattern "Python (\d+\.\d+)"
    $versionNumber = $pythonVersion.Matches.Groups[1].Value
    $major, $minor = $versionNumber -split '\.'
    
    if ([int]$major -lt 3 -or ([int]$major -eq 3 -and [int]$minor -lt 12)) {
        Write-Host "❌ Python version $versionNumber found. AXF requires Python >= 3.12." -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "⚠️ Could not verify Python version. Proceeding with caution." -ForegroundColor Yellow
}

Write-Host "✅ Prerequisites met (Python $versionNumber)." -ForegroundColor Green

# 2. Setup Virtual Environment
Write-Host "🐍 Setting up virtual environment..." -ForegroundColor Yellow
python -m venv .venv
if (-not (Test-Path ".venv\Scripts\activate.ps1")) {
    Write-Host "❌ Failed to create virtual environment." -ForegroundColor Red
    exit 1
}

# Activate (optional for script, but good for user context)
& .\.venv\Scripts\Activate.ps1

Write-Host "✅ Virtual environment ready." -ForegroundColor Green

# 3. Install Dependencies (if requirements.txt exists)
if (Test-Path "requirements.txt") {
    Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host "✅ Dependencies installed." -ForegroundColor Green
} else {
    Write-Host "⚠️ No requirements.txt found. Skipping dependency installation." -ForegroundColor Yellow
}

# 4. Verify Environment
Write-Host "🔎 Verifying environment..." -ForegroundColor Yellow
python verification/verify_environment.py

Write-Host "🎉 Bootstrap complete! Read AGENTS.md to start." -ForegroundColor Green
