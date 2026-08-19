# lc0140__word_break_2.py
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0140__word_break_2 import *

# RELOAD:
# import importlib;    import lc0140__word_break_2;  importlib.reload(lc0140__word_break_2);  from lc0140__word_break_2 import *

# The idea: Use trie datastruct to hold the dictionary. Check every breaking position for valid prefix; if so, recursively find brekings of the suffix, then combine the latter with prefix.
# See: https://algo.monster/liteproblems/140


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    ##

    def insert(self, s: str) -> None:
        node = self
        for char in s:
            index = ord(char) - ord('a')
            if ( node.children[index] is None ):
                node.children[index] = Trie()
            node = node.children[index]
        node.isEnd = True
    ##

    def search(self, s: str) -> bool:
        node = self
        for char in s:
            index = ord(char) - ord('a')
            if ( node.children[index] is None ):
                return False
            node = node.children[index]
        return node.isEnd
    ##


def word_break_2(s: str, wordList: list[str]) -> list[str]:
    def word_break_2_recurse(remainingStr: str) -> list[list[str]]:
        if ( not remainingStr ):  # base case
            return [[]]
        result = []
        # try every breaking position for valid prefix
        for pos in range(1, len(remainingStr)+1):
            prefix = remainingStr[:pos]
            if ( trie.search(prefix) ):
                suffix = remainingStr[pos:]
                suffixBreakings = word_break_2_recurse(suffix)
                for suffixBreaking in suffixBreakings:
                    result.append([prefix] + suffixBreaking)
        return result
    ##

    trie = Trie()
    for word in wordList:
        trie.insert(word)
    resultAsListOfLists = word_break_2_recurse(s)
    resultAsListOfStrings = [" ".join(strList) \
                             for strList in resultAsListOfLists]
    return resultAsListOfStrings
##


def test__word_break_2():
    tasks = [
        ["catsanddog", ["cat","cats","and","sand","dog"]],  # ["cats and dog","cat sand dog"]
        ["pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]],  # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
        ["catsandog", ["cats","dog","sand","and","cat"]],  # []
    ]
    for s, wordList in tasks:
        print("================================================")
        print(f"Input: {s},  wordList = {wordList}")
        res = word_break_2(s, wordList)
        print(f"Result: {res}")
##

