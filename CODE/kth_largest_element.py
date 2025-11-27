# kth_largest_element.py - Find the kth largest element in an unsorted array.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from kth_largest_element import *

# RELOAD:
# import importlib;    import kth_largest_element;  importlib.reload(kth_largest_element);  from kth_largest_element import *

import heapq  # min-heap

# The idea: push elements into min-heap; when heap-size == k+1, pop min element from the heap. After the whole array is pushed the heap must contain k largest elements; minimal element is kth largest.

def kth_largest_element(arr: list, k: int) -> int:
    if ( len(arr) < k ):
        raise Exception("Array too small")
    minHeap = []
    for x in arr:
        heapq.heappush(minHeap, x)
        if ( len(minHeap) == k+1 ):
            m = heapq.heappop(minHeap) # discard curr smallest, leave k larger
            #print(f"@@ Dropped {m}, remained {minHeap}")
    # now minimal element in the heap is kth largest in 'arr'
    el = heapq.heappop(minHeap)
    return(el)


def test__kth_largest_element():
    arrAndKs = [ [[1,2,3], 3], [[1,3,2,5,4], 2], [[3], 1], [[4,3,2,1], 3] ]
    for arr, k in arrAndKs:
        print("================================")
        print(f"arr={arr}, k={k}")
        res = kth_largest_element(arr, k)
        print(f"Result: {res}")
