# kth_smallest_element_in_bst.py - Find the kth smallest element in a binary search tree.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  sys.path.insert(0, os.path.join(os.getcwd(), "SET01"));  from kth_smallest_element_in_bst import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);    import kth_smallest_element_in_bst; importlib.reload(kth_smallest_element_in_bst); from kth_smallest_element_in_bst import *

from binary_tree_level_order_traversal import *  # for "visualization"


# The idea: run inorder traversal while counting elements

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


def kth_smallest_element_in_bst(root: Node, k: int):
    """Returns kth smallest element or None if not enough nodes."""
    if ( (root is None) or (k == 0) ):
        return(None)
    elemCnt = 0  # will count till 'k'
    kthElem = None

    def inorder(root: Node):
        """Traverses the subtree until 'elemCnt' reaches 'k'."""
        nonlocal elemCnt
        nonlocal kthElem
        if ( root is None ):
            return
        # if ( elemCnt >= k ):
        #     return  # job done
        inorder(root.left)
        if ( elemCnt >= k ):
            return  # job done
        elemCnt += 1
        # print(f"@@ In {root.data}, elemCnt={elemCnt}")
        if ( elemCnt == k ):
            kthElem = root.data
            return
        inorder(root.right)
        return

    inorder(root)
    return(kthElem)


def test__kth_smallest_element_in_bst():
    ##  0
    t1n0 = Node(0)
    ##     0
    ##      \
    ##       1
    ##        \
    ##         2
    t2n0 = Node(0)
    t2n1 = Node(1);    t2n2 = Node(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##      3
    ##     / \
    ##    1   5
    ##   / \ /
    ##  0  2 4
    t3n0 = Node(3)
    t3n1 = Node(1);    t3n2 = Node(5)
    t3n0.left = t3n1;  t3n0.right = t3n2
    t3n3 = Node(0);    t3n4 = Node(2);     t3n5 = Node(4)
    t3n1.left = t3n3;  t3n1.right = t3n4;  t3n2.left = t3n5

    tasks = [ [t1n0,1], [t1n0,3], [t2n0,1], [t2n0,2],
              [t3n0,2], [t3n0,4], [t3n0,5] ]
    for root, k in tasks:
        print("===========================")
        byLevels = binary_tree_level_order(root)
        print(f"Tree by levels: {byLevels},  k={k}")
        res = kth_smallest_element_in_bst(root, k)
        print(f"Result: {res}")
