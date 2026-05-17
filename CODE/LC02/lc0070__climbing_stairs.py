# lc0070__climbing_stairs.py
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0070__climbing_stairs import *

# RELOAD:
# import importlib; import lc0070__climbing_stairs; importlib.reload(lc0070__climbing_stairs); from lc0070__climbing_stairs import *


# The idea:
# One can reach stair #i from either stair #i-1 or stair #i-2. So f(i) = f(i-2) + f(i-1); this is Fibonachi sequence. Define f(0)==0, f(1)==1, then perform n iterations.
# See https://algo.monster/liteproblems/70

#    n:  1  2  3
# iter:  0  1  2
#    a:  1  1  2
#    b:  1  2  3

def climbing_stairs(n: int) -> int:
    if ( n <= 1 ):
        return n
    a = 0;  b = 1
    for i in range(0, n):
        sum = a + b
        a = b
        b = sum
    return b
##


def test__climbing_stairs():
    tasks = [
        2,  # 2
        3,  # 3
    ]
    for n in tasks:
        print("==============================")
        print(f"Input: {n}")
        res = climbing_stairs(n)
        print(f"Result: {res}")
##
