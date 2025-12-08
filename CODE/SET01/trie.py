# trie.py - Implement a trie with insert, search, and startsWith methods.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from trie import *

# RELOAD:
# import importlib; import trie; importlib.reload(trie); from trie import *


class TrieNode:
    def __init__(self):
        self.children = {}  # for (char :: node) mappings
        self.wordEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
            
    def insert(self, word):
        node = self.root
        for ch in word:
            if ( ch not in node.children ):
                node.children[ch] = TrieNode()  # insert new node to go to it
            node = node.children[ch]  # go to existent node
        node.wordEnd = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ( ch not in node.children ):
                return(False)
            node = node.children[ch]
        return(node.wordEnd)

    def starts_with(self, word):
        node = self.root
        for ch in word:
            if ( ch not in node.children ):
                return(False)
            node = node.children[ch]
        return(True)
####


def test__trie():
    words = ["abra", "abracadabra", "kit", "kitten", "world", "i", "order"]
    trie = Trie()
    for w in words:
        trie.insert(w)
    # check words that do appear
    for w in words:
        print(f"(Present) '{w}' => {trie.search(w)},  preffix '{w[:-1]}' => {trie.starts_with(w[:-1])}")
    # check words that don't appear, though prefixes can
    for w in ["tree", "scatter", "a", "at", "blank", ""]:
        print(f"(Absent)  '{w}' => {trie.search(w)},  preffix '{w[:-1]}' => {trie.starts_with(w[:-1])}")
