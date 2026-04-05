# lc0050__power.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0050__power import *

# RELOAD:
# import importlib; import lc0050__power; importlib.reload(lc0050__power); from lc0050__power import *

# The idea for x^n:
# - if n is even, x^n == x^(n/2) * x^(n/2)
# - if n is odd,  x^n == x * x^((n-1)/2) * x^((n-1)/2)
# - if n is odd, n//2 == (n-1)/2

def power(x: float, n: int) -> float:
    if ( x == 0 ):  return 0
    if ( n == 0 ):  return 1
    if ( n == 1 ):  return x
    negativeRes = (x < 0) and ((n % 2) != 0)
    if ( x < 0 ):
        x *= -1
    if ( n < 0 ):
        x = 1/x
        n *= -1

    res1 = power_recurse(x, n)
    res = res1 if (not negativeRes) else -res1
    return res
##


def power_recurse(x: float, n: int) -> float:
    # base cases
    if ( x == 0 ):  return 0
    if ( n == 0 ):  return 1
    if ( n == 1 ):  return x
    # recursive case
    halfN = n // 2
    halfPwr = power_recurse(x, halfN)
    if ( (n % 2) == 0 ):
        res = halfPwr * halfPwr
    else:
        res = halfPwr * halfPwr * x
    return res
##


def test__power():
    tasks = [[2,4], [2,5], [2,-5], [3,1], [3,-1], [-3,2], [-3,3], [3,13]]
    for x, n in tasks:
        print("===================================")
        print(f"x={x}, n={n}, expected: {x**n}")
        res = power(x, n)
        print(f"Result: {res}")
