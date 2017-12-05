#! /usr/bin/env python3

from setuptools import setup, find_packages
from awarehouse import __version__

PACKAGE_NAME = "awarehouse"

with open('README.rst') as f:
    README = f.read()


setup(
    name=PACKAGE_NAME,
    version=__version__,
    license="GNU GENERAL PUBLIC LICENSE V3",
    url="https://github.com/apointeau/awarehouse",
    download_url="https://github.com/apointeau/awarehouse.git",
    author="Antoine POINTEAU",
    author_email="web.pointeau@gmail.com",
    description="",
    long_description=README,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'awarehouse = awarehouse.cli.__main__:main'
        ]
    },
    zip_safe=False
)
