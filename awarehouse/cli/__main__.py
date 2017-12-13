#! /usr/bin/env python

# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-22T16:54:20+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: a42_warehouse.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-23T00:51:31+01:00

import sys
import argparse
sys.path.insert(0, "./lib")

from awarehouse import AWContext
from awarehouse.cli import filesys
from awarehouse.cli import cleaner
from awarehouse.cli import storage


def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    filesys.create_sub_parser(subparsers)
    cleaner.create_sub_parser(subparsers)
    storage.create_sub_parser(subparsers)

    return parser


def main():
    parser = create_parser()
    if len(sys.argv) > 2:
        sys.argv.insert(2, '--')
    args = parser.parse_args()

    awc = AWContext()
    return args.handler(awc, args)


if __name__ == "__main__":
    main()
