# lc0093__restore_ip_address.py
# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
#    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0093__restore_ip_address import *

# RELOAD:
# import importlib; import lc0093__restore_ip_address; importlib.reload(lc0093__restore_ip_address); from lc0093__restore_ip_address import *

# The idea: recursions for 1,2,3 digits in a segment.
# See https://algo.monster/liteproblems/93


def restore_ip_address(s: str) -> list[str]:
    def is_valid_segment(begin: int, end: int) -> bool:
        if ( (s[begin] == '0') and (begin != end) ):
            return False  # heading zeroes prohibited
        val = int(s[begin:end+1])
        return 0 <= val <= 255
    ##

    def restore_ip_address__recurse(startIdx: int) -> None:
        """Continue building IP from 'startIdx'"""
        nonlocal result
        # Base case - valid IP formed
        if ( (startIdx >= len(s)) and (len(ipSegments) == 4) ):
            result.append('.'.join(ipSegments))
            return
        # Base case - either string or num-segments exhausted
        if ( (startIdx >= len(s)) or (len(ipSegments) >= 4) ):
            return

        # recursive cases - try segment of 1,2,3 digits
        for segEndIdx in range(startIdx, min(startIdx+3, len(s))):
            if ( is_valid_segment(startIdx, segEndIdx) ):
                ipSegments.append(s[startIdx:segEndIdx+1])
                restore_ip_address__recurse(segEndIdx + 1)  # process remaining
                ipSegments.pop()  # clean for next step
        return
    ##
    
    ipSegments = []  # for building one IP address
    result = []
    restore_ip_address__recurse(0)
    return result
##

    
def test__restore_ip_address():
    tasks = [
        "25525511135",    # ["255.255.11.135","255.255.111.35"]
        "0000",           # ["0.0.0.0"]
        "101023",         # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    ]
    for s in tasks:
        print("=======================================")
        print(f"Input: {s}")
        res = restore_ip_address(s)
        print(f"Result: {res}")
##
