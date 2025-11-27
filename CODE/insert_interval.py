# insert_interval.py - Given a set of non-overlapping intervals sorted by start times, insert a new interval and merge if necessary.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from insert_interval import *

# RELOAD:
# import importlib;    import insert_interval;  importlib.reload(insert_interval);  from insert_interval import *


def insert_interval(intervals: list, newInterv: list) -> list:
    res = []
    n = len(intervals)
    if ( n == 0 ):
        return(newInterv)
    
    i = 0
    # insert prior intervals
    while ( (i < n) and (intervals[i][1] < newInterv[0]) ):
        res.append(intervals[i])
        i += 1
    # interval #i either not exists or ends after 'newInterv' started
    if ( i == n ):
        return(res + newInterv)  # no more intervals were after #i-1
    # interval #i ends after 'newInterv' started
    newBeg = newInterv[0];  newEnd = newInterv[1]
    while ( (i < n) and (intervals[i][0] <= newInterv[1]) ):
        # interval #i starts before 'newInterv' ended - merge
        print(f"@@ Merge {intervals[i]} with (new) {newInterv}")
        newBeg = min(newBeg, intervals[i][0])
        newEnd = max(newEnd, intervals[i][1])
        i += 1
    res.append([newBeg, newEnd])
    # append intervals that start after 'newInterv' ended
    for j in range(i, n):
        res.append(intervals[j])

    return(res)
        


def test__insert_interval():
    l1 = [[1,3], [7,9], [13,15]]
    newInts = [[1,4], [2,4], [6,8], [7, 9], [8, 13], [2,14]]
    for newInt in newInts:
        print("===============================")
        print(f"Input:  {l1}, insert {newInt}")
        res = insert_interval(l1, newInt)
        print(f"Output: {res}")
