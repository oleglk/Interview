# lc0153__minimum_in_rotated_sorted_array.py
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#   [4,5,6,7,0,1,2] if it was rotated 4 times.
#   [0,1,2,4,5,6,7] if it was rotated 7 times.
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0153__minimum_in_rotated_sorted_array import *

# RELOAD:
# import importlib;    import lc0153__minimum_in_rotated_sorted_array;  importlib.reload(lc0153__minimum_in_rotated_sorted_array);  from lc0153__minimum_in_rotated_sorted_array import *

# The idea: binary search while detecting on which side is the "break".
# See: https://www.geeksforgeeks.org/dsa/find-minimum-element-in-a-sorted-and-rotated-array/


def minimum_in_rotated_sorted_array(nums: list[int]) -> int:
    left = 0;  right = len(nums) - 1
    while ( left < right ):
        mid = (left + right) // 2
        if ( nums[mid] > nums[right] ):  # break on the right of 'mid'
            left = mid + 1
        else:                            # break on the left of 'mid' or at it
            right = mid
    return nums[left]
##


def test__minimum_in_rotated_sorted_array():
    tasks = [
        [3,4,5,1,2],      # 1
        [4,5,6,7,0,1,2],  # 0
        [11,13,15,17],    # 11
    ]
    for nums in tasks:
        print("=================================")
        print(f"Input: {nums}")
        res = minimum_in_rotated_sorted_array(nums)
        print(f"Result: {res}")
##
