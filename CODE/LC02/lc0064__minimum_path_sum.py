# lc0064__minimum_path_sum.py
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0064__minimum_path_sum import *

# RELOAD:
# import importlib; import lc0064__minimum_path_sum; importlib.reload(lc0064__minimum_path_sum); from lc0064__minimum_path_sum import *

# The idea: use dynamic programming. For internal cells dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]. Left column and top row are initialized for single path.

def minimum_path_sum(grid: list[list[int]]) -> int:
    m = len(grid)
    if ( m < 1 ): raise Exception("No grid")
    n = len(grid[0])
    if ( n < 1 ): raise Exception("No grid")

    dp = [[0]*n for row in range(m)]
    dp[0][0] = grid[0][0]
    # init left column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    # init top row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # fill 'dp' table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]
##


def test__minimum_path_sum():
    tasks = [
        [[1,3,1],[1,5,1],[4,2,1]],  # 7
        [[1,2,3],[4,5,6]],          # 12
    ]
    for grid in tasks:
        print("===========================")
        print(f"Input: {grid}")
        res = minimum_path_sum(grid)
        print(f"Result: {res}")
##
