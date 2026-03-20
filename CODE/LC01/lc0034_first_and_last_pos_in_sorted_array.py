# lc0034_first_and_last_pos_in_sorted_array.py
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0034_first_and_last_pos_in_sorted_array import *

# RELOAD:
# import importlib; import lc0034_first_and_last_pos_in_sorted_array; importlib.reload(lc0034_first_and_last_pos_in_sorted_array); from lc0034_first_and_last_pos_in_sorted_array import *

# The idea: use two modified binary search procedures:
# - find_first() - when element found continues search leftwards
# - find_last()  - when element found continues search rightwards
# See: https://www.geeksforgeeks.org/dsa/find-first-and-last-positions-of-an-element-in-a-sorted-array/


def find_first(nums: list[int], target: int) -> int:
    if ( (nums is None) or (len(nums) == 0) ):
        return -1
    lo = 0;  hi = len(nums) - 1
    first = -1

    while ( lo <= hi ):
        med = (lo + hi) // 2
        if ( target == nums[med] ):
            first = med
            hi = med - 1  # continue searching leftwards
        elif ( target < nums[med] ):
            hi = med - 1  # search in left half
        else:  # target > nums[med]
            lo = med + 1  # search in right half

    return first


def find_last(nums: list[int], target: int) -> int:
    if ( (nums is None) or (len(nums) == 0) ):
        return -1
    lo = 0;  hi = len(nums) - 1
    last = -1

    while ( lo <= hi ):
        med = (lo + hi) // 2
        if ( target == nums[med] ):
            last = med
            lo = med + 1  # continue searching rightwards
        elif ( target < nums[med] ):
            hi = med - 1  # search in left half
        else:  # target > nums[med]
            lo = med + 1  # search in right half

    return last
##


def first_and_last_pos_in_sorted_array(nums: list[int], target: int) -> tuple[int, int]:
    if ( (nums is None) or (len(nums) == 0) ):
        return (-1, -1)
    first = find_first(nums, target)
    last  = find_last(nums, target)
    return (first, last)
##

def test__first_and_last_pos_in_sorted_array():
    tasks = [
        [[1, 3, 5, 5, 5, 5, 67, 123, 125], 5],  # (2, 5)
        [[1, 3, 5, 5, 5, 5, 7, 123, 125], 7],   # (6, 6)
        [[1, 2, 3], 4],                         # (-1, -1)
        [[5,7,7,8,8,10], 8],                    # (3, 4)
    ]
    for nums, target  in tasks:
        print("=======================================")
        print(f"Input: {nums}, target={target}")
        res = first_and_last_pos_in_sorted_array(nums, target)
        print(f"Result: {res}")
##

    
