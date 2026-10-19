# lc0174__dungeon_game.py
# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.
# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
# Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).
# To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
# Return the knight's minimum initial health so that he can rescue the princess.
# Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0174__dungeon_game import *

# RELOAD:
# import importlib;    import lc0174__dungeon_game;  importlib.reload(lc0174__dungeon_game);  from lc0174__dungeon_game import *

# The idea: DP going backward from bottom-right where DP[i][j] = max(1, min(DP[i+1}[j], DP[i][j+1]) - dungeon[i][j]. DP corresponds to amount of health at entering its cells.
# See: https://algo.monster/liteproblems/174


def dungeon_game(dungeon: list[list[int]]) -> int:
    nRows, nCols = len(dungeon), len(dungeon[0])
    # dp is one larger to incorporate boundary conditions
    dp = [[float('inf')] * (nCols+1) for _ in range(nRows+1)]
    # the knight must survive visiting princess's cell - >= 1 health left
    dp[nRows-1][nCols] = dp[nRows][nCols-1] = 1

    # propagate from bottom-right
    for r in range(nRows-1, -1, -1):
        for c in range(nCols-1, -1, -1):
            min_health_at_leave = min(dp[r][c+1], dp[r+1][c])
            # dp is min health at enter
            dp[r][c] = max(1, min_health_at_leave - dungeon[r][c])

    return dp[0][0]
##


def test__dungeon_game():
    tasks = [
        [[-2,-3,3],[-5,-10,1],[10,30,-5]],  # 7
    ]
    for dungeon in tasks:
        print("===========================================")
        print(f"Dungeon: {dungeon}")
        res = dungeon_game(dungeon)
        print(f"Result: {res}")
##
