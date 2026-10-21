# lc0186__reverse_words_in_sring_2.py
# Given a character array s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. Unlike its counterpart (Reverse Words in a String I), the input array has no leading or trailing spaces, and words are separated by exactly one space.
# Your solution must modify s in-place.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0186__reverse_words_in_sring_2 import *

# RELOAD:
# import importlib;    import lc0186__reverse_words_in_sring_2;  importlib.reload(lc0186__reverse_words_in_sring_2);  from lc0186__reverse_words_in_sring_2 import *

# The idea: first reverse the whole string, then reverse individual words back. Have reverse_range() utility function.

# See: https://www.jointaro.com/interviews/questions/reverse-words-in-a-string-ii/


def reverse_words_in_sring_2(arr: list[str]) -> list[str]:
    def reverse_range(arr: list[str], begin: int, end: int) -> list[str]:
        if ( (begin < 0) or (end >= len(arr)) ):
            return
        while ( begin < end ):
            arr[begin], arr[end] = arr[end], arr[begin]
            begin += 1
            end -= 1
    ##
    n = len(arr)
    # reversal of the whole array puts words in required order
    reverse_range(arr, 0, n-1)

    # reverse individual words
    wordBegin = 0
    for i in range(0, n+1):
        if ( (i == n) or (arr[i] == ' ') ):  # word end found
            reverse_range(arr, wordBegin, i-1)
            wordBegin = i + 1  # advance 'wordBegin' to right after space

    return arr
##

    
def test__reverse_words_in_sring_2():
    tasks = [
        "one",          # "one"
        "this is it",   # "it is this"
    ]
    for s in tasks:
        print("===============================================")
        arr = list(s)
        print(f"Input: {arr}")
        reverse_words_in_sring_2(arr)
        print(f"Result: {arr}")
##
