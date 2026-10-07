# lc0162__find_peak_element.py
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -inf.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0162__find_peak_element import *

# RELOAD:
# import importlib;    import lc0162__find_peak_element;  importlib.reload(lc0162__find_peak_element);  from lc0162__find_peak_element import *

# The idea: binary search. If nums[mid] < nums[mid+1], there must be peak on the right, otherwise - on the left.
# See: https://medium.com/@roya90/find-peak-element-b847419a7767


def find_peak_element(nums: list[int]) -> int:
    if ( nums is None ):  return None
    if ( len(nums) == 1 ):  return 0
    lo = 0;  hi = len(nums) - 1
    while ( lo < hi ):
        mid = (lo + hi) // 2
        if ( nums[mid] < nums[mid+1] ):  # there must be peak on the right
            lo = mid + 1
        else:                            # there must be peak on the left
            hi = mid
    return lo
##


def test__find_peak_element():
    tasks = [
        [1,2,3,1],        # 2
        [1,2,1,3,5,6,4],  # 1 or 5
    ]
    for nums in tasks:
        print("============================================")
        print(f"Input: {nums}")
        res = find_peak_element(nums)
        print(f"Result: {res}")
##
