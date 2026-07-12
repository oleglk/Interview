# lc0102__binary_tree_level_order_traversal.py
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0102__binary_tree_level_order_traversal import *

# RELOAD:
# import importlib;    import lc0102__binary_tree_level_order_traversal;  importlib.reload(lc0102__binary_tree_level_order_traversal);  from lc0102__binary_tree_level_order_traversal import *

# The idea: fill the queue one level at a time; rely on catching number of elements in the queue when it holds exactly next level.


from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


def binary_tree_level_order(root: Node|None) -> list[list[int]]|None:
    if ( root is None ):
        return None
    queue = deque([root])  # 1st level has single node
    resListOfLists = []
    while queue:
        numNodesAtLevel = len(queue)  # at this moment queue contains 1 level
        nodesAtLevel = []  # for labels of nodes from current level
        # pull nodes of one level from the queue
        for i in range(0, numNodesAtLevel):
            node = queue.popleft()
            nodesAtLevel.append(node.data)
            # push nodes of the next level into the queue
            if ( node.left is not None ):
                queue.append(node.left)
            if ( node.right is not None ):
                queue.append(node.right)
        resListOfLists.append(nodesAtLevel[:])
    return resListOfLists
##


def test__binary_tree_level_order():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
    ## By levels: [[0], [1, 2], [3, 4, 5]]
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
    ## By levels: [[1], [0, 2], [3]]
    t5n0 = Node(1)
    t5n1 = Node(0);    t5n2 = Node(2);    t5n3 = Node(3)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3

    tasks = [t1n0, t2n0, t3n0, t4n0, t5n0]
    for root in tasks:
        byLevels = binary_tree_level_order(root)
        print(f"By levels: {byLevels}")
##
