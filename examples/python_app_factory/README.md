# Example: Python App Factory

> **Demo**: How AXF standardizes Python microservice scaffolding & testing.

## 🎯 Goal
Automate creation of production-ready Python services (FastAPI/Flask) with tests, Docker, and CI/CD, ensuring every scaffold passes verification before handoff.

## 📋 Workflow
1. **Spec**: Human defines service requirements (name, framework, endpoints).
2. **Scaffold**: AI generates project structure (`main.py`, `tests/`, `Dockerfile`, `requirements.txt`).
3. **Lint**: AI runs `ruff check` & `mypy`.
4. **Test**: AI runs `pytest` & generates coverage report.
5. **Docker**: AI builds & verifies container.
6. **Verify**: AI runs `verify_example.py` to validate structure & tests.
7. **Evidence**: AI attaches coverage report, Docker build log, lint output.

## 🛠️ Files
- `task.md` — Sample task definition
- `verify_example.py` — Verification script (checks structure, tests, Docker)
- `evidence_sample.md` — Sample evidence output

## ▶️ How to Run
1. Read `AGENTS.md` (Universal Agent Contract).
2. Open `task.md` & fill in your specific goal.
3. Execute sequentially.
4. Run `python verify_example.py` to validate.
5. Attach evidence using `templates/evidence_template.md`.

---
*This example proves AXF works for real-world Python development pipelines.*
