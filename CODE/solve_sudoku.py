# solve_sudoku.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from solve_sudoku import *

# RELOAD:
# import importlib; import solve_sudoku; importlib.reload(solve_sudoku); from solve_sudoku import *


# The idea: in every cell starting from top-left try each number and call recursively. If no luck, clear the number. Mark used numbers in bit-fields for rows, columns and boxes.


# helper for boxes' bit-fields (index calc examples: 1//3=0, 4//3=1, 7//3=2)
def _box_idx(row, col):
    return row//3 * 3  +  col//3


# checks if 'num' already marked in row, column, or box
def is_safe(mat, i, j, num, rows, cols, boxes):
    bit1 = 1 << num
    if ( (rows[i] & bit1) or (cols[j] & bit1) or
         (boxes[_box_idx(i, j)] & bit1) ):
        return False
    return True


def mark_number_in_cell(i, j, num, rows, cols, boxes):
    bit1 = 1 << num
    rows[i] |= bit1
    cols[j] |= bit1
    boxes[_box_idx(i, j)] |= bit1
    

def clear_number_in_cell(i, j, num, rows, cols, boxes):
    bit0 = ~(1 << num)
    rows[i] &= bit0
    cols[j] &= bit0
    boxes[_box_idx(i, j)] &= bit0
    

def solve_sudoku_rec(mat, i, j, rows, cols, boxes):
    n = len(mat)
    # base case is if the whole matrix is processed
    if ( (i == n-1) and (j == n) ):  # step-column outside the matrix in last row
        return True

    # if stepped beyound last column in non-last raw, go to next row
    if ( j == n ):
        i += 1
        j = 0

    # if the cell is already filled, move to the next
    if ( mat[i][j] != 0 ):
        return solve_sudoku_rec(mat, i, j+1, rows, cols, boxes)
    
    # try to put each "valid" number into [i][j]
    for num in range(1, n+1):
        if ( is_safe(mat, i, j, num, rows, cols, boxes) ):
             mat[i][j] = num
             mark_number_in_cell(i, j, num, rows, cols, boxes)
             
             # try to solve the rest of the matrix; if fails, undo this number
             if ( True == solve_sudoku_rec(mat, i, j+1, rows, cols, boxes) ):
                 return True

             mat[i][j] = 0  # to allow trying other numbers
             clear_number_in_cell(i, j, num, rows, cols, boxes)

    return False


def solve_sudoku(mat):
    n = len(mat)
    rows = [0]*n
    cols = [0]*n
    boxes = [0]*n
    # Set the bits in bitmasks for values that are initially present
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                mark_number_in_cell(i, j, mat[i][j], rows, cols, boxes)


    return solve_sudoku_rec(mat, 0, 0, rows, cols, boxes)


def test__solve_sudoku():
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

    solve_sudoku(mat)
    for row in mat:
        print(" ".join(map(str, row)))
