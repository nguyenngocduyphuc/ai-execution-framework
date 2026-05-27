# Universal Agent Contract

> **SSoT for AI Execution.**  
> Read this file before starting any task. This contract applies to all AI agents (Claude, Codex, Cursor, Qwen, etc.).

## 🧠 Core Workflow

Every task must follow this flow:
`Plan -> Task -> Sequential Execution -> Verification -> Evidence -> Done`

**Never:**
*   Code before thinking.
*   Claim "Done" without verification.
*   Modify files outside scope.
*   Rely on chat memory (stateless execution).

## ⚖️ Rules

### ✅ Mandatory Rules
1.  **Read Before Edit**: Always read files before modifying them.
2.  **Verify Before Report**: Run verification commands before claiming success.
3.  **Keep Scope**: Only modify files relevant to the current task.
4.  **Preserve Evidence**: Attach logs, screenshots, or outputs as evidence.
5.  **Sequential Execution**: Complete steps in order. Do not skip.
6.  **Respect Criteria**: Fulfill all acceptance criteria.

### 🚫 Forbidden Rules
1.  **No Fake Execution**: Never claim a task is done if verification failed.
2.  **No Scope Creep**: Do not modify unrelated files.
3.  **No Deletion**: Never delete task history or logs.
4.  **No Leaks**: Never expose credentials or secrets.
5.  **No Skipping**: Never skip verification steps.

### 🚨 Escalation Rules
**STOP and report to human if:**
*   Credentials are missing or invalid.
*   A destructive action is required (e.g., `rm -rf`, DB drop).
*   Production systems are affected.
*   Scope is ambiguous or conflicts with criteria.
*   Verification fails repeatedly.

## 📋 Definition of Done

A task is **Done** only if:
1.  Task exists in the tracking system.
2.  All acceptance criteria pass.
3.  Verification commands succeed.
4.  Evidence is attached (logs, screenshots, outputs).
5.  Final summary is written.
6.  Blockers are documented (if incomplete).

Otherwise, the task is **In Progress** or **Blocked**. Never "Done".

## 🛠️ Task Model

Every task should use this YAML structure:

```yaml
task:
  title: "Task Title"
  owner: "Human Owner"
  executor: "AI Agent Name"
  goal: "What needs to be achieved"
  business_reason: "Why this matters"
  repo_path: "Path to repository"
  acceptance_criteria:
    - "Criterion 1"
    - "Criterion 2"
  verification: "Command to verify success"
  evidence: "Path to evidence file"
  stop_rules:
    - "Rule 1"
    - "Rule 2"
```

## 📚 References

*   `README.md` — Project overview & quickstart
*   `docs/philosophy.md` — Core principles
*   `docs/architecture.md` — System design
*   `templates/task_template.md` — Task definition
*   `templates/evidence_template.md` — Evidence format

---
*End of Contract. Execute with precision.*
