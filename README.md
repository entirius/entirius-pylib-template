# Entirius PyLib Template

A template for creating Python libraries following Entirius standards and Architecture Decision Records (ADRs).

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This template demonstrates best practices for creating Python libraries in the Entirius ecosystem, following all established Architecture Decision Records (ADRs).

## Features

- 🚀 Modern Python packaging with `pyproject.toml` (ADR-009)
- ⚡ UV package manager support (ADR-007)
- 🏗️ Hatchling build backend (ADR-013)
- 🧪 Comprehensive test suite with pytest
- 📝 Type hints with mypy
- 🔧 Code formatting with ruff
- 📊 Code coverage reporting
- 📚 Comprehensive documentation
- 🔒 Mozilla Public License 2.0 (ADR-004)

## Installation

### Using UV (Recommended - ADR-007)

```bash
# Install from local development
uv pip install -e .

# Install with development dependencies
uv pip install -e ".[dev,test]"

# Install all optional dependencies
uv pip install -e ".[all]"
```

### Using pip

```bash
# Install from local development
pip install -e .

# Install with development dependencies
pip install -e ".[dev,test]"
```

## Quick Start

```python
from entirius_pylib_template import hello_entirius, process_data, TemplateConfig

# Basic greeting
message = hello_entirius("Developer")
print(message)  # Output: Hello, Developer! Welcome to Entirius.

# Process string data
result = process_data("example_data")
print(result["valid"])  # Output: True

# Use custom configuration
config = TemplateConfig(max_length=50, min_length=3)
result = process_data(["valid", "x"], config)
print(result["valid_items"])  # Output: 1
```

## API Reference

### Core Functions

#### `hello_entirius(name: Optional[str] = None) -> str`

Generate a greeting message for the Entirius platform.

**Parameters:**
- `name` (optional): Name to include in greeting. Defaults to "World".

**Returns:**
- Formatted greeting string.

**Example:**
```python
>>> hello_entirius()
'Hello, World! Welcome to Entirius.'
>>> hello_entirius("Developer")
'Hello, Developer! Welcome to Entirius.'
```

#### `validate_input(value: str, config: Optional[TemplateConfig] = None) -> bool`

Validate input string against configuration rules.

**Parameters:**
- `value`: The string to validate.
- `config` (optional): Validation configuration. Uses default if not provided.

**Returns:**
- `True` if valid, `False` otherwise.

#### `process_data(data: Union[str, List[str], Dict[str, Any]], config: Optional[TemplateConfig] = None) -> Dict[str, Any]`

Process various data types with template logic.

**Parameters:**
- `data`: Input data to process (string, list, or dict).
- `config` (optional): Processing configuration.

**Returns:**
- Dictionary with processed results and metadata.

### Configuration

#### `TemplateConfig`

Configuration class for template operations.

**Attributes:**
- `max_length: int = 100` - Maximum allowed string length
- `min_length: int = 1` - Minimum required string length  
- `allowed_chars: str = r"[a-zA-Z0-9_-]"` - Regex for allowed characters
- `strip_whitespace: bool = True` - Whether to strip whitespace

### Exceptions

#### `TemplateError`

Custom exception for template-specific errors.

## Development

### Environment Setup

```bash
# Create virtual environment with UV
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
uv pip install -e ".[dev,test]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=entirius_pylib_template --cov-report=html

# Run specific test file
pytest tests/test_template.py

# Run specific test
pytest tests/test_template.py::TestHelloEntirius::test_default_greeting
```

### Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Fix linting issues
ruff check . --fix

# Type checking
mypy .

# Run all quality checks
ruff format . && ruff check . && mypy .
```

### Building and Publishing

```bash
# Build package
uv build

# Check distribution
twine check dist/*

# Upload to PyPI (maintainers only)
twine upload dist/*
```

## Architecture Decisions

This template follows established Entirius platform standards:

- **[ADR-004](../docs-entirius/docs/adr/adr-004-mozilla-public-license.md)**: Mozilla Public License 2.0
- **[ADR-007](../docs-entirius/docs/adr/adr-007-uv-python-package-manager.md)**: UV Python Package Manager
- **[ADR-008](../docs-entirius/docs/adr/adr-008-github-repository-naming-conventions.md)**: GitHub Repository Naming (`entirius-pylib-*`)
- **[ADR-009](../docs-entirius/docs/adr/adr-009-pyproject-toml-standard.md)**: pyproject.toml Standard
- **[ADR-010](../docs-entirius/docs/adr/adr-010-ruff-python-linter.md)**: Ruff Python Linter
- **[ADR-011](../docs-entirius/docs/adr/adr-011-kiss-principle.md)**: KISS Principle
- **[ADR-013](../docs-entirius/docs/adr/adr-013-hatchling-build-backend.md)**: Hatchling Build Backend

## Directory Structure

```
entirius-pylib-template/
├── src/
│   └── entirius_pylib_template/
│       ├── __init__.py         # Public API exports
│       └── template.py         # Core implementation
├── tests/
│   ├── __init__.py            # Test package
│   └── test_template.py       # Test suite
├── pyproject.toml             # Project configuration (ADR-009)
├── README.md                  # This file
├── LICENSE                    # MPL-2.0 license
├── CLAUDE.md                  # Claude Code guidance
└── CHANGELOG.md               # Version history
```

## Integration with Django

### Django Models Example

```python
from django.db import models
from entirius_pylib_template import validate_input, TemplateConfig

class ExampleModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    
    def clean(self):
        config = TemplateConfig(max_length=100, min_length=3)
        if not validate_input(self.slug, config):
            raise ValidationError("Invalid slug format")
```

### Django Serializers Example

```python
from rest_framework import serializers
from entirius_pylib_template import process_data, TemplateConfig

class ExampleSerializer(serializers.Serializer):
    data = serializers.CharField()
    
    def validate_data(self, value):
        config = TemplateConfig(max_length=50)
        result = process_data(value, config)
        if not result["valid"]:
            raise serializers.ValidationError("Data validation failed")
        return result["processed_data"]
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the code standards
4. Add tests for new functionality
5. Run quality checks: `ruff format . && ruff check . && mypy . && pytest`
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the Mozilla Public License 2.0. See the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

## Support

- **Issues**: [GitHub Issues](https://github.com/entirius/entirius-pylib-template/issues)
- **Documentation**: [Entirius Documentation](https://docs.entirius.com)
- **Repository**: [GitHub Repository](https://github.com/entirius/entirius-pylib-template)

---

**Made with ❤️ by the Entirius Team**