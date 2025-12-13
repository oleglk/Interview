# median_of_two_sorted_arrays.py - Given two sorted arrays, find median of their union.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from median_of_two_sorted_arrays import *

# RELOAD:
# import importlib; import median_of_two_sorted_arrays; importlib.reload(median_of_two_sorted_arrays); from median_of_two_sorted_arrays import *


def median_of_two_sorted_arrays(arr1: list, arr2: list) -> int:
    n1 = len(arr1)
    n2 = len(arr2)
    n  = n1 + n2
    if ( n == 0 ):
        return(0)
    if ( n == 1 ):
        return(arr1[0] if (n1 > 0) else arr2[0])
    
    # determine indices of middle elements so that median = (j1+j2)/2
    if ( (n % 2) == 0 ):  # 0123->1,2; 012345->2,3
        midIdx1 = (n // 2) - 1
        midIdx2 = n // 2
    else:                 # 012->1,1; 01234->2,2
        midIdx1 = midIdx2 = (n // 2)

    # browse the arrays counting to 'midIdx1', then take one next element
    i = i1 = i2 = -1
    while (i < midIdx1):
        i1, i2, med1 = pick_next(arr1, arr2, i1, i2)
        if ( med1 is None ):
            raise Exception(f"Unexpected end for med1 at {i1}, {i2}:")
        i += 1
    # 'med1' taken from 'midIdx1', choose 'med2'
    if ( (n % 2) == 0 ):  # for even n take next element for median-2
        i1, i2, med2 = pick_next(arr1, arr2, i1, i2)
        if ( med2 is None ):
            raise Exception(f"Unexpected end for med2 at {i1}, {i2}:")
    else:                 # for odd n pseudo-med2 == med1
        med2 = med1

    median = (med1 + med2) / 2.0
    return(median)


def pick_next(arr1, arr2, i1, i2):
    """Chooses next min element of two arrays.
       Returns (i1, i2, nextElem). At end nextElem=None."""
    n1 = len(arr1)
    n2 = len(arr2)
    if ( (i1 < -1) or (i2 < -1) or (i1 >=n1) or (i2 >= n2) ):
        raise Exception(f"pick_next(..., {i1}, {i2})")
    
    if ( ((i1+1) < n1) and ((i2+1) < n2) ): # choose min of two next elements
        if ( arr1[i1+1] <= arr2[i2+1] ):
            nextElem = arr1[i1+1]
            i1 += 1
        else:
            nextElem = arr2[i2+1]
            i2 += 1
    elif ( ((i1+1) < n1) and ((i2+1) == n2) ):  # pick element from 'arr1'
        nextElem = arr1[i1+1]
        i1 += 1
    elif ( ((i1+1) == n1) and ((i2+1) < n2) ):  # pick element from 'arr2'
        nextElem = arr2[i2+1]
        i2 += 1
    else:
        nextElem = None
    return(i1, i2, nextElem)


def test__median_of_two_sorted_arrays():
    tasks = [ [[0],[1]], [[2,4,6],[3,5,10]], [[1,3],[2]], [[1,3,9],[2,7]] ]
    #           0.5        4.5                 2.0          3.0
    for arr1, arr2 in tasks:
        print("=======================")
        print(f"Input: {arr1} and {arr2}")
        res = median_of_two_sorted_arrays(arr1, arr2)
        print(f"Result: {res}")
        
