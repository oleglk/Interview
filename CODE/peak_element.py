# peak_element.py - Given an array arr[] where no two adjacent elements are same, find the index of some peak element; an element is considered to be a peak element if it is strictly greater than its adjacent elements.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from peak_element import *

# RELOAD:
# import importlib; import peak_element; importlib.reload(peak_element); from peak_element import *


# The idea:
# Can use binary earch, since:
# - If an element is smaller than it's next element then it is guaranteed that at least one peak element will exist on the right side of this element.
# - Conversely if an element is smaller than it's previous element then it is guaranteed that at least one peak element will exist on the left side of this element.


def peak_element(arr: list) -> int:
    n = len(arr)
    # treat corner cases
    if ( n == 1 ):
        return 0
    if ( arr[0] > arr[1] ):
        return 0
    if ( arr[n-1] > arr[n-2] ):
        return n-1

    # binary search
    lo = 1
    hi = n-2
    while ( lo <= hi ):  # ??? Why this termination condition ???
        mid = (lo + hi) // 2
        if ( (arr[mid-1] < arr[mid]) and (arr[mid] > arr[mid+1]) ):
            return mid
        if ( arr[mid] < arr[mid+1] ): # a peak must exist on the right
            lo = mid + 1
        else:                         # a peak must exist on the left
            hi = mid  # !!! GFG uses hi=mid-1


def test__peak_element():
    tasks = [
        [1, 3, 2],                   # 1
        [1, 2, 4, 5, 7, 8, 3],       # 5
        [10, 20, 15, 2, 23, 90, 80], # 1 or 5
        [1, 2, 3],                   # 2
        [1, 2, 3, 2, 1, 2, 1]        # 2 or 5
    ]
    for arr in tasks:
        print("====================================")
        print(f"Input: {arr}")
        res = peak_element(arr)
        print(f"Result: {res}")
