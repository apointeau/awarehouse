import os
from codecs import open

from setuptools import setup, find_packages

from awarehouse import __version__

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()
with open(os.path.join(here, "requirement.txt")) as f:
    install_requires = [entry for entry in f]

setup(
    name="awarehouse",
    version=__version__,

    description="Awarehouse is a distributed smart file manager",
    long_description=long_description,

    url="https://github.com/apointeau/awarehouse",
    download_url="https://github.com/apointeau/awarehouse.git",

    author="Antoine POINTEAU",
    author_email="web.pointeau@gmail.com",

    license="GNU GENERAL PUBLIC LICENSE V3",

    classifiers=[
        "Development Status :: 1 - Planning",

        "Intended Audience :: End Users/Desktop",
        "Topic :: Desktop Environment :: File Managers",

        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5"
    ],

    keywords="file manager smart classifier",

    packages=find_packages(),

    install_requires=install_requires,

    extras_require={},

    entry_points={
        'console_scripts': [
            'awarehouse=awarehouse.cli.__main__:main'
        ]
    },
)
