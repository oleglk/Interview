# lc0073__set_matrix_zeroes.py
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0073__set_matrix_zeroes import *

# RELOAD:
# import importlib; import lc0073__set_matrix_zeroes; importlib.reload(lc0073__set_matrix_zeroes); from lc0073__set_matrix_zeroes import *

# The idea: check all elements and mark rows and columns to be nullified by setting zeroes in 1st row and 1st column respectively. Since element [0][0] belongs to both 1st row and column, use it for 1st row and maintain a separate col0 variable for the 1st column. Separate row0 variable needed too. Nullify elements in non-1st (!) rows and columns based on zeros in 1st rows and columns. Then (!) nullify elements in 1st row and 1st column based on row0 and col0.
# See https://www.geeksforgeeks.org/dsa/set-matrix-rows-and-columns-to-zeroes/


def set_matrix_zeroes(matr: list[list[int]]) -> list[list[int]]:
    col0 = 1  # separate variable for the 1st column
    row0 = 1  # separate variable for the 1st row
    m = len(matr)
    n = len(matr[0])

    # mark rows and columns to be nullified
    # mark 1st row separately
    for col in range(0, n):
        if ( matr[0][col] == 0 ):  # need to nullify 1st row
            row0 = 0
    # mark 1st column separately
    for row in range(0, m):
        if ( matr[row][0] == 0 ):  # need to nullify 1st column
            col0 = 0
    # mark non-1st rows and columns
    for row in range(0, m):
        for col in range(0, n):
            if ( matr[row][col] == 0 ):
                matr[row][0] = 0
                if ( col > 0 ):
                    matr[0][col] = 0
                else:
                    col0 = 0
    print(f"@@ Marked matrix = {matr}, row0= {row0}, col0={col0}")
    
    # nullify marked rows and columns except for row 0 and column 0
    # row 0 and column 0 are preserved to avoid false marking
    for row in range(1, m):
        if ( matr[row][0] == 0 ):
            print(f"@@ nullify row {row}")
            for col in range(1, n):  matr[row][col] = 0  # nullify row
    for col in range(1, n):
        if ( matr[0][col] == 0 ):
            print(f"@@ nullify col {col}")
            for row in range(1, m):  matr[row][col] = 0  # nullify column

    # if needed, nullify row 0 and column 0
    if ( row0 == 0 ):              # need to nullify 1st row
        print(f"@@ nullify row 0")
        for col in range(0, n):  matr[0][col] = 0  # nullify 1st row
    if ( col0 == 0 ):              # need to nullify 1st column
        print(f"@@ nullify col 0")
        for row in range(0, m):  matr[row][0] = 0  # nullify 1st column

    return matr
##


def test__set_matrix_zeroes():
    tasks = [
        [[0,1],[2,3]],                    # [[0,0],[0,3]]
        [[1,1,1],[1,0,1],[1,1,1]],        # [[1,0,1],[0,0,0],[1,0,1]]
        [[0,1,2,0],[3,4,5,2],[1,3,1,5]],  # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    ]
    for matr in tasks:
        print("=======================================")
        print(f"Input: {matr}")
        res = set_matrix_zeroes(matr)
        print(f"Result: {res}")
##
