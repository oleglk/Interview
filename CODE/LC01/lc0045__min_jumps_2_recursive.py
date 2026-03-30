# lc0045__min_jumps_2_recursive.py
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
#     0 <= j <= nums[i] and
#     i + j < n
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0045__min_jumps_2_recursive import *

# RELOAD:
# import importlib; import lc0045__min_jumps_2_recursive; importlib.reload(lc0045__min_jumps_2_recursive); from lc0045__min_jumps_2_recursive import *

# The idea: recursively try all cells reachable from 1st - with memoization.
# See https://www.geeksforgeeks.org/dsa/minimum-number-of-jumps-to-reach-end-of-a-given-array/

_BIG_NUM = float('inf')

def min_jumps_2_recursive(arr: list[int]) -> int:
    memo = [-1] * len(arr)
    res = min_jumps_2_recurse(arr, 0, memo)
    if ( res == _BIG_NUM ):
        return -1  # last cell cannot be reached
    return res


def min_jumps_2_recurse(arr: list[int], i: int, memo: list[int]) -> int:
    if ( i == len(arr) - 1 ):
        return 0  # end is reached
    if ( memo[i] != -1 ):
        return memo[i]

    res = _BIG_NUM
    for j in range(i+1, min((i+arr[i]+1), len(arr))):
        val = min_jumps_2_recurse(arr, j, memo)
        if ( val != _BIG_NUM ):  # end reachable from #j
            res = min(res, 1+val)  # 1 to reach #j, val to reach end from #j

    if ( res != _BIG_NUM ):
        memo[i] = res
    return res
##


def test__min_jumps_2_recursive():
    tasks = [
        [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],  # 3
        [1, 4, 3, 2, 6, 7],                 # 2
        [0, 10, 20],                        # -1
        [2, 3, 1, 1, 4],                    # 2
        [2, 3, 0, 1, 4],                    # 2
    ]
    for arr in tasks:
        print("===============================")
        print(f"Input: {arr}")
        res = min_jumps_2_recursive(arr)
        print(f"Result: {res}")
##
