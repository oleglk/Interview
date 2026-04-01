# CODE/LC01/lc0047__permutations_2.py
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0047__permutations_2 import *

# RELOAD:
# import importlib; import lc0047__permutations_2; importlib.reload(lc0047__permutations_2); from lc0047__permutations_2 import *

# The idea: build permutations recursively while marking used numbers.
# Store the result in a set to avoid repetitions
# See solution for unique numbers in: https://algo.monster/liteproblems/46
# This one is identical except for storing result in a set instead of list.


def permute_2(arr: list[int]) -> set[tuple[int]]:
    currPermutation = [0]*len(arr)
    result = set()
    used = [False]*len(arr)
    permute_recurse_2(arr, 0, used, currPermutation, result)
    return result
##


def permute_recurse_2(arr: list[int], pos: int, used: list[bool], currPermutation: list[int], result: set[tuple[int]]) -> None:
    n = len(arr)
    if ( pos >= n ):  # full permutation is built
        result.add(tuple(currPermutation))
        return

    # put numbers from unused position into #pos, fill the rest recursively
    for i, val  in enumerate(arr):
        if ( not used[i] ):
            used[i] = True  # reserve #i for current permutation
            currPermutation[pos] = val
            # fill positions right of 'pos'
            permute_recurse_2(arr, pos+1, used, currPermutation, result)
            used[i] = False  # free #i for next permutation

    return
##


def test__permute_2():
    tasks = [[1,2,3],  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
             [1,1,2],  # [[1,1,2], [1,2,1], [2,1,1]]
             [1],      # [1]
    ]
    for arr in tasks:
        print ("============================================")
        print(f"Input: {arr}")
        res = permute_2(arr)
        print(f"Result: {res}")
##


