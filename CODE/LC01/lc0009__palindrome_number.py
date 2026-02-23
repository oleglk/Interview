# lc0009__palindrome_number.py
# Given an integer x, return true if x is a palindrome, and false otherwise.
# (-2^31 <= x <= 2^31-1)

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0009__palindrome_number import *

# RELOAD:
# import importlib;    import lc0009__palindrome_number;  importlib.reload(lc0009__palindrome_number);  from lc0009__palindrome_number import *

# The idea: reverse x mathematically by retrieving least-significant digits and accumulaing new number starting from them. Afterwards compare the new number to x.
# Note that negative numbers aren't palindromes.
# Numbers that overflow when reversed aren't palindromes since x didn't overflow.


def reverse_positive_integer(x: int) -> int:
    """Returns the reverse of 'x' or -1 if it overflows 2^31-1.""" 
    base = 10
    maxVal = 2**31 - 1
    outInt = 0
    while ( x > 0 ):
        lastDigit = x % base
        x //= base
        # check for potential overflow: outInt*base + lastDigit  VS  maxVal
        if ( outInt > (maxVal - lastDigit) / base ):
            return -1  # overflow
        outInt = outInt * base + lastDigit
    return outInt


def is_palindrome_number(x: int) -> bool:
    if ( x < 0 ):
        return False  # negative is not a palindrome
    revX = reverse_positive_integer(x)
    print(f"@@ Reverse of {x} is {revX}")
    if ( revX ) == -1:
        return False  # overflowing-when-reversed is not a palindrome
    return (revX == x)


def test__is_palindrome_number():
    tasks = [
        0,         # True
        1,         # True
        121,       # True
        -121,      # False
        10,        # False
        5445,      # True
        2147483647 # False
    ]
    for n in tasks:
        print("=========================")
        print(f"Input: {n}")
        res = is_palindrome_number(n)
        print(f"Result: {res}")
