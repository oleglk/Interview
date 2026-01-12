# gray_code.py - Reflective method to generate Gray codes.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from gray_code import *

# RELOAD:
# import importlib; import gray_code; importlib.reload(gray_code); from gray_code import *


# The idea: recursively obtain solution list for one bit less (prev-list), prepend 0 to prev-list elements, prepend 1 to reversed-copy-of prev-list elements, concatenate the two lists.


def gray_codes(nBits: int) -> list[int]:
    if ( nBits == 1 ):
        return ['0', '1']  # base case

    # obtain codes of length nBits-1
    prevCodes = gray_codes(nBits - 1)
    prevCodesRev = prevCodes[::-1]

    # prepend 0 in 'prevCodes', prepend 1 in 'prevCodesRev'
    for i in range(0, len(prevCodes)):
        prevCodes[i]    = '0' + prevCodes[i]
        prevCodesRev[i] = '1' + prevCodesRev[i]

    # resulting list is concatenation - 'prevCodes' followed by 'prevCodesRev'
    prevCodes.extend(prevCodesRev)
    return prevCodes


def test__gray_codes():
    for length in [2, 3]:
        print("==================================")
        print(f"Gray code of bit-length {length}:")
        res = gray_codes(length)
        print(res)
