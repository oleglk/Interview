# lc0132__palindrome_partitioning_2.py
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0132__palindrome_partitioning_2 import *

# RELOAD:
# import importlib;    import lc0132__palindrome_partitioning_2;  importlib.reload(lc0132__palindrome_partitioning_2);  from lc0132__palindrome_partitioning_2 import *

# The idea: (1) precompute is_palindrome using DP: DP[i][j] = (s[i] == s[j]) and DP[i+1][j-1]. (2) Solve by DP.
# See https://neetcode.io/solutions/palindrome-partitioning    for precomputing.
# See https://www.coddykit.com/courses/interview_prep/palindrome-partitioning-ii-10365790    for the general solution.


def palindrome_partitioning_2(s: str) -> int:
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

    n = len(s)
    isPalindrome = precompute_palindromes()
    cuts = [float('inf')] * n  # cuts[i] = min num of cuts for s[0..i]

    for i in range(0, n):  # check prefixes of increasing length
        if ( isPalindrome[0][i] ):  # entire prefix is palindrome
            cuts[i] = 0
        else:
            # try every split at [0..i-1]
            for j in range(0, i):
                if ( isPalindrome[j+1][i] ):  # palindrome to the right of split
                    # consider cuts of prefix [0..j] + one cut at j
                    cuts[i] = min(cuts[i], (cuts[j] + 1))

    return cuts[n-1]
##


def test__palindrome_partitioning_2():
    tasks = [
        "aab",    # 1
        "a",      # 0
        "ab",     # 1
    ]
    for s in tasks:
        print("===============================================")
        print(f"Input: {s}")
        res = palindrome_partitioning_2(s)
        print(f"Result: {res}")
##
