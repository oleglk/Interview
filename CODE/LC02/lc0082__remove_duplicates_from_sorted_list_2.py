# lc0082__remove_duplicates_from_sorted_list_2.py
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0082__remove_duplicates_from_sorted_list_2 import *

# RELOAD:
# import importlib; import lc0082__remove_duplicates_from_sorted_list_2; importlib.reload(lc0082__remove_duplicates_from_sorted_list_2); from lc0082__remove_duplicates_from_sorted_list_2 import *

# The idea: 'prev' pointer points at the last unique element, 'curr' pointer runs ahead and skips "runs" of duplicated elements. 'prev'.next reconnected to the 1st element not skipped by 'curr'. Prepend a dummy node for the initial position of 'prev'.
# See https://algo.monster/liteproblems/82

from UTILS.lib__linked_list import *


def remove_duplicates_from_sorted_list_2(head: Node) -> Node:
    if ( head is None ):
        return None
    dummyNode = Node(-1)
    dummyNode.next = head
    prev = dummyNode  # will point at the last unique element
    curr = head  # (head is not None)

    while ( curr is not None ):
        while ( (curr.next is not None) and (curr.data == curr.next.data) ):
            # skip duplicate(s)
            curr = curr.next  # curr points at the last known duplicated element
        # curr points at the last duplicated element; curr is not None

        # check if curr moved (e.g. did skip duplicates)
        if ( prev.next != curr ):  # curr did move to skip duplicates
            prev.next = curr.next  # point at the element after last duplicated
            # prev itself remains pointing at the last non-duplicated element
        else:                      # curr did not move
            # 1st element after prev (pointed to by curr) is not duplicated 
            prev = prev.next  # (same as prev = curr)
            
        curr = curr.next

    return dummyNode.next
##


def list_to_string(head: Node):
    s = ""
    while ( head is not None ):
        s += str(head.data)
        s += " > "
        head = head.next
    return s
##


def test__remove_duplicates_from_sorted_list_2():
    tasks = [
        [1,2,3,3,4,4,5],  # [1,2,5]
        [1,1,1,2,3],      # [2,3]
        [1,2],            # [1,2]
    ]
    for pyList  in tasks:
        print("=================================")
        linkedList = LinkedList.from_python_list(pyList)
        print(f"Input: {list_to_string(linkedList.head)}")
        res = remove_duplicates_from_sorted_list_2(linkedList.head)
        print(f"Result: {list_to_string(res)}")
##
    
