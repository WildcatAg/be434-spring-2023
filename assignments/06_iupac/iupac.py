#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-02-28
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
#blows up at test 1

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='SEQ',
                        #nargs = '+',
                        #type=str,
                        help='Input sequence(s)')


    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdin)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    printedtext = ''
    trans = {"R": "[AG]","Y": "[CT]","S": "[GC]","W": "[AT]","K": "[GT]","M": "[AC]","B": "[CGT]","D": "[AGT]","H": "[ACT]","V": "[ACG]","N": "[ACGT]",}
    errortext = 'XXXXX'
    #file_arg = args.outfile
    sequence1 = args.sequence
    sequence2 = sequence1.split()
    #sequence1 = args.sequence.split()
    

    #Check if input is a file or string
    #If file, open for translate and print
    #If string, translate and print
    #if os.path.isfile(file_arg):
        #open(file_arg).read()
    
    #Loop 
    for SEQ in args.sequence:
        printedtext = trans.get(sequence1, sequence1)
        #printedtext = trans.get(sequence1, errortext)
        
    print(printedtext)

    #print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    #print(f'positional = "{pos_arg}"')



# --------------------------------------------------
if __name__ == '__main__':
    main()
