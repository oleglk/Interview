# product_of_array_except_self.py - Return an array where each element at index i is the product of all other elements in the input array, without using division and in O(n) time.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from product_of_array_except_self import *

# RELOAD:
# import importlib; import product_of_array_except_self; importlib.reload(product_of_array_except_self); from product_of_array_except_self import *

# The idea: first build array of prefixes - products before [i], then combine with running suffix (products after [i]).


def product_of_array_except_self(arr: list) -> list:
    if ( (len(arr) == 0) or (len(arr) == 1) ):
        return([1])
    # compute array of prefixes
    prefix = [1]*len(arr)
    prefix[0] = 1
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] * arr[i-1]
        
    # compute the results using prefixes and running suffix
    res = [1]*(len(arr))
    suffix = 1
    for i in range(len(arr)-1, -1, -1):
        res[i] = prefix[i] * suffix
        suffix = suffix * arr[i]

    return(res)
        

def test__product_of_array_except_self():
    arr1 = [1, 2, 3]          # Output: [6, 3, 1]
    arr2 = [10, 3, 5, 6, 2]   # Output: [180, 600, 360, 300, 900]
    arr3 = [12, 0]            # Output: [0, 12]
    arr4 = [1, 2, 3, 4]       # Output: [24,12,8,6]
    arr5 = [-1, 1, 0, -3, 3]  # Output: [0,0,9,0,0]
    for arr in [arr1, arr2, arr3, arr4, arr5]:
        print("=========================")
        print(f"Input:  {arr}")
        res = product_of_array_except_self(arr)
        print(f"Output: {res}")
