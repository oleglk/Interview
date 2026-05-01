# lc0053__max_subarray_sum.py
# Given an integer array nums, find the with the largest sum, and return its sum.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0053__max_subarray_sum import *

# RELOAD:
# import importlib; import lc0053__max_subarray_sum; importlib.reload(lc0053__max_subarray_sum); from lc0053__max_subarray_sum import *

# The idea: check best sum ending at each number. If prefix sum <= 0, restart subarray.


def max_subarray_sum(nums: list[int]) -> int:
    if ( nums is None ):  return 0
    if ( len(nums) == 1 ):  return nums[0]
    maxSum = 0
    currSum = nums[0]
    for x in nums[1:]:
        # if prefix-sum > 0, add x to prefix-sum, otherwise restart subarray
        currSum = max(currSum + x, x)
        maxSum = max(maxSum, currSum)
    return maxSum
##


def test__max_subarray_sum():
    tasks = [[-2,1,-3,4,-1,2,1,-5,4],  # 6
             [1],                      # 1
             [5,4,-1,7,8],             # 23
            ]
    for nums in tasks:
        print("======================================")
        print(f"Input: {nums}")
        res = max_subarray_sum(nums)
        print(f"Result: {res}")
##

        
