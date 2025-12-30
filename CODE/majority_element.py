# majority_element.py - Find element appearing more than n/2 times in O(n) time O(1) space.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from majority_element import *

# RELOAD:
# import importlib; import majority_element; importlib.reload(majority_element); from majority_element import *


# The idea:  Boyer-Moore Voting Algorithm:
## If the vote count becomes 0, select the current element as the new candidate and set votes = 1.
## Otherwise, if the current element matches the candidate, increase the vote count; if it does not match, decrease the vote count.


def majority_element(arr: list[int]) -> int:
    if ( (arr is None) or (len(arr) == 0) ):
         return -1
    # phase 1 - find the most frequent element
    count = 0
    candidate = -1
    for el in arr:
        if ( count == 0 ):  # pick curr element as the new candidate
            candidate = el
            count = 1
        elif ( el == candidate ):  # another occurence of the old candidate
            count += 1
        else:  # (el != candidate) - a different element found
            count -= 1

    # phase 2 - count occurences of the most frequent element
    count = 0
    for el in arr:
         if ( el == candidate ):
             count += 1

    if ( count > (len(arr) / 2) ):
        return candidate
    else:
        return -1


def test__majority_element():
    tasks = [
        [1,1,2,1,3,5,1],   # 1
        [7],               # 7
        [2,13],            # -1
        [1,2,1,2,2,2,1]    # 2
        ]
    for arr in tasks:
        print("============================")
        print(f"Input: {arr}")
        res = majority_element(arr)
        print(f"Result: {res}")
