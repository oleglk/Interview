# validate_binary_search_tree.py - Given the root of a binary tree, determine if it is a valid BST.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  sys.path.insert(0, os.path.join(os.getcwd(), "SET01"));    from validate_binary_search_tree import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);  from binary_tree_level_order_traversal import *;    import validate_binary_search_tree; importlib.reload(validate_binary_search_tree); from validate_binary_search_tree import *


from binary_tree_level_order_traversal import *  # for "visualization"


# The idea: inorder traversal of a valid BST produces non-decreasing sequence.
# See https://algo.monster/liteproblems/98 .
# BST properties to be checked:
# - Every node in the left subtree of a node must have values strictly less than that node's value.
# - Every node in the right subtree of a node must have values strictly greater than that node's value
# - Both the left and right subtrees themselves must also be valid BSTs


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


# Note, 'prev' is a 1-value list to allow modifications in recursive calls
def is_bst_inorder(root: Node, prev: list)-> bool:
    """Checks if subtree rooted on 'root' is BST; updates 'prev'"""
    if ( root is None ):
        return(True)

    if ( is_bst_inorder(root.left, prev) == False ):
        return(False)  # left subtree violates

    # 'prev[0]' must hold the largest value from the left subtree
    if ( root.data <= prev[0] ):
        return(False)
    prev[0] = root.data

    # during verification of the right subtree
    #   we'll check if its root is larger than the current node
    return(is_bst_inorder(root.right, prev))


def is_bst(root: Node)-> bool:
    prev = [float('-inf')]
    return(is_bst_inorder(root, prev))


def test__is_bst():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
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
    t2n0 = Node(0)
    t2n1 = Node(1);    t2n2 = Node(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##     0
    t3n0 = Node(0)
    ##      0
    ##     /
    ##    1
    t4n0 = Node(0)
    t4n1 = Node(1)
    t4n0.left = t4n1
    ##      3
    ##     / \
    ##    1   5
    ##   / \ /
    ##  0  2 4
    t5n0 = Node(3)
    t5n1 = Node(1);    t5n2 = Node(5)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n3 = Node(0);    t5n4 = Node(2);     t5n5 = Node(4)
    t5n1.left = t5n3;  t5n1.right = t5n4;  t5n2.left = t5n5


    for root in [t1n0, t2n0, t3n0, t4n0, t5n0]:
        print("===============================")
        byLevels = binary_tree_level_order(root)
        print(f"Tree by levels: {byLevels}")
        res = is_bst(root)
        print(f"Result: {res}")
