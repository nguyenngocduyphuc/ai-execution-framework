# Task: Scaffold FastAPI Service with Tests & Docker

```yaml
task:
  title: "Scaffold FastAPI Service with Tests & Docker"
  owner: "Nam Pham"
  executor: "AI Agent (Claude/Cursor)"
  goal: "Generate production-ready FastAPI service with 80%+ test coverage & Dockerfile."
  business_reason: "Standardize microservice creation to reduce onboarding time from 2 days to 2 hours."
  repo_path: "/Users/phuongnam/02.AI/NP_AI_macos/16.AI_Execution_Framework/examples/python_app_factory/"
  priority: "P1"
  status: "To Do"
```

## Acceptance Criteria
- [ ] Project structure matches `templates/project_template.md`
- [ ] `main.py` implements 3 endpoints (GET, POST, health)
- [ ] `tests/` contains ≥ 5 unit tests
- [ ] `pytest` passes with ≥ 80% coverage
- [ ] `ruff check` & `mypy` pass with 0 errors
- [ ] `Dockerfile` builds successfully

## Verification
```bash
pytest tests/ -v --cov=src --cov-report=term-missing
ruff check .
mypy src/
docker build -t myservice .
```

## Execution Plan
1. **Read**: Scan `templates/project_template.md` & `AGENTS.md`.
2. **Scaffold**: Generate `src/main.py`, `tests/test_main.py`, `Dockerfile`, `requirements.txt`.
3. **Lint**: Run `ruff check .` & `mypy src/`. Fix errors.
4. **Test**: Run `pytest`. Add tests until coverage ≥ 80%.
5. **Docker**: Build & verify container runs.
6. **Evidence**: Attach coverage report, lint output, Docker log.

## Evidence
- [ ] Coverage report attached
- [ ] Lint output attached
- [ ] Docker build log attached

## Stop Rules
- [ ] Destructive action (overwriting existing service)
- [ ] Docker daemon unavailable
- [ ] Scope exceeds 3 endpoints

## Summary
[Write summary after execution]
