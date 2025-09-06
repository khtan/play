""" cli/sf.py """
import sys
import os
from  typing import List

# Add the lib directory to the path so we can import it
lib_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, lib_path)

from lib.core import greet # pylint: disable=C0413

def main() -> None:
    """ Main function for the CLI tool """
    print(f"lib_path: {lib_path}")    
    args: List[str] = sys.argv
    name: str = args[1] if len(args) > 1 else "SFWorld"
    print(greet(name))

if __name__ == "__main__":
    main()
