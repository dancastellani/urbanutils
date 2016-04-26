import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "urbanutils",
    version = "0.1.0",
    author = "Daniel Castellani",
    author_email = "daniel.castellani@nyu.edu",
    description = ("A library of utilities to work with urban data. "),
    license = "MIT",
    keywords = "urban data profiling cleaning curation",
    url = "https://github.com/dancastellani/urban_utils",
    packages=['urban_utils', 'test'],
    excludes=['test'],
    long_description=read('README.rst'),

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],

    install_requires=[
        'pandas'
    ],
)