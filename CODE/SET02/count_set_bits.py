# count_set_bits.py - count set bits in a given integer.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from count_set_bits import *

# RELOAD:
# import importlib; import count_set_bits; importlib.reload(count_set_bits); from count_set_bits import *

# The idea: n&(n-1) clears the rightmost set bit - bacause -1 inverts all bits after last set bit inclusive.
# See https://www.geeksforgeeks.org/dsa/count-set-bits-in-an-integer/

# 10              = 00001010
# 9               = 00001001 -1 inverts all bits after last set bit inclusive
# 8               = 00001000
# 7               = 00000111
# 6               = 00000110
# 5               = 00000101
# 4               = 00000100
# 3               = 00000011
# 2               = 00000010
# 1               = 00000001

# 10&9            = 00001000 - least significant set bit is removed
# 10&9-1          = 00000111
# 10&9 & (10&9-1) = 00000000 - least significant set bit is removed
# --- 10 became zero after 2 iterations => 10 has 2 set bits


def count_set_bits(n: int) -> int:
    count = 0
    while ( n != 0 ):  # e.g. while n has set bits
        n = n & (n-1)  # clear the rightmost set bit
        count += 1
    return count


def test__count_set_bits():
    tasks = [10,  # 2
             8,   # 1
             7,   # 3
             -1   # 32
             ]
    for n in tasks:
        print("==================================")
        print(f"Input: {n} -> {bin(n)}")
        res = count_set_bits(n)
        print(f"Result: {res}")
