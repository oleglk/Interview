# lc0144__binary_tree_preorder.py
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0144__binary_tree_preorder import *

# RELOAD:
# import importlib;    import lc0144__binary_tree_preorder;  importlib.reload(lc0144__binary_tree_preorder);  from lc0144__binary_tree_preorder import *

# The idea: visit node, DFS on left subtree, DFS on right subtree.

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node


def binary_tree_preorder(root: Node) -> list[int]:
    result = []
    def preorder_recurse(node: Node) -> None:
        nonlocal result
        if ( node is None ):
            return
        result.append(node.data)  # visit the node first
        preorder_recurse(node.left)
        preorder_recurse(node.right)
        return
    ##
    preorder_recurse(root)
    return result
##


def test__binary_tree_preorder():
    #    1
    #     \
    #      2
    #     /
    #    3
    # Result:  [1,2,3]
    t1n1 = Node(1);  t1n2 = Node(2);  t1n3 = Node(3)
    t1n1.right = t1n2;  t1n2.left = t1n3
    
    #                    1
    #                  /   \
    #                 2     3
    #                / \     \
    #               4   5     8
    #                  / \   /
    #                 6   7 9
    # Result:  [1,2,4,5,6,7,3,8,9]
    t2n1 = Node(1);  t2n2 = Node(2);  t2n3 = Node(3);
    t2n4 = Node(4);  t2n5 = Node(5);  t2n6 = Node(6);
    t2n7 = Node(7);  t2n8 = Node(8);  t2n9 = Node(9);
    t2n1.left = t2n2;  t2n1.right = t2n3
    t2n2.left = t2n4;  t2n2.right = t2n5;  t2n3.right = t2n8
    t2n5.left = t2n6;  t2n5.right = t2n7;  t2n8.left = t2n9
    
    # None
    # Result: []
    t3n1 = None

    #   1
    # Result: [1]
    t4n1 = Node(1)

    tasks = [t1n1, t2n1, t3n1, t4n1]
    for root in tasks:
        byLevels = binary_tree_level_order(root, includeNone=True)
        print(f"Input by levels: {byLevels}")
        res = binary_tree_preorder(root)
        print(f"Result: {res}")
##

