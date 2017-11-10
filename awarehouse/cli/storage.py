# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-09T22:49:05+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: storage.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-10T01:16:12+01:00

import sys
import readline

if sys.version_info.major == 2:
    input = raw_input


def command_list(awc, args):
    for s in awc.storages:
        print("Name:   {0}".format(s.name))
        print("Status: {0}".format("connected" if s.connected else "disconnected"))
        print("")


def get_field(dname, optional=False, choices=None):
    res = input("{0}: ".format(dname))
    if res == "" and not optionnal:
        print("error: empty answer, this field is required".format(dname))
        return get_field(dname, choices=choices)
    if choices and not res in choices:
        print("error: invalid choice: '{}' (choose from {})".format(res, ', '.join(choices)))
        return get_field(dname, choices=choices)
    return res


def command_add(awc, args):
    print("Welcome to the storage prompt builder !")
    print("- please fill the following fields -\n")
    typeChoices = ["FOLDER", "SFTP"]
    storage = {
        "name": get_field("Storage name"),
        "type": get_field("Type [{0}]".format(', '.join(typeChoices)), choices=typeChoices)
    }


def commands_router(awc, args):
    if args.list:
        command_list(awc, args)
    elif args.add:
        command_add(awc, args)


def create_sub_parser(subParser):
    subParser.set_defaults(func=commands_router)
    group = subParser.add_mutually_exclusive_group()
    group.add_argument("--list", action="store_true", help="print all the current storages")
    group.add_argument("--add", action="store_true", help="run the storage prompt builder")
