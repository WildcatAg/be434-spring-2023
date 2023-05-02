#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-29
Purpose: vigenere cipher
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
        description='vigenere cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=str,
                        help='Input file')

    parser.add_argument('-k',
                        '--keyword',
                        help='A keyword',
                        metavar='KEYWORD',
                        type=str,
                        default="CIPHER")

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
    fh = args.file
    shift = args.keyword
    
    print(encrypt(fh, shift))
# --------------------------------------------------

#---------------------------------------------------

def encrypt(fh,shift):
    
    encryption = ""
    for tempvar in fh:
        for letter in tempvar.split():
    # for letter in range(len(fh)):
            ##Change keyword to numbers and then pass through
            tempvar = fh[shift]
            tempvar = letter
        # Encrypt uppercase characters
        if (letter.isupper()):
        #if (tempvar.isupper()):
            encryption += chr((ord(letter) + shift-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            encryption += chr((ord(letter) + shift - 97) % 26 + 97)
 
    return encryption

# --------------------------------------------------


# --------------------------------------------------
if __name__ == '__main__':
    main()



    #modulo 
    for each line 
    countervar = 0 #starting position of index for each line at line, reinitialize counter at 0 
    incrememnt counter at capital letters only, not space or symbols
    countervar = mod% len(cipher key) #position in the cipher key to use
    
    counter for calputal letters
    lookups in alpha 
    deceode is subtraction , coding is addition (modulus)


