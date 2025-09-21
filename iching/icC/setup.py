""" Setup script for the ic package with console scripts."""
from setuptools import setup, find_packages

setup(
    name="icC",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello=cli.hello:main',
            'icf=cli.icf:main',
            'icc=cli.icc:main',
        ],
    },
)
