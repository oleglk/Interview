# meeting_rooms_1.py - Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from meeting_rooms_1 import *

# RELOAD:
# import importlib; import meeting_rooms_1; importlib.reload(meeting_rooms_1); from meeting_rooms_1 import *


# The idea: sort intervals by start time, then compare end-time of each interval with start time of the next interval.

def meeting_rooms_1(times: list) -> bool:
    times.sort(key=lambda x: x[0])
    for i in range(0, len(times)-1):
        if ( times[i+1][0] < times[i][1] ):
            return(False)
    return(True)


def test__meeting_rooms_1():
    tasks = [ [(1,2), (5,6), (3,4)],  [(2,3), (4,5), (1,3)], [(1,2), (2,3)] ]
    for times in tasks:
        print("================================")
        print(f"Input: {times}")
        res = meeting_rooms_1(times)
        print(f"Result: {res}")
