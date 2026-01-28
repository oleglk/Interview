# serialize_binary_tree_level_order.py - Serialize using BFS including None markers.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  sys.path.insert(0, os.path.join(os.getcwd(), "SET01"));  from serialize_binary_tree_level_order import *

# RELOAD:
# import importlib; import serialize_binary_tree_level_order; importlib.reload(serialize_binary_tree_level_order); from serialize_binary_tree_level_order import *

# The idea:
# BFS inherently provides level order.

from typing import Optional
from collections import deque

from binary_tree_level_order_traversal import *  # for "visualization"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


def serialize_binary_tree_level_order(root: Optional[Node]) -> str:
    if (root is None):
        return " None"
    queue = deque([root])
    res = ""

    while ( queue ):
        node = queue.popleft()
        if ( node is not None ):
            res += f" {node.data}"
            if ( node.left is not None ):
                queue.append(node.left)
            else:
                queue.append(None)
            if ( node.right is not None ):
                queue.append(node.right)
            else:
                queue.append(None)
        else:
            res += " None"
    return res
##


def test__serialize_binary_tree_level_order():
    ##  0
    t1n0 = Node(0)
    ##     0
    ##      \
    ##       1
    ##        \
    ##         2
    t2n0 = Node(0)
    t2n1 = Node(1);    t2n2 = Node(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##      3
    ##     / \
    ##    1   5
    ##   / \ /
    ##  0  2 4
    t3n0 = Node(3)
    t3n1 = Node(1);    t3n2 = Node(5)
    t3n0.left = t3n1;  t3n0.right = t3n2
    t3n3 = Node(0);    t3n4 = Node(2);     t3n5 = Node(4)
    t3n1.left = t3n3;  t3n1.right = t3n4;  t3n2.left = t3n5

    for root in [t1n0, t2n0, t3n0]:
        print("===========================")
        byLevels = binary_tree_level_order(root)
        print(f"Tree by levels: {byLevels}")
        ser = serialize_binary_tree_level_order(root)
        print(f"Serialized: {ser}")
