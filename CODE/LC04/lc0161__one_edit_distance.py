# lc0161__one_edit_distance.py
# An edit between two strings is one of the following changes. 
#    Add a character
#    Delete a character
#    Change a character
# Given two strings s1 and s2, find if s1 can be converted to s2 with exactly one edit.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0161__one_edit_distance import *

# RELOAD:
# import importlib;    import lc0161__one_edit_distance;  importlib.reload(lc0161__one_edit_distance);  from lc0161__one_edit_distance import *

# The idea: traverse both strings simultneously. If characters in pos match, advance in both. If mismatch and length differ, it must be either insert into shorter or delete from longer, so advance in longer. If mismatch and lengths equal, advance in both. Count mismatches; if >1, return false.
# See: https://www.geeksforgeeks.org/dsa/check-if-two-given-strings-are-at-edit-distance-one/


def one_edit_distance(s1: str, s2: str) -> bool:
    mismCnt = 0
    l1 = len(s1);  l2 = len(s2)
    if ( abs(l1 - l2) > 1 ):  return False  # >1 edits needed

    i1 = 0;  i2 = 0
    while ( (i1 < l1) and (i2 < l2) ):
        if ( s1[i1] == s2[i2] ):  # current characters equal
            i1 += 1
            i2 += 1
            continue
        # current characters not equal
        mismCnt += 1
        if ( mismCnt > 1 ):
            return False
        if ( l1 == l2 ):  # only change can lead to one edit - advance both
            i1 += 1
            i2 += 1
            continue
        # lengths unequal; add to shorter or del from longer - advance longer
        if ( l1 < l2 ):
            i2 += 1
        else:
            i1 += 1

    # check leftover
    if ( (i1 < l1) or (i2 < l2) ):  # last char is mismatch
        return (mismCnt == 0)

    return True
##


def test__one_edit_distance():
    tasks = [
        ["geek", "geeks"],  # True
        ["geeks", "geeks"], # True
        ["peaks", "geeks"]  # False
    ]
    for s1, s2 in tasks:
        print("==============================================")
        print(f"Input: {s1}, {s2}")
        res = one_edit_distance(s1, s2)
        print(f"Result: {res}")
##
