# lc0008__string_to_integer.py

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
# The algorithm for myAtoi(string s) is as follows:
#    Whitespace: Ignore any leading whitespace (" ").
#    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
#    Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#    Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
# Return the integer as the final result.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0008__string_to_integer import *

# RELOAD:
# import importlib;    import lc0008__string_to_integer;  importlib.reload(lc0008__string_to_integer);  from lc0008__string_to_integer import *


def string_to_integer(intStr: str) -> int:
    base = 10
    isNegative = False
    isLeading = True
    signPermitted = True  # sign permitted before 1st digit incl leading zero
    res = 0  # will accumulate the result
    maxValPos = 2**31 - 1
    maxValNeg = -2**31
    intStr = intStr.strip()  # remove enclosing spaces

    for ch in intStr:
        if ( (not ch.isdigit()) and
             (not (isLeading and signPermitted and
                   ((ch == '-') or (ch == '+')))) ):
            # 1st non-digit terminates; single "0" treated here too
            return res  # stop at the 1st non-digit
        if ( isLeading and (ch == '0') ):
            signPermitted = False
            continue  # ignore leading zeroes
        if ( isLeading and signPermitted and (ch == '-') ):
            isNegative = True
            isLeading = False
            continue
        if ( isLeading and signPermitted and (ch == '+') ):
            isNegative = False
            isLeading = False
            continue
        # the current char must be a digit
        if ( not ch.isdigit() ):
            raise Exception(f"Got '{ch}' instead of a digit")
        isLeading = False
        signPermitted = False
        digit = ord(ch) - ord('0')
        if ( not isNegative ):  # positive; res >= 0
            # check for positive overflow before updating the number
            #       res*base + digit  VS  maxValPos
            if ( res > (maxValPos - digit) / base ):
                return maxValPos
            res = res*base + digit
        else:                # negative; res <= 0
            # check for negative overflow before updating the number
            #       res*base - digit  VS  maxValNeg
            if ( res < (maxValNeg + digit) / base ):
                return maxValNeg
            res = res*base - digit

    return res


def test__string_to_integer():
    tasks = [
        "42",            # 42
        " -042",         # -42
        "1337c0d3",      # 1337
        "0-1",           # 0
        "0",             # 0
        "words and 987", # 0
        "2147483648",    # 2147483647
        "-2147483649",   # -2147483648
    ]
    for s in tasks:
        print("============================")
        print(f"Input: '{s}'")
        res = string_to_integer(s)
        print(f"Result: {res}")
