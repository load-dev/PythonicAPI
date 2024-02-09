from setuptools import setup, find_packages
import os

VERSION = '1.0'
DESCRIPTION = 'PythonicAPI (pnapi) is a python package that simplifies web API creation with flask or other modules. It provides functions for server-side tasks. With pnapi, you can build web APIs faster and easier.'

# Setting up
setup(
    name="PythonicAPI",
    version=VERSION,
    author="LOAD",
    author_email="<load@load-dev.xyz>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['json', 'mysql-connector-python'],
    keywords=['python', 'api', 'pythonic api', 'flask superstructure', 'flask', 'sockets', "professional", "requests"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)