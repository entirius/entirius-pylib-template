# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the entirius-pylib-template codebase.

## Project Overview

This is the **Entirius PyLib Template** - a template for creating Python libraries that follow all Entirius platform standards and Architecture Decision Records (ADRs). This template serves as a reference implementation for creating new Python libraries in the Entirius ecosystem.

**Repository**: https://github.com/entirius/entirius-pylib-template

## Technology Stack

- **Python 3.11+** - Primary programming language (per ADR requirements)
- **Hatchling** - Build backend (per ADR-013)
- **pyproject.toml** - Modern Python packaging (per ADR-009)
- **UV** - Package manager (per ADR-007)
- **Ruff** - Linting and formatting (per ADR-010)
- **mypy** - Type checking
- **pytest** - Testing framework

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode with all extras
uv pip install -e ".[dev,test]"

# Verify installation
python -c "from entirius_pylib_template import hello_entirius; print(hello_entirius('Template'))"
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=entirius_pylib_template --cov-report=term-missing --cov-report=html

# Run specific test file
pytest tests/test_template.py

# Run specific test class
pytest tests/test_template.py::TestHelloEntirius

# Run specific test
pytest tests/test_template.py::TestHelloEntirius::test_default_greeting
```

### Code Quality
```bash
# Format code
ruff format .

# Lint and fix issues
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

## Project Structure

```
entirius-pylib-template/
├── src/
│   └── entirius_pylib_template/
│       ├── __init__.py         # Public API exports
│       └── template.py         # Core implementation
├── tests/
│   ├── __init__.py            # Test package
│   └── test_template.py       # Comprehensive test suite
├── pyproject.toml             # Project configuration (ADR-009)
├── README.md                  # Main documentation
├── LICENSE                    # MPL-2.0 license (ADR-004)
├── CLAUDE.md                  # This file
└── CHANGELOG.md               # Version history (when created)
```

## Core Functions

The template demonstrates best practices with these functions:

1. **hello_entirius(name)** - Basic string processing with validation
2. **validate_input(value, config)** - Input validation with configuration
3. **process_data(data, config)** - Complex data processing for multiple types
4. **TemplateConfig** - Configuration dataclass with validation
5. **TemplateError** - Custom exception handling

## Architecture Decision Records

This template follows ALL established Entirius platform standards:

- **[ADR-004](../docs-entirius/docs/adr/adr-004-mozilla-public-license.md)**: Mozilla Public License 2.0
- **[ADR-007](../docs-entirius/docs/adr/adr-007-uv-python-package-manager.md)**: UV Python Package Manager
- **[ADR-008](../docs-entirius/docs/adr/adr-008-github-repository-naming-conventions.md)**: GitHub Repository Naming (`entirius-pylib-*`)
- **[ADR-009](../docs-entirius/docs/adr/adr-009-pyproject-toml-standard.md)**: pyproject.toml Standard
- **[ADR-010](../docs-entirius/docs/adr/adr-010-ruff-python-linter.md)**: Ruff Python Linter
- **[ADR-011](../docs-entirius/docs/adr/adr-011-kiss-principle.md)**: KISS Principle
- **[ADR-012](../docs-entirius/docs/adr/adr-012-english-language-requirement.md)**: English Language Requirement
- **[ADR-013](../docs-entirius/docs/adr/adr-013-hatchling-build-backend.md)**: Hatchling Build Backend

## Configuration

The project uses pyproject.toml for configuration (per ADR-009):

- **Build system**: Hatchling backend (per ADR-013)
- **Dependencies**: Minimal runtime dependencies (KISS principle)
- **Development tools**: ruff, mypy, pytest with comprehensive configuration
- **Python requirement**: >=3.11
- **License**: MPL-2.0

## Development Guidelines

### Code Standards
- Follow PEP 8 style guide (enforced by ruff)
- Use type hints for all functions (checked by mypy)
- Write comprehensive docstrings with examples
- Maintain test coverage above 90%
- Use meaningful commit messages

### Template Design Principles
- **Simplicity**: Clear, simple API with minimal dependencies (ADR-011)
- **Type Safety**: Full type hints and mypy compliance
- **Testing**: Comprehensive test suite with multiple test classes
- **Documentation**: Clear docstrings with examples
- **Error Handling**: Custom exceptions with clear messages
- **Configuration**: Dataclass-based configuration with validation

### Function Implementation Guidelines
- All public functions must have type hints
- Handle edge cases gracefully with clear error messages
- Raise TemplateError for invalid inputs with descriptive messages
- Use consistent parameter naming across functions
- Include usage examples in docstrings
- Follow dataclass patterns for configuration

## Testing Strategy

The template demonstrates comprehensive testing patterns:

- **Unit tests**: Individual function testing
- **Integration tests**: Cross-function workflow testing
- **Edge case testing**: Empty strings, None values, invalid types
- **Error testing**: Exception handling and error messages
- **Configuration testing**: Custom configuration validation
- **Coverage**: HTML and terminal coverage reports

