""" lib/core.py containing basic core helper functions """
import os
import json
from typing import TypeVar
from expression import Error, Ok, Result
from common.core_classes import IChingConfig

HaveAddOperator = TypeVar('HaveAddOperator', int, float, str, bytes)
# reminder for error string type
errstr = str # pylint: disable=invalid-name
T1 = HaveAddOperator
def greet(name: str) -> str:
    """ Returns a greeting message """
    return f"Hello, {name}"

def add(a: T1, b: T1) -> T1:
    """ Returns the + of two values """
    return a + b
# region sf functions
def view_file(file_path: str) -> None:
    """ Brings up Windows default app on the file_path """
    try:
        os.startfile(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except (IOError, OSError) as e:
        print(f"IOError or OSError on {file_path}: {e}")
    except Exception as e: # pylint: disable=W0718
        print(f"An unexpected error occurred: {e}")

def load_json(file_path: str) -> Result[IChingConfig, str]:
    """ Loads a JSON file """
    if not os.path.exists(file_path):
        return Error(f"File {file_path} not found")

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            json_str = json.dumps(data)
            config: IChingConfig = json.loads(json_str, object_hook=IChingConfig) # type: ignore
            return Ok(config)
        except json.JSONDecodeError as e:
            return Error(f"Failed to parse JSON from {file_path}: {e}")
        # Break broad-except for FP style
        except Exception as e: # pylint: disable=broad-except
            return Error(f"Unexpected error occurred while loading {file_path}: {e}")
# endregion sf functions
# region sc functions

def get_trigram_unicode(trigram_number: int) -> Result[str, errstr]:
    """ Get the Unicode character for a given trigram number (1-8) """
    if 0 <= trigram_number <= 7:
        return Ok(chr(0x2630 - trigram_number + 7))
    else:
        return Error("Trigram number must be between 0 and 7")
# endregion sc functions
