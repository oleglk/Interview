# lc0021__merge_sorted_lists.py
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0021__merge_sorted_lists import *

# RELOAD:
# import importlib; import lc0021__merge_sorted_lists; importlib.reload(lc0021__merge_sorted_lists); from lc0021__merge_sorted_lists import *

# The idea: maintain current pointers into the 2 input lists; move smallest of the 2 elements into the end of the output list.



from UTILS.lib__linked_list import *

def merge_sorted_lists(head1: Node, head2: Node) -> Node:
    dummyHead1 = Node(-1)
    dummyHead1.next = head1
    dummyHead2 = Node(-1)
    dummyHead2.next = head2
    dummyOutHead = Node(-1)
    dummyOutHead.next = None
    ptrToNext1 = dummyHead1
    ptrToNext2 = dummyHead2
    ptrToOut = dummyOutHead

    while ( (ptrToNext1.next is not None) or (ptrToNext2.next is not None) ):
        next1None = (ptrToNext1.next is None)
        next2None = (ptrToNext2.next is None)
        neitherNone = (not next1None) and (not next2None)
        print(f"a1:{ptrToNext1.next.data if not next1None else 'None'}")
        print(f"a2:{ptrToNext2.next.data if not next2None else 'None'}")
        if ( next2None or
             (neitherNone and (ptrToNext1.next.data <= ptrToNext2.next.data))  ):
            # move 1st element from list1 into tail of out-list
            ptrToOut.next = ptrToNext1.next  # append to out-list
            ptrToNext1 = ptrToNext1.next  # delete 1st element from list1
            next1None = (ptrToNext1.next is None)
            print(f"b1:{ptrToNext1.next.data if not next1None else 'None'}")
        elif ( next1None or
             (neitherNone and (ptrToNext1.next.data >  ptrToNext2.next.data))  ):
            # move 1st element from list2 into tail of out-list
            ptrToOut.next = ptrToNext2.next  # append to out-list
            ptrToNext2 = ptrToNext2.next  # delete 1st element from list2
            next2None = (ptrToNext2.next is None)
            print(f"b2:{ptrToNext2.next.data if not next2None else 'None'}")
        else:
            raise Exception("Should not reach here!")
        ptrToOut = ptrToOut.next  # advance out-list pointer
        ptrToOut.next = None      # maintain out-list properly terminated

        next1None = (ptrToNext1.next is None)
        next2None = (ptrToNext2.next is None)
        neitherNone = (not next1None) and (not next2None)
        print(f"c1:{ptrToNext1.next.data if not next1None else 'None'}")
        print(f"c2:{ptrToNext2.next.data if not next2None else 'None'}")
    return dummyOutHead.next
##


def list_to_string(head: Node):
    s = ""
    while ( head is not None ):
        s += str(head.data)
        s += " > "
        head = head.next
    return s
##


def test__merge_sorted_lists():
    tasks = [
        [[1,3,5], [2,4,6]],  # [1,2,3,4,5,6]
        [[], [1,2]],         # [1,2]
        [[1,2], []],         # [1,2]
        [[1,3], [2,4,6]],    # [1,2,3,4,6]
        [[1,3,5], [2,4]]     # [1,2,3,4,5]
    ]
    for pyList1, pyList2  in tasks:
        print("=================================")
        linkedList1 = LinkedList.from_python_list(pyList1)
        linkedList2 = LinkedList.from_python_list(pyList2)
        print(f"Input: {list_to_string(linkedList1.head)},  {list_to_string(linkedList2.head)}")
        newHead = merge_sorted_lists(linkedList1.head, linkedList2.head)
        print(f"Result: {list_to_string(newHead)}")
##
