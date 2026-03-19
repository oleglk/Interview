# lc0033__search_in_rotated_sorted_array.py
# You are given an integer array nums that was originally sorted in ascending order with all distinct values. However, this array may have been left rotated at some unknown pivot index k (where 1 <= k < nums.length).
# Your task is to search for a given target value in this possibly rotated array and return its index. If the target is not found in the array, return -1.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0033__search_in_rotated_sorted_array import *

# RELOAD:
# import importlib; import lc0033__search_in_rotated_sorted_array; importlib.reload(lc0033__search_in_rotated_sorted_array); from lc0033__search_in_rotated_sorted_array import *

# The idea: since half of the array is always sorted, can use binary search.
# The target sits either in sorted (easy to check) or unsorted half.


def search_in_rotated_sorted_array(nums: list[int], target: int) -> int:
    left = 0;  right = len(nums) - 1
    while ( left <= right ):
        mid = (left + right) // 2
        if ( nums[mid] == target ):
            return mid

        # either left- or right part is sorted
        if ( nums[left] < nums[mid] ):  # left half is sorted
            if ( nums[left] <= target < nums[mid] ):  # target in left half
                right = mid - 1
            else:                                     # target in right half
                left = mid + 1
        else:                           # right half is sorted
            if ( nums[mid] < target <= nums[right] ): # target in right half
                left = mid + 1
            else:                                     # target in left half
                right = mid - 1
    return -1  # not found
##


def test__search_in_rotated_sorted_array():
    tasks = [
        [[4,5,6,7,0,1,2], 0],     # 4
        [[4,5,6,7,0,1,2], 3],     # -1
        [[1], 0],                 # -1
        [[3,4,1,2], 3],           # 0
        [[3,4,1,2], 2],           # 3
        [[1,2,3,4,5], 4],         # 3
    ]
    for nums, target  in tasks:
        print("===============================")
        print(f"Input: {nums}, target={target}")
        res = search_in_rotated_sorted_array(nums, target)
        print(f"Result: {res}")
##
