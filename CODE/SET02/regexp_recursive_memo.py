# regexp_recursive_memo.py - Regular Expression Matching ('.' and '*') - recursive with memoization. '.' means any char, '*' means 0 or more occurences of preceding char.
# See https://medium.com/@msaqib_9803/regular-expression-matching-coding-interview-question-1eb5e3f47fac

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from regexp_recursive_memo import *

# RELOAD:
# import importlib; import regexp_recursive_memo; importlib.reload(regexp_recursive_memo); from regexp_recursive_memo import *

def regexp_recursive(inpStr: str, pattern: str) -> bool:
    memo = {}
    return regexp_recurse(inpStr, pattern, memo)


def regexp_recurse(inpStr: str, pattern: str, memo: dict) -> bool:
    if ( (inpStr, pattern) in memo ):
        return memo[(inpStr, pattern)]
               
    # base case is when the pattern is exhausted
    if ( len(pattern) == 0 ):
        result = (len(inpStr) == 0)  # true if string also exhausted
    else:  # pattern not exhausted
        firstCharMatches = (len(inpStr) > 0) and ((inpStr[0] == pattern[0]) or (pattern[0] == '.'))
    
        # check for '*'
        if ( (len(pattern) > 1) and (pattern[1] == '*') ):  # with '*'
            # either ignore the 1st pattern char or use it - if 1st char matches
            # when 1st pattern char is used, it can match multiple input chars
            resIgnoreFirst = regexp_recurse(inpStr, pattern[2:], memo)
            resUseFirst = firstCharMatches and regexp_recurse(inpStr[1:], pattern, memo)
            result = resIgnoreFirst or resUseFirst
        else:                                                # without '*'
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
        ["obc", "abc"]  # False
    ]
    for inpStr, pattern in tasks:
        print("================================")
        print(f"Input: {inpStr},  pattern={pattern}")
        res = regexp_recursive(inpStr, pattern)
        print(f"Result: {res}")
