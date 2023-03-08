#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@LAPTOP-RG1541RL>
Date   : 2023-02-05
Purpose: Summing
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Summing", 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
                        "number", 
                        help="Numbers to add", 
                        metavar="INT", 
                        nargs="+", 
                        type=int, 
                        default=0
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    # careful here, we always use lowercase for strings because upper can be a reserved words
    value = args.number
    
    # create a list for putting the numbers from the command line as strings
    listlength = len(value)
    numlist = ''
    numlista = ''
    # create a total
    total = 0

    for value in args.number:
        total += value
        numlist += str(value)
        numlista = ' + '.join(numlist)

    if listlength == 1:
        print(str(value)+' = '+str(value))
    else:
        print(str(numlista) +' = '+str(total))

    #print(listlength)    
# --------------------------------------------------
if __name__ == "__main__":
    main()
