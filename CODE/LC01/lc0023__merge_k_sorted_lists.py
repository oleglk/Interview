# lc0023__merge_k_sorted_lists.py
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# The idea: use min-heap to continuously choose next smaller element.


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0023__merge_k_sorted_lists import *

# RELOAD:
# import importlib; import lc0023__merge_k_sorted_lists; importlib.reload(lc0023__merge_k_sorted_lists); from lc0023__merge_k_sorted_lists import *


import heapq

from UTILS.lib__linked_list import *

def merge_k_sorted_lists(headsArr: list[Node]) -> Node:
    queue = []
    
    # insert heads into the queue
    for iList, head in enumerate(headsArr):
        if ( head is not None ):
            heapq.heappush(queue, (head.data, iList, head))

    outHead = Node(-1)  # dummy node to point to the output list
    tail = outHead
    
    # continuously insert (move) next min into the output list
    while ( queue ):
        val, iList, minNode = heapq.heappop(queue)
        tail.next = minNode
        tail = tail.next  # == minNode
        # move next from minNode's list into queue
        if ( minNode.next is not None ):
            heapq.heappush(queue, (minNode.next.data, iList, minNode.next))
            headsArr[iList] = headsArr[iList].next #though headsArr not used any more
        
    return outHead.next
##


def list_to_string(head: Node):
    s = ""
    while ( head is not None ):
        s += str(head.data)
        s += " > "
        head = head.next
    return s
##


def test__merge_k_sorted_lists():
    tasks = [
        [[1,3,5,7], [2,4,6,8], [0,9]], # [1,2,3,4,5,6,7,8,9]
        [[1,3,7], [2,4,8], [9,10,11]], # [1,2,3,4,7,8,9,10,11]
        [[1,4,5],[1,3,4],[2,6]],       # [1,1,2,3,4,4,5,6]
        [],                            # []
        [[]],                          # []
    ]
    for pyLists in tasks:
        headsArr = []
        print("==================================")
        print("Inputs: ")
        for pyList in pyLists:
            headsArr.append(LinkedList.from_python_list(pyList).head)
            print(f"  {list_to_string(headsArr[-1])}, ")
        res = merge_k_sorted_lists(headsArr)
        print(f"Result: {list_to_string(res)}")
##

# l1 = LinkedList.from_python_list([0,1]).head;  l2 = LinkedList.from_python_list([2]).head
# res = merge_k_sorted_lists([l1, l2]);  print(f"Result: {list_to_string(res)}")
