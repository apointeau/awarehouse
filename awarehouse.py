#! /usr/bin/env python

# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-22T16:54:20+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: a42_warehouse.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-09T23:46:10+01:00

import os
import sys
import argparse

from awarehouse import AWContext
from awarehouse import cli

def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    cparser = subparsers.add_parser("config", help="config help")
    cli.config.create_sub_parser(cparser)

    sparser = subparsers.add_parser("storage", help="storage help")
    cli.storage.create_sub_parser(sparser)

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    awc = AWContext(os.environ.get("AWAREHOUSE_CONF", None))
    args.func(awc, args)

if __name__ == "__main__":
    main()
