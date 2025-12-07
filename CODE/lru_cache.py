# lru_cache.py - Design and implement a data structure for Least Recently Used (LRU) cache. It should support get and put operations in O(1) time.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lru_cache import *

# RELOAD:
# import importlib;  import UTILS.lib__double_linked_list;  importlib.reload(UTILS.lib__double_linked_list);  from UTILS.lib__double_linked_list import *;    import lru_cache; importlib.reload(lru_cache); from lru_cache import *


# The idea: doubly linked list of key-value pairs in LRU order and dictionary of key::list-item. Most recently used item added to the tail of the list. Accessed existent item moved to the tail of the list.

from UTILS.lib__double_linked_list import *


class LRUCache:
    def __init__(self, capacity):
        if ( capacity == 0 ):
            raise Exception("capacity == 0")
        self.capacity = capacity
        self.keyToListNode = {}
        self.keysAndVals = DoubleLinkedList()


    def put(self, key, val):
        print(f"-I- put({key}, {val})")
        if ( key in self.keyToListNode ):
            # find and remove the old key-value pair
            oldNode = self.keyToListNode[key]
            self.keysAndVals.delete_by_node(oldNode)
        if ( len(self.keyToListNode) == self.capacity ):
            self._discard_oldest()
        # insert the new key-value pair
        newNode = self.keysAndVals.add_in_tail((key, val))
        self.keyToListNode[key] = newNode


    def get(self, key):
        print(f"-I- get({key})")
        if ( key not in self.keyToListNode ):
            return(None)
        theNode = self.keyToListNode[key]
        self.keysAndVals.move_to_tail(theNode)
        return(theNode.elem[1])


    def _discard_oldest(self):
        keyAndVal = self.keysAndVals.delete_head()
        if ( keyAndVal is None ):
            return  # was empty
        key, val = keyAndVal
        del self.keyToListNode[key]
        print(f"-I- Discarded LRU ({key}, {val})")
########


def test__lru_cache():
    cache = LRUCache(4)
    for k in range(0, 6):
        cache.put(k, f"val_{k}")  # 0 and 1 should be discarded
    node2 = cache.get(2)          # refresh 2 - make 3 LRU
    cache.put(6, "val_6")         # expected content: 2 4 5 6
    print(f"Result: {cache.keysAndVals.content_to_string()}")
