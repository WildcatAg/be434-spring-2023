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
            start = ord('A')
            if char.isalpha() == False: #If its not a letter, reprint
                cip.append(char)
                # if decode is False:
                #     #start = ord('A')
                #     chartemp=char 
                #     shiftpos = ord(k) - start 
                #     pos = start + (ord(l) - start + shiftpos) % 26
                #     cip.append(chartemp) 
                #return ''.join([l for l in cip])
                return ''.join(char)
            else: #it is a letter    
                if decode is False: #if decode flag is false
                    for l, k in zip(line, cycle(shift)): #for each position in line and keyword
                        #sstart = ord('A')
                        shiftpos = ord(k) - start 
                        pos = start + (ord(l) - start + shiftpos) % 26
                        cip.append(chr(pos))
                    #print(l,k)
                    return ''.join([l for l in cip])
                #return ''.join(char)
            
            
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

#print(lines, textlen, keylen)
    #print(fh) ERROR: #<_io.TextIOWrapper name='inputs/fox.txt' mode='r' encoding='UTF-8'>
    #print(encrypt(fh, shift)) #calls the function
# for char2 in keyword: #keyword
# #print(keyword)
# keyindex = keyword.find(char2)
# #print(char2, keyindex)
# for i in range(textlen)
# for char1 in line: #text in from user
# #print(line)
# if char1.isalpha():
#     textindex = line.find(char1)
#     mathvar = textindex[i] + keyindex[i] % 26
#     print(mathvar)#print(char1, textindex)
# else:
#     chartemp=char1
#     textindex1 = textindex +1
#     #print(chartemp, textindex1)
#     mathvar = textindex % keyindex
#     print(mathvar)
    # mathvar = keyindex % textindex
    # print(mathvar)
    #                    len(key)):
    #         key.append(key[i % len(key)])
    # return("" . join(key))
    

    main()     






        # for char in line.upper():  # split to line to words
        #     if char in alpha:
        #         if decode is False:
        #             tempvar1 = (alpha.find(char) + shift) % 26
        #         else:
        #             tempvar1 = (alpha.find(char) - shift) % 26
        #         fho.write(alpha[tempvar1])
        #     else:
        #         fho.write(char)


# keylen = len(keyword) #counts the length of the keyword
# textlen = len(line) #counts length of line of text from read file
# keyindex = 0
# textindex = 0
# char1 = ""
# char2 =""
# def cipherText(string1, key):
#     cipher_text = []
#     for i in range(len(string1)):
#         x = (ord(string1[i]) + ord(key[i])) % 26
#         x += ord('A')
#         cipher_text.append(chr(x))
#     return("" . join(cipher_text))

# text = "code"
# key = "team"
# def solve(text, key):
#     cip = []
#     start = ord('a')
#     for l, k in zip(text, key):
#         shift = ord(k) - start
#         pos = start + (ord(l) - start + shift) % 26
#         cip.append(chr(pos))
#     return ''.join([l for l in cip])


#     args = get_args()
#     fh = open(args.file, "r") #brings in file
#     line = fh.readline() #reads a line
#     keyword = args.keyword #brings in keyword
#     keylen = len(keyword) #counts the length of the keyword
#     textlen = len(line) #counts length of line of text from read file
#     keyindex = 0
#     textindex = 0
#     char1 = ""
#     char2 =""
     
# # This function returns the# encrypted text generated# with the help of the key
# def cipherText(line, keyword, textlen):
#     cipher_text = []
#     for i in range(textlen):
#         x = (ord(line[i]) +
#              ord(keyword[i])) % 26
#         x += ord('A')
#         cipher_text.append(chr(x))
#     return("" . join(cipher_text))
     
# # This function decrypts the# encrypted text and returns# the original text
# def originalText(cipher_text, keyword):
#     orig_text = []
#     for i in range(len(cipher_text)):
#         x = (ord(cipher_text[i]) -
#              ord(keyword[i]) + 26) % 26
#         x += ord('A')
#         orig_text.append(chr(x))
#     return("" . join(orig_text))