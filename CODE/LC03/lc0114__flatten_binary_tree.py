# lc0114__flatten_binary_tree.py
# Given the root of a binary tree, flatten the tree into a "linked list":
#    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
#    The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0114__flatten_binary_tree import *

# RELOAD:
# import importlib;    import lc0114__flatten_binary_tree;  importlib.reload(lc0114__flatten_binary_tree);  from lc0114__flatten_binary_tree import *

# The idea: recursion; flatten left and right subtrees; reconnect: last of left subtree to the first of right subtree, root to first of left subtree.
# See https://www.afternerd.com/blog/flatten-binary-tree-linked-list/

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
####


def flatten_binary_tree(root: TreeNode|None) -> None:
    # base cases
    if ( root is None ):
        return
    if ( root.left is None ): # if no left subtree, this node needs no processing
        return

    # left subtree exists - recursive case
    flatten_binary_tree(root.left)
    flatten_binary_tree(root.right)
    # find last node in the flattened left subtree - go right until None
    lastInLeft = root.left
    while ( lastInLeft.right is not None ):
        lastInLeft = lastInLeft.right

    # reconnect
    lastInLeft.right = root.right
    root.right = root.left
    root.left = None
    return
##


def test__flatten_binary_tree():
    #          1             1
    #         / \             \
    #        2   5       =>    2
    #       / \   \             \
    #      3   4   6             3
    #                             \
    #                              4
    #                               \
    #                                5
    #                                 \
    #                                  6
    t1n0 = TreeNode(1)
    t1n1 = TreeNode(2);  t1n2 = TreeNode(5)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = TreeNode(3);  t1n4 = TreeNode(4);  t1n5 = TreeNode(6)
    t1n1.left = t1n3;  t1n1.right = t1n4;  t1n2.right = t1n5
    #       []
    t2n0 = None
    #       1       =>        1
    t3n0 = TreeNode(1)

    tasks = [t1n0, t2n0, t3n0]
    for root in tasks:
        print("============================================")
        byLevels1 = binary_tree_level_order(root, includeNone=True)
        print(f"Input by levels: {byLevels1}")
        flatten_binary_tree(root)
        byLevels2 = binary_tree_level_order(root, includeNone=True)
        print(f"Output by levels: {byLevels2}")

