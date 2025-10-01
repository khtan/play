"""Test cases for lib/core.py"""
import json
# import sys
import os
from common.core_classes import IChingConfig
# Add the lib directory to the path so we can import it
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from common.core import greet, add, load_json # pylint: disable=C0413
from common.hexagram import generate_html # pylint: disable=C0413
# region tests
def test_greet():
    """Test the greet function."""
    assert greet("World") == "Hello, World"

def test_add_int():
    """Test the add function with integers."""
    assert add(2, 3) == 5

def test_add_str():
    """Test the add function with strings."""
    assert add("Hello", "World") == "HelloWorld"

def test_load_json_ok_self_created_file():
    """Test the load_json function with a sample JSON file."""
    # Create a temporary JSON file for testing
    test_json_path = 'test_config.json'
    test_data = {
        "version": 1,
        "cards_dir": "I:/My Drive/lib-home/religion/iching/iching-cards"
    }
    with open(test_json_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f)

    # Test loading the JSON file
    cresult = load_json(test_json_path)
    if cresult.is_ok():
        config: IChingConfig = cresult.ok
        assert config['version'] == 1
        assert config['cards_dir'] == "I:/My Drive/lib-home/religion/iching/iching-cards"
    else:
        assert False, f"load_json failed with error: {cresult.error}"
    # Clean up the temporary file
    os.remove(test_json_path)
def test_load_json_ok_external_file():
    """Test the load_json function with a sample JSON file."""
    # Sensitive: assumes pytest starts at root of project
    test_json_path = 'tests/test_core_config.json'

    # Test loading the JSON file
    cresult = load_json(test_json_path)
    if cresult.is_ok():
        config: IChingConfig = cresult.ok
        assert config['version'] == 1
        assert config['cards_dir'] == "I:/My Drive/lib-home/religion/iching/iching-cards"
    else:
        assert False, f"load_json failed with error: {cresult.error}"
def test_load_json_missingfile():
    """Test the load_json function with a sample JSON file."""

    # Test loading the JSON file
    file_path = "nonexistent.json"
    cresult = load_json(file_path)
    if cresult.is_ok():
        config: IChingConfig = cresult.ok
        assert config['version'] == 1
        assert config['cards_dir'] == "I:/My Drive/lib-home/religion/iching/iching-cards"
    else:
        assert cresult.error == f"File {file_path} not found"
def test_generate_small_html():
    """Test the generate_html function."""
    hex_numbers = [1, 63, 64, 2]
    of = "output_hexagrams.html"
    result = generate_html(hex_numbers, show_num=True, output_file=of, display_type="circle")
    if result.is_error():
        assert False, f"generate_html failed with error: {result.error}"
    assert os.path.exists(of)
def test_generate_large_html():
    """Test the generate_html function."""
    hex_numbers = list(range(1,65))
    of = "output_hexagrams.html"
    result = generate_html(hex_numbers, show_num=True, output_file=of, display_type="circle")
    if result.is_error():
        assert False, f"generate_html failed with error: {result.error}"
    assert os.path.exists(of)
def test_generate_small_all_html():
    """Test the generate_html function."""
    hex_numbers = [1, 63, 64, 2]
    of = "output_hexagrams_all.html"
    result = generate_html(hex_numbers, show_num=True, output_file=of, display_type="all")
    if result.is_error():
        assert False, f"generate_html failed with error: {result.error}"
    assert os.path.exists(of)
def test_generate_large_all_html():
    """Test the generate_html function."""
    hex_numbers = list(range(1,65))
    of = "output_hexagrams_all.html"
    result = generate_html(hex_numbers, show_num=True, output_file=of, display_type="all")
    if result.is_error():
        assert False, f"generate_html failed with error: {result.error}"
    assert os.path.exists(of)

#endregion tests
