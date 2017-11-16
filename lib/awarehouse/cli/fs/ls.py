# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:43:28+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: cmd_ls.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-16T01:48:23+01:00


def myprint(awc, args, dir, name):
    if args.is_opt_l:  # TODO
        print("  {0}".format(name))
    else:
        print("  {0}".format(name))


def call_handler(awc, args):
    if len(args.PATH) == 0:
        args.PATH = ['/']
    for path in args.PATH:
        print("{0}:".format(path))
        dirContent = awc.listdir(path)
        for name in dirContent:
            myprint(awc, args, path, name)
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
        '-l',
        action="store_true",
        dest="is_opt_l",
        help="use a long listing format"
    )
    sp.add_argument(
        'PATH',
        nargs='*'
    )
