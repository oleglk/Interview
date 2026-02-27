# lc0013__roman_to_integer.py
# Given a string s representing a Roman numeral, find it's corresponding integer value.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0013__roman_to_integer import *

# RELOAD:
# import importlib; import lc0013__roman_to_integer; importlib.reload(lc0013__roman_to_integer); from lc0013__roman_to_integer import *

class RomanToInt:
    symbolToBase =  {
           "I":1,   "IV":4,   "V":5,   "IX":9,
           "X":10,  "XL":40,  "L":50,  "XC":90,
           "C":100, "CD":400, "D":500, "CM":900,
           "M":1000 }

    @staticmethod
    def get_symbol_at_idx(romanStr: str, idx:int) -> tuple[str, int]:
        """Returns (num-character(s)-used, int-value)."""
        if ( idx >= len(romanStr) ):
            raise Exception(f"Index {idx} out of bounds")
        for c in romanStr:
            if ( c not in RomanToInt.symbolToBase ):
                raise Exception(f"Invalid symbol {c}")
        onlyOneLeft = idx == (len(romanStr) - 1)
        # check for "subtraction case" - "IV", "IX", "XL", "XC", "CD", "CM"
        # happens when curr char is SMALLER than the next char
        if ( (not onlyOneLeft) and
             (RomanToInt.symbolToBase[romanStr[idx]] <
              RomanToInt.symbolToBase[romanStr[idx+1]]) ):
            # two-character "subtraction" symbol
            symbol = romanStr[idx:idx+2]
            return (2, RomanToInt.symbolToBase[symbol])
        # one-character symbol
        return(1, RomanToInt.symbolToBase[romanStr[idx]])
    ##


    @staticmethod
    def convert(romanStr: str) -> int:
        if ( (romanStr is None) or (romanStr == "") ):
            return 0
        res = 0
        idx = 0
        while ( idx < len(romanStr) ):
            numCharsUsed, val = RomanToInt.get_symbol_at_idx(romanStr, idx)
            res += val
            idx += numCharsUsed
        return res
    ##
####
            

def test__roman_to_integer():
    tasks = [
        "III",         # 3
        "V",           # 5   
        "IX",          # 9   
        "XL",          # 40  
        "MCMIV",       # 1904
        "MMMDCCXLIX",  # 3749
        "LVIII",       # 58  
        "MCMXCIV",     # 1994 
    ]
    for romanStr in tasks:
        print("=========================================")
        print(f"Input: {romanStr}")
        res = RomanToInt.convert(romanStr)
        print(f"Result: {res}")
##
