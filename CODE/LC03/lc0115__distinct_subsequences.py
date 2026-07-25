# lc0115__distinct_subsequences.py
# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0115__distinct_subsequences import *

# RELOAD:
# import importlib;    import lc0115__distinct_subsequences;  importlib.reload(lc0115__distinct_subsequences);  from lc0115__distinct_subsequences import *

# The idea: starting from right, recurse on numbers of chars left in s and t. Treat cases of match and mismatch in the currently last char.
# See https://algomaster.io/learn/dsa/distinct-subsequences


def distinct_subsequences(s: str|None, t: str|None) -> int:
    def distinct_subsequences_recurse(i: int, j: int) -> int:
        """Searches for subsequences in strings of lengths i, j from beginning"""
        # base cases
        if ( j == 0 ):  # found complete subsequence - take nothing more
            return 1
        if ( i == 0 ):  # s exhausted while no subsequence completed - no way
            return 0
        if ( (i,j) in memo ):
            return memo[(i,j)]

        # recursive cases - char s[i-1] matched t[j-1] or not
        # if matched, we either use s[i-1] to "serve" t[i-1] or not
        # if not matched, we cannot use s[i-1] to "serve" t[i-1]
        numSubseqIfNotUseLastInS = distinct_subsequences_recurse(i-1, j)
        if ( s[i-1] != t[j-1] ):
            result = numSubseqIfNotUseLastInS
        else:  # char s[i-1] matched t[j-1]
            numSubseqIfUseLastInS = distinct_subsequences_recurse(i-1, j-1)
            result = numSubseqIfNotUseLastInS + numSubseqIfUseLastInS
        memo[(i,j)] = result
        return result
    ##
    memo = {}
    if ( s is None ):  return 0
    if ( t is None ):  return 1
    return distinct_subsequences_recurse(len(s), len(t))
##


def test__distinct_subsequences():
    tasks = [
        ["rabbbit", "rabbit"],  # 3
        ["babgbag", "bag"],     # 5
    ]
    for s, t in tasks:
        print("==================================================")
        print(f"Input: {s},  {t}")
        res = distinct_subsequences(s, t)
        print(f"Result: {res}")
##
