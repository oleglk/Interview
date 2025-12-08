# subsets.py - Given a set of distinct integers, return all possible subsets (the power set).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from subsets import *

# RELOAD:
# import importlib; import subsets; importlib.reload(subsets); from subsets import *


# The idea: a bit in numbers 0..2^n-1 represents an element - taken or not.


def subsets(arr: list) -> list:
    res = []
    n = len(arr)
    numSubsets = 2**n

    for bitField in range(0, numSubsets):
        subset = []
        for iBit in range(0, n):
            if ( (bitField >> iBit) & 1 ):  # move bit 'iBit' into pos-0 and test
                subset.append(arr[iBit])
        res.append(subset)
    return(res)


def test__subsets():
    tasks = [ [], [0], [0,1], [0,1,2] ]
    for arr in tasks:
        print("=============================")
        print(f"Input: {arr}")
        res = subsets(arr)
        print("Result:")
        print("\n".join([f"  {i}: {x}" for i,x in enumerate(res)]))
