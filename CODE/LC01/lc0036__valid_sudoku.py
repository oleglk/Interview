# lc0036__valid_sudoku.py
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1) Each row must contain the digits 1-9 without repetition.
# 2) Each column must contain the digits 1-9 without repetition.
# 3) Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0036__valid_sudoku import *

# RELOAD:
# import importlib; import lc0036__valid_sudoku; importlib.reload(lc0036__valid_sudoku); from lc0036__valid_sudoku import *

# The idea:
# Pass over the cells once; maintain sets of digit occurences for rows, columns, and 3x3 boxes.
## Box index verification:
## 0,0 -> 0
## 2,2 -> 0*3 + 0 -> 0
## 0,3 -> 0*3 + 1 -> 1
## 2,3 -> 0*3 + 1 -> 1
## 3,2 -> 1*3 + 0 -> 3


def box_index(row, col):
    return (row // 3) * 3 + (col // 3)


def valid_sudoku(grid: list[list[str]]) -> bool:
    # init arrays of occurence sets
    occRows = []
    occCols = []
    occBoxes = []
    for i in range(0, 9):
        occRows.append(set())
        occCols.append(set())
        occBoxes.append(set())
    # traverse the cells while checking and updating occurence flags
    for row in range(0, 9):
        for col in range(0, 9):
            ch = grid[row][col]
            if ( ch != "." ):
                if ( ch in occRows[row] ):
                    print(f"@@ {ch} of {row},{col} appears in row {row}")
                    return False
                else:
                    occRows[row].add(ch)
                if ( ch in occCols[col] ):
                    print(f"@@ {ch} of {col},{col} appears in col {col}")
                    return False
                else:
                    occCols[col].add(ch)
                box = box_index(row, col)
                if ( ch in occBoxes[box] ):
                    print(f"@@ {ch} of {row},{col} appears in box {box}")
                    return False
                else:
                    occBoxes[box].add(ch)
                
    return True;  # no duplicated occurences found
##


def test__valid_sudoku():
    tasks = [
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]],  # true
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]], # false
    ]
    for grid in tasks:
        print("=============================")
        for row in range(0, 9):
            for col in range(0, 9):
                print(f"{grid[row][col]}", end="")
            print()
        res = valid_sudoku(grid)
        print(f"Result: {res}")
##

