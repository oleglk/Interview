# lc0031__next_permutation.py
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
# Given an array of integers nums, find the next permutation of nums.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0031__next_permutation import *

# RELOAD:
# import importlib; import lc0031__next_permutation; importlib.reload(lc0031__next_permutation); from lc0031__next_permutation import *

## 12345 ->()-> 12354 ->(12453)-> 12435
## 123456 ->()-> 123465 ->(123564)-> 123546
## 1247653 ->(1257643)-> 1253467
## 1237654 ->(1247653)-> 1243567
# The idea:
# 1) Find the rightmost digit that's smaller than successor -> nums[i]; all positions to the right of #i form descending suffix. If no such position, i=-1 and whole sequence is descending.
# 2) Find the rightmost digit that's larger than nums[i] -> nums[j]
# 3) Swap nums[i] and nums[j].
# (All positions to the right of #i still form descending suffix, ?)
# 4) Reverse order of i+1...end to convert descending suffix into ascending suffix. 
# See https://algo.monster/liteproblems/31

def next_permutation(nums: list[int]) -> list[int]:
    if ( (nums is None) or (len(nums) == 1) ):
        return nums
    # Find the rightmost element that's smaller than successor -> nums[iPivot]
    iPivot = -1
    for i in range(len(nums)-2, -1, -1):
        if ( nums[i] < nums[i+1] ):
            iPivot = i
            break
    # if pivot not found (iPivot == -1), we have the largest permutation
    # positions to the right of #iPivot form descending suffix

    if ( iPivot >= 0 ):  # not the largest permutation
        # Find the element to swap pivot with (must exist)
        #   - the smallest element that's larger than nums[iPivot]
        #   Since suffix right of iPivot is descending,
        #   it's rightmost element that is larger than nums[iPivot]
        for i in range(len(nums)-1, iPivot, -1):
            if ( nums[i] > nums[iPivot] ):
                iSwap = i
                break
        # swap #iPivot with #iSwap
        tmp = nums[iSwap];  nums[iSwap] = nums[iPivot];  nums[iPivot] = tmp

    # reverse the order after iPivot to get the NEXT larger permutation
    # - it turns descending suffix into ascending
    # - (if iPivot == -1), it turns largest permutation into smallest
    nums[iPivot+1:] = nums[iPivot+1:][::-1]

    return nums
##


def test__next_permutation():
    tasks = [
        [1,2,3,4,5],        # [1,2,3,5,4]
        [5,4,3],            # [3,4,5]
        [1,2,3,5,4],        # [1,2,4,3,5]
        [2,3,1],            # [3,1,2]
        [1,1,5],            # [1,5,1]
    ]
    for nums in tasks:
        print("======================================")
        print(f"Input: {nums}")
        res = next_permutation(nums)
        print(f"Result: {res}")
##
