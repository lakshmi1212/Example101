# Example101: Math Operations

This repository provides basic math operations (addition and subtraction) with comprehensive pytest coverage and CI/CD workflow integration.

## Math Operations
- **add(a, b)**: Returns the sum of a and b.
- **subtract(a, b)**: Returns the result of a minus b.

## Folder Structure
- `src/` : Source code for math operations
- `tests/` : Pytest-based test cases for all operations
- `default/` : Project configuration files (README, requirements, metadata)

## Running Tests
1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run tests:
   ```bash
   pytest tests/
   ```

## CI/CD Workflow
- Workflow file: `.github/workflows/ci.yml`
- Triggers on push to `Feature1` and pull requests to `main`
- Generates JUnit and HTML test reports in the `reports/` directory

## Metadata
- See `default/math.json` for workflow and project configuration metadata.
