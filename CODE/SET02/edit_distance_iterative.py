# edit_distance_iterative.py - Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2 (insert, delete, replace). Note that operations are applied to word1.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from edit_distance_iterative import *

# RELOAD:
# import importlib; import edit_distance_iterative; importlib.reload(edit_distance_iterative); from edit_distance_iterative import *


# The idea: Build DP table from smaller to larger. Choose btw 4 possibilities:
# - if w1[m-1] == w2[n-1], take value (m-1, n-1)
# - if w1[m-1] != w2[n-1], take minimum of the following 3:
# --  (delete w1[m-1]), take (m-1, n) +1
# --  (insert w2[n-1] as w1[m]), take (m, n-1) +1
##                     (we made w1[m] match w2[n-1], now compare left of it)
# --  (replace w1[m-1] by w2[n-1]), take (m-1, n-1) +1


def edit_distance(word1, word2):
    m = len(word1)  # rows
    n = len(word2)  # columns
    
    # init DP table, size (m+1 x n+1) since 0 is included
    dp = [[0]*(n+1) for _ in range(0, m+1)]
    for i in range(0, m+1):
        dp[i][0] = i  # if word2 empty, delete all chars of word1
    for j in range(0, n+1):
        dp[0][j] = j  # if word1 empty, insert all chars of word2

    # fill the rest of the table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if ( word1[i-1] == word2[j-1] ):
                dp[i][j] = dp[i-1][j-1]  # when position equal, nothing to do
            else:  # take 1 + min of delete, insert, replace
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return(dp[m][n])  # ultimate result - in the bottom-right cell
                

def test__edit_distance():
    tasks = [ ["geek","gesek"], ["gfg","gfg"], ["abcd","bcfe"] ]
    #          1                 0              3
    for word1, word2 in tasks:
        print("===========================")
        print(f"Input: {word1}, {word2}")
        res = edit_distance(word1, word2)
        print(f"Result: {res}")
