#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-02-12
Purpose: Jump the five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
