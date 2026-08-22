# lc0143__reorder_list.py
# You are given the head of a singly linked-list. The list can be represented as:
# L0 -> L1 -> ... -> Ln-1 -> Ln
# Reorder the list to be on the following form:
# L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0143__reorder_list import *

# RELOAD:
# import importlib;    import lc0143__reorder_list;  importlib.reload(lc0143__reorder_list);  from lc0143__reorder_list import *

# The idea:
# Phase 1: find the center of the list using fast- and slow pointers, set None terminator at the end of 1st half.
# Phase 2: reverse the 2nd half of the list.
# Phase 3: interleave 1st and 2nd halves of the list.
# See: https://www.geeksforgeeks.org/dsa/rearrange-a-given-linked-list-in-place/

from UTILS.lib__linked_list import *

# Class Node imported from lib__linked_list.py :
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # Pointer to the next node


def reverse_list(head: Node) -> Node:
    # Meaning of the variables: oldPrev -> curr -> oldNext
    oldPrev = None
    curr = head
    oldNext = None
    while ( curr is not None ):
        oldNext = curr.next
        curr.next = oldPrev
        oldPrev = curr
        curr = oldNext
    return oldPrev  # oldPrev stays at last curr that was not None
##


def reorder_list(head: Node) -> Node:
    if ( head is None ):  return None
    # Phase 1: find the center of the list using fast- and slow pointers
    fast = slow = head
    while ( (fast is not None) and (fast.next is not None) ):
        slow = slow.next
        fast = fast.next.next
    node2 = slow.next  # 2nd half of the list
    slow.next = None   # terminate 1st half of the list

    # Phase 2: reverse the 2nd half of the list
    node2 = reverse_list(node2)

    # Phase 3: interleave 1st and 2nd halves of the list
    node1 = head
    dummyHead = Node(0)
    curr = dummyHead
    while ( (node1 is not None) or (node2 is not None) ):
        # take node from the 1st half if available
        if ( node1 is not None ):
            curr.next = node1
            curr = curr.next
            node1 = node1.next
        # take node from the 2nd half if available
        if ( node2 is not None ):
            curr.next = node2
            curr = curr.next
            node2 = node2.next

    return dummyHead.next
##


def print_list(node):
    if node is None:
        return
    while node is not None:
        print(f"{node.data}->", end="")
        node = node.next
##


def test__reorder_list():
    tasks = [
        [1,2,3,4],    # [1,4,2,3]
        [1,2,3,4,5],  # [1,5,2,4,3]
    ]
    for pyList in tasks:
        print("===============================================")
        lst = LinkedList.from_python_list(pyList)
        print("Input: ", end='')
        print_list(lst.head);        print("")
        res = reorder_list(lst.head)
        print("Result: ", end='')
        print_list(res);        print("")
##

