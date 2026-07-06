# lc0092__reverse_linked_list_2.py
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0092__reverse_linked_list_2 import *

# RELOAD:
# import importlib; import lc0092__reverse_linked_list_2; importlib.reload(lc0092__reverse_linked_list_2); from lc0092__reverse_linked_list_2 import *

# The idea: prepend dummy node, find section to reverse, perform reversal, reconnect.
# See https://algo.monster/liteproblems/92

from UTILS.lib__linked_list import *

# 1,2,3,4,5; l=3, r=4 --> 1,2,4,3,5

# Note, left and right are 1...
def reverse_linked_list_2(head: Node, left: int, right: int) -> Node:
    if ( head is None ):  return None
    dummy = Node(-1)
    dummy.next = head
    ## TODO: treat the case of 'right' being too large
    ##       for instance count elements and set right = min(right, n)
    # find begin of the section to reverse - node just before it
    prev = dummy
    for _ in range(0, left-1):
        if ( prev is None ):  return head  # left is too large
        prev = prev.next
    beforeReverse = prev
    firstReversed = prev.next  # will become last reversed
    # 1,2,3,4,5; l=3, r=4 --> beforeReverse=2, firstReversed=3

    # reverse the section
    curr = prev.next  # 1,2,3,4,5; l=3, r=4 --> curr=3
    for _ in range(0, right - left + 1):  # ? why not (right-left) ?
        # 1,2,3,4,5; l=3, r=4 --> cyckle performed for curr=3,4
        tmpNext = curr.next
        curr.next = prev
        prev = curr
        curr = tmpNext
    # prev is the last made pointing backward - now 1st in reversed section
    # curr is the first node after reversed section
    # 1,2,3,4,5; l=3, r=4 --> 1->2, 2->3, 3->2, 4->3, 5->None, prev=4, curr=5

    # reconnect new begin and end of the reversed section
    beforeReverse.next = prev  # 2->4
    firstReversed.next = curr  # 3->5
    # 1,2,3,4,5; l=3, r=4 --> 1->2->4->3->5->None

    return dummy.next
##


def test__reverse_linked_list_2():
    tasks = [
        [[1,2,3,4,5], 2, 4],   # [1,4,3,2,5]
        [[5], 1, 1],           # [5]
        [[1,2,3,4], 1,2],      # [2,1,3,4]
    ]
    for pyList, left, right in tasks:
        print("==========================================")
        linkedList = LinkedList.from_python_list(pyList)
        print(f"Input: {LinkedList.list_to_string(linkedList.head)}, left={left}, right={right}")
        res = reverse_linked_list_2(linkedList.head, left, right)
        print(f"Result: {LinkedList.list_to_string(res)}")
##
