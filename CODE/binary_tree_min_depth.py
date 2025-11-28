# binary_tree_min_depth.py - Find the minimum depth of a binary tree (the number of nodes along the shortest path from the root node down to the nearest leaf node).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from binary_tree_min_depth import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);  from binary_tree_level_order_traversal import *;    import binary_tree_min_depth;  importlib.reload(binary_tree_min_depth);  from binary_tree_min_depth import *

from binary_tree_level_order_traversal import *  # for "visualization"

# The idea: recursion minDepth = 1 + min(min-depth among all existent subtrees)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


def binary_tree_min_depth(root):
    if ( root is None ):
        return(0)
    if ( (root.left is None) and (root.right is None) ):  # leaf
        return(1)
    
    if ( root.left is None ):
        return(1 + binary_tree_min_depth(root.right))
    if ( root.right is None ):
        return(1 + binary_tree_min_depth(root.left))
    return(1 + min(binary_tree_min_depth(root.left),
                   binary_tree_min_depth(root.right)))


def test__binary_tree_min_depth():
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
        res = binary_tree_min_depth(root)
        print("===============================")
        byLevels = binary_tree_level_order(root)
        print(f"Tree by levels: {byLevels}")
        print(f"Result: {res}")
