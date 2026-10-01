# lc0156__binary_tree_upside_down.py
# You are given a binary tree and need to transform it by flipping it upside down according to specific rules.
# The transformation works as follows:
#    The leftmost node (original left child) becomes the new root of the tree
#    The original root node becomes the right child of what was previously its left child
#    The original right child becomes the left child of what was previously the root's left child
# This transformation is applied recursively throughout the tree, level by level, starting from the bottom.
# For example, if you have a tree structure like:
#     1
#    / \
#   2   3
#  / \
# 4   5
# After the transformation, it becomes:
#   4
#  / \
# 5   2
#    / \
#   3   1
# The problem guarantees that:
#    Every right node has a sibling (a left node that shares the same parent)
#    No right node has any children of its own

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0156__binary_tree_upside_down import *

# RELOAD:
# import importlib;    import lc0156__binary_tree_upside_down;  importlib.reload(lc0156__binary_tree_upside_down);  from lc0156__binary_tree_upside_down import *


# The idea: recursive call on left subtree, then rearranging pointers on the current level.
# See: https://algo.monster/liteproblems/156

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node


def binary_tree_upside_down(root: Node|None) -> Node|None:
    # base cases
    if ( root is None ):  return None
    if ( root.left is None ):  # it's a leaf, right child absent too - guaranteed
        return root  # no rearrangement needed for single node

    # recurse on left subtree only (right child is leaf or absent)
    newRoot = binary_tree_upside_down(root.left)

    # rearrange pointers on the current level
    #    The original root node becomes the right child of what was previously its left child
    root.left.right = root
    #    The original right child becomes the left child of what was previously the root's left child
    root.left.left = root.right
    root.left  = None  # old root is now a leaf
    root.right = None  # old root is now a leaf

    return  newRoot
##


def test__binary_tree_upside_down():
#     1
#    / \
#   2   3
#  / \
# 4   5
# Result:
#   4
#  / \
# 5   2
#    / \
#   3   1
    t1n1 = Node(1)
    t1n2 = Node(2);  t1n3 = Node(3)
    t1n1.left = t1n2;  t1n1.right = t1n3
    t1n4 = Node(4);  t1n5 = Node(5)
    t1n2.left = t1n4;  t1n2.right = t1n5
    tasks = [t1n1]
    for root in tasks:
        print("================================================")
        byLevelsIn = binary_tree_level_order(root, includeNone=True)
        print(f"Input by levels: {byLevelsIn}")
        newRoot = binary_tree_upside_down(root)
        byLevelsOut = binary_tree_level_order(newRoot, includeNone=True)
        print(f"Input by levels: {byLevelsOut}")

    
