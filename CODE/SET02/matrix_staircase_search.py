# matrix_staircase_search.py - Search target in row-wise and column-wise sorted matrix using staircase search.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from matrix_staircase_search import *

# RELOAD:
# import importlib; import matrix_staircase_search; importlib.reload(matrix_staircase_search); from matrix_staircase_search import *


# The idea: Start from top-right corner. If element > target, eliminate current column by --col, since entire remaining-part-of-column is > target. If element < target, eliminate current row by ++row, since entire remaining-part-of-row is < target. If element = target, return true. If row or column goes out of bounds, element not found.

# Matrix example:
# 10, 20, 30, 40
# 15, 25, 35, 45
# 27, 29, 37, 48
# 32, 33, 39, 50

# Look for target=60:
# r=0, c=3 => element(40) < target => eliminate row#0 =>
# r=1, c=3 => element(45) < target => eliminate row#1 =>
# r=2, c=3 => element(48) < target => eliminate row#2 =>
# r=3, c=3 => element(50) < target => eliminate row#3 =>
# r=4, c=3 => row went out of bounds - target not found
# Look for target=29:
# r=0, c=3 => element(40) > target => eliminate col#3 =>
# r=0, c=2 => element(30) > target => eliminate col#2 =>
# r=0, c=1 => element(20) < target => eliminate row#0 =>
# r=1, c=1 => element(25) < target => eliminate row#1 =>
# r=2, c=1 => element(29) = target => found
# Look for target=28:
# r=0, c=3 => element(40) > target => eliminate col#3 =>
# r=0, c=2 => element(30) > target => eliminate col#2 =>
# r=0, c=1 => element(20) < target => eliminate row#0 =>
# r=1, c=1 => element(25) < target => eliminate row#1 =>
# r=2, c=1 => element(29) > target => eliminate col#1 =>
# r=2, c=0 => element(27) < target => eliminate row#2 =>
# r=3, c=0 => element(32) > target => eliminate col#0 =>
# r=3, c=-1 col went out of bounds - target not found


def matrix_staircase_search(matrix: list[list], target: int) -> bool:
    if ( matrix is None ): return False
    nRows = len(matrix)
    if ( nRows == 0 ): return False
    if ( len(matrix[0]) == 0 ): return False
    r = 0;  c = len(matrix[0])-1
    while ( (r < nRows) and (c >= 0) ):
        element = matrix[r][c]
        if ( element > target ): # entire column > target, eliminate column
            c -= 1
        elif ( element < target ):  # entire row < target, eliminate row
            r += 1
        else: # element == target
            return True
    return False

        
def test__matrix_staircase_search():
    tasks = [
        [ [[0]], 0 ],  [ [[0]], 1 ],
        [ [[3, 30, 38], [20, 52, 54], [35, 60, 69]], 62 ],
        [ [[18, 21, 27], [38, 55, 67]], 55 ],
        [ [[3, 30, 38], [20, 52, 54], [35, 60, 69]], 35 ]
        ]
    for matr, targ in tasks:
        print("===================================================")
        print(f"Inputs: {matr}, target={targ}")
        res = matrix_staircase_search(matr, targ)
        print(f"Result: {res}")
