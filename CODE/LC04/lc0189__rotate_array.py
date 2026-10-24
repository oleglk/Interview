# lc0189__rotate_array.py
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0189__rotate_array import *

# RELOAD:
# import importlib;    import lc0189__rotate_array;  importlib.reload(lc0189__rotate_array);  from lc0189__rotate_array import *

# The idea: first reverse the whole array, then reverse the two split parts separately.
# See: https://algo.monster/liteproblems/189


def rotate_array(nums: list[int], k: int) -> None:
    def reverse_range(left: int, right: int) -> None:
        nonlocal nums
        while ( left < right ):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    ##
    
    n = len(nums)
    k = k % n  # rotation by n is identity transform
    reverse_range(0, n-1)  # reverse the whole array
    reverse_range(0, k-1)  # reverse the front part
    reverse_range(k, n-1)  # reverse the rear part
##


def test__rotate_array():
    tasks = [
        [[1,2,3,4,5,6,7], 3],   # [5,6,7,1,2,3,4]
        [[-1,-100,3,99], 2],    # [3,99,-1,-100]
    ]
    for  nums, k  in tasks:
        print("================================================")
        print(f"Input: {nums}, {k}")
        rotate_array(nums, k)
        print(f"Result: {nums}")
##
