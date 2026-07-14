# lc0104__binary_tree_max_depth.py
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0104__binary_tree_max_depth import *

# RELOAD:
# import importlib;    import lc0104__binary_tree_max_depth;  importlib.reload(lc0104__binary_tree_max_depth);  from lc0104__binary_tree_max_depth import *


# The idea: recursion; depth = 1 + max(delthLeft, depthRight)
# See https://www.geeksforgeeks.org/dsa/find-the-maximum-depth-or-height-of-a-tree/


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def binary_tree_max_depth(root: Node|None) -> int:
    if ( root is None):
        return 0
    depthLeft = binary_tree_max_depth(root.left)
    depthRight = binary_tree_max_depth(root.right)
    maxDepth = 1 + max(depthLeft, depthRight)
    return maxDepth
##


def test__binary_tree_max_depth():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
    ## Depth: 3
    t1n0 = Node(0)
    t1n1 = Node(1);    t1n2 = Node(2)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = Node(3);    t1n4 = Node(4);     t1n5 = Node(5)
    t1n1.left = t1n3;  t1n1.right = t1n4;  t1n2.left = t1n5
    ##     0
    ##      \
    ##       1
    ##        \
    ##         2
    ## Depth: 3
    t2n0 = Node(0)
    t2n1 = Node(1);    t2n2 = Node(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##     0
    ## Depth: 1
    t3n0 = Node(0)
    ##      0
    ##     /
    ##    1
    ## Depth: 2
    t4n0 = Node(0)
    t4n1 = Node(1)
    t4n0.left = t4n1
    ##     1
    ##    / \
    ##   0   2
    ##        \
    ##         3
    ## Depth: 3
    t5n0 = Node(1)
    t5n1 = Node(0);    t5n2 = Node(2);    t5n3 = Node(3)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3

    tasks = [t1n0, t2n0, t3n0, t4n0, t5n0]
    for t in tasks:
        print("====================================")
        byLevels = binary_tree_level_order(t)
        print(f"Tree by levels: {byLevels}")
        res = binary_tree_max_depth(t)
        print(f"Result: {res}")
##
