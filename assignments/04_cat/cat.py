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

##blows up at test fox, cant import, read, or open files -- not sure where im going wrong
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
 
    return args ## keep

def main():

    args = get_args() ## keep 

    testfile = open(args.file)
    testfile.read()
    print(testfile)
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
