#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-02
Purpose: Find common kmers
"""
##You will create a Python program called kmers.py that accepts 
# two readable text files and an optional -k|--kmer argument 
# that accepts an integer value greater than 0 and which defaults
# to 3.

#/bin/import_list.txt
import argparse
import os
#import csv
#import emoji
import io
#import random
import re
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
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter) 
    
    parser.add_argument('filea',
                        metavar='FILE1',
                        type=str,
                        help='Input file 1')

    parser.add_argument('fileb',
                        metavar='FILE2',
                        type=str,
                        help='Input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)
    
    args = parser.parse_args()
    
    if os.path.isfile(args.filea) == False:
        parser.error(f"No such file or directory: '{args.filea}'")

    if os.path.isfile(args.fileb) == False:
        parser.error(f"No such file or directory: '{args.fileb}'")
    
    # if os.path.isfile(args.FILE1) == False:
    #     parser.error(f'--col "{args.FILE1}" No such file or directory:')
    # else:
    #     if os.path.isfile(args.FILE2) == False:
    #         parser.error(f'--col "{args.FILE2}" No such file or directory:')
    return args
    
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    
    # for fh1 in args.file:
    #     for line1 in fh1:
    #         for word1 in line1.split():
    #             print(word1)
    #             line_num += 1
    
    
    print (args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
