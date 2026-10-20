# lc0179__largest_number.py
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0179__largest_number import *

# RELOAD:
# import importlib;    import lc0179__largest_number;  importlib.reload(lc0179__largest_number);  from lc0179__largest_number import *

# The idea: sort with custom comparison function that compares ab with ba. Treat the all-0 case explicitly.
# See: https://algo.monster/liteproblems/179


from functools import cmp_to_key

def largest_number(nums: list[int]) -> str:
    def concat_cmp(a: str, b:str) -> bool:
        """Compares ab and ba to provide descending order sort"""
        ab = a + b;  ba = b + a
        if ( ab < ba ):
            return 1
        elif ( ab > ba ):
            return -1
        else:
            return 0
    ##
    numsStr = [str(x) for x in nums]  # convert all numbers into strings

    numsStr.sort( key = cmp_to_key(concat_cmp) )

    if ( numsStr[0] == '0' ):  # largest is '0', thus all are '0'
        return '0'

    return "".join(numsStr)
##


def test__largest_number():
    tasks = [
        [10,2],         # "210"
        [3,30,34,5,9],  # "9534330"
    ]
    for nums in tasks:
        print("======================================================")
        print(f"Input: {nums}")
        res = largest_number(nums)
        print(f"Result: {res}")
##
