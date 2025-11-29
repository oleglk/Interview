# string_to_integer.py - Implement the my_atoi(string s) function which converts a string to a 32-bit signed integer (similar to C/C++'s atoi).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from string_to_integer import *

# RELOAD:
# import importlib;    import string_to_integer;  importlib.reload(string_to_integer);  from string_to_integer import *


def my_atoi(s: str) -> int:
    base = 10
    maxValPos = 2**31 - 1  # positive limit; we'll serve -2**31 separately
    maxValNeg = -2**31     # negative limit
    s = s.strip()
    sign = -1 if (s[0] == '-') else 1
    if (sign == -1):
        s = s[1:]  # drop the sign, will multiply at end

    # take digit-only substring - until end or 1st non-digit
    for i, c in enumerate(s):
        if ( not c.isdigit() ):  # non-digit terminates
           s = s[0:i]
           break
    if ( s == "2147483648" and (sign < 0) ): # INT_MAX=2**31-1, INT_MIN=-2**31
        return(-2147483648)  # to avoid dealing with it
            
    res = 0
    for c in s:
        # check for future overflow if (base*res + int(c)) > maxVal
        ### ==> overflow if res > (maxVal - int(c)) / base
        if ( res > ((maxValPos - int(c)) / base) ):
            return(maxValPos if (sign > 0) else maxValNeg)
        res = base*res + int(c)

    res *= sign
    return(res)


def test__my_atoi():
    strNums = ["0", "-1", "1", "-123", "123", "-2147483648", "2147483648", "2147483647", "3000000000", "-3000000000"]
    for strNum in strNums:
        print("===========================")
        print(f"Input = '{strNum}'")
        res = my_atoi(strNum)
        print(f"Result = {res}")
