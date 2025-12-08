# meeting_rooms_2.py - Given an array of meeting time intervals, find the minimum number of conference rooms required.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from meeting_rooms_2 import *

# RELOAD:
# import importlib; import meeting_rooms_2; importlib.reload(meeting_rooms_2); from meeting_rooms_2 import *

# The idea: build event queue (min-heap) where an event is (time, beginOrEnd); 'nRooms' will track number of rooms needed each time; incremented by begin-event, decremented by end-event; loop of extract-min, update 'currrent'; maintain 'maxRooms' var that picks max seen value of 'nRooms'.


import heapq

class PrioQueue:
    def __init__(self):
        self.hp = []

    def enqueue(self, x):
        heapq.heappush(self.hp, x)

    def dequeue(self):
        return(heapq.heappop(self.hp))

    def is_empty(self):
        return(len(self.hp) == 0)
####


def meeting_rooms_2(times):
    """Returns mn number of rooms to accomodate meetings specified by (begin-time, end-time) pairs in 'times' list."""
    # build priority queue of begin/end events
    queue = PrioQueue()
    for beg, end  in  times:
        # if end- and begin events come at the same time, process end first
        #   in order to "free" the room; use event-type ordering
        queue.enqueue((beg, "2B"))
        queue.enqueue((end, "1E"))
    # determine max number of rooms used simultaneously
    nRooms = 0
    maxRooms = 0
    while ( not queue.is_empty() ):
        time, begOrEnd = queue.dequeue()
        if ( begOrEnd == "2B" ):
            nRooms += 1
            if ( nRooms > maxRooms ):
                maxRooms = nRooms
        else:
            nRooms -= 1
    return(maxRooms)
                                                                                                                                      

def test__meeting_rooms_2():
    tasks = [ [(1,2), (5,6), (3,4)],  [(2,3), (4,5), (1,3)], [(1,2), (2,3)],
              [(1,2), (2,4), (2,5), (3,6), (7,8)],
              [(1,3), (1,2), (1,3), (1,4)] ]
    for times in tasks:
        print("================================")
        print(f"Input: {times}")
        res = meeting_rooms_2(times)
        print(f"Result: {res}")
