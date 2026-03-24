# lc0040__combination_sum_2.py
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0040__combination_sum_2 import *

# RELOAD:
# import importlib; import lc0040__combination_sum_2; importlib.reload(lc0040__combination_sum_2); from lc0040__combination_sum_2 import *

# The idea: recursively try option with current element and without it.

def combination_sum_2_recurse(arr: list[int], currIdx: int, currCombo: list[int],
                              res: set[tuple[int]], remains: int) -> None:
    # base case 1: valid combo found
    if ( remains == 0 ):
        res.add(tuple(sorted(currCombo))) # list constructor forces copy of 'currCombo'
        #print(f"@@ Appended ({currCombo}) to obtain ({res})")
        return
    # base case 2: index out of range
    if ( currIdx >= len(arr) ):
        return
    # base case 3: target sum exhausted
    if ( remains < 0 ):
        return

    # try option of using current element
    # 'currIdx' is incremented to avoid using current element again
    currCombo.append(arr[currIdx])
    combination_sum_2_recurse(arr, currIdx+1, currCombo, res,
                              remains - arr[currIdx])
    # try option of not using current element
    currCombo.pop()  # restore combo without current element
    combination_sum_2_recurse(arr, currIdx+1, currCombo, res,
                              remains)

    return
##


def combination_sum_2(arr: list[int], target: int) -> list[list[int]]:
    res = set()
    combination_sum_2_recurse(arr, 0, [], res, target)
    return res
##


def test__combination_sum_2():
    tasks = [
        [[10,1,2,7,6,1,5], 8],   # [[1,1,6], [1,2,5], [1,7], [2,6]]
        [[2,5,2,1,2], 5],        # [[1,2,2], [5]]
    ]
    for arr, target  in tasks:
        print("====================================")
        print(f"Input: {arr}, target={target}")
        res = combination_sum_2(arr, target)
        print(f"Result: {res}")
##
