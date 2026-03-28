# lc0044__wildcard_matching.py
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
#    '?' Matches any single character.
#    '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0044__wildcard_matching import *

# RELOAD:
# import importlib; import lc0044__wildcard_matching; importlib.reload(lc0044__wildcard_matching); from lc0044__wildcard_matching import *


def wildcard_recursive(inpStr: str, pattern: str) -> bool:
    memo = {}
    return wildcard_recurse(inpStr, 0, pattern, 0, memo)
##


def wildcard_recurse(s: str, sIdx: int, p: str, pIdx: int, memo: dict) -> bool:
    if ( (sIdx, pIdx) in memo ):
        return memo[(sIdx, pIdx)]
    lenS = len(s);  lenP = len(p)

    # base case is when pattern exhausted
    if ( pIdx == lenP ):
        result = (sIdx == lenS)  # match if string exhausted too
    else:  # pattern not exhausted
        firstCharMatches = (sIdx < lenS) and ((s[sIdx] == p[pIdx]) or (p[pIdx] == '?'))

        # check for '*'
        if ( (pIdx < lenP-1) and (p[pIdx+1] == '*') ):  # '*'
            # "use" and "skip" pertain to pattern
            resUseFirst = firstCharMatches and wildcard_recurse(s, sIdx+1, p, pIdx, memo)
            resSkipFirst = wildcard_recurse(s, sIdx, p, pIdx+2, memo)
            result = resUseFirst or resSkipFirst
        else:                                           # no '*'
            result = firstCharMatches and wildcard_recurse(s, sIdx+1, p, pIdx+1, memo)

    memo[(sIdx, pIdx)] = result
    return result
##


def test__wildcard_recursive():
    tasks = [
        ["aa", "a"],    # False
        ["aa", "a*"],   # True
        ["ab", ".*"],   # True
        ["abc", "abc"], # True
        ["abc", "abd"], # False
        ["obc", "abc"], # False
        ["aa", "*"],    # True
        ["cb", ".a"],   # False
    ]
    for inpStr, pattern in tasks:
        print("================================")
        print(f"Input: {inpStr},  pattern={pattern}")
        res = wildcard_recursive(inpStr, pattern)
        print(f"Result: {res}")

            
