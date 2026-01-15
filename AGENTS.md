# AGENTS.md

This file contains guidelines and commands for agentic coding agents working in this repository.

## Repository Overview

This is a Python learning repository containing exercises, challenges, and documentation from roadmap.sh and other sources. The repository is organized into:
- `python/before/` - Learning exercises by difficulty level
- `python/challenges/` - Coding challenges with solutions
- `python/roadmapsh/` - Roadmap.sh related exercises
- `python/docs/` - Documentation files

## Development Commands

### Package Management
```bash
# Initialize new project with uv
uv init [project_name]
cd [project_name]

# Add dependencies
uv add [package]
uv add --dev [dev_package]

# Install and run tools
uv tool install [package]
uvx [package]  # Run packages directly
```

### Code Quality
```bash
# Linting and formatting with ruff
ruff check [file]           # Check code style
ruff check [file] --fix     # Auto-fix issues
ruff format [file]          # Format code

# Run on entire directory
ruff check .
ruff format .
```

### Testing
```bash
# Run tests with pytest
pytest [file]               # Run specific test file
pytest [file]::[test_name]  # Run specific test
pytest -v                   # Verbose output
pytest -k "pattern"         # Run tests matching pattern

# Run with coverage
pytest --cov=[module]
```

### Virtual Environment
```bash
# Activate (if using venv)
source ./venv/bin/activate

# Deactivate
deactivate
```

## Code Style Guidelines

### General Principles
- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Write docstrings for functions and classes
- Prefer descriptive variable names in English
- Keep functions focused and small

### Import Organization
```python
# Standard library imports
import os
import sys
from typing import List, Optional

# Third-party imports
import pytest
import requests

# Local imports
from .module import function
```

### Type Hints
```python
# Function signatures
def process_data(data: List[str]) -> Optional[dict]:
    """Process the input data and return results."""
    pass

# Variable annotations
result: int = 42
items: List[str] = []
```

### Function Documentation
```python
def calculate_factorial(number: int) -> int:
    """
    Calculate the factorial of a given number recursively.
    
    Args:
        number: A non-negative integer
        
    Returns:
        The factorial of the input number
        
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
    """
    pass
```

### Error Handling
```python
# Input validation
if not isinstance(number, int):
    raise TypeError("The type of the input is not valid")

if number < 0:
    raise ValueError("The input should be a positive number")

# Exception handling in main code
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
```

### Testing Patterns
```python
# Use pytest for testing
import pytest

# Parametrized tests
@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 2),
    (3, 6),
])
def test_function(input: int, expected: int) -> None:
    assert function(input) == expected

# Exception testing
def test_invalid_input():
    with pytest.raises(TypeError, match="Invalid type"):
        function("invalid")
```

### Code Structure
```python
# File structure
"""
Module docstring explaining purpose.
"""

# Imports
from typing import List, Optional

# Constants
DEFAULT_TIMEOUT = 30

# Functions
def main_function() -> None:
    """Main entry point."""
    pass

if __name__ == "__main__":
    main_function()
```

## Naming Conventions

- **Variables**: `snake_case` (descriptive, e.g., `user_input`, `result_list`)
- **Functions**: `snake_case` (verb-based, e.g., `calculate_factorial`, `process_data`)
- **Classes**: `PascalCase` (noun-based, e.g., `DataProcessor`, `UserManager`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`)
- **Private members**: Prefix with `_` (e.g., `_internal_helper`)

## File Organization

### Challenge Files
```
# 1. Problem description (comments)
# 2. Imports
# 3. Test functions
# 4. Solution functions
# 5. Main execution block
```

### Exercise Files
```
# 1. Module docstring
# 2. Imports
# 3. Implementation
# 4. Example usage (if applicable)
```

## Best Practices

1. **Test-Driven Development**: Write tests before implementation
2. **Type Safety**: Use type hints consistently
3. **Error Handling**: Validate inputs and handle exceptions appropriately
4. **Documentation**: Include docstrings for public functions
5. **Code Quality**: Run `ruff check --fix` and `ruff format` before commits
6. **Testing**: Ensure all tests pass with `pytest`

## Configuration Files

When adding new Python projects, include:
- `pyproject.toml` for project configuration
- `ruff.toml` or ruff config in `pyproject.toml`
- `pytest.ini` if custom pytest configuration needed

## Git Workflow

1. Create feature branches for new exercises
2. Ensure code passes linting and tests
3. Commit with descriptive messages
4. Push and create pull requests for review

## Common Patterns

### Input Validation
```python
def validate_input(data: str) -> None:
    if not isinstance(data, str):
        raise TypeError("Expected string input")
    if not data.strip():
        raise ValueError("Input cannot be empty")
```

### Generator Functions
```python
def number_generator(start: int, end: int):
    """Generate numbers in range."""
    for i in range(start, end + 1):
        yield i
```

### Class Definitions
```python
class DataProcessor:
    """Process data with configurable options."""
    
    def __init__(self, config: dict) -> None:
        self.config = config
    
    def process(self, data: List[Any]) -> List[Any]:
        """Process the input data."""
        return [self._transform(item) for item in data]
```

Remember to run quality checks before submitting changes:
```bash
ruff check --fix .
ruff format .
pytest -v
```