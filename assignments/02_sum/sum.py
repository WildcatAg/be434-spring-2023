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
        "INT", help="Numbers to add", metavar="INT", nargs="+", type=int, default=0
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    INT = args.INT
    print(INT)

    #for n in INT:
        # hint: str.join
    k = sum(INT)
    print(k)


# --------------------------------------------------
if __name__ == "__main__":
    main()
