# lc0159__longest_substring_with_at_most_2_distinct_chars.py
# Given a string s, return the length of the longest substring that contains at most two distinct characters.
# A substring is a continuous sequence of characters within the string (i.e., characters must appear next to each other without skipping).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0159__longest_substring_with_at_most_2_distinct_chars import *

# RELOAD:
# import importlib;    import lc0159__longest_substring_with_at_most_2_distinct_chars;  importlib.reload(lc0159__longest_substring_with_at_most_2_distinct_chars);  from lc0159__longest_substring_with_at_most_2_distinct_chars import *

# The idea: sliding window and dict counting char appearances. Extend rightwards to include new char. Reduce from left until only 2 distinct chars remain.


def longest_substring_with_at_most_2_distinct_chars(s: str) -> int:
    maxLen = 0
    charsCounts = {}
    iLeft = 0
    iRight = 0
    if ( len(s) == 0 ):
        return 0
    # extend window rightwards to include new char
    for iRight in range(len(s)):
        charsCounts[s[iRight]] = 1 + charsCounts.get(s[iRight], 0)
        # reduce window from left until <= 2 distinct chars remain
        while ( len(charsCounts) > 2 ):
            charsCounts[s[iLeft]] -= 1
            if ( charsCounts[s[iLeft]] == 0 ):
                del charsCounts[s[iLeft]]
            iLeft += 1
        # update max length if needed
        maxLen = max(maxLen, iRight - iLeft + 1)

    return maxLen
##


def test__longest_substring_with_at_most_2_distinct_chars():
    tasks = [
        "geeksforgeeks",  # 3
        "ccaabbb",        # 5
    ]
    for s in tasks:
        print("============================================")
        print(f"Input: {s}")
        res = longest_substring_with_at_most_2_distinct_chars(s)
        print(f"Result: {res}")
##

            
