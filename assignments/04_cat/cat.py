#!/usr/bin/env python3

"""
Author : myles <myles@localhost>
Date   : 2023-03-04
Purpose: Python cat
"""

import argparse

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
    return parser.parse_args()

#---------------------------
    #args = parser.parse_args()
 
    
# --------------------------------------------------
def main():

    args = get_args() ## keep 
       
    # This is how you can update it to work
    for filehandle in args.file:
        # go through each line, and save the line number if you need it
        for line_num, line in enumerate(filehandle, start=1):
            if args.numbers == True:
                # print the line number if requested
                print(f'{line_num:>6}\t{line.rstrip()}')
            else:
                # otherwise just print the line
                print(line, end='')
    
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
