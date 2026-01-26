# pow.py - Binary exponentiation (fast power)

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from pow import *

# RELOAD:
# import importlib; import pow; importlib.reload(pow); from pow import *


# The idea (for x^n):
# - if n is 0, x^n = 1
# - if n is even, x^n = ( x^(n/2) )^2
# - if n is odd, x^n = x*( x^((n-1)/2) )^2

def binary_exponent(x: float, n: int) -> float:
    """Recursively computes x^n for any x and any integer n"""
    if ( n == 0 ):
        return 1
    if ( x == 0 ):
        return 0
    exp = n if (n > 0) else -n
    negativeRes = (x < 0) and (n%2 != 0)
    if ( x < 0 ):
        x = -x  # remember to negate in the end

    res = binary_exponent_rec(x, exp)
    if ( n < 0 ):
        res = 1 / res
    if ( negativeRes ):
        res = -res
    return res


def binary_exponent_rec(x: float, n: int) -> float:
    """Recursively computes x^n for x >= 0 and integer n >= 0"""
    if ( n == 0 ):
        return 1
    if ( x == 0 ):
        return 0

    # if n is even, n/2==n//2; if n is odd, (n-1)/2==n//2
    res1 = binary_exponent_rec(x, n // 2)
    if ( n%2 == 0 ):
        res = res1 * res1
    else:
        res = x * res1 * res1
    return res



def test__binary_exponent():
    tasks = [[2,4], [2,5], [2,-5], [3,1], [3,-1], [-3,2], [-3,3], [3,13]]
    for x, n in tasks:
        print("===================================")
        print(f"x={x}, n={n}, expected: {x**n}")
        res = binary_exponent(x, n)
        print(f"Result: {res}")
