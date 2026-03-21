# lc0035__search_insert_pos_in_sorted_array.py
# Given a 0 based sorted array arr[] of distinct integers and an integer k, find the index of k if it is present. If not, return the index where k should be inserted to maintain the sorted order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0035__search_insert_pos_in_sorted_array import *

# RELOAD:
# import importlib; import lc0035__search_insert_pos_in_sorted_array; importlib.reload(lc0035__search_insert_pos_in_sorted_array); from lc0035__search_insert_pos_in_sorted_array import *

# The idea: run regular binary search. At the end, if element not found, left index stays at the insertion position, since it points at the first element no smaller than target.


def search_insert_pos_in_sorted_array(arr: list[int], target: int) -> int:
    if ( arr is None ):
        return -1
    if ( len(arr) == 0 ):
        return 0
    lo = 0;  hi = len(arr) - 1

    while ( lo <= hi ):
        mid = (lo + hi) // 2
        if ( target == arr[mid] ):
            return mid
        if ( target < arr[mid] ):
            hi = mid - 1  # continue searching in the left half
        else:  # target > arr[mid]
            lo = mid + 1  # continue searching in the right half
    # upon finishing the loop, arr[lo] is the leftmost element >= target
    return lo
##


def test__search_insert_pos_in_sorted_array():
    tasks = [
        [[1, 3, 5, 6], 5],    # 2
        [[1, 3, 5, 6], 2],    # 1
        [[1, 3, 5, 6], 7],    # 4
    ]
    for  arr, target  in tasks:
        print("================================")
        print(f"Input: {arr}, target={target}")
        res = search_insert_pos_in_sorted_array(arr, target)
        print(f"Result: {res}")
##

        
