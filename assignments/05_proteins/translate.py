#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-03-04
Purpose: Translate DNA/RNA to proteins
"""

# /bin/import_list.txt
import argparse
# import csv
# import emoji
import io
# import random
import os
# import re
# import string
import sys
# from pprint import pprint
# from pydash import flatten
# from tabulate import tabulate
# from typing import List, NamedTuple, Optional
# from typing import List, Optional, TypedDict

### Blows up after 80%


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Translate DNA/RNA to proteins",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("sequence", metavar="str", help="DNA/RNA sequence")

    parser.add_argument(
        "-c",
        "--codons",
        help="A file with codon translations",
        metavar="FILE",
        type=argparse.FileType("rt"),
        required=True,
        default=None,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    from pprint import pprint  # keep - imports pretty print

    # should this be imported with sys and io?

    # print('seq =', args.sequence)
    # print('codons =', args.codons)
    # print('outfile =', args.outfile)

    codon_table = {}
    #codondna = {}  # (position 0:2, ':', 4) from i:i values
    #codonrna = {}  # position 0:2, ':', 4 from i:i values
    # outfh = open(args.outfile,"wt")
    # args.outfile.write('hello')
    # -----------------
    ##Now consider what changes your code would need to do to create a dictionary where
    ##the keys are the codons and the values are the residues.
    for line in args.codons:  # works
        tempvar = line.rstrip().split()
        codon_table[tempvar[0]] = tempvar[1]

        # Works
        # codon_table = dict.fromkeys(args.codons[0:2],args.codons[4]) #Doesnt work
        # codon_table = dict.fromkeys(line[0:2],line [4]) #better but stuck
    # pprint(codon_table) # pretty print
    # -------------------

    # Define dictionary for base to base represented
    # Base and base represented
    #trans = {
       # "R": "[AG]",
        #"Y": "[CT]",
        #"S": "[GC]",
        #"W": "[AT]",
        #"K": "[GT]",
        #"M": "[AC]",
        #"B": "[CGT]",
        #"D": "[AGT]",
       # "H": "[ACT]",
       # "V": "[ACG]",
       # "N": "[ACGT]",
       # }
    # base and complimentary base
    # complbase = {"R": "Y","Y": "R","S": "S","W": "W","K": "M","M": "K","B": "V","D": "H","H": "D","V": "B","N": "N",}

    # creat dictionary from codon files; initialize dict., open file; read positions and assign to key
    # codondna = {} #(position 0:2, ':', 4) from i:i values
    # codonrna = {} #position 0:2, ':', 4 from i:i values
    # ---------------
    # Alter this code to print the codon and then what the codon translates to so that it will print the following:
    # Once you've got that, make your program print the protein sequence on one line:

    # codon size is 3 basepairs
    # k = 3
    # seq = 'actga'
    # for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1)]:
    #    print(codon)

    k = 3
    seq = args.sequence
    for codon in [seq[i : i + k] for i in range(0, len(seq), k)]:
        # print(f'{codon.upper()} {(codon_table.get(codon.upper()))}')
        # tempvar1 = codon_table.get(codon.upper())
        # print(tempvar1)
        # print(codon.upper())
        if codon_table.get(codon.upper()) is None:
            args.outfile.write("-")
        else:
            args.outfile.write(codon_table.get(codon.upper()))
        # args.outfile.write(tempvar1)
    args.outfile.write("\n")
    print(f'Output written to "{args.outfile.name}".')
    #exit()

    # # loop for translating sequence provided
    # for str in args.sequence:
    #     if str in trans:
    #         print(f"{trans.get(str)}")
    #     else:
    #         print(f"-")

    # # loop for translating in file
    # for str in args.codons:
    #     if str in trans:
    #         print(f"{trans.get(str)}")
    #     else:
    #         print(f"-")

    # # loop for translating 3mers
    # for str in args.codons:
    #     if str in trans:
    #         print(f"{trans.get(str)}")
    #     else:
    #         print(f"-")


# ---------------
# Finally, make this string print into the args.outfile instead of to STDOUT,
# and have your program report the name of the output file:

# outfile filehandle
# args.outfile.write()
# print( , file=outfh)
# outfh.close()
# print(f'{outfh} \n {os.path.basename(outfh)})
# ---------------

# --------------
if __name__ == "__main__":
    main()
