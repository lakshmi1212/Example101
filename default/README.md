# Math Operations Example

This repository implements basic math operations (addition, subtraction) with production-ready tests and CI/CD workflow integration.

## Usage

- Source code is in `src/math_operations.py`
- Tests are in the `tests/` folder

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests:

```
pytest tests/
```

## Workflow

- CI runs on push to `Feature1` and pull requests to `main`
- Test reports are generated in `reports/`

## Files

- `src/math_operations.py`: Business logic
- `tests/test_add.py`: Addition tests
- `tests/test_subtract.py`: Subtraction tests
- `default/math.json`: Workflow metadata
- `default/requirements.txt`: Python dependencies
