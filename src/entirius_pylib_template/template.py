"""
Core template functionality for Entirius PyLib Template.

This module demonstrates best practices for Python library development
in the Entirius ecosystem.
"""

import re
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass


class TemplateError(Exception):
    """Custom exception for template-specific errors."""
    pass


@dataclass
class TemplateConfig:
    """Configuration class for template operations."""
    max_length: int = 100
    min_length: int = 1
    allowed_chars: str = r"[a-zA-Z0-9_-]"
    strip_whitespace: bool = True
    
    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        if self.max_length < self.min_length:
            raise TemplateError("max_length must be greater than or equal to min_length")


def hello_entirius(name: Optional[str] = None) -> str:
    """
    Generate a greeting message for the Entirius platform.
    
    Args:
        name: Optional name to include in greeting. Defaults to "World".
        
    Returns:
        A formatted greeting string.
        
    Example:
        >>> hello_entirius()
        'Hello, World! Welcome to Entirius.'
        >>> hello_entirius("Developer")
        'Hello, Developer! Welcome to Entirius.'
    """
    if name is None:
        name = "World"
    
    if not isinstance(name, str):
        raise TemplateError("Name must be a string")
    
    return f"Hello, {name}! Welcome to Entirius."


def validate_input(
    value: str,
    config: Optional[TemplateConfig] = None
) -> bool:
    """
    Validate input string against configuration rules.
    
    Args:
        value: The string to validate.
        config: Optional configuration. Uses default if not provided.
        
    Returns:
        True if valid, False otherwise.
        
    Raises:
        TemplateError: If value is not a string.
        
    Example:
        >>> validate_input("test_value")
        True
        >>> validate_input("")
        False
        >>> validate_input("a" * 200)
        False
    """
    if not isinstance(value, str):
        raise TemplateError("Value must be a string")
    
    if config is None:
        config = TemplateConfig()
    
    # Strip whitespace if configured
    if config.strip_whitespace:
        value = value.strip()
    
    # Check length constraints
    if len(value) < config.min_length or len(value) > config.max_length:
        return False
    
    # Check allowed characters
    if not re.match(f"^{config.allowed_chars}+$", value):
        return False
    
    return True


def process_data(
    data: Union[str, List[str], Dict[str, Any]],
    config: Optional[TemplateConfig] = None
) -> Dict[str, Any]:
    """
    Process various data types with template logic.
    
    This function demonstrates handling different input types and
    returning structured data following Entirius patterns.
    
    Args:
        data: Input data to process (string, list, or dict).
        config: Optional configuration for processing.
        
    Returns:
        Dictionary with processed results and metadata.
        
    Raises:
        TemplateError: If data type is not supported.
        
    Example:
        >>> result = process_data("test")
        >>> result['input_type']
        'string'
        >>> result['valid']
        True
    """
    if config is None:
        config = TemplateConfig()
    
    result = {
        "input_type": type(data).__name__,
        "processed_at": "timestamp_placeholder",
        "config_used": {
            "max_length": config.max_length,
            "min_length": config.min_length,
        }
    }
    
    if isinstance(data, str):
        result["processed_data"] = data.strip() if config.strip_whitespace else data
        result["valid"] = validate_input(data, config)
        result["length"] = len(result["processed_data"])
        
    elif isinstance(data, list):
        processed_items = []
        valid_items = 0
        
        for item in data:
            if isinstance(item, str):
                processed_item = item.strip() if config.strip_whitespace else item
                is_valid = validate_input(item, config)
                processed_items.append({
                    "value": processed_item,
                    "valid": is_valid,
                    "length": len(processed_item)
                })
                if is_valid:
                    valid_items += 1
            else:
                raise TemplateError(f"List items must be strings, got {type(item)}")
        
        result["processed_data"] = processed_items
        result["total_items"] = len(data)
        result["valid_items"] = valid_items
        result["valid"] = valid_items == len(data)
        
    elif isinstance(data, dict):
        processed_dict = {}
        valid_keys = 0
        
        for key, value in data.items():
            if not isinstance(key, str):
                raise TemplateError("Dictionary keys must be strings")
            
            key_valid = validate_input(key, config)
            processed_key = key.strip() if config.strip_whitespace else key
            
            processed_dict[processed_key] = {
                "original_value": value,
                "key_valid": key_valid,
                "value_type": type(value).__name__
            }
            
            if key_valid:
                valid_keys += 1
        
        result["processed_data"] = processed_dict
        result["total_keys"] = len(data)
        result["valid_keys"] = valid_keys
        result["valid"] = valid_keys == len(data)
        
    else:
        raise TemplateError(f"Unsupported data type: {type(data)}")
    
    return result