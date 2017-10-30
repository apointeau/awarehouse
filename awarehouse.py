# @Author: Antoine Pointeau <kalif>
# @Date:   2017-10-22T16:54:20+02:00
# @Email:  web.pointeau@gmail.com
# @Filename: a42_warehouse.py
# @Last modified by:   kalif
# @Last modified time: 2017-10-30T23:32:41+01:00

import argparse

from awarehouse import AWContext

def getParser():
    """
    This function build the command line parser using the python module argparse
    """
    # TODO add description and/or epilog
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--conf', metavar='FILE')
    return parser

def main():
    parser = getParser()
    args = parser.parse_args()
    awc = AWContext(args.conf)

if __name__ == "__main__":
    main()
