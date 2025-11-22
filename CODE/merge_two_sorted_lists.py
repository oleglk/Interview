# merge_two_sorted_lists.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from merge_two_sorted_lists import *

# RELOAD:
# import importlib;  import UTILS.lib__linked_list;  importlib.reload(UTILS.lib__linked_list);  from UTILS.lib__linked_list import *;    import merge_two_sorted_lists;  importlib.reload(merge_two_sorted_lists);  from merge_two_sorted_lists import *

from UTILS.lib__linked_list import *


def merge_two_sorted_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    """Assumes ascending order. Returns new merged list.
       (For efficiency consider building reversed-order list by prepending)"""
    l3 = LinkedList()
    curr1 = l1.head
    curr2 = l2.head
    while ( (curr1 is not None) and (curr2 is not None) ):
        if ( curr1.data <= curr2.data ):
            l3.append(curr1.data)
            curr1 = curr1.next
        else:
            l3.append(curr2.data)
            curr2 = curr2.next
    # (only) one input list can contain more elements
    while ( curr1 is not None ):
        l3.append(curr1.data)
        curr1 = curr1.next
    while ( curr2 is not None ):
        l3.append(curr2.data)
        curr2 = curr2.next
    return(l3)


def test__merge_two_sorted_lists():
    l0 = LinkedList()  # empty list
    l1 = LinkedList.from_python_list([1, 3, 5])
    l2 = LinkedList.from_python_list([2])
    l3 = LinkedList.from_python_list([2, 4])
    l4 = LinkedList.from_python_list([2, 4, 6])

    for  iL1, iL2 in ([l0, l0], [l0, l1], [l1, l0], [l1, l2], [l1, l3], [l2, l1], [l2, l4], [l3, l4], [l4, l4]):
        print("==========================")
        print(f"Input 1:");  iL1.display()
        print(f"Input 2:");  iL2.display()
        res = merge_two_sorted_lists(iL1, iL2)
        print(f"Output:");   res.display()

