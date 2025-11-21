# reverse_linked_list.py

# RELOAD:
# import importlib;  import LIB.lib__linked_list;  importlib.reload(LIB.lib__linked_list);  from LIB.lib__linked_list import *;    import reverse_linked_list;  importlib.reload(reverse_linked_list);  from reverse_linked_list import *

from LIB.lib__linked_list import *

# |1 2|->|2 3|->|3 4|->|4 5|
def reverse_linked_list(listObj):
    head = listObj.head
    if ( (head is None) or (head.next is None) ):
        return(head)
    prev = None
    curr = head
    while ( curr is not None ):
        next = curr.next
        print(f"curr={curr.data}, next={next.data if (next is not None) else 'None'}")
        curr.next = prev
        print(f"Set curr.next to: {curr.next.data if (curr.next is not None) else 'None'}")
        prev = curr
        curr = next
    listObj.head = prev
    return(head)


def test__reverse_linked_list():
    l1 = LinkedList.from_python_list([1,2,3,4])
    print(f"Original:");  print(l1.display())
    reverse_linked_list(l1)
    print(f"Reversed:");  print(l1.display())
#################################################################################

# test__reverse_linked_list()

