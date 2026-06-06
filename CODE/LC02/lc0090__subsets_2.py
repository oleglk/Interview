# lc0090__subsets_2.py
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0090__subsets_2 import *

# RELOAD:
# import importlib; import lc0090__subsets_2; importlib.reload(lc0090__subsets_2); from lc0090__subsets_2 import *

# The idea: first count appearances of each number. Start with one empty subset. Iteratively add 1..cnt of each number to all previously formed subsets.


from collections import defaultdict

def subsets_2(nums: list[int]) -> list[list[int]]:
    subsets = [[]]  # start with one empty subset
    cntAppear = defaultdict(int)
    for num in nums:
        cntAppear[num] += 1

    # add 1..cnt of each appearing number to all previously formed subsets
    for num in cntAppear:  # this way we pick each appearing number once
        numSubsetsSoFar = len(subsets)
        for iSub in range(0, numSubsetsSoFar):
            for cnt in range(1, cntAppear[num]+1):
                subsets += [subsets[iSub] + [num]*cnt]
                            
    return subsets
##


def test__subsets_2():
    tasks = [
        [1,2,2],               # [[],[1],[1,2],[1,2,2],[2],[2,2]]
        [0],                   # [0]
        [1,2,3],               # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    ]
    for nums in tasks:
        print("========================================")
        print(f"Input: {nums}")
        res = subsets_2(nums)
        print(f"Result: {res}")
##
