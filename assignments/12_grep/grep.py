#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-20
Purpose: Python grep
"""

#/bin/import_list.txt
import argparse
#import csv
#import emoji
#import io
import os
#import random
import re
#import string
import sys
#from pprint import pprint
#from pydash import flatten
#from tabulate import tabulate
#from typing import List, NamedTuple, Optional
#from typing import List, Optional, TypedDict

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')
    
    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)')
    
    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default= sys.stdout)

    args = parser.parse_args()
    
    fh = re.search("txt\b", args.file)
    #fh = os.path.isfile(args.file)
    patternhandle = str(args.pattern)

    if patternhandle:
        if not fh:
        #if not args.file:
        #if os.path.isfile(args.file) == False:
            parser.error(f'--col "{args.file}" No such file or directory:')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    #search_var = args.pattern
    new_list = []
    idx = 1
    temp_line = ""
    
    if args.insenstive:
        for line in args.file:    
            #if temp_line.get(args.pattern.upper()) and temp_line.get(args.pattern.lower()) is None:
            if re.IGNORECASE(re.search(args.pattern)) == True:
                new_list = ""
                print (new_list)
            else:
                new_list = new_list.insert(idx, temp_line)

    else:
        for line in args.file:
            temp = line.rstrip().split()
            temp_search = re.search(args.pattern, temp)#if args.pattern in temp_line: 
            if temp_search:
        #if re.search(args.pattern, temp) == True:
                new_list.insert(idx, line)
        
    if args.outfile: #if flag, write each line
        #args.outfile.write(new_list)
        args.outfile.write(f'"{args.file.name}" {new_list}''\n')
        print(args.outfile)
         #   print(f'"{args.outfile.name}": {TEXT RETURNED} "\n"')
        #else:
         #   print(f'"{args.outfile.name}": {TEXT RETURNED} "\n"')
    else:
        print(f'"{args.file.name}" {new_list}')
    
    #The output should include the name of the file when there is more than one file argument
    #print(f'"{args.outfile.name}": {TEXT RETURNED} "\n"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
