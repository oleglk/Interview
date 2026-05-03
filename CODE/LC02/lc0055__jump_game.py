# CODE/LC02/lc0055__jump_game.py
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0055__jump_game import *

# RELOAD:
# import importlib; import lc0055__jump_game; importlib.reload(lc0055__jump_game); from lc0055__jump_game import *


# The idea: traverse positions in 'nums' from left to right while maintaining 'maxReach' (rightmost reachable position index). Stop (stuck) if current index > maxReach.
# See https://www.hellointerview.com/learn/code/greedy/jump-game .


def jump_game(nums: list[int]) -> bool:
    if ( nums is None ):
        return True
    maxReach = 0
    for i in range(0, len(nums)):
        if ( i > maxReach ):
            return False  # 'i' unreachable - we are stuck
        maxReach = max(maxReach, i+nums[i])
    return True
##


def test__jump_game():
    tasks = [
        [0],            # True
        [1],            # True
        [1,3,0,1,4],    # True
        [2,2,1,0,5,1,1] # False
    ]
    for nums in tasks:
        print("================================")
        print(f"Input: {nums}")
        res = jump_game(nums)
        print(f"Result: {res}")
##
