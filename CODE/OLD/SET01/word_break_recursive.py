# word_break.py - Given a string s and a dictionary of strings wordDict, determine if s can be segmented into a space-separated sequence of one or more dictionary words. Words in string s ARE NOT DELIMITED ANYHOW"

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from word_break_recursive import *

# RELOAD:
# import importlib; import word_break_recursive; importlib.reload(word_break_recursive); from word_break_recursive import *

prefixMemo = [];  # for memoization - -1|0|1 indexed by prefix length

def word_break_recursive(s: str, wordDict: dict) -> bool:
    prefixMemo = [-1]*(len(s)+1)  # lengths from 0 to len() inclusive
    return(can_segment_recursive(s, len(s), wordDict, prefixMemo))


def can_segment_recursive(s: str, sLen: int, wordDict: dict, memo: list) -> bool:
    if ( (s == '') or (sLen == 0) ):
        return(1)  # base case - string either was empty or depleted
    subS = s[:sLen]   # this iteration takes 'sLen' first characters
    for word in wordDict:
        if ( not subS.endswith(word) ):
            continue
        # the current substring ends with 'word'; check if prefix is segmentable
        prefLength = len(subS) - len(word)
        prefix = subS[:-len(word)]  # if 'word' truncated; only for debug prints
        print(f"@@ Substring '{subS}': prefix='{prefix}', ends with '{word}'")
        if ( memo[prefLength] != -1 ):
           canDoPrefix = memo[prefLength]
           print(f"@@@@ Used memoized answer={canDoPrefix} for prefix '{prefix}'")
        else:
            canDoPrefix = can_segment_recursive(s, prefLength, wordDict, memo)
            memo[prefLength] = canDoPrefix
        if ( canDoPrefix ):
            return(1)
    return(0)


def test__word_break_recursive():
    tasks = [ ["thesong", {"the":1, "song":1, "break":1, "can":1, "long":1}],
              ["ashape", {"a":1, "share":1}],
              ["catsanddog", {"cat":1, "cats":1, "and":1, "sand":1, "dog":1}],
              ["ilike", {"i":1, "like":1, "gfg":1}],
              ["ilikegfg", {"i":1, "like":1, "man":1, "india":1, "gfg":1}],
              ["ilikemangoes", {"i":1, "like":1, "gfg":1}] ]
    for s, wordDict  in tasks:
        print("===========================")
        print(f"Input: '{s}' with {wordDict}")
        res = word_break_recursive(s, wordDict)
        print(f"Result: {res == 1}")
