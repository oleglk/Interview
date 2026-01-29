# hit_count.py - Design a hit counter which counts the number of hits received in the past 5 minutes. It should support the following two operations: hit and getHits. hit(timestamp) – Shows a hit at the given timestamp. getHits(timestamp) – Returns the number of hits received in the past 5 minutes (300 seconds) (from currentTimestamp). Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order. You may assume that the earliest timestamp starts at 1.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from hit_count import *

# RELOAD:
# import importlib; import hit_count; importlib.reload(hit_count); from hit_count import *


# The idea: maintain a queue of the hits. Delete older-than-threshold hits upon each get().


class HitCount:
    _maxTime = 300
    def __init__(self):
        self.queue = []

    def hit(self, timeStamp):
        self.queue.append(timeStamp)

    def get_num_hits(self, timeStamp):
        while ( (len(self.queue) > 0) and
                (timeStamp - self.queue[0]) >= HitCount._maxTime ):
            self.queue.pop(0)
        return len(self.queue)


def test__HitCount():
    counter = HitCount();

    # hit at timestamp 1.
    counter.hit(1);

    # hit at timestamp 2.
    counter.hit(2);

    # hit at timestamp 3.
    counter.hit(3);

    # get hits at timestamp 4, should return 3.
    print(counter.get_num_hits(4));

    # hit at timestamp 300.
    counter.hit(300);

    # get hits at timestamp 300, should return 4.
    print(counter.get_num_hits(300));

    # get hits at timestamp 301, should return 3.
    print(counter.get_num_hits(301));
