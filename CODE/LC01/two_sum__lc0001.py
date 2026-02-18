# two_sum__lc0001.py
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from two_sum__lc0001 import *

# RELOAD:
# import importlib; import two_sum__lc0001; importlib.reload(two_sum__lc0001); from two_sum__lc0001 import *


# The idea: two passes over the array: 1st pass builds hash of complements {target-arr[i] :: i }, 2nd pass looks up matching complement.


def two_sum(arr: list[int], target: int) -> list[int]:
    # build hash of complements
    complements = {}
    for  i, num1  in enumerate(arr):
        complements[target - num1] = i
    print(f"@@ complements={complements}")
    # look for pair of _distinct_ indices where elements sum to 'target'
    for  i, num2  in enumerate(arr):
        if ( (num2 in complements) and (i != complements[num2]) ):
            return (i, complements[num2])  # found
    return None  # not found


def test__two_sum():
    tasks = [ [[2,7,11,15], 9],  # 0,1
              [[3,2,4],     6],  # 1,2
              [[3,3],       6],  # 0,1
              [[1,2,3,4,5], 8],  # 2,4
              [[10,11,12], 100]  # None
            ]
    for  arr, target in tasks:
        print("=======================================")
        print(f"{arr}, target={target}")
        res = two_sum(arr, target)
        print(f"Result: {res}")

              
              
              
