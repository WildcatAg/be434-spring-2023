#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-03-04
Purpose: Python cat
"""

import argparse
import os
import sys
import io

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs = "+",
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-n',
                        '--numbers',
                        help='Number the lines',
                        action='store_true')

#---------------------------
    args = parser.parse_args()
    
    filehandle = args.file
    
    if os.path.isfile(filehandle):
        
    else:
        filehandle = io.StringIO(filehandle + '\n')

    return args

#OR

    #args = parser.parse_args()

    #if os.path.isfile(args.text):
    #    args.text = open(args.text).read().rstrip()

    #return args


# --------------------------------------------------
def main():

    args = get_args()
    out_fh = open(args.file, 'wt') if args.file else sys.stdout
    for line in args.file:
        out_fh.write(line.upper())
    out_fh.close()

#OR

    #args = get_args()
    #out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    #out_fh.write(args.text.upper() + '\n')
    #out_fh.close()
# --------------------------------------------------
if __name__ == '__main__':
    main()
