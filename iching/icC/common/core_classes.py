""" lib/core_classes.py to keep all simple core classes"""
from typing import TypedDict

class IChingConfig(TypedDict):
    """ Configuration for the I Ching CLI tool """
    version: int
    cards_dir: str
