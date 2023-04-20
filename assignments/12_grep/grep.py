#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-20
Purpose: Python grep
"""

#/bin/import_list.txt
import argparse
#import csv
#import emoji
#import io
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
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')
    
    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)')
    
    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default= sys.stdout)

    args = parser.parse_args()
    
    #if os.path.isfile(args.file) == False:
    ##    parser.error(f'--col "{args.file}" No such file or directory:')
    #else:
    #    if os.path.isfile(args.pattern) == False:
     #       parser.error(f'--col "{args.FILE2}" No such file or directory:')

    #if args.pattern != str:
    #    parser.error(f'--seqtype "{args.seqtype}" must be a valid sequence')

    #if not 0 < args.pctgc < 1:
     #   parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')



    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()



# --------------------------------------------------
if __name__ == '__main__':
    main()
