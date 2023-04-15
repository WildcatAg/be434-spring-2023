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

    return parser.parse_args()
# --------------------------------------------------
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    ## If input is string and not file then RLE on the input sequence
    ## If file, open the file w for loop to strip lines
    #print the encoded sequences, file containing multiple sequences, 
    # ou can use str.splitlines() to process each sequence:

    for seq in args.sequence.splitlines():
        #print(seq)    ##30% comment in at minimum
        print(rle(seq)) #**comment out to reach 30%**
    #print(args)
    

# --------------------------------------------------
# --------------------------------------------------
#consider writing a function in your run.py program called rle()
#that will accept a single sequence and return the encoded version

def rle(seq):
    """ Create RLE """
    
    ##From seq, for loop to find common characters in each line char by char in order
        ##if intersection, count number of char and print ''char' + 'count''
            ##else print char
    ##create an empty list - lists are ordered - that accepts the replaced values
    ##old_list = (seq)
    new_list = ()
    index_char = 1 #for indexing occurence of value
    #for letter in seq    
        #new_list.append()
    
    ##count times the character shows up and then display that if flag is true
    ##else append list with character in question
    for index,character in list(enumerate(seq[:-1])):
        if character == seq[index+1]:
            index_char =+ 1
            new_list.append(character+index_char)
        else:
            new_list.append(character)
    
    print(new_list)

    ##placeholder = (seq) or [seq]?
        ##duplicate_vals = placeholder.count()
    
    ##print (newlist)
    
    #return ''
    pass
# --------------------------------------------------
# --------------------------------------------------
if __name__ == '__main__':
    main()
