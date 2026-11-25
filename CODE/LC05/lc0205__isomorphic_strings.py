# lc0205__isomorphic_strings.py
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0205__isomorphic_strings import *

# RELOAD:
# import importlib;    import lc0205__isomorphic_strings;  importlib.reload(lc0205__isomorphic_strings);  from lc0205__isomorphic_strings import *

# The idea: traverse positions in the two strings and check for mapping conflicts.
# See: https://www.geeksforgeeks.org/dsa/check-if-two-given-strings-are-isomorphic-to-each-other/


def isomorphic_strings(s1: str, s2: str) -> bool:
    if ( len(s1) != len(s2) ):
        return False
    mappedFrom = {}  # will map chars of s1 to chars of s2
    isMappedTo = set()  # whether a char in s2 is mapped to
    
    for i in range(0, len(s1)):
        if ( s1[i] in mappedFrom ):
            if ( mappedFrom[s1[i]] != s2[i] ): # this char mapped differently
                return False
        else:  # s1[i] is not yet mapped from
            if ( s2[i] in isMappedTo ):  # s2[i] mapped from other char
                return False
            # neither s1[i] nor s2[i] are mapped
            mappedFrom[s1[i]] = s2[i]
            isMappedTo.add(s2[i])

    return True
##


def test__isomorphic_strings():
    tasks = [
        ["egg", "add"],     # True
        ["f11", "b23"],     # False
        ["paper", "title"], # True
    ]
    for s1, s2 in tasks:
        print("================================")
        print(f"Input: {s1}, {s2}")
        res = isomorphic_strings(s1, s2)
        print(f"Result: {res}")
##
