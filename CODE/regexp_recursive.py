# regexp_recursive.py - Regular Expression Matching ('.' and '*')

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from regexp_recursive import *

# RELOAD:
# import importlib; import regexp_recursive; importlib.reload(regexp_recursive); from regexp_recursive import *


def regexp_recurse(inpStr: str, pattern: str, iS: int, iP: int) -> bool:
    """Check matching of inpStr[iS:] by pattern[iP:]."""
    print(f"@@ regexp_recurse({inpStr}, {pattern}, {iS}, {iP})")
    lenS = len(inpStr)
    lenP = len(pattern)
    if ( (iS >= lenS) and (iP >= lenP) ):
        return True    # both exhausted
    # if ( (iS >= lenS) and (iP < lenP) ):  # ??? What about '*' ???
    #     return False
    if ( (iS >= lenS) and (iP < lenP) ):
         if ( (iP == lenP-1) and (pattern[iP] == '*') ):
             return True  # ???
         else:
             return False   # only string exhausted
    if ( (iS < lenS) and (iP >= lenP) ):
        return False   # only pattern exhausted

    if ( (iP < (lenP-1)) and (pattern[iP+1] == '*') ):
        # next character is '*'
        ret1 = ret2 = False
        if ( inpStr[iS] == pattern[iP] ):
            # try to match the rest of str with the same pattern again
            ret1 = regexp_recurse(inpStr, pattern, iS+1, iP)
        # treat * as matching zero occurrences, advance pattern to after *
        ret2 = regexp_recurse(inpStr, pattern, iS, iP+2)
        return (ret1 or ret2)
    else:
        # next character is not '*'; require exact match
        if ( (inpStr[iS] != pattern[iP]) and not (pattern[iP] == ".") ):
            return False
        return regexp_recurse(inpStr, pattern, iS+1, iP+1)


def test__regexp_recurse():
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
        res = regexp_recurse(inpStr, pattern, 0, 0)
        print(f"Result: {res}")
