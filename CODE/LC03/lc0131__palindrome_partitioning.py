# lc0131__palindrome_partitioning.py
# Given a string s, partition s such that every of the partition is a palindrome. Return all possible palindrome partitioning of s.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0131__palindrome_partitioning import *

# RELOAD:
# import importlib;    import lc0131__palindrome_partitioning;  importlib.reload(lc0131__palindrome_partitioning);  from lc0131__palindrome_partitioning import *

# The idea: (1) precompute is_palindrome using DP: DP[i][j] = (s[i] == s[j]) and DP[i+1][j-1]. (2) Solve by recursion.
# See https://algocademy.com/blog/palindrome-partitioning-a-comprehensive-guide-to-solving-this-classic-algorithm-problem/
# and
# https://neetcode.io/solutions/palindrome-partitioning
# for precomputing.

def palindrome_partitioning(s: str) -> list[str]:
    def precompute_palindromes() -> list[list[bool]]:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        # discover palindromes starting from length = 1
        for lng in range(1, n+1):
            for beg in range(0, n - lng + 1):
                dp[beg][beg + lng - 1] = (s[beg] == s[beg + lng - 1]) and \
                     ((beg + 1 > beg + lng - 2) or dp[beg + 1][beg + lng - 2])
        return dp
    ##
    dp = precompute_palindromes()
    result = [];  onePartition = []
    
    def partition_recurse(beg: int) -> None:
        nonlocal result, onePartition
        if ( beg >= len(s) ):  # full palindromic partition is completed
            result.append(onePartition[:])
            return
        for end in range(beg, len(s)):
            if ( dp[beg][end] ):  # substring beg..end is a palindrome
                onePartition.append(s[beg : end+1])
                partition_recurse(end + 1)
                onePartition.pop()  # clean for trying next end index
        return
    ##
    partition_recurse(0)
    return result
##


def test__palindrome_partitioning():
    tasks = ["aab",    # ["a", "a", "b"], ["aa", "b"]
             "a"]      # ["a"]
    for s in tasks:
        print("==================================================")
        print(f"Input: {s}")
        res = palindrome_partitioning(s)
        print(f"Result: {res}")
##
