# lc0067__add_binary.py
# Given two binary strings a and b, return their sum as a binary string.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0067__add_binary import *

# RELOAD:
# import importlib; import lc0067__add_binary; importlib.reload(lc0067__add_binary); from lc0067__add_binary import *

# The idea: use 2 pointers for input strings; at each position add digits under pointers and carry; build the result reversed.
# See https://www.jointaro.com/interviews/questions/add-binary/


def add_binary(a: str, b: str) -> str:
    nA = len(a)
    nB = len(b)
    if ( nA == 0 ):  return b
    if ( nB == 0 ):  return a
    carry = 0
    iA = nA - 1
    iB = nB - 1
    res = []

    while ( (iA >= 0) or (iB >= 0) or (carry == 1) ):
        sum = carry  # for total sum of one position
        if ( iA >= 0 ):
            sum += int(a[iA])
        if ( iB >= 0 ):
            sum += int(b[iB])
        res1 = sum % 2  # new value of the current position
        carry = sum // 2  # (3->1, 2->1, 1->0, 0->0)
        res.append(res1)
        iA -= 1
        iB -= 1

    res.reverse()
    return res
##


def test__add_binary():
    tasks = [
        ["11", "1"],       # "100"
        ["1010", "1011"],  # "10101"
    ]
    for a, b  in tasks:
        print("=====================================")
        print(f"Input: {a}, {b}")
        res = add_binary(a, b)
        print(f"Result: {res}")
##

