# lc0042__trapping_rain_water.py
# Given an array barHeights[] of size n consisting of non-negative integers, where each element represents the height of a bar in an elevation map and the width of each bar is 1, determine the total amount of water that can be trapped between the bars after it rains.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0042__trapping_rain_water import *

# RELOAD:
# import importlib; import lc0042__trapping_rain_water; importlib.reload(lc0042__trapping_rain_water); from lc0042__trapping_rain_water import *

# The idea:
# Amount above each bar = min{maxHeightOnLeft, maxHeightOnRight} - barHeight.
# Start by computing maxHeightOnLeft, maxHeightOnRight arrays.
# Bars #0 and #n-1 don't store any water.


def trapping_rain_water(barHeights: list[int]) -> int:
    n = len(barHeights)
    
    # compute maxHeightOnLeft, maxHeightOnRight arrays
    maxHeightOnLeft = [0]*n;  maxHeightOnRight = [0]*n
    maxHeightOnLeft[0] = barHeights[0]
    for i in range(1, n, 1):
        maxHeightOnLeft[i] = max(maxHeightOnLeft[i-1], barHeights[i])
    maxHeightOnRight[n-1] = barHeights[n-1]
    for i in range(n-2, -1, -1):
        maxHeightOnRight[i] = max(maxHeightOnRight[i+1], barHeights[i])

    # compute amount of water in [1..n-2]
    total = 0
    for i in range(1, n-1):
        aboveBar = min(maxHeightOnLeft[i], maxHeightOnRight[i]) - barHeights[i]
        total += aboveBar

    return total
##


def test__trapping_rain_water():
    tasks = [
        [3, 0, 1, 0, 4, 0, 2],  # 10
        [3, 0, 2, 0, 4],        # 7
        [1, 2, 3, 4],           # 0
    ]
    for barHeights in tasks:
        print("===============================")
        print(f"Input: {barHeights}")
        res = trapping_rain_water(barHeights)
        print(f"Result: {res}")
##
