# regexp_matching.py
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '.' and '*' where:
#    '.' means any char,
#    '*' means 0 or more occurences of preceding char.
# The matching should cover the entire input string (not partial).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from regexp_matching import *

# RELOAD:
# import importlib; import regexp_matching; importlib.reload(regexp_matching); from regexp_matching import *


def regexp_recursive(inpStr: str, pattern: str) -> bool:
    memo = {}
    return regexp_recurse(inpStr, 0, pattern, 0, memo)
##


def regexp_recurse(s: str, sIdx: int, p: str, pIdx: int, memo: dict) -> bool:
    if ( (sIdx, pIdx) in memo ):
        return memo[(sIdx, pIdx)]
    lenS = len(s);  lenP = len(p)

    # base case is when pattern exhausted
    if ( pIdx == lenP ):
        result = (sIdx == lenS)  # match if string exhausted too
    else:  # pattern not exhausted
        firstCharMatches = (sIdx < lenS) and ((s[sIdx] == p[pIdx]) or (p[pIdx] == '.'))

        # check for '*'
        if ( (pIdx < lenP-1) and (p[pIdx+1] == '*') ):  # '*'
            # "use" and "skip" pertain to pattern
            resUseFirst = firstCharMatches and regexp_recurse(s, sIdx+1, p, pIdx, memo)
            resSkipFirst = regexp_recurse(s, sIdx, p, pIdx+2, memo)
            result = resUseFirst or resSkipFirst
        else:                                           # no '*'
            result = firstCharMatches and regexp_recurse(s, sIdx+1, p, pIdx+1, memo)

    memo[(sIdx, pIdx)] = result
    return result
##


def test__regexp_recursive():
    tasks = [
        ["aa", "a"],    # False
        ["aa", "a*"],   # True
        ["ab", ".*"],   # True
        ["abc", "abc"], # True
        ["abc", "abd"], # False
        ["obc", "abc"], # False
        ["aa", "*"],    # False
        ["cb", ".a"],   # False
    ]
    for inpStr, pattern in tasks:
        print("================================")
        print(f"Input: {inpStr},  pattern={pattern}")
        res = regexp_recursive(inpStr, pattern)
        print(f"Result: {res}")

            
