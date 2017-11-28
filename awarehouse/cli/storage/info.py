# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:35:55+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: list_command.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T01:49:29+01:00


def call_handler(awc, args):
    for s in awc.storages:
        print("Name:   {0}".format(s.name))
        print("Role:   {0}".format(s.role))
        print("Status: {0}".format("connected" if s.connected else "disconnected"))
        print("")


def create_sub_parser(subparsers):
    msg = (
        "info help"
    )
    sp = subparsers.add_parser(
        "info",
        description=msg,
        help=msg
    )
    sp.set_defaults(handler=call_handler)
