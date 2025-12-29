# find_duplicate_number.py - Find duplicate in n+1 numbers without modifying array using Floyd's cycle detection.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from find_duplicate_number import *

# RELOAD:
# import importlib; import find_duplicate_number; importlib.reload(find_duplicate_number); from find_duplicate_number import *


# The idea: treat array of numbers as linked list where next = num[i].
# Phase 1: use fast and slow pointers to find intersection - some meeting point inside the cycle.
#          It could be mathematically proven that (forward) distance from the meeting point to the cycle entrance equals distance from start to the cycle entrance.
# Phase 2: Move 2 pointers at the same speed - one from start, other from phase-1-meeting-point; they must meet at the cycle entrance which is the duplicated element.

# ========= Walkthrough_1: ==========
#  0 1 2 3 4
# [3 1 3 4 2]
# 0-3>4>2>3>4>2>3>4...
# (1)
# t=0:3 h=0:3:4
# t=3:4 h=4:2:3
# t=4:2 h=3:4:2 meet
# (2)
# t=0   h=2
# t=0:3 h=2:3 equal - 3 is duplicated
# ========== Walkthrough_2: ==========
#  0 1 2 3 4
# [1 3 4 2 2]
# 0-1>3>2>4>2>4>2...
# (1)
# t=0:1 h=0:1:3
# t=1:3 h=3:2:4
# t=3:2 h=4:2:4
# t=2:4 h=4:2:4 meet
# (2)
# t=0 h=4
# t=0:1 h=4:2
# t=1:3 h=2:4
# t=3:2 h=4:2 equal - 2 is duplicated


def find_duplicate_number(arr: list[int]) -> int:
    # phase 1 - find the loop - different speed from same start position
    # the 1st phase finds _some_ position inside the loop
    tort = arr[0]  # "tortoise" slow pointer
    hare = arr[0]  # "hare" fast pointer
    while(True):
        # since values in arr are 1..n, we cannot jump out of range
        tort = arr[tort]  # 1 step
        hare = arr[arr[hare]]  # 2 steps
        if ( tort == hare ):
            break
    # phase 2 - find entrance to the loop - equal speed from different starts
    ptr1 = arr[0]
    ptr2 = hare
    while ( ptr1 != ptr2 ):
        ptr1 = arr[ptr1]
        ptr2 = arr[ptr2]
    return ptr1  # the pointers met at the duplicate number


def test__find_duplicate_number():
    tasks = [[3,1,3,4,2], [1,3,4,2,2]]
    for arr in tasks:
        print("==================================")
        print(f"Input: {arr}")
        res = find_duplicate_number(arr)
        print(f"Result: {res}")
