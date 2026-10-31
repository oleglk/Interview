# lc0199__binary_tree_right_side_view.py
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0199__binary_tree_right_side_view import *

# RELOAD:
# import importlib;    import lc0199__binary_tree_right_side_view;  importlib.reload(lc0199__binary_tree_right_side_view);  from lc0199__binary_tree_right_side_view import *

# The idea: run level-order traversal while picking rightmost(last) node of each level for the result.
# See: https://algo.monster/liteproblems/199


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node

from collections import deque


def binary_tree_right_side_view(root: Node|None) -> list[Node]:
    if ( root is None ):
        return []
    queue = deque([root])
    result = []

    while ( queue ):
        # at this point the queue holds exactly one level
        numNodesOnLevel = len(queue)
        for i in range(0, numNodesOnLevel):
            node = queue.popleft()
            if ( i == numNodesOnLevel - 1 ):  # righmost node of the level
                result.append(node.data)
            if ( node.left is not None ):
                queue.append(node.left)
            if ( node.right is not None ):
                queue.append(node.right)
    return result
##


def test__binary_tree_right_side_view():
    #      0
    #     / \
    #   1     2
    #  / \   / \
    # 3   4 5   6
    t1n1 = Node(0);  t1n2 = Node(1);  t1n3 = Node(2)
    t1n1.left = t1n2;  t1n1.right = t1n3
    t1n4 = Node(3);  t1n5 = Node(4);  t1n6 = Node(5);  t1n7 = Node(6)
    t1n2.left = t1n4;  t1n2.right = t1n5
    t1n3.left = t1n6;  t1n3.right = t1n7
    #  result = [0, 2, 6]
    
    #      0
    #     /
    #   1
    #  / \
    # 3   4
    t2n1 = Node(0);  t2n2 = Node(1)
    t2n1.left = t2n2
    t2n3 = Node(3);  t2n4 = Node(4)
    t2n2.left = t2n3;  t2n2.right = t2n4
    #  result = [0, 1, 4]

    tasks = [t1n1, t2n1]
    for root in tasks:
        print("============================================")
        byLevels = binary_tree_level_order(root, includeNone=False)
        print(f"Input by levels: {byLevels}")
        res = binary_tree_right_side_view(root)
        print(f"Result: {res}")
##
