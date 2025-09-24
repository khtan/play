""" test_unicode.py """
import sys
import logging
from pytest import fail
# region globals
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def test_02() -> None: 
    """ xxx """
    logger.info("Stdout encoding: %s", sys.stdout.encoding)

def test_00() -> None: # _unicode_char_print
    """ Test Unicode output """
    hexagram: str = chr(0x4DC0)
    try:
        encoding: str | None = sys.stdout.encoding
        if encoding is None:
            fail("Skipping test_00 due to stdout having no encoding")
        elif "utf" not in str(encoding).lower():
            fail("Skipping test_00 due to stdout having non-UTF encoding")
        print(f"PHex: {hexagram}")
    except NameError as ne: # pylint: disable=W0718
        print(f"NameError: >{ne}<")
        fail(f"NameError: >{ne}<")        
    except UnicodeEncodeError as uee: # pylint: disable=W0718
        print(f"UnicodeEncodeError: >{uee}<")
        fail(f"UnicodeEncodeError: >{uee}<")        
    except Exception as e: # pylint: disable=W0718
        print(f"EPHex: >{e}<")
        fail(f"EPHex: {e}")

def test_01() -> None: # _unicode_char_info
    """ Test Unicode output """
    hexagram: str = chr(0x4DC0)
    try:
        logger.info("LHex: %s", hexagram)
    except Exception as e: # pylint: disable=W0718
        logger.info("ELHex: %s", e)
