# lc0012__integer_to_roman.py
# Given an integer, convert it to a Roman numeral.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0012__integer_to_roman import *

# RELOAD:
# import importlib; import lc0012__integer_to_roman; importlib.reload(lc0012__integer_to_roman); from lc0012__integer_to_roman import *

# The idea (see https://www.geeksforgeeks.org/python/python-program-to-convert-integer-to-roman/):
# Maintain array of base values mapped to Roman symbols.
# Each time find the largest base value smaller than remain of the number. Repeat the corresponding symbol (remain / max_base_value) times. Update remain = (remain % max_base_value).

class IntToRoman:
    baseToSymbol = {
           1:"I",   4:"IV",   5:"V",   9:"IX",
          10:"X",  40:"XL",  50:"L",  90:"XC",
         100:"C", 400:"CD", 500:"D", 900:"CM",
        1000:"M" }
    
    basesMaxToMin = None

    @staticmethod
    def _find_max_base(num: int) -> int:
        if IntToRoman.basesMaxToMin is None:
            IntToRoman.basesMaxToMin = sorted(list(
                IntToRoman.baseToSymbol.keys()), reverse=True)
            print(f"basesMaxToMin computed as {IntToRoman.basesMaxToMin}")
        for base in IntToRoman.basesMaxToMin:
            if ( base <= num ):
                return base
    ##


    @staticmethod
    def convert(num: int) -> str:
        res = ""
        while ( num > 0 ):
            # find the largest base we can divide by - the next Roman symbol
            base = IntToRoman._find_max_base(num)
            repetitions = num // base
            res += IntToRoman.baseToSymbol[base] * repetitions
            # update 'num' to remainder from deletion by largest base
            num %= base
        return res
    ##
####


def test__integer_to_roman():
    tasks = [
        5,    # "V"
        9,    # "IX"
        40,   # "XL"
        1904, # "MCMIV"
        3749, # "MMMDCCXLIX"
        58,   # "LVIII"
        1994  # "MCMXCIV"
    ]
    for num in tasks:
        print("=========================================")
        print(f"Input: {num}")
        res = IntToRoman.convert(num)
        print(f"Result: {res}")
##
