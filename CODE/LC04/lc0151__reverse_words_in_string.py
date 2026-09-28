# lc0151__reverse_words_in_string.py
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# The original string may have heading/trailing/multiple spaces.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0151__reverse_words_in_string import *

# RELOAD:
# import importlib;    import lc0151__reverse_words_in_string;  importlib.reload(lc0151__reverse_words_in_string);  from lc0151__reverse_words_in_string import *


# The idea:
# - copy into mutable collection - list
# - reverse the whole string
# - work word-by-word
# -- compact separator spaces
# -- copy the word (to compact spaces), still reversed
# -- reverse individual word to restore correct internal order
# - copy back into string
# See: https://algomaster.io/learn/dsa/reverse-words-in-a-string


def reverse_words_order(s: str) -> str:
    chars = list(s)  # copy into mutable collection
    n = len(chars)
    reverse_in_list(chars, 0, n-1)  # reverse the whole string

    # process individual words
    iRead = 0  # read in list pointer
    iWrite = 0 # write into list pointer
    while ( iRead < n ):
        # we are skipping all original spaces
        if ( chars[iRead] != ' ' ):
            # word begin found - insert one separator, then copy the word
            if ( iWrite > 0 ):
                chars[iWrite] = ' '
                iWrite += 1
            wordStart = iWrite
            while ( (iRead < n) and (chars[iRead] != ' ') ):
                chars[iWrite] = chars[iRead]
                iRead += 1
                iWrite += 1
            reverse_in_list(chars, wordStart, iWrite-1)  # reverse one word
        else:
            iRead += 1  # skip original space

    return "".join(chars[:iWrite]) #  copy back into a string and return it
##


def reverse_in_list(lst: list, iLeft: int, iRight: int) -> None:
    while ( iLeft < iRight ):
        lst[iLeft], lst[iRight] = lst[iRight], lst[iLeft]
        iLeft += 1
        iRight -= 1
    return
##


def test__reverse_words_order():
    tasks = [
        "the sky is blue",
        "  hello world  ",
        "a good   example"
    ]
    for s in tasks:
        print("===========================================")
        print(f"Input: '{s}'")
        res = reverse_words_order(s)
        print(f"Result: '{res}'")
##

