# lc0098_validate_binary_search_tree.py
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# -    The left subtree of a node contains only nodes with keys strictly less than the node's key.
# -    The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# -    Both the left and right subtrees must also be binary search trees.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0098_validate_binary_search_tree import *

# RELOAD:
# import importlib; import lc0098_validate_binary_search_tree; importlib.reload(lc0098_validate_binary_search_tree); from lc0098_validate_binary_search_tree import *

# The idea: DFS into subtrees while checking values against valid range. The latter updated at each node by its value.
# See https://www.geeksforgeeks.org/dsa/a-program-to-check-if-a-binary-tree-is-bst-or-not/


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def is_valid_bst_recurse(root: Node, minVal: int, maxVal: int) -> bool:
    if ( root is None ):
        return True  # empty tree is valid BST
    if ( (root.data < minVal) or (root.data > maxVal) ):
        return False  # the current node violates BST property

    leftOK = is_valid_bst_recurse(root.left, minVal, root.data)
    rightOK = is_valid_bst_recurse(root.right, root.data, maxVal)
    return (leftOK and rightOK)
##


def is_valid_bst(root: Node) -> bool:
    return is_valid_bst_recurse(root, float('-inf'), float('inf'))
##


def test__is_valid_bst():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
    ### Is-Valid = False
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
    ### Is-Valid = True
    t2n0 = Node(0)
    t2n1 = Node(1);    t2n2 = Node(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##     0
    ### Is-Valid = True
    t3n0 = Node(0)
    ##      0
    ##     /
    ##    1
    ### Is-Valid = False
    t4n0 = Node(0)
    t4n1 = Node(1)
    t4n0.left = t4n1
    ##     1
    ##    / \
    ##   0   2
    ##        \
    ##         3
    ### Is-Valid = True
    t5n0 = Node(1)
    t5n1 = Node(0);    t5n2 = Node(2);    t5n3 = Node(3)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3

    for root in [t1n0, t2n0, t3n0, t4n0, t5n0]:
        print("===============================")
        byLevels = binary_tree_level_order(root)
        print(f"Original tree by levels: {byLevels}")
        res = is_valid_bst(root)
        print(f"Inorder: {res}")
##
    
