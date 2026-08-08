# lc0129__sum_root_to_leaf.py
# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
#    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0129__sum_root_to_leaf import *

# RELOAD:
# import importlib;    import lc0129__sum_root_to_leaf;  importlib.reload(lc0129__sum_root_to_leaf);  from lc0129__sum_root_to_leaf import *

# The idea: use pre-order DFS while supplying numbers till parent node.
# See https://algo.monster/liteproblems/129


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def sum_root_to_leaf(root: Node) -> int:
    def sum_root_to_leaf_recurse(root: Node, numTillParent: int) -> int:
        if ( root is None ):
            return 0
        currNum = 10 * numTillParent + root.data  # append the number at root

        if ( (root.left is None) and (root.right is None) ):  # leaf node
            return currNum

        # recursive cases
        leftSum = sum_root_to_leaf_recurse(root.left, currNum)
        rightSum = sum_root_to_leaf_recurse(root.right, currNum)
        return leftSum + rightSum
    ##
    return sum_root_to_leaf_recurse(root, 0)
##


def test__sum_root_to_leaf():
    #          1
    #         / \
    #        2   3
    # sum = 25
    t1n0 = Node(1);  t1n1 = Node(2);  t1n2 = Node(3)
    t1n0.left = t1n1;  t1n0.right = t1n2
    #          4
    #         / \
    #        9   0
    #       / \
    #      5   1
    # sum = 1026
    t2n0 = Node(4);  t2n1 = Node(9);  t2n2 = Node(0)
    t2n0.left = t2n1;  t2n0.right = t2n2
    t2n3 = Node(5);  t2n4 = Node(1)
    t2n1.left = t2n3;  t2n1.right = t2n4

    tasks = [t1n0, t2n0]
    for root in tasks:
        print("=============================================")
        byLevels = binary_tree_level_order(root)
        print(f"Tree by levels: {byLevels}")
        res = sum_root_to_leaf(root)
        print(f"Result: {res}")
##
