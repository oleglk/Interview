# island_perimeter.py - find the total length of exposed land edges in a binary grid (1s for land, 0s for water), where exactly one island exists, surrounded by water, with no internal lakes.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from island_perimeter import *

# RELOAD:
# import importlib; import island_perimeter; importlib.reload(island_perimeter); from island_perimeter import *

# The idea: scan the grid and add 1 for each water-boundary edge of land cells. E.g. pick land cells and check their boundaries.


def island_perimeter(grid: list) -> int:
    """'grid' is list of lists with 0|1 meaning land|water."""
    perimeter = 0
    nRows = len(grid)
    if ( nRows == 0 ):  raise Exception("nRows == 0")
    nCols = len(grid[0])
    if ( nCols == 0 ):  raise Exception("nCols == 0")
    # Traverse land cells
    for i in range(0, nRows):
        for j in range(0, nCols):
            if ( grid[i][j] == 0 ):
                continue
            if ( (i > 0) and (grid[i-1][j] == 0) ):
                perimeter += 1;  #print(f"{i},{j}: A")
            if ( (i < (nRows-1)) and (grid[i+1][j] == 0) ):
                perimeter += 1;  #print(f"{i},{j}: B")
            if ( (j > 0) and (grid[i][j-1] == 0) ):
                perimeter += 1;  #print(f"{i},{j}: C")
            if ( (j < (nCols-1)) and (grid[i][j+1] == 0) ):
                perimeter += 1;  #print(f"{i},{j}: D")
    return(perimeter)


def test__island_perimeter():
    # 1
    g1 = [[1]]
    # 0
    g2 = [[0]]
    # 000
    # 010
    # 000
    g3 = [(0,0,0), (0,1,0), (0,0,0)]  # 4
    # 100
    # 010
    # 001
    g4 = [(1,0,0), (0,1,0), (0,0,1)]  # 8
    # 110
    # 010
    # 011
    g5 = [(1,1,0), (0,1,0), (0,1,1)]  # 6

    for g in [g1, g2, g3, g4, g5]:
        print("======================================")
        print(f"Input: {g}")
        res = island_perimeter(g)
        print(f"Result: {res}")
