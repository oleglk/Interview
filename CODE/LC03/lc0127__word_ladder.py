# lc0127__word_ladder.py
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#    Every adjacent pair of words differs by a single letter.
#    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#    sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
# Constraints:
#    1 <= beginWord.length <= 10
#    endWord.length == beginWord.length
#    1 <= wordList.length <= 5000
#    wordList[i].length == beginWord.length
#    beginWord, endWord, and wordList[i] consist of lowercase English letters.
#    beginWord != endWord
#    All the words in wordList are unique.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0127__word_ladder import *

# RELOAD:
# import importlib;    import lc0127__word_ladder;  importlib.reload(lc0127__word_ladder);  from lc0127__word_ladder import *

# The idea: run level-order traversal from beginWord; return level number where endWord first appears. Generate neighbor words by trying to replace each char with all 26 letters.
# See https://algo.monster/liteproblems/127

from collections import deque


def word_ladder(beginWord: str, endWord: str, wordList: list[str]) -> int:
    wordSet = set(wordList)
    if ( endWord not in wordSet ):
        return 0  # endWord is unreachable
    queue = deque([beginWord])
    levelNum = 1
    while ( queue ):
        levelNum += 1  # for words reachable from the current level
        cntAtLevel = len(queue)
        for _ in range(cntAtLevel):
            # process all words at the current level
            currWord = queue.popleft()
            # generate neighbor words
            for pos in range(0, len(currWord)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ( currWord[pos] == ch ):  continue
                    neighbor = currWord[:pos] + ch + currWord[pos+1:]
                    if ( neighbor not in wordSet ):  continue
                    # valid new neighbor word found
                    if ( neighbor == endWord ):
                        return levelNum
                    # schedule neighbor for processing and "mark visited"
                    queue.append(neighbor)
                    wordSet.remove(neighbor)  # like "visited"
    return 0  # endWord not reached
##


def test__word_ladder():
    tasks = [
        ["hit", "cog", ["hot","dot","dog","lot","log","cog"]], # 5
        ["hit", "cog", ["hot","dot","dog","lot","log"]]        # 0
    ]
    for beginWord, endWord, wordList  in tasks:
        print("===================================================")
        print(f"Input: {beginWord},  {endWord},  {wordList}")
        res = word_ladder(beginWord, endWord, wordList)
        print(f"Result: {res}")
##

