# lc0173__binary_search_tree_iterator.py
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#    int next() Moves the pointer to the right, then returns the number at the pointer.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0173__binary_search_tree_iterator import *

# RELOAD:
# import importlib;    import lc0173__binary_search_tree_iterator;  importlib.reload(lc0173__binary_search_tree_iterator);  from lc0173__binary_search_tree_iterator import *

# The idea:
# - maintain stack of nodes
# - constructor pushes left-side path into the stack
# - hasNext() tells if the stack is empty
# - next() returns first node in the stack, but before that pushes into stack left subtree of the returned node's right child
# See: https://www.jointaro.com/interviews/questions/binary-search-tree-iterator/


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node


class BSTIterator:
    def __init__(self, root: Node|None):
        self.nodeStack = []
        self._push_left(root)
    ##


    def _push_left(self, node: Node|None) -> None:
        while ( node is not None ):
            self.nodeStack.append(node)
            node = node.left
    ##


    def hasNext(self) -> bool:
        return ( len(self.nodeStack) > 0 )
    ##


    def next(self) -> int|None:
        if ( not self.hasNext() ):  return None
        nextNode = self.nodeStack.pop()
        # 'nextNode' is the current min node;
        # its successor is the min (leftmost) node in its right subtree
        if ( nextNode.right is not None ):
            self._push_left(nextNode.right)
        return nextNode.data
    ##
####


def test__BSTIterator():
       #   7
       #  / \
       # 3  15
       #   / \
       #  9  20
    t1n0 = Node(7)
    t1n1 = Node(3);  t1n2 = Node(15)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = Node(9);  t1n4 = Node(20)
    t1n2.left = t1n3;  t1n2.right = t1n4

    tasks = [t1n0]
    for root in tasks:
        print("===================================================")
        byLevels = binary_tree_level_order(root, includeNone=True)
        print(f"Input by levels: {byLevels}")
        it = BSTIterator(root)
        print("Result: ", end="")
        while ( it.hasNext() ):
            print(f" {it.next()}", end="")
        print("")
##
