# binary_search_tree_iterator.py - Iterator returning next smallest element using controlled stack.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  sys.path.insert(0, os.path.join(os.getcwd(), "SET01"));  from binary_search_tree_iterator import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);    import binary_search_tree_iterator; importlib.reload(binary_search_tree_iterator); from binary_search_tree_iterator import *

from binary_tree_level_order_traversal import *  # for "visualization"


# The idea: inorder traversal using explicit stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


class BSTIterator:
    def __init__(self, root: Node):
        self.stack = []
        self._push_all_left(root)


    def has_next(self) -> bool:
        return(len(self.stack) != 0)


    def get_next(self) -> int:
        if ( not self.has_next() ):
            return(None)
        theNext = self.stack.pop()
        # the next smallest element will be in the right subtree if any
        if ( theNext.right is not None ):
            self._push_all_left(theNext.right)
        return(theNext.data)


    def _push_all_left(self, node: Node):
        while ( node is not None ):
            self.stack.append(node)
            node = node.left


def test__binary_search_tree_iterator():
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

    for root in [t1n0, t2n0, t3n0]:
        print("===========================")
        byLevels = binary_tree_level_order(root)
        print(f"Tree by levels: {byLevels}")
        iter = BSTIterator(root)
        print(f"Result: ", end="")
        while ( iter.has_next() ):
            print(f" {iter.get_next()}", end="")
        print()

