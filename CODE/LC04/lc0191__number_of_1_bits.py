# lc0191__number_of_1_bits.py
# Given a positive integer n, write a function that returns the number of set bits in its binary representation.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0191__number_of_1_bits import *

# RELOAD:
# import importlib;    import lc0191__number_of_1_bits;  importlib.reload(lc0191__number_of_1_bits);  from lc0191__number_of_1_bits import *

# The idea: (n-1) has all bits starting from rightmost 1 rightwards reversed vs those of n; (n & (n-1)) nullifies all these bits. Count how many times one can perform (n & (n-1)) until n becomes zero.
# See: https://algo.monster/liteproblems/191


def number_of_1_bits(n: int) -> int:
    count1 = 0
    while ( n != 0 ):
        count1 += 1
        n &= n - 1
    return count1
##


def test__number_of_1_bits():
    tasks = [
        11,          # 3
        128,         # 1
        2147483645,  # 30
    ]
    for n in tasks:
        print("=====================================")
        print(f"Input: {n}")
        res = number_of_1_bits(n)
        print(f"Result: {res}")
##
