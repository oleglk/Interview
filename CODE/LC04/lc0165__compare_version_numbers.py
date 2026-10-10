# lc0165__compare_version_numbers.py
# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.
# Return the following:
#    If version1 < version2, return -1.
#    If version1 > version2, return 1.
#    Otherwise, return 0.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0165__compare_version_numbers import *

# RELOAD:
# import importlib;    import lc0165__compare_version_numbers;  importlib.reload(lc0165__compare_version_numbers);  from lc0165__compare_version_numbers import *

# The idea: compare versions while at least one has characters left; accumulate current revision by (revision = 10*revision + int(version[i])), which ignores leading 0-s.
# See: https://algo.monster/liteproblems/165


def compare_version_numbers(version1: str, version2: str) -> int:
    n1 = len(version1);  n2 = len(version2)
    i1 = 0;  i2 = 0
    # compare while any string has characters left
    while ( (i1 < n1) or (i2 < n2) ):
        revision1 = 0;  revision2 = 0
        # parse and accumulate current revision field from version1
        while ( (i1 < n1) and (version1[i1] != ".") ):
            revision1 = 10 * revision1 + int(version1[i1])
            i1 += 1
        # parse and accumulate current revision field from version2
        while ( (i2 < n2) and (version2[i2] != ".") ):
            revision2 = 10 * revision2 + int(version2[i2])
            i2 += 1
        # compare the revisions
        if ( revision1 < revision2 ):    return -1
        elif ( revision1 > revision2 ):  return 1
        # skip dot separators; no problem if i >= n
        i1 += 1
        i2 += 1
        # current revisions are equal
    return  0  # no different revisions found - versions equal
##


def test__compare_version_numbers():
    tasks = [
        ["1.2", "1.10"],     # -1
        ["1.01", "1.001"],   # 0
        ["1.0", "1.0.0.0"],  # 0
    ]
    for version1, version2  in tasks:
        print("===========================================")
        print(f"Input: {version1}, {version2}")
        res = compare_version_numbers(version1, version2)
        print(f"Result: {res}")
##
