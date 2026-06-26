# lc0072__edit_distance_recursive.py
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
#    Insert a character
#    Delete a character
#    Replace a character

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0072__edit_distance_recursive import *

# RELOAD:
# import importlib; import lc0072__edit_distance_recursive; importlib.reload(lc0072__edit_distance_recursive); from lc0072__edit_distance_recursive import *

# The idea: use recursion.
# - If w1[m-1] == w2[n-1], match remaining prefixes - recurse(m-1, n-1)
# - If w1[m-1] != w2[n-1], take 1 + minimum of 3 operations:
# -- delete w1[m-1], match w1[0..m-2] with w2[0..n-1] - recurse(m-1, n)
# ---- (compare up to before the deleted char)
# -- insert w2[n-1] into w1, match w1[0..m-1] with w2[0..n-2] - recurse(m, n-1)
# ---- (compare up to before the inserted char)
# -- replace w1[m-1] by w2[n-1], match w1[0..m-2] with w2[0..n-2] - recurse(m-1, n-1)
# See https://www.geeksforgeeks.org/dsa/edit-distance-dp-5/

def edit_distance_recurse(w1: str, w2: str, m: int, n: int, memo: list[list[int]]) -> int:
    # base cases
    if ( m == 0 ):
        return n  # cost of inserting n chars into w1
    if ( n == 0 ):
        return m  # cost of deleting m chars from w1

    if ( memo[m][n] != -1 ):  return memo[m][n]

    if ( w1[m-1] == w2[n-1] ):  # current characters match
        memo[m][n] = edit_distance_recurse(w1, w2, m-1, n-1, memo)
        return  memo[m][n]
    
    # current characters don't match - try the 3 operations
    # deletion consumes 1 char in w1 and none in w2
    cntDelete  = edit_distance_recurse(w1, w2, m-1, n,   memo)
    # insertion consumes 1 char in w2 and none in w1
    cntInsert  = edit_distance_recurse(w1, w2, m,   n-1, memo)
    # replacement consumes 1 char in w1 and 1 char in w2
    cntReplace = edit_distance_recurse(w1, w2, m-1, n-1, memo)
    memo[m][n] = 1 + min(cntDelete, cntInsert, cntReplace)
    return memo[m][n]
##


def edit_distance(w1: str, w2: str) -> int:
    m = len(w1)
    n = len(w2)
    memo = [[-1]*(n+1) for i in range(0, m+1)]  # need [0..m]x[0..n]
    return edit_distance_recurse(w1, w2, m, n, memo)
##


def test__edit_distance():
    tasks = [
        ["horse", "ros"],                   # 3
        ["intention", "execution"],         # 5
        ["geek", "gesek"],                  # 1
        ["gfg", "gfg"],                     # 0
        ["GEEXSFRGEEKKS", "GEEKSFORGEEKS"], # 3
    ]
    for w1, w2  in tasks:
        print("=====================================")
        print(f"Input: {w1}, {w2}")
        res = edit_distance(w1, w2)
        print(f"Result: {res}")
##
