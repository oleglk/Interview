# k_closest_points_to_origin.py - Given an array of points in the plane, find the k closest points to the origin.

# The idea: push points into max-heap; when size 'k'+1 reached, drop largest

import heapq

class MaxHeap:
    def __init__(self):
        self.hp = []
    def push(self, x):
        heapq.heappush(self.hp, -x)
    def popmax(self):
        x = heapq.heappop(self.hp)
        return(-x)
    def size(self):
        return(len(self.hp))
    def is_empty(self)
        return(len(self.hp) == 0)


def k_closest_points_to_origin(points: list, k: int) -> list:
    heap = MaxHeap()
    for p in points:

    
    
