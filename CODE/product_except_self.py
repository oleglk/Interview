# product_except_self.py - Given an array nums of n integers where n > 1, return an array output such that output[i] is the product of all the elements of nums except nums[i]. Solve without division and in O(n).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from product_except_self import *

# RELOAD:
# import importlib;    import product_except_self;  importlib.reload(product_except_self);  from product_except_self import *


# The idea: first build array of products-to-the-left of each index,
#           then, going from right, multiply by running product-to-the-right

def product_except_self(arr: list) -> int:
    """Returns array of producta of all array elements except the ones at correspondent index."""
    res = [1] * len(arr)
    leftProd = [1] * len(arr)
    fromRight = 1
    leftProd[0] = 1
    leftProd[1] = arr[0]
    # go from left and calc products-to-the-left
    for i in range(1, len(arr)-1):
        leftProd[i+1] = leftProd[i] * arr[i]
    print(f"Products-to-the-left: {leftProd}")
    # go from right and multiply products-to-the-left by running product-to-the-right
    for i in range(len(arr)-1, -1, -1):
        print(f"res[{i}] = {leftProd[i]} * {fromRight}")
        res[i] = leftProd[i] * fromRight
        fromRight *= arr[i]
    return(res)
        

def test__product_except_self():
    arr1 = [1, 2, 3]  # Output: [6, 3, 1]
    arr2 = [10, 3, 5, 6, 2]  # Output: [180, 600, 360, 300, 900]
    arr3 = [12, 0]  # Output: [0, 12]
    for arr in [arr1, arr2, arr3]:
        print("=========================")
        print(f"Input:  {arr}")
        res = product_except_self(arr)
        print(f"Output: {res}")
