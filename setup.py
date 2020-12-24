from setuptools import setup

import os
import re

version = "1.1.0"

setup(
    zip_safe=True,
    name="desafe",
    version=version,
    author="pjon",
    url="https://github.com/joncastro/SafeInCloud",
    py_modules=["desafe"],
    description="An utility to decrypt Safe in Cloud password files",
    use_2to3=True,
    license="LICENSE",
    install_requires=["pycryptodome", "xmltodict", "passlib", "docopt"],
    entry_points={"console_scripts": ["desafe = desafe:main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
)
