# lc0097__interleaving_string.py
# Given three strings s1, s2 and s3, determine if s3 is formed by interleaving s1 and s2.
# A string s3 is an interleaving of s1 and s2 if:
# -    It contains all characters of s1 and s2 while preserving their relative order.
# -    Characters from s1 and s2 appear in s3 in the same order as in their original strings.
# -    The length of s3 equals the combined length of s1 and s2.
# Examples:
# s1 = "AAB", s2 = "AAC", s3 =  "AAAABC". Output: true.
# s1 = "YX", s2 = "X", s3 = "XXY".        Output: false

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0097__interleaving_string import *

# RELOAD:
# import importlib; import lc0097__interleaving_string; importlib.reload(lc0097__interleaving_string); from lc0097__interleaving_string import *

# The idea: TODO
# See https://www.geeksforgeeks.org/dsa/find-if-a-string-is-interleaved-of-two-other-strings-dp-33/

def interleaving_string_recurse(s1: str, s2: str, s3: str, i: int, j: int, memo: dict) -> bool:
    k = i + j  # current index in s3
    m = len(s1);  n = len(s2)

    # check base case of finished string
    if ( (i == m) and (j == n) and (k == (m + n)) ):  # all matched
        return True
    # check base case of exhausted s3 while s1 and/or s2 not finished
    if ( ((i < m) or (j < n)) and (k >= len(s3)) ):
        return False

    if ( memo[i][j] != -1 ):
        return memo[i][j]
    
    # try matching with each of s1, s2
    nextInS1 = (i < m) and (s1[i] == s3[k]) and interleaving_string_recurse(s1, s2, s3, i+1, j, memo)
    nextInS2 = (j < n) and (s2[j] == s3[k]) and interleaving_string_recurse(s1, s2, s3, i, j+1, memo)
    memo[i][j] = nextInS1 or nextInS2

    return memo[i][j]
##


def interleaving_string(s1: str, s2: str, s3: str) -> bool:
    m = len(s1);  n = len(s2)
    if ( len(s3) != (m+n) ):
        return False

    # memo is [m+1]*[n+1] to account for case of s1 or s2 exhausted
    memo = [[-1]*(n+1) for _ in range(0, m+1)]
    return interleaving_string_recurse(s1, s2, s3, 0, 0, memo)
##


def test__interleaving_string():
    tasks = [
        ["aabcc", "dbbca", "aadbbcbcac"],  # True
        ["aabcc", "dbbca", "aadbbbaccc"],  # False
        ["", "", ""],                      # True
        ["AAB", "AAC", "AAAABC"],          # True
        ["YX", "X", "XXY"],                # False
    ]
    for s1, s2, s3 in tasks:
        print("===============================")
        print(f"Input: s1={s1}, s2={s2}, s3={s3}")
        res = interleaving_string(s1, s2, s3)
        print(f"Result: {res}")
##
