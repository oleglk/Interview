# generate_parentheses.py - Given a number n, print all combinations of balanced parentheses of length n.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from generate_parentheses import *

# RELOAD:
# import importlib; import generate_parentheses; importlib.reload(generate_parentheses); from generate_parentheses import *


# The idea: recursion; can add "(" if number of open-s < n/2; can add ")" if number of close-s < number of open-s; the string is complete when its length is n.


def generate_parentheses(n: int) -> list[str]:
    if ( n % 2 ) != 0:
        raise Exception("Length must be even")
    res = []
    np = n / 2  # num of pairs of parentheses

    def valid_parentheses(currList: list[str], nOpen: int, nClose: int) -> None:
        nonlocal res, np

        if ( len(currList) == 2*np ):  # complete string built
            res.append("".join(currList))
            return

        if ( nOpen < np ):  # can add opener
            valid_parentheses(currList + ['('], nOpen+1, nClose)

        if ( nClose < nOpen ):  # can add closer
            valid_parentheses(currList + [')'], nOpen, nClose+1)

        return

    valid_parentheses([], 0, 0)
    return res


def test_generate_parentheses():
    for np in [0, 1, 2, 3]:
        print("======================================")
        print(f"Num pairs: {np}")
        res = generate_parentheses(2*np)
        print(f"Result: {res}")

