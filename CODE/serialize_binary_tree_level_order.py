# serialize_binary_tree_level_order.py - Serialize using BFS including None markers.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  sys.path.insert(0, os.path.join(os.getcwd(), "SET01"));  from serialize_binary_tree_level_order import *

# RELOAD:
# import importlib; import serialize_binary_tree_level_order; importlib.reload(serialize_binary_tree_level_order); from serialize_binary_tree_level_order import *

# The idea:
# BFS inherently provides level order.

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


def serialize_binary_tree_level_order(root: Node) > str:
    if (root is None):
        return ""
    queue = dequeue([root])
    res = ""

    while ( queue ):
        node = queue.popleft()
        res += f" 
