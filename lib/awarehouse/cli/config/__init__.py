# @Author: Antoine Pointeau <kalif>
# @Date:   2017-11-15T23:37:28+01:00
# @Email:  web.pointeau@gmail.com
# @Filename: __init__.py
# @Last modified by:   kalif
# @Last modified time: 2017-11-15T23:37:29+01:00

def create_sub_parser(subParser):
    subParser.add_argument("--list", action="store_true", help="print all the current configuration fields")
    subParser.add_argument("--set")
    subParser.add_argument("--unset")
    return subParser
