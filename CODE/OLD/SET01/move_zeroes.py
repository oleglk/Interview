# move_zeroes.py - Given an array nums, move all 0's to the end while maintaining the relative order of non-zero elements. Do this in-place.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from move_zeroes import *

# RELOAD:
# import importlib;    import move_zeroes;  importlib.reload(move_zeroes);  from move_zeroes import *


# The idea: collect non-0s on the left. 'i' is the right boundary of non-0s
## Example:  1020304; need to obtain 1234000
## 1020304 i=0, j=0: (1) - exchange with i=0 (itself) => 1020304
## 1020304 i=0, j=1: (0) - continue
## 1020304 i=0, j=2: (2) - i=i+1, exchange with i=1 => 1200304
## 1200304 i=1, j=3: (0) - continue
## 1200304 i=1, j=4: (3) - i=i+1, exchange with i=2 => 1230004
## 1230004 i=2, j=5: (0) - continue
## 1230004 i=2, j=6: (4) - i=i+1, exchange with i=3 => 1234000


def move_zeroes(arr: list) -> list:
    inz = -1  # to the left of it are known non-0s
    for j in range(0, len(arr)):
        if ( arr[j] == 0 ):
            continue
        # exchange non-0 element with [i+1]
        inz += 1  # move the boundary of known non-0s
        print(f"@@ {arr}:  Exchange #{j} with #{inz}")
        tmp = arr[inz]
        arr[inz] = arr[j]
        arr[j] = tmp
    return(arr)


def test__move_zeroes():
    arr1 = [1,0,2,0,3,0,4]
    arr2 = []
    arr3 = [0]
    arr4 = [1]
    arr5 = [0,0,1,2]
    arr6 = [1,2,0,0]
    arr7 = [0,1,0,0,2,0,3,0,0,4,0]
    for arr in [arr1, arr2, arr3, arr4, arr5, arr6, arr7]:
        print("==========================")
        print(f"Input:  {arr}")
        res = move_zeroes(arr)
        print(f"Output: {res}")
