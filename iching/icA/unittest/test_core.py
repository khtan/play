# unittest/test_core.py
import unittest
import sys
import os

# Add the lib directory to the path so we can import it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.core import greet, add

class TestCore(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
