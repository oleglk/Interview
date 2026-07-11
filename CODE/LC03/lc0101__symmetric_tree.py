# CODE/LC03/lc0101__symmetric_tree.py
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0101__symmetric_tree import *

# RELOAD:
# import importlib; import lc0101__symmetric_tree; importlib.reload(lc0101__symmetric_tree); from lc0101__symmetric_tree import *

# The idea: DFS, is symmetric when (leftSubtree.left == rightSubtree.right) and (leftSubtree.right == rightSubtree.left).


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def is_symmetric(root: Node|None) -> bool:
    def is_mirror(leftNode: Node|None, rightNode: Node|None) -> bool:
        # base cases
        if ( (leftNode is None) and (rightNode is None) ):
            return True
        if ( (leftNode is None) or (rightNode is None) ):
            return False
        if ( leftNode.data != rightNode.data ):
            return False

        # recursive case
        return is_mirror(leftNode.left, rightNode.right) and \
               is_mirror(leftNode.right, rightNode.left)
    ##

    if ( root is None ):
        return True
    return is_mirror(root.left, root.right)
##


def test__is_symmetric():
    #       1
    #     /   \
    #    2     2
    #   / \   / \
    #  3   4 4   3
    # Result: True
    t1n1 = Node(1);  t1n2 = Node(2);  t1n3 = Node(2)
    t1n1.left = t1n2;  t1n1.right = t1n3
    t1n4 = Node(3);    t1n5 = Node(4);     t1n6 = Node(4);    t1n7 = Node(3)
    t1n2.left = t1n4;  t1n2.right = t1n5;  t1n3.left = t1n6;  t1n3.right = t1n7
    #       1
    #     /   \
    #    2     2
    #     \     \
    #      3     3
    # Result: False
    t2n1 = Node(1);  t2n2 = Node(2);  t2n3 = Node(2)
    t2n1.left = t2n2;  t2n1.right = t2n3
    t2n4 = Node(3);   t2n5 = Node(3)
    t2n2.right = t2n4;  t2n3.right = t2n5

    tasks = [t1n1, t2n1]
    for t in tasks:
        print("====================================")
        byLevels = binary_tree_level_order(t)
        print(f"Tree by levels: {byLevels}")
        res = is_symmetric(t)
        print(f"Result: {res}")
##

