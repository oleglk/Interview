# detect_cycle_in_linked_list.py


# RELOAD:
# import importlib;  import LIB.lib__linked_list;  importlib.reload(LIB.lib__linked_list);  from LIB.lib__linked_list import *;    import detect_cycle_in_linked_list;  importlib.reload(detect_cycle_in_linked_list);  from detect_cycle_in_linked_list import *

from LIB.lib__linked_list import *

def detect_cycle(listObj):
    if ( not listObj.head ):
        return(False)
    fast = slow = listObj.head
    while ( (fast is not None) and ((slow != fast) or (slow == listObj.head) ):
        print(f"fast={fast.data if (fast is not None) else 'None'}")
        print(f"slow={slow.data if (slow is not None) else 'None'}")
        fast = fast.next.next if ( fast.next is not None ) else None
        slow = slow.next
    return(fast is not None)
