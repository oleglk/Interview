# lc0015__3sum.py
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0015__3sum import *

# RELOAD:
# import importlib; import lc0015__3sum; importlib.reload(lc0015__3sum); from lc0015__3sum import *

# The idea: dict {num :: [list of indices]} for (target) 3rd numbers, checking sums of all combination of 2 indices vs existent targets.


class ThreeSum:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.targetDict = ThreeSum.build_targets_dict(self.nums)
    ##


    @staticmethod
    def build_targets_dict(nums: list[int]) -> dict[int, list[int]]:
        """Builds and returns numbers from 'nums' mapped to list of their occurence indices."""
        res = {}
        for  i, num  in enumerate(nums):
            if ( num not in res ):
                res[num] = [i]
            else:
                res[num].append(i)
        return res
    ##


    def find_target_appearance_for_indices(self, i:int, j:int) -> bool:
        """Returns True if (-nums[i]-nums[j]) appears in 'targetDict'
        at index other than 'i' and 'j'."""
        if ( (i < 0) or (i >= len(self.nums)) or
             (j < 0) or (j >= len(self.nums)) ):
            raise Exception(f"Index ({i}, {j}) out of range")
        target = -self.nums[i] - self.nums[j]
        if ( target not in self.targetDict ):
            return False  # 'target' doesn't appear at all
        for idx in self.targetDict[target]:  # browse appearances of 'target'
            if ( (idx != i) and (idx != j) ):
                return True  # nums[i]+nums[j]+nums[idx] = 0
        return False  # 'target' appears only at 'i' or 'j'
    ##

    
    def find_zero_sum_triplets(self):
        """Finds and returns all unique triplets summing to zero."""
        res = set()  # will hold sorted triplet-tuples
        # check all pairs of indices
        for i in range(0, len(self.nums)):
            for j in range(i+1, len(self.nums)):
                target = -self.nums[i] - self.nums[j]
                if ( self.find_target_appearance_for_indices(i, j) ):
                    res.add(tuple(sorted((self.nums[i], self.nums[j], target))) )
        return res
    ##
####


def test__ThreeSum():
    tasks = [
        [-1,0,1,2,-1,-4],  # [-1,-1,2],[-1,0,1]
        [0,1,1],           # []
        [0,0,0],           # [0,0,0]
        [0,-1,2,-3,1],     # [0,-1,1], [2,-3,1]
        [2,3,1,0,5]        # []
    ]
    for nums in tasks:
        print("================================")
        print(f"Input: {nums}")
        obj = ThreeSum(nums)
        res = obj.find_zero_sum_triplets()
        print(f"Result: {res}")
