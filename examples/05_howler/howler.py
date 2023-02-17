#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-02-17
Purpose: Howler excercise
"""
import os
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler excercise',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='None')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
  
    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    if args.out:
        print(args.text.upper(), file=open(args.out, 'wt'))
    else:
        print(args.text.upper())
   
# --------------------------------------------------
if __name__ == '__main__':
    main()
