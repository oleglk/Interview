# merge_intervals.py - combine overlapping intervals

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from merge_intervals import *

# RELOAD:
# import importlib; import merge_intervals; importlib.reload(merge_intervals); from merge_intervals import *


# The idea: sort intervals by start time; repeatedly either add next interval to the last in result list (if overlapped), or insert new interval into the result list.


def merge_intervals(intervals: list) -> list:
    # assume interval given as (start, end) tuple, so sort just works
    intervals.sort()
    res = [intervals[0]]  # init result with the 1st interval
    # repeatedly compare last resulting interval
    # with intervals in the sorted list; extend the last or add new interval
    for i in range(1, len(intervals)):
        if ( intervals[i][0] <= res[-1][1] ):  # do overlap
            res[-1][1] = max(intervals[i][1], res[-1][1])  # extend the last
        else:                                   # do not overlap
            res.append(intervals[i])  # add new interval which becomes the last
    return res


def test__merge_intervals():
    tasks = [
        [[1,3],[2,6],[8,10],[15,18]],  # [[1,6],[8,10],[15,18]]
        [[1,4],[4,5]],                 # [[1,5]]
        [[4,7],[1,4]],                 # [[1,7]]
        [[3,4],[1,2],[5,6]]            # [[1,2],[3,4],[5,6]]
    ]
    for intervals in tasks:
        print("============================================")
        print(f"Input: {intervals}")
        res = merge_intervals(intervals)
        print(f"Result: {res}")
