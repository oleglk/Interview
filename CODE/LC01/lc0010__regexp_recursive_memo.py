# lc0010__regexp_recursive_memo.py
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#    '.' Matches any single character.​​​​
#    '*' Matches zero or more of the preceding element.
# Return a boolean indicating whether the matching covers the entire input string (not partial).

# See https://medium.com/@msaqib_9803/regular-expression-matching-coding-interview-question-1eb5e3f47fac

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0010__regexp_recursive_memo import *

# RELOAD:
# import importlib; import lc0010__regexp_recursive_memo; importlib.reload(lc0010__regexp_recursive_memo); from lc0010__regexp_recursive_memo import *


def regexp_recursive(inpStr: str, pattern: str) -> bool:
    memo = {}
    return regexp_recurse(inpStr, pattern, memo)


def regexp_recurse(inpStr: str, pattern: str, memo: dict) -> bool:
    if ( (inpStr, pattern) in memo ):
        #print("@@ >0")
        return memo[(inpStr, pattern)]

    # base case - if the pattern is exhausted
    if ( pattern == "" ):
        #print("@@ >1")
        result = (inpStr == "")  # success if the string exhausted too
    else:  # pattern not exhausted
        # cannot immediately fail if string exhausted - pattern may have '*'
        firstCharMatches = (len(inpStr) > 0) and ((inpStr[0] == pattern[0]) or (pattern[0] == '.'))
        # cannot immediately fail if !firstCharMatches - pattern may have '*'

        # check for '*' in the pattern
        if ( (len(pattern) > 1) and (pattern[1] == '*') ):
            # '*' appears
            # either use first atom (may match multiple chars) or skip it
            resIgnoreFirst = regexp_recurse(inpStr, pattern[2:], memo)
            resUseFirst = firstCharMatches and regexp_recurse(inpStr[1:], pattern, memo)
            #print("@@ >2")
            result = resIgnoreFirst or resUseFirst
        else:
            # '*' doesn't appear
            #print("@@ >3")
            result = firstCharMatches and regexp_recurse(inpStr[1:], pattern[1:], memo)

    memo[(inpStr, pattern)] = result
    return result


def test__regexp_recursive():
    tasks = [
        ["aa", "a"],    # False
        ["aa", "a*"],   # True
        ["ab", ".*"],   # True
        ["abc", "abc"], # True
        ["abc", "abd"], # False
        ["obc", "abc"], # False
        ["ab", "abc"],  # False
    ]
    for inpStr, pattern in tasks:
        print("================================")
        print(f"Input: {inpStr},  pattern={pattern}")
        res = regexp_recursive(inpStr, pattern)
        print(f"Result: {res}")

        
