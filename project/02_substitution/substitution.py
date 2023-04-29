#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-29
Purpose: substitution cipher
"""

#/bin/import_list.txt
import argparse
#import csv
#import emoji
import io
import os
#import random
#import re
#import string
import sys
#from pprint import pprint
#from pydash import flatten
#from tabulate import tabulate
#from typing import List, NamedTuple, Optional
#from typing import List, Optional, TypedDict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='substitution cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=str,
                        help='Input file')

    parser.add_argument('-s',
                        '--seed',
                        help='A random seed',
                        metavar='SEED',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type = argparse.FileType('wt'),
                        default= sys.stdout)
    
    args = parser.parse_args()
    
    #fh = args.file
    #if os.path.isfile(file) == False:
    if os.path.isfile(args.file) == False:
        #parser.error(f"No such file or directory: '{sys.stdin}'")   
        parser.error(f"No such file or directory: '{args.file}'")
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
