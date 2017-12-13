# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-16T22:27:24+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: makedirs.py
# @Last modified by:   kalif
# @Last modified time: 2017-12-13T01:30:36+01:00


def call_handler(awc, args):
    for directory in args.DIRECTORY:
        awc.makedirs(directory)


def create_sub_parser(subparsers):
    msg = (
        "mkdir help"
    )
    sp = subparsers.add_parser(
        "mkdir",
        description=msg,
        help=msg
    )
    sp.set_defaults(handler=call_handler)
    sp.add_argument(
        'DIRECTORY',
        nargs='+'
    )
