# binary_search.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from binary_search import *

# RELOAD:
# import importlib;    import binary_search;  importlib.reload(binary_search);  from binary_search import *


def binary_search(arr: list, val: int):
    """Return index of 'val' in sorted 'arr' or -1 if not found."""
    if ( not arr ):
        return(-1)
    lo = 0           # current bottom index
    hi = len(arr) -1 # current top index

    while ( hi >= lo ):
        med = (lo + hi)//2
        if ( arr[med] == val ):
            return(med)  # found at index #med
        elif ( arr[med] < val ):
            lo = med + 1  # continue searching in upper half
        else:
            hi = med - 1  # continue searching in lower half
    return(-1)  # not found


def test__binary_search():
    arr1 = [1,3,5,7]
    arr2 = [8,10]
    arr3 = [1,2,3,7,8]
    v1 = 3
    v2 = 8
    for arr in [arr1, arr2, arr3]:
        for v in [v1, v2]:
            print("==========================")
            print(f"Array={arr},  val={v}")
            i = binary_search(arr, v)
            print(f"Resulting index: {i}")
