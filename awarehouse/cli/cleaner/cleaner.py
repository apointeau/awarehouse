# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-23T00:42:15+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: cleaner.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-23T00:43:26+01:00


def call_handler(awc, args):
    pass


def create_sub_parser(subparsers):
    sp = subparsers.add_parser(
        "cleaner",
        help=(
            "The cleaner is program that will help you storing "
            "your untidy files in the warehouse."
        ),
    )
    sp.set_defaults(handler=call_handler)
