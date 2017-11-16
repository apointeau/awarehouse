# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-16T01:14:30+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: TOUCH.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T01:48:33+01:00

def call_handler(awc, args):
    for filePath in args.FILE:
        awc.touch(filePath)

def create_sub_parser(subparsers):
    msg = (
        "Update the access and modification times of each FILE to the current time. "
        "A FILE argument that does not exist is created empty."
    )
    sp = subparsers.add_parser(
        "touch",
        description=msg,
        help=msg
    )
    sp.set_defaults(handler=call_handler)
    sp.add_argument(
        'FILE',
        nargs='+'
    )
