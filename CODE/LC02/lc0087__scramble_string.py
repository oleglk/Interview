# lc0087__scramble_string.py
# We can scramble a string s to get a string t using the following algorithm:
# 1.   If the length of the string is 1, stop.
# 2.   If the length of the string is > 1, do the following:
#        Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
#        Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
#        Apply step 1 recursively on each of the two substrings x and y.
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0087__scramble_string import *

# RELOAD:
# import importlib; import lc0087__scramble_string; importlib.reload(lc0087__scramble_string); from lc0087__scramble_string import *

# The idea: use recursion. TODO: Better apply memoisation.
# See https://medium.com/@mrinmayeerane2810/leetcode-87-scramble-string-0ed548688abb


def is_scramble(s1: str, s2: str) -> bool:
    # check base conditions
    if ( len(s1) != len(s2) ):  return False
    if ( s1 == s2 ):  return True
    if ( (s1 == "") or (s2 == "") ):  return False  # ? is it needed ?
    if ( len(s1) == 1 ):  return False  # len(s2) == 1 too, but they aren't equal

    # recursive cases with all possible split positions
    n = len(s1)
    for i in range(1, n):  # in the source: (1,n); (0,n) and (1,n-1) don't work
        notSwapped = is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:])
        # 12,345 ->swap(2)-> 345,12
        swapped = is_scramble(s1[:i], s2[n-i:]) and is_scramble(s1[i:], s2[:n-i])
        if ( swapped or notSwapped ):
            return True

    return False
##


def test__is_scramble():
    tasks = [
        ["great", "rgeat"],   # True
        ["abcde", "caebd"],   # False
        ["a", "a"],           # True
    ]
    for s1, s2  in tasks:
        print("======================================")
        print(f"Input: {s1}, {s2}")
        res = is_scramble(s1, s2)
        print(f"Result: {res}")
##
