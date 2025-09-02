import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
from typing import Any

# Import the main function from cli.sf
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'cli'))
from sf import main

class TestSF(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)  # Mock stdout to capture print output
    @patch('sys.argv', new=['sf.py', 'TestName'])  # Mock sys.argv
    def test_main_with_name(self, mock_argv: Any, mock_stdout: StringIO) -> None:
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, TestName")

    @patch('sys.stdout', new_callable=StringIO)  # Mock stdout to capture print output
    @patch('sys.argv', new=['sf.py'])  # Mock sys.argv with no additional arguments
    def test_main_without_name(self, mock_argv: Any, mock_stdout: StringIO) -> None:
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, SFWorld")

if __name__ == '__main__':
    unittest.main()