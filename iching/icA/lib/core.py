# lib/core.py
from typing import TypeVar
HaveAddOperator = TypeVar('HaveAddOperator', int, float, str, bytes)
T1 = HaveAddOperator
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: T1, b: T1) -> T1:
    return a + b
