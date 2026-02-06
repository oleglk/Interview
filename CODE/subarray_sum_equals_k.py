# subarray_sum_equals_k.py - Count continuous subarrays summing to k using prefix sum map.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from subarray_sum_equals_k import *

# RELOAD:
# import importlib; import subarray_sum_equals_k; importlib.reload(subarray_sum_equals_k); from subarray_sum_equals_k import *


# The idea: maintain running prefix-sum FROM INDEX 0 and a hash of all prefix-sums FROM INDEX 0 mapped to occurence counts. If (running_prefix_sum - k) exist in the hash, increment the result by number of its occurences.
# E.g. subarray_sum = running_prefix_sum - some_prefix_sum_from_hash; if ==k, we found an occurence of continuous subarray summing to k.

from collections import defaultdict

def subarray_sum_equals_k(arr: list[int], k: int) -> int:
    prefixSums = defaultdict(int)  # inexistent keys considered mapped to 0
    currSum = 0
    res = 0
    for x in arr:
        currSum += x
        if ( currSum == k ):
            res += 1  # matching subarray from index 0
        if ( (currSum - k) in prefixSums ):
            # matching subarray(s) starting from indices other than 0 exist(s)
            res += prefixSums[currSum - k]
        prefixSums[currSum] += 1
    return res


def test__subarray_sum_equals_k():
    tasks = [
        [[10, 2, -2, -20, 10],  -10],  # 3
        [[9, 4, 20, 3, 10, 5],  33],   # 2
        [[1, 3, 5],  2]                # 0
        ]
    for arr, k  in tasks:
        print("====================================")
        print(f"Input: {arr}, k={k}")
        res = subarray_sum_equals_k(arr, k)
        print(f"Result: {res}")
