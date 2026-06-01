# lc0085__maximal_rectangle.py
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0085__maximal_rectangle import *

# RELOAD:
# import importlib; import lc0085__maximal_rectangle; importlib.reload(lc0085__maximal_rectangle); from lc0085__maximal_rectangle import *

# The idea: bring this problem to lc0084__largest_rectangle_in_histogram.
# Grow the rectangles starting from upper row downwards: if value in the matrix is 1, add 1 to column height; if value is 0, reset column height to zero.
# Example:
# 0111  -> heights = (0,1,1,1) -> solve for 1 row
# 0011  -> heights = (0,0,2,2) -> solve for 2 rows
# 0011  -> heights = (0,0,3,3) -> solve for 3 rows
# See https://algo.monster/liteproblems/85


# Builds histograms and calls largest_rectangle_in_histogram() on each
def maximal_rectangle(mat: list[list[int]]) -> int:
    n = len(mat)
    if ( n == 0 ):  return 0
    m = len(mat[0])
    if ( m == 0 ):  return 0
    heights = [0]*m  # will accumulate the histogram
    maxArea = -1
    for row in range(0, n):
        # include 'row' in the histogram
        for col, val in enumerate(mat[row]):
            if ( val == 1 ):
                heights[col] += 1
            else:
                heights[col] = 0
        # solve for the currently obtained histogram
        maxArea = max(maxArea, largest_rectangle_in_histogram(heights))
    return maxArea
##


######## Solution of largest-rectangle-in-histogram problem #####################
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
#################################################################################

def test__maximal_rectangle():
    tasks = [
        [[1,0,1,0,0], [1,0,1,1,1], [1,1,1,1,1], [1,0,0,1,0]],  # 6
        [[0]],                                                 # 0
        [[1]],                                                 # 1
        [[0,1,1,1], [0,0,1,1], [0,0,1,1]],                     # 6
    ]
    for mat in tasks:
        print("=============================================")
        print(f"Input: {mat}")
        res = maximal_rectangle(mat)
        print(f"Result: {res}")
##
