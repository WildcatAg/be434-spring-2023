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

    parser.add_argument('text', 
                        metavar='str', 
                        #nargs="+",
                        help='Solfege'
                        )

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Solfege"""

    args = get_args()
    
    text = args.text
    
    #create the dictionary - jump5 thing
    songtable = {'Do':'Do, A deer, a female deer', 'Re':'Re, A drop of golden sun', 'Mi':'Mi, A name I call myself','Fa':'Fa, A long long way to run','Sol':'Sol, A needle pulling thread','La':'La, A note to follow sol','Ti':'Ti, A drink with jam and bread'}
    
    #create list to accept input
    printtable = text.split() 
    
    #Create error text
    errortext = 'I don\'t know "' + text + '"'
    
    #create output
    printedtext = '' #songtable.get(text, errortext)

    #Loop 
    for str in args.text:
        printedtext = songtable.get(text, errortext)
  
    print(printedtext)

        #print(printtable += printedtext + "\n")
        #print(printtable, "\n")
    
    #for text in args.text:
        #if text.strip() in songtable:
            #printedtext = songtable.get(text, errortext)
     ##   else: 
       ##     printedtext = errortext

  

# --------------------------------------------------
if __name__ == '__main__':
    main()
