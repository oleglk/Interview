# lc0041__first_missing_positive.py
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0041__first_missing_positive import *

# RELOAD:
# import importlib; import lc0041__first_missing_positive; importlib.reload(lc0041__first_missing_positive); from lc0041__first_missing_positive import *

# The idea:
# Note that 1 <= result <= n+1. If there is a gap in 1..n, the result comes from it. Otherwise assume the result is n+1.
# Mark presense of x by swapping x into position nums[x-1].
# Entry #i not equal to i+1 will mean missing number i+1.
# See https://algo.monster/liteproblems/41 for MUCH MORE DETAILS.


def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    # mark presense of x=nums[i]
    for i in range(0, n):
        # we want position #x-1 to hold x
        # swap until all affected positions are served
        while ( (nums[i] >= 1) and (nums[i] <= n) and
                (nums[nums[i]-1] != nums[i]) ):
            # swap #i with #(x-1)
            targetIdx = nums[i] - 1
            nums[i], nums[targetIdx] = nums[targetIdx], nums[i]

    # check presense; first #i not equal to i+1 means smallest missing number i+1
    for i in range(0, n):
        if ( nums[i] != i+1 ):
            return i+1
    return n+1  # no missing
##


def test__first_missing_positive():
    tasks = [
        [1,2,0],         # 3
        [3,4,-1,1],      # 2
        [7,8,9,11,12],   # 1
    ]
    for nums in tasks:
        print("==========================")
        print(f"Input: {nums}")
        res = first_missing_positive(nums)
        print(f"Result: {res}")
##

