# lc0064__unique_paths_2.py
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0064__unique_paths_2 import *

# RELOAD:
# import importlib; import lc0064__unique_paths_2; importlib.reload(lc0064__unique_paths_2); from lc0064__unique_paths_2 import *

# The idea: use DP. dp[0][i] = dp[i][0] = 1. For other cells dp[i][j] = dp[i-1][j] + dp[i][j-1]. But if #i,j contains obstacle, dp[i][j] == 0. The answer will be in the bottom-right corner.

# See https://codeanddebug.in/blog/unique-paths-ii/


def unique_paths_2(obstacleGrid: list[list[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if ( (obstacleGrid[0][0] == 1) or (obstacleGrid[m-1][n-1] == 1) ):
        return 0
    dp = [[0]*n for row in range(m)]
    dp[0][0] = 1

    for i in range(0, m):
        for j in range(0, n):
            if ( obstacleGrid[i][j] == 1 ):
                dp[i][j] = 0
                continue
            if ( i > 0 ):  # can come from above
                dp[i][j] += dp[i-1][j]
            if ( j > 0 ):  # can come from left
                dp[i][j] += dp[i][j-1]
    return dp[m-1][n-1]
##


def test__unique_paths_2():
    tasks = [
        [[0,0,0],[0,1,0],[0,0,0]],  # 2
        [[0,1],[0,0]],              # 1
    ]
    for obstacleGrid in tasks:
        print("====================================")
        print(f"Input: {obstacleGrid}")
        res = unique_paths_2(obstacleGrid)
        print(f"Result: {res}")
##
