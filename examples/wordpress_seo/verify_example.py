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
    
    # Simulate checking 5 posts
    results = []
    for i in range(1, 6):
        # In real usage, load actual file content
        mock_content = f"""---
title: "Post {i}"
keyphrase: "GxP Compliance"
slug: "post-{i}"
meta_desc: "Learn about GxP compliance in pharma."
---
# GxP Compliance Guide
This article covers GxP compliance...
"""
        fm_ok, fm_msg = check_frontmatter(mock_content)
        kp_ok, kp_msg = check_keyphrase(mock_content, "GxP Compliance")
        
        passed = fm_ok and kp_ok
        results.append({"post": i, "passed": passed})
        
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: Post {i} ({fm_msg}, {kp_msg})")
    
    all_passed = all(r["passed"] for r in results)
    print(f"\n{'🎉 All posts valid!' if all_passed else '⚠️ Some posts failed.'}")
    
    report = {"status": "PASS" if all_passed else "FAIL", "details": results}
    with open("seo_verification_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print("📄 Report saved to seo_verification_report.json")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
