# lc0111__min_depth_of_binary_tree.py
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0111__min_depth_of_binary_tree import *

# RELOAD:
# import importlib;    import lc0111__min_depth_of_binary_tree;  importlib.reload(lc0111__min_depth_of_binary_tree);  from lc0111__min_depth_of_binary_tree import *

# The idea: recursively treat all 3 cases: no kids, one kid, 2 kids.
# See https://algo.monster/liteproblems/111


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
####

def min_depth_of_binary_tree(root: TreeNode|None) -> int:
    # base cases
    if ( root is None):
        return 0
    if ( (root.left is None) and (root.right is None) ):
        return 1  # leaf
    
    # recursive cases - 1 or 2 children
    if ( (root.left is not None) and (root.right is not None) ):
        return 1 + min(min_depth_of_binary_tree(root.left), \
                       min_depth_of_binary_tree(root.right))
    
    if ( root.left is not None ):
        return 1 + min_depth_of_binary_tree(root.left)
    if ( root.right is not None ):
        return 1 + min_depth_of_binary_tree(root.right)

    raise Exception("Should not reach here")
##


def test__min_depth_of_binary_tree():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
    ## Min depth = 3
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
    ## Min depth = 3
    t2n0 = TreeNode(0)
    t2n1 = TreeNode(1);    t2n2 = TreeNode(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##     0
    ## Min depth = 1
    t3n0 = TreeNode(0)
    ##      0
    ##     /
    ##    1
    ## Min depth = 2
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
    ## Min depth = 2
    t5n0 = TreeNode(1)
    t5n1 = TreeNode(0);    t5n2 = TreeNode(2);    t5n3 = TreeNode(3);    t5n4 = TreeNode(4)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3
    t5n3.left = t5n4

    tasks = [t1n0, t2n0, t3n0, t4n0, t5n0]
    for root in tasks:
        byLevels = binary_tree_level_order(root, includeNone=True)
        print(f"By levels: {byLevels}")
        res = min_depth_of_binary_tree(root)
        print(f"Min depth: {res}")
##
