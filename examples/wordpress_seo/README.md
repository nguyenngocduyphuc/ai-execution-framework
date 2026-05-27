# Example: WordPress SEO Pipeline

> **Demo**: How AXF standardizes SEO article generation & publishing for `phamducphuongnam.com`.

## 🎯 Goal
Automate SEO article creation, Yoast validation, and WordPress publishing using AI agents while maintaining full verification & evidence.

## 📋 Workflow
1. **Research**: AI scans keyword database & competitor content.
2. **Draft**: AI generates article following `master-template-v813`.
3. **Validate**: AI runs `p8_publish_gate.py` (12 gates).
4. **Fix**: AI auto-fixes Yoast violations.
5. **Publish**: AI pushes to WordPress via REST API.
6. **Verify**: AI runs post-publish SEO audit.
7. **Evidence**: AI attaches gate report, publish log, Lighthouse score.

## 🛠️ Files
- `task.md` — Sample task definition
- `verify_example.py` — Verification script (checks frontmatter, keyphrase, meta)
- `evidence_sample.md` — Sample evidence output

## ▶️ How to Run
1. Read `AGENTS.md` (Universal Agent Contract).
2. Open `task.md` & fill in your specific goal.
3. Execute sequentially.
4. Run `python verify_example.py` to validate.
5. Attach evidence using `templates/evidence_template.md`.

---
*This example proves AXF works for real-world SEO pipelines.*
