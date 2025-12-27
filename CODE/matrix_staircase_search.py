# matrix_staircase_search.py - Search target in row/col sorted matrix using staircase search.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from matrix_staircase_search import *

# RELOAD:
# import importlib; import matrix_staircase_search; importlib.reload(matrix_staircase_search); from matrix_staircase_search import *


# The idea: Start from top-right corner. If element > taget, eliminate current column by --col, since entire remaining-part-of-column is > target. If element < target, eliminate current row by ++row, since entire remaining-part-of-row is < target. If element = target, return true. If row or column goes out of bounds, element not found.


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
