#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-02
Purpose: Filter delimited records
"""
##The program will search the --file for the --val value 
# either in the given --col column or anywhere on the line 
# in a case-insensitive fashion. Any records matching will 
# be written to the --outfile. The input files are delimited 
# by commas and tabs, so you will need to use the --delimiter 
# option to parse them.


import argparse
#import csv
from pprint import pprint
#import re
#import sys
#import random

from tabulate import tabulate
#XYZ = [ ... ]#list of tuples
# print(tabulate(XYZ ))  or
# print(tabulate(XYZ, headers=('name1', 'name2')))


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        default=None)   
    
    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        default=None)
    
    
    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default="")

  
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        default="out.csv")

    parser.add_argument('-d',
                        '--delimeter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=",")

    args = parser.parse_args()

## check for file validity w parser error
## if args.XYZ -is something bad-:
        ##parser.error(f'BLAH BLAH "{args.XYZ}" blah blah')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()


    print(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
