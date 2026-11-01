# lc0200__number_of_islands.py
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0200__number_of_islands import *

# RELOAD:
# import importlib;    import lc0200__number_of_islands;  importlib.reload(lc0200__number_of_islands);  from lc0200__number_of_islands import *

# The idea: pick exploration-start cells by nested loop over whole grid; explore by DFS while marking current cell as visited and going to the 4 neighbours.
# See: https://techsauce.medium.com/number-of-islands-interview-question-e2c35ae23c66


def number_of_islands(grid: list[list[str]]) -> int:
    m = len(grid)
    if ( m == 0 ):  return 0
    n = len(grid[0])
    if ( n == 0 ):  return 0
    islandCnt = 0
    # try starting exploration from every cell;
    # unvisited cells belong to new islands
    for y in range(0, m):
        for x in range(0, n):
            if ( grid[y][x] != '1' ):
                continue  # skip visited or sea
            # the cell belongs to an uncounted yet island
            islandCnt += 1
            # traverse and mark-visited this new island
            number_of_islands__dfs(grid, x, y)
    return islandCnt
##


def number_of_islands__dfs(grid: list[list[str]], x: int, y: int) -> None:
    m = len(grid);  n = len(grid[0])
    if ( (x < 0) or (x >= n) or (y < 0) or (y >= m) ):
        return  # "cell" out of bounds
    if ( grid[y][x] != '1' ):
        return  # skip visited or sea
    # unvisited cell of the island being explored
    grid[y][x] = 'X'  # mark visited
    # explore the 4 neighbouring cells
    number_of_islands__dfs(grid, x-1, y)
    number_of_islands__dfs(grid, x+1, y)
    number_of_islands__dfs(grid, x, y-1)
    number_of_islands__dfs(grid, x, y+1)
    return
##


def test__number_of_islands():
    g1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
    ]    # count = 1
    g2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
    ]    # count = 3
    
    tasks = [g1, g2]
    for grid in tasks:
        print("============================================")
        print(f"Input:")
        for row in grid:
            print(f"  {row}")
        res = number_of_islands(grid)
        print(f"Result: {res}")
##

       
