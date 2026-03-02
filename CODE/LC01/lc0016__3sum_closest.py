# lc0016__3sum_closest.py
# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0016__3sum_closest import *

# RELOAD:
# import importlib; import lc0016__3sum_closest; importlib.reload(lc0016__3sum_closest); from lc0016__3sum_closest import *

# The idea: work on the sorted array; at each iteration fix the 1st index and move the other two according to whether the current sum is smaller or larger than the target. (2nd index goes over smaller boundary, 3rd - over larger.)
# See: https://algo.monster/liteproblems/16

def three_sum_closest(nums: list[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    minDiff = float('inf')  # for minimal diff seen so far
    bestSum = 0

    # at each iteration fix the 1st index and choose the other two
    for i in range(0, n-2):  # i is the fixed leftmost index
        j = i + 1
        k = n - 1
        while ( j < k ):
            sum = nums[i] + nums[j] + nums[k]
            diff = abs(target - sum)
            if (sum == target):  # diff == 0
                return sum  # found exact match
            if ( diff < minDiff ):
                minDiff = diff  # update the minimal diff seen so far
                bestSum = sum   # update the closest sum seen so far
            if ( sum < target ):
                j += 1  # move left pointer to larger number
            else:  # (sum > target)
                k -= 1  # move right pointer to smaller number
    return bestSum


def test__three_sum_closest():
    tasks = [
        [[-1, 2, 1, -4],  1],  # 2
        [[0, 0, 0],  1],       # 0
        [[-1, 2, 2, 4],  4],   # 5
        [[1, 10, 4, 5],  10],  # 10
    ]
    for  nums, target  in tasks:
        print("====================================")
        print(f"Input: {nums}, target={target}")
        res = three_sum_closest(nums, target)
        print(f"Result: {res}")

        
