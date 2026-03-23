# lc0038__count_and_say.py
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#   countAndSay(1) = "1"
#   countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 1 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run); count comes first.
# For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0038__count_and_say import *

# RELOAD:
# import importlib; import lc0038__count_and_say; importlib.reload(lc0038__count_and_say); from lc0038__count_and_say import *

# The idea:
# - encode function that collects repetition substrings and encodes them
# - s = "1";  for i=2 to n: s = encode(s)
# See: https://algo.monster/liteproblems/38


def rle_encode(s: str) -> str:
    n = len(s)
    enc = []  # collects encoded result as a list
    start = 0
    while ( start < n ):
        end = start
        # move end to after the repeated sequence
        while ( (end < n) and (s[end] == s[start]) ):
            end += 1
        # add encoding of the last repeated sequence
        enc.append(str(end-start))
        enc.append(s[start])
        start = end  # advance start to begin of the next sequence
    return "".join(enc)  # return resulting encoding as a string
##


def nth_element_of_count_and_say(n: int) -> str:
    encStr = "1"
    for i in range(1, n):
        encStr = rle_encode(encStr)
    return encStr
##


def test__nth_element_of_count_and_say():
    for n in range(1, 8):
        print("================================")
        print(f"n={n}")
        res = nth_element_of_count_and_say(n)
        print(f"Result: {res}")
##
