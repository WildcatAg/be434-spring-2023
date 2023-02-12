#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-02-12
Purpose: Solfege
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Solfege')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Solfege"""

    args = get_args()
    
    
    songtable = {'Do':'Do, A deer, a female deer', 'Re':'Re, A drop of golden sun', 'Mi':'Mi, A name I call myself','Fa':'Fa, A long long way to run','Sol':'Sol, A needle pulling thread','La':'La, A note to follow sol','Ti':'Ti, A drink with jam and bread'}
    text = args.text
    
    for char in args.text:
        print(songtable.get(char, char), end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
