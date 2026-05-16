# lc0069__sqrt.py
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0069__sqrt import *

# RELOAD:
# import importlib; import lc0069__sqrt; importlib.reload(lc0069__sqrt); from lc0069__sqrt import *

# The idea: use binary search to find smallest y whose y*y > x; the answer is y-1.
# See https://algo.monster/liteproblems/69


def int_sqrt(x: int) -> int:
    if ( x <= 1 ):
        return x
    left = 1;  right = x
    firstLarger = -1

    while ( left <= right ):
        mid = (left + right) // 2
        # check if mid*mid > x while preventing overflow
        if ( mid > x // mid ):
            firstLarger = mid  # could be the target unless smaller one found
            right = mid - 1
        else:
            left = mid + 1

    if ( firstLarger == -1 ):  raise Exception("firstLarger == -1")
    return (firstLarger - 1)
##

        
def test__int_sqrt():
    tasks = [
        4,   # 2
        8,   # 2
        2,   # 1
    ]
    for x in tasks:
        print("====================================")
        print(f"Input: {x}")
        res = int_sqrt(x)
        print(f"Result: {res}")
##
