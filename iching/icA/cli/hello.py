# cli/hello.py
import sys
import os

# Add the lib directory to the path so we can import it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.core import greet

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    
    print(greet(name))

if __name__ == "__main__":
    main()
