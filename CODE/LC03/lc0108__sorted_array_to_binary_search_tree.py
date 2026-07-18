# lc0108__sorted_array_to_binary_search_tree.py
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0108__sorted_array_to_binary_search_tree import *

# RELOAD:
# import importlib;    import lc0108__sorted_array_to_binary_search_tree;  importlib.reload(lc0108__sorted_array_to_binary_search_tree);  from lc0108__sorted_array_to_binary_search_tree import *


# The idea: recursively build subtrees while taking middle element as the root.
# See https://algo.monster/liteproblems/108

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def sorted_array_to_binary_search_tree(nums: list[int]) -> Node|None:
    if ( len(nums) == 0 ):
        return None
    def make_bst(leftIdx: int, rightIdx: int) -> Node|None:
        if ( leftIdx > rightIdx ):
            return None

        midIdx = leftIdx + (rightIdx - leftIdx) // 2
        root = Node(nums[midIdx])
        root.left = make_bst(leftIdx, midIdx - 1)
        root.right = make_bst(midIdx + 1, rightIdx)

        return root
    ##
    return make_bst(0, len(nums) - 1)
##


def test__sorted_array_to_binary_search_tree():
    tasks = [
        [-10,-3,0,5,9],  # [[0],[-10,5],[None,-3,None,9]] or [[0],[-3,9],[-10,None,5,None]]
        [1,3],           # [[3],[1,None]] or [[1],[None,3]]
    ]
    for nums in tasks:
        print("============================================")
        print(f"Input: {nums}")
        resRoot = sorted_array_to_binary_search_tree(nums)
        byLevels = binary_tree_level_order(resRoot, includeNone=True)
        print(f"Result by levels: {byLevels}")
##
