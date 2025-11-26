# valid_palindrome.py - Given a string, determine if it is a palindrome considering only alphanumeric characters and ignoring cases.
#   Assume a valid palindrome can have odd count of alphanumerics.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from valid_palindrome import *

# RELOAD:
# import importlib;    import valid_palindrome;  importlib.reload(valid_palindrome);  from valid_palindrome import *


# The idea: scan from both sides, jump over non-alphanumerics


def valid_palindrome(s: str) -> bool:
    if ( (len(s) == 0) ):
        return(False)
    i1 = -1
    i2 = len(s)
    while (i1 <= i2):
        # advance i1, i2 to next alphanumerics
        i1 += 1
        print(f"@@ i1={i1}")
        while ( (i1 < i2) and (not s[i1].isalnum()) ):
            i1 += 1
        i2 -=1
        print(f"@@ i2={i2}")
        while ( (i1 < i2) and (not s[i2].isalnum()) ):
            i2 -= 1
        if ( (i1 <= i2) and (s[i1].upper() != s[i2].upper()) ):
            return(0)
    return(1)


def test__valid_palindrome():
    s1 = "1"
    s2 = "12"
    s3 = "121"
    s4 = "2112"
    s5 = "21123"
    s6 = "1234"
    s7 = "123421"
    for s in [s1, s2, s3, s4, s5, s6, s7]:
        print("=================================")
        print(f"Input: {s}")
        res = valid_palindrome(s)
        print(f"Result: {res}")
