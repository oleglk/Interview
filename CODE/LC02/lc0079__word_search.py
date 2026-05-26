# lc0079__word_search.py
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0079__word_search import *

# RELOAD:
# import importlib; import lc0079__word_search; importlib.reload(lc0079__word_search); from lc0079__word_search import *

# The idea: starting from all relevant positions (1st char match) run 4 recursive searches.
# See https://www.geeksforgeeks.org/dsa/check-if-a-word-exists-in-a-grid-or-not/


def word_search(board: list[list[int]], word: str) -> bool:
    m = len(board)
    if ( m == 0 ):  return False
    n = len(board[0])
    if ( n == 0 ):  return False
    for row in range(0, m):
        for col in range(0, n):
            if ( board[row][col] == word[0] ):  # match may start in [row][col]
                if ( word_search_recurse(board, word, row, col, 0) ):
                    return True
    return False
##


# Checks match of suffix starting from 'startIdx'
def word_search_recurse(board: list[list[int]], word: str, row: int, col: int, startIdx: int) -> bool:
    m = len(board)
    n = len(board[0])
    # check base case of word fully matched
    if ( startIdx == len(word) ):
        return True
    # check base cases of going out of boundary
    if ( (row < 0) or (row >= m) or (col < 0) or (col >= n) ):
        return False
    # check base case of current cell not matched
    if ( board[row][col] != word[startIdx] ):
        return False

    # temporarily mark current cell as visited
    saved = board[row][col]
    board[row][col] = "#"
    # try going in all 4 directions
    resRight = word_search_recurse(board, word, row,   col+1, startIdx+1)
    resDown  = word_search_recurse(board, word, row+1, col,   startIdx+1)
    resLeft  = word_search_recurse(board, word, row,   col-1, startIdx+1)
    resUp    = word_search_recurse(board, word, row-1, col,   startIdx+1)
    board[row][col] = saved  # restpre the current cell
    return resRight or resDown or resLeft or resUp
##

                
def test__word_search():
    tasks = [
        [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"],  # True
        [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"],  # True
        [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"],  # False
        [[['T','E','E'],['S','G','K'],['T','E','L']], "GEEK"],  # True
        [[['T','E','U'],['S','G','K'],['T','E','L']], "GEEK"],  # False
    ]
    for board, word  in tasks:
        print("=======================================")
        print(f"Input: {board}, word={word}")
        res = word_search(board, word)
        print(f"Result: {res}")
##
