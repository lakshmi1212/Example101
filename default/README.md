# Example101: Math Operations

This project provides basic math operations (addition, subtraction) with production-level automated testing and CI/CD integration.

## Folder Structure
- `src/`: Source code for math operations
- `tests/`: Pytest test cases for math operations
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI metadata for workflow generation

## Usage
```python
from src.math_operations import add, subtract
print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
```

## Running Tests
```bash
pip install -r default/requirements.txt
pytest tests/
```

## CI/CD
- Workflow file: `.github/workflows/ci.yml`
- Trigger: Pushes to `Feature1`, PRs to `main`
- Reports: HTML and JUnit XML in `reports/`
