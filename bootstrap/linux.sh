#!/bin/bash
# AXF Bootstrap Script for Linux
# Usage: chmod +x bootstrap/linux.sh && ./bootstrap/linux.sh

set -e

echo "🚀 AXF Bootstrap (Linux)"
echo "========================"

# 1. Check Prerequisites
echo "🔍 Checking prerequisites..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.12+."
    exit 1
fi

# Check Python Version >= 3.12
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
REQUIRED_VERSION="3.12"
if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python version $PYTHON_VERSION found. AXF requires Python >= 3.12."
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install Git."
    exit 1
fi

echo "✅ Prerequisites met (Python $PYTHON_VERSION)."

# 2. Setup Virtual Environment
echo "🐍 Setting up virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "✅ Virtual environment ready."

# 3. Install Dependencies (if requirements.txt exists)
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    echo "✅ Dependencies installed."
else
    echo "⚠️ No requirements.txt found. Skipping dependency installation."
fi

# 4. Verify Environment
echo "🔎 Verifying environment..."
python3 verification/verify_environment.py

echo "🎉 Bootstrap complete! Read AGENTS.md to start."
