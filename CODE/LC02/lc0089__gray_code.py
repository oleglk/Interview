# lc0089__gray_code.py
# An n-bit gray code sequence is a sequence of 2n integers where:
#   Every integer is in the inclusive range [0, 2n - 1],
#   The first integer is 0,
#   An integer appears no more than once in the sequence,
#   The binary representation of every pair of adjacent integers differs by exactly one bit, and
#    The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0089__gray_code import *

# RELOAD:
# import importlib; import lc0089__gray_code; importlib.reload(lc0089__gray_code); from lc0089__gray_code import *

# The idea: start with sequence for n-1, make reversed copy, prepend 0 to original, 1 to reversed, concatenate.
# [0,1]  ->  0,1  1,0  ->  00,01  11,10
# See https://www.geeksforgeeks.org/dsa/generate-n-bit-gray-codes/


def gray_code(n: int) -> list[str]:
    if ( n == 0 ):  return []
    seq = ["0", "1"]
    if ( n == 1 ):  return seq
    for numDigits in range(2, n+1):
        rseq = seq[::-1]  # create the reversed sequence
        size = len(seq)
        for i in range(0, size):
            seq[i] = "0" + seq[i]   # prepend 0 to elements of orig sequence
        for i in range(0, size):
            rseq[i] = "1" + rseq[i] # prepend 1 to elements of reversed sequence
        seq.extend(rseq)  # concatenate original and reversed lists

    return seq
##


def test__gray_code():
    tasks = [
        2,  # ['00', '01', '11', '10']
        3,  # ['000', '001', '011', '010', '110', '111', '101', '100']
    ]
    for n in tasks:
        print("======================================")
        print(f"n={n}")
        res = gray_code(n)
        print(f"Result: {res}")
##
