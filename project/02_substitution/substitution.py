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
import string
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
    
    ##Check the file
    if os.path.isfile(args.file) == False:
        #parser.error(f"No such file or directory: '{sys.stdin}'")   
        parser.error(f"No such file or directory: '{args.file}'")
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    fh = args.file
    shift = args.seed
    
    print (encrypt(fh, shift))

#---------------------------------------------------
def encrypt(fh,shift):

    lower = range(97,123) 
    upper = range(65,91)
    
    #Need to be enumerated?
    seedsplit = str(shift).split()
    
    encryption = ""
    #From the fh for each split line
    for tempvar in fh:
        #for each 
        for letter in tempvar.split():
    # for letter in range(len(fh)):
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

#---------------------------------------------------

def translateMessage(message, key, mode):
    args = get_args()
    translated = ''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charsA = "SOMETHING"
    charsB = args.seed
    
    for symbol in message:
        if symbol.upper() in charsA:
# Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:# The symbol is not in LETTERS, just add it unchanged.
            translated += symbol
    return translated

# --------------------------------------------------
if __name__ == '__main__':
    main()



# --------------------------------------------------
if __name__ == '__main__':
    main()
