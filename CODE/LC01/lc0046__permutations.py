# lc0046__permutations.py
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0046__permutations import *

# RELOAD:
# import importlib; import lc0046__permutations; importlib.reload(lc0046__permutations); from lc0046__permutations import *

# The idea: build permutations recursively while marking used numbers.
# See: https://algo.monster/liteproblems/46


def permute(arr: list[int]) -> list[list[int]]:
    n = len(arr)
    currPermutation = [0]*n
    used = [False]*n
    result = []
    permute_recurse(arr, 0, used, currPermutation, result)
    return result
##


def permute_recurse(arr: list[int], pos: int, used: list[int], currPermutation: list[int], result: list[list[int]]):
    n = len(arr)
    if ( pos >= n ):  # finished current permutation
        result.append(currPermutation[:]) # append shallow copy of 'currPermutation'

    # if #j unused, put it into #pos and fill remaining positions recursively
    for j, val in enumerate(arr):
        if ( not used[j] ):
            used[j] = True
            currPermutation[pos] = val
            # fill positions to the right of #pos
            permute_recurse(arr, pos+1, used, currPermutation, result)
            used[j] = False  # make#j available for next permutation
    return
##


def test__permute():
    tasks = [[1,2,3],
             [0,1],
             [1],
    ]
    for arr in tasks:
        print ("============================================")
        print(f"Input: {arr}")
        res = permute(arr)
        print(f"Result: {res}")
##
