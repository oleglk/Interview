# lc0039__combination_sum_1.py
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the of at least one of the chosen numbers is different.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0039__combination_sum_1 import *

# RELOAD:
# import importlib; import lc0039__combination_sum_1; importlib.reload(lc0039__combination_sum_1); from lc0039__combination_sum_1 import *

# The idea: recursively try option with current element and without it.

def combination_sum_1_recurse(arr: list[int], currIdx: int, currCombo: list[int],
                              res: list[list[int]], remains: int) -> None:
    # base case 1: valid combo found
    if ( remains == 0 ):
        res.append(currCombo)
        print(f"@@ Appended ({currCombo}) to obtain ({res})")
        return
    # base case 2: index out of range
    if ( currIdx >= len(arr) ):
        return
    # base case 3: target sum exhausted
    if ( remains < 0 ):
        return

    # try option of using current element
    # 'curIdx' not incremented to allow using current element again
    currCombo.append(arr[currIdx])
    combination_sum_1_recurse(arr, currIdx, currCombo, res,
                              remains - arr[currIdx])
    # try option of not using current element
    currCombo.pop()  # restore combo without current element
    combination_sum_1_recurse(arr, currIdx+1, currCombo, res,
                              remains)

    return
##


def combination_sum_1(arr: list[int], target: int) -> list[list[int]]:
    res = []
    combination_sum_1_recurse(arr, 0, [], res, target)
    return res
##


def test__combination_sum_1():
    tasks = [
        [[2,3,6,7], 7],         # [[2,2,3],[7]]
        [[2,3,5], 8],           # [[2,2,2,2],[2,3,3],[3,5]]
        [[2], 1],               # []
    ]
    for arr, target  in tasks:
        print("====================================")
        print(f"Input: {arr}, target={target}")
        res = combination_sum_1(arr, target)
        print(f"Result: {res}")
##

                              
