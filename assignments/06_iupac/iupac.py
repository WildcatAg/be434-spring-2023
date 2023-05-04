#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-02-28
Purpose: Rock the Casbah
"""
# blows up at test 1

# /bin/import_list.txt
import argparse
# import csv
# import emoji
import io
import os
# import random
import re
# import string
import sys
# from pprint import pprint
# from pydash import flatten
# from tabulate import tabulate
# from typing import List, NamedTuple, Optional
# from typing import List, Optional, TypedDict
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "sequence",
        metavar="SEQ",
        nargs="+",
        type=str,
        help="Input sequence(s)",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="FILE",
        type=argparse.FileType("w"),
        default=sys.stdout,
    )

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    from pprint import pprint  # keep - imports pretty print
    printedtext = list() #empty list to be printed
    fho = args.outfile
    #Key / Value
    trans = {"R": "[AG]","Y": "[CT]","S": "[GC]","W": "[AT]","K": "[GT]","M": "[AC]","B": "[CGT]","D": "[AGT]","H": "[ACT]","V": "[ACG]","N": "[ACGT]",}
    index = 0
    temp = []
    ##the keys are the codons and the values are the residues.
    for line in args.sequence:  # works
        tempvar = line.rstrip().split()
        for letter in tempvar:
            for char in letter:
                if trans.get(char.upper()) is None:
                    temp.append(char)
                else:
                    chartemp = trans.get(char.upper()) 
                    temp.append(chartemp)
            
            printtemp = ''.join(temp)
            printstr = str(args.sequence)
            printstr1 = printstr.strip("[]'")
            #print(f' {args.sequence} {str(temp.strip())}')
            print(f'{printstr1} {printtemp}')
    #         args.outfile.write("-")
    #     else:
    #         args.outfile.write(codon_table.get(codon.upper()))
        #trans[tempvar[index]] = tempvar[index+1]
        #print(trans[tempvar[0]])
        # Works
        #basepairs
    exit()
    # k = 3
    # seq = args.sequence
    # for codon in [seq[i : i + k] for i in range(0, len(seq), k)]:
    #     if codon_table.get(codon.upper()) is None:
    #         args.outfile.write("-")
    #     else:
    #         args.outfile.write(codon_table.get(codon.upper()))
    # args.outfile.write("\n")
    # print(f'Output written to "{args.outfile.name}".')










#     #sequence2 = sequence1.split()
   
#     for tempvar in args.sequence.split():  # reading in line ###.read() also works
#         #sequence1 = args.sequence.split()# print(line)
#         for char in tempvar.upper():  # split to line to words
#             print(tempvar)
#             # tempasc = chr(tempvar)
#             # for char in tempvar:
#             if char in trans:
#                 # print(char, alpha.find(char))\
#                 #tempvar1 = trans.find(char) 
#                 fho.write(trans[tempvar])
#             else:
#                 fho.write(char)
    
#     # if args.outfile: #if flag, write each line
#     #     args.outfile.write(f'"{sequence1}" {sequence2}''\n')
#     #     print(args.outfile)
#     # else:
#     #     print(f'"{sequence1}" {sequence2}')
#     # exit()
#     # #Loop 
#     # # for SEQ in args.sequence:
#     # #     if sequence1 in trans [Loc X]:
#     # #         sequence2 = 
#     #     printedtext = trans.get(sequence1, sequence1)
        
#     #     #printedtext = trans.get(sequence1, errortext)
#     #     print(f'"{args.sequence}" {printedtext}')
#     #     #print(printedtext)
#     # #print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
#     # #print(f'positional = "{pos_arg}"')
#     # for line in args.sequence:  # works
#     #     tempvar = line.rstrip().split() 
#     for sequence1 in [trans[i : i + k] for i in range(0, len(seq), k)]:
#         if trans.get(sequence1.upper()) is None:
#             fho.append(sequence1)
#             #print(f'"{args.sequence}" {printedtext}')
#         else:
#             fho.append(sequence2)
#             #print(f'"{args.sequence}" [{printedtext}]')
#     fho.write("\n")
    
#     # print(printedtext)
#     # #print(f'"{args.sequence}" {printedtext}')
# # --------------------------------------------------
if __name__ == '__main__':
    main()
