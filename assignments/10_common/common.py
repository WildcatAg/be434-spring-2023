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
#import io
#import os
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
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                    help='Input file 1',
                    metavar='FILE1',
                    default=None)   
    
    parser.add_argument('file2',
                    help='Input file 2',
                    metavar='FILE2',
                    default=None)   

    parser.add_argument('-o',
                    '--outfile',
                    help='Output file',
                    metavar='FILE',
                    type = argparse.FileType('wt'),
                    default= sys.stdout)

    args = parser.parse_args()
    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    fh1 = open(args.file1,'r')
    fh2 = open(args.file2, 'r')
    printtext = []
    for line1 in fh1.readlines(): 
        for word1 in line1.split():
            tempvar1 = word1
            for line2 in fh2.readlines():
                for word2 in line2.split():
                    tempvar2 = word2  
                    if tempvar1 == tempvar2:
                        printtext.append(tempvar1)
    #printtext1 = str(printtext.strip("[]'"))
                        printtext1 = str(printtext)
                        p2 = printtext1.strip("[]") #Works no quotes, no brackets
    print(printtext1)
    #print(p2) #Works no quotes, no brackets







    # fh1 = args.file1 #file handle opens -> need to read it now
    # fh2 = args.file2
    
    # fhread1 = fh1.read() #read the open files and intialize a variable to do it
    # fhread2 = fh2.read()
    # fho = args.outfile
    # comp_set1 = set() #comparative set 1
    # comp_set2 = set() #comparative set 2
    # compoutfile = set() #file to write values to
    
    # for line in fh1.readlines():
    #     print(line)
    # exit()






    # #open each file, read the line, split to words to list, 
    # # assign list to set
    # ####
    # xxx = ""
    # #for fh1 in args.file1:
    # for line1 in fhread1:
    #     print(line1)
    #     exit()
    #     #for word1 in line1:
    #     #for word1 in line1.splitlines().split()
    #     #for word1 in line1.split(re.sub('[^a-zA-Z]', '', word1)):
    #     comp_set1.add(fhread1)
    #     print(comp_set1)    #printfriendly = ", ".join(compoutfile)
    #         #comp_set1 = comp_set1.add(word1) --NO
                    
    # #open each file, read the line, split to words, assign to set2
    # #for fh2 in args.file2:
    # for line2 in fhread2:        
    #     #for word2 in line2:
    #     comp_set2.add(fhread2)
    #             #comp_set2 = comp_set2.add(word2) --NO
    #         #for word2 in line2.split(re.sub('[^a-zA-Z]', '', word2)):
    #         #   #re.sub('[^a-zA-Z]', '', word2)
    # #compare sets and write commons to a outfile
    
    # compoutfile = comp_set1.intersection(comp_set2)
    # printfriendly = ", ".join(compoutfile)
    
    # print(compoutfile)
    # print(printfriendly)


       #If the "-o|--outfile" option is provided, 
    # then the program should print the words to the 
    # provided output file and nothing to STDOUT: 
    # #if outfile flag is true, write contents to file named, else stdout
    #if fho:
    #    fho.write(compoutfile)
    #else:
    #    print(compoutfile)
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
