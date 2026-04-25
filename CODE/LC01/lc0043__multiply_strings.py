# lc0043__multiply_strings.py
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0043__multiply_strings import *

# RELOAD:
# import importlib; import lc0043__multiply_strings; importlib.reload(lc0043__multiply_strings); from lc0043__multiply_strings import *

# The idea:
# - maxlength of resulting string is n1+n2
# - following school "column" multiplication procedure where indices i and j grow from right to left - e.g. consider strings reversed
# - result of #i * #j affects 2 positions: units added to #(i+j), carry-over added to #(i+j+1)
#  -- units-to-#(i+j) is easy to verify, carry goes to next position which is #(i+j+1)
# See https://medium.com/@bryanchen1105/beyond-int-how-to-conquer-the-multiply-strings-interview-classic-fd339ba9d009

     #   123
     #  *
     #   456
     #   ---
     #   738
     #  615
     # 492
     # =====
     # 56088

     # i goes over 654, j goes over 321
     # i=0, j=0, resArr=000000:     #   tmp = 0 + 6*3 = 18 => resArr=810000
     # i=0, j=1, resArr=810000:     #   tmp = 1 + 6*2 = 13 => resArr=831000
     # i=0, j=2, resArr=831000:     #   tmp = 1 + 6*1 = 7  => resArr=837000
     # i=1, j=0, resArr=837000:     #   tmp = 3 + 5*3 = 18 => resArr=888000
     # i=1, j=1, resArr=888000:     #   tmp = 8 + 5*2 = 18 => resArr=888100
     # i=1, j=2, resArr=888100:     #   tmp = 1 + 5*1 = 6  => resArr=888600
     # i=2, j=0, resArr=888600:     #   tmp = 8 + 4*3 = 20 => resArr=880800
     # i=2, j=1, resArr=880800:     #   tmp = 8 + 4*2 = 16 => resArr=880610
       
def multiply_strings(s1: str, s2: str) -> str:
    # reverse both input strings
    s1 = s1[::-1];  s2 = s2[::-1]
    n1 = len(s1);  n2 = len(s2);  n = n1 + n2
    resArr = [0]*(n1+n2)  # will hold the result in reversed order

    # perform digit multiplications
    for i in range(0, n1):
        for j in range(0, n2):
            tmp = resArr[i+j] + int(s1[i]) * int(s2[j])
            resArr[i+j]    = tmp %  10  # keep only unit's digit
            resArr[i+j+1] += tmp // 10  # add carryover

    resArr = resArr[::-1]  # reverse the result
    # to trim heading zeroes, find leftmost non-zero digit
    i0 = 0  # will point at the 1st non-zero digit
    while ( (i0 < n) and (resArr[i0] == 0) ):
        i0 += 1
    if ( i0 == n ):  # result is zero
        i0 = n-1  # point at the last zero

    # convert back to string while trimming leading zeroes
    s = "".join( map(str, resArr[i0:]) )
    return s
##


def test__multiply_strings():
    tasks = [
        ["12", "0"],                   # 0
        ["12", "1"],                   # 12
        ["2", "3"],                    # 6
        ["123", "456"],                # 56088
    ]
    for s1, s2 in tasks:
        print("==========================================")
        print(f"Input: {s1},  {s2}")
        res = multiply_strings(s1, s2)
        print(f"Result: {res}")
##
