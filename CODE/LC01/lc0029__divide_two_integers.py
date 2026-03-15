# lc0029__divide_two_integers.py
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# Return the quotient after dividing dividend by divisor.
# If the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0029__divide_two_integers import *

# RELOAD:
# import importlib; import lc0029__divide_two_integers; importlib.reload(lc0029__divide_two_integers); from lc0029__divide_two_integers import *


# The idea: subtract divisor multiplied by powers of 2 obtained through left shift. Work on negative numbers to support -2^31.
# See: https://algo.monster/liteproblems/29

def divide_two_integers(dividend: int, divisor: int) -> int:
    if ( divisor == 1 ):
        return dividend
    if ( divisor == 0 ):
        raise Exception("Zero division")
    isPositive = True if ( ((dividend >= 0) and (divisor >= 0)) or ((dividend < 0) and (divisor < 0)) )  else False

    # handle overflow case
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if ( (dividend == INT_MIN) and (divisor == -1) ):
        return INT_MAX  # quotient would be strictly greater than 2^31 - 1

    # convert both numbers to negative to support -2^31
    if ( dividend > 0 ):        dividend = -dividend
    if ( divisor > 0 ):         divisor  = -divisor

    # (further comparisons are inverted since we work with negative numbers)
    quotient = 0
    while ( dividend <= divisor ):
        # find max 2^x * divisor that could be subtracted from current dividend
        currDivisor = divisor
        currQuotient = 1  # how many times divisor can be subtracted
        # checking (currDivisor >= -2^30) prevents divisor overflow
        while ( (currDivisor >= -2^30) and (dividend <= (currDivisor << 1)) ):
            currDivisor <<= 1   # multiply by 2
            currQuotient <<= 1  # multiply by 2
        # now currDivisor is the max 2^x * divisor
        # update dividend and quotient
        dividend -= currDivisor   # (subtracting negative from negative)
        quotient += currQuotient  # quotient is maintained positive
        
    # restore the sign
    if ( not isPositive ):
        quotient = -quotient
    return quotient
##


def test__divide_two_integers():
    tasks = [
        [15, 4],        # 3
        [7, -3],        # 2
        [-2**31, 2]     # -1073741824
    ]
    for dividend, divisor  in  tasks:
        print("================================================")
        print(f"Input: {dividend}, {divisor}")
        res = divide_two_integers(dividend, divisor)
        print(f"Result: {res}")
##
