# lc0054__spiral_matrix.py
# Given an m x n matrix, return all elements of the matrix in spiral order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0054__spiral_matrix import *

# RELOAD:
# import importlib; import lc0054__spiral_matrix; importlib.reload(lc0054__spiral_matrix); from lc0054__spiral_matrix import *

# The idea: walk along squeezing borders.
# See https://www.geeksforgeeks.org/dsa/print-a-given-matrix-in-spiral-form/


def spiral_matrix(mat: list[list[int]]) -> list[int]:
    if (mat is None):
        return []
    n = len(mat)
    m = len(mat[0])
    top = left = 0
    bottom = n - 1
    right = m - 1
    res = []
    while ( (top <= bottom) and (left <= right) ):
        # traverse top boundary row from left to right
        for j in range(left, right+1):
            res.append(mat[top][j])
        top += 1  # squeeze top
        # traverse right boundary column from top to bottom
        for i in range(top, bottom+1):
            res.append(mat[i][right])
        right -= 1  # squeeze right
        # traverse bottom boundary row from right to left
        if ( top <= bottom ):
            for j in range(right, left-1, -1):
                res.append(mat[bottom][j])
            bottom -= 1  # squeeze bottom
        # traverse left boundary column from bottom to top
        if ( left <= right ):
            for i in range(bottom, top-1, -1):
                res.append(mat[i][left])
            left += 1  # squeeze left
    return res
##


def test__spiral_matrix():
    tasks = [
        [[ 1,  2,  3,  4], 
         [ 5,  6,  7,  8], 
         [ 9, 10, 11, 12], 
         [13, 14, 15, 16]],  # [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
        [[1]],
        [[1, 2, 3],
         [4, 5, 6]]          # [1,2,3,6,5,4]
        ]
    for mat in tasks:
        print("========================================")
        print(f"Input: {mat}")
        res = spiral_matrix(mat)
        print(f"Result: {res}")
##
