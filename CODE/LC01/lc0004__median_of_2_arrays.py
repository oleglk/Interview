# lc0004__median_of_2_arrays.py
# Given two sorted arrays nums1 and nums2 of size n1 and n2 respectively, return the median of the two sorted arrays.

# Load:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0004__median_of_2_arrays import *

# RELOAD:
# import importlib; import lc0004__median_of_2_arrays; importlib.reload(lc0004__median_of_2_arrays); from lc0004__median_of_2_arrays import *

# The idea (INEFFICIENT): traverse the 2 arrays simultaneously until the needed index is reached.
# if n1+n2 is odd, targetIndex1 = targetIndex2 = (n1+n2) // 2 - 1
# if n1+n2 is even, targetIndex1 = (n1+n2) // 2, targetIndex2 = targetIndex1 + 1

def median_of_2_arrays(nums1: list[int], nums2: list[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    n  = n1 + n2
    if ( n == 0 ):
        return(0)
    if ( n == 1 ):
        return(nums1[0] if (n1 > 0) else nums2[0])

    # median == (*targetIndex1 + *targetIndex2) / 2
    # odd: 3//2=1;  even: 4//2-1=1
    targetIndex1 = n//2 if (n % 2 != 0) else n//2 - 1  # index of 1st median
    # targetIndex2 = targetIndex1 if (n % 2 != 0) else targetIndex1 + 1

    # browse the arrays counting to 'targetIndex1', then take one next element
    i = i1 = i2 = -1
    while (i < targetIndex1):
        i1, i2, nextElem = pick_next(nums1, nums2, i1, i2)
        if ( nextElem is None ):
            raise Exception("Unexpected end while searching for median-1")
        i += 1
    median1 = nextElem  # since i == targetIndex1
    if ( n % 2 == 0 ):  # even total count - take one next element for 2nd median
        i1, i2, median2 = pick_next(nums1, nums2, i1, i2)
        if ( median2 is None ):
            raise Exception("Unexpected end while taking median-2")
    else:               # odd total count - 2nd median is dummy 
        median2 = median1

    return (median1 + median2) / 2.0


def pick_next(arr1, arr2, i1, i2):
    """Chooses next min element of two arrays starting from after i1, i2.
       Returns ((updated)i1, (updated)i2, nextElem). At end nextElem=None."""
    n1 = len(arr1)
    n2 = len(arr2)
    if ( (i1 < -1) or (i2 < -1) or (i1 >=n1) or (i2 >= n2) ):
        raise Exception(f"pick_next(..., {i1}, {i2})")

    arr1Ends = (i1+1) >= n1;    arr2Ends = (i2+1) >= n2
    if ( (not arr1Ends) and (not arr2Ends) ):  # choose min from 2 arrays
        if ( arr1[i1+1] <= arr2[i2+1] ):
            i1 += 1
            nextElem = arr1[i1]
        else:
            i2 += 1
            nextElem = arr2[i2]
    elif ( (not arr1Ends) and (arr2Ends) ):  # pick from arr1
        i1 += 1
        nextElem = arr1[i1]
    elif ( (arr1Ends) and (not arr2Ends) ):  # pick from arr2
        i2 += 1
        nextElem = arr2[i2]
    else:  # both arrays end
        nextElem = None

    return (i1, i2, nextElem)
##


def test__median_of_2_arrays():
    tasks = [ [[0],[1]], [[2,4,6],[3,5,10]], [[1,3],[2]], [[1,3,9],[2,7]] ]
    #           0.5        4.5                 2.0          3.0
    for arr1, arr2 in tasks:
        print("=======================")
        print(f"Input: {arr1} and {arr2}")
        res = median_of_2_arrays(arr1, arr2)
        print(f"Result: {res}")
