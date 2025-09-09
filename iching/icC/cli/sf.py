""" View hexagrams on Windows """
import sys
import os
import logging
from argparse import ArgumentParser, SUPPRESS, RawDescriptionHelpFormatter
from  typing import List
# constants
PROGRAM = 'icC/cli/sf.py'

# argparser
ap = ArgumentParser(
    prog=PROGRAM,
    formatter_class=RawDescriptionHelpFormatter,
    description=__doc__,
    add_help=False,
    epilog="""
Notes:
Sample Usage:
"""
)
required = ap.add_argument_group('required arguments')
required.add_argument('-x', '--hexa',
    type=int, choices=range(1, 65), nargs='+', required=True, help='Hexagram numbers 1-64')
optional = ap.add_argument_group('optional arguments')
optional.add_argument('-h', '--help', action='help', default=SUPPRESS,
                      help='show this help message and exit')

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
from lib.core import view_file # pylint: disable=C0413

def to_padded_string(n: int) -> str:
    """ Convert a number to a zero-padded string """
    return f"{n:02}"

def get_hexagram_path(n: int) -> str:
    """ Get the path to the hexagram image """
    hexname = to_padded_string(n)
    return r"I:\My Drive\lib-home\religion\iching\iching-cards" + "\\" + hexname + ".jpg"

def main() -> None:
    """ Main function for the CLI tool """
    # logger.debug("lib_path: {}", lib_path)
    logger.debug("lib_path: %s", lib_path)
    args: List[str] = sys.argv
    if len(args) < 2:
        ap.print_help()
        sys.exit(1)
    else:
        options=ap.parse_args(args[1:])
        for hexagram_num in options.hexa:
            hexpath: str = get_hexagram_path(int(hexagram_num))
            view_file(hexpath)

if __name__ == "__main__":
    main()
# EOF
