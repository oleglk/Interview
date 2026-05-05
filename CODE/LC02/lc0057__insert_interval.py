# lc0057__insert_interval.py
# You are given an array of non-overlapping intervals 'intervals' where intervals[i] = [starti, endi] represent the start and the end of the i-th interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0057__insert_interval import *

# RELOAD:
# import importlib; import lc0057__insert_interval; importlib.reload(lc0057__insert_interval); from lc0057__insert_interval import *

# The idea:
# - (list of intervals is already sorted by start time)
# - copy all intervals that end before newInterval begins
# - merge newInterval with the 1st old interval that ends after newInterval begins (both start- and end-time may change)
# - merge all consequent old intervals that begin before the new merged interval ends (only end-time may change)
# - copy all old intervals that begin after the new merged interval ends


def insert_interval(intervals: [list[int,int]], newInterval: list[int,int]) -> list[list[int,int]]:
    if ( len(intervals) == 0 ):
        return newInterval
    n = len(intervals)
    resList = []
    # copy all intervals that end before newInterval begins
    currI = 0
    while ( (currI < n) and (intervals[currI][1] < newInterval[0]) ):
        resList.append(intervals[currI])
        currI += 1
    if ( currI >= n ):  # no more old intervals
        resList.append(newInterval)
        return resList
    # #currI is the 1st old interval that ends after newInterval begins
    # merge all intervals that start before new (merged) interval ends
    while ( (currI < n) and (intervals[currI][0] <= newInterval[1]) ):
        # #currI begins before newInterval ends - e.g. they overlap
        mergedStart = min(intervals[currI][0], newInterval[0])
        mergedEnd   = max(intervals[currI][1], newInterval[1])
        newInterval = [mergedStart, mergedEnd]
        currI += 1
    resList.append(newInterval)
    # #currI is the 1st old interval that begins after newInterval ends
    # copy all old intervals that begin after the new merged interval ends
    while ( currI < n ):
        resList.append(intervals[currI])
        currI += 1
    return resList
##


def test__insert_interval():
    tasks = [
        [[[1,3], [4,5], [6,7], [8,10]],  [5,6]],  # [[1,3], [4,7], [8,10]]
        [[[1,2], [3,5], [6,7], [8,10], [12,16]],  [4,9]],  # [[1,2], [3,10], [12,16]]
        [[[1,3],[6,9]],  [2,5]],  # [[1,5], [6,9]]
    ]
    for  intervals, newInterval  in tasks:
        print("========================================")
        print(f"Input: {intervals}, newInterval={newInterval}")
        res = insert_interval(intervals, newInterval)
        print(f"Result: {res}")
##

