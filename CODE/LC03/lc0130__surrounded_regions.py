# lc0130__surrounded_regions.py
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#    Connect: A cell is connected to adjacent cells horizontally or vertically.
#    Region: To form a region connect every 'O' cell.
#    Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0130__surrounded_regions import *

# RELOAD:
# import importlib;    import lc0130__surrounded_regions;  importlib.reload(lc0130__surrounded_regions);  from lc0130__surrounded_regions import *

# The idea: (a) replace all O-s with Y-s; (b) find all boundary 'Y' regions by dfs and replace their Y-s by O-s; (c) replace all remaining Y-s by X-s.
# See https://www.geeksforgeeks.org/dsa/given-matrix-o-x-replace-o-x-surrounded-x/


def surrounded_regions(grid: list[list[str]]) -> None:
    m = len(grid)
    if ( m == 0 ):  return
    n = len(grid[0])
    if ( n == 0 ):  return

    def fill_dfs(row: int, col: int, old: str, new: str) -> None:
        nonlocal grid
        """Flood-fills all adjacent (connected) 'old' char cells by 'new' char"""
        if ( (row < 0) or (row >= m) or (col < 0) or (col >= n) ):
            return
        if ( grid[row][col] != old ):
            return

        grid[row][col] = new
        fill_dfs(row-1, col, old, new)
        fill_dfs(row+1, col, old, new)
        fill_dfs(row, col-1, old, new)
        fill_dfs(row, col+1, old, new)
        return
    ##
    # (a) replace all O-s with Y-s
    for row in range(0, m):
        for col in range(0, n):
            if ( grid[row][col] == 'O' ):
                grid[row][col] = 'Y'
    # (b) find all boundary 'Y' regions by dfs and replace their Y-s by O-s
    for row in range(0, m):
        fill_dfs(row, 0,   'Y', 'O')
        fill_dfs(row, n-1, 'Y', 'O')
    for col in range(0, n):
        fill_dfs(0,   col, 'Y', 'O')
        fill_dfs(m-1, col, 'Y', 'O')
    # (c) replace all remaining Y-s by X-s - these are the surrounded regions
    for row in range(0, m):
        for col in range(0, n):
            if ( grid[row][col] == 'Y' ):
                grid[row][col] = 'X'

    return
##


def test__surrounded_regions():
    tasks = [
        [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],  # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        [["X"]],  # [["X"]]
    ]

    for grid in tasks:
        print("=================================================")
        print(f"Input:  {grid}")
        surrounded_regions(grid)
        print(f"Output: {grid}")
##
