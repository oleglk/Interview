# lc0024__swap_nodes_in_pairs.py
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0024__swap_nodes_in_pairs import *

# RELOAD:
# import importlib; import lc0024__swap_nodes_in_pairs; importlib.reload(lc0024__swap_nodes_in_pairs); from lc0024__swap_nodes_in_pairs import *

# The idea: use (initially dummy) pointer at 1st of two consequent elements; swap then move the pointer 2 elements.


from UTILS.lib__linked_list import *


def swap_nodes_in_pairs(head: Node) -> Node:
    dummy = Node(-1)
    dummy.next = head  # init for swapping first two elements
    currPtr = dummy
    while ( (currPtr.next is not None) and (currPtr.next.next is not None) ):
        p1 = currPtr.next
        p2 = currPtr.next.next
        # swap p1 and p2
        p1.next = p2.next
        p2.next = p1
        currPtr.next = p2  # point before the next pair to be swapped
        # move pointer-at-next-pair forward 2 elements
        currPtr = p1
    return dummy.next
##


def test__swap_nodes_in_pairs():
    tasks = [
        [1,2,3,4],       # [2,1,4,3]
        [],              # []
        [1],             # [1]
        [1,2,3],         # [2,1,3]
    ]
    for pyList in tasks:
        print("=================================")
        linkedList = LinkedList.from_python_list(pyList)
        print(f"Input: {LinkedList.list_to_string(linkedList.head)}")
        newHead = swap_nodes_in_pairs(linkedList.head)
        print(f"Result: {LinkedList.list_to_string(newHead)}")
##

    
