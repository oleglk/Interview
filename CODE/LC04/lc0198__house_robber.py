# lc0198__house_robber.py
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0198__house_robber import *

# RELOAD:
# import importlib;    import lc0198__house_robber;  importlib.reload(lc0198__house_robber);  from lc0198__house_robber import *


# The idea: dynamic programming bottom-up. dp[i] = max(dp[i-1], dp[i-2] + nums[i]) .
# See: https://levelup.gitconnected.com/solving-the-house-robber-leetcode-problem-1d34df04ea20


def house_robber(nums: int) -> int:
    n = len(nums)
    dp = [0] * n # dp[i] == max robbed sum for houses 0..i
    
    if ( n == 0 ):  return 0
    if ( n == 1 ):  return nums[0]
    if ( n == 2 ):  return max(nums[0], nums[1])
    
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        # take max btw not robbing and robbing house #i
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[n-1]
##


def test__house_robber():
    tasks = [
        [1,2,3,1],   # 4
        [2,7,9,3,1], # 12
    ]
    for nums in tasks:
        print("======================================")
        print(f"Input: {nums}")
        res = house_robber(nums)
        print(f"Result: {res}")
##
