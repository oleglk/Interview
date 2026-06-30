# lc0078__subsets__recursive.py
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Constraint: 1 <= nums.length <= 10

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0078__subsets__recursive import *

# RELOAD:
# import importlib; import lc0078__subsets__recursive; importlib.reload(lc0078__subsets__recursive); from lc0078__subsets__recursive import *

# The idea: include num at current index and recurse for subsequent indices, then exclude num at current index and recurse for subsequent indices.


def subsets_recurse(nums: list[int], currIdx: int, subset: list[int], result: list[list[int]]) -> None:
    # base case: subset completed
    if ( currIdx == len(nums) ):
        result.append(subset[:])  # append a copy of the current subset
        return
    
    # recursive case: num at current index included
    subset.append(nums[currIdx])
    subsets_recurse(nums, currIdx+1, subset, result)
    # recursive case: num at current index excluded
    subset.pop()
    subsets_recurse(nums, currIdx+1, subset, result)

    return
##


def subsets(nums: list[int]) -> list[list[int]]:
    subset = []
    result = []
    subsets_recurse(nums, 0, subset, result)
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
