# lc0088__merge_sorted_arrays.py
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0088__merge_sorted_arrays import *

# RELOAD:
# import importlib; import lc0088__merge_sorted_arrays; importlib.reload(lc0088__merge_sorted_arrays); from lc0088__merge_sorted_arrays import *


# The idea: process from right (max) to left. Use 3 pointers: read1, read2, write1. Stop when nums2 exhausted.
# See https://algo.monster/liteproblems/88


def merge_sorted_arrays(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    read1 = m - 1
    read2 = n - 1
    write1 = m + n - 1

    # keep merging until nums2 exhausts
    while ( read2 >= 0 ):
        if ( (read1 < 0) or (nums2[read2] > nums1[read1]) ):
            nums1[write1] = nums2[read2]
            read2 -= 1
        else:
            nums1[write1] = nums1[read1]
            read1 -= 1
        write1 -= 1
    # when nums2 exhausted first, remaining elements in nums1 are already sorted

    return
##


def test__merge_sorted_arrays():
    tasks = [
        [[1,2,3,0,0,0], 3, [2,5,6], 3],  # [1,2,2,3,5,6]
        [[1], 1, [], 0],                 # [1]
        [[0], 0, [1], 1],                # [1]
        [[4,5,0], 2, [3], 1],            # [3,4,5]
    ]
    for nums1, m, nums2, n  in tasks:
        print("=======================================")
        print(f"Input: {nums1}, m={m}, {nums2}, n={n}")
        merge_sorted_arrays(nums1, m, nums2, n)
        print(f"Result: {nums1}")
##
