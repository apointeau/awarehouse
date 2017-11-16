# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:30:54+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: __init__.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T01:18:11+01:00

import sys
import argparse

import ls
import touch


def call_handler(awc, args):
    parser = argparse.ArgumentParser(
        prog="{0} {1}".format(sys.argv[0], "fs")
    )
    subparsers = parser.add_subparsers()

    ls.create_sub_parser(subparsers)
    touch.create_sub_parser(subparsers)

    sub_args = parser.parse_args(args.SUB_ARGS)
    sub_args.handler(awc, sub_args)


def create_sub_parser(subparsers):
    sp = subparsers.add_parser(
        "fs",
        help="file system help"
    )
    sp.set_defaults(handler=call_handler)
    sp.add_argument('SUB_ARGS', nargs='*')
