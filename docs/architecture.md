# AXF Architecture

> **Standardized structure for AI-Human collaboration.**

This document outlines the technical architecture and directory layout of the AI Execution Framework.

## 🏗️ High-Level Design

AXF is designed as a **repository-based framework**. The repo itself is the "control plane".
*   **Stateless Agents**: AI agents do not store state locally. They read from the repo and write evidence back to it.
*   **Git-Centric**: All changes are tracked via Git. The repo history is the audit trail.
*   **CLI-Driven**: Bootstrap and verification are handled via CLI scripts, making them IDE-agnostic.

## 📂 Directory Layout

```text
ai-execution-framework/
│
├── docs/                   # Documentation & Philosophy
│   ├── philosophy.md       # Core principles
│   ├── architecture.md     # This file
│   └── governance.md       # Rules & policies
│
├── bootstrap/              # Environment Setup
│   ├── macos.sh            # macOS bootstrap script
│   ├── windows.ps1         # Windows bootstrap script
│   └── linux.sh            # Linux bootstrap script
│
├── config/                 # Configuration
│   ├── routes.json         # Agent routing rules
│   ├── agents.json         # Agent definitions
│   ├── tools.json          # Tool configurations
│   └── environments.json   # Env variables & paths
│
├── templates/              # Standardized Templates
│   ├── task_template.md    # Task definition format
│   ├── project_template.md # Project kickoff format
│   └── evidence_template.md# Evidence attachment format
│
├── verification/           # Verification Scripts
│   ├── verify_environment.py # Check env health
│   ├── verify_task.py      # Check task completion
│   └── verify_routes.py    # Check agent routing
│
├── scripts/                # Utility Scripts
│   └── (automation tools)
│
├── examples/               # Real-World Examples
│   ├── wordpress_seo/      # SEO pipeline example
│   ├── python_app_factory/ # Python dev example
│   ├── automation_project/ # Automation example
│   └── pharma_validation_docs/ # Pharma compliance example
│
├── AGENTS.md               # Universal Agent Contract (SSoT)
├── README.md               # Project Overview
├── LICENSE                 # MIT License
└── CONTRIBUTING.md         # Contribution Guidelines
```

## 🔁 Execution Flow

1.  **Bootstrap**: User runs `bootstrap/*.sh` to setup environment.
2.  **Onboard**: AI agent reads `AGENTS.md` to learn the contract.
3.  **Task**: Human/AI defines task using `templates/task_template.md`.
4.  **Execute**: AI agent follows the workflow: Read -> Plan -> Code -> Verify.
5.  **Verify**: `verification/` scripts run to check success.
6.  **Evidence**: AI attaches evidence using `templates/evidence_template.md`.
7.  **Done**: Task marked complete in tracking system (Asana/GitHub).

## 🔒 Security & Governance

*   **Credentials**: Never stored in repo. Loaded via `.env` or system keychain.
*   **Destructive Actions**: Blocked by default. Require explicit human approval.
*   **Audit Trail**: Git history + Evidence files provide full traceability.

---
*Architecture designed for scale, safety, and standardization.*
