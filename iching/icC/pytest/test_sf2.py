""" test_sf2.py """
import os
import sys
from unittest.mock import patch
import pytest

# from io import StringIO

# Import the main function from cli.sf
lib_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, lib_path)

from cli.icf import main # pylint: disable=C0413

def test_no_arguments(capsys):
    """Test case 1: No arguments provided"""
    # Mock sys.argv to simulate no arguments
    with patch.object(sys, 'argv', ['sf.py']):
        with pytest.raises(SystemExit) as exc_info:
            main()

        # Check that it exits with code 1
        assert exc_info.value.code == 1

        # Check that help was printed
        captured = capsys.readouterr()
        assert "required arguments" in captured.out
        assert "--hexa" in captured.out

def test_correct_argument():
    """Test case 2: One correct argument (-x 1)
        Need improvement: expected_path can change
    """
    # Mock the view_file function to track calls
    with patch('lib.core.view_file') as mock_view:
        # Mock sys.argv to simulate correct argument
        with patch.object(sys, 'argv', ['sf.py', '-x', '1']):
            main()

            # Check that view_file was called with the correct path
            expected_path = r"I:\My Drive\lib-home\religion\iching\iching-cards\01.jpg"
            mock_view.assert_called_once_with(expected_path)

def test_incorrect_argument(capsys):
    """Test case 3: One incorrect argument (hello)"""
    # Mock sys.argv to simulate incorrect argument
    with patch.object(sys, 'argv', ['sf.py', 'hello']):
        with pytest.raises(SystemExit) as exc_info:
            main()

        # Check that it exits with a non-zero code (argparse typically uses 2 for errors)
        assert exc_info.value.code != 0

        # Check that an error message was printed
        captured = capsys.readouterr()
        assert "error" in captured.err.lower() or "unrecognized arguments" in captured.err.lower()
