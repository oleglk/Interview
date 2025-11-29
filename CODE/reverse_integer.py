# reverse_integer.py - Given a 32-bit signed integer, reverse digits of an integer. If reversing causes overflow, return 0.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from reverse_integer import *

# RELOAD:
# import importlib;    import reverse_integer;  importlib.reload(reverse_integer);  from reverse_integer import *


# The idea: cut least-significant digits from the source number, "push" into result by (10*result + digit), check overflow before each actual "push".


def reverse_integer(n: int) -> int:
    base = 10
    maxVal = 2**31 - 1
    sign = 1  if ( n >= 0 )  else -1
    if ( n == -2**31 ):  # cannot negate it, INT_MAX == 2**31 - 1
        return 0         # -2147483648 would anyway overflow if reversed
    pn = n * sign  # always positive
    res = 0
    while (pn > 0):
        leastDig = pn % base  # take least-significant digit
        pn //= base           # drop least-significant digit
        # check for future overflow
        ## (base*res + leastDig > maxVal)        causes overflow
        ## (res > (maxVal - leastDig) / base)    causes overflow
        if ( res > (maxVal - leastDig) / base ):   # ?? or // base ???
            return(0)  # overflow would occur
        res = base*res + leastDig  # push new digit
    reversed = res * sign
    return(reversed)


def test__reverse_integer():
    numbers = [1234, 0, -1234, 2147483647, 1234567890, -1234567890, 1000000009]
    for n in numbers:
        print("=========================")
        print(f"Input: {n}")
        res = reverse_integer(n)
        print(f"Result: {res}")
