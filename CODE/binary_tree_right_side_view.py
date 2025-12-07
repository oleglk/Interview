# binary_tree_right_side_view.py - Given a binary tree, imagine yourself standing on the right side. Return the values of the nodes you can see ordered from top to bottom.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from binary_tree_right_side_view import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);  from binary_tree_level_order_traversal import *;    import binary_tree_right_side_view;  importlib.reload(binary_tree_right_side_view);  from binary_tree_right_side_view import *


# The idea: perform BFS by levels left-to-right, pick the last node on each level.

from binary_tree_level_order_traversal import *  # for "visualization"

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


class Queue:
    def __init__(self):
        self.lst = []
    def enqueue(self, x):
        self.lst.append(x)
    def dequeue(self):
        if (self.is_empty()):
            raise Exception("dequeue(EMPTY)")
        return(self.lst.pop(0))
    def is_empty(self):
        return(len(self.lst) == 0)
    def size(self):
        return(len(self.lst))
##


def binary_tree_right_side_view(root: Node):
    if ( root is None ):
        raise Exception("Root is None")
    queue = Queue()  # BFS queue
    queue.enqueue(root)  # enque the 1st level

    rightSideNodes = []
    while ( not queue.is_empty() ):
        numLevelNodes = queue.size()  # currently the queue holds one level
        # levelNodes = []
        for i in range(0, numLevelNodes):
            node = queue.dequeue()
            if ( node.left is not None ):
                queue.enqueue(node.left)
            if ( node.right is not None ):
                queue.enqueue(node.right)
        # # done with current level; the last node is the rightmost one
        if ( node is not None ):
            rightSideNodes.append(node.data)
    return(rightSideNodes)
####


def test__binary_tree_right_side_view():
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
    ##     0
    ##    / \
    ##   1   2
    ##        \
    ##         3
    t5n0 = Node(0)
    t5n1 = Node(1);    t5n2 = Node(2);    t5n3 = Node(3)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3

    for root in [t1n0, t2n0, t3n0, t4n0, t5n0]:
        print("===============================")
        byLevels = binary_tree_level_order(root)
        print(f"Tree by levels: {byLevels}")
        res = binary_tree_right_side_view(root)
        print(f"Result: {res}")
