""" test_sf.py """
import os
import sys
from io import StringIO
import pytest

# Import the main function from cli.sf
lib_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, lib_path)

from cli.sf import main # pylint: disable=C0413

@pytest.mark.parametrize("mock_argv, expected_output", [
    (['sf.py', 'TestName'], "following arguments are required"),
    # (['sf.py'], "required arguments"),
])
def test_main(mocker, mock_argv, expected_output):
    """Test the main function with and without a name argument."""
    # Mock sys.stdout
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    mock_stderr = mocker.patch('sys.stderr', new_callable=StringIO)
    # Mock sys.argv
    mocker.patch('sys.argv', new=mock_argv)

    main()
    # assert mock_stdout.getvalue().strip() == expected_output
    output = mock_stdout.getvalue().strip()
    print ("STDOUT:", output)
    errout = mock_stderr.getvalue().strip()
    print ("STDERR:", errout)
    # assert expected_output in output, (
    # f"Expected substring '{expected_output}' not found in '{output}'")
    