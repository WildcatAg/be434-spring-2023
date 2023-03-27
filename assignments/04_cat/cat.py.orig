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
    #for x in args.file:
    # if os.path.isfile(args.file):
    #open(args.file)
    #open('args.file')
    #open("args.file")
    #print(args.file.read, 'rt')
    #print(open(args.file).read())
    print("anything....")
    #x = open("args.file")
    #x = open('args.file')
    #x = open(args.file, 'rt').read()
    #x = open(args.file).read()
    #x = open(args.file)
    #x = open(args.file,'rt')
    #x.read()
    #print(x)

    return args ## keep

def main():

    args = get_args() ## keep 
    
    #x = open(args.file).rstrip()
    #print(x.read)
    #testfile4 = open(x).rstrip()
    #testfile3 = args.x.read()
    #testfile2 = open(args.x).read()
    #testfile1 = open(args.file).read()
    #testfile = open(args.file, 'rt')
    #testfile.read()
    #print(testfile)
    #print(testfile1)
    #print(testfile1.read())
    #print(testfile2)
    #print(testfile2.read())
    #print(testfile3)
    #print(testfile3.read())
    #print(testfile4)
    #print(testfile4.read())
    print("anything...")
# --------------------------------------------------
if __name__ == '__main__':
    main()
