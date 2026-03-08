# lc0022_generate_parentheses.py
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0022_generate_parentheses import *

# RELOAD:
# import importlib; import lc0022_generate_parentheses; importlib.reload(lc0022_generate_parentheses); from lc0022_generate_parentheses import *


# The idea: recursively build string of parentheses while obeying at each step:
# - number of openers <= n
# - number of closers <= n
# - number of closers <= number of openers
# E.g. try adding each type of parentheses if possible.


def generate_parentheses(nPairs: int) -> list[str]:
    def parentheses_recurse(cntL: int, cntR: int, prefix: str) -> None:
        nonlocal result
        # check validity
        if ( (cntL > nPairs) or (cntR > nPairs) or (cntR > cntL) ):
            return  # invalid
        # check for completed string
        if ( (cntL == nPairs) and (cntR == nPairs) ):
            result.append(prefix)  # complete string is built
            return
        # try adding more parentheses
        parentheses_recurse(cntL+1, cntR, prefix + '(')
        parentheses_recurse(cntL, cntR+1, prefix + ')')
        return
    ##
    
    result = []   # will hold list of parentheses-strings
    parentheses_recurse(0, 0, "")
    return result
##


def test__generate_parentheses():
    tasks = [
        0, # ""
        1, # "()"
        2, # "(())", "()()"
        3, # "((()))", "(()())", "(())()", "()(())", "()()()"
    ]
    for nPairs in tasks:
        print("===============================")
        print(f"Input: {nPairs}")
        res = generate_parentheses(nPairs)
        print(f"Result: {res}")
##
