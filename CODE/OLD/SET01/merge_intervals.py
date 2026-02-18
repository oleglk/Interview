# merge_intervals.py - Given a collection of intervals, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from merge_intervals import *

# RELOAD:
# import importlib;    import merge_intervals;  importlib.reload(merge_intervals);  from merge_intervals import *


def merge_intervals(intervals: list):
    if ( len(intervals) <= 1 ):
        return(intervals)
    """Merges overlapping intervals. Input is list of [start, end]"""
    intervals.sort(key=lambda x: x[0])  # sort intervals by start time
    merged = [intervals[0]]
    for ivl in intervals[1:]:
        if ( ivl[0] <= merged[-1][1] ):  # 'ivl' overlaps the last merged
            merged[-1][1] = ivl[1]       # extend the last merged
        else:                            # 'ivl' doesn't overlap the last merged
            merged.append(ivl)           # insert the new interval
    return(merged)


def test__merge_intervals():
    ivs1 = [[1,2]]
    ivs2 = [[2,4], [1,2], [5,6]]
    ivs3 = [[1,2], [4,5], [6,7], [3,4], [7,8], [9,10]]
    for intervs in [ivs1, ivs2, ivs3]:
        print("=====================")
        print(f"Input:  {intervs}")
        res = merge_intervals(intervs)
        print(f"Output: {res}")
