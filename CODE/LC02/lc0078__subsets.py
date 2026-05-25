# lc0078__subsets.py
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0078__subsets import *

# RELOAD:
# import importlib; import lc0078__subsets; importlib.reload(lc0078__subsets); from lc0078__subsets import *

# The idea: subsets correspond to 0|1 bits in numbers 0 .. (2^n)-1.


def subsets(nums: list[int]) -> list[int]:
    result: list[list[int]] = []
    n = len(nums)
    for bitField in range(0, 1<<n):
        subset: list[int] = []  # for subset corresponding to current 'bitField'
        for iBit in range(0, n):
            if ( bitField & (1 << iBit) ):
                subset.append(nums[iBit])
        result.append(subset)
    return result
##


def test__subsets():
    tasks = [
        [1,2,3],        # [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
        [2,4],          # [[], [2], [2,4], [4]]
        [0],            # [[], [0]
    ]
    for nums in tasks:
        print("======================================")
        print(f"Input: {nums}")
        res = subsets(nums)
        print(f"Result: {res}")
##

        
