# lc0103__binary_tree_zigzag_level_order_traversal.py
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0103__binary_tree_zigzag_level_order_traversal import *

# RELOAD:
# import importlib;    import lc0103__binary_tree_zigzag_level_order_traversal;  importlib.reload(lc0103__binary_tree_zigzag_level_order_traversal);  from lc0103__binary_tree_zigzag_level_order_traversal import *

# The idea: fill the queue one level at a time; rely on catching number of elements in the queue when it holds exactly next level. Alternate order within each level.


from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


def binary_tree_zigzag_level_order(root: Node|None) -> list[list[int]]|None:
    if ( root is None ):
        return None
    resListOfLists = []
    leftToRight = True
    queue = deque([root])

    while ( len(queue) > 0 ):
        numNodesAtOneLevel = len(queue)  # at this time queue holds one level
        oneLevelNodeLabels = deque([])  # allows varying the order
        for _ in range(0, numNodesAtOneLevel):  # process nodes of one level
            node = queue.popleft()
            if ( leftToRight ):
                oneLevelNodeLabels.append(node.data)
            else:
                oneLevelNodeLabels.appendleft(node.data)
            if ( node.left is not None ):
                queue.append(node.left)
            if ( node.right is not None ):
                queue.append(node.right)
        resListOfLists.append(list(oneLevelNodeLabels))
        leftToRight = not leftToRight

    return resListOfLists
##


def test__binary_tree_zigzag_level_order():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
    ## By levels: [[0], [2, 1], [3, 4, 5]]
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
    ## By levels: [[0], [1], [2]]
    t2n0 = Node(0)
    t2n1 = Node(1);    t2n2 = Node(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##     0
    ## By levels: [[0]]
    t3n0 = Node(0)
    ##      0
    ##     /
    ##    1
    ## By levels: [[0], [1]]
    t4n0 = Node(0)
    t4n1 = Node(1)
    t4n0.left = t4n1
    ##     1
    ##    / \
    ##   0   2
    ##        \
    ##         3
    ## By levels: [[1], [2, 0], [3]]
    t5n0 = Node(1)
    t5n1 = Node(0);    t5n2 = Node(2);    t5n3 = Node(3)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3

    tasks = [t1n0, t2n0, t3n0, t4n0, t5n0]
    for root in tasks:
        byLevels = binary_tree_zigzag_level_order(root)
        print(f"By levels: {byLevels}")
##
