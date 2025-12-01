# container_with_most_water.py - Given n non-negative integers a1..an, where each represents a point at coordinate (i, ai). Find two lines that together with the x-axis form a container, such that the container contains the most water.


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from container_with_most_water import *

# RELOAD:
# import importlib; import container_with_most_water; importlib.reload(container_with_most_water); from container_with_most_water import *


def container_with_most_water(heights: list) -> int:
    maxArea = 0
    iLeft = 0
    iRight = len(heights) - 1
    while ( iLeft < iRight ):
        # check area with the current boundaries
        area = (iRight - iLeft) * min(heights[iLeft], heights[iRight])
        if ( area > maxArea ):
            maxArea = area
        # move the smaller boundary inwards
        if ( heights[iLeft] < heights[iRight] ):
            iLeft += 1
        else:
            iRight -= 1
    return(maxArea)


def test__container_with_most_water():
    tasks = [[1,2], [1,5,4,3], [3,1,2,4,5], [2,1,8,6,4,6,5,5]]
    #         1      6          12           25
    for heights in tasks:
        print("===========================")
        print(f"Input: {heights}")
        res = container_with_most_water(heights)
        print(f"Result: {res}")
