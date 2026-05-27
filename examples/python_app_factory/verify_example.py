#!/usr/bin/env python3
"""
AXF Verification Script: Python App Factory Example
Checks if scaffolded service meets structural & testing requirements.
"""

import os
import sys
import json

REQUIRED_FILES = [
    "src/main.py",
    "tests/test_main.py",
    "Dockerfile",
    "requirements.txt",
    "pyproject.toml"
]

def check_structure(path):
    """Check if required files exist."""
    missing = [f for f in REQUIRED_FILES if not os.path.exists(os.path.join(path, f))]
    return len(missing) == 0, missing

def check_tests(path):
    """Run real pytest and check coverage."""
    try:
        # Run pytest with coverage
        result = subprocess.run(
            ["python", "-m", "pytest", "tests/", "-v", "--cov=src", "--cov-report=term-missing"],
            capture_output=True,
            text=True,
            cwd=path
        )
        
        if result.returncode != 0:
            return False, {"error": "Tests failed", "output": result.stdout}
        
        # Parse coverage from output (simple heuristic)
        coverage = 0
        tests_passed = 0
        
        for line in result.stdout.split("\n"):
            if "TOTAL" in line:
                # Example: TOTAL 10 2 80%
                parts = line.split()
                if len(parts) > 2 and "%" in parts[-1]:
                    coverage = int(parts[-1].replace("%", ""))
            if "passed" in line:
                # Example: 3 passed in 0.12s
                try:
                    tests_passed = int(line.split()[0])
                except (IndexError, ValueError):
                    pass
        
        return coverage >= 80 and tests_passed > 0, {"coverage": coverage, "tests_passed": tests_passed}
        
    except FileNotFoundError:
        return False, {"error": "pytest not found. Install via: pip install pytest pytest-cov"}

def check_dockerfile(path):
    """Check if Dockerfile contains required instructions."""
    dockerfile_path = os.path.join(path, "Dockerfile")
    if not os.path.exists(dockerfile_path):
        return False, "Dockerfile missing"
    
    with open(dockerfile_path, "r") as f:
        content = f.read().lower()
    
    required = ["from python", "workdir", "copy", "run pip", "cmd"]
    missing = [r for r in required if r not in content]
    return len(missing) == 0, missing

def main():
    print("🔎 AXF Verification: Python App Factory Example")
    print("=" * 48)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Check structure
    struct_ok, missing = check_structure(base_path)
    print(f"{'✅ PASS' if struct_ok else '❌ FAIL'}: Structure ({'All files present' if struct_ok else f'Missing: {missing}'})")
    
    # Check tests
    test_ok, test_data = check_tests(base_path)
    print(f"{'✅ PASS' if test_ok else '❌ FAIL'}: Tests (Coverage: {test_data['coverage']}%, Passed: {test_data['tests_passed']})")
    
    # Check Dockerfile
    docker_ok, docker_missing = check_dockerfile(base_path)
    print(f"{'✅ PASS' if docker_ok else '❌ FAIL'}: Dockerfile ({'Valid' if docker_ok else f'Missing: {docker_missing}'})")
    
    all_passed = struct_ok and test_ok and docker_ok
    print(f"\n{'🎉 Service scaffold valid!' if all_passed else '⚠️ Scaffold has issues.'}")
    
    report = {
        "status": "PASS" if all_passed else "FAIL",
        "details": {
            "structure": struct_ok,
            "tests": test_data,
            "dockerfile": docker_ok
        }
    }
    
    with open("python_factory_verification_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print("📄 Report saved to python_factory_verification_report.json")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
