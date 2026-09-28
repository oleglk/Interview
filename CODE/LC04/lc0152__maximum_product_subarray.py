# lc0152__maximum_product_subarray.py
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0152__maximum_product_subarray import *

# RELOAD:
# import importlib;    import lc0152__maximum_product_subarray;  importlib.reload(lc0152__maximum_product_subarray);  from lc0152__maximum_product_subarray import *


# The idea:
# Scan the array left to right while maintaining maxEndingHere, minEndingHere, globalMax. minEndingHere needed since negative number may turn min into max.
# At each element the choice is:
# - extend the max
# - extend the min
# - start over
# See: https://algo.monster/liteproblems/152


def maximum_product_subarray(nums: list[int]) -> int:
    maxEndingHere = minEndingHere = globalMax = nums[0]
    for num in nums[1:]:
        prevMax = maxEndingHere
        prevMin = minEndingHere
        maxEndingHere = max(num, prevMax*num, prevMin*num)
        minEndingHere = min(num, prevMax*num, prevMin*num)
        globalMax = max(globalMax, maxEndingHere)
    return globalMax
##


def test__maximum_product_subarray():
    tasks = [
        [2,3,-2,4],   # 6
        [-2,0,-1],    # 0
        [-2,3,-4],    # 24
    ]
    for nums in tasks:
        print("=======================================")
        print(f"Input: {nums}")
        res = maximum_product_subarray(nums)
        print(f"Result: {res}")
##
