#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-02
Purpose: Find common kmers
"""
##You will create a Python program called kmers.py that accepts 
# two readable text files and an optional -k|--kmer argument 
# that accepts an integer value greater than 0 and which defaults
# to 3.
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter) 
    
    parser.add_argument('FILE1',
                        metavar='FILE1',
                        help='Input file 1')

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        help='Input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print (args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
