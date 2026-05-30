# lc0083__remove_duplicates_from_sorted_list.py
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0083__remove_duplicates_from_sorted_list import *

# RELOAD:
# import importlib; import lc0083__remove_duplicates_from_sorted_list; importlib.reload(lc0083__remove_duplicates_from_sorted_list); from lc0083__remove_duplicates_from_sorted_list import *

# The idea: traverse the list with 'curr' pointer. Whenever current element equals the next one, remove the latter.
# See https://algo.monster/liteproblems/83

from UTILS.lib__linked_list import *


def remove_duplicates_from_sorted_list(head: Node) -> Node:
    if ( head is None ):
        return None
    curr = head
    while ( (curr is not None) and (curr.next is not None) ):
        if ( curr.data == curr.next.data ):
            curr.next = curr.next.next
            # don't advance 'curr' - next time compare old 'curr' with new next
        else:
            curr = curr.next
    return head  # 1st element is never removed
##


def test__remove_duplicates_from_sorted_list():
    tasks = [
        [1,2,3,3,4,4,5],  # [1,2,3,4,5]
        [1,1,1,2,3],      # [1,2,3]
        [1,2],            # [1,2]
        [1,1,2,3,3],      # [1,2,3]
    ]
    for pyList  in tasks:
        print("=================================")
        linkedList = LinkedList.from_python_list(pyList)
        print(f"Input: {LinkedList.list_to_string(linkedList.head)}")
        res = remove_duplicates_from_sorted_list(linkedList.head)
        print(f"Result: {LinkedList.list_to_string(res)}")
##
