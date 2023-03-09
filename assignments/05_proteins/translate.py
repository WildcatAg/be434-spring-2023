#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-03-04
Purpose: Translate DNA/RNA to proteins
"""

import argparse


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
                        default=None)

    parser.add_argument('-o',
                    '--outfile',
                    help='Output filename',
                    metavar='FILE',
                    type=argparse.FileType('rt'),
                    default='out.txt',
                    nargs = '+' 
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg

    file_arg = args.file

    pos_arg = args.positional


# --------------------------------------------------
if __name__ == '__main__':
    main()
