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

    # base case 1: string exhausted;
    # check if pattern exhausted or has only *-s left
    if ( sIdx >= lenS ):
        result = (pIdx >= lenP) or ((p[pIdx] == '*') and wildcard_recurse(s, sIdx, p, pIdx+1, memo))

    elif ( pIdx >= lenP ):
        # base case 2: pattern exhausted but string - not
        result = False
                                    
    else:  # neither string nor pattern exhausted
        if ( p[pIdx] == '*' ):
            resMatchOne  = wildcard_recurse(s, sIdx+1, p, pIdx+1, memo)
            resMatchMany = wildcard_recurse(s, sIdx+1, p, pIdx,   memo)
            resMatchNone = wildcard_recurse(s, sIdx,   p, pIdx+1, memo)
            result = resMatchOne or resMatchMany or resMatchNone
        elif ( (s[sIdx] == p[pIdx]) or (p[pIdx] == '?') ):
            # exact match or '?' in pattern; continue from next positions
            result = wildcard_recurse(s, sIdx+1, p, pIdx+1, memo)
        else:
            # mismatch in the current position
            result = False

    memo[(sIdx, pIdx)] = result
    return result
##


def test__wildcard_recursive():
    tasks = [
        ["aa", "a"],    # False
        ["aa", "a*"],   # True
        ["ab", "?*"],   # True
        ["abc", "abc"], # True
        ["abc", "abd"], # False
        ["obc", "abc"], # False
        ["aa", "*"],    # True
        ["cb", "?a"],   # False
    ]
    for inpStr, pattern in tasks:
        print("================================")
        print(f"Input: {inpStr},  pattern={pattern}")
        res = wildcard_recursive(inpStr, pattern)
        print(f"Result: {res}")

            
