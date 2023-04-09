#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-03-04
Purpose: Find common words
"""

#/bin/import_list.txt
import argparse
#import csv
#import emoji
import io
#import os
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
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                    help='Input file 1',
                    metavar='FILE1',
                    type=argparse.FileType('rt'),
                    default=None)   
    
    parser.add_argument('file2',
                    help='Input file 2',
                    metavar='FILE2',
                    type=argparse.FileType('rt'),
                    default=None)   

    parser.add_argument('-o',
                    '--outfile',
                    help='Output file',
                    metavar='FILE',
                    type = argparse.FileType('wt'),
                    default= sys.stdout)

    args = parser.parse_args()

    #The program should halt with an error message 
    # if either of the positional arguments are not 
    # the names of valid, readable files


    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    #The program should find sequences are shared
    #The program should find common words
    
    comp_set1 = set() #comparative set 1
    comp_set2 = set() #comparative set 2
    compoutfile = set() #file to write values to
    
    #open each file, read the line, split to words to list, 
    # assign list to set
    
    for fh1 in args.file1:
        for line1 in fh1:
            for word1 in line1.split():
            #for word1 in line1.splitlines().split()
            #for word1 in line1.split(re.sub('[^a-zA-Z]', '', word1)):
                comp_set1.add(word1)
                #comp_set1 = comp_set1.add(word1) --NO
                    
    #open each file, read the line, split to words, assign to set2
    for fh2 in args.file2:
        for line2 in fh2:        
            for word2 in line2.split():
                comp_set2.add(word2)
                #comp_set2 = comp_set2.add(word2) --NO
            #for word2 in line2.split(re.sub('[^a-zA-Z]', '', word2)):
            #   #re.sub('[^a-zA-Z]', '', word2)
    #compare sets and write commons to a outfile
    
    compoutfile = comp_set1.intersection(comp_set2)

       #If the "-o|--outfile" option is provided, 
    # then the program should print the words to the 
    # provided output file and nothing to STDOUT: 
    # #if outfile flag is true, write contents to file named, else stdout
    if args.outfile:
        args.outfile = compoutfile.write()
    
    print(compoutfile)
    #print(comp_set1)
    #print(comp_set2)
    



#-------
#def clean(word1):
    #"""Remove non-word characters from word"""

    #return re.sub('[^a-zA-Z]', '', word1)
#-------

# --------------------------------------------------
if __name__ == '__main__':
    main()
