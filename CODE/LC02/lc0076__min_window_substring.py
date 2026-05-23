# lc0076__min_window_substring.py
# Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0076__min_window_substring import *

# RELOAD:
# import importlib; import lc0076__min_window_substring; importlib.reload(lc0076__min_window_substring); from lc0076__min_window_substring import *

# The idea: sliding window, dict of target counts and dict of in-window counts. Count of satisfied characters.
# See https://algo.monster/liteproblems/76 for explaination.
# See https://interviewing.io/questions/minimum-window-substring for more clear implementation.

from collections import defaultdict

def min_window_substring(s: str, t: str) -> str:
    targetCounts = defaultdict(int)  # for target counts
    for c in t:
        targetCounts[c] += 1
    cntRequired = len(targetCounts)

    cntSatisfied = 0 # how many needed chars appear in window at sufficient count
    left = 0  # leftmost index of the current window
    minWndLeft = -1
    minWndLength = float('inf')
    windowCounts = defaultdict(int)

    for right, char in enumerate(s):  # continuously expand window to the right
        windowCounts[char] += 1
        if ( (char in targetCounts) and (windowCounts[char] == targetCounts[char]) ):
            # char just became satisfied
            cntSatisfied += 1

        # try squeezing the window from left; register valid windows
        while ( (left <= right) and (cntSatisfied == cntRequired) ):
            if ( (right - left + 1) < minWndLength ):
                minWndLeft = left
                minWndLength = right - left + 1

            # remove leftmost window char and check window validity
            leftChar = s[left]
            windowCounts[leftChar] -= 1
            if ( (leftChar in targetCounts) and (windowCounts[leftChar] < targetCounts[leftChar]) ):
               cntSatisfied -= 1 
            left += 1

    # return the min-window substring
    return s[minWndLeft:(minWndLeft + minWndLength)] if (minWndLeft >= 0) else ""
##


def test__min_window_substring():
    tasks = [
        ["ADOBECODEBANC", "ABC"],  # "BANC"
        ["a", "a"],                # "a"
        ["a", "aa"],               # ""
        ["ab","b"],                # "b"
    ]
    for s, t  in tasks:
        print("============================================")
        print(f"Input: {s},  {t}")
        res = min_window_substring(s, t)
        print(f"Result: {res}")
##
