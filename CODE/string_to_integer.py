# string_to_integer.py - Implement the my_atoi(string s) function which converts a string to a 32-bit signed integer (similar to C/C++'s atoi).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from string_to_integer import *

# RELOAD:
# import importlib;    import string_to_integer;  importlib.reload(string_to_integer);  from string_to_integer import *


def my_atoi(s: str) -> int:
    base = 10
    maxVal = 2**31 - 1  # positive limit; we'll serve -2**31 separately
    s = s.strip()

    # take digit-only substring - until end or 1st non-digit
    idxNotDigit = -1
    for i, c in enumerate(s):
        if ( not c.isdigit() ):  # non-digit terminates the number
           idxNotDigit = i
           break
    if ( idxNotDigit >= 0 ):
        s = s[0:idxNotDigit]
    if ( s == "-2147483648" ): # INT_MAX=2**31-1, INT_MIN=-2**31
        return(-2147483648)  # to avoid dealing with it
            
    
    sign = -1 if (s[0] == '-') else 1
    if (sign == -1):
        s = s[1:]  # drop the sign, will multiply at end
    res = 0
    for c in s:
        # check for future overflow if (base*res + int(c)) > maxVal
        ### ==> overflow if res > (maxVal - int(c)) / base
        if ( res > ((maxVal - int(c)) / base) ):
            return(sign * maxVal)
        res = base*res + int(c)

    res *= sign
    return(res)
