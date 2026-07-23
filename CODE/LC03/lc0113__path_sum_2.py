# lc0113__path_sum_2.py
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0113__path_sum_2 import *

# RELOAD:
# import importlib;    import lc0113__path_sum_2;  importlib.reload(lc0113__path_sum_2);  from lc0113__path_sum_2 import *

# The idea: recursion while keeping current path in "global" variable and passing current path sum as argument.
# See https://algo.monster/liteproblems/113

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
####


def find_paths_for_sum(root: TreeNode, targetSum: int) -> list[list[int]]:
    def find_paths_recurse(root: TreeNode, currentSum: int) -> None:
        nonlocal currentPath
        if ( root is None ):
            return
        currentSum += root.data
        currentPath.append(root.data)

        if ( (root.left is None) and (root.right is None) \
             and (currentSum == targetSum) ):
            result.append(currentPath[:])

        # recurse with the current node included
        find_paths_recurse(root.left, currentSum)
        find_paths_recurse(root.right, currentSum)

        # pop the current node to explore other routes
        currentPath.pop()

        return
    ##

    result: list[list[int]] = []
    currentPath: list[int] = []
    find_paths_recurse(root, 0)
    return result
##


def test__find_paths_for_sum():
    #                                 5
    #                                / \
    #                               4   8
    #                              /   / \
    #                             11  13  4
    #                            / \     / \
    #                           7   2   5   1
    # targetSum = 22
    # Result = [[5,4,11,2], [5,8,4,5]]
    t1n0 = TreeNode(5)
    t1n1 = TreeNode(4);  t1n2 = TreeNode(8)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = TreeNode(11);  t1n4 = TreeNode(13);  t1n5 = TreeNode(4)
    t1n1.left = t1n3;  t1n2.left = t1n4;  t1n2.right = t1n5
    t1n6 = TreeNode(7);  t1n7 = TreeNode(2);  t1n8 = TreeNode(5);  t1n9 = TreeNode(1)
    t1n3.left = t1n6;  t1n3.right = t1n7;  t1n5.left = t1n8;  t1n5.right = t1n9
    #                                1
    #                               / \
    #                              2   3
    # targetSum = 5
    # Result = []
    t2n0 = TreeNode(1)
    t2n1 = TreeNode(2);  t2n2 = TreeNode(3)
    t2n0.left = t2n1;  t2n0.right = t2n2
    #                                1
    #                               /
    #                              2
    # targetSum = 0
    # Result = []
    t3n0 = TreeNode(1)
    t3n1 = TreeNode(2)
    t3n0.left = t3n1

    tasks = [
        [t1n0, 22],
        [t2n0, 5],
        [t3n0, 0],
    ]
    for root, sum in tasks:
        byLevels = binary_tree_level_order(root, includeNone=True)
        print(f"By levels: {byLevels}")
        print(f"Sum to find: {sum}")
        res = find_paths_for_sum(root, sum)
        print(f"Result: {res}")
##

    
