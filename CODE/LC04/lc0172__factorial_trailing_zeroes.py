# lc0172__factorial_trailing_zeroes.py
# Given an integer n, return the number of trailing zeroes in n! .

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0172__factorial_trailing_zeroes import *

# RELOAD:
# import importlib;    import lc0172__factorial_trailing_zeroes;  importlib.reload(lc0172__factorial_trailing_zeroes);  from lc0172__factorial_trailing_zeroes import *

# The idea: trailing zeroes are created by pairs of 5 and 2, while there always are more 2s than 5s. Thus number of trailing zeroes equals to number of 5s in prime factorization of the number. Every 5th number in factorial product is divisable by 5 and thus contributes one 5; every 25th number is divisable by 25 and thus contributes _another_ 5; etc.
# See: https://algo.monster/liteproblems/172


def factorial_trailing_zeroes(n: int) -> int:
    numOf5 = 0
    # Each iteration divides n by 5 to count higher powers of 5
    while ( n > 0 ):
        n //= 5
        numOf5 += n
    return numOf5
##


def test__factorial_trailing_zeroes():
    tasks = [
        3,   # 0
        5,   # 1
        0,   # 0
        10,  # 2
    ]
    for n in tasks:
        print("================================================")
        print(f"Input: {n}")
        res = factorial_trailing_zeroes(n)
        print(f"Result: {res}")
##

    
