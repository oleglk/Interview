# lc0058__length_of_last_word.py
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0058__length_of_last_word import *

# RELOAD:
# import importlib; import lc0058__length_of_last_word; importlib.reload(lc0058__length_of_last_word); from lc0058__length_of_last_word import *

# The idea: traverse the string from the end; first skip trailing spaces, then count characters until the first space.


def length_of_last_word(s: str) -> int:
    if ( (s is None) or (len(s) == 0) ):
         return 0
    # skip trailing spaces
    i = len(s) - 1
    while ( (i >= 0) and ((s[i] == ' ') or (s[i] == '\t')) ):
        i -= 1
    if ( i < 0 ):
        return 0  # all spaces
    # count characters (right-to-left) until the first space
    lastI = i  # points at the last char in the word
    while ( (i >= 0) and ((s[i] != ' ') and (s[i] != '\t')) ):
        i -= 1
    # either i == -1 or i points at the space before word begin
    wordLen = lastI - i
    return wordLen
##


def test__length_of_last_word():
    tasks = [
        "Hello World",                  # 5
        "   fly me   to   the moon  ",  # 4
        "luffy-is-still-joyboy",        # 21
        " "                             # 0
        ]
    for s in tasks:
        print("======================================")
        print(f"Input: '{s}'")
        res = length_of_last_word(s)
        print(f"Result: {res}")
##
