# Example101: Math Operations

## Overview
This repository implements basic math operations (addition, subtraction) and provides comprehensive pytest-based tests. CI integration is ready for GitHub Actions.

## Folder Structure
- `src/`: Production Python code
- `tests/`: Pytest test files
- `default/`: Documentation, requirements, and meta files

## Usage
```
from src.math_operations import add, subtract
result = add(2, 3)
result2 = subtract(5, 2)
```

## Running Tests
```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow
See `.github/workflows/ci.yml` for pipeline details. All test results are saved in `reports/` and uploaded to S3.

## Requirements
See `default/requirements.txt` for dependencies.
