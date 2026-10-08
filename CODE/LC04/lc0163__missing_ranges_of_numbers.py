# lc0163__missing_ranges_of_numbers.py
# You have an inclusive interval [lower, upper] and a sorted array of unique integers arr[], all of which lie within this interval. A number x is considered missing if x is in the range [lower, upper] but not present in arr. Your task is to return the smallest set of sorted ranges that includes all missing numbers, ensuring no element from arr is within any range, and every missing number is covered exactly once.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0163__missing_ranges_of_numbers import *

# RELOAD:
# import importlib;    import lc0163__missing_ranges_of_numbers;  importlib.reload(lc0163__missing_ranges_of_numbers);  from lc0163__missing_ranges_of_numbers import *

# The idea: if two cobsequent numbers differ by more than 1, there's a missing range between them.
# See: https://www.geeksforgeeks.org/dsa/missing-ranges-of-numbers/


def missing_ranges_of_numbers(arr: list[int], lower: int, upper: int) -> \
        list[list[int]]:
    if ( len(arr) == 0 ):
        return [[lower, upper]]
    missingRangesList = []
    # check lower boundary
    if ( lower < arr[0] ):
        missingRangesList.append( [lower, arr[0]-1] )
    # check internal ranges
    for i in range(0, len(arr)-1):
        if ( (arr[i+1] - arr[i]) > 1 ):
            missingRangesList.append( [arr[i]+1, arr[i+1]-1] )
    # check upper boundary
    if ( upper > arr[-1] ):
        missingRangesList.append( [arr[-1]+1, upper] )
    return missingRangesList
##

    
def test__missing_ranges_of_numbers():
    tasks = [
        [[14, 15, 20, 30, 31, 45], 10, 50],  # [[10, 13], [16, 19], [21, 29], [32, 44], [46, 50]]
        [[-48, -10, -6, -4, 0, 4, 17], -54, 17],  # [[-54, -49], [-47, -11], [-9, -7], [-5, -5], [-3, -1], [1, 3], [5,16]]
    ]
    for arr, lower, upper  in tasks:
        print("=============================================")
        print(f"Input: {arr}, lower={lower}, upper={upper}")
        res = missing_ranges_of_numbers(arr, lower, upper)
        print(f"Result: {res}")
##
