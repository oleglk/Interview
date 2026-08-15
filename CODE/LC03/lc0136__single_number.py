# lc0136__single_number.py
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0136__single_number import *

# RELOAD:
# import importlib;    import lc0136__single_number;  importlib.reload(lc0136__single_number);  from lc0136__single_number import *

# The idea: XOR all numbers gives the single one:
# - (a XOR a) == 0, thus all duplicated numbers get eliminated
# - (a XOR 0) == a, thus the single number will result.
# See: https://algo.monster/liteproblems/136

from functools import reduce

def single_number(nums: list[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)
##


def test__single_number():
    tasks = [
        [2,2,1],      # 1
        [4,1,2,1,2],  # 4
        [1],          # 1
    ]
    for nums in tasks:
        print("================================================")
        print(f"Input: {nums}")
        res = single_number(nums)
        print(f"Result: {res}")
##
