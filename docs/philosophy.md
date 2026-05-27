# AXF Philosophy

> **AI is not a chatbot. AI is an execution worker.**

This document defines the core principles behind the AI Execution Framework (AXF). These principles guide how humans and AI agents collaborate to deliver technical work.

## 1. AI-Agent Agnostic

AXF does not depend on a specific AI model or vendor.
*   **Goal**: Portability. A workflow defined in AXF should work with Claude, Codex, Cursor, Qwen, or any future agent.
*   **Mechanism**: Standardized markdown contracts, CLI scripts, and environment-agnostic configs.
*   **Benefit**: No vendor lock-in. Future-proof your AI workflows.

## 2. Everything-As-Code

Tribal knowledge is the enemy of scale.
*   **Goal**: Make every workflow, rule, and template explicit and version-controlled.
*   **Mechanism**: Markdown files (`.md`), JSON configs (`.json`), and scripts (`.sh`, `.py`).
*   **Benefit**: Reproducibility. Anyone (human or AI) can clone the repo and understand exactly how to work.

## 3. Verification First

Trust, but verify. Then verify again.
*   **Goal**: Eliminate "hallucinated" completion. A task is not done until it is proven done.
*   **Mechanism**: Every task must have:
    *   **Acceptance Criteria**: Clear, binary pass/fail conditions.
    *   **Verification Command**: A script or command that proves the work is correct.
    *   **Evidence**: Logs, screenshots, or outputs attached to the task.
*   **Benefit**: Quality assurance. Reduces rework and builds trust in AI output.

## 4. Read Before Write

Context is king.
*   **Goal**: Prevent AI agents from making uninformed changes.
*   **Mechanism**: The "Read Before Edit" rule in the Universal Agent Contract. Agents must scan files, understand scope, and check constraints before writing.
*   **Benefit**: Safety. Reduces accidental breakage and scope creep.

## 5. Observable & Reproducible

Black boxes are unacceptable.
*   **Goal**: Every action taken by an AI agent should be logged and traceable.
*   **Mechanism**: Evidence templates, structured logs, and version control.
*   **Benefit**: Auditing. You can trace exactly what happened, why, and who/what did it.

## 6. Bootstrap Philosophy

Zero to Hero in 30 minutes.
*   **Goal**: A new machine or contributor should be operational quickly.
*   **Mechanism**: Automated bootstrap scripts that install dependencies, verify environment, and validate access.
*   **Benefit**: Onboarding speed. No manual setup, no tribal knowledge required.

---
*These principles are non-negotiable. They form the foundation of AXF.*
