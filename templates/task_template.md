# Task Template

> Use this template to define any task in AXF.
> Fill in all fields. Incomplete tasks will be rejected.

---

## Task Metadata

```yaml
task:
  title: "[Short, actionable title]"
  owner: "Human Owner Name"
  executor: "AI Agent Name (e.g., Claude, Codex)"
  goal: "What needs to be achieved (1-2 sentences)"
  business_reason: "Why this matters to the project/user"
  repo_path: "Path to the repository (e.g., /path/to/repo)"
  priority: "P0 | P1 | P2 | P3"
  status: "To Do | In Progress | Blocked | Done"
```

## Acceptance Criteria

*List the binary pass/fail conditions that must be met.*

- [ ] Criterion 1: e.g., "Unit tests pass with 100% coverage"
- [ ] Criterion 2: e.g., "No linting errors"
- [ ] Criterion 3: e.g., "Documentation updated"

## Verification

*Provide the exact command or steps to verify the task.*

```bash
# Example:
pytest tests/ -v
ruff check .
```

## Execution Plan

*Step-by-step plan for the AI agent.*

1.  **Read**: Scan `AGENTS.md` and relevant docs.
2.  **Plan**: Outline changes.
3.  **Execute**: Make changes sequentially.
4.  **Verify**: Run verification commands.
5.  **Evidence**: Attach logs/screenshots.

## Evidence

*Attach evidence of completion.*

- [ ] Log output attached
- [ ] Screenshot attached (if UI)
- [ ] Test results attached

## Stop Rules

*Conditions that require stopping and escalating to human.*

- [ ] Credentials missing
- [ ] Destructive action required
- [ ] Scope ambiguous
- [ ] Verification fails repeatedly

## Summary

*Final summary of work done.*

[Write summary here]

---
*End of Task Template*
