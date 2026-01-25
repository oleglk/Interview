# gas_station.py - Given two arrays gas[] and cost[], each gas station i provides gas[i] fuel, and it takes cost[i] fuel to travel to the next station. Starting with an empty tank, find the index of the gas station from which you can complete a full circular tour. If it’s not possible, return -1.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from gas_station import *

# RELOAD:
# import importlib; import gas_station; importlib.reload(gas_station); from gas_station import *


# The idea: start with empty tank at station 0. For each "hop" compute tank+gas-cost; if falls below zero upon reaching station #i, reset start to #i+1.
# The rationale of resetting to #i+1: if we cannot complete the tour with some remaining fuel when starting from stations [old-start, i], we cannot do it without remaining fuel either.
# The solution effectively "drops" all start options where tour is impossible.

def gas_station(gas: list[int], cost: list[int]) -> int:
    if ( sum(gas) < sum(cost) ):
        return -1  # cannot complete the tour
    # the tour is possible, need to find the starting point

    n = len(gas)
    remaining = 0
    startIdx = 0  # current starting station
    for i in range(0, n):
        remaining += gas[i] - cost[i] # how much would remain at next station
        if ( remaining < 0 ):
            # reset starting point to the next station,
            # since cannot start at any of [startIdx, i] (see the "rationale")
            remaining = 0
            startIdx = i + 1
    return startIdx


def test__gas_station():
    tasks = [
        [[1,2,3,4,5], [3,4,5,1,2]],  # 3
        [[2,3,4], [3,4,3]],          # -1
        [[4,5,7,4], [6,6,3,5]],      # 2
        [[3,9], [7,6]],              # -1
        [[5,2,0,3,3], [1,5,5,1,1]]   # 3
    ]
    for gas, cost  in tasks:
        print("=========================================")
        print(f"Input:  gas={gas}, cost={cost}")
        res = gas_station(gas, cost)
        print(f"Result: {res}")

