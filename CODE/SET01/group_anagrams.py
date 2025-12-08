# group_anagrams.py - Given an array of strings, group the anagrams together. Return a list of groups.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from group_anagrams import *

# RELOAD:
# import importlib;    import group_anagrams;  importlib.reload(group_anagrams);  from group_anagrams import *

# The idea: Hash keyed by sorted input strings where values are lists of original input strings.


def group_anagrams(strings: list):
    hash = {}  # for sorted-str :: list-of-original-str
    for origStr in strings:
        sortStr = "".join(sorted(origStr.upper()))  # 'sorted()' returns list
        if ( sortStr not in hash ):
            hash[sortStr] = [origStr]
        else:
            #hash[sortStr] = hash[sortStr] + [origStr]
            hash[sortStr].append(origStr)
    return(hash.values())


def test__group_anagrams():
    l1 = "abba", "name", "", "mena", "baba", "hand"
    for lst in [l1]:
        print("=============================")
        print(f"Input: {lst}")
        res = group_anagrams(lst)
        print(f"Output: {res}")
