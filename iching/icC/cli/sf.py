""" View hexagrams on Windows """
import os
import sys
import logging
from os import getenv
from argparse import ArgumentParser, SUPPRESS, RawDescriptionHelpFormatter
from typing import List
from lib.core_classes import IChingConfig

# Constants
PROGRAM = 'icC/cli/sf.py'
EPILOG = """
Notes: 01 Qian-Initiating, 02 Kun-Responding, 29 Kan-Dark, 30 Li-Bright, 51 Zhen-Action, 52 Gen-Still, 57 Xun-Proceed Humbly, 58 Dui-Joyful
       63 Ji Ji-Already Fulfilled, 64 Wei Ji-Not Yet Fulfilled
Sample Usage: TBD
"""
# internal functions
def setup_logging() -> logging.Logger:
    """Set up logging configuration and return logger instance."""
    log_level_name = getenv('LOG_LEVEL', 'WARNING').upper()
    try:
        log_level = getattr(logging, log_level_name)
    except AttributeError:
        log_level = logging.WARNING
    logging.basicConfig(level=log_level)
    return logging.getLogger(__name__)

def setup_command_parser() -> ArgumentParser:
    """Create and configure command line argument parser."""
    ap = ArgumentParser(
        prog=PROGRAM,
        formatter_class=RawDescriptionHelpFormatter,
        description=__doc__,
        add_help=False,
        epilog=EPILOG
    )
    required = ap.add_argument_group('required arguments')
    required.add_argument('-x', '--hexa',
        type=int, choices=range(1, 65), nargs='+', required=True,
        help='Hexagram numbers 1-64')
    optional = ap.add_argument_group('optional arguments')
    optional.add_argument('-h', '--help', action='help', default=SUPPRESS,
                        help='show this help message and exit')
    optional.add_argument('-c', '--configfile', type=str,
                        help='path to json configuration file, defaulting to config.json',
                        default='config.json')
    return ap

def setup_path() -> str:
    """Add lib directory to Python path and return the path."""
    lib_path = os.path.join(os.path.dirname(__file__), '..')
    sys.path.insert(0, lib_path)
    return lib_path

# Main function
def main() -> None:
    """Main function for the CLI tool"""
    logger = setup_logging()
    ap = setup_command_parser()
    lib_path = setup_path()

    logger.debug("lib_path: %s", lib_path)

    # Import after setting up path
    from lib.core import view_file, load_json  # pylint: disable=C0415

    args: List[str] = sys.argv
    if len(args) < 2:
        ap.print_help()
        exit(1)

    options = ap.parse_args(args[1:])

    cresult = load_json(options.configfile)
    if cresult.is_error():
        logger.error("load_json failed with error: %s", cresult.error)
        exit(1)
    logger.info("Loaded config from %s", options.configfile)
    config: IChingConfig = cresult.ok
    cards_lib_root = config['cards_dir']

    for hexagram_num in options.hexa:
        hexpath: str = get_hexagram_path(cards_lib_root, int(hexagram_num))
        view_file(hexpath)

# Helper functions
def to_padded_string(n: int) -> str:
    """Convert a number to a zero-padded string"""
    return f"{n:02}"

def get_hexagram_path(cards_dir: str, n: int) -> str:
    """Get the path to the hexagram image"""
    hexname = to_padded_string(n)
    jpgname = hexname + ".jpg"
    fullpath = os.path.join(cards_dir, jpgname)
    return fullpath

if __name__ == "__main__":
    main()
