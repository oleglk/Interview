# longest_consecutive.py - Given an array of integers, find the length of the longest subsequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from longest_consecutive import *

# RELOAD:
# import importlib; import longest_consecutive; importlib.reload(longest_consecutive); from longest_consecutive import *


# The idea: make a set of numbers in array; verify subsequences starting from each number whose predecessor is absent.


def longest_consecutive(arr: list[int]) -> int:
    # create a set with all element of 'arr'
    st = set()
    for val in arr:
        st.add(val)

    maxCnt = 0   # length of the longest so far subsequence
    currCnt = 0  # length of the currently checked subsequence
    # elements that start subsequences are those whose predecessors are absent
    for val in arr:
        if ( (val in st) and ((val-1) not in st) ):  # 'val' can be a start
            # check for subsequence that starts from 'val'
            currCnt = 0
            curr = val
            while ( curr in st ):
                currCnt += 1
                st.remove(curr)  # remove to avoid recomputation
                curr += 1  # go to next value
            # subsequence stopped - check its length
            maxCnt = max(maxCnt, currCnt)
            currCnt = 0

    return maxCnt


def test__longest_consecutive():
    tasks = [
        [],              # 0
        [1],             # 1
        [1,2,3],         # 3
        [2,6,1,9,4,5,3], # 6
        [1,1,1,2,2,3],   # 3
        [100,4,200,1,3,2]# 4
    ]
    for arr in tasks:
        print("====================================")
        print(f"Input: {arr}")
        res = longest_consecutive(arr)
        print(f"Result: {res}")
