# lc0154__minimum_in_rotated_sorted_array_2.py
# You are given an array that was originally sorted in ascending order, but has been rotated between 1 and n times. A rotation means taking the last element and moving it to the front of the array.
# For example, if you start with [0,1,4,4,5,6,7]:
#    After 1 rotation: [7,0,1,4,4,5,6]
# The array may contain duplicate values. Your task is to find and return the minimum element in this rotated array.


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0154__minimum_in_rotated_sorted_array_2 import *

# RELOAD:
# import importlib;    import lc0154__minimum_in_rotated_sorted_array_2;  importlib.reload(lc0154__minimum_in_rotated_sorted_array_2);  from lc0154__minimum_in_rotated_sorted_array_2 import *

# The idea: binary search while detecting on which side is the "break".
# But if element at middle equals that on right, right -= 1
# See: https://algo.monster/liteproblems/154


def minimum_in_rotated_sorted_array_2(nums: list[int]) -> int:
    left = 0;  right = len(nums) - 1
    while ( left < right ):
        mid = (left + right) // 2
        if ( nums[mid] > nums[right] ):  # break on the right
            left = mid + 1  # min could not be at mid
        elif ( nums[mid] < nums[right] ):  # break on the left
            right = mid     # min could be at mid
        else:  # nums[mid] == nums[right] -> cannot know where break is
            right -= 1  # eliminate one repetition
    return nums[left]
##


def test__minimum_in_rotated_sorted_array_2():
    tasks = [
        [1,3,5],      # 1
        [2,2,2,0,1],  # 0
        [3,4,5,1,2],  # 1
    ]
    for nums in tasks:
        print("======================================")
        print(f"Input: {nums}")
        res = minimum_in_rotated_sorted_array_2(nums)
        print(f"Result = {res}")
##
