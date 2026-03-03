# lc0017__phone_letter_combos.py

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters:
## 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0017__phone_letter_combos import *

# RELOAD:
# import importlib; import lc0017__phone_letter_combos; importlib.reload(lc0017__phone_letter_combos); from lc0017__phone_letter_combos import *


# The idea: put current prefix in the queue; extract from queue, append per-current-digit letters, reinsert each resulting new prefix in the queue, etc.


from collections import deque

def phone_number_letter_combos(numArr: list[int]) -> list[str]:
    digitToLetters = {2:"abc", 3:"def",
                      4:"ghi", 5:"jkl", 6:"mno",
                      7:"pqrs", 8:"tuv", 9:"wxyz"}
    results = []
    prefix = ""
    prefixQueue = deque()
    prefixQueue.append("")  # schedule empty prefix

    while ( prefixQueue ):
        prefix = prefixQueue.popleft()
        # if 'prefix' is a complete sequence, add it to results list
        if ( len(prefix) == len(numArr) ):
            results.append(prefix)
            continue
        # schedule prefixes with letters for the current digit
        currDigit = numArr[len(prefix)]
        if currDigit not in digitToLetters:
            continue  # skip 0,1
        for letter in digitToLetters[currDigit]:
            newPrefix = prefix + letter
            prefixQueue.append(newPrefix)
    return results
##


def test_phone_number_letter_combos():
    tasks = [
        [2,3],     # ad ae af bd be bf cd ce cf
        [2],       # a b c
        [],        #
        [2,3,4]    # "adg", "adh", "adi",
                   # "aeg", "aeh", "aei",
                   # "afg", "afh", "afi",
                   # "bdg", "bdh", "bdi",
                   # "beg", "beh", "bei",
                   # "bfg", "bfh", "bfi",
                   # "cdg", "cdh", "cdi",
                   # "ceg", "ceh", "cei",
                   # "cfg", "cfh", "cfi"
    ]
    for numArr in tasks:
        print("=====================================")
        print(f"Input: {numArr}")
        res = phone_number_letter_combos(numArr)
        print(f"Result: {res}")
##
