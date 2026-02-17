# find_duplicate_number_2.py - You are given an array nums containing n + 1 integers, where each integer is in the range [1, n] inclusive. The array has exactly one repeated number that appears more than once. Your task is to find and return this duplicate number.
# Note that the numbers aren't arbitrary.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from find_duplicate_number_2 import *

# RELOAD:
# import importlib; import find_duplicate_number_2; importlib.reload(find_duplicate_number_2); from find_duplicate_number_2 import *

# The idea: without duplicates, count of numbers <=x should be <= x. So if count of numbers <=x is greater than x, duplicated value is <=x, otherwise duplicated value is > x.
# We need the smallest x for which count of numbers <=x is greater than x

# Note that the solution isn't for arbitrary numbers, but only for values in the range [1, n] inclusive.


def find_duplicate_number_2(nums: list[int]) -> int:
    n = len(nums) - 1
    lo = 1;  hi = n  # values, not indices
    minBound = -1  # for smallest x for which count of numbers <=x is > than x
    
    while ( lo <= hi ):
        mid = (lo + hi) // 2
        cnt = sum([1 for x in nums if x <= mid])
        if ( cnt > mid ):
            minBound = mid
            hi = mid - 1  # duplicated val is <=mid   # hi = mid causes inf loop
        else:
            lo = mid + 1  # duplicated val is >mid
    return minBound


def test__find_duplicate_number_2():
    tasks = [[3,1,3,4,2], [1,3,4,2,2]]
    for arr in tasks:
        print("==================================")
        print(f"Input: {arr}")
        res = find_duplicate_number_2(arr)
        print(f"Result: {res}")
