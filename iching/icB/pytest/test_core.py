import sys
import os

# Add the lib directory to the path so we can import it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.core import greet, add

def test_greet():
    assert greet("World") == "Hello, World"

def test_add_int():
    assert add(2, 3) == 5

def test_add_str():
    assert add("Hello", "World") == "HelloWorld"
