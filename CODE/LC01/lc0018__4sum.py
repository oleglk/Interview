# lc0018__4sum.py
# Given an array nums of n integers and integer target, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# -    0 <= a, b, c, d < n
# -    a, b, c, and d are distinct.
# -    nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0018__4sum import *

# RELOAD:
# import importlib; import lc0018__4sum; importlib.reload(lc0018__4sum); from lc0018__4sum import *


# The idea: sort the array; in a nested loop fix two leftmost indices, play with remaining two (rightmost) indices using properties of sorted array.
# See: https://algo.monster/liteproblems/18


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()  # sort ascending
    print(f"@ Sorted-nums = {nums}")
    n = len(nums)
    res = []

    # traverse two leftmost indices while eliminating duplicates
    for i in range(0, n-3):
        if ( (i > 0) and (nums[i] == nums[i-1]) ):
            #print(f"@@ -skip duplicated i={i}: nums[i]={nums[i]}")
            continue  # skip duplicate at 1st index
        for j in range(i+1, n-2):
            if ( (j > (i+1)) and (nums[j] == nums[j-1]) ):
                #print(f"@@ -skip duplicated j={j}: nums[j]={nums[j]}")
                continue  # skip duplicate at 2nd index
            # traverse 2 rightmost indices starting from remaining range inwards
            k = j + 1
            l = n - 1
            while ( k < l ):
                currSum = nums[i] + nums[j] + nums[k] + nums[l]
                #print(f"@@ Check {nums[i]} + {nums[j]} + {nums[k]} + {nums[l]} = {currSum}")
                if ( currSum == target ):
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    # advance the two rightmost indices inwards
                    k += 1
                    l -= 1
                    # skip duplicates for the two rightmost indices
                    while ( (k < l) and (nums[k] == nums[k-1]) ):
                        print(f"@@ -skip duplicated k={k}: nums[k]={nums[k]}")
                        k += 1
                    while ( (k < l) and (nums[l] == nums[l+1]) ):
                        print(f"@@ -skip duplicated l={l}: nums[l]={nums[l]}")
                        l -= 1
                elif ( currSum < target ):
                    k += 1  # advance left rightmost index to increase the sum
                elif ( currSum > target ):
                    l -= 1  # advance right rightmost index to decrease the sum
    return res
##

def test__four_sum():
    tasks = [
        [[1,0,-1,0,-2,2], 0],  # [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
        [[2,2,2,2,2], 8],      # [[2,2,2,2]]
        [[10,2,3,4,5,7,8], 23],# [[2,3,8,10], [2,4,7,10], [3,5,7,8]]
        [[-1,0,0,1,2], 0]      # [[-1,0,0,1]]
    ]
    for nums, target  in tasks:
        print("==============================")
        print(f"Input: {nums}, target = {target}")
        res = four_sum(nums, target)
        print(f"Result: {res}")
##
