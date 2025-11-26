# longest_palindrome.py - Given a string s, return the longest palindromic substring in s.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from longest_palindrome import *

# RELOAD:
# import importlib;    import longest_palindrome;  importlib.reload(longest_palindrome);  from longest_palindrome import *


# The idea: expand palindrome candidates around each char and around each pair of consequent chars - former for odd-length palindrome, latter for even-length palindrome.

def longest_palindrome(s: str) -> str:
    """Returns longest palindromic substring of 's'"""
    best = ''
    if ( len(s) == 0 ):
        return('')
    if ( len(s) == 1 ):  # not picked by the loop
        return(s)
    for i in range(0, len(s)-1):
        best = longest_str(best,
                           longest_str(expand(s, i, i), expand(s, i, i+1)))
    # would be dummy: best = longest_str(best, expand(s, len(s)-1, len(s)-1)
    return(best)


def expand(s: str, i: int, j: int) -> str:
    """Expands palindrome-candidate substring around indices 'i', 'j' in 's'.
       'i' and 'j' must be consequent or equal.
       Returns the longest palindrome substring found."""
    if ( (i < 0) or (i >= len(s)) or (j < 0) or (j >= len(s))
         or (j < i) or ((j - i) > 1)  ):
        return('')
    maxExp = min(i, len(s) - j - 1)  # how far can expand from this center
    bestShift = -1  # for max expansion while keep being palindrome
    for shift in range(0, maxExp+1):
        if ( s[i-shift] == s[j+shift] ):
            bestShift = shift
        else:
            break
    if ( bestShift >= 0 ):
        res = s[i - bestShift  :  j + bestShift + 1]
    else:
        res = s[i] if ( i == j )  else  ''
    #print(f"@@ expand('{s}', {i}, {j}) => '{res}'")
    return(res)


def longest_str(s1, s2):
    return(s1 if len(s1) >= len(s2)  else  s2)


def longest_palindrome__ChatGPT(s):
    if not s:
        return ''
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    best = ''
    for i in range(len(s)):
        best = max(best, expand(i, i), expand(i, i+1), key=len)
    return best



def test__longest_palindrome():
    s1 = "012321";  s2 = "01";  s3 = "0";  s4 = "012210";
    s5 = "0123332101";  s6 = "01100123210"
    for s in [s1, s2, s3, s4, s5, s6]:
        print("=================================")
        print(f"Input: {s}")
        res = longest_palindrome(s)
        print(f"Result: {res}")
