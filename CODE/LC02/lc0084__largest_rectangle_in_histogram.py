# lc0084__largest_rectangle_in_histogram.py
# Given an array of integers 'heights' representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0084__largest_rectangle_in_histogram import *

# RELOAD:
# import importlib; import lc0084__largest_rectangle_in_histogram; importlib.reload(lc0084__largest_rectangle_in_histogram); from lc0084__largest_rectangle_in_histogram import *

# The idea: rectangle with height of any bar is restricted from left by closest previous smaller bar, and from right - by closest next smaller bar.

# How to find previous-smaller-element:
# See https://medium.com/algorithms-digest/previous-smaller-element-e3996fb8be3c
# See (Python code) - https://www.geeksforgeeks.org/dsa/find-the-nearest-smaller-numbers-on-left-side-in-an-array/
# How to find next-smaller-element:
# (Oleg) modify the code of previous-smaller-element - init array elements to n instead of -1, and traverse from right to left

# The main algorithm - using previous-smaller-element and next-smaller-element:
# https://www.geeksforgeeks.org/dsa/largest-rectangular-area-in-a-histogram-using-stack/#expected-approach-on-time-and-on-space
# (see approach using 2 stacks)


def find_previous_smaller_element(heights: list[int]) -> list[int]:
    n = len(heights)
    pse = [-1]*n  # for resulting indices of previous smaller elements
    st = []  # helper stack - will hold element indices
    
    for i in range(0, n):
        # look for pse[i]
        # pop all elements >= heights[i] - they cannot be prev-smaller
        # (and for further elements larger than #i, #i itself is prefered)
        while ( st and (heights[st[-1]] >= heights[i]) ):
            st.pop()
        # if stack is not empty, top is index of the nearest smaller
        if ( st ):
            pse[i] = st[-1]
        # push index of the current element
        st.append(i)

    return pse
##


def find_next_smaller_element(heights: list[int]) -> list[int]:
    n = len(heights)
    nse = [n]*n  # for resulting indices of next smaller elements
    st = []  # helper stack - will hold element indices
    
    for i in range(n-1, -1, -1):
        # look for nse[i]
        # pop all elements >= heights[i] - they cannot be next-smaller
        # (and for further elements larger than #i, #i itself is prefered)
        while ( st and (heights[st[-1]] >= heights[i]) ):
            st.pop()
        # if stack is not empty, top is index of the nearest smaller
        if ( st ):
            nse[i] = st[-1]
        # push index of the current element
        st.append(i)

    return nse
##


def largest_rectangle_in_histogram(heights: list[int]) -> int:
    pse = find_previous_smaller_element(heights)
    nse = find_next_smaller_element(heights)
    maxArea = -1
    for i in range(0, len(heights)):
        width = nse[i] - pse[i] - 1
        area = heights[i] * width
        maxArea = max(maxArea, area)
    return maxArea
##


def test__largest_rectangle_in_histogram():
    tasks = [
        [2,1,5,6,2,3],           # 10
        [2,4],                   # 4
        [60,20,50,40,10,50,60],  # 100
    ]
    for heights in tasks:
        print("=======================================")
        print(f"Input: {heights}")
        res = largest_rectangle_in_histogram(heights)
        print(f"Result: {res}")
##

