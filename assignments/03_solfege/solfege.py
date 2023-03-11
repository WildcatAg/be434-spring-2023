#!/usr/bin/env python3
# This class is derailing me hard 
    # create a dictionary with the notes and matching phrases

    # write a for loop to go through each "note" from the user 
    # in args.solfege; 
  
    # make sure the "note" is in the dictionary
    # and print expected phrase for each note

    # or tell the user you don't know the note if it doesn't exist
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

    # you do indeed need the nargs="+", to say you want one or more
    ### nargs seems to be the one place things blow up consistently for me, which is why you see me commenting it out. 
    parser.add_argument('text', 
                        metavar='str', 
                        nargs="+",
                        help='Solfege'
                        )

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Solfege"""

    args = get_args()
    
    text = args.text
    
    #create the dictionary - jump5 thing
    #songtable = {'Do':'Do, A deer, a female deer', 'Re':'Re, A drop of golden sun', 'Mi':'Mi, A name I call myself','Fa':'Fa, A long long way to run','Sol':'Sol, A needle pulling thread','La':'La, A note to follow sol','Ti':'Ti, A drink with jam and bread'}
### Got it. Thank you. This was my way of handling the comma insertion in an easier way, since I knew the response was fixed.



    # the key should be the "note" and the value should be the "phrase"  
    songtable = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread',
    }

    
    #create list to accept input
    #text is already a list of user inputs from the command line, you don't need to split. 
    #printtable = text.split() 
    ###OK. This was what I was attempting to do since I was blowing up with two words of input, 
    ###I thought a list could be created and then read in to be processed piece be piece as appended.

    #Create error text
    #errortext = 'I don\'t know "' + text + '"'
    
    #create output
    #printedtext = '' #songtable.get(text, errortext)

    #Loop 
    for str in args.text:
        # each time you are overwriting this variable, so it only works for one note, which is the last one
        ###I thought about that, so I tried a += thinking it would append the same way, but then the line just 
        ### repeated itself as you describe
       
        # printedtext = songtable.get(text, errortext)
        # instead let's create this as we go
        # first we need to see if the note exists
       
        if str in songtable:
            print(f'{str}, {songtable.get(str)}')
        else:
            print(f'I don\'t know "{str}"')
### Waaaaaay cleaner. Thank you for pointing this out. 

    #print(printedtext)

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
