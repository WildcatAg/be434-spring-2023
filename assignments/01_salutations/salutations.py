#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-03-04
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Greetings and salutations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='greeting',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        metavar='name',
                        type=str,
                        default='Stranger')
   
##    parser.add_argument('-e',
  ##                      '--excited',
    ##                    help='Include an exclamation point',
      ##                  metavar='str',
        ##                type=str,
          ##              default='False')
    
    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true')
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.excited == True:
        print(args.greeting + ', ' + args.name + '!')
    else:
        print(args.greeting + ', ' + args.name + '.')
# --------------------------------------------------
if __name__ == '__main__':
    main()
