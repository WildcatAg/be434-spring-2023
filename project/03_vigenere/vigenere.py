#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-29
Purpose: vigenere cipher
"""
# /bin/import_list.txt
import argparse
import io
import os
import string
import sys
from itertools import cycle
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="vigenere cipher",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("file", metavar="FILE", type=str, help="Input file")

    parser.add_argument(
        "-k",
        "--keyword",
        help="A keyword",
        metavar="KEYWORD",
        type=str,
        default="TEST",
    )

    parser.add_argument("-d", "--decode", help="A boolean flag", action="store_true")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    args = parser.parse_args()

    if os.path.isfile(args.file) == False:
        # parser.error(f"No such file or directory: '{sys.stdin}'")
        parser.error(f"No such file or directory: '{args.file}'")
    return args
# --------------------------------------------------
def main():
    args = get_args()
    fh = open(args.file, "r")
    fho = args.outfile
    shift = args.keyword
    decode = args.decode
    output = encrypt(fh, shift, fho, decode)
    line = fh.readline() #reads a line
    print(output)

def encrypt(fh, shift, fho, decode):
    #alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #start = ord('A')
    cip = []
    
    for line in fh.readlines():  # reading in line 
        #start = ord('A')
        for char in line: #break into characters
            if char.upper().isalpha() == True: #If its not a letter, reprint
                if decode is False: #if decode flag is false
                    for l, k in zip(line, cycle(shift)): #for each position in line and keyword
                        start = ord('A')
                        shiftpos = ord(k) - start 
                        pos = start + (ord(l) - start + shiftpos) % 26
                        cip.append(chr(pos))
                        #fho.write((chr(pos)))
                        #print(l,k)
                    return ''.join([l for l in cip])
                    
                else: #decode
                    shiftpos = ord(k) + start 
                    pos = start - (ord(l) + start - shiftpos) % 26
            else: #it is a letter    
                print(char)
                cip.append(char)
                fho.write(char)
                #fho.write(cip.append(char))
                # if decode is False:
                #     #start = ord('A')
                #     chartemp=char 
                #     shiftpos = ord(k) - start 
                #     pos = start + (ord(l) - start + shiftpos) % 26
                #     cip.append(chartemp) 
                #return ''.join([l for l in cip])
            return ''.join(char)
            # if char in alpha:
            #     if decode is False:
            #         tempvar1 = (alpha.find(char) + shift) % 26
            #     else:
            #         tempvar1 = (alpha.find(char) - shift) % 26
            #     fho.write(alpha[tempvar1])
            # else:
            #     fho.write(char)
if __name__ == "__main__":
    main()
