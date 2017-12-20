# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:35:55+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: list_command.py
# @Last modified by:   kalif
# @Last modified time: 2017-12-20T22:02:32+01:00


def printer(storage):
    print("Name:   {0}".format(storage.name))
    print("Role:   {0}".format(storage.role))
    print("Status: {0}".format("connected" if storage.connected else "disconnected"))
    print("")


def call_handler(awc, args):
    print("# --- MASTER --- #")
    printer(awc.master)
    print("# --- SLAVES --- #")
    for storage in awc.slaves:
        printer(storage)



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
