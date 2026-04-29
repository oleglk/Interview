# lc0051__n_queens.py
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0051__n_queens import *

# RELOAD:
# import importlib; import lc0051__n_queens; importlib.reload(lc0051__n_queens); from lc0051__n_queens import *

# The idea: decide where to place one queen in each row. Recursively check all columns.
# Check, mark, unmark position safety in 3 arrays: usedColumn[j], usedDiagonal[i+j], usedAntiDiagonal[n-i+j].
# (All cells on SW-NE diagonal have same (row+col);  all cells on NW-SE anti-diagonal have same (n-row+col).)
# See https://algo.monster/liteproblems/51


class NQueensStatus:
    def __init__(self, n: int) -> None:
        self.n = n
        self.board = [["."]*n for col in range(0, n)]
        self.usedColumns = [0]*n
        # ??? Unclear why the origin uses 2*n diagonal positions
        # diagonal indices == [0 + 0  ...   (n-1) + (n-1)] -> 2n-1 positions
        self.usedDiagonals = [0]*(2*n)
        # anti-diagonal indices = [n - (n-1) + 0  ...  n - 0 + n-1] == [1...2n-1] -> 2n-1 positions
        self.usedAntiDiagonals = [0]*(2*n)

    def mark_used(self, row: int, col: int) -> None:
        self.board[row][col] = "Q"  # place the queen
        self.usedColumns[col] = True
        self.usedDiagonals[row + col] = True
        self.usedAntiDiagonals[self.n - row + col] = True

    def mark_unused(self, row: int, col: int) -> None:
        self.board[row][col] = "."  # erase the queen
        self.usedColumns[col] = False
        self.usedDiagonals[row + col] = False
        self.usedAntiDiagonals[self.n - row + col] = False

    def cell_is_safe(self, row: int, col: int) -> bool:
        return (not self.usedColumns[col]) and (not self.usedDiagonals[row + col]) and (not self.usedAntiDiagonals[self.n - row + col])
####

        
