# lc0148__sort_list.py
# Given the head of a linked list, return the list after sorting it in ascending order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0148__sort_list import *

# RELOAD:
# import importlib;    import lc0148__sort_list;  importlib.reload(lc0148__sort_list);  from lc0148__sort_list import *

# The idea: merge sort - 3 phases"
# - split in two halves using fast and slow pointers
# - sort each half recursively
# - merge the two sorted halves
# See: https://algo.monster/liteproblems/148


from UTILS.lib__linked_list import *

# Class Node imported from lib__linked_list.py :
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # Pointer to the next node
####


def merge_sort_list(head: Node|None) -> Node|None:
    if ( (head is None) or (head.next is None) ):
        return head  # base case
    
    # (1) split in two halves using fast and slow pointers
    slow = head
    fast = head.next
    while ( fast and fast.next ):
        fast = fast.next.next
        slow = slow.next
    first = head
    second = slow.next
    slow.next = None
    
    # (2) sort each half recursively
    firstSorted  = merge_sort_list(first)
    secondSorted = merge_sort_list(second)
    
    # (3) merge the two sorted halves
    dummyHead = Node(float('-inf'))
    current = dummyHead
    # while both halves not exhausted, pick minimal-value nodes
    while ( (firstSorted is not None) and (secondSorted is not None) ):
        if ( firstSorted.data <= secondSorted.data ):
            current.next = firstSorted
            firstSorted = firstSorted.next
        else:
            current.next = secondSorted
            secondSorted = secondSorted.next
        current = current.next
    # take the remaining nodes from one half    # if 1st has remainder, take it,
    current.next = firstSorted or secondSorted  # otherwise take 2nd
    
    return dummyHead.next
##


def print_list(node):
    if node is None:
        return
    while node is not None:
        print(f"{node.data}->", end="")
        node = node.next
##


def test__merge_sort_list():
    tasks = [
        [4,3,2,1],   # [1,2,3,4]
        [1,5,2,4,3], # [1,2,3,4,5]
    ]
    for pyList in tasks:
        print("===============================================")
        lst = LinkedList.from_python_list(pyList)
        print("Input: ", end='')
        print_list(lst.head);        print("")
        res = merge_sort_list(lst.head)
        print("Result: ", end='')
        print_list(res);        print("")
##
