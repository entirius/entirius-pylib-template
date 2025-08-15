# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2025-08-15

### Added
- Initial template implementation following Entirius ADR standards
- Core template functionality with `hello_entirius`, `validate_input`, and `process_data` functions
- `TemplateConfig` dataclass for configurable validation
- `TemplateError` custom exception class
- Comprehensive test suite with pytest
- Type hints support with mypy configuration
- Code formatting and linting with ruff (ADR-010)
- Modern Python packaging with pyproject.toml (ADR-009)
- UV package manager support (ADR-007)
- Hatchling build backend (ADR-013)
- Mozilla Public License 2.0 (ADR-004)
- Comprehensive README with usage examples
- CLAUDE.md guidance for AI-assisted development
- GitHub repository naming convention compliance (ADR-008)
- English language requirement compliance (ADR-012)
- KISS principle adherence (ADR-011)

### Documentation
- Complete API reference documentation
- Django integration examples
- Development workflow instructions
- Architecture Decision Records compliance
- Code quality guidelines
- Testing strategy documentation

### Infrastructure
- pytest configuration with coverage reporting
- mypy type checking configuration
- ruff linting and formatting configuration
- Comprehensive test coverage (>90%)
- Build and distribution setup

[Unreleased]: https://github.com/entirius/entirius-pylib-template/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/entirius/entirius-pylib-template/releases/tag/v1.0.0