### Test Organization
- **TestHelloEntirius**: Basic function testing
- **TestTemplateConfig**: Configuration validation
- **TestValidateInput**: Input validation with various configs
- **TestProcessData**: Complex data processing
- **TestIntegration**: End-to-end workflow testing

## Usage as Template

### Creating New Library from Template
1. Copy the entire directory structure
2. Rename `entirius_pylib_template` to your library name
3. Update `pyproject.toml` with new name, description, dependencies
4. Update all imports in `__init__.py` and tests
5. Replace template functions with your implementation
6. Update README.md with your library documentation
7. Update CLAUDE.md with library-specific guidance

### Key Files to Customize
- `src/{library_name}/__init__.py` - Public API exports
- `src/{library_name}/core.py` - Core implementation (rename from template.py)
- `tests/test_core.py` - Test suite (rename from test_template.py)
- `pyproject.toml` - Project metadata and dependencies
- `README.md` - Library documentation
- `CLAUDE.md` - Development guidance

## Integration with Entirius Platform

### Django Services Integration
```bash
# Install in Django services (e.g., entirius-service-ai-gateway)
uv pip install -e ../../pylib/entirius-pylib-template
```

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

## Important Notes for Claude Code

### Development Workflow
- **Always run tests** after making code changes: `pytest`
- **Use proper linting commands**: `ruff check .`, `ruff format .`, `mypy .`
- **Follow template design principles** and maintain API consistency
- **Ensure all ADRs are followed** when making any changes
- **Update version** in pyproject.toml when making changes
- **Maintain backward compatibility** unless major version change

### Package Management
- **Use UV exclusively** per ADR-007: `uv pip install` instead of `pip install`, `uv venv` instead of `python -m venv`
- **Use pyproject.toml** per ADR-009: all configuration in pyproject.toml
- **Use hatchling** per ADR-013: build-backend = "hatchling.build"
- **Follow naming convention** per ADR-008: `entirius-pylib-*` pattern

### Quality Standards
- **Type hints required** for all public functions
- **Comprehensive docstrings** with examples
- **Error handling** with TemplateError for clear error messages
- **Test coverage** above 90% for all code
- **Ruff compliance** for formatting and linting
- **mypy compliance** for type checking

### Security Considerations
- **Input validation** for all public functions
- **No eval() or exec()** usage anywhere
- **Safe string handling** to prevent injection attacks
- **Minimal dependencies** to reduce attack surface
- **No secrets in code** - follow security best practices

## Template Features Demonstration

### Type Hints and Validation
The template shows proper type hints usage:
```python
def validate_input(
    value: str,
    config: Optional[TemplateConfig] = None
) -> bool:
```

### Error Handling
Custom exception usage:
```python
class TemplateError(Exception):
    """Custom exception for template-specific errors."""
    pass
```

### Configuration Pattern
Dataclass with validation:
```python
@dataclass
class TemplateConfig:
    max_length: int = 100
    min_length: int = 1
    
    def __post_init__(self) -> None:
        if self.max_length < self.min_length:
            raise TemplateError("max_length must be greater than or equal to min_length")
```

### Complex Data Processing
Multi-type input handling:
```python
def process_data(
    data: Union[str, List[str], Dict[str, Any]],
    config: Optional[TemplateConfig] = None
) -> Dict[str, Any]:
```

## Common Operations

### Adding New Functions
1. Add function to `src/entirius_pylib_template/template.py`
2. Add function to exports in `src/entirius_pylib_template/__init__.py`
3. Add comprehensive tests in `tests/test_template.py`
4. Update README.md with usage examples
5. Run full test suite and quality checks

### Updating Configuration
1. Update `TemplateConfig` dataclass in `template.py`
2. Update validation in `__post_init__` method
3. Add tests for new configuration options
4. Update docstrings and README

### Making Releases
1. Update version in `pyproject.toml`
2. Run full test suite: `pytest`
3. Run quality checks: `ruff format . && ruff check . && mypy .`
4. Build package: `uv build`
5. Tag release and create GitHub release

## Related Documentation

- Main project documentation: `../docs-entirius/`
- Architecture Decision Records: `../docs-entirius/docs/adr/`
- Other Python libraries: `../pylib/`
- Django services: `../services/`

## Troubleshooting

### Common Issues
- **Import errors**: Ensure library is installed in development mode: `uv pip install -e .`
- **Type checking errors**: Run `mypy .` to check type annotations
- **Test failures**: Run `pytest -v` for detailed test output
- **Build issues**: Ensure pyproject.toml is valid and dependencies are correct

### Performance Considerations
- **Function efficiency**: All functions designed for performance
- **Memory usage**: Efficient string and data processing
- **Type checking**: Zero-overhead runtime type checking

## Support

For questions, issues, or contributions related to this template:

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Main project**: Reference main Entirius project documentation
- **Architecture**: Follow established ADRs for all architectural decisions
- **Templates**: Use this template as reference for new Python libraries