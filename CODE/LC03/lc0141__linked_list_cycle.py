# lc0141__linked_list_cycle.py
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0141__linked_list_cycle import *

# RELOAD:
# import importlib;    import lc0141__linked_list_cycle;  importlib.reload(lc0141__linked_list_cycle);  from lc0141__linked_list_cycle import *

# The idea: run fast- and slow pointers on the list. If they ever meet, there's a cycle.
# See: www.hellointerview.com/learn/code/linked-list/linked-list-cycle


from UTILS.lib__linked_list import *

# Class Node imported from lib__linked_list.py :
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # Pointer to the next node


def linked_list_cycle(head: Node) -> bool:
    slow = fast = head
    while ( (fast is not None) and (fast.next is not None) ):
        fast = fast.next.next
        slow = slow.next
        if ( fast == slow ):
            return True
    return False
##


def test__linked_list_cycle():
    l1 = LinkedList.from_python_list([1,2,3,4])
    l2 = LinkedList.from_python_list([1, 2, 2, 2, 2, 2])
    l3 = LinkedList();  l3.append(1);  e2 = l3.append(2);  l3.append_node(e2)
    l4 = LinkedList();  l4.append(1);  l4.append(2);  e3 = l4.append(3);  l4.append(4);  l4.append_node(e3)
    for lst in [l1, l2, l3, l4]:
        print("============")
        lst.display_limited(10)
        hasCycle = linked_list_cycle(lst.head)
        print(f"Has cycle: {hasCycle}")
##
