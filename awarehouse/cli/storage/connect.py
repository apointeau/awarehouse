# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-16T23:28:21+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: create.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-17T00:10:40+01:00

import datetime


def log(msg, level="INFO"):
    now = datetime.datetime.now()
    print("[{0}] {1} - {2}".format(
        level,
        now.strftime("%Y-%m-%d %H:%M"),
        msg
    ))


def call_handler(awc, args):
    log("Search the storage called '{0}'".format(args.name))
    for s in awc.storages:
        if s.name == args.name:
            log("Initiate connection ...")
            s.connect()


def create_sub_parser(subparsers):
    msg = (
        "connect help"
    )
    sp = subparsers.add_parser(
        "connect",
        description=msg,
        help=msg
    )
    sp.set_defaults(handler=call_handler)
    sp.add_argument("-n", "--name", metavar="NAME", required=True)
    sp.add_argument("-v", "--verbose", action="store_true")
