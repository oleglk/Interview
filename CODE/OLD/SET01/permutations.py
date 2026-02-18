# permutations.py - Given a collection of distinct integers, return all possible permutations.

# Solution taken from https://www.geeksforgeeks.org/dsa/print-all-possible-permutations-of-an-array-vector-without-duplicates-using-backtracking/


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from permutations import *

# RELOAD:
# import importlib; import permutations; importlib.reload(permutations); from permutations import *


def permute_rec(res, arr, idx):
    if ( idx == len(arr) ):  # done with 'idx'
        res.append(arr[:])   # append shallow copy of the permutation in 'arr'
        return

    # swap each element starting from index 'idx'
    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]   # swap
        permute_rec(res, arr, idx+1)          # permute after index 'idx'
        arr[idx], arr[i] = arr[i], arr[idx]   # swap back ("backtrack")


def permute_array(arr):
    res = []
    permute_rec(res, arr, 0)
    return(res)


def test__permute_array():
    tasks = [ [0], [0,1], [0,1,2], [0,1,2,3] ]
    for arr in tasks:
        print("=============================")
        print(f"Input: {arr}")
        res = permute_array(arr)
        print("Result:")
        print("\n".join([f"  {i}: {x}" for i,x in enumerate(res)]))
