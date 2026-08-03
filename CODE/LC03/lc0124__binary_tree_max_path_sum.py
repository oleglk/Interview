# lc0124__binary_tree_max_path_sum.py
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0124__binary_tree_max_path_sum import *

# RELOAD:
# import importlib;    import lc0124__binary_tree_max_path_sum;  importlib.reload(lc0124__binary_tree_max_path_sum);  from lc0124__binary_tree_max_path_sum import *

# The idea:
# (Terminology: 2-side path goes left-subtree, current-node, right-subtree;  1-side path goes left-subtree, current-node or right-subtree, current-node.)
# Use recursion on current node. Both 2-side paths and 1-side paths update global max value. Only 1-side paths could be extended by the caller, thus only they are returned by recursive function.
# See https://dev.to/saxenaaman628/the-unique-insight-behind-the-binary-tree-maximum-path-sum-leetcode-124-6od

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def binary_tree_max_path_sum(root: Node) -> int:
    def binary_tree_max_path_sum_recurse(root: Node) -> int:
        nonlocal maxVal
        # base case
        if ( root is None ):
            return 0

        leftVal = binary_tree_max_path_sum_recurse(root.left)
        rightVal = binary_tree_max_path_sum_recurse(root.right)
        # leftVal and rightVal are lengths of 1-sided subpaths

        # update global max with best of 2-sided and 1-sided paths
        maxVal = max(maxVal, root.data + max(0, leftVal) + max(0, rightVal))

        # send upwards to the caller the best of 1-sided paths
        return root.data + max(max(0, leftVal), max(0, rightVal))
    ##
    if ( root is None ):
        return 0
    maxVal = float('-inf')
    binary_tree_max_path_sum_recurse(root)
    return maxVal
##


def test__binary_tree_max_path_sum():
    #       1
    #      / \
    #     2   3
    t1n0 = Node(1);  t1n1 = Node(2);  t1n2 = Node(3)
    t1n0.left = t1n1;  t1n0.right = t1n2
    # result(t1n0) = 6
    #            -10
    #            /  \
    #           9   20
    #              /  \
    #             15   7
    t2n0 = Node(-10);  t2n1 = Node(9);  t2n2 = Node(20)
    t2n0.left = t2n1;  t2n0.right = t2n2
    t2n3 = Node(15);  t2n4 = Node(7)
    t2n2.left = t2n3;  t2n2.right = t2n4
    # result(t2n0) = 42

    tasks = [t1n0, t2n0]
    for root in tasks:
        print("================================================")
        byLevels = binary_tree_level_order(root)
        print(f"Tree by levels: {byLevels}")
        res = binary_tree_max_path_sum(root)
        print(f"Result: {res}")
##
