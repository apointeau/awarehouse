# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:33:59+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: add.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T01:49:05+01:00

import sys
import readline

if sys.version_info.major == 2:
    input = raw_input


def get_field(dname, optional=False, choices=None):
    res = input("{0}: ".format(dname))
    if res == "" and not optional:
        print("error: empty answer, this field is required".format(dname))
        return get_field(dname, choices=choices)
    if choices and res not in choices:
        print("error: invalid choice: '{}' (choose from {})".format(res, ', '.join(choices)))
        return get_field(dname, choices=choices)
    return res


def call_handler(awc, args):
    print("Welcome to the storage prompt builder !")
    print("- please fill the following fields -\n")
    typeChoices = ["FOLDER", "SFTP"]
    storage = {
        "name": get_field("Storage name"),
        "type": get_field("Type [{0}]".format(', '.join(typeChoices)), choices=typeChoices)
    }


def create_sub_parser(subparsers):
    msg = (
        "add help"
    )
    sp = subparsers.add_parser(
        "add",
        description=msg,
        help=msg
    )
    sp.set_defaults(handler=call_handler)
