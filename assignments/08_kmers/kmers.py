#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-02
Purpose: Find common kmers
"""

# /bin/import_list.txt
import argparse
import os
# import csv
# import emoji
import io
# import random
import re
# import string
import sys
from itertools import cycle
# from pprint import pprint
# from pydash import flatten
# from tabulate import tabulate
# from typing import List, NamedTuple, Optional
# from typing import List, Optional, TypedDict
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find common kmers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("filea", metavar="FILE1", type=str, help="Input file 1")

    parser.add_argument("fileb", metavar="FILE2", type=str, help="Input file 2")

    parser.add_argument("-k", "--kmer", help="K-mer size", metavar="int", type=int, default=3)

    args = parser.parse_args()

    if os.path.isfile(args.filea) == False:
        parser.error(f"No such file or directory: '{args.filea}'")

    if os.path.isfile(args.fileb) == False:
        parser.error(f"No such file or directory: '{args.fileb}'")

    if args.kmer != int:
        parser.error(f"invalid int value: '{args.kmer}'")

    # if (args.kmer <= 0) == True:
    # if args.kmer <= 0 == True:
    #if not args.kmer > 1:
    #if args.kmer < 1: ##should be this but doesnt work -- "kmers.py: error: invalid int value: '3'"
    #number = args.kmer
    if args.kmer: ##or this but doesnt work -- "kmers.py: error: invalid int value: '3'"
        #if number < 1:    
        parser.error(f'--kmer "{args.kmer}" must be > 0')
    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    kmer = args.kmer
    fh1 = open(args.filea, "r")
    fh2 = open(args.fileb, "r")
    printtext = []
    for line1 in fh1.readlines(): 
        for word1 in line1.split():
            tempvar1 = word1
            for line2 in fh2.readlines():
                for word2 in line2.split():
                    tempvar2 = word2  
                    if tempvar1 == tempvar2:
                        printtext.append(tempvar1)
                    else:
                        print("0")
    print(printtext)
    # for fh1 in args.file:
    #     for line1 in fh1:
    #         for word1 in line1.split():
    #             print(word1)
    #             line_num += 1

    #print(args)

##From Readme ---------
    words1 = {}
    words2 = {}
    index1 = 0
    index2 = 0
    printtext = []

    for line1 in fh1: #process first file, read line
        for word1 in line1.split(): #split to words
            words1[word1] = 1 #index word1
            for kmer1 in find_kmers(word1, index1):
                index1 += 1 # increment the count of this "kmer" in "words1"
                words1.append(kmer1)
    for line2 in fh2: #Process second file, read line
        for word2 in line2.split():#split to words
            #words1[word2] = 1 #or??
            words2[word2] = 1 #index word1
            for kmer2 in find_kmers(word2, index2):
                index2 += 1# increment the count of this "kmer" in "words1"
                words2.append(kmer2)

    if [word1,index1] == [word2, index2]:
        printstr = printtext.append(word1)
        
    ##From Readme ---------


    # print(f'{printstr}          {index1}     {index2}')
    table = []

    for l, k in zip(line1, cycle(line2)):
        start = ord(l) #restart index each time
        shiftpos = ord(k)
        if chr(start) == chr(shiftpos):
            table.append(chr(start))

###From Translate.py---------------------
    k = args.kmer
    codon_table = {}
    seqa = open(args.filea, "r")
    
    for line in fh1:  # works
        tempvar = line.rstrip().split()
        codon_table[tempvar[0]] = tempvar[1]
    
    for codon in [seqa[i : i + k] for i in range(0, len(seqa), k)]:
        # tempvar1 = codon_table.get(codon.upper())
        # print(tempvar1)
        if codon_table.get(codon.upper()) is None:
            args.outfile.write("-")
        else:
            args.outfile.write(codon_table.get(codon.upper()))
        # args.outfile.write(tempvar1)
    args.outfile.write("\n")
    print(f'Output written to "{args.outfile.name}".')
###From Translate.py---------------------

def find_kmers(seqa, k):
    """ Find k-mers in string """

    n = len(seqa) - k + 1
    return [] if n < 1 else [seqa[i:i + k] for i in range(n)]
# --------------------------------------------------
if __name__ == "__main__":
    main()
