""" test_sf.py 
 This implementation is probably not correct because it actually calls 
 the main function which is not mocked.
 The side effect of bringing up the .jpg file is observed. 
 This makes the test dependent on its evironment.
"""
import os
import sys
import logging
from io import StringIO
import pytest

# Import the main function from cli.sf
lib_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, lib_path)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
from cli.icf import main # pylint: disable=C0413

@pytest.mark.parametrize("mock_argv, expected_output", [
    # first element is the script name, and not used, hence 
    (['icf.py', '-x 1'], ""), # one correct arg
    # (['icf.py', 'TestName'], "following arguments are required"), # one incorrect arg
    (['icf.py'], "required arguments"), # zero arg
])
def test_main(mocker, mock_argv, expected_output):
    """Test the main function with and without a name argument.
       ToDo: this parameterized test should be refactored into error and non error cases.
       The error case should examine the return code and stderr output. 
          The stdout should not have any value
       The non error case should expect nothing in stdout and stderr but return code should be 0.
          It should additionally check that the expected side effect (opening a jpg file) occurred.
    """
    # Mock sys.stdout
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    mock_stderr = mocker.patch('sys.stderr', new_callable=StringIO)
    # Mock sys.argv
    mocker.patch('sys.argv', new=mock_argv)
    try:
        main()
    except SystemExit as e:
        logger.debug("SystemExit with code: %s", e.code)
        # We expect a SystemExit with code 1 for error cases
        if len(mock_argv) < 2:
            assert e.code == 1

    output = mock_stdout.getvalue().strip()
    logger.debug("STDOUT: %s", output)
    errout = mock_stderr.getvalue().strip()
    logger.debug("STDERR: %s", errout)
    if output and "not found" in output:
        pytest.xfail("Env: check cards_dir setting in config file exists")
    assert expected_output in output, (
        f"Expected output '{expected_output}' but got '{output}'")

def test_out():
    """Test the main function output."""
    print("This is test_out")# This is a placeholder for an actual test case
    assert True
