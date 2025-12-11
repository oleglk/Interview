# search_in_rotated_sorted_array.py - Given a rotated sorted array and target, return index of target or -1.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from search_in_rotated_sorted_array import *

# RELOAD:
# import importlib; import search_in_rotated_sorted_array; importlib.reload(search_in_rotated_sorted_array); from search_in_rotated_sorted_array import *


# The idea: first find the "break" index - that of the smallest element in the array, then regular binary search in one of two sorted halves.

def find_smallest(arr: list) -> int:
    lo = 0
    hi = len(arr) - 1
    if ( len(arr) == 1 ):
        return(0)

    while ( lo <= hi ):
        # one part is sorted, other part contains the smallest element (break)
        if ( arr[lo] <= arr[hi] ):  # <= (not <) accounts for lo==hi
            return(lo)  # the whole subarray sorted - no break, 1st is smallest
        mid = (lo + hi) // 2
        if ( arr[mid] > arr[hi] ):  # right part contains the break, go right
            lo = mid + 1    # #mid excluded, since it's > #hi
        else:                       # left part contains the break, go left
            hi = mid        # #mid included - we didn't compare it to left part

    # hint? return lo, since lo>hi and we have ...max,min,...
    #       while looking for min
    return(lo)  #


def binary_search(arr: list, lo: int, hi: int, target:int) -> int:
    while ( lo <= hi ):
        mid = (lo + hi) // 2
        if ( arr[mid] == target ):
            return(mid)

        if ( arr[mid] < target ):
            lo = mid + 1
        else:
            hi = mid - 1

    return(-1)  # lo > hi and still not found


def search_in_rotated_sorted_array(arr: list, target:int) -> int:
    if (arr is None):  return -1
    n = len(arr)
    
    breakIdx = find_smallest(arr)
    if ( arr[breakIdx] == target ):
        return(breakIdx)
    
    if ( breakIdx == 0 ):  # no rotation, the whole array is sorted
        return(binary_search(arr, 0, n-1, target))  # search in the whole array

    if ( (target >= arr[0]) and (target <= arr[breakIdx-1]) ):
        return(binary_search(arr, 0, breakIdx-1, target))   # search left part
    else:
        return(binary_search(arr, breakIdx+1, n-1, target)) # search right part


def test__search_in_rotated_sorted_array():
    tasks = [ [[0],0],[[0],1],[[3,4,1,2],2],[[4,5,1,2,3],6],[[33,42,72,99],42] ]
    #           0       -2      3             -1              1
    for arr, target in tasks:
        print("==========================")
        print(f"Input: {arr}, target={target}")
        res = search_in_rotated_sorted_array(arr, target)
        print(f"Result: {res}")
