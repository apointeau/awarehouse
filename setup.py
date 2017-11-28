#! /usr/bin/env python3

from setuptools import setup, find_packages
from awarehouse import __version__

PACKAGE_NAME = "awarehouse"

setup(
    name=PACKAGE_NAME,
    version=__version__,
    license="GNU GENERAL PUBLIC LICENSE V3",
    url="",
    download_url="",
    author="Antoine POINTEAU",
    author_email="web.pointeau at gmail dot com",
    description="",
    packages=find_packages(exclude=["tests", "docs"]),
    keywords=['file manager', ''],
    entry_points={
        'console_scripts': [
            'awarehouse = awarehouse.cli.__main__:main'
        ]
    },
)
