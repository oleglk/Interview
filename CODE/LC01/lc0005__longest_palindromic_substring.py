# lc0005__longest_palindromic_substring.py
# Given a string s, return the longest palindromic substring in s.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0005__longest_palindromic_substring import *

# RELOAD:
# import importlib;    import lc0005__longest_palindromic_substring;  importlib.reload(lc0005__longest_palindromic_substring);  from lc0005__longest_palindromic_substring import *


# The idea: expand palindrome candidates around each char and around each pair of consequent chars - former for odd-length palindrome, latter for even-length palindrome.


def longest_str(s1, s2, s3):
    if ( len(s1) >= len(s2) ):
        return(s1 if len(s1) >= len(s3)  else  s3)
    else:
        return(s2 if len(s2) >= len(s3)  else  s3)


def longest_palindromic_substring(s: str) -> str:
    if ( not s ):
        return ""
    if (len(s) == 1):
        return s
    best = ""
    for i in range(0, len(s)-1):
        best = longest_str(best, expand(s, i, i), expand(s, i, i+1))
    return(best)

    
def expand(s: str, l: int, r: int) -> str:
    """Expands to both sides while l...r is palindrome."""
    while ( (l >= 0) and (r < len(s)) and (s[l] == s[r]) ):
        l -= 1
        r += 1
    # previous substring could have been palindromic
    return s[l+1:r]  if (s[l+1] == s[r-1])  else  ""



def test__longest_palindromic_substring():
    tasks = [
        "012321",        # 12321
        "01",            # 0
        "0",             # 0
        "012210",        # 012210
        "0123332101",    # 012333210
        "01100123210",   # 0123210
        "babad",         # bab
        "cbbd"           # bb
    ]
    for s in tasks:
        print("=================================")
        print(f"Input: {s}")
        res = longest_palindromic_substring(s)
        print(f"Result: {res}")
