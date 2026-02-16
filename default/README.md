# Example101: Math Operations

## Overview
This project provides basic math operations (addition and subtraction) via Python functions and includes comprehensive pytest test suites.

## Folder Structure
- `src/`: Contains production code.
    - `math_operations.py`: Implements `add` and `subtract` functions.
- `tests/`: Contains test files.
    - `test_add.py`: Tests for addition.
    - `test_subtract.py`: Tests for subtraction.
- `default/`: Project documentation and configuration.
    - `README.md`: This file.
    - `requirements.txt`: Python dependencies.
    - `math.json`: CI metadata file.

## Usage
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
3. Run tests:
   ```bash
   pytest tests/
   ```

## CI Workflow
- All tests are executed via GitHub Actions using `.github/workflows/ci.yml`.
- Reports are generated in `reports/` (junit and html).

## Python Version
- 3.10

## Requirements
See `default/requirements.txt` for dependencies.
