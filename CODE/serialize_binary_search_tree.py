# serialize_binary_search_tree.py - Serialize BST without null markers using preorder and reconstruct based on bounds.
# See https://algo.monster/liteproblems/449

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  sys.path.insert(0, os.path.join(os.getcwd(), "SET01"));  from serialize_binary_search_tree import *

# RELOAD:
# import importlib; import serialize_binary_search_tree; importlib.reload(serialize_binary_search_tree); from serialize_binary_search_tree import *

# The idea:
# Serialization is trivial.
# Deserialization approach:
# - Uses the BST property to reconstruct the tree without storing null markers
# - Maintains min/max bounds for valid node values at each position
# - Starting with bounds (-inf, inf) for the root:
#   -  Takes the next value from the serialized string if it's within bounds
#   -  Creates a node with that value
#   -  Recursively builds left subtree with bounds (min, current_value)
#   -  Recursively builds right subtree with bounds (current_value, max)
# - The bounds ensure nodes are placed correctly according to BST rules


from typing import Optional
import math

from binary_tree_level_order_traversal import *  # for "visualization"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


def serialize_bst(root: Optional[Node]) -> str:
    def preorder(node: Optional[Node]) -> None:
        if ( node is None ):
            return
        values.append(node.data)  # visit node first
        preorder(node.left)       # visit left subtree
        preorder(node.right)      # visit right subtree

    values = []
    preorder(root)
    # return list of integers converted to space-separated string
    return " ".join(map(str, values))


def deserialize_bst(data: str) -> Optional[Node]:
    def build_bst(minVal: int, maxVal: int) -> Optional[Node]:
        nonlocal values, currIdx
        #print(f"@@ values: {values}, currIdx: {currIdx}")
        if ( (currIdx >= len(values)) or
             (not (minVal <= values[currIdx] <= maxVal)) ):
            return None  # either finished or value out of bounds
        currVal = values[currIdx]  # (after idx-bound check!)
        # create current node (we use preorder) and advance index
        currNode = Node(currVal)
        currIdx += 1
        # process children
        currNode.left  = build_bst(minVal, currVal)
        currNode.right = build_bst(currVal, maxVal)
        # return root of the ready subtree
        return currNode

    if ( not data ):  # empty tree
        return None

    # convert serialized string into list of integers
    values = list(map(int, data.split()))
    if ( len(values) == 0 ):  # empty tree
        return None
    currIdx = 0  # initially point at the root node

    root = build_bst(-math.inf, math.inf)
    return root


def test__serialize_deserialize_bst():
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
        ser1 = serialize_bst(root)
        print(f"Serialized-1: {ser1}")
        des = deserialize_bst(ser1)
        desByLevels = binary_tree_level_order(des)
        print(f"Deserialized: {desByLevels}")
        ser2 = serialize_bst(des)
        print(f"Serialized-2: {ser2}")
