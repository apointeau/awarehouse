# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:43:28+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: cmd_ls.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T01:48:23+01:00

import os


def myprint(awc, args, dir, name):
    print("  {0}".format(name))


def directory_printer(awc, args, path):
    if args.is_recursive:
        print("{0}:".format(path))
    dirContent = awc.listdir(path)
    subDirectories = []
    for name in dirContent:
        myprint(awc, args, path, name)
        subPath = os.path.join(path, name)
        if awc.isdir(subPath):
            subDirectories.append(subPath)
    if args.is_recursive:
        print("")
    for sdir in subDirectories:
        directory_printer(awc, args, sdir)


def call_handler(awc, args):
    if len(args.PATH) == 0:
        args.PATH = ['/']
    for path in args.PATH:
        if awc.exists(path):
            directory_printer(awc, args, path)
        else:
            print("ls: cannot access '{0}': No such file or directory".format(path))


def create_sub_parser(subparsers):
    msg = (
        "ls help"
    )
    sp = subparsers.add_parser(
        "ls",
        description=msg,
        help=msg
    )
    sp.set_defaults(handler=call_handler)
    sp.add_argument(
        "-R", "--recursive",
        action="store_true",
        dest="is_recursive"
    )
    sp.add_argument(
        "PATH",
        nargs='*'
    )
