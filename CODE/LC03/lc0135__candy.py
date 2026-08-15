# lc0135__candy.py
# You have n children standing in a line, and each child has a rating value given in an array called ratings.
# You need to distribute candies to these children following these rules:
#    Every child must receive at least one candy
#    If a child has a higher rating than their neighbor (the child directly to their left or right), they must receive more candies than that neighbor
# Your task is to find the minimum total number of candies needed to satisfy both requirements.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0135__candy import *

# RELOAD:
# import importlib;    import lc0135__candy;  importlib.reload(lc0135__candy);  from lc0135__candy import *

# The idea init arrays fromLeft and fromRight to all 1-s. Pass left-to-right on fromLeft and right-to-left on fromRight and set if rating[curr] > rating[prev], then from*[curr] = from*[prev] + 1. Then take max of the two (fromLeft, fromRight) for each child.
# See: https://algo.monster/liteproblems/135


def distribute_candies(rating: list[int]) -> int:
    n = len(rating)
    fromLeft = [1]*n
    fromRight = [1]*n

    # left-to-right pass
    for i in range(1, n):
        if ( rating[i] > rating[i-1] ):
            fromLeft[i] = fromLeft[i-1] + 1

    # right-to-left pass
    for i in range(n-2, -1, -1):
        if ( rating[i] > rating[i+1] ):
            fromRight[i] = fromRight[i+1] + 1

    # take max of fromLeft, fromRight for each child
    candyCounts = (max(leftCount, rightCount) \
                   for leftCount, rightCount in zip(fromLeft, fromRight))
    return sum(candyCounts)
##


def test__distribute_candies():
    tasks = [
        [1,0,2],  # 5
        [1,2,2],  # 4
    ]
    for rating in tasks:
        print("=======================================")
        print(f"Input: {rating}")
        res = distribute_candies(rating)
        print(f"Result: {res}")
##
