# max_loot_circular_recursive.py - You are given an array arr[] which represents houses arranged in a circle, where each house has a certain value. A thief aims to maximize the total stolen value without robbing two adjacent houses. Since the houses are in a circle, the first and last houses are also considered adjacent. The task is to determine the maximum amount the thief can steal.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from max_loot_circular_recursive import *

# RELOAD:
# import importlib;    import max_loot_circular_recursive;  importlib.reload(max_loot_circular_recursive);  from max_loot_circular_recursive import *


# The idea: choose between 2 runs of regular house-robber problem - one includes first house but excludes the last, the second - vice-versa.


def max_loot_circular_recursive(houseVals: list) -> int:
    n = len(houseVals)
    if ( n == 1 ):  # will be excluded from both runs- treat separately
        return(houseVals[0])

    # rob 1st, skip last
    memo = [-1]*n  # one-dimensional array - only last idx changes in rec calls
    sum1 = _max_loot_circular_recurse(houseVals, 0, n-2, memo)
    # skip 1st, rob last
    memo = [-1]*n  # one-dimensional array - only last idx changes in rec calls
    sum2 = _max_loot_circular_recurse(houseVals, 1, n-1, memo)
    sum = max(sum1, sum2)
    return(sum)


# Computes sum between #i and #j inclusive
def _max_loot_circular_recurse(houseVals, i, j, memo):
    if ( i > j ):
        return(0)
    if ( i == j ):
        return(houseVals[i])

    if ( memo[j] != -1 ):
        return(memo[j])
    
    # rob last, skip pre-last
    sum1 = houseVals[j] + _max_loot_circular_recurse(houseVals, i, j-2, memo)
    # skip last, allow pre-last
    sum2 = _max_loot_circular_recurse(houseVals, i, j-1, memo)
    sum = max(sum1, sum2)
    memo[j] = sum
    return(sum)


def test__max_loot_circular_recursive():
    hVals = [[], [7], [1,2], [2,5,4], [2, 2, 3, 1, 2],  [1, 2, 3, 1]]
    # results 0,  7    2      5        5                 4
    for hvs in hVals:
        print("=============================")
        print(f"Input: {hvs}")
        res = max_loot_circular_recursive(hvs)
        print(f"Result: {res}")
