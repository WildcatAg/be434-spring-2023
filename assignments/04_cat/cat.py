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
 
    #make variable to open file
    #file = args.file
    #filehandle = open(args.file)
    #filehandle.read()

#    for str in args.file:
#       if os.path.isfile(file):
#           file = open(args.file)
#            print(args.file, "\n")

    #TypeError: stat: path should be string, bytes, os.PathLike or integer, not list
    #for FILE in args.file:
    #   if os.path.isfile(file):
    #    file = open(args.file)
    #    print(args.file, "\n")

    #TypeError: stat: path should be string, bytes, os.PathLike or integer, not list
    #for FILE in args.file:
    #   if os.path.isfile(filehandle):
    #    filehandle = open(args.file)
    #    print(args.file, "\n")


    #else:
    #    args.file = io.StringIO(args.file + '\n')
    #else:
    #    args.file = open(args.file).read().rstrip()

    #return parser.parse_args()
    
    return args ## keep
# --------------------------------------------------
def main():

    args = get_args() ## keep 
       
    
    #filehandle = open(args.file, 'rt')
    
    #file = args.file
    #open(file) # "TypeError: expected str, bytes or os.PathLike object, not list"
    
    #file = open(args.file).read()
    #open(file).read() "TypeError: expected str, bytes or os.PathLike object, not list"
    
    
    #open(args.file)"TypeError: expected str, bytes or os.PathLike object, not list"
    
    #print(file) ##""TypeError: expected str, bytes or os.PathLike object, not list""

    #Only thing that sort of works when trying to see a file
    print(args.file) #"[<_io.TextIOWrapper name='fox.txt' mode='rt' encoding='UTF-8'>]"
    
    #filehandle.read()
    
    #variable for capturing line number
    #line_num = 0 ##keep
   
    #if numbered lines flag is true count the returns /n
    # add to line_num in a file and print,
    #for filehandle in args.file:
    #    if args.numbers == True:
    #        line_num += filehandle.count('/n')
    #       print(f'{line_num}   {filehandle.read(str)}') 
    #   
    #out_fh.close()
    
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
