# lc0139__word_break.py
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0139__word_break import *

# RELOAD:
# import importlib;    import lc0139__word_break;  importlib.reload(lc0139__word_break);  from lc0139__word_break import *

# The idea: DP. DP[i]==True if some valid breaking ends at i-1. This means existent word ands at i-1 and a valid breaking ends before this word, the latter equals DP[word_begin].
# See: https://www.geeksforgeeks.org/dsa/word-break-problem-dp-32/#expected-approach-2-using-bottom-up-dp-onmk-time-and-on-space


def word_break(s: str, wordList: list[str]) -> bool:
    if ( (s is None) or (s == "") ):
        return True
    n = len(s)
    dp = [False] * (n + 1)  # DP[i]==True if some valid breaking ends at i-1
    dp[0] = True  # no chars is a valid breaking

    # check every position in the string to be next to word end
    for i in range(1, n+1):
        # check every word to be able to finish before #i
        for word in wordList:
            wordStart = i - len(word)
            if ( (wordStart >= 0) and (s[wordStart : i] == word) and \
                 (dp[wordStart] == True) ):
                dp[i] = True

    return dp[n]
##


def test__word_break():
    tasks = [
        ["leetcode", ["leet","code"]],                    # true
        ["applepenapple", ["apple","pen"]],               # true
        ["catsandog", ["cats","dog","sand","and","cat"]], # false
    ]
    for s, wordList in tasks:
        print("=============================================")
        print(f"Input: {s}, wordList={wordList}")
        res = word_break(s, wordList)
        print(f"Result: {res}")
##
