# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:43:28+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: cmd_ls.py
# @Last modified by:   kalif
# @Last modified time: 2017-12-13T01:48:22+01:00

import os


def printer(awc, path, recursive):
    if recursive:
        print("{0}:".format(path))
        subDirectories = []
    dirContent = awc.listdir(path)
    for name in dirContent:
        if recursive:
            print("  {0}".format(name))
            subPath = os.path.join(path, name)
            if awc.isdir(subPath):
                subDirectories.append(subPath)
        else:
            print("{0}".format(name))
    if recursive:
        print("")
        for sdir in subDirectories:
            printer(awc, sdir, recursive)


def call_handler(awc, args):
    if len(args.PATH) == 0:
        args.PATH = ['/']
    for path in args.PATH:
        if awc.exists(path):
            if not awc.isdir(path):
                print(path)
            else:
                printer(awc, path, args.recursive)
        else:
            print("error: '{0}' no such file or directory".format(path))
        if len(args.PATH) > 1:
            print("")

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
        dest="recursive"
    )
    sp.add_argument(
        "PATH",
        nargs='*'
    )
