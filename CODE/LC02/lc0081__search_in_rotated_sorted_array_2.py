# lc0081__search_in_rotated_sorted_array_2.py
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0081__search_in_rotated_sorted_array_2 import *

# RELOAD:
# import importlib; import lc0081__search_in_rotated_sorted_array_2; importlib.reload(lc0081__search_in_rotated_sorted_array_2); from lc0081__search_in_rotated_sorted_array_2 import *

# The idea: modified binary search - detect which part is sorted and take  decisions based on the sorted part.
# !!! Unclear: where to use mid versus mid+-1 !!!

def search_in_rotated_sorted_array_2(nums: list[int], target: int) -> bool:
    if ( not nums ):  return False
    n = len(nums)
    left = 0;  right = n - 1

    while ( left < right ):
        mid = (left + right) // 2
        # detect which part is sorted
        if ( nums[mid] < nums[right] ):   # break not on the right
            # right part is sorted
            if ( nums[mid] < target <= nums[right] ):   # target on the right
                left = mid + 1
            else:                                       # target on the left
                right = mid
        elif ( nums[mid] > nums[right] ): # break on the right
            # left part is sorted
            if ( nums[left] <= target <= nums[mid] ):   # target on the left
                right = mid
            else:                                       # target on the right
                left = mid + 1
        else:  # nums[mid] == nums[right] - #mid duplicated
            right -= 1  # slow but safe
    return (nums[left] == target)
##


def test__search_in_rotated_sorted_array_2():
    tasks = [
        [[2,5,6,0,0,1,2], 0],        # true
        [[2,5,6,0,0,1,2], 3],        # false
        [[4,5,6,6,7,0,1,2,4,4], 2],  # true
        [[4,5,6,6,7,0,1,2,4,4], 8],  # false
        [[4,5,6,6,7,0,1,2,4,4], 4],  # true
    ]
    for nums, target  in tasks:
        print("======================================")
        print(f"Input: {nums}, target = {target}")
        res = search_in_rotated_sorted_array_2(nums, target)
        print(f"Result: {res}")
##
