# lc0074__search_2d_matrix.py
# You are given an m x n integer matrix matrix with the following two properties:
#    Each row is sorted in non-decreasing order.
#    The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0074__search_2d_matrix import *

# RELOAD:
# import importlib; import lc0074__search_2d_matrix; importlib.reload(lc0074__search_2d_matrix); from lc0074__search_2d_matrix import *

# The idea: run binary search while virtually flattening the matrix through index math.
# See https://www.geeksforgeeks.org/dsa/search-element-sorted-matrix/


def search_2d_matrix(matr: list[list[int]], target: int) -> bool:
    if ( not matr ):  return False
    m = len(matr)     # number of rows
    n = len(matr[0])  # number of columns
    if ( n == 0 ):  return False

    lo = 0;  hi = m * n - 1  # init binary-search limits
    while ( lo <= hi ):
        mid = (lo + hi) // 2
        row = mid // n
        col = mid % n
        if ( matr[row][col] == target ):
            return True
        if ( matr[row][col] < target ):
            lo = mid + 1
        else:  # matr[row][col] > target
            hi = mid - 1
    return False
##


def test__search_2d_matrix():
    tasks = [
        [[[1,3,5,7],[10,11,16,20],[23,30,34,60]],  3],    # True
        [[[1,3,5,7],[10,11,16,20],[23,30,34,60]],  13],   # False
        [[[1,5,9],[14,20,21],[30,34,43]],  14],           # True
        [[[1,5,9,11],[14,20,21,26],[30,34,43,50]],  42],  # False
    ]
    for matr, target in tasks:
        print("=======================================")
        print(f"Input: {matr},  target={target}")
        res = search_2d_matrix(matr, target)
        print(f"Result: {res}")
##
