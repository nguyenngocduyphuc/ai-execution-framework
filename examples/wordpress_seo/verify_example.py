#!/usr/bin/env python3
"""
AXF Verification Script: WordPress SEO Example
Checks if draft posts meet basic SEO requirements.
"""

import os
import sys
import json
import re

def check_frontmatter(content):
    """Check for required YAML frontmatter fields."""
    required = ["title", "keyphrase", "slug", "meta_desc"]
    match = re.search(r"---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "No frontmatter found"
    
    fm = match.group(1)
    for field in required:
        if field not in fm:
            return False, f"Missing field: {field}"
    return True, "Frontmatter valid"

def check_keyphrase(content, keyphrase):
    """Check if keyphrase appears in opening, H1, and H2."""
    if not keyphrase:
        return False, "No keyphrase defined"
    
    # Check opening (first 100 words)
    opening = content.split("\n")[5:15]  # Approximate opening
    if not any(keyphrase.lower() in line.lower() for line in opening):
        return False, "Keyphrase missing in opening"
    
    # Check H1/H2
    headings = re.findall(r"^#{1,2}\s+(.*)", content, re.MULTILINE)
    if not any(keyphrase.lower() in h.lower() for h in headings):
        return False, "Keyphrase missing in headings"
    
    return True, "Keyphrase placement valid"

def main():
    print("🔎 AXF Verification: WordPress SEO Example")
    print("=" * 45)
    
    # Read real sample file
    sample_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_post.md")
    if not os.path.exists(sample_path):
        print("❌ FAIL: sample_post.md not found")
        return 1
        
    with open(sample_path, "r") as f:
        content = f.read()
    
    # Extract keyphrase from frontmatter
    kp_match = re.search(r"keyphrase:\s*\"(.*?)\"", content)
    keyphrase = kp_match.group(1) if kp_match else None
    
    fm_ok, fm_msg = check_frontmatter(content)
    kp_ok, kp_msg = check_keyphrase(content, keyphrase)
    
    passed = fm_ok and kp_ok
    results = [{"post": "sample_post.md", "passed": passed}]
    
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"{status}: {sample_path} ({fm_msg}, {kp_msg})")
    
    print(f"\n{'🎉 Sample post valid!' if passed else '⚠️ Sample post failed.'}")
    
    report = {"status": "PASS" if passed else "FAIL", "details": results}
    with open("seo_verification_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print("📄 Report saved to seo_verification_report.json")
    return 0 if passed else 1

if __name__ == "__main__":
    sys.exit(main())
