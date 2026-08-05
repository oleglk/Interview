# CODE/LC03/lc0126__word_ladder_2.py
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#    Every adjacent pair of words differs by a single letter.
#    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#    sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
# Constraints:
#  1 <= beginWord.length <= 5
#  endWord.length == beginWord.length
#  1 <= wordList.length <= 500
#  wordList[i].length == beginWord.length
#  beginWord, endWord, and wordList[i] consist of lowercase English letters.
#  beginWord != endWord
#  All the words in wordList are unique.
#  The sum of all shortest transformation sequences does not exceed 10**5.


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0126__word_ladder_2 import *

# RELOAD:
# import importlib;    import lc0126__word_ladder_2;  importlib.reload(lc0126__word_ladder_2);  from lc0126__word_ladder_2 import *

# The idea: two phases:
# 1) BFS to find min distances to all words
# 2) DFS to recreate paths backwards using min distances. Each predecessor must have distance one less than current.
# In both phases find neighbor words by trying to replace each character with all 26 abc letters then checking wordList.
# See https://www.hellointerview.com/community/questions/word-ladder-ii/cm5eh7nrh04qi838ol80fldhe


from collections import deque

def word_ladder_2(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    wordSet = set(wordList)
    if ( endWord not in wordSet ):
        return []

    def find_distances_bfs() -> dict[str, int]:
        queue = deque([beginWord])
        distances = {beginWord:0}
        while ( queue ):
            currWord = queue.popleft()
            currDist = distances[currWord]
            # explore neighbors - try to replace each char by each of 26 letters
            for i in range(0, len(currWord)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ( currWord[i] == ch ):  continue
                    neighbor = currWord[:i] + ch + currWord[i+1:]
                    if ( (neighbor in wordSet) and (neighbor not in distances) ):
                         # valid neighbor encountered 1st time
                        distances[neighbor] = currDist + 1
                        queue.append(neighbor)
        return distances
    ##

    distances = find_distances_bfs()
    if ( endWord not in distances ):
        return []  # no path to endWord

    allPaths = []
    currPath = [endWord]  # for reversed current path

    def build_paths_dfs(word: str, path: list[str]) -> None:
        nonlocal allPaths
        # base case - if reached the begin word
        if ( word == beginWord ):
            allPaths.append(path[::-1])
            return
        # explore neighbors - try to replace each char by each of 26 letters
        # valid neighbor in min-path has distance one less than that of current
        for i in range(0, len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ( word[i] == ch ):  continue
                neighbor = word[:i] + ch + word[i+1:]
                if ( (neighbor in distances) and \
                     (distances[neighbor] == distances[word] - 1) ):
                    # step to valid neighbor, then backtrack
                    path.append(neighbor)
                    build_paths_dfs(neighbor, path)
                    path.pop()
    ##

    build_paths_dfs(endWord, currPath)
    return allPaths
##

        
def test__word_ladder_2():
    tasks = [
        ["hit", "cog", ["hot","dot","dog","lot","log","cog"]],
        # ["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]
        ["hit", "cog", ["hot","dot","dog","lot","log"]]
        # []
    ]
    for beginWord, endWord, wordList  in tasks:
        print("===================================================")
        print(f"Input: {beginWord},  {endWord},  {wordList}")
        res = word_ladder_2(beginWord, endWord, wordList)
        print(f"Result: {res}")
##

        
