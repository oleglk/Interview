# lc0007__reverse_integer.py - Given a 32-bit signed integer, reverse digits of an integer. If reversing causes overflow, return 0.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0007__reverse_integer import *

# RELOAD:
# import importlib;    import lc0007__reverse_integer;  importlib.reload(lc0007__reverse_integer);  from lc0007__reverse_integer import *

# The idea: in loop extract last digit by division (% AND //), append the last digit to the result:
# (lastDigit = inpInt % 10,  inpInt //= 10,  outInt = outInt * 10 + lastDigit)
# Do check for overflow before incrementing outInt.


def reverse_integer(inpInt: int) -> int:
    base = 10
    maxVal = 2**31 - 1
    outInt = 0
    if (inpInt == -2**31):
        return 0  # -2147483648 anyway overflows if reversed
    sign = 1 if (inpInt >= 0) else -1
    inpInt *= sign  # convert to positive for simplicity

    while ( inpInt > 0 ):
        lastDigit = inpInt % base
        inpInt //= base
        # check for overflow before incrementing 'outInt'
        if ( outInt > (maxVal - lastDigit) / base ):
            return 0  # overflow would occur
        outInt = outInt * base + lastDigit  # append the current digit

    outInt *= sign
    return outInt


def test__reverse_integer():
    numbers = [1234,           # 4321
               0,              # 0
               -1234,          # -4321
               2147483647,     # 0
               1234567890,     # 987654321
               -1234567890,    # -987654321
               1000000009      # 0
               ]
    for n in numbers:
        print("=========================")
        print(f"Input: {n}")
        res = reverse_integer(n)
        print(f"Result: {res}")
