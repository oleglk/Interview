# lc0190__reverse_bits.py
# Reverse bits of a given 32 bits signed integer.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0190__reverse_bits import *

# RELOAD:
# import importlib;    import lc0190__reverse_bits;  importlib.reload(lc0190__reverse_bits);  from lc0190__reverse_bits import *

# The idea: (a) mask 32 bits so that they represent 2-s complement pattern (UNCLEAR); (b) repeat 32 times: take the input's rightmost bit and shift it left into the result, then shift the input right; (c) if bit 31 is set, subtract 2^32 to interpret the unsigned 32-bit pattern as a signed two's-complement integer (UNCLEAR).
# See: https://thita.ai/problems/reverse-bits/editorial


def reverse_bits(n: int) -> int:
    # mask 32 bits so that they represent 2-s complement pattern (UNCLEAR)
    n &= 0xFFFFFFFF

    nReversed = 0
    for _ in range(32):
        # take the input's rightmost bit and shift it left into the result
        bit = n & 1
        # original bit0 starts in pos #0 and moves into pos #31 after 31 shifts
        nReversed <<= 1
        nReversed |= bit
        n >>= 1  # put the next bit into rightmost position

    # if bit 31 is set, subtract 2^32 to interpret the unsigned 32-bit pattern
    #                   as a signed two's-complement integer (UNCLEAR).
    if ( nReversed & 0x80000000 ):
        nReversed -= 1<<32

    return nReversed
##


def test__reverse_bits():
    tasks = [
        43261596,   # 964176192
        2147483644, # 1073741822
    ]
    for n in tasks:
        print("===========================================")
        print(f"Input: {n}")
        res = reverse_bits(n)
        print(f"Result = {res}")
##
