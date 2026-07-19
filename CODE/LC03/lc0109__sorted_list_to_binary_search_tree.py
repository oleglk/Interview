# lc0109__sorted_list_to_binary_search_tree.py
# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0109__sorted_list_to_binary_search_tree import *

# RELOAD:
# import importlib;    import lc0109__sorted_list_to_binary_search_tree;  importlib.reload(lc0109__sorted_list_to_binary_search_tree);  from lc0109__sorted_list_to_binary_search_tree import *


# The idea: recursively build subtrees while taking middle element as the root.
# Find middle element using fast- and slow pointers.
# See https://algomap.io/question-bank/convert-sorted-list-to-binary-search-tree

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"
from UTILS.lib__linked_list import *

# class Node for list-node defined in lib__linked_list.py:
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
####

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
####


def sorted_list_to_binary_search_tree(head: Node|None) -> TreeNode|None:
    if ( head is None ):
        return None

    def find_middle(begin: Node|None, end: Node|None) -> Node|None:
        if ( begin is None ):
            return None
        slow = fast = begin
        while ( (fast is not None) and (fast != end) and \
                (fast.next is not None) and (fast.next != end) ):
            slow = slow.next
            fast = fast.next.next
        return slow
    ##

    def sublist_to_subtree(begin: Node|None, end: Node|None) -> TreeNode|None:
        if ( (begin is None) or (begin == end) ):
            return None
        mid = find_middle(begin, end)
        if ( mid is None ):
            return None

        subtreeRoot = TreeNode(mid.data)
        subtreeRoot.left  = sublist_to_subtree(begin, mid)
        subtreeRoot.right = sublist_to_subtree(mid.next, end)
        return subtreeRoot
    ##

    return sublist_to_subtree(head, None)
##


def test__sorted_list_to_binary_search_tree():
    tasks = [
        [-10,-3,0,5,9],  # [[0],[-10,5],[None,-3,None,9]] or [[0],[-3,9],[-10,None,5,None]]
        [1,3],           # [[3],[1,None]] or [[1],[None,3]]
    ]
    for pyList in tasks:
        print("============================================")
        print(f"Input: {pyList}")
        linkedList = LinkedList.from_python_list(pyList)
        resRoot = sorted_list_to_binary_search_tree(linkedList.head)
        byLevels = binary_tree_level_order(resRoot, includeNone=True)
        print(f"Result by levels: {byLevels}")
##
