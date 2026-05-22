# lc0075__sort_colors.py
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0075__sort_colors import *

# RELOAD:
# import importlib; import lc0075__sort_colors; importlib.reload(lc0075__sort_colors); from lc0075__sort_colors import *

# The idea: indices after0 and before2 mark boundaries red-white and white-blue. Move index curr through the array and swap object at curr with either that of after0 or before2 depending on the color at curr; advance boundary index. I color is 1, just move further. Finish when curr > before2.
# See https://www.geeksforgeeks.org/dsa/sort-an-array-of-0s-1s-and-2s/


def sort_colors(nums: list[int]) -> list[int]:
    if ( len(nums) <= 1 ):
        return nums
    after0 = curr = 0;  before2 = len(nums) - 1
    while ( curr <= before2 ):
        if ( nums[curr] == 0 ):
            nums[curr], nums[after0] = nums[after0], nums[curr]
            after0 += 1
            curr += 1  # can advance since we leave 0 or 1 behind curr
            # don't advance curr since nums[curr] isn't yet checked
        elif ( nums[curr] == 2 ):
            nums[curr], nums[before2] = nums[before2], nums[curr]
            before2 -= 1
            # don't advance curr since nums[curr] isn't yet checked
        else: # nums[curr] == 1
            curr += 1
    return nums
##


def test__sort_colors():
    tasks = [
        [2,0,2,1,1,0],              # [0,0,1,1,2,2]
        [2,0,1],                    # [0,1,2]
        [0,1,2,0,1,2],              # [0, 0, 1, 1, 2, 2]
        [0,1,1,0,1,2,1,2,0,0,0,1],  # [0,0,0,0,0,1,1,1,1,1,2,2]
    ]
    for nums in tasks:
        print("======================================")
        print(f"Input: {nums}")
        res = sort_colors(nums)
        print(f"Result: {res}")
##
