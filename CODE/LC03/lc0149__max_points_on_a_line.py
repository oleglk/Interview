# lc0149__max_points_on_a_line.py
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0149__max_points_on_a_line import *

# RELOAD:
# import importlib;    import lc0149__max_points_on_a_line;  importlib.reload(lc0149__max_points_on_a_line);  from lc0149__max_points_on_a_line import *

# The idea: check slope on all pairs of points; for each line-starting point build map {slope::cnt}. Canonize the slope and represent as string to avoid floating-point issues.
# See: https://www.geeksforgeeks.org/dsa/count-maximum-points-on-same-line/

from math import gcd


def max_points_on_a_line(x: list[int], y: list[int]) -> int:
    if ( len(x) <= 2 ):  return len(x)
    n = len(x)
    maxPoints = 0
    
    # traverse all points as line-starters
    for i in range(0, n):
        overlapCnt = 0  # num of points equal to the current starter
        slopeToCnt = {} # counts of lines starting at current starter per slopes
        currMax = 0  # for current starter - max num of points on same line
        
        # traverse second points for current starter;
        # begin from i+1 to avoid counting same pair twice
        for j in range(i+1, n):
            if ( (x[i] == x[j]) and (y[i] == y[j]) ):
                overlapCnt += 1
            else:
                if ( x[i] == x[j] ):  # vertical line; use pseudo-slope
                    slopeStr = "vertical"
                else:                 # normal slope
                    # represent slope in canonical string form
                    diffX = x[j] - x[i]
                    diffY = y[j] - y[i]
                    g = gcd(abs(diffX), abs(diffY))
                    diffX //= g
                    diffY //= g
                    if ( diffX < 0 ):  # canonize signs too
                        diffX *= -1
                        diffY *= -1
                    slopeStr = f"{diffY}/{diffX}"
                # increment count for either normal or vertical lines
                slopeToCnt[slopeStr] = slopeToCnt.get(slopeStr, 0) + 1
                currMax = max(currMax, slopeToCnt[slopeStr])

        # update global maximum by current point's maximum
        maxPoints = max(maxPoints, 1 + overlapCnt + currMax)

    return maxPoints
##


def test__max_points_on_a_line():
    tasks = [
        [[1,2,3], [1,2,3]],              # 3
        [[1,3,5,4,2,1], [1,2,3,1,3,4]],  # 4
        [[1,2,1,1,1], [1,2,3,4,5]],      # 4
    ]
    for x, y in tasks:
        print("=====================================")
        print(f"Input: x={x}, y={y}")
        res = max_points_on_a_line(x, y)
        print(f"Result: {res}")
##
