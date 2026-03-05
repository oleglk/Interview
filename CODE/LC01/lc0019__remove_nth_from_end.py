# lc0019__remove_nth_from_end.py
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0019__remove_nth_from_end import *

# RELOAD:
# import importlib; import lc0019__remove_nth_from_end; importlib.reload(lc0019__remove_nth_from_end); from lc0019__remove_nth_from_end import *

# The idea: use 2 pointers - front- and rear spaced by n steps; when front-pointer reaches end of list, rear-pointer is at the nth element from the end.

# dummy>0>1>2>3>4>None, n=2
#       ^   ^
#             ^   ^


from UTILS.lib__linked_list import *


def remove_nth_from_list_end(head: Node, n:int) -> Node:
    if ( head is None ):
        return None
    # prepend dummy node pointing at the head (want '.next' point at node-to-del)
    dummy = Node(-1)
    dummy.next = head
    rear = dummy  # rear pointer starts '.next' pointing at the head
    # init position of the front pointer
    front = dummy  # start with '.next' pointing at the head, move n steps
    for i in range(0, n):
        if ( front.next is None ):
            return head  # no change if not enough elements
        front = front.next
    # move both pointers until 'front.next' is None
    while ( front.next is not None ):
        front = front.next
        rear = rear.next
    # 'rear.next' is the node to be deleted
    if ( rear.next == head ):
        head = head.next
    else:
        rear.next = rear.next.next
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


def test__remove_nth_from_list_end():
    tasks = [
        [[1,2,3,4,5], 2],  # [1,2,3,5]
        [[1], 1],          # []
        [[1,2], 1],        # [1]
        [[1,2], 2]         # [2]
    ]
    for pyList, n  in tasks:
        print("=================================")
        linkedList = LinkedList.from_python_list(pyList)
        print(f"Input: {list_to_string(linkedList.head)}, n={n}")
        newHead = remove_nth_from_list_end(linkedList.head, n)
        print(f"Result: {list_to_string(newHead)}")
##
