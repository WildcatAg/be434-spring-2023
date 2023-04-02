#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-02
Purpose: Create Workout Of (the) Day (WOD)
"""

import argparse
import csv

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='num',
                        type=int,
                        default=4)

    parser.add_argument('-f',
                        '--file',
                        help='Input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.file.name)


# --------------------------------------------------
if __name__ == '__main__':
    main()
