# lc0037__sudoku_solver.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0037__sudoku_solver import *

# RELOAD:
# import importlib; import lc0037__sudoku_solver; importlib.reload(lc0037__sudoku_solver); from lc0037__sudoku_solver import *


# Sudoky playfield is a 9x9 matrix.
# A sudoku solution must satisfy all of the following rules:
#   - Each of the digits 1-9 must occur exactly once in each row.
#   - Each of the digits 1-9 must occur exactly once in each column.
#   - Each of the digits 1-9 must occur exactly once in each of the 9, 3x3 sub-boxes of the grid.

# The idea: in every cell starting from top-left try each number and call recursively. If no luck, clear the number. Mark used numbers in bit-fields for rows, columns and boxes.


# helper for boxes' bit-fields (index calc examples: 1//3=0, 4//3=1, 7//3=2)
## (1,1)=>0, (3,0)=>3, (5,2)=>3, (6,6)=>8, (8,8)=>8
## (3,3)=>4, (0,3)=>1, (2,5)=>1
def _box_idx(row, col):
    return row//3 * 3  +  col//3
##


# tells whether 'num' could be placed into #i,j
def is_safe(i, j, num, rows, cols, boxes):
    bit1 = 1 << num
    if ( (rows[i] & bit1) or (cols[i] & bit1) or
         (boxes[_box_idx(i,j)] & bit1) ):
        return False
    else:
        return True
##


def mark_number_in_cell(i, j, num, rows, cols, boxes):
    bit1 = 1 << num
    rows[i] |= bit1
    cols[i] |= bit1
    boxes[_box_idx(i,j)] |= bit1
##


def clear_number_in_cell(i, j, num, rows, cols, boxes):
    bit0 = ~(1 << num)
    rows[i] &= bit0
    cols[i] &= bit0
    boxes[_box_idx(i,j)] &= bit0
 ##
 

# Solves sudoku field starting from row=i, column=j
def sudoku_solver_rec(mat, i, j, rows, cols, boxes):
    n = len(mat)
    # base case - all solved - is when we step into column n+1 from the last row
    if ( (i == n-1) and (j == n) ):
        return True

    # treat stepping into next row
    if ( j == n ):
        i += 1
        j = 0

    # if cell #i,j is already filled, go to the next cell
    if ( mat[i][j] != 0 ):
        return sudoku_solver_rec(mat, i, j+1, rows, cols, boxes)
    
    # try to put every number 1..n into #i,j
    for num in range(1, n+1):
        if ( is_safe(i, j, num, rows, cols, boxes) ):
            mat[i][j] = num
            mark_number_in_cell(i, j, num, rows, cols, boxes)

            # try to solve the rest of the matrix
            if ( sudoku_solver_rec(mat, i, j+1, rows, cols, boxes) ):
                return True

            # solving the rest of the matrix failed - undo this number
            mat[i][j] = 0
            clear_number_in_cell(i, j, num, rows, cols, boxes)

    return False  # failed to solve
##


# Solves sudoku from the given initial state
def sudoku_solver(mat):
    n = len(mat)
    rows = [0]*n
    cols = [0]*n
    boxes = [0]*n
    # mark numbers used in the initial state
    for i in range(0, n):
        for j in range(0, n):
            if ( mat[i][j] != 0 ):
                mark_number_in_cell(i, j, mat[i][j], rows, cols, boxes)

    return sudoku_solver_rec(mat, 0, 0, rows, cols, boxes)
##


def test__sudoku_solver():
    mat = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    sudoku_solver(mat)
    for row in mat:
        print(" ".join(map(str, row)))  # map(str, ...) converts to strings

