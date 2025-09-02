# cli/sf.py
import sys
import os
from  typing import List

# Add the lib directory to the path so we can import it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.core import greet

def main() -> None:
    args: List[str] = sys.argv
    name: str = args[1] if len(args) > 1 else "SFWorld"
    print(greet(name))

if __name__ == "__main__":
    main()
