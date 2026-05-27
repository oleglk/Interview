# lc0080__remove_duplicates_2.py
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# ...  you must have the result be placed in the first part of the array nums.
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0080__remove_duplicates_2 import *

# RELOAD:
# import importlib; import lc0080__remove_duplicates_2; importlib.reload(lc0080__remove_duplicates_2); from lc0080__remove_duplicates_2 import *

# The idea: move 2 indices left-to-right. 'Take' index (fast) examines the elements, 'put' index (slow) shows the next insertion position. 'take' skips elements that are equal to 2 their successors.
# See https://www.geeksforgeeks.org/dsa/reduce-the-array-such-that-each-element-appears-at-most-2-times/


def remove_duplicates_2(nums: list[int]) -> int:
    if ( len(nums) <= 2 ):
        return len(nums)
    n = len(nums)
    iPut = 0  # element insertion index
    for iTake in range(0, n):
        if ( (iTake < n-2) and (nums[iTake] == nums[iTake+1]) and (nums[iTake] == nums[iTake+2]) ):
            continue  # skip #iTake, since it's duplicated at least 3 times
        # include #iTake into the result
        nums[iPut] = nums[iTake]
        iPut += 1
    return iPut, nums
##


def test__remove_duplicates_2():
    tasks = [
        [1,1,1,2,2,3],        # 5
        [0,0,1,1,1,1,2,3,3],  # 7
        [3,3,3],              # 2
    ]
    for nums in tasks:
        print("====================================")
        print(f"Input: {nums}")
        resK, resNums = remove_duplicates_2(nums)
        print(f"Result: {resK}, nums={nums}")
##

