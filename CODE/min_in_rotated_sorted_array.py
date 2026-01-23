# min_in_rotated_sorted_array.py - Given a sorted array of distinct elements arr[] of size n that is rotated at some unknown point, the task is to find the minimum element in it.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from min_in_rotated_sorted_array import *

# RELOAD:
# import importlib; import min_in_rotated_sorted_array; importlib.reload(min_in_rotated_sorted_array); from min_in_rotated_sorted_array import *


# The idea: use binary search.
# a) If arr[mid] > arr[high] //5 6 7 8 1 2 3 4//, left half is sorted - continue searching in the right part => low = mid + 1.
# b) If arr[mid] <= arr[high] //8 1 2 3 4 5 6 7//6 7 8 1 2 3 4 5//, right part is sorted - continue searching in the left part => high = mid.
# Termination condition: if low < high, the current subarray is sorted, and low is the minimum.

from typing import Protocol, TypeVar, Any

#ElemType = TypeVar("ElemType", bound="Comparable")

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    

def min_in_rotated_sorted_array(arr: list[Comparable]) -> Comparable:
    if (len(arr) == 1): return arr[0]
    lo = 0
    hi = len(arr) - 1

    while arr[lo] > arr[hi]:
        mid = (lo + hi) // 2
        if ( arr[mid] > arr[hi] ):  # left half is sorted, search in right
            lo = mid + 1
        else:                       # right part is sorted, search in left
            hi = mid
            
    # arr[lo] < arr[hi] - the whole subarray is sorted and lo is the min
    return arr[lo]


def test__min_in_rotated_sorted_array():
    tasks = [
        [5, 6, 1, 2, 3, 4],      # 1
        [3, 1, 2],               # 1
        [4, 2, 3],               # 2
        [5, 6, 7, 8, 1, 2, 3, 4],# 1
        [7, 1, 2, 3, 4, 5, 6],   # 1
        [5, 6, 7, 1, 2, 3, 4],   # 1
    ]
    for arr in tasks:
        print("===========================")
        print(f"Input: {arr}")
        res = min_in_rotated_sorted_array(arr)
        print(f"Result: {res}")
