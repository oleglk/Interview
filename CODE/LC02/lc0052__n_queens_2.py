# lc0052__n_queens_2.py
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0052__n_queens_2 import *

# RELOAD:
# import importlib; import lc0052__n_queens_2; importlib.reload(lc0052__n_queens_2); from lc0052__n_queens_2 import *

# The idea: decide where to place one queen in each row. Recursively check all columns.
# Check, mark, unmark position safety in 3 arrays: usedColumn[j], usedDiagonal[i+j], usedAntiDiagonal[n-i+j].
# (All cells on SW-NE diagonal have same (row+col);  all cells on NW-SE anti-diagonal have same (n-row+col).)
## n-row+col for n=4:
## 4567
## 3456
## 2345
## 1234
# See https://algo.monster/liteproblems/51, https://algo.monster/liteproblems/52


class NQueens2Status:
    def __init__(self, n: int) -> None:
        self.n = n
        self.usedColumns = [False]*n
        # max-idx for usedDiagonal is 2n-2 -> 2n-1 entries
        self.usedDiagonals = [False]*(2*n-1)
        # max-idx for usedAntiDiagonal is n-0+(n-1)=2n-1 -> 2n entries
        self.usedAntiDiagonals = [False]*(2*n)
    ##

    def mark_used(self, row: int, col: int) -> None:
        self.usedColumns[col] = True
        self.usedDiagonals[row + col] = True
        self.usedAntiDiagonals[self.n - row + col] = True
    ##

    def mark_unused(self, row: int, col: int) -> None:
        self.usedColumns[col] = False
        self.usedDiagonals[row + col] = False
        self.usedAntiDiagonals[self.n - row + col] = False
    ##

    def cell_is_safe(self, row: int, col: int) -> bool:
        return (not self.usedColumns[col]) and (not self.usedDiagonals[row + col]) and (not self.usedAntiDiagonals[self.n - row + col])
####


class NQueens2:
    def __init__(self, n: int) -> None:
        self.n = n
        self.status = NQueens2Status(n)
        self.solutionsCnt = 0
    ##


    def solve_recurse(self, row: int) -> None:
        """Recursively place queens row by row using backtracking."""
        if ( row == self.n ):  # solution is found
            self.solutionsCnt += 1
            return
        
        # try placing queen in all columns of 'row'
        for col in range(0, self.n):
            if ( self.status.cell_is_safe(row, col) ):
                self.status.mark_used(row, col)    # occupy col in row
                self.solve_recurse(row+1)  # fill subsequent rows
                self.status.mark_unused(row, col)  # free col in row
            
        return
    ##
    
    def do_job(self) -> int:
        self.solve_recurse(0)
        return self.solutionsCnt
    ##

    @staticmethod
    def solve(n: int) -> int:
        slv = NQueens2(n)
        return slv.do_job()
####


def test__NQueens2():
    tasks = [1, 2, 3, 4]
    for n in tasks:
        print("==========================================")
        print(f"n = {n}")
        res = NQueens2.solve(n)
        print(f"Result: {res}")
##
