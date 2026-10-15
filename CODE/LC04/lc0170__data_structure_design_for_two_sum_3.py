# lc0170__data_structure_design_for_two_sum_3.py
# You have to design a data structure that accepts a stream of integers and then checks if it has a pair of integers that sum up to a particular value.
# Implement the TwoSum class:
#    TwoSum(): Initializes the TwoSum object, with an empty array initially.
#    void add(int number): Adds number to the data structure.
#    boolean find(int value): Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0170__data_structure_design_for_two_sum_3 import *

# RELOAD:
# import importlib;    import lc0170__data_structure_design_for_two_sum_3;  importlib.reload(lc0170__data_structure_design_for_two_sum_3);  from lc0170__data_structure_design_for_two_sum_3 import *

# The idea: store mapping of integer :: appearance-count. In find(), for each stored number lookup (target - number).
# See: https://www.geeksforgeeks.org/dsa/data-structure-design-for-two-sum-iii/


class DatastructForTwoSum():
    def __init__(self):
        self.seen = {}  # numbers seen so far
    ##


    def add(self, num: int) -> None:
        if ( num in self.seen ):
            self.seen[num] += 1
        else:
            self.seen[num] = 1
    ##


    def find(self, target: int) -> bool:
        for num in self.seen:
            complement = target - num
            if ( ((complement != num) and (complement in self.seen)) or \
                 ((complement == num) and (self.seen[num] > 1)) ):
                return True
        return False
    ##
####


def test__DatastructForTwoSum():
    tasks = [
        [[1,3,5], 4],   # True
        [[1,3,5], 7],   # False
    ]
    for nums, target in tasks:
        ds = DatastructForTwoSum()
        for num in nums:
            ds.add(num)
        print(f"nums={nums}, target={target}")
        res = ds.find(target)
        print(f"Result: {res}")
##
