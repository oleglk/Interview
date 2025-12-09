# longest_increasing_subsequence.py - Given an integer array nums, return the length of the longest strictly increasing subsequence.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from longest_increasing_subsequence import *

# RELOAD:
# import importlib; import longest_increasing_subsequence; importlib.reload(longest_increasing_subsequence); from longest_increasing_subsequence import *

# The idea: (DP) max length of a segment ending on #i: L[i] = max(L[i], [L[j]+1 for all j<i if A[j]<A[i].


def longest_increasing_subsequence(nums: list) -> int:
    n = len(nums)
    if ( n == 0 ):
        return([])
    maxLength = [1]*n
    maxLength[0] = 1

    for i in range(1, n):
        for j in range(0, i):
            if ( nums[j] < nums[i] ):
                maxLength[i] = max(maxLength[i], (maxLength[j]+1))
    return(maxLength[n-1])


def test__longest_increasing_subsequence():
    tasks = [ [1], [3,10,2,1,20], [30,20,10], [2,2,2], [10,20,35,80] ]
    #          1    3              1           1        4
    for nums in tasks:
        print("=================================")
        print(f"Input: {nums}")
        res = longest_increasing_subsequence(nums)
        print(f"Result: {res}")
