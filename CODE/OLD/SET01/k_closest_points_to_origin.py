# k_closest_points_to_origin.py - Given an array of points in the plane, find the k closest points to the origin.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from k_closest_points_to_origin import *

# RELOAD:
# import importlib; import k_closest_points_to_origin; importlib.reload(k_closest_points_to_origin); from k_closest_points_to_origin import *

# The idea: push points into max-heap; when size 'k'+1 reached, drop largest

import heapq

class MaxHeapOfPoints:
    """Stores tuples (-dist, x, y)"""
    def __init__(self):
        self.hp = []
    def push(self, xy):
        heapq.heappush(self.hp, dist_tuple(xy[0], xy[1]))
    def popmax(self):
        dxy = heapq.heappop(self.hp)
        return((dxy[1], dxy[2]))
    def size(self):
        return(len(self.hp))
    def is_empty(self):
        return(len(self.hp) == 0)
    def values(self):
        return([(v[1], v[2]) for v in self.hp])
####


def dist_tuple(x, y):
    """Returns tuple (dist^2,x,y) - point coords preceded by dist^2 to origin.
       Needed to dictate heap ordering. Negated to achieve max-heap."""
    return tuple([-x*x - y*y, x, y])


def k_closest_points_to_origin(points: list, k: int) -> list:
    if ( k == 0 ):
        return([])
    heap = MaxHeapOfPoints()
    for xy in points:
        heap.push(xy)
        if ( heap.size() >= k+1 ):
            heap.popmax()
    return(heap.values())


def test__k_closest_points_to_origin():
    tasks = [ [[], 1],  [[(1,1), (1,2), (1,3)], 2],
              [[[-1,4], [5,3], [-1,-1], [8,-6], [1,2]], 2],
              [[[1,3],[-2,2]], 1] ]
    for points, k  in  tasks:
        print("=================================")
        print(f"Input: {points},  k={k}")
        res = k_closest_points_to_origin(points, k)
        print(f"Result: {res}")

