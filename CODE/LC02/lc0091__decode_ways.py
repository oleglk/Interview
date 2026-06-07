# lc0091__decode_ways.pyr
# You need to decode a secret message that's encoded as a string of numbers. The decoding uses this mapping:
#    "1" → 'A'
#    "2" → 'B'
#    ...
#    "25" → 'Y'
#    "26" → 'Z'
# The challenge is that a string of numbers can be decoded in multiple ways because some codes overlap. For instance, "25" could be interpreted as either "2" and "5" (giving 'BE') or as "25" (giving 'Y').
# Given a string s containing only digits, you need to find the total number of ways to decode it.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0091__decode_ways import *

# RELOAD:
# import importlib; import lc0091__decode_ways; importlib.reload(lc0091__decode_ways); from lc0091__decode_ways import *


# The idea: use dynamic programming. At each position #i 1-char code possible if c[i-1]!='0' and 2-char code possible if c[i-2]!='0' and (c[i-2]c[i-1])<=26. Number of decode ways for 1-char code is dp[i-1], while for 2-char code - dp[i-2]. dp[0]=1. At the end dp[n] has the answer.
# See https://algo.monster/liteproblems/91

def decode_ways(s: str) -> int:
    n = len(s)
    dp = [1] + [0]*n  # 1 way to decode empty string, others - just init to 0

    for i in range(1, n+1):
        # consider 1-char code if applicable
        if ( s[i-1] != '0' ):
            dp[i] += dp[i-1]  # 1-digit code is valid
        # consider 2-char code if applicable
        if ( (i >= 2) and (s[i-2] != '0') and (int(s[i-2:i]) <= 26) ):
            dp[i] += dp[i-2]  # 2-digit code is valid

    return dp[n]
##


def test__decode_ways():
    tasks = [
        "12",      # 2
        "226",     # 3
        "06",      # 0
    ]
    for s in tasks:
        print("========================================")
        print(f"Input: {s}")
        res = decode_ways(s)
        print(f"Result: {res}")
##
