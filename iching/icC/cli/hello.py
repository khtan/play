""" cli/hello.py """
import sys
import os

# Add the lib directory to the path so we can import it
lib_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, lib_path)
from common.core import greet # pylint: disable=C0413

def main():
    """ Main function for the CLI tool """
    print(f"lib_path: {lib_path}")
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    print(greet(name))

if __name__ == "__main__":
    main()
