# lc0206__reverse_linked_list.py
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0206__reverse_linked_list import *

# RELOAD:
# import importlib;    import lc0206__reverse_linked_list;  importlib.reload(lc0206__reverse_linked_list);  from lc0206__reverse_linked_list import *

# The idea: iteratively reverse pointers.
# See: https://www.geeksforgeeks.org/dsa/reverse-a-linked-list/

from UTILS.lib__linked_list import *

# Class Node imported from lib__linked_list.py :
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # Pointer to the next node


def reverse_linked_list(head: Node|None) -> Node|None:
    prev = None
    curr = head
    while ( curr is not None ):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
##


def test__reverse_linked_list():
    tasks = [
        [1,2,3,4,5],
        [1,2],
        []
    ]
    for pyList in tasks:
        print("===========================================")
        print(f"Input: {pyList}")
        lst = LinkedList.from_python_list(pyList)
        newHead = reverse_linked_list(lst.head)
        newLst = LinkedList()  # neede to print the result
        newLst.head = newHead
        print("Result: ", end=None)
        newLst.display();  print("")
##
