# @Author: Antoine Pointeau <kalif>
# @Date:   2017-12-13T00:57:01+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: rm.py
# @Last modified by:   kalif
# @Last modified time: 2017-12-13T01:34:31+01:00


def remove(awc, path, recursive):
    if not awc.exists(path):
        print("error: '{0}' no such file or directory".format(path))
    elif recursive:
        awc.rmtree(path)
    elif awc.isdir(path) and len(awc.listdir(path)):
        print("error: '{0}' directory is not empty".format(path))
    else:
        awc.rm(path)


def call_handler(awc, args):
    for path in args.PATH:
        remove(awc, path, args.recursive)


def create_sub_parser(subparsers):
    msg = (
        "rm help"
    )
    sp = subparsers.add_parser(
        "rm",
        description=msg,
        help=msg
    )
    sp.set_defaults(handler=call_handler)
    sp.add_argument(
        '-r', '-R', '--recursive',
        action="store_true",
        dest="recursive"
    )
    sp.add_argument(
        'PATH',
        nargs='+'
    )
