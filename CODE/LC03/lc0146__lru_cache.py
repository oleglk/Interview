# lc0146__lru_cache.py
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
#    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#    int get(int key) Return the value of the key if the key exists, otherwise return -1.
#    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0146__lru_cache import *

# RELOAD:
# import importlib;    import lc0146__lru_cache;  importlib.reload(lc0146__lru_cache);  from lc0146__lru_cache import *

# The idea: combo of 2 datastructures:
# - doubly linked list holding keys and values
# - dictionary mapping keys to the doubly-linked-list nodes.
# See: https://www.hellointerview.com/community/questions/lru-cache/cm5eh7nrh04r2838os7lk8nwf

class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    ##
####

    
class LRUCache:
    def __init__(self, capacity: int) -> None:
        if ( capacity <= 0 ):
            raise Exception("Capacity should be positive")
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head
    ##

    def get(self, key: int) -> int:
        if ( key not in self.map ):
            return -1
        node = self.map[key]
        self._move_to_head(node)  # make most-recently-used
        return node.value
    ##

    def put(self, key: int, value: int) -> None:
        if ( key not in self.map ):  # need to add new record
            if ( len(self.map) == self.capacity ):  # need to evict LRU record
                lruRec = self.tail.prev
                lruKey = lruRec.key
                self._remove_from_list(lruRec)
                del self.map[lruKey]
            node = Node(key, value)
            self._insert_into_head(node)
            self.map[key] = node
        else:                        # need to update existing record
            node = self.map[key]
            node.value = value
            self._move_to_head(node)  # make most-recently-used
    ##

    def _remove_from_list(self, node: Node) -> None:
        if ( node is None ):  return
        node.prev.next = node.next
        node.next.prev = node.prev
    ##

    def _insert_into_head(self, node: Node) -> None:
        if ( node is None ):  return
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
    ##
    
    def _move_to_head(self, node: Node) -> None:
        if ( node is None ):  return
        self._remove_from_list(node)
        self._insert_into_head(node)
    ##
####


def test__lru_cache():
    lRUCache = LRUCache(2);
    lRUCache.put(1, 1); # cache is {1=1}
    lRUCache.put(2, 2); # cache is {1=1, 2=2}
    print(lRUCache.get(1));    # return 1
    lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2));    # return -1 (not found)
    lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1));    # return -1 (not found)
    print(lRUCache.get(3));    # return 3
    print(lRUCache.get(4));    # return 4
##
