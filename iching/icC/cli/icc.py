""" Show hexagram and trigram characters """
import os
import sys
import logging
import platform
from os import getenv
from argparse import ArgumentParser, SUPPRESS, RawDescriptionHelpFormatter
from typing import List
from expression import Error, Ok, Result
# from lib.core_classes import IChingConfig

# Constants
PROGRAM = 'icC/cli/icc.py'
EPILOG = """
Notes: TBD
Sample Usage: TBD
"""
# internal functions
def check_encoding_and_advice() -> Result[None, str]:
    """
    Check whether sys.stdout.encoding is UTF-8.
    If not, print a warning with advice for Linux and Windows shells.
    """
    encoding = sys.stdout.encoding
    if encoding and isinstance(encoding, str) and "utf" in str(encoding).lower():
        return Ok(None) # ✅ Good encoding, nothing to do

    # Build warning message
    msg_lines = ["⚠️  Warning: Your terminal does not appear to use UTF-8 encoding."]
    msg_lines.append(f"Detected encoding: {encoding!r}")

    system = platform.system().lower()
    if "linux" in system or "darwin" in system:
        msg_lines.append("💡 On Linux/macOS, try:")
        msg_lines.append("    export LANG=en_US.UTF-8")
        msg_lines.append("    export LC_ALL=en_US.UTF-8")
    elif "windows" in system:
        msg_lines.append("💡 On Windows Command Prompt (cmd.exe), try:")
        msg_lines.append("    chcp 65001")
        msg_lines.append("    set PYTHONIOENCODING=utf-8")
        msg_lines.append("💡 On PowerShell, you may need:")
        msg_lines.append("    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8")
        msg_lines.append("    $env:PYTHONIOENCODING = 'utf-8'")
    else:
        msg_lines.append("💡 Make sure your shell supports UTF-8 output.")
    return Error("\n".join(msg_lines))

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

def output_hexagram_html(hex_numbers, output_file) -> None:
    """ write out the hexagrams in specified html file """
    r = generate_html(hex_numbers, "x", show_num=True, output_file=output_file)
    if r.is_error():
        logger.error("generate_html failed with error: %s", r.error)
    else:
        logger.info("Wrote hexagram HTML to %s", output_file)

# Main function
## globals
### set up logging, then check encoding
logger = setup_logging()
encoding_state = check_encoding_and_advice()
if encoding_state.is_error():
    logger.info(encoding_state.error) # warning and continue
### add lib_path to mport from lib
lib_path = setup_path()
logger.debug("lib_path: %s", lib_path)
from common.core import get_trigram_unicode, load_json  # pylint: disable=C0413
from common.hexagram import get_hexagram_unicode, generate_html   # pylint: disable=C0413

## main
def main() -> None:
    """Main function for the CLI tool"""
    # set up command line parse
    ap = setup_command_parser()
    # parse args and handle the -h case
    args: List[str] = sys.argv
    if len(args) < 2:
        ap.print_help()
        exit(1)

    # parse args and load config file
    options = ap.parse_args(args[1:])
    cresult = load_json(options.configfile)
    if cresult.is_error():
        logger.error("load_json failed with error: %s", cresult.error)
        exit(1)
    logger.info("Loaded config from %s", options.configfile)
    # config: IChingConfig = cresult.ok
    # cards_lib_root = config['cards_dir']
    # loop over -x and -t args and build output string
    outstr: str = ""
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
    print(outstr)
    if options.hexa is not None:
        output_file = "output_hexagrams.html"
        output_hexagram_html(options.hexa, output_file)

if __name__ == "__main__":
    main()
