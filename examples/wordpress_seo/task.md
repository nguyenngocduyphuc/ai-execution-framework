# Task: Audit & Fix Yoast SEO for 5 Draft Posts

```yaml
task:
  title: "Audit & Fix Yoast SEO for 5 Draft Posts"
  owner: "Nam Pham"
  executor: "AI Agent (Codex/Claude)"
  goal: "Ensure 5 draft articles pass all 12 P8 publish gates before WordPress upload."
  business_reason: "Publishing unoptimized content hurts search rankings & compliance."
  repo_path: "/Users/phuongnam/02.AI/NP_AI_macos/8.P8_SEO_Clean/"
  priority: "P1"
  status: "To Do"
```

## Acceptance Criteria
- [ ] All 5 posts have valid YAML frontmatter (title, keyphrase, slug, meta_desc)
- [ ] Exact keyphrase appears in opening paragraph, H1, and ≥1 H2
- [ ] Meta description ≤ 155 chars, contains keyphrase
- [ ] No generic openings ("In today's digital world...")
- [ ] Lighthouse SEO score ≥ 90/100

## Verification
```bash
cd /path/to/P8_SEO_Clean
python scripts/p8_publish_gate.py --batch 1-5 --report
python scripts/p8_yoast_real_fixer.py --dry-run
```

## Execution Plan
1. **Read**: Scan `content/posts/drafts/` for target articles.
2. **Audit**: Run `p8_publish_gate.py` to identify violations.
3. **Fix**: Apply `p8_yoast_real_fixer.py --apply`.
4. **Verify**: Re-run gate check. All 12/12 must pass.
5. **Evidence**: Attach gate report JSON & fixer log.

## Evidence
- [ ] Gate report attached
- [ ] Fixer log attached
- [ ] Screenshot of WordPress draft preview

## Stop Rules
- [ ] API credentials missing for WordPress
- [ ] Destructive action (deleting posts)
- [ ] Scope exceeds 5 posts

## Summary
[Write summary after execution]
