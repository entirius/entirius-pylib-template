"""
Entirius PyLib Template - A template for creating Python libraries following Entirius standards.

This is a template module that demonstrates best practices for creating Python libraries
in the Entirius ecosystem, following all established Architecture Decision Records (ADRs).

Version: 1.0.0
Author: Piotr Brzozowski
License: MPL-2.0
"""

__version__ = "1.0.0"
__author__ = "Piotr Brzozowski"
__email__ = "piotr.brzozowski@entirius.com"
__license__ = "MPL-2.0"

from .template import (
    hello_entirius,
    process_data,
    validate_input,
    TemplateError,
    TemplateConfig,
)

__all__ = [
    "hello_entirius",
    "process_data", 
    "validate_input",
    "TemplateError",
    "TemplateConfig",
]