# lc0203__remove_linked_list_elements.py
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0203__remove_linked_list_elements import *

# RELOAD:
# import importlib;    import lc0203__remove_linked_list_elements;  importlib.reload(lc0203__remove_linked_list_elements);  from lc0203__remove_linked_list_elements import *

# The idea: Add dummy head node, then run over list while looking at previous.next.
# See: https://algo.monster/liteproblems/203

from UTILS.lib__linked_list import *

# Class Node imported from lib__linked_list.py :
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # Pointer to the next node


def remove_linked_list_elements(head: Node, val: int) -> Node:
    if ( head is None ):
        return head
    # Add dummy head node
    dummy = Node(val - 1)
    dummy.next = head
    prev = dummy
    # run over list while looking at prev.next
    while ( prev.next is not None ):
        if ( prev.next.data != val ):
            prev = prev.next  # just move forward
        else:
            prev.next = prev.next.next  # remove element
            # don't move to examine new prev.next in the next iteration
    return dummy.next
##


def test__remove_linked_list_elements():
    tasks = [
        [[1,2,6,3,4,5,6], 6],  # [1,2,3,4,5]
        [[], 1],               # []
        [[7,7,7,7], 7],        # []
    ]
    for pyList, val  in tasks:
        print("===========================================")
        print(f"Input: {pyList}, {val}")
        lst = LinkedList.from_python_list(pyList)
        newHead = remove_linked_list_elements(lst.head, val)
        newLst = LinkedList()  # neede to print the result
        newLst.head = newHead
        print("Result: ", end=None)
        newLst.display();  print("")
##
