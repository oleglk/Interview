# lc0208__implement_trie.py
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
# Implement the Trie class:
#    Trie() Initializes the trie object.
#    void insert(String word) Inserts the string word into the trie.
#    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0208__implement_trie import *

# RELOAD:
# import importlib;    import lc0208__implement_trie;  importlib.reload(lc0208__implement_trie);  from lc0208__implement_trie import *

# The idea: see the code.
# See: https://algo.monster/liteproblems/208

from __future__ import annotations  # to reference Trie within its method


class Trie:
    def __init__(self):
        self.children = [None] * 26  # one for each letter
        self.isEnd = False           # whether a word ends at this node
    ##

    def insert(self, word: str) -> None:
        currNode = self
        for ch in word:
            code = ord(ch) - ord('a')
            if ( self.children[code] is None ):
                 self.children[code] = Trie()
            currNode = self.children[code]
        currNode.isEnd = True
    ##
    
    def _find_prefix(self, prefix: str) -> Trie|None:
        """Returns last node of the prefix or None if not found."""
        currNode = self
        for ch in prefix:
            code = ord(ch) - ord('a')
            if ( self.children[code] is None ):
                return None
        currNode = self.children[code]
        return currNode
    ##

    def search(self, word: str) -> bool:
        lastNode = self._find_prefix(word)
        return (lastNode is not None) and lastNode.isEnd
    ##

    def startsWith(self, prefix: str) -> bool:
        lastNode = self._find_prefix(prefix)
        return (lastNode is not None)
    ##
###


def test__Trie():
    content = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    tr = Trie()
    for word in content:
        tr.insert(word)

    tasks = [
        "ins",     # False, True
        "insert",  # True, True
        "apple",   # False, False
        "sea",     # False, True
        "search",  # True, True
    ]
    for word in tasks:
        print("=======================================")
        print(f"Input: {word}")
        resSearch = tr.search(word)
        resStarts = tr.startsWith(word)
        print(f"Search: {resSearch}, StartsWith: {resStarts}")
##
