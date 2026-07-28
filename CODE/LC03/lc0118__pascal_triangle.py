# lc0118__pascal_triangle.py
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it:
#               1
#              1 1
#             1 2 1
#            1 3 3 1
#           1 4 6 4 1

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0118__pascal_triangle import *

# RELOAD:
# import importlib;    import lc0118__pascal_triangle;  importlib.reload(lc0118__pascal_triangle);  from lc0118__pascal_triangle import *

# The idea: dynamic programming based on each internal number being the sum of the two numbers directly above it, while first and last numbers in each row are 1-s.
# See https://www.geeksforgeeks.org/dsa/pascal-triangle/


def pascal_triangle(numRows: int) -> list[list[int]]:
    matr = [[1]]  # for the resulting triangle
    for row in range(1, numRows):
        rowList = []  # will accumulate the current row
        rowLen = row + 1
        for i in range(0, rowLen):
            if ( (i == 0) or (i == rowLen-1) ):  # edge element ==1
                rowList.append(1)
            else:                                # internal element is a sum
                rowList.append(matr[row-1][i-1] + matr[row-1][i])
        matr.append(rowList[:])
    return matr
##


def print_list_of_lists(lst: list[list[int]]) -> None:
    if ( lst is None ):
        print("None")
    for row in lst:
        for val in row:
            print(f"{val} ", end="")
        print("")  # EOL
##


def test__pascal_triangle():
    tasks = [5]
    for numRows in tasks:
        print("==========================================")
        matr = pascal_triangle(numRows)
        print(f"numRows: {numRows}")
        print_list_of_lists(matr)
##

        
