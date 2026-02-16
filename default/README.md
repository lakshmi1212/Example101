# Example101 Math Operations

This repository provides basic math operations (addition and subtraction) with production-ready tests and CI integration.

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

## Testing

Run tests using pytest:

```bash
pytest tests/
```

## CI/CD Workflow

- Automated tests are executed on push and pull requests.
- Reports are generated in JUnit and HTML formats.
- Results are uploaded to S3 for archiving.

See `default/math.json` for workflow meta data.
