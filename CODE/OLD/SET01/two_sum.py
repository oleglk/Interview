# two_sum.py
# Given an array of integers and a target number, return indices of two numbers adding up to the target.

# import os;  import sys;  sys.path.append(os.getcwd())

def two_sum(arr, target):
    complements = {}
    for i, num in enumerate(arr):
        complements[target - num] = i
    for i, num in enumerate(arr):
        if ( num in complements ):
            return([i, complements[num]])
    return(None)


def test__two_sum():
    arr1 = [1,2,3,4,5];  targ1 = 8
    arr2 = [10,11,12];  targ2 = 100
    print(f"{arr1} target={targ1} ==> {two_sum(arr1, targ1)}")
    print(f"{arr2} target={targ2} ==> {two_sum(arr2, targ2)}")

#################################################################################
test__two_sum()
