# longest_substring_without_repeating.py - Given a string s, find the length of the longest substring without repeating characters.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from longest_substring_without_repeating import *

# RELOAD:
# import importlib;    import longest_substring_without_repeating;  importlib.reload(longest_substring_without_repeating);  from longest_substring_without_repeating import *

# The idea: sliding window; upon encountering repeated char, drop characters from window tail until the repeated one (including)


def longest_substring_without_repeating(s: str) -> int:
    lst = list(s)
    i1 = i2 = 0     # boundaries of sliding window
    seenChars = set({lst[0]})  # characters encountered - included in current substring
    maxLength = 1
    for i2 in range(1, len(lst)):
        if ( lst[i2] not in seenChars ):
            seenChars.add(lst[i2])
            continue
        # the last character is repeated
        lastLength = i2 - i1  # length without #i2
        if ( lastLength > maxLength ):
            maxLength = lastLength
        # drop characters from tail until the repeated char found
        while ( lst[i1] != lst[i2] ):
            seenChars.remove(lst[i1])
            i1 += 1
        i1 += 1  # pass over the 1st occurence of the repeated char itself
    maxLength = max(maxLength, len(lst) - i1)  # account for last substring

    return(maxLength)


def test__longest_substring_without_repeating():
    s1 = "123"
    s2 = "122345"
    s3 = "1223452345678"
    s4 = "12341"
    for s in [s1, s2, s3, s4]:
        print("====================")
        print(f"Input: '{s}'")
        res = longest_substring_without_repeating(s)
        print(f"Result: {res}")
