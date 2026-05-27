#!/usr/bin/env python3
"""
AXF Environment Verification Script
Checks if the environment is ready for AI execution.
"""

import sys
import os
import subprocess
import json

def check_command(cmd):
    """Check if a command exists."""
    try:
        subprocess.run([cmd, "--version"], capture_output=True, text=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_python_version():
    """Check Python version >= 3.12."""
    version = sys.version_info
    return version.major == 3 and version.minor >= 12

def check_git():
    """Check if git is installed."""
    return check_command("git")

def check_venv():
    """Check if virtual environment is active."""
    return os.environ.get("VIRTUAL_ENV") is not None

def main():
    print("🔎 AXF Environment Verification")
    print("=" * 40)

    results = {
        "python_version": check_python_version(),
        "git": check_git(),
        "venv": check_venv(),
    }

    for check, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {check}")

    if all(results.values()):
        print("\n🎉 Environment is ready!")
        report = {"status": "PASS", "details": results}
    else:
        print("\n⚠️ Environment has issues. Please fix before proceeding.")
        report = {"status": "FAIL", "details": results}

    # Write report to file
    with open("verification_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print(f"📄 Report saved to verification_report.json")
    return 0 if all(results.values()) else 1

if __name__ == "__main__":
    sys.exit(main())
