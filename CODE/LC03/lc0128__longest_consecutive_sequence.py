# lc0128__longest_consecutive_sequence.py
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
## Example:
## Input: [100, 4, 200, 1, 3, 2]   Output: 4
## Explanation: The longest consecutive sequence is [1, 2, 3, 4].

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0128__longest_consecutive_sequence import *

# RELOAD:
# import importlib;    import lc0128__longest_consecutive_sequence;  importlib.reload(lc0128__longest_consecutive_sequence);  from lc0128__longest_consecutive_sequence import *

# The idea: use set of numbers for easier lookup; try starting sequences from all numbers that have no predecessors.
# See https://medium.com/@niharikofficial/cracking-the-longest-consecutive-sequence-problem-in-o-n-the-ultimate-guide-9fa2ba188afe


def longest_consecutive_sequence(nums: list[int]) -> int:
    numsSet = set(nums)
    result = 0

    # look for numbers without predecessor
    for x in nums:
        if (x-1) in numsSet:  # x cannot start a consecutive sequence
            continue
        # x starts a consecutive sequence
        cnt = 1
        while (x+1) in numsSet:
            cnt += 1
            x += 1
        result = max(result, cnt)

    return result
##
### Why it runs in O(N):
### Building the set takes O(n). Although there is a nested while loop, each number is only visited at most twice across the entire execution (once during the outer loop, and once inside the while loop).


def test__longest_consecutive_sequence():
    tasks = [
        [100,4,200,1,3,2],      # 4
        [0,3,7,2,5,8,4,6,0,1],  # 9
    ]
    for nums in tasks:
        print("======================================================")
        print(f"Input: {nums}")
        res = longest_consecutive_sequence(nums)
        print(f"Result: {res}")
##
