# lc0086__partition_list.py
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0086__partition_list import *

# RELOAD:
# import importlib; import lc0086__partition_list; importlib.reload(lc0086__partition_list); from lc0086__partition_list import *

# The idea: build separate lists of smaller and larger elements, then concatenate.
# See https://algo.monster/liteproblems/86

from UTILS.lib__linked_list import *


def partition_list(head: Node, x: int) -> Node:
    if ( head is None ):  return None
    dummyLeft = Node(-1)
    dummyRight = Node(-1)
    tailLeft = dummyLeft
    tailRight = dummyRight
    curr = head
    
    # build list of smaller and list of larger
    while ( curr is not None ):
        if ( curr.data < x ):
            tailLeft.next = curr
            tailLeft = tailLeft.next
        else:
            tailRight.next = curr
            tailRight = tailRight.next
        curr = curr.next
    # concatenate the 2 lists and mark the end
    head = dummyLeft.next
    tailLeft.next = dummyRight.next
    tailRight.next = None

    return head
##


def test__partition_list():
    tasks = [
        [[1,4,3,2,5,2], 3],  # [1,2,2, 4,3,5]
        [[2,1], 2],          # [1, 2]
        [[3,1,2], 2],        # [1, 3,2]
    ]
    for pyList, x in tasks:
        print("==========================================")
        linkedList = LinkedList.from_python_list(pyList)
        print(f"Input: {LinkedList.list_to_string(linkedList.head)}, x={x}")
        res = partition_list(linkedList.head, x)
        print(f"Result: {LinkedList.list_to_string(res)}")
##
