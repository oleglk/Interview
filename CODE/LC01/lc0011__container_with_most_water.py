# lc0011__container_with_most_water.py

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0011__container_with_most_water import *

# RELOAD:
# import importlib; import lc0011__container_with_most_water; importlib.reload(lc0011__container_with_most_water); from lc0011__container_with_most_water import *

# The idea: start with outer lines, then move the smaller boundary inwards
# See https://www.geeksforgeeks.org/dsa/container-with-most-water/


def container_with_most_water(heights: list[int]) -> int:
    maxArea = 0
    left = 0
    right = len(heights) - 1

    while ( left < right ):
        # consider the current area
        area = (right - left) * min(heights[left], heights[right])
        maxArea = max(maxArea, area)
        # move the smaller boundary inwards
        if ( heights[left] < heights[right] ):
            left += 1
        else:
            right -= 1

    return maxArea


def test__container_with_most_water():
    tasks = [[1,2], [1,5,4,3], [3,1,2,4,5], [2,1,8,6,4,6,5,5]]
    #         1      6          12           25
    for heights in tasks:
        print("===========================")
        print(f"Input: {heights}")
        res = container_with_most_water(heights)
        print(f"Result: {res}")
