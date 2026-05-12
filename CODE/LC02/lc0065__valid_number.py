# lc0065__valid_number.py
# Given a string s, return whether s is a valid number.
# For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0065__valid_number import *

# RELOAD:
# import importlib; import lc0065__valid_number; importlib.reload(lc0065__valid_number); from lc0065__valid_number import *

# Formally, a valid number is defined using one of the following definitions:
# - An integer number followed by an optional exponent.
# - A decimal number followed by an optional exponent.
# An integer number is defined with an optional sign '-' or '+' followed by digits.
# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
# - Digits followed by a dot '.'.
# - Digits followed by a dot '.' followed by digits.
# - A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.
# The digits are defined as one or more digits.

# The idea: traverse the string while maintaining flags of seen stuff and checking error conditions. Upon exponent reset flags of sign, dot and digits.


def valid_number(s: str) -> bool:
    if ((s is None) or (len(s) == 0)):  return False
    seenSign = seenDot = seenNum = seenExp = False
    for c in s:
        if ( (c == '+') or (c == '-') ):
            if ( seenSign or seenNum or seenDot ):
                return False
            seenSign = True
        elif ( (c >= '0') and (c <= '9') ):
            seenNum = True
        elif ( c == '.' ):
            if ( seenDot or seenExp ):
                return False
            seenDot = True
        elif ( (c == 'e') or (c == 'E') ):
            if ( seenExp or (not seenNum) ):
                return False
            seenExp = True
            seenSign = seenDot = seenNum = False
        else:
            return False  # any other character is invalid
    return seenNum
##


def test__valid_number():
    tasksGood = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    tasksBad = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for s in tasksGood:
        print("=======================================")
        print(f"Input (number): {s}")
        res = valid_number(s)
        if ( res == True):  print("Result: passed")
        else:               print("Result: failed")
    for s in tasksBad:
        print("=======================================")
        print(f"Input: (not number) {s}")
        res = valid_number(s)
        if ( res == False):  print("Result: passed")
        else:                print("Result: failed")
##
