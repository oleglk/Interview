# maximum_subarray.py - Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from maximum_subarray import *

# RELOAD:
# import importlib;    import maximum_subarray;  importlib.reload(maximum_subarray);  from maximum_subarray import *


def maximum_subarray(arr: list) -> int:
    if ( not arr ):
        return(0)
    maxSum = arr[0]
    maxEnding = arr[0]
    for i in range(1, len(arr)):
        # extend prev range or start over
        maxEnding = max(maxEnding + arr[i], arr[i])
        maxSum = max(maxSum, maxEnding)  # memorize the max sum seen so far
    return(maxSum)


def test__maximum_subarray():
    arr1 = [-3]                       # -3
    arr2 = [10, -5, 1]                # 10
    arr3 = [2, 3, -8, 7, -1, 2, 3]    # 11
    arr4 = [1, 2, -1, -1, 100, -100]  # 101
    for arr in [arr1, arr2, arr3, arr4]:
        print("###################")
        print(f"Input: {arr}")
        res = maximum_subarray(arr)
        print(f"Result: {res}")
