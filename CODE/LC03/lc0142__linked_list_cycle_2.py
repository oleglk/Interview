# lc0142__linked_list_cycle_2
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0142__linked_list_cycle_2 import *

# RELOAD:
# import importlib;    import lc0142__linked_list_cycle_2;  importlib.reload(lc0142__linked_list_cycle_2);  from lc0142__linked_list_cycle_2 import *

# The idea: (Phase 1) run fast- and slow pointers on the list. If they ever meet, there's a cycle. (Phase 2) reset one of the pointers to the head. Move both pointers one step at a time; they will meet at the cycle entrance.
# See: https://algomaster.io/learn/dsa/linked-list-cycle-ii

# Proof of phase 2:
#  let a = distance from head to cycle entrance,
#  b = distance from cycle entrance to 1st meeting point,
#  c = distance from 1st meeting point to cycle entrance (b+c = cycle length).
# Slow pointer travels a+b till the 1st meeting point. At the same time fast pointer makes 2*(a+b) steps. From another point of view, fast pointer makes circles in the cycle, thus covers a+b + k*(b+c).
# 2*(a+b) = a+b + k*(b+c)  ==>  a+b = k*(b+c)  ==>  a = (k-1)*(b+c) + b+c - b
# ==> a = (k-1)*(b+c) + c, thus a = c modulo(b+c). E.g. a and c differ by a whole number of cycle lengths.
# E.g. while from-head pointer travels a steps, from-meeting-point pointer travels c and some number of full cycle length steps.


from UTILS.lib__linked_list import *

# Class Node imported from lib__linked_list.py :
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # Pointer to the next node


def linked_list_cycle_2(head: Node) -> Node:
    if ( head is None ):
        return None
    # Phase 1 - check if there is a cycle
    slow = fast = head
    while ( (fast is not None) and (fast.next is not None) ):
        slow = slow.next
        fast = fast.next.next
        if ( fast == slow ):  # cycle found, both pointers are at meeting point
            # Phase 2 - find cycle entrance by moving pointers at the same speed
            slow = head
            while ( fast != slow ):  # eventually will reach fast==slow
                slow = slow.next
                fast = fast.next
            # fast == slow, thus we are at cycle entrance
            return fast
    # fast reached end without seing fast==slow = there's no cycle
    return None
##

                
def test__linked_list_cycle_2():
    l1 = LinkedList.from_python_list([1,2,3,4])
    l2 = LinkedList.from_python_list([1, 2, 2, 2, 2, 2])
    l3 = LinkedList();  l3.append(1);  e2 = l3.append(2);  l3.append_node(e2)
    l4 = LinkedList();  l4.append(1);  l4.append(2);  e3 = l4.append(3);  l4.append(4);  l4.append_node(e3)
    for lst in [l1, l2, l3, l4]:
        print("============")
        lst.display_limited(10)
        cycleStart = linked_list_cycle_2(lst.head)
        print(f"Cycle from: {cycleStart.data if (cycleStart is not None) else "None"}")
##
