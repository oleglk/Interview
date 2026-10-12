# lc0167__two_sum_2_input_array_sorted.py
# You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.
# Find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] of length 2.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0167__two_sum_2_input_array_sorted import *

# RELOAD:
# import importlib;    import lc0167__two_sum_2_input_array_sorted;  importlib.reload(lc0167__two_sum_2_input_array_sorted);  from lc0167__two_sum_2_input_array_sorted import *

# The idea: run two indices from the two sides of the array. Check sum = numbers[left] + numbers[right]. If sum == target, finished; if sum < target, move 'left' rightwards; if sum > target, move 'right' leftwards.
# See: https://www.geeksforgeeks.org/dsa/pair-with-given-sum-in-sorted-array-two-sum-ii/


def two_sum_2_input_array_sorted(numbers: list[int], target: int) -> tuple[int, int]:
    if ( len(numbers) < 2 ):  return (-1, -1)
    left = 0;  right = len(numbers) - 1
    while ( left < right ):
        sum = numbers[left] + numbers[right]
        if ( sum == target ):
            return (left+1, right+1)  # 1-indexed
        elif ( sum < target ):
            left += 1
        elif ( sum > target ):
            right -= 1
    return (-1, -1)  # no suitable numbers found
##


def test__two_sum_2_input_array_sorted():
    tasks = [
        [[2,7,11,15], 9],  # [1,2]
        [[2,3,4], 6],      # [1,3]
        [[-1,0], -1],      # [1,2]
    ]
    for numbers, target in tasks:
        print("==================================")
        print(f"Input: {numbers}, {target}")
        res = two_sum_2_input_array_sorted(numbers, target)
        print(f"Result: {res}")
##
