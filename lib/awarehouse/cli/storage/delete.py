# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-16T23:28:27+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: delete.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T23:35:27+01:00

def call_handler(awc, args):
    for s in awc.storages:
        


def create_sub_parser(subparsers):
    msg = (
        "delete help"
    )
    sp = subparsers.add_parser(
        "delete",
        description=msg,
        help=msg
    )
    sp.set_defaults(handler=call_handler)
    sp.add_argument('NAME', required=True)
