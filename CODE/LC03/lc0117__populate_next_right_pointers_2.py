# lc0117__populate_next_right_pointers_2.py
# Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0117__populate_next_right_pointers_2 import *

# RELOAD:
# import importlib;    import lc0117__populate_next_right_pointers_2;  importlib.reload(lc0117__populate_next_right_pointers_2);  from lc0117__populate_next_right_pointers_2 import *

# The idea: perform level-order traversal while keeping previous node in a variable.
# See https://algo.monster/liteproblems/117

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"


class TreeNode:
    def __init__(self, v):
        self.data = v;
        self.left = None;
        self.right = None;
        self.next = None;
####

from collections import deque

def populate_next_right_pointers_2(root: TreeNode) -> None:
    if ( root is None ):
        return
    queue = deque([root])

    while ( queue ):  # while the queue isn't empty
        # the queue contains exactly one level
        cntAtLevel = len(queue)
        prevNode = None  # for nodes whose right pointers are to be set
        for _ in range(0, cntAtLevel):  # process exactly one level
            node = queue.popleft()
            if ( prevNode is not None ):
                prevNode.next = node
            prevNode = node
            # enqueue nodes of the next level
            if ( node.left is not None ):
                queue.append(node.left)
            if ( node.right is not None ):
                queue.append(node.right)
##


# Visualisation for trees with 'next' pointers
def preorder_with_next(root: Node):
    if ( root is None ):
        print(" None")
        return
    print(f" {root.data}->{root.next.data if (root.next is not None) else "None"}")
    preorder_with_next(root.left)
    preorder_with_next(root.right)
    return
##


def test__populate_next_right_pointers_2():
    #          1
    #         / \
    #        2   5
    #       / \   \
    #      3   4   6
    t1n0 = TreeNode(1)
    t1n1 = TreeNode(2);  t1n2 = TreeNode(5)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = TreeNode(3);  t1n4 = TreeNode(4);  t1n5 = TreeNode(6)
    t1n1.left = t1n3;  t1n1.right = t1n4;  t1n2.right = t1n5
    #            1
    t2n0 = TreeNode(1)

    tasks = [t1n0, t2n0]
    for root in tasks:
        print("============================================")
        byLevels1 = binary_tree_level_order(root, includeNone=True)
        print(f"Input by levels: {byLevels1}")
        populate_next_right_pointers_2(root)
        print(f"Result:")
        preorder_with_next(root)
##

