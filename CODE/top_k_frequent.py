# top_k_frequent.py - Given a non-empty array of integers, return the k most frequent elements.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from top_k_frequent import *

# RELOAD:
# import importlib;    import top_k_frequent;  importlib.reload(top_k_frequent);  from top_k_frequent import *

def top_k_frequent(arr: list, k: int) -> list:
    if ( k == 0 ):
        return([])
    freq = {}  # for frequences' counts
    # count frequences
    for x in arr:
        if ( x in freq ):
            freq[x] += 1
        else:
            freq[x] = 1
    # turn 'freq' into list of pairs
    listOfPairs = list(freq.items())
    listOfPairs.sort(key = lambda x: x[1], reverse=True)  # sort by frequences
    topK = [x[0] for x in listOfPairs[0:k]]
    return(topK)


def test__top_k_frequent():
    arrAndK = [ [[1,1,2,3], 2], [[1,2,2,3,3,3,4,4,4,4], 3], [[1,2,2], 1],
                [[1,2,3,4,5], 2] ]
    for arr, k  in arrAndK:
        print("=======================")
        print(f"arr={arr}, k={k}")
        res = top_k_frequent(arr, k)
        print(f"Result: {res}")
