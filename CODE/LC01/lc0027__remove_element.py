# lc0027__remove_element.py
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0027__remove_element import *

# RELOAD:
# import importlib; import lc0027__remove_element; importlib.reload(lc0027__remove_element); from lc0027__remove_element import *

# The idea: use 2 pointers: one is the insertion position for the next non-val element, other runs through the whole array in search for next non-val element.

def remove_element(arr: list[int], val: int) -> list[int]:
    if ( arr is None ):  return (None, 0)
    nextUniqInsert = 0
    for elem in arr:
        if ( elem != val ):
            arr[nextUniqInsert] = elem
            nextUniqInsert += 1
    return (arr, nextUniqInsert)
##


def test__remove_element():
    tasks = [
        [[1,2,3,4,5], 3],       # [1,2,4,5], k=4
        [[3,2,2,3], 3],         # [2,2,_,_], k=2
        [[0,1,2,2,3,0,4,2], 2], # [0,1,4,0,3,_,_,_], k=5
        [[3], 3]                # [_], k=0
    ]
    for arr, val  in  tasks:
        print("==============================")
        print(f"Input: {arr}, val={val}")
        resArr, k = remove_element(arr, val)
        print(f"Result: {resArr}, k={k}")
##

