# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-09T22:59:10+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: awfs.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-09T23:37:29+01:00

def create_sub_parser(parser):
    parser.add_argument("--list", action="store_true", help="print all the current configuration fields")
    parser.add_argument("--set")
    parser.add_argument("--unset")
    return parser
