#!/usr/bin/env python3
    # write a for loop to go through each of the files
    # from the command line

    # count the number of lines per file

    # if the boolean flag number is true print
    # the line numbers, otherwise print the line only
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

    # added the return here, because it was lost down below.
    args = parser.parse_args()
    
    #if args.file:
        #print(args.file)

    return args

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
    teststring = ''
    line_num = 0
    vals = []
    
    #if args.file:
    #    for word1 in line1.split()
    #    teststring = args.file
    #    print(teststring)

    if args.file:
        for fh1 in args.file:
            for line1 in fh1:
                for word1 in line1.split():
                    print(word1)
                #line_num += 1

    for fh2 in args.file2:
        for line2 in fh2:        
            for word2 in line2.split():
                line_num += 1

    for num, val in enumerate(vals, start=1):
         print(num, val)

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
