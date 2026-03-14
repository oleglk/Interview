# lc0028__find_first_string_occurence.py
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0028__find_first_string_occurence import *

# RELOAD:
# import importlib; import lc0028__find_first_string_occurence; importlib.reload(lc0028__find_first_string_occurence); from lc0028__find_first_string_occurence import *

# The idea: check string matches starting from all positions in [0...n-m].


def find_first_string_occurence(needle: str, haystack: str) -> int:
    n = len(haystack)
    m = len(needle)
    for i in range(0, n - m + 1):
        substr = haystack[i:i+m]
        if ( substr == needle ):
            return i  # found
    return -1 # not found
##


def test__find_first_string_occurence():
    tasks = [
        ["sadbutsad", "sad"],  # 0
        ["leetcode", "leeto"], # -1
        ["hello", "ll"],       # 2
        ["aaaaa", "bba"]       # -1
    ]
    for haystack, needle in tasks:
        print("==================================")
        print(f"Input: haystack={haystack}, needle={needle}")
        res = find_first_string_occurence(needle, haystack)
        print(f"Result: {res}")
##
