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
        default="CIPHER",
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
#def main():
#    """Make a jazz noise here"""
    # args = get_args()
    # fh = open(args.file, "r")
    # fhread = fh.read()
    # keyword = args.keyword
    # keyindex = len(keyword)
    # #print(fhread, keyindex, keyword)
    # #print(encrypt(fh, keyword, keyindex))
    # print(caeser(fh, keyword, keyindex))
# --------------------------------------------------


def main():
    args = get_args()
    fh = open(args.file, "r")
    fho = args.outfile
    shift = args.keyword
    decode = args.decode
    #output = encrypt(fh, shift, fho, decode)
    line = fh.readline() #reads a line
    textlen = len(line)
    keylen = len(shift)
    #print(output)

    #print(line, textlen, keylen)
    #print(fh) #ERROR: #<_io.TextIOWrapper name='inputs/fox.txt' mode='r' encoding='UTF-8'>
    print(encrypt(fh, shift, fho, decode)) #calls the function
    
    for char2 in shift: #keyword
        #print(keyword)
        keyindex = shift.find(char2)
        #print(char2, keyindex)
    for i in range(textlen):
        for char1 in line: #text in from user
        #print(line)
            if char1.isalpha():
                textindex = line.find(char1)
                #mathvar = textindex[i] + keyindex[i] % 26
                #print(mathvar)#print(char1, textindex)
            else:
                chartemp=char1
                textindex1 = textindex +1
                #print(chartemp, textindex1)
                mathvar = textindex % keyindex
                print(mathvar)
    
    #mathvar = keyindex % textindex
    
    #print(mathvar)

def encrypt(fh, shift, fho, decode):
    #alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #start = ord('A')
    table = []
    
    for line in fh.readlines():  # reading in line 
        #start = ord('A')
        for char in line: #break into characters
            if char.upper().isalpha() == True: #If a letter
                if decode is False: #if decode flag is false
                    for l, k in zip(line, cycle(shift)): #for each position in line and keyword
                        start = ord('A') #restart index each time
                        shiftpos = ord(k) - start 
                        pos = start + (ord(l) - start + shiftpos) % 26
                        table.append(chr(pos))
                        #fho.write((chr(pos)))
                        #print(l,k)
                    return ''.join([l for l in table])
                else: #decode
                    shiftpos = ord(k) + start 
                    pos = start - (ord(l) + start - shiftpos) % 26
            else: #it is not a letter    
                print(char)
                table.append(char)
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
##------------END

# #---------------------------------------------------or
#     args = get_args()
#     fh = open(args.file, "r")
#     fho = args.outfile
#     decode = args.decode
#     keyword = args.keyword #brings in keyword
#     line = fh.readline() #reads a line
#     output = vign(line, keyword)
#     print(output)


# def vign(line, keyword):
#     cipher_text = []
#     for line1 in line:  # reading in line ###.read() also works
#         for i in range(len(line1)):
#             x = (ord(line1[i]) + ord(keyword[i])) % 26
#             x += ord('A')
#             cipher_text.append(chr(x))
#     return("" . join(cipher_text))
# #----------------------- end

if __name__ == "__main__":
    main()
