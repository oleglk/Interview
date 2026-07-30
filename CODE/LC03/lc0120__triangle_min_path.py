# lc0120__triangle_min_path.py
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0120__triangle_min_path import *

# RELOAD:
# import importlib;    import lc0120__triangle_min_path;  importlib.reload(lc0120__triangle_min_path);  from lc0120__triangle_min_path import *

# The idea: bottom-up DP where DP[i][j] = DP[i][j] + min(DP[i+1][j], DP[i+1][j+1]. The result is in DP[0][0]. TO save space, modify 'triangle' array in place.
# The solution suggested by Gemini AI.


def triangle_min_path(triangle: list[int]) -> int:
    # process rows starting from the one above bottom-most
    for row in range(len(triangle)-2, -1, -1):
        # (each next row has one more columns, so [i+1][j+1] is safe)
        for col in range(0, len(triangle[row])):
            triangle[row][col] += min(triangle[row+1][col], \
                                      triangle[row+1][col+1])
    return triangle[0][0]
##


def test__triangle_min_path():
    tasks = [
        [[2],[3,4],[6,5,7],[4,1,8,3]],  # 11
        [[-10]],                        # -10
    ]
    for triangle in tasks:
        print("==============================================")
        print(f"Input: {triangle}")
        res = triangle_min_path(triangle)
        print(f"Result: {res}")
##
