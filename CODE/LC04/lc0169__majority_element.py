# lc0169__majority_element.py
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than int(n/2) times. You may assume that the majority element always exists in the array.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0169__majority_element import *

# RELOAD:
# import importlib;    import lc0169__majority_element;  importlib.reload(lc0169__majority_element);  from lc0169__majority_element import *

# The idea: view it as num-of-unique-elements teams where fight btw 2 teams eliminates a member from each. Majority team has enough members to fight all the rest. Maintain count and candidate-number. Travers nums. Candidate changes when count = 0. If current number matches candidate, increment count, otherwise decrement count.
# See: https://algo.monster/liteproblems/169

def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if ( count == 0 ):  # pick new candidate
            candidate = num
            count = 1
        elif ( num == candidate ):
            count += 1
        else:  # num != candidate
            count -= 1
    return candidate
##


def test__majority_element():
    tasks = [
        [3,2,3],          # 3
        [2,2,1,1,1,2,2],  # 2
    ]
    for nums in tasks:
        print("=============================================")
        print(f"Input: {nums}")
        res = majority_element(nums)
        print(f"Result: {res}")
##
