# lc0026__remove_duplicates_from_sorted_array.py
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0026__remove_duplicates_from_sorted_array import *

# RELOAD:
# import importlib; import lc0026__remove_duplicates_from_sorted_array; importlib.reload(lc0026__remove_duplicates_from_sorted_array); from lc0026__remove_duplicates_from_sorted_array import *

# The idea: use 2 pointers: one is the insertion position for the next unique element, other runs through the whole array in search for next unique element.


# Returns the new array and num of unique elements
def remove_duplicates_from_sorted_array(arr: list[int]) -> tuple[list[int], int]:
    if ( arr is None ):  return (None, 0)
    if (len(arr) == 1 ):
        return (arr, 1)
    # 1st element is unique, so nextUniqInsert starts from 1
    nextUniqInsert = 1
    for i in range(1, len(arr)):
        if ( arr[i] != arr[i-1] ):  # arr[i] is the next unique element
            arr[nextUniqInsert] = arr[i]
            nextUniqInsert += 1
    return (arr, nextUniqInsert)
##

def test__remove_duplicates_from_sorted_array():
    tasks = [
        [1,1,2],                # [1,2,...], 2
        [0,0,1,1,1,2,2,3,3,4],  # [0,1,2,3,4,...], 5
        [1,2]                   # [1,2], 2
    ]
    for arr in tasks:
        print("======================================")
        print(f"Input: {arr}")
        resArr, numUnique = remove_duplicates_from_sorted_array(arr)
        print(f"Result: {resArr}, numUnique={numUnique}")
##
