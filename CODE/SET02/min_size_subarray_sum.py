# min_size_subarray_sum.py - Find the smallest contiguous subarray length with a sum >= target, given an array of positive integers.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from min_size_subarray_sum import *

# RELOAD:
# import importlib; import min_size_subarray_sum; importlib.reload(min_size_subarray_sum); from min_size_subarray_sum import *


# The idea: sliding window; expand right until target reached, shrink from left while target maintained.


def min_size_subarray_sum(arr: list[int], target: int) -> int:
    sum = 0
    left = 0
    theMaxLen = len(arr) + 1  # substitutes infinity
    ans = theMaxLen

    for right in range(0, len(arr)):  # expand rightwards
        sum += arr[right]
        while ( sum >= target ):  # current range is valid
            ans = min(ans, right - left + 1)
            # squeeze from left
            # protection from (left > arr) given in (sum >= target) 
            sum -= arr[left]
            left += 1

    return ans if (ans < theMaxLen) else 0


def test__min_size_subarray_sum():
    tasks = [
        [[2,3,1,2,4,3], 7],      # 2
        [[1,4,4], 4],            # 1
        [[1,1,1,1,1,1,1,1], 11], # 0
        [[1,4,45,6,0,19], 51],   # 2
        [[1,10,5,2,7], 100]      # 0
    ]
    for arr, target in tasks:
        print("=================================")
        print(f"Input: {arr}, target={target}")
        res = min_size_subarray_sum(arr, target)
        print(f"Result: {res}")
