""" lib/core.py """
import os
from typing import TypeVar
HaveAddOperator = TypeVar('HaveAddOperator', int, float, str, bytes)
T1 = HaveAddOperator
def greet(name: str) -> str:
    """ Returns a greeting message """
    return f"Hello, {name}"

def add(a: T1, b: T1) -> T1:
    """ Returns the + of two values """
    return a + b

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
