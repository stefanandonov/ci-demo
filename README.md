# ci-demo

Small demo project for Week 9 — CI pipeline basics with GitHub Actions.

## Files

- `calculator.py` — two functions: `add`, `subtract`
- `test_calculator.py` — pytest tests for both
- `.github/workflows/ci.yml` — CI pipeline: checkout → set up Python → install deps → run tests

## Run locally

```bash
pip install pytest
pytest -v
```

## Run in GitHub Actions

1. `git init && git add . && git commit -m "init ci-demo"`
2. Push to a new GitHub repo on branch `main`.
3. Open the **Actions** tab — the workflow runs automatically on push.
4. You can also trigger it manually via **Run workflow** (enabled by `workflow_dispatch`).

## Demo: breaking the pipeline on purpose

To show a failing CI run live, edit `calculator.py`:

```python
def add(a, b):
    return a - b  # intentional bug
```

Commit and push. The `test_add` step will fail, and the Actions log will show:

```
test_calculator.py::test_add FAILED
...
E       assert -1 == 5
```

Read the log top-to-bottom, find the first ❌, fix `add` back to `return a + b`,
commit and push again to see it go green.
