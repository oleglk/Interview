# lc0187__repeated_dna_sequences.py
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#    For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0187__repeated_dna_sequences import *

# RELOAD:
# import importlib;    import lc0187__repeated_dna_sequences;  importlib.reload(lc0187__repeated_dna_sequences);  from lc0187__repeated_dna_sequences import *

# The idea: Maintain 2 sets - 'seen' and 'repeated'. Run 10-long sliding window over s.If window not in 'seen', insert into 'seen', otherwise insert into 'repeated'.
# See: https://www.geeksforgeeks.org/dsa/find-repeated-dna-sequences/


def repeated_dna_sequences(s: str) -> list[str]:
    seen = set()
    repeated = set()

    # run sliding window over 's'
    # (why len(s)-9: if len=10, need to produce range(0,1) and 1==10-9)
    for i in range(0, len(s)-9):
        substr = s[i:i+10]
        if ( substr not in seen ):
            seen.add(substr)  # 1st occurence of 'substr'
        else:
            repeated.add(substr)  # repeated occurence of 'substr'

    return list(repeated)
##

            
def test__repeated_dna_sequences():
    tasks = [
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",    # ["AAAAACCCCC","CCCCCAAAAA"]
        "AAAAAAAAAAAAA",                       # ["AAAAAAAAAA"]
    ]
    for s in tasks:
        print("=======================================")
        print(f"Input: {s}")
        res = repeated_dna_sequences(s)
        print(f"Result: {res}")
##
