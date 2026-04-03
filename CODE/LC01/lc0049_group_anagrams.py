# lc0049_group_anagrams.py
# Given an array of strings strs, group the anagramss together. You can return the answer in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0049_group_anagrams import *

# RELOAD:
# import importlib; import lc0049_group_anagrams; importlib.reload(lc0049_group_anagrams); from lc0049_group_anagrams import *

# The idea: build a dict of sorted-name :: list of anagram-names

from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[str]:
    strMap = defaultdict(list)  # for sorted-key :: list of keys
    for name in strs:
        sortedName = "".join(sorted(name))
        strMap[sortedName].append(name)
    resList = []
    for sortedName in strMap:
        resList.append(strMap[sortedName])
    return resList
##


def test__group_anagrams():
    tasks = [
        ["eat","tea","tan","ate","nat","bat"],  # [["bat"],["nat","tan"],["ate","eat","tea"]]
        [""],                                   # [[""]]
        ["a"],                                  # [["a"]]
        ["anna","panni","nana"],                # [["anna","nana"],["panni"]]
    ]
    for strs in tasks:
        print("=================================================")
        print(f"Input: {strs}")
        res = group_anagrams(strs)
        print(f"Result: {res}")
##
