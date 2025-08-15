"""
Test suite for entirius-pylib-template.

This test suite demonstrates best practices for testing Python libraries
in the Entirius ecosystem.
"""

import pytest
from entirius_pylib_template import (
    hello_entirius,
    process_data,
    validate_input,
    TemplateError,
    TemplateConfig,
)


class TestHelloEntirius:
    """Test cases for hello_entirius function."""
    
    def test_default_greeting(self):
        """Test default greeting without name parameter."""
        result = hello_entirius()
        assert result == "Hello, World! Welcome to Entirius."
    
    def test_custom_name_greeting(self):
        """Test greeting with custom name."""
        result = hello_entirius("Developer")
        assert result == "Hello, Developer! Welcome to Entirius."
    
    def test_empty_string_name(self):
        """Test greeting with empty string name."""
        result = hello_entirius("")
        assert result == "Hello, ! Welcome to Entirius."
    
    def test_invalid_name_type(self):
        """Test that non-string name raises TemplateError."""
        with pytest.raises(TemplateError, match="Name must be a string"):
            hello_entirius(123)


class TestTemplateConfig:
    """Test cases for TemplateConfig dataclass."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = TemplateConfig()
        assert config.max_length == 100
        assert config.min_length == 1
        assert config.allowed_chars == r"[a-zA-Z0-9_-]"
        assert config.strip_whitespace is True
    
    def test_custom_config(self):
        """Test custom configuration values."""
        config = TemplateConfig(
            max_length=50,
            min_length=5,
            allowed_chars=r"[a-zA-Z]",
            strip_whitespace=False
        )
        assert config.max_length == 50
        assert config.min_length == 5
        assert config.allowed_chars == r"[a-zA-Z]"
        assert config.strip_whitespace is False
    
    def test_invalid_length_config(self):
        """Test that max_length < min_length raises TemplateError."""
        with pytest.raises(TemplateError, match="max_length must be greater than or equal to min_length"):
            TemplateConfig(max_length=5, min_length=10)


class TestValidateInput:
    """Test cases for validate_input function."""
    
    def test_valid_input_default_config(self):
        """Test validation with valid input and default config."""
        assert validate_input("test_value") is True
        assert validate_input("Test123") is True
        assert validate_input("a-b_c") is True
    
    def test_invalid_input_default_config(self):
        """Test validation with invalid input and default config."""
        assert validate_input("") is False  # Too short
        assert validate_input("a" * 101) is False  # Too long
        assert validate_input("test@value") is False  # Invalid character
        assert validate_input("test value") is False  # Space not allowed
    
    def test_valid_input_custom_config(self):
        """Test validation with custom configuration."""
        config = TemplateConfig(min_length=3, max_length=10, allowed_chars=r"[a-z]")
        assert validate_input("test", config) is True
        assert validate_input("abcdefghij", config) is True
    
    def test_invalid_input_custom_config(self):
        """Test validation with custom configuration."""
        config = TemplateConfig(min_length=3, max_length=10, allowed_chars=r"[a-z]")
        assert validate_input("ab", config) is False  # Too short
        assert validate_input("abcdefghijk", config) is False  # Too long
        assert validate_input("Test", config) is False  # Uppercase not allowed
    
    def test_whitespace_stripping(self):
        """Test whitespace stripping behavior."""
        config = TemplateConfig(strip_whitespace=True)
        assert validate_input("  test  ", config) is True
        
        config = TemplateConfig(strip_whitespace=False)
        assert validate_input("  test  ", config) is False  # Space not in allowed chars
    
    def test_non_string_input(self):
        """Test that non-string input raises TemplateError."""
        with pytest.raises(TemplateError, match="Value must be a string"):
            validate_input(123)


class TestProcessData:
    """Test cases for process_data function."""
    
    def test_process_string_data(self):
        """Test processing string data."""
        result = process_data("test_value")
        
        assert result["input_type"] == "str"
        assert result["processed_data"] == "test_value"
        assert result["valid"] is True
        assert result["length"] == 10
        assert "config_used" in result
    
    def test_process_string_with_whitespace(self):
        """Test processing string data with whitespace."""
        result = process_data("  test  ")
        
        assert result["processed_data"] == "test"
        assert result["length"] == 4
    
    def test_process_list_data(self):
        """Test processing list data."""
        data = ["test1", "test2", "invalid@value"]
        result = process_data(data)
        
        assert result["input_type"] == "list"
        assert result["total_items"] == 3
        assert result["valid_items"] == 2
        assert result["valid"] is False
        assert len(result["processed_data"]) == 3
        
        # Check individual items
        assert result["processed_data"][0]["valid"] is True
        assert result["processed_data"][1]["valid"] is True
        assert result["processed_data"][2]["valid"] is False
    
    def test_process_dict_data(self):
        """Test processing dictionary data."""
        data = {"valid_key": "value1", "invalid@key": "value2"}
        result = process_data(data)
        
        assert result["input_type"] == "dict"
        assert result["total_keys"] == 2
        assert result["valid_keys"] == 1
        assert result["valid"] is False
        
        # Check processed data structure
        assert "valid_key" in result["processed_data"]
        assert "invalid@key" in result["processed_data"]
        assert result["processed_data"]["valid_key"]["key_valid"] is True
        assert result["processed_data"]["invalid@key"]["key_valid"] is False
    
    def test_process_list_with_non_string_item(self):
        """Test that list with non-string items raises TemplateError."""
        data = ["valid", 123, "also_valid"]
        with pytest.raises(TemplateError, match="List items must be strings"):
            process_data(data)
    
    def test_process_dict_with_non_string_key(self):
        """Test that dict with non-string keys raises TemplateError."""
        data = {123: "value", "valid_key": "value"}
        with pytest.raises(TemplateError, match="Dictionary keys must be strings"):
            process_data(data)
    
    def test_process_unsupported_data_type(self):
        """Test that unsupported data types raise TemplateError."""
        with pytest.raises(TemplateError, match="Unsupported data type"):
            process_data(123)
    
    def test_process_with_custom_config(self):
        """Test processing with custom configuration."""
        config = TemplateConfig(max_length=5, min_length=2)
        result = process_data("toolong", config)
        
        assert result["valid"] is False
        assert result["config_used"]["max_length"] == 5
        assert result["config_used"]["min_length"] == 2


class TestIntegration:
    """Integration test cases."""
    
    def test_complete_workflow(self):
        """Test complete workflow with all functions."""
        # Create custom config
        config = TemplateConfig(max_length=20, min_length=3)
        
        # Test data
        test_data = ["valid", "too_long_invalid_value", "ok"]
        
        # Process data
        result = process_data(test_data, config)
        
        # Verify results
        assert result["total_items"] == 3
        assert result["valid_items"] == 2
        
        # Test individual validation
        for item_data in result["processed_data"]:
            expected_valid = validate_input(item_data["value"], config)
            assert item_data["valid"] == expected_valid
    
    def test_error_handling_consistency(self):
        """Test that error handling is consistent across functions."""
        # All functions should raise TemplateError for type issues
        with pytest.raises(TemplateError):
            validate_input(123)
        
        with pytest.raises(TemplateError):
            hello_entirius(123)
        
        with pytest.raises(TemplateError):
            process_data(123)