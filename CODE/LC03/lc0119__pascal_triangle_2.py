# lc0119__pascal_triangle_2.py
# Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#               1
#              1 1
#             1 2 1
#            1 3 3 1
#           1 4 6 4 1

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0119__pascal_triangle_2 import *

# RELOAD:
# import importlib;    import lc0119__pascal_triangle_2;  importlib.reload(lc0119__pascal_triangle_2);  from lc0119__pascal_triangle_2 import *

# The idea: dynamic programming based on each internal number being the sum of the two numbers directly above it, while first and last numbers in each row are 1-s. For space optimization use one row traversed right to left.
# See https://algo.monster/liteproblems/119


def pascal_triangle_get_row(rowIndex: int) -> list[int]:
    if ( rowIndex == 0 ):  return [1]
    if ( rowIndex == 1 ):  return [1, 1]

    # row #rowIndex has rowIndex+1 elements
    oneRow = [1]*(rowIndex+1)
    
    # generate rows up to 'rowIndex'
    for row in range(2, rowIndex+1):
        # traverse right-to-left to preserve prev-row elements until they are used
        # edge elements already set to 1, so calc only middle elements
        for pos in range(row-1, 0, -1):
            oneRow[pos] = oneRow[pos] + oneRow[pos-1]

    return oneRow
##


def test__pascal_triangle_get_row():
    tasks = [2, 3, 4]
    for rowIndex in tasks:
        print("=====================================")
        print(f"rowIndex = {rowIndex}")
        oneRow = pascal_triangle_get_row(rowIndex)
        print(f"Result: {oneRow}")
##
