# lc0003__longest_substring_no_repeat.py - Longest Substring Without Repeating Characters.
# Given a string s, find the length of the longest substring without duplicate characters.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0003__longest_substring_no_repeat import *

# RELOAD:
# import importlib; import lc0003__longest_substring_no_repeat; importlib.reload(lc0003__longest_substring_no_repeat); from lc0003__longest_substring_no_repeat import *

# The idea: sliding window; upon encountering repeated char, drop characters from window tail until the repeated one (including)


def longest_substring_no_repeat(s: str) -> int:
    lst = list(s)
    i1 = i2 = 0   # left and right boundaries of the sliding window
    seenChars = set()
    maxLength = 0
    for i2, ch in enumerate(lst):  # advance right bound
        if ( ch not in seenChars ):
            seenChars.add(ch)
            continue
        # 'ch' - the last char - is repeated
        maxLength = max(maxLength, i2 - i1)  # length without #i2
        # drop char-s from window tail until 'ch' encountered
        while ( lst[i1] != ch ):
            seenChars.remove(lst[i1])
            i1 += 1
        # 'ch'==lst[i2] isn't removed from 'seenChars', since it appears again
        i1 += 1  # pass over the 1st occurence of 'ch' itself
    maxLength = max(maxLength, i2 - i1 + 1)  # count the last window
    return maxLength


def test__longest_substring_no_repeat():
    tasks = [
        "123",           # 3
        "122345",        # 4
        "1223452345678", # 7
        "12341",         # 4
        "abcabcbb",      # 3
        "bbbbb",         # 1
        "pwwkew"         # 3
        ]
    for s in tasks:
        print("====================")
        print(f"Input: '{s}'")
        res = longest_substring_no_repeat(s)
        print(f"Result: {res}")
