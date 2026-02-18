# valid_anagram.py - Given two strings s and t, return True if t is an anagram of s, otherwise False.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from valid_anagram import *

# RELOAD:
# import importlib;    import valid_anagram;  importlib.reload(valid_anagram);  from valid_anagram import *


def valid_anagram(s: str, t: str) -> bool:
    s = s.upper();  t = t.upper()
    # count characters in the two strings
    countsS = {};  countsT = {}
    for c in s:
        if ( c not in countsS ):
            countsS[c] = 1
        else:
            countsS[c] +=1
    for c in t:
        if ( c not in countsT ):
            countsT[c] = 1
        else:
            countsT[c] +=1
    return(countsS == countsT)


def test__valid_anagram():
    s11 = "ABBA";  s12 = "baba";  s13 = "bobo";  s14 = ""
    for t in [s12, s13, s14]:
        res = valid_anagram(s11, t)
        print(f"'{s11}' and '{t}' => is-anagram={res}")

