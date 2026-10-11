# lc0166__fraction_to_recurring_decimal.py
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses
# If multiple answers are possible, return any of them.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0166__fraction_to_recurring_decimal import *

# RELOAD:
# import importlib;    import lc0166__fraction_to_recurring_decimal;  importlib.reload(lc0166__fraction_to_recurring_decimal);  from lc0166__fraction_to_recurring_decimal import *

# The idea: perform manual long division. Note that the same remainder seen twice means recurring part. Mark positions of remainder beginnings in a dict. When remainder seen 2nd time, insert "(" at its 1st (stored) position and insert ")" at the current position. 
# See: https://algo.monster/liteproblems/166


def fraction_to_recurring_decimal(numerator: int, denominator: int) -> str:
    if ( numerator == 0 ):
        return 0
    result = []
    isNegative = (numerator > 0) ^ (denominator > 0)
    if ( isNegative ):
        result.append("-")
    # work with 2 positive numbers for simplicity
    dividend, divisor = abs(numerator), abs(denominator)
    
    # take integer part, return if zero remainder
    result.append( str(dividend // divisor) )
    remainder = dividend % divisor
    if ( remainder == 0 ):
        return "".join(result)
    result.append(".")  # result isn't integer, insert the dot

    # process fractional part
    remainderPositions = {}
    while ( remainder > 0 ):
        remainderPositions[remainder] = len(result)
        
        # manual division
        remainder *= 10
        fractDigit = remainder // divisor
        result.append( str(fractDigit) )
        
        # calc new remainder and check if it already appeared
        remainder = remainder % divisor
        if ( remainder in remainderPositions ):
            # insert "(" at the position of the 1st occurence of this remainder
            result.insert(remainderPositions[remainder], "(")
            # add ")" at the current position
            # - end of recurring part == beginning of its 2nd occurence
            result.append(")")
            break  # the rest is recurring
    return "".join(result)
##


def test__fraction_to_recurring_decimal():
    tasks = [
        [1, 2],   # "0.5"
        [2, 1],   # "2"
        [4, 333], # "0.(012)"
    ]
    for numerator, denominator  in tasks:
        print("==============================================")
        print(f"Input: {numerator} / {denominator}")
        res = fraction_to_recurring_decimal(numerator, denominator)
        print(f"Result: {res}")
##
