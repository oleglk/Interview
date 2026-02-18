# add_two_numbers.py - You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order. Add the two numbers and return the sum as a linked list.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from add_two_numbers import *

# RELOAD:
# import importlib;  import UTILS.lib__linked_list;  importlib.reload(UTILS.lib__linked_list);  from UTILS.lib__linked_list import *;    import add_two_numbers;  importlib.reload(add_two_numbers);  from add_two_numbers import *

from UTILS.lib__linked_list import *


# The idea: traverse the 2 lists, add elemments while taking care of carry.


def add_two_numbers(l1: Node, l2: Node) -> LinkedList:
    res = LinkedList()
    base = 10
    carry = 0
    # add elements or zeroes (where one list have no digits)
    while ( (l1 is not None) or (l2 is not None) ):
        d1 = l1.data if (l1 is not None) else 0
        d2 = l2.data if (l2 is not None) else 0
        r = d1 + d2 + carry  # current resulting digit
        if ( r >= base ):
            carry = 1
            r -= base
        else:
            carry = 0
        res.append(r)
        l1 = l1.next if (l1 is not None) else None
        l2 = l2.next if (l2 is not None) else None
    # both lists are finished, but carry may remain
    if ( carry != 0 ):
        res.append(1)
    return(res)


def test__add_two_numbers():
    listPairs = [ [[1], [2]],  [[5,5,5], [6,6]], [[3,2,1], [9]] ]
    for n1, n2 in listPairs:
        print("==============")
        l1 = LinkedList.from_python_list(n1)
        l2 = LinkedList.from_python_list(n2)
        print(f"Input: {n1}  +  {n2}")
        res = add_two_numbers(l1.head, l2.head)
        print("Result:  ", end="")
        res.display()
