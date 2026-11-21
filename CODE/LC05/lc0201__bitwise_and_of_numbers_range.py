# lc0201__bitwise_and_of_numbers_range.py
# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0201__bitwise_and_of_numbers_range import *

# RELOAD:
# import importlib;    import lc0201__bitwise_and_of_numbers_range;  importlib.reload(lc0201__bitwise_and_of_numbers_range);  from lc0201__bitwise_and_of_numbers_range import *

# The idea: all bits that ever flip on the way from 'left' to 'right' become nullified, only prefix made of unchanged bits is preserved. So the answer is common prefix and all 0-s to the right of it.
# See: https://algomap.io/question-bank/bitwise-and-of-numbers-range


def bitwise_and_of_numbers_range(left, right):
    if ( left > right ):
        raise Exception("left > right")
    # right-shift both bounds until equality to find the common prefix
    nShifts = 0
    while ( left < right ):
        left >>= 1
        right >>= 1
        nShifts += 1
    # left = right = common prefix aligned to the right
    # shift left to move the common prefix into the leftmost bits
    left <<= nShifts
    return left
##


def test__bitwise_and_of_numbers_range():
    tasks = [
        [5, 7],          # 4
        [0, 0],          # 0
        [1, 2147483647], # 0
    ]
    for left, right  in tasks:
        print("================================================")
        print(f"Input: [{left}, {right}]")
        res = bitwise_and_of_numbers_range(left, right)
        print(f"Result: {res}")
##
