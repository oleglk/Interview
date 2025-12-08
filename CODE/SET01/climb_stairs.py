# climb_stairs.py - number of ways to climb n stairs with 1 or 2 steps per move

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from climb_stairs import *

# RELOAD:
# import importlib;    import climb_stairs;  importlib.reload(climb_stairs);  from climb_stairs import *


def climb_stairs(n: int) -> int:
    w1 = 1  # 0 stairs - 1 way
    w2 = 1  # 1 stair  - 1 way
    w = 1   # for 0 and 1 cases
    for i in range(2, n+1):
        w = w1 + w2  # either 1 stair and i-1 ways or 2 stairs and i-2 ways
        w1 = w2
        w2 = w
    return(w)


def test__climb_stairs():
    for i in range(0, 8+1):
        print(f"{i} => {climb_stairs(i)}")
