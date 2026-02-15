# word_search.py - find a given word in a 2D board of characters, forming the word by moving between adjacent (up, down, left, right) cells without reusing any cell for that word.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from word_search import *

# RELOAD:
# import importlib; import word_search; importlib.reload(word_search); from word_search import *


# The idea: run dfs from all cells in the grid.
#  See https://www.hellointerview.com/learn/code/backtracking/word-search .

def word_search(board: list[list], word: str) -> bool:
    rows = len(board);
    if ( rows == 0 ):  return False
    cols = len(board[0]);
    if ( cols == 0 ):  return False
    visited = set()

    def dfs(r, c, idx):
        # 'idx' is currently searched for index within the word
        if ( idx == len(word) ):
            return True  # found the whole word on the previous step
        # check if cell valid, and if yes, whether char unvisited and matches
        if ( (r < 0) or (r >= rows) or (c < 0) or (c >= cols) or
             ((r,c) in visited) or (board[r][c] != word[idx]) ):
            #print(f"@@ Reject for '{word}' at {r}, {c}, {idx}")
            return False
        # char matches and word unfinished; explore all 4 directions
        #print(f"@@ Explore for '{word}' at {r}, {c}, {idx}")
        visited.add((r,c))  # prevent reuse of the cell in the current path
        found = (dfs(r-1, c, idx+1) or dfs(r+1, c, idx+1) or
                 dfs(r, c-1, idx+1) or dfs(r, c+1, idx+1))
        #if ( found ):  print(f"@@ Found for '{word}' at {r}, {c}, {idx}")
        visited.remove((r,c)) # free up the cell for use by other path
        return found

    for r in range(0, rows):
        for c in range(0, cols):
            if ( True == dfs(r, c, 0) ):
                return True
    return False


def test__word_search():
    b0 = [['Q']]
    b1 = [['c','a','t'],
          ['o','m','n'],
          ['w','a','r']]
    b2 = [['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']]
    tasks = [
        [b0, "Q"],          # True
        [b1, "cat"],        # True
        [b1, "or"],         # False
        [b1, "car"],        # False
        [b1, "com"],        # True
        [b1, "warn"],       # True
        [b2, "ABCCED"],     # True
        [b2, "ABCB"]        # False
    ]
    for board, word in tasks:
        print("===============================")
        print(f"Board: {board},  word: {word}")
        res = word_search(board, word)
        print(f"Result: {res}")
