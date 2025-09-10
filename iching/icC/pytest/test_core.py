"""Test cases for lib/core.py"""
import sys
import os

# Add the lib directory to the path so we can import it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.core import greet, add # pylint: disable=C0413

def test_greet():
    """Test the greet function."""
    assert greet("World") == "Hello, World"

def test_add_int():
    """Test the add function with integers."""
    assert add(2, 3) == 5

def test_add_str():
    """Test the add function with strings."""
    assert add("Hello", "World") == "HelloWorld"
