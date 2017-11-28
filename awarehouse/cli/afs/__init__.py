# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:30:54+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: __init__.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T22:33:39+01:00

import sys
import argparse

from awarehouse.cli.afs import ls
from awarehouse.cli.afs import touch
from awarehouse.cli.afs import makedirs


def call_handler(awc, args):
    parser = argparse.ArgumentParser(
        prog="{0} {1}".format(sys.argv[0], "afs")
    )
    subparsers = parser.add_subparsers()

    ls.create_sub_parser(subparsers)
    touch.create_sub_parser(subparsers)
    makedirs.create_sub_parser(subparsers)

    sub_args = parser.parse_args(args.SUB_ARGS)
    sub_args.handler(awc, sub_args)


def create_sub_parser(subparsers):
    sp = subparsers.add_parser(
        "afs",
        help="awarehouse file system help"
    )
    sp.set_defaults(handler=call_handler)
    sp.add_argument('SUB_ARGS', nargs='*')
