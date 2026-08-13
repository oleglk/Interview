# lc0134__gas_station.py
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0134__gas_station import *

# RELOAD:
# import importlib;    import lc0134__gas_station;  importlib.reload(lc0134__gas_station);  from lc0134__gas_station import *

# The idea: perform up to 2 complete tours to verify the solution. When gas drops below 0, start over from the next station - the whole stretch [old_start...current] is unusable to start from: if we cannot complete the tour with some remaining fuel when starting from stations [old_start...current], we cannot do it without remaining fuel either. If size([start...current]) grows to n, we found the solution.
# See: https://algo.monster/liteproblems/134


def gas_station(gas: list[int], cost: list[int]) -> int:
    if ( (gas is None) or (cost is None) or (len(gas) != len(cost)) ):
         print("Invalid inputs")
         return -1
    n = len(gas)
    startIdx = None
    remaining = 0
    currIdx = 0

    # perform up to 2 full cycles
    while ( currIdx < 2*n ):
        if ( startIdx is None ):
            startIdx = currIdx  # start over

        remaining += gas[currIdx % n] - cost[currIdx % n]
        if ( remaining < 0 ):  # cannot reach past station #currIdx
            # cannot start from any of [startIdx...currIdx]
            remaining = 0
            startIdx = None  # command to start over from the next station

        # advance current station:
        # - either we can reach the next, or we are starting over from the next
        currIdx += 1

        # check if we completed full cycle
        if ( (startIdx is not None) and ((currIdx - startIdx) == n) ):
            return (startIdx % n)

    return -1
##


def test__gas_station():
    tasks = [
        [[1,2,3,4,5], [3,4,5,1,2]],  # 3
        [[2,3,4], [3,4,3]],          # -1
    ]
    for gas, cost in tasks:
        print("==============================================")
        print(f"InputL gas={gas}, cost={cost}")
        res = gas_station(gas, cost)
        print(f"Result: {res}")
##
