# lc0031__next_permutation.py
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
# Given an array of integers nums, find the next permutation of nums.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0031__next_permutation import *

# RELOAD:
# import importlib; import lc0031__next_permutation; importlib.reload(lc0031__next_permutation); from lc0031__next_permutation import *

## 12345 ->()-> 12354 ->(12453)-> 12435
## 123456 ->()-> 123465 ->(123564)-> 123546
## 1247653 ->(1257643)-> 1253467
## 1237654 ->(1247653)-> 1243567
# The idea:
# 1) Find the rightmost digit that's smaller than successor -> nums[i]; all positions to the right of #i form descending suffix. If no such position, i=-1 and whole sequence is descending.
# 2) Find the rightmost digit that's larger than nums[i] -> nums[j]
# 3) Swap nums[i] and nums[j].
# (All positions to the right of #i still form descending suffix, ?)
# 4) Reverse order of i+1...end to convert descending suffix into ascending suffix. 
