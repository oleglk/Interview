# longest_substring_with_at_most_k_distinct.py - Find length of Longest Substring with At Most K Distinct characters in a given string.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from longest_substring_with_at_most_k_distinct import *

# RELOAD:
# import importlib; import longest_substring_with_at_most_k_distinct; importlib.reload(longest_substring_with_at_most_k_distinct); from longest_substring_with_at_most_k_distinct import *

# The idea: sliding window, hash keeping character counts, counter of distinct chars.


def longest_substring_with_at_most_k_distinct(inpStr: str, k: int) -> int:
    charToFreq = {}  # maps [a..z] to appearence count
    maxLength = 0
    cntDistinct = 0

    left = 0  # window-begin index
    for right, ch  in enumerate(inpStr):
        # "register" the right char
        if ( ch not in charToFreq ):
            charToFreq[ch] = 1
            cntDistinct += 1
        else:
            charToFreq[ch] += 1

        # shrink window from left until num of distinct chars reduces to k
        while ( cntDistinct > k ):
            if ( charToFreq[inpStr[left]] == 1 ):  # guaranteed to be >= 1
                cntDistinct -= 1
            charToFreq[inpStr[left]] -= 1
            left += 1

        maxLength = max(maxLength, right-left+1)
    return maxLength


def test__longest_substring_with_at_most_k_distinct():
    for s, k  in [
            ["", 1],             # 0
            ["aabacbebebe", 3],  # 7 - "cbebebe"
            ["aaaa", 2],         # 4
            ["aabaaab", 2],      # 7 - "aabaaab"
            ]:
        print("======================================")
        print(f"Input: {s}, k={k}")
        res = longest_substring_with_at_most_k_distinct(s, k)
        print(f"Result: {res}")
