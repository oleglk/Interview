# lc0202__happy_number.py
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0202__happy_number import *

# RELOAD:
# import importlib;    import lc0202__happy_number;  importlib.reload(lc0202__happy_number);  from lc0202__happy_number import *

# The idea: run the loop of replacement by sum of squares of digits. If 1 reached, return True. If cycle detected, return False. The reason it works: possible number of values is restricted - [1, 9^2+...+9^2].
# See: https://algo.monster/liteproblems/202


def happy_number(n: int) -> bool:
    seen = set()  # seen numbers for loop detection
    while ( (n != 1) and (n not in seen) ):
        seen.add(n)
        # compute sum of squares of n's digits
        sumOfSquares = 0
        while ( n > 0 ):
            n, lastDigit = divmod(n, 10)
            sumOfSquares += lastDigit * lastDigit
        n = sumOfSquares
    return (n == 1)
##


def test__happy_number():
    tasks = [
        19,  # True
        2,   # False
    ]
    for n in tasks:
        print("=========================================")
        print(f"Input: {n}")
        res = happy_number(n)
        print(f"Result: {res}")
##
