# regexp_recursive.py - Regular Expression Matching ('.' and '*')

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from regexp_recursive import *

# RELOAD:
# import importlib; import regexp_recursive; importlib.reload(regexp_recursive); from regexp_recursive import *


def regexp_recurse(inpStr: str, pattern: str) -> bool:
    # base case is when the pattern is exhausted
    if ( len(pattern) == 0 ):
        return( len(inpStr) == 0 )

    firstCharMatches = (len(inpStr)) > 0) and
    ((inpStr[0] == pattern[0]) or (pattern[0] == '.'))
    
    # check for '*'
    if ( (len(pattern) > 1) and (pattern[1] == '*') ):
        # either ignore the 1st pattern char or use it - if 1st char matches
        # when 1st pattern char is used, it can match multiple input chars
        resIgnoreFirst = regexp_recurse(inpStr, pattern[2:])
        resUseFirst = firstCharMatches and regexp_recurse(inpStr[1:], pattern)
