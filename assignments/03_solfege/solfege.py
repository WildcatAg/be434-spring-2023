#!/usr/bin/env python3
# This class is derailing me hard 
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
    
    text = args.text
    
    #create the dictionary - jump5 thing
    songtable = {'Do':'Do, A deer, a female deer', 'Re':'Re, A drop of golden sun', 'Mi':'Mi, A name I call myself','Fa':'Fa, A long long way to run','Sol':'Sol, A needle pulling thread','La':'La, A note to follow sol','Ti':'Ti, A drink with jam and bread'}
    printedtext = ''
    for str in args.text:
        printedtext = songtable.get(text, text)
    
    print(printedtext)


# --------------------------------------------------
if __name__ == '__main__':
    main()
