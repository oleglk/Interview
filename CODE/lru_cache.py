# lru_cache.py - Design and implement a data structure for Least Recently Used (LRU) cache. It should support get and put operations in O(1) time.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lru_cache import *

# RELOAD:
# import importlib; import lru_cache; importlib.reload(lru_cache); from lru_cache import *


# The idea: doubly linked list of key-value pairs in LRU order and dictionary of key::list-item. Most recently used item added to the head of the list.


class LRUCache:
    def __init__(self):
        self.keyToIdx = {}
        self.keysAndVals = DoubleLinkedList()


    def put(self, key, val):
        if ( key in self.keyToIdx ):
            # find and remove the old key-value pair
            oldIdx = self.keyToIdx[key]
            self.keyToIdx[key] = 0  # will be made most-recently-used
            self.keysAndVals.pop(oldIdx)  # old key-value pair not needed
        # insert the new 
