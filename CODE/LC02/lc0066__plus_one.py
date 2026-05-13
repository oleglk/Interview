# lc0066__plus_one.py
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0066__plus_one import *

# RELOAD:
# import importlib; import lc0066__plus_one; importlib.reload(lc0066__plus_one); from lc0066__plus_one import *

# The idea: initial +1 is the same as adding carry to least-significant digit. While carry==1 add 1 to existing digits from right to left. If existing digits exhausted and still carry==1, prepend new digit.

def plus_one(digits: list[int]) -> list[int]:
    if ( (digits is None) or (len(digits) == 0) ):
        return 1
    n = len(digits)
    carry = 1  # initial +1 identical to adding carry to least-significant digit
    
    for i in range(n-1, -1, -1):  # process existing digits
        if ( carry == 0 ):
            return digits  # no more additions
        if ( digits[i] < 9 ):
            digits[i] += 1
            carry = 0  # ending carry propagation
        else:  # digits[i] == 9, continuing carry propagation
            digits[i] = 0
            
    # all existing digits are processed
    if ( carry == 1 ):  # need to prepend a new digit (==1)
        digits.insert(0, 1)

    return digits
##


def test__plus_one():
    tasks = [
        [1,2,3],  # [1,2,4]
        [9],      # [1,0]
        [1,3,9],  # [1,4,0]
    ]
    for digits in tasks:
        print("===========================")
        print(f"Input: {digits}")
        res = plus_one(digits)
        print(f"Result: {res}")
##
