""" cli/sf.py """
import sys
import os
import logging
from  typing import List

# Get the log level from an environment variable, default to 'WARNING'
log_level_name = os.getenv('LOG_LEVEL', 'WARNING').upper()

# Convert the string to the actual logging constant
try:
    log_level: int = getattr(logging, log_level_name)
except AttributeError:
    # Handle the case of an invalid log level name
    log_level: int = logging.WARNING
logging.basicConfig(level=log_level)

# Set up logging
logger = logging.getLogger(__name__)

# Add the lib directory to the path so we can import it
lib_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, lib_path)
from lib.core import greet, view_file # pylint: disable=C0413

def main() -> None:
    """ Main function for the CLI tool """
    # logger.debug("lib_path: {}", lib_path)
    logger.debug("lib_path: %s", lib_path)
    args: List[str] = sys.argv
    name: str = args[1] if len(args) > 1 else "SFWorld"
    print(greet(name))

    view_file(r"I:\My Drive\lib-home\religion\iching\iching-cards\01.jpg")
if __name__ == "__main__":
    main()
