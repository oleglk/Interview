# pow.py - Binary exponentiation (fast power)

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from pow import *

# RELOAD:
# import importlib; import pow; importlib.reload(pow); from pow import *


# The idea: repeatedly square as much as needed; handle odd power by making last multiplication. Use reciprocal for negative power.
## x^5 == (x^2)^2 * x
## 5/2=2; 2/2=1, so square while n > 1, halve n each time


def binary_exponent(x: float, n: int) -> float:
    if ( n == 0 ):
        return 1
    if ( x == 0 ):
        return 0
    exp = n if (n > 0) else -n
    
    res = x
    while ( exp > 1 ):
        res = res * res
        exp = exp // 2
        
    if ( ((abs(n) % 2) != 0) and (abs(n) != 1) ):  # odd power
        res = res * x
    if ( n < 0 ):                                  # negative power
        res = 1 / res

    return res


def test__binary_exponent():
    tasks = [[2,4], [2,5], [2,-5], [3,1], [3,-1], [3,2], [3,3]]
    for x, n in tasks:
        print("===================================")
        print(f"x={x}, n={n}, expected: {x**n}")
        res = binary_exponent(x, n)
        print(f"Result: {res}")
