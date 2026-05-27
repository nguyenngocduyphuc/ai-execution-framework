# AXF Governance

> **Rules of Engagement.**  
> This document defines how the AXF project is managed, how decisions are made, and how contributors interact with the framework.

## 1. Decision Making

AXF follows a **meritocratic, evidence-based** decision-making process.

*   **Proposals**: All changes must be proposed via Pull Request (PR) with a clear description of the problem and solution.
*   **Review**: PRs must be reviewed by at least one maintainer.
*   **Approval**: PRs are merged when:
    *   All checks pass (verification scripts, linting).
    *   Reviewer approves.
    *   No blocking issues remain.

## 2. Code of Conduct

We are building a standard for AI-Human collaboration. Respect is paramount.

*   **Be Constructive**: Feedback should be actionable and specific.
*   **Be Respectful**: Treat all contributors with dignity, regardless of experience.
*   **Be Patient**: AI agents are powerful but can hallucinate. Verify, don't assume.
*   **Zero Tolerance**: Harassment, discrimination, or malicious behavior will result in immediate removal.

## 3. Versioning

AXF follows **Semantic Versioning (SemVer)**.

*   **MAJOR**: Breaking changes to the Universal Agent Contract or directory structure.
*   **MINOR**: New features, templates, or examples (backwards compatible).
*   **PATCH**: Bug fixes, documentation updates.

## 4. Security

*   **Credentials**: Never commit secrets. Use `.env` or system keychains.
*   **Destructive Actions**: Scripts that delete data must require explicit `--force` flags and human confirmation.
*   **Reporting**: Report vulnerabilities to `security@antigravity.dev` (or your contact). Do not open public issues for security flaws.

## 5. Dispute Resolution

If a disagreement arises:

1.  **Discuss**: Open an issue or comment on the PR.
2.  **Escalate**: If unresolved, tag maintainers.
3.  **Decide**: Maintainers have the final say based on what best serves the AXF philosophy.

---
*Governance ensures stability. Philosophy ensures direction.*
