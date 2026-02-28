# lc0014__longest_common_prefix.py
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0014__longest_common_prefix import *

# RELOAD:
# import importlib; import lc0014__longest_common_prefix; importlib.reload(lc0014__longest_common_prefix); from lc0014__longest_common_prefix import *

# The idea: run over all strings while comparing current-position char between them.


def longest_common_prefix(strs: list[str]) -> str:
    if ( (strs is None) or (len(strs) == 0) ):
        return ""
    # find min length
    minLength = float('inf')
    for s in strs:
        if ( s is None ):
            return ""
        if ( len(s) < minLength ):
            minLength = len(s)
    if ( minLength == 0 ):
        return ""
    mismatch = False
    for currPos in range(0, minLength):
        currChar = strs[0][currPos]
        for s in strs:
            if ( s[currPos] != currChar ):  # found 1st non-matching pos
               return s[0:currPos]  # not including current position
    # no mismatch till min-length
    return strs[0][0:minLength]


def test__longest_common_prefix():
    tasks = [
        ["flower","flow","flight"],                   # "fl"
        ["dog","racecar","car"],                      # ""
        ["geeksforgeeks", "geeks", "geek", "geezer"], # "gee"
    ]
    for strs in tasks:
        print("===================================")
        print(f"Input: {strs}")
        res = longest_common_prefix(strs)
        print(f"Result: {res}")

