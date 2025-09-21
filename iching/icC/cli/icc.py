""" Show hexagram and trigram characters """
import os
import sys
import logging
from os import getenv
from argparse import ArgumentParser, SUPPRESS, RawDescriptionHelpFormatter
from typing import List
# from lib.core_classes import IChingConfig

# Constants
PROGRAM = 'icC/cli/icc.py'
EPILOG = """
Notes: TBD
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
    optional = ap.add_argument_group('optional arguments')
    optional.add_argument('-x', '--hexa',
        type=int, choices=range(1, 65), nargs='+', metavar="1..64",
        help='Hexagram numbers 1-64')
    optional.add_argument('-t', '--tri',
        type=int, choices=range(0, 8), nargs='+', metavar="0..7",
        help='Trigram numbers 0-7')
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
    from lib.core import get_hexagram_unicode, get_trigram_unicode, load_json  # pylint: disable=C0415

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
    # config: IChingConfig = cresult.ok
    # cards_lib_root = config['cards_dir']
    outstr: str = "outstr:"
    if options.hexa is not None:
        for hexagram_num in options.hexa:
            r = get_hexagram_unicode(hexagram_num)
            if r.is_error():
                logger.error("get_hexagram_unicode failed with error: %s", r.error)
            else:
                outstr = outstr + str(r.ok)
    if options.tri is not None :
        for trigram_num in options.tri:
            r = get_trigram_unicode(trigram_num)
            if r.is_error():
                logger.error("get_trigram_unicode failed with error: %s", r.error)
            else:
                outstr = outstr + str(r.ok)
    logger.debug("Output: %s", outstr)
    sys.stdout.buffer.write(outstr.encode('utf-8', errors='replace'))    
    sys.stdout.flush()
    # print(outstr)

if __name__ == "__main__":
    main()
