# count_islands_union_find.py - count "islands" on the grid-map using disjoint sets with union and find operations.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from count_islands_union_find import *

# RELOAD:
# import importlib; import count_islands_union_find; importlib.reload(count_islands_union_find); from count_islands_union_find import *


# The idea: init to every land cell being a separate island, then merge adjacent land cells in 4 directions. Actually it's enough to "look" right and down from current cell. Islands-being-built represented by disjoint sets. Member in the set is a single index for grid-cell position.


class CountIslands:
    # Value 1 in the grid cell means land, 0 means water.
    def __init__(self, grid: list[list[bool]]) -> None:
        self.grid = grid
        self.nRows = len(grid)
        if ( self.nRows == 0 ):  raise Exception("Invalid grid")
        self.nCols = len(grid[0])
        if ( self.nCols == 0 ):  raise Exception("Invalid grid")
        self.nCells = self.nRows * self.nCols
        # initially each cell, land or water, is parent of itself
        self.parent = list(range(0, self.nCells))
        # count land cells
        self.islandsCount = 0  # init to num of land cells
        for r in range(0, self.nRows):
            for c in range(0, self.nCols):
                self.islandsCount += grid[r][c]
        


    def find_parent(self, x: int) -> int:
        """Finds parent of element x.
           Optimizes the array by path compression while searching"""
        if ( x != self.parent[x] ):
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]


    def merge(self, x: int, y: int):
        """Makes root of y son of root of x"""
        parX = self.find_parent(x)
        parY = self.find_parent(y)
        if ( parX != parY ):
            self.parent[parY] = parX


    def grid_to_index(self, row: int, col: int) -> int:
        return  row * self.nCols + col

    def index_to_grid(self, idx: int) -> tuple:
        return tuple([idx // self.nCols, idx % self.nCols])

    def grid_cell_valid(self, row: int, col: int) -> bool:
        return (row >= 0) and (row < self.nRows) and (col >= 0) and (col < self.nCols)

    # def index_valid(self, idx: int) -> bool:
    #     r, c = self.index_to_grid(idx)
    #     return self.grid_cell_valid(r, c)

    
    # def index_is_land(self, idx: int) -> bool:
    #     r, c = index_to_grid(idx)
    #     return self.grid[r][c]


    def merge_and_count(self) -> int:
        """Merges adjacent cells into islands; returns count of islands."""
        # traverse land cells and merge them with adjacent land cells
        # every actual merge decrements count of islands by 1
        # Oleg: it's enough to look rightwards and downwards ?
        for row in range(0, self.nRows):
            for col in range(0, self.nCols):
                if ( not self.grid[row][col] ):  # water cell - skip it
                    continue
                idx1 = self.grid_to_index(row, col)
                # check if right neighbor is land
                if ( self.grid_cell_valid(row, col+1) and self.grid[row][col+1] ):
                    idx2 = self.grid_to_index(row, col+1)
                    if ( self.find_parent(idx1) != self.find_parent(idx2) ):
                        print(f"@@ Merge {self.index_to_grid(idx1)} with {self.index_to_grid(idx2)}")
                        self.merge(idx1, idx2)
                        self.islandsCount -= 1
                # check if bottom neighbor is land
                if ( self.grid_cell_valid(row+1, col) and self.grid[row+1][col] ):
                    idx3 = self.grid_to_index(row+1, col)
                    if ( self.find_parent(idx1) != self.find_parent(idx3) ):
                        print(f"@@ Merge {self.index_to_grid(idx1)} with {self.index_to_grid(idx3)}")
                        self.merge(idx1, idx3)
                        self.islandsCount -= 1
        return self.islandsCount


    @staticmethod
    def run(grid: list[list]) -> int:
        cntIslands = CountIslands(grid)
        return cntIslands.merge_and_count()


def test__count_islands_union_find():
    g1 = [[0,1], [1,0]]               # 2
    g2 = [[]]                         # -1
    g3 = [[1,0,0], [0,1,1], [0,1,1]]  # 2
    g4 = [[1,0], [1,0]]               # 1
    g5 = [[0,1,0], [0,1,0], [1,0,1]]  # 3
    for g in [g1, g2, g3, g4, g5]:
        print("=============================")
        print(f"Input: {g}")
        try:
            res = CountIslands.run(g)
        except Exception as ex:
            print(f"Exception occured: {str(ex)}")
            res = -1
        print(f"Result: {res}")
