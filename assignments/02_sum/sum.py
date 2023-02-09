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
        description="Summing", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "nums", help="Numbers to add", metavar="INT", nargs="+", type=int, default=0
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # careful here, we always use lowercase for strings because upper can be a reserved words
    # INT = args.int

    # create a total
    total = 0

    # create a list for putting the numbers from the command line as strings
    str_numbers = []

    for num in args.nums:
        total += num

        # add the num to the list as a string

    # print the number statement and total (do this based on the readme)
    summed_up = ' + '.join(str_numbers)

    print(total)


# --------------------------------------------------
if __name__ == "__main__":
    main()
