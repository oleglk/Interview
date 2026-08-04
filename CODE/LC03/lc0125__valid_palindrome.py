# lc0125__valid_palindrome.py
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0125__valid_palindrome import *

# RELOAD:
# import importlib;    import lc0125__valid_palindrome;  importlib.reload(lc0125__valid_palindrome);  from lc0125__valid_palindrome import *

# The idea: compare leftmost and rightmost characters while skipping non-alphanumerics.

def valid_palindrome(s: str) -> bool:
    if ( (s is None) or (s == "") ):
        return True
    leftIdx = 0;  rightIdx = len(s) - 1
    while ( leftIdx < rightIdx ):
        # skip non-alphanumerics on both sides
        while ( (leftIdx < rightIdx) and (not s[leftIdx].isalnum()) ):
            leftIdx += 1
        while ( (leftIdx < rightIdx) and (not s[rightIdx].isalnum()) ):
            rightIdx -= 1
        if ( s[leftIdx].lower() != s[rightIdx].lower() ):
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
##


def test__valid_palindrome():
    tasks = [
        "A man, a plan, a canal: Panama",  # True
        "race a car",                      # False
        " "                                # True
    ]
    for s in tasks:
        print("=============================================")
        print(f"Input: {s}")
        res = valid_palindrome(s)
        print(f"Result: {res}")
##
