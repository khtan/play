from setuptools import setup, find_packages

setup(
    name="icA",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello=cli.hello:main',
        ],
    },
)
