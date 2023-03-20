#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-03-19
Purpose: Create synthetic sequences
"""

import argparse
import re
import os
import random
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='out.fa')
    
    parser.add_argument('-t',
                    '--seqtype',
                    help='DNA or RNA',
                    metavar='str',
                    type=str,
                    default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)
   
    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)    
   
    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)
   
    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)   
    
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    #parser.add_argument('-f',
    #                    '--file',
    #                    help='A readable file',
    #                    metavar='FILE',
    #                    type=argparse.FileType('rt'),
    #                    default=None)

    args = parser.parse_args()

    if args.seqtype != str:
        parser.error(f'--seqtype "{args.seqtype}" must be a valid sequence')

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

##type=argparse.FileType('wt')    -- args.outfile will be an open, writable file handle


    print('hello')


# --------------------------------------------------
if __name__ == '__main__':
    main()
