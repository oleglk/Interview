# binary_tree_level_order_traversal.py - Given the root of a binary tree, return the level order traversal of its nodes' values (from left to right, level by level).


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from binary_tree_level_order_traversal import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);  from binary_tree_level_order_traversal import *


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


def binary_tree_level_order(root: Node):
    """Traversal of binary tree nodes from left to right, level by level.
       Returns list of lists of per-level node-data values."""
    if (root is None):
        return(None)
    queue = Queue()
    queue.enqueue(root)

    resListOfLists = []
    while ( not queue.is_empty() ):
        numLevelNodes = queue.size()  # currently the queue holds one level
        levelNodes = []
        for i in range(0, numLevelNodes):
            # traverse one level of the tree - distinguished by count
            # enqueue the next level
            node = queue.dequeue()
            levelNodes.append(node.data)
            if ( node.left is not None ):
                queue.enqueue(node.left)
            if ( node.right is not None ):
                queue.enqueue(node.right)
        resListOfLists.append(levelNodes)  # done with current level
    return(resListOfLists)


def test__binary_tree_level_order():
    t1n0 = Node(0)
    t1n1 = Node(1);    t1n2 = Node(2)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = Node(3);    t1n4 = Node(4);     t1n5 = Node(5)
    t1n1.left = t1n3;  t1n1.right = t1n4;  t1n2.left = t1n5
    t2n0 = Node(0)
    t2n1 = Node(1);    t2n2 = Node(2)
    t2n0.right = t2n1
    t2n1.right = t2n2

    for root in [t1n0, t2n0]:
        byLevels = binary_tree_level_order(root)
        print(f"Result: {byLevels}")

