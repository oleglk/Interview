# missing_in_array.py - Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from missing_in_array import *

# RELOAD:
# import importlib; import missing_in_array; importlib.reload(missing_in_array); from missing_in_array import *


# The idea: create a set of numbers that do appear by making values negative in 'nums' at indices whose values are present.


def missing_in_array(nums: list[int]) -> list[int]:
    # build the set of present numbers by negating at correspondent indices
    for x in nums:
        idx = abs(x) - 1
        nums[idx] = -abs(nums[idx])
    # filter [1..n] using the above set
    res = []
    for i, x in enumerate(nums):
        if ( x > 0 ):
            res.append(i+1)
    return res


def test__missing_in_array():
    tasks = [[1],               # []
             [2,2],             # [1]
             [3,1,1],           # [2]
             [1,2,2,5,5],       # [3,4]
             [4,3,2,7,8,2,3,1]  # [5,6]
            ]
    for nums in tasks:
        print("=================================")
        print(f"Input: {nums}")
        res = missing_in_array(nums)
        print(f"Result: {res}")
