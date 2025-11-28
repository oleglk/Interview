# max_loot_iterative.py - Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount you can rob without robbing adjacent houses.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from max_loot_iterative import *

# RELOAD:
# import importlib;    import max_loot_iterative;  importlib.reload(max_loot_iterative);  from max_loot_iterative import *


def max_loot_iterative(houseVals):
    n = len(houseVals)
    maxLoots = [0] * (n+1)  # 0 houses + n houses, thus n+1
    maxLoots[0] = 0
    maxLoots[1] = houseVals[0]

    for i in range(2, n+1):
        # ? logically must be houseVals[i], but it goes out-of-range at n+1
        maxLoots[i] = max(maxLoots[i-2] + houseVals[i-1],
                          maxLoots[i-1])
    return(maxLoots[n])


def test__max_loot_iterative():
    hVals = [[7], [1,2], [2,5,4], [6,7,1,3,8,2,4], [5,3,4,11,2]]
    # results 7    2      6        19               16
    for hvs in hVals:
        print("=============================")
        print(f"Input: {hvs}")
        res = max_loot_iterative(hvs)
        print(f"Result: {res}")
