# lc0061__rotate_list.py
# Given the head of a linked list, rotate the list to the right by k places.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0061__rotate_list import *

# RELOAD:
# import importlib; import lc0061__rotate_list; importlib.reload(lc0061__rotate_list); from lc0061__rotate_list import *

# 1->2->3->4->5, k=2 ==> 4->5->1->2->3
# The idea:
# - (effective rotation is by k%n positions (rotate by n does nothing))
# - determine the length of the list => n
# - calculate k %= n
# - find the break position using fast- and slow pointers
# - break and reconnect the list

from UTILS.lib__linked_list import *


def rotate_list(head: Node, k: int) -> Node:
    if ( (head is None) or (head.next is None) ):
        return head
    # determine the length of the list => n
    n = 1
    curr = head
    while ( curr.next is not None ):
        n += 1
        curr = curr.next
    k %= n  # k == effective rotation amount
    if ( k == 0 ):
        return head
    # k < n
    # find the break position using fast- and slow pointers
    slow = fast = head
    for _ in range(k):
        fast = fast.next
    while ( fast.next is not None ):
        slow = slow.next
        fast = fast.next
    # slow == new tail,  slow.next == new head,  fast == old tail
    #       s     f
    # 1->2->3->4->5->None
    # break and reconnect the list
    fast.next = head
    head = slow.next
    slow.next = None

    return head
##


def list_to_string(head: Node):
    s = ""
    while ( head is not None ):
        s += str(head.data)
        s += " > "
        head = head.next
    return s
##


def test__rotate_list():
    tasks = [
        [[1,2,3,4,5], 2],  # [4,5,1,2,3]
        [[1,2,3], 1]       # [3,1,2]
    ]
    for pyList, k  in tasks:
        print("=================================")
        linkedList = LinkedList.from_python_list(pyList)
        print(f"Input: {list_to_string(linkedList.head)}, k={k}")
        res = rotate_list(linkedList.head, k)
        print(f"Result: {list_to_string(res)}")
##


