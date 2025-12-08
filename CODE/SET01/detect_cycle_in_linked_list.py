# detect_cycle_in_linked_list.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from detect_cycle_in_linked_list import *

# RELOAD:
# import importlib;  import UTILS.lib__linked_list;  importlib.reload(UTILS.lib__linked_list);  from UTILS.lib__linked_list import *;    import detect_cycle_in_linked_list;  importlib.reload(detect_cycle_in_linked_list);  from detect_cycle_in_linked_list import *

from UTILS.lib__linked_list import *

# Runs fast- and slow pointers on a list.
# If they meet, there's a cycle, otherwise the fast pointer reaches end-of-list.
# 
def detect_cycle(listObj: LinkedList) -> bool:
    if ( not listObj.head ):
        return(False)
    fast = slow = listObj.head
    while ( (fast is not None) and ((slow != fast) or (slow == listObj.head)) ):
        print(f"fast={fast.data if (fast is not None) else 'None'}")
        print(f"slow={slow.data if (slow is not None) else 'None'}")
        fast = fast.next.next if ( fast.next is not None ) else None
        slow = slow.next
    return(fast is not None)


def test__detect_cycle():
    l1 = LinkedList.from_python_list([1,2,3,4])
    l2 = LinkedList.from_python_list([1, 2, 2, 2, 2, 2])
    l3 = LinkedList();  l3.append(1);  e2 = l3.append(2);  l3.append_node(e2)
    l4 = LinkedList();  l4.append(1);  l4.append(2);  e3 = l4.append(3);  l4.append(4);  l4.append_node(e3)
    for lst in [l1, l2, l3, l4]:
        print("============")
        lst.display_limited(10)
        hasCycle = detect_cycle(lst)
        print(f"Has cycle: {hasCycle}")
