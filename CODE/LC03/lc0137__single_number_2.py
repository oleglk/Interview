# lc0137__single_number_2.py
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# -2^31 <= nums[i] <= 2^31 - 1

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0137__single_number_2 import *

# RELOAD:
# import importlib;    import lc0137__single_number_2;  importlib.reload(lc0137__single_number_2);  from lc0137__single_number_2 import *

# The idea: work bit by bit. If sum of a particular bit is divisible by 3, single number has it as 0, otherwise as 1. Compose the result of individual bits. Unclear trick for setting bit #31.
# See: https://algo.monster/liteproblems/137


def single_number_2(nums: list[int]) -> int:
    result = 0
    for bitIdx in range(0, 32):
        bitSum = 0
        for num in nums:
            bitVal = (num >> bitIdx) & 0x1  # value of the bit in currrent number
            bitSum += bitVal
        if ( (bitSum % 3) != 0 ):
            # the bit == 1 in the single number; set it in the result
            if ( bitIdx != 31 ):  # a normal bit
                result |= (1 << bitIdx)
            else:                # sign bit, UNCLEAR
                result -= (1 << bitIdx)

    return result
##


def test__single_number_2():
    tasks = [
        [2,2,3,2],        # 3
        [0,1,0,1,0,1,99], # 99
    ]
    for nums in tasks:
        print("==================================================")
        print(f"Input: {nums}")
        res = single_number_2(nums)
        print(f"Result: {res}")
##
