#!/usr/bin/env python3

# Continuing to work on this, despite not being able to run it. 1/29/23
# Damn this is ticking me off

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n',
                        '--name',
                        metavar="name",
                        default='World',
                        help="Name to greet")
    return parser.parse_args()


def main():

    args = get_args()
    name = args.name
    print("Hello," + name + "!")


if __name__ == '__main__':
    main()
