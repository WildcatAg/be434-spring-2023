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
                        type=str,
                        help='Input text')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
  
    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
<<<<<<< HEAD
    
    if args.outfile:
        print(args.text.upper(), file=open(args.outfile, 'wt'))
=======

    # you named this outfile in the argparse above, not out
    # changed to outfile
    if args.outfile:
        # you need to open the file handle first to print to it
        out_fh = open(args.outfile, 'wt')
        # I added the '\n' because you strip this off above
        # I prefer to use write like so, as we do in the chapter
        # out_fh.write(args.text.upper() + '\n') 
        print(args.text.upper() + '\n', file=out_fh)
>>>>>>> d6bc64c128a48767eb46d46f919fed276df74aa3
    else:
        print(args.text.upper() + '\n')
   
# --------------------------------------------------
if __name__ == '__main__':
    main()
