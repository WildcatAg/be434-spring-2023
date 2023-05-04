#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-15
Purpose: Run-length encoding/data compression
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
#import sys
#from pprint import pprint
#from pydash import flatten
#from tabulate import tabulate
#from typing import List, NamedTuple, Optional
#from typing import List, Optional, TypedDict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()
    
    return args
    
# --------------------------------------------------
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    #if string is a file, open first as fh and read it as variable passed in. 
    if os.path.isfile(args.sequence) == True:
        fh = open(args.sequence, "r")
        sequence = fh.read()
        printedtext = (rle(sequence))
        print(printedtext)
    else: #if not, just read as string
        sequence = args.sequence
        printedtext = (rle(sequence))
    #printedtext = (rle(sequence))
        print(printedtext)
    

# --------------------------------------------------
def rle(sequence):
    encoding = ''
    prev_char = ''
    index = 1 #start at 1
    
    for char in sequence:
    #for char in args.sequence: NO
        # If the prev and current characters don't match...
        if char != prev_char:
            # ...then add the count and character to our encoding
            if prev_char:
                if count == 1:
                    encoding += prev_char
                else:
                    encoding +=  prev_char + str(count) #need to declare counting index as a string to print
            count = 1
            prev_char = char
        else:
            # Index increases if the characters do match and repeats
            count += 1
    else: #if count = 1, just return char, else return count
        if count == 1:
            encoding += prev_char
        else:
            encoding += prev_char + str(count)
        return encoding
# --------------------------------------------------
if __name__ == '__main__':
    main()
