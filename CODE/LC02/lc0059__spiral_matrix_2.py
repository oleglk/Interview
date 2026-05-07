# lc0059__spiral_matrix_2.py
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0059__spiral_matrix_2 import *

# RELOAD:
# import importlib; import lc0059__spiral_matrix_2; importlib.reload(lc0059__spiral_matrix_2); from lc0059__spiral_matrix_2 import *


# The idea: traverse along squeezing borders while filling incremented counter value.


def spiral_matrix_2(n: int) -> list[list[int]]:
    mat = [[0]*n for row in range(0, n)]
    left = top = 0
    right = bottom = n-1
    count = 1

    while ( (left <= right) and (top <= bottom) ):
        # go right along top border
        for col in range(left, right+1, 1):
            mat[top][col] = count
            count += 1
        top += 1  # squeeze from top
        # go down along right border
        for row in range(top, bottom+1, 1):
            mat[row][right] = count
            count += 1
        right -= 1  # squeeze from right
        if ( top <= bottom ):
            # go left along the bottom border
            for col in range(right, left-1, -1):
                mat[bottom][col] = count
                count += 1
            bottom -= 1  # squeeze from bottom
        if ( left <= right ):
            # go up along the left border
            for row in range(bottom, top-1, -1):
                mat[row][left] = count
                count += 1
            left += 1  # squeeze from left
    return mat
##
def test__spiral_matrix_2():
    tasks = [
        1,      # [[1]]
        2,      # [[1,2],[4,3]]
        3       # [[1,2,3],[8,9,4],[7,6,5]]
    ]
    for n in tasks:
        print("=====================================")
        print(f"Input: {n}")
        res = spiral_matrix_2(n)
        print(f"Result: {res}")
##
