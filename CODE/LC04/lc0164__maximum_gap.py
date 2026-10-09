# lc0164__maximum_gap.py
# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
# You must write an algorithm that runs in linear time and uses linear extra space.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0164__maximum_gap import *

# RELOAD:
# import importlib;    import lc0164__maximum_gap;  importlib.reload(lc0164__maximum_gap);  from lc0164__maximum_gap import *

# The idea: spread array elements into buckets of size average gap, which should be smaller than max gap; max gap will be between consecutive populated buckets. In each bucket track only min and max values.
# See: https://www.jointaro.com/interviews/questions/maximum-gap/
#  and
#      https://dev.to/seanpgallivan/solution-maximum-gap-212k


def maximum_gap(nums: list[int]) -> int:
    n = len(nums)
    if ( n <= 1 ):  return 0
    if ( n == 2 ):  return abs(nums[0] - nums[1])

    minVal = min(nums)
    maxVal = max(nums)
    if ( minVal == maxVal ):  return 0
    # set bucket size to average gap, which should be smaller than max gap
    bucketSize = (maxVal - minVal) // (n - 1)  # for [1,3,5] want bucketSize=2
    bucketsNum = (maxVal - minVal) // bucketSize + 1  # for [1,3,5] want =3
    #print(f"bucketSize={bucketSize}, bucketsNum={bucketsNum}")

    minInBucketList = [float('inf')] * bucketsNum
    maxInBucketList = [float('-inf')] * bucketsNum

    # "distribute" into buckets by computing min and max
    for val in nums:
        bucketI = (val - minVal) // bucketSize
        #print(f"val={val} goes into bucket {bucketI}")
        minInBucketList[bucketI] = min(minInBucketList[bucketI], val)
        maxInBucketList[bucketI] = max(maxInBucketList[bucketI], val)

    # just in case - find max gap inside buckets
    maxGap = float('-inf')
    for bucketI in range(0, bucketsNum):
        maxGap = max(maxGap, maxInBucketList[bucketI] - minInBucketList[bucketI])

    # find max gap between consecutive populated buckets
    #      - between prev max and next min
    prevMax = maxInBucketList[0]  # 1st bucket always populated (by minVal)
    for bucketI in range(1, bucketsNum):
        if ( minInBucketList[bucketI] == float('inf') ):  # non-populated bucket
            continue
        maxGap = max(maxGap, minInBucketList[bucketI] - prevMax)
        prevMax = maxInBucketList[bucketI]

    return maxGap
##

        
def test__maximum_gap():
    tasks = [
        [3,6,9,1],  # 3
        [10],       # 0
        [8,3,1],    # 5
    ]
    for nums in tasks:
        print("==============================================")
        print(f"Input: {nums}")
        res = maximum_gap(nums)
        print(f"Result: {res}")
##
