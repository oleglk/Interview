# find_anagrams.py - find all anagrams of 'pattern' in the input string - return list of start indices.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from find_anagrams import *

# RELOAD:
# import importlib; import find_anagrams; importlib.reload(find_anagrams); from find_anagrams import *


# The idea: use sliding window, frequency-dict for pattern, and running frequency-dict for the sliding window. Whenever the two dict-s are equal, anagram is found.

from collections import Counter

def find_anagrams(inpStr: str, pattern: str) -> list[int]:
    lS = len(inpStr)
    lP = len(pattern)
    if ( (lP > lS) or (lP == 0) or (lS == 0) ):
        return []
    res = []

    # make 'countsP' the counter for the pattern
    countsP = Counter()
    for i in range(0, lP):
        countsP[pattern[i]] += 1
    
    # init 'countsW' dict with the characters in the initial window
    countsW = Counter()
    for i in range(0, lP):
        countsW[inpStr[i]] += 1
    if ( countsW == countsP ):  # initial window is an anagram
        res.append(0)

    # main loop - slide the window, update counts, then check for match
    for winStartIdx in range(1, lS-lP+1):
        winEndIdx = winStartIdx + lP - 1
        countsW[inpStr[winStartIdx-1]] -= 1 # char before new start leaves window
        countsW[inpStr[winEndIdx]]     += 1 # char at new end enters window
        if ( countsW == countsP ):  # current window is an anagram
            res.append(winStartIdx)

    return res

    
def test__find_anagrams():
    tasks = [
        ["qabcpbacrbca", "abc"],  # 1, 5, 9
        ["cdef", "m"],            # 
        ["cdef", "e"],            # 2
        ["cbaebabacd", "abc"],    # 0, 6
    ]
    for inpStr, pattern in tasks:
        print("================================")
        print(f"String: '{inpStr}', pattern: '{pattern}'")
        res = find_anagrams(inpStr, pattern)
        print(f"Result: {res}")
