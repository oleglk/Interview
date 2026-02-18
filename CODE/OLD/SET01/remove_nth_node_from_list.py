# remove_nth_node_from_list.py - Given the head of a linked list, remove the nth node from the end and return its head.

##### INCORRECT - BUG WHEN DELETING 2ND ELEMENT FROM BEGINNING #############

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from remove_nth_node_from_list import *

# RELOAD:
# import importlib;  import UTILS.lib__linked_list;  importlib.reload(UTILS.lib__linked_list);  from UTILS.lib__linked_list import *;    import remove_nth_node_from_list;  importlib.reload(remove_nth_node_from_list);  from remove_nth_node_from_list import *

from UTILS.lib__linked_list import *

# The idea: run 2 pointers with gap of n nodes; when the front pointer reaches end, trailing pointer is at predecessor of nth node:
## 0123456789, n=3; delete 7
## begin: 0123456789    end: 0123456789
##        t  f                     t  f

def remove_nth_node(lst: LinkedList, n: int) -> Node:
    """Removes nth node from the end of the list. Last node means 'n' = 1."""
    head = lst.head
    if ( n == 0 ):
        return(head)
    trail = head
    front = head
    for i in range(0, n):
        if ( front.next is not None ):
            front = front.next
        elif ( i < (n-1) ):  # not enough nodes - cannot delete nth from end
            print(f"@@ Front stuck at {front.data} - not enough nodes")
            return(head)  # unmodified
    print(f"@@ Gap position: trail={trail.data}, front={front.data}")
    while ( front.next is not None ):
        front = front.next
        trail = trail.next
    # now 'trail'.next is the node to be deleted
    print(f"@@ Del position: trail={trail.data}, front={front.data}")
    if ( trail == head ):
        lst.head = trail.next
    else:
        trail.next = trail.next.next
    return(lst)


def test__remove_nth_node():
    tasks = [ [[0], 1],  [[0,1], 1],  [[0,1,2], 1],  [[0,1,2], 2],
              [[0,1,2,3,4], 2] ]
    for pyList, n in tasks:
        lst = LinkedList.from_python_list(pyList)
        print("==========================")
        print(f"Input: {pyList},  n={n}")
        head = remove_nth_node(lst, n)
        print("Result:  ", end="")
        lst.display()

        
