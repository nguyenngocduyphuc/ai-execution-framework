# AI Execution Framework (AXF)

> **Standardize AI & Human Collaboration.**  
> AI-Agent Agnostic. Verification First. Everything-As-Code.

AXF is an open-source framework that transforms AI agents from "chatbots" into **structured execution workers**. It provides a universal contract, templates, and verification tools to ensure AI-assisted work is **observable, reproducible, verifiable, and versioned**.

## 🎯 Core Philosophy

1.  **AI = Execution Worker**: AI doesn't just chat; it executes. Every task follows a strict flow: `Plan -> Task -> Execute -> Verify -> Evidence -> Done`.
2.  **Verification First**: No verification = no completion. Every task must have acceptance criteria, a verification command, and evidence.
3.  **Read Before Write**: AI agents must read context, understand scope, and verify constraints before modifying any file.
4.  **Everything-As-Code**: No tribal knowledge. Workflows, rules, and templates are defined in markdown, config, and scripts.

## 🚀 Quick Start

1.  **Clone the Repo**:
    ```bash
    git clone https://github.com/nguyenngocduyphuc/ai-execution-framework.git
    cd ai-execution-framework
    ```
2.  **Bootstrap Environment**:
    ```bash
    # macOS
    chmod +x bootstrap/macos.sh && ./bootstrap/macos.sh
    # Windows
    powershell -ExecutionPolicy Bypass -File bootstrap/windows.ps1
    # Linux
    chmod +x bootstrap/linux.sh && ./bootstrap/linux.sh
    ```
3.  **Read the Contract**:
    Open `AGENTS.md`. This is the "Constitution" for your AI agent. Read it before starting any task.
4.  **Execute a Task**:
    Use `templates/task_template.md` to define your work. Follow the `Universal Agent Contract`.

## 📁 Repository Structure

| Directory | Purpose |
|-----------|---------|
| `docs/` | Philosophy, Architecture, Governance |
| `bootstrap/` | Environment setup scripts (macOS/Win/Linux) |
| `config/` | Routes, agents, tools, environments config |
| `templates/` | Standardized task, project, and evidence templates |
| `verification/` | Scripts to verify environment and task completion |
| `scripts/` | Utility scripts for automation |
| `examples/` | Real-world usage examples (SEO, Python, Automation) |

## ⚖️ Universal Agent Contract

Every AI agent must follow these rules:

*   **Mandatory**: Read before edit, Verify before report, Keep scope, Preserve evidence.
*   **Forbidden**: Fake execution, Scope creep, Delete history, Leak credentials.
*   **Escalation**: STOP if credentials missing, destructive action required, or scope ambiguous.

See `AGENTS.md` for the full contract.

## 🤝 Contributing

We welcome contributions! Please read `CONTRIBUTING.md` for guidelines.

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---
*Built for the community. By the community.*
