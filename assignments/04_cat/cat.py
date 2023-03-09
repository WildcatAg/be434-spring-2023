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

    parser.add_argument('FILE',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs = "+",
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-n',
                        '--numbers',
                        help='Number the lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')

    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
