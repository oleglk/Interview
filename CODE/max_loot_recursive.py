# max_loot_recursive.py - Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount you can rob without robbing adjacent houses.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from max_loot_recursive import *

# RELOAD:
# import importlib;    import max_loot_recursive;  importlib.reload(max_loot_recursive);  from max_loot_recursive import *


def max_loot_recursive(houseVals):
    n = len(houseVals)
    maxLootMemo = {}  # to memoize loot-amount per num of houses
    return(_max_loot_recurse(houseVals, n, maxLootMemo))


def _max_loot_recurse(houseVals, n, memo):
    if ( n == 0 ):
        return(0)
    if ( n == 1 ):
        return(houseVals[0])
    # either rob last (#n-1) and skip pre-last (#n-2)
    # or    skip last (#n-1) and rob  pre-last (#n-2)
    if ( n in memo ):
        return(memo[n])

    maxLoot = max(houseVals[n-1] + _max_loot_recurse(houseVals, n-2, memo),
                  _max_loot_recurse(houseVals, n-1, memo))
    memo[n] = maxLoot
    return(maxLoot)


def test__max_loot_recursive():
    hVals = [[7], [1,2], [2,5,4], [6,7,1,3,8,2,4], [5,3,4,11,2]]
    # results 7    2      6        19               16
    for hvs in hVals:
        print("=============================")
        print(f"Input: {hvs}")
        res = max_loot_recursive(hvs)
        print(f"Result: {res}")
