# lc0056__merge_intervals.py
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0056__merge_intervals import *

# RELOAD:
# import importlib; import lc0056__merge_intervals; importlib.reload(lc0056__merge_intervals); from lc0056__merge_intervals import *

# The idea:
# Sort intervals by begin time. Maintain the last merged interval as the last in the resulting list. Traverse later intervals; if a later interval overlaps with the last merged one, extend the last merge; otherwise append this later interval to result list and treat as last merged.
# See https://www.geeksforgeeks.org/dsa/merging-intervals/


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if ( len(intervals) <= 1 ):
        return intervals
    intervals.sort()  # sort by begin time
    result = [intervals[0]]
    lastMerged = result[-1]
    for curr in intervals[1:]:
        if ( curr[0] <= lastMerged[1] ):  # overlap
            lastMerged[1] = max(lastMerged[1], curr[1])  # extend the last merged
        else:  # no overlap - make the current later interval be the last merged
            result.append(curr)
            lastMerged = result[-1]
    return result
##


def test__merge_intervals():
    tasks = [
        [[1,3],[2,6],[8,10],[15,18]],  # [[1,6],[8,10],[15,18]]
        [[1,4],[4,5]],                 # [[1,5]]
        [[4,7],[1,4]],                 # [[1,7]]
        [[1,3],[2,4],[6,8],[9,10]],    # [[1,4],[6,8],[9,10]]
        [[7,8],[1,5],[2,4],[4,6]]      # [[1,6],[7,8]]
    ]
    for intervals in tasks:
        print("============================================")
        print(f"Input: {intervals}")
        res = merge_intervals(intervals)
        print(f"Result: {res}")
##
