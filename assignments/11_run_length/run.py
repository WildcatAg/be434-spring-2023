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
#import os
#import random
import re
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
    sequence = args.sequence
    print(rle(sequence))
# --------------------------------------------------
def rle_encode(sequence):
    encoding = ''
    prev_char = ''
    index = 1 #start at 1

    #if not sequence: return ''
    
    for char in sequence:
        # If the prev and current characters don't match...
        if char != prev_char:
            # ...then add the count and character to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding
# --------------------------------------------------
if __name__ == '__main__':
    main()
