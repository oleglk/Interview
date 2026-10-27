# lc0192__word_frequency.py
# Note, the task is changed from the origin at Leetcode.
# Given a string str, the task is to find the frequency of each word in a string.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0192__word_frequency import *

# RELOAD:
# import importlib;    import lc0192__word_frequency;  importlib.reload(lc0192__word_frequency);  from lc0192__word_frequency import *

# The idea: scan the string, treat spaces as last-word ends unless the last-word is empty.
# See: https://www.geeksforgeeks.org/dsa/calculate-the-frequency-of-each-word-in-the-given-string/


def word_frequency(s: str) -> dict[str, int]:
    freqDict = {}
    lastWord = ""
    n = len(s)
    for i in range(0, n+1):  # including after-end-of-string
        if ( i < n ):
            ch = s[i]
        else:
            ch = ' '  # simulate space at the string end to process the last word
        if ( ch.isspace() ):  # word end or repeated space
            if ( lastWord == "" ):  # repeated space
                continue
            # word end
            if ( lastWord not in freqDict ):
                freqDict[lastWord] = 1
            else:
                freqDict[lastWord] += 1
            lastWord = ""  # prepare for new word
        else:  # not a space - continue collecting the word
            lastWord += ch
    return freqDict
##


def test__word_frequency():
    tasks = [
        "Geeks For Geeks",  # {Geeks: 2, For: 1}
        "learning to code is learning to create and innovate",  # {learning: 2, to: 2, code: 1, is: 1, create: 1, and: 1, innovate: 1}
    ]
    for s in tasks:
        print("========================================")
        print(f"Input: {s}")
        res = word_frequency(s)
        print(f"Result: {res}")
##

