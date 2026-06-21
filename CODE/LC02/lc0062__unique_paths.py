# lc0062__unique_paths.py
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0063__unique_paths import *

# RELOAD:
# import importlib; import lc0063__unique_paths; importlib.reload(lc0063__unique_paths); from lc0063__unique_paths import *

# The idea: use DP. dp[0][i] = dp[i][0] = 1. For other cells dp[i][j] = dp[i-1][j] + dp[i][j-1]. The answer will be in the bottom-right corner.
# dp[i][j] == number of ways to reach cell #i,j; last step is either from left or from above; for 1st row last step is from left; for 1st column last step is from above.
# See https://algo.monster/liteproblems/62


def unique_paths(m: int, n: int) -> int:
    if ( (m == 0) or (n == 0) ):
        return 0
    if ( (m == 1) or (n == 1) ):
        return 1
    # initialize the DP table
    dp = [[0]*n for row in range(m)]
    for i in range(m):  dp[i][0] = 1
    for j in range(n):  dp[0][j] = 1
    # fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]  # the answer is in the bottom-right corner
##


def test__unique_paths():
    tasks = [
        [2, 2],  # 2
        [3, 7],  # 28
        [3, 2]   # 3
    ]
    for m, n  in tasks:
        print("====================================")
        print(f"Input: {m} x {n}")
        res = unique_paths(m, n)
        print(f"Result: {res}")
##
