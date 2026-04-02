# lc0048__rotate_image.py
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0048__rotate_image import *

# RELOAD:
# import importlib; import lc0048__rotate_image; importlib.reload(lc0048__rotate_image); from lc0048__rotate_image import *

# 123
# 456
# 789
# \/
# 741
# 852
# 963
# #0,0 -> #0,2;  #0,1 -> #1,2;  #0,2 -> 2,2
# #2,0 -> #0,0;  #2,1 -> #1,0;  #2,2 -> 2,0
# #i,j -> #j,n-i-1

# The idea: flip horizontally then transpose. Both operations make swaps in-place.
# See: https://algo.monster/liteproblems/48
# Horizontal flip: #i,j     -> #n-i-1,j
# Transposition:   #n-i-1,j -> #j,n-i-1


def matrix_horizontal_flip(arr: list[list[int]]) -> None:
    nRows = len(arr)
    nCols = len(arr[0])
    for r in range(0, nRows//2):
        # swap row #r with row #(nRows - r - 1)
        for c in range(0, nCols): # flip the entire row
            arr[r][c], arr[nRows - r - 1][c] = arr[nRows - r - 1][c], arr[r][c]
    return
##


def matrix_transpose(arr: list[list[int]]) -> None:
    nRows = len(arr)
    nCols = len(arr[0])
    for r in range(0, nRows):
        for c in range(0, r): # flip above the main diagonal
            arr[r][c], arr[c][r] = arr[c][r], arr[r][c]
    return
##


def matrix_totate_90(arr: list[list[int]]) -> None:
    if ( arr is None ):
        return
    matrix_horizontal_flip(arr)
    matrix_transpose(arr)
    return
##


def test__matrix_totate_90():
    tasks = [
        [[1,2,3],[4,5,6],[7,8,9]],  # [[7,4,1],[8,5,2],[9,6,3]]
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    ]
    for arr in tasks:
        print("==================================")
        print(f"Input: {arr}")
        matrix_totate_90(arr)
        print(f"Result: {arr}")
##
