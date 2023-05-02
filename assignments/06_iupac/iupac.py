#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-02-28
Purpose: Rock the Casbah
"""
#blows up at test 1

#/bin/import_list.txt
import argparse
#import csv
#import emoji
import io
import os
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
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='SEQ',
                        #nargs = '+',
                        #type=str,
                        help='Input sequence(s)')


    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdin)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    printedtext = ''
    trans = {"R": "[AG]","Y": "[CT]","S": "[GC]","W": "[AT]","K": "[GT]","M": "[AC]","B": "[CGT]","D": "[AGT]","H": "[ACT]","V": "[ACG]","N": "[ACGT]",}
    errortext = 'XXXXX'
    #file_arg = args.outfile
    sequence1 = args.sequence
    sequence2 = sequence1.split()
    #sequence1 = args.sequence.split()
    
    if args.outfile: #if flag, write each line
        args.outfile.write(f'"{sequence1}" {sequence2}''\n')
        print(args.outfile)
    else:
        print(f'"{sequence1}" {sequence2}')

    #Loop 
    for SEQ in args.sequence:
        if sequence1 in trans [Loc X]:
            sequence2 = 

        printedtext = trans.get(sequence1, sequence1)
        
        #printedtext = trans.get(sequence1, errortext)
        print(f'"{args.sequence}" {printedtext}')
        #print(printedtext)

    #print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    #print(f'positional = "{pos_arg}"')

    for line in args.sequence:  # works
        tempvar = line.rstrip().split() 

    for sequence1 in [trans[i : i + k] for i in range(0, len(seq), k)]:
        if trans.get(sequence1.upper()) is None:
            args.outfile.append(sequence1)
            #print(f'"{args.sequence}" {printedtext}')
        else:
            args.outfile.append(sequence2)
            #print(f'"{args.sequence}" [{printedtext}]')
    args.outfile.write("\n")
    
    print(printedtext)
    #print(f'"{args.sequence}" {printedtext}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
