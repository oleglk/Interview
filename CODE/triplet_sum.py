# triplet_sum.py - Given an array nums of n integers, return all unique triplets [nums[i], nums[j], nums[k]] such that they sum to zero.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from triplet_sum import *

# RELOAD:
# import importlib; import triplet_sum; importlib.reload(triplet_sum); from triplet_sum import *

# The idea: maintain map {value :: [list of occurence indices]}; traverse all pairs of unique indices and if complementing value exists in the map, add to the answer triple for first suitable index listed in the map.


def triplet_sum(arr: list) -> list:
    n = len(arr)
    res = set();  # for resulting array of triples
    # build the map of value occurences
    map = {}
    for i, v  in enumerate(arr):
        if ( v not in map ):
            map[v] = []
        map[v].append(i)

    # traverse pairs of unique indices, look for complements
    for i in range(0, n):
        for j in range(i+1, n):
            s2 = arr[i] + arr[j]
            if ( -s2 in map ):
                for k in map[-s2]:
                    if ( (k != i) and (k != j) ):
                        #print(f"@@ Pick #{i},{j},{k} == {arr[i]},{arr[j]},{arr[k]}")
                        comb = tuple(sorted([arr[i], arr[j], arr[k]]))
                        res.add(comb)
    return(res)
                        

def test__triplet_sum():
    tasks = [[1,2,-3],  [-1,0,1,2,-1,-4],   [0,1,1],  [0,0,0],  [1,4,2,0,-5,5]]
    #        [1,2,-3]  [[-1,-1,2],[-1,0,1]]   []      [0,0,0] [-5,1,4],[-5,0,5]
    for arr in tasks:
        print("===============================")
        print(f"Input: {arr}")
        res = triplet_sum(arr)
        print(f"Result: {res}")

