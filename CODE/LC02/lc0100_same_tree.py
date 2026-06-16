# lc0100_same_tree.py
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0100_same_tree import *

# RELOAD:
# import importlib; import lc0100_same_tree; importlib.reload(lc0100_same_tree); from lc0100_same_tree import *

# The idea: simultaneous DFS on both trees.
# See https://algo.monster/liteproblems/100


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def same_tree(p: Node|None, q: Node|None) -> bool:
    if ( (p is None) and (q is None) ):
        return True  # empty trees are identical
    if ( (p is None) or (q is None) ):  # only one is empty
        return False
    if ( p.data != q.data ):
        return False
    # check recursive case
    if ( (not same_tree(p.left, q.left)) or (not same_tree(p.right, q.right)) ):
        return False
    return True
##


def test__same_tree():
    ##    t1            t2
    ##    1     vs      1  
    ##   / \           / \ 
    ##  2   3         2   3
    t1n1 = Node(1); t1n2 = Node(2); t1n3 = Node(3)
    t1n1.left = t1n2; t1n1.right = t1n3
    t2n1 = Node(1); t2n2 = Node(2); t2n3 = Node(3)
    t2n1.left = t2n2; t2n1.right = t2n3
    ##    t3            t4
    ##    1     vs      1
    ##     \           /
    ##      2         2
    t3n1 = Node(1); t3n2 = Node(2)
    t3n1.right = t3n2
    t4n1 = Node(1); t4n2 = Node(2)
    t4n1.left = t4n2
    ##    t1            t5
    ##    1     vs      1  
    ##   / \           / \ 
    ##  2   3         2   4
    t5n1 = Node(1); t5n2 = Node(2); t5n3 = Node(4)
    t5n1.left = t5n2; t5n1.right = t5n3
    
    tasks = [
        [t1n1, t2n1],  # True
        [t3n1, t4n1],  # False
        [t1n1, t5n1],  # False
        [t1n1, t3n1],  # False
        [t4n1, t4n1],  # True
    ]
    for p, q in tasks:
        print("====================================")
        byLevelsP = binary_tree_level_order(p)
        print(f"Tree p by levels: {byLevelsP}")
        byLevelsQ = binary_tree_level_order(q)
        print(f"Tree q by levels: {byLevelsQ}")
        res = same_tree(p, q)
        print(f"Result: {res}")
##


        
    
