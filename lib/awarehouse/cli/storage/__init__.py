# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:32:48+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: __init__.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T01:30:37+01:00

import sys
import argparse

import add
import info

def call_handler(awc, args):
    parser = argparse.ArgumentParser(
        prog="{0} {1}".format(sys.argv[0], "storage")
    )
    subparsers = parser.add_subparsers()

    add.create_sub_parser(subparsers)
    info.create_sub_parser(subparsers)

    sub_args = parser.parse_args(args.SUB_ARGS)
    sub_args.handler(awc, sub_args)


def create_sub_parser(subparsers):
    sp = subparsers.add_parser(
        "storage",
        help="storage help"
    )
    sp.set_defaults(handler=call_handler)
    sp.add_argument('SUB_ARGS', nargs='*')
