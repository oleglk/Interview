# merge_k_sorted_lists.py - Merge k sorted linked lists using min-heap.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from merge_k_sorted_lists import *

# RELOAD:
# import importlib;  import UTILS.lib__linked_list;  importlib.reload(UTILS.lib__linked_list);  from UTILS.lib__linked_list import *;    import merge_k_sorted_lists;  importlib.reload(merge_k_sorted_lists);  from merge_k_sorted_lists import *

# The idea (https://www.geeksforgeeks.org/dsa/merge-k-sorted-linked-lists-set-2-using-min-heap/):  use a min heap to efficiently track the smallest element among all lists at any given time by initially storing the first node from each list in the heap, then repeatedly extracting the minimum element to build the merged list while adding the next node from that same list to maintain the heap's role in finding the next smallest element.


import heapq
from UTILS.lib__linked_list import *

def merge_k_sorted_lists(arr: list[LinkedList]) -> LinkedList:
    resList = LinkedList()
    minHeap = []
    
    # init the heap - insert heads of input lists into the heap
    for i, lst in enumerate(arr):
        if ( lst.head is not None ):
            heapq.heappush(minHeap, (lst.head.data, i, lst.head))

    while ( len(minHeap) > 0 ):
        minData, iList, minNode = heapq.heappop(minHeap)
        # push into the heap the next element of the used list
        if ( minNode.next is not None ):
            heapq.heappush(minHeap, (minNode.next.data, iList, minNode.next))
        # append to the result
        resList.append(minData)

    return resList


def test__merge_k_sorted_lists():
    tasks = [
        [[1,5], [2,4]],
        [[1,3,5,7], [2,4,6,8], [9,10]],
        [[3,4,5], [5,6,7], [7,8,9]]
        ]
    for arr in tasks:
        print("====================================")
        print(f"Input: {arr}")
        linkedLists = []
        for lst in arr:
            linkedList = LinkedList.from_python_list(lst)
            linkedLists.append(linkedList)
        res = merge_k_sorted_lists(linkedLists)
        print(f"Result:")
        res.display()
