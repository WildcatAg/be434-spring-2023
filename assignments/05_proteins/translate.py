#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-03-04
Purpose: Translate DNA/RNA to proteins
"""

import argparse
#import os
#import io

#blows up at 60%

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        default=None)

    parser.add_argument('-o',
                    '--outfile',
                    help='Output filename',
                    metavar='FILE',
                    type=argparse.FileType('wt'),
                    default='out.txt',
                    nargs = '+' 
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    ###translate.py: error: the following arguments are required: str
    print('seq =', args.sequence)
    print('codons =', args.codons)
    print('outfile =', args.outfile)
    
    #for line in args.codons:
    #    print(line.rstrip().split())

    #Define dictionary for base to base represented
    #Base and base represented
    #trans = {"R": "[AG]","Y": "[CT]","S": "[GC]","W": "[AT]","K": "[GT]","M": "[AC]","B": "[CGT]","D": "[AGT]","H": "[ACT]","V": "[ACG]","N": "[ACGT]",}
    #base and complimentary base
    #complbase = {"R": "Y","Y": "R","S": "S","W": "W","K": "M","M": "K","B": "V","D": "H","H": "D","V": "B","N": "N",}
    
    #creat dictionary from codon files; initialize dict., open file; read positions and assign to key
    #codondna = {} #(position 0:2, ':', 4) from i:i values
    #codonrna = {} #position 0:2, ':', 4 from i:i values

#outfile filehandle - rt or wt? Im writing to it arent i?
    #outfh = open(args.outfile,"wt")

    #codon size is 3 basepairs
    #k = 3
    #seq = 'actga'
    #for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1)]:
    #    print(codon)

#loop for translating sequence provided
    #for str in args.sequence:
    #    if str in trans:
    #        print(f'{trans.get(str)}')
    #    else:
    #        print(f'-')

#loop for translating in file    
    #for str in args.codons:
    #       if str in trans:
    #            print(f'{trans.get(str)}')
    #        else:
    #            print(f'-')

#loop for translating 3mers
    #for str in args.codons:
    #        if str in trans:
    #            print(f'{trans.get(str)}')
    #        else:
    #            print(f'-')




# --------------------------------------------------
if __name__ == '__main__':
    main()

