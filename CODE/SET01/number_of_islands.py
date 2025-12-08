# number_of_islands.py - Given a 2D grid of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from number_of_islands import *

# RELOAD:
# import importlib;    import number_of_islands;  importlib.reload(number_of_islands);  from number_of_islands import *


# The idea: use dfs from each grid cell. To mark visited, write 0 in the cell.


class NumberOfIslands:

    def __init__(self, grid: list) -> int:
        if ( len(grid) == 0 ):
            return(0)
        self.nRows = len(grid);  self.nCols = len(grid[0])
        self.theGrid = grid
        self.count = 0
    
        for r in range(0, self.nRows):
            for c in range(0, self.nCols):
                if ( self.theGrid[r][c] == 1 ):
                    self.count += 1
                    self.dfs(r, c)

    @staticmethod
    def run(grid):
        solution = NumberOfIslands(grid)
        return(solution.count)


    def dfs(self, startR: int, startC: int):
        #print(f"@@ r={startR}, c={startC},  g={self.theGrid}")
        if ( (startR < 0) or (startR >= self.nRows) or
             (startC < 0) or (startC >= self.nCols) ):
            return  # silently ignore out-of-bound tasks
        print(f"@@ r={startR}, c={startC},  g={self.theGrid}")
        if ( self.theGrid[startR][startC] == 0 ):
            return  # silently ignore start from sea
        self.theGrid[startR][startC] = 0  # mark visited by erasing
        self.dfs(startR-1, startC);    self.dfs(startR+1, startC)
        self.dfs(startR,   startC-1);  self.dfs(startR,   startC+1)
        return


def test__number_of_islands():
    g1 = [[0,1], [1,0]]
    g2 = [[]]
    g3 = [[1,0,0], [0,1,1], [0,1,1]]
    g4 = [[1,0], [1,0]]
    for g in [g1, g2, g3, g4]:
        print("=============================")
        print(f"Input: {g}")
        res = NumberOfIslands.run(g)
        print(f"   => {res}")

