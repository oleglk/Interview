# rotate_array.py - Rotate an array of n elements to the right by k steps, where k is non-negative.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from rotate_array import *

# RELOAD:
# import importlib;    import rotate_array;  importlib.reload(rotate_array);  from rotate_array import *

## 123456 -> (1) 612345 -> (2) 561234 -> (3) 456123 -> ...

# The idea: combine 2 slices
## Input 123456, 2 => Desired output: 561234
## (1) new 1st slice: k last members: n-k...n-1 inclusive -> 56
## (2) new 2nd slice: n-k first members: 0...n-k-1 -> 1234


def rotate_array(arr: list, k: int) -> list:
    n = len(arr)
    k %= n  # normalize the problem
    if ( (n < 2) or (k < 1) ):
        return arr
    arr = arr[n-k:] + arr[:n-k]
    return arr


def test__rotate_array():
    arr1 = [1,2,3,4,5,6]
    arr2 = [1,2]
    arr3 = [1,2,3,4,5,6,7]
    k1 = 2
    k2 = 5
    for arr in [arr1, arr2, arr3]:
        for k in [k1, k2]:
            print("=====================")
            print(f"Input: arr={arr}, k={k}")
            res = rotate_array(arr, k)
            print(f"Output:    {res}")
