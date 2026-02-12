# random_pick_with_weight.py - Design a data structure that randomly picks an index from an array w, where the probability of picking index i is w[i] / sum(w).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from random_pick_with_weight import *

# RELOAD:
# import importlib; import random_pick_with_weight; importlib.reload(random_pick_with_weight); from random_pick_with_weight import *


# The idea: build the array of intervals with lengths proportional to weights. Pick random numbers falling into these intervals. Use binary search to find index of the interval being picked - the one where the random number belongs.

# See https://algo.monster/liteproblems/528


import random


class Solution:
    def __init__(self, weights: list[int]):
        self.intervals = []
        self.totalSum = 0  # eventually the sum of all weights
        for w in weights:
            self.totalSum += w
            self.intervals.append(self.totalSum)

    def pick_index(self):
        target = random.randint(1, self.totalSum)  # ? maybe from 1 ?

        # Binary search to find the index
        left = 0;  right = len(self.intervals) - 1
        while ( left < right ):
            mid = left + (right - left) // 2
            if ( target > self.intervals[mid] ):
                left = mid + 1
            else:
                right = mid
        return left


    @staticmethod
    def test__pick_index():
        weights = [1, 8, 4]
        print("=======================")
        print(f"Weights: {weights}")
        sol = Solution(weights)
        freq = [0]*len(weights)
        for _ in range(0, len(weights)*10):
            idx = sol.pick_index()
            freq[idx] += 1
        print(f"Result: {freq}")

