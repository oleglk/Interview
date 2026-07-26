# lc0116__populate_next_right_pointers.py
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0116__populate_next_right_pointers import *

# RELOAD:
# import importlib;    import lc0116__populate_next_right_pointers;  importlib.reload(lc0116__populate_next_right_pointers);  from lc0116__populate_next_right_pointers import *

# The idea: traverse current level by previously set 'next' pointers while populating 'next' pointers of the level below it.
# See https://guides.codepath.org/compsci/Populating-Next-Right-Pointers-in-Each-Node


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"


class TreeNode:
    def __init__(self, v):
        self.data = v;
        self.left = None;
        self.right = None;
        self.next = None;
####


def populate_next_right_pointers(root: Node|None) -> None:
    if ( root is None ):
        return
    leftmost = root
    while ( leftmost.left is not None ):  # entire next level available
        head = leftmost
        while ( head is not None ):  # traverse the current level
            head.left.next = head.right
            if ( head.next is not None ):
                head.right.next = head.next.left
            head = head.next  # contunue traversing the current level
        leftmost = leftmost.left  # switch to the next level
    return
##


def preorder_with_next(root: Node):
    if ( root is None ):
        print(" None")
        return
    print(f" {root.data}->{root.next.data if (root.next is not None) else "None"}")
    preorder_with_next(root.left)
    preorder_with_next(root.right)
    return
##


def test__populate_next_right_pointers():
    #           1
    #         /   \
    #        2     5
    #       / \   / \
    #      3   4 6   7
    t1n0 = TreeNode(1)
    t1n1 = TreeNode(2);  t1n2 = TreeNode(5)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = TreeNode(3);  t1n4 = TreeNode(4);  t1n5 = TreeNode(6);  t1n6 = TreeNode(7)
    t1n1.left = t1n3;  t1n1.right = t1n4;  t1n2.left = t1n5;  t1n2.right = t1n6

    tasks = [t1n0]
    for root in tasks:
        print("============================================")
        byLevels1 = binary_tree_level_order(root, includeNone=True)
        print(f"Input by levels: {byLevels1}")
        populate_next_right_pointers(root)
        print(f"Result:")
        preorder_with_next(root)
##


