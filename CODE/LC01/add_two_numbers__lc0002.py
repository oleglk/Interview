# add_two_numbers__lc0002.py
# Add Two Numbers - You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from add_two_numbers__lc0002 import *

# RELOAD:
# import importlib; import add_two_numbers__lc0002; importlib.reload(add_two_numbers__lc0002); from add_two_numbers__lc0002 import *

# The idea: traverse the 2 lists, add elemments while taking care of carry.

from UTILS.lib__linked_list import *


def add_two_numbers(n1: LinkedList, n2: LinkedList) -> LinkedList:
    if ( (n1 is None) or (n2 is None) ):
        return None
    base = 10;
    d1 = n1.head;  d2 = n2.head
    carry = 0
    res = LinkedList()
    while ( (d1 is not None) or (d2 is not None) ):
        # calculate the current digit
        d = carry
        if ( d1 is not None ):
            d += d1.data;
        if ( d2 is not None ):
            d += d2.data;
        if ( d > base ):
            carry = 1
            d -= base
        else:
            carry = 0
        res.append(d)
        # advance lists' positions
        if ( d1 is not None ):
            d1 = d1.next
        if ( d2 is not None ):
            d2 = d2.next
    return res


def test__add_two_numbers():
    listPairs = [ [[1], [2]],  [[5,5,5], [6,6]], [[3,2,1], [9]] ]
    for n1, n2 in listPairs:
        print("==============")
        l1 = LinkedList.from_python_list(n1)
        l2 = LinkedList.from_python_list(n2)
        print(f"Input: {n1}  +  {n2}")
        res = add_two_numbers(l1, l2)
        print("Result:  ", end="")
        res.display()
