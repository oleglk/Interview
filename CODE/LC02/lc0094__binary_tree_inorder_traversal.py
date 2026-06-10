# lc0094__binary_tree_inorder_traversal.py
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0094__binary_tree_inorder_traversal import *

# RELOAD:
# import importlib; import lc0094__binary_tree_inorder_traversal; importlib.reload(lc0094__binary_tree_inorder_traversal); from lc0094__binary_tree_inorder_traversal import *

# The idea: recursion - DFS of left subtree, print value, DFS of right subtree.
# See https://algo.monster/liteproblems/94

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node

def binary_tree_inorder_traversal(root: Node) -> list[int]:
    def dfs(root: Node) -> None:
        nonlocal result
        if ( root is None ):  # base case
            return
        
        dfs(root.left)
        result.append(root.data)
        dfs(root.right)
        return
    ##

    result: list[int] = []
    dfs(root)
    return result
##


def test__binary_tree_inorder_traversal():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
    ### Inorder: 3,1,4,0,5,2
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
    ### Inorder: 0,1,2
    t2n0 = Node(0)
    t2n1 = Node(1);    t2n2 = Node(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##     0
    ### Inorder: 0
    t3n0 = Node(0)
    ##      0
    ##     /
    ##    1
    ### Inorder: 1,0
    t4n0 = Node(0)
    t4n1 = Node(1)
    t4n0.left = t4n1
    ##     0
    ##    / \
    ##   1   2
    ##        \
    ##         3
    ### Inorder: 1,0,2,3
    t5n0 = Node(0)
    t5n1 = Node(1);    t5n2 = Node(2);    t5n3 = Node(3)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3

    for root in [t1n0, t2n0, t3n0, t4n0, t5n0]:
        print("===============================")
        byLevels = binary_tree_level_order(root)
        print(f"Original tree by levels: {byLevels}")
        res = binary_tree_inorder_traversal(root)
        print(f"Inorder: {res}")
##
