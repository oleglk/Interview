# CODE/LC03/lc0110__balanced_binary_tree.py
# Given a binary tree, determine if it is heigt-balanced.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0110__balanced_binary_tree import *

# RELOAD:
# import importlib;    import lc0110__balanced_binary_tree;  importlib.reload(lc0110__balanced_binary_tree);  from lc0110__balanced_binary_tree import *

# The idea: use same recursive function to calc subtree heights and check subtree balance. The tree is balanced if for any subtree left-right height differ by maximum 1.

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
####


def balanced_binary_tree(root: TreeNode|None) -> bool:
    def check_height(root: TreeNode|None) -> int:
        """Returns subtree height or -1 if unbalanced"""
        if ( root is None ):
            return 0
        leftHeight = check_height(root.left)
        rightHeight = check_height(root.right)
        if ( (leftHeight == -1) or (rightHeight == -1) \
             or (abs(leftHeight - rightHeight) > 1) ):
            return -1  # unbalanced
        return 1 + max(leftHeight, rightHeight)  # balanced, return height
    ##
    return check_height(root) != -1
##


def test__balanced_binary_tree():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
    ## Is balanced: True
    t1n0 = TreeNode(0)
    t1n1 = TreeNode(1);    t1n2 = TreeNode(2)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = TreeNode(3);    t1n4 = TreeNode(4);     t1n5 = TreeNode(5)
    t1n1.left = t1n3;  t1n1.right = t1n4;  t1n2.left = t1n5
    ##     0
    ##      \
    ##       1
    ##        \
    ##         2
    ## Is balanced: False
    t2n0 = TreeNode(0)
    t2n1 = TreeNode(1);    t2n2 = TreeNode(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##     0
    ## Is balanced: True
    t3n0 = TreeNode(0)
    ##      0
    ##     /
    ##    1
    ## Is balanced: True
    t4n0 = TreeNode(0)
    t4n1 = TreeNode(1)
    t4n0.left = t4n1
    ##     1
    ##    / \
    ##   0   2
    ##        \
    ##         3
    ##        /
    ##       4
    ## Is balanced: False
    t5n0 = TreeNode(1)
    t5n1 = TreeNode(0);    t5n2 = TreeNode(2);    t5n3 = TreeNode(3);    t5n4 = TreeNode(4)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3
    t5n3.left = t5n4

    tasks = [t1n0, t2n0, t3n0, t4n0, t5n0]
    for root in tasks:
        byLevels = binary_tree_level_order(root, includeNone=True)
        print(f"By levels: {byLevels}")
        res = balanced_binary_tree(root)
        print(f"Is balanced: {res}")
##
