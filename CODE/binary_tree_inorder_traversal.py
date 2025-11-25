# binary_tree_inorder_traversal.py - inorder traversal without recursion

# The idea: use explicit stack.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from binary_tree_inorder_traversal import *

# RELOAD:
# import importlib;    import UTILS.lib__stack;  importlib.reload(UTILS.lib__stack);  from UTILS.lib__stack import *;    import binary_tree_inorder_traversal;  importlib.reload(binary_tree_inorder_traversal);  from binary_tree_inorder_traversal import *

from UTILS.lib__stack import *


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##



def binary_tree_inorder(root: Node):
    result = []
    stack = Stack()
    current = root

    while ( (current is not None) or (not stack.is_empty()) ):
        # descend into left tree
        while ( current is not None ):
            stack.push(current)
            current = current.left
        # process lowermost node held in stack
        node = stack.pop()
        result.append(node.data)
        current = node.right  # arrange for traversing lowermost right subtree

    return(result)


def test__binary_tree_inorder():
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

    for root in [t1n0, t2n0]:
        inorder = binary_tree_inorder(root)
        print(f"Result: {inorder}")
