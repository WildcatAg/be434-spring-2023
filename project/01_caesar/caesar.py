#!/usr/bin/env python3
"""
Author : myles <myles@localhost>
Date   : 2023-04-29
Purpose: caesar shift
"""
# /bin/import_list.txt
import argparse

# import csv
# import emoji
# import io
import os

# import random
# import re
# import string
import sys

# from pprint import pprint
# from pydash import flatten
# from tabulate import tabulate
# from typing import List, NamedTuple, Optional
# from typing import List, Optional, TypedDict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="caesar shift",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("file", metavar="FILE", type=str, help="Input file")
    parser.add_argument(
        "-n",
        "--number",
        help="A number to shift",
        metavar="NUMBER",
        type=int,
        default=3,
    )
    parser.add_argument("-d", "--decode", help="A boolean flag", action="store_true")
    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )  # "std.out")

    args = parser.parse_args()

    # fh = args.file
    # if os.path.isfile(file) == False:
    if os.path.isfile(args.file) == False:
        # parser.error(f"No such file or directory: '{sys.stdin}'")
        parser.error(f"No such file or directory: '{args.file}'")
    return args


# --------------------------------------------------
def main():
    # """Make a jazz noise here"""
    args = get_args()
    fh = open(args.file, "r")
    fho = args.outfile
    shift = args.number
    decode = args.decode
    #     #alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #     # A - Z = 65 - 90
    #     # a - z = 97 - 122
    #     lower = range(97,123)
    #     upper = range(65,91)
    output = encrypt(fh, shift, fho, decode)
    # print(output)


def encrypt(fh, shift, fho, decode):
    # lower = range(97,123)
    # upper = range(65,91)
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for line in fh.readlines():  # reading in line ###.read() also works
        # print(line)
        for char in line.upper():  # split to line to words
            # print(tempvar)
            # tempasc = chr(tempvar)
            # for char in tempvar:
            if char in alpha:
                # print(char, alpha.find(char))
                if decode is False:
                    tempvar1 = (alpha.find(char) + shift) % 26
                else:
                    tempvar1 = (alpha.find(char) - shift) % 26
                fho.write(alpha[tempvar1])
            else:
                fho.write(char)
        # fho.write(" ")
    # fho.write('\n')


#     fh = args.file
#     shift = args.number

#     print(encrypt(fh, shift))
#     # if args.outfile:
#     #    args.outfile = encrypt(fh, shift).write()
#     # print(args.outfile)
#     # else:
#     #    print ("Text  : " + fh)
#     #    print ("Shift : " + str(shift))
#     #    print ("Cipher: " + encrypt(fh,shift))

# # # --------------------------------------------------
# # # #---------------------------------------------------
# # def encrypt(fh,shift):
# # #% returns remainder
# #     encryption = ""
# #     for tempvar in fh:
# #         for letter in tempvar.split():
# #     # for letter in range(len(fh)):
# #             tempvar = fh[shift]
# #             tempvar = letter
# #         # Encrypt uppercase characters
# #         # A - Z = 65 - 90
# #         # a - z = 97 - 122
# #         if (letter.isupper()):
# #         #if (tempvar.isupper()):
# #             encryption += chr((ord(letter) + shift+65) % 26 + 65)
# #         # Encrypt lowercase characters
# #         else:
# #             encryption += chr((ord(letter) + shift + 97) % 26 + 97)
# #     return encryption
# # # #check the above function
# # #---------------------------------------------------
# # # # --------------------------------------------------
if __name__ == "__main__":
    main()
