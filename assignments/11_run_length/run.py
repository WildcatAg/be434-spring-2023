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

    ## If input is string and not file then RLE on the input sequence
    ## If file, open the file w for loop to strip lines
    #print the encoded sequences, file containing multiple sequences, 
    # ou can use str.splitlines() to process each sequence:

    for seq in args.sequence.splitlines():
        #print(seq)    ##30% comment in at minimum
        #print(rle(seq)) #**comment out to reach 30%** Add new line for each print?
        rle(seq)
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
    new_list = []
    new_char = str()
    index_char = 1 #for indexing occurence of value
    #for letter in seq    
        #new_list.append()
    ##Regular expression attempts
    ##
    ##for index,character in list(enumerate(seq[:-1])):
    #for index,character in enumerate(seq[:-1]):
    #new_list = re.search(character, seq)

    #x = re.sub(character, index_char, seq, *)
    #print(x)
    
    ##count times the character shows up and then display that if flag is true
    ##else append list with character in question
    ##for index,character in list(enumerate(seq[:-1])):
    #for index,character in enumerate(seq[:-1]):
    
    
    
    for index,character in enumerate(seq):
        #if character == seq[index+1, character]: ##if character is equal to character at index point +1
        indexp = index + 1 #the next character over
        if indexp != len(seq):
            if character == seq[indexp]:
                index_char+=1 #add 1 to index char, starting from 1 for single occurence
                #new_char = character+str(index_char)
                #new_list.append(character+str(index_char))
                #new_list.append(new_char)
                #print(new_list)
                #return new_list
            else:
                if index_char > 1:
                    new_list.append(character+str(index_char))
                else:
                    new_list.append(character)
                index_char=1
                #return new_list
                #print(new_list)
    
    print(''.join(new_list))

##string validation -- check whether input is AaCcTtGg etc. or give parser error
    #if re.findall('[^AaCcGgTt]',args.sequence):
    ##placeholder = (seq) or [seq]?
        ##duplicate_vals = placeholder.count()
    
    ##print (newlist)
    
    #return ''
    
   
    
    
    

# --------------------------------------------------
# --------------------------------------------------
if __name__ == '__main__':
    main()
