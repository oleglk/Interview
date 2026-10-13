# lc0168__excel_sheet_column_title.py
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0168__excel_sheet_column_title import *

# RELOAD:
# import importlib;    import lc0168__excel_sheet_column_title;  importlib.reload(lc0168__excel_sheet_column_title);  from lc0168__excel_sheet_column_title import *

# The idea: work similar to conversion into base26, but each time subtract 1 to bring the current number into 0-based. Build list of digits, at the end reverse it and convert into string.
# See: https://algo.monster/liteproblems/168


def excel_sheet_column_title(columnNumber: int) -> str:
    result = []
    while ( columnNumber > 0 ):
        columnNumber -= 1  # bring current digit to 0-based
        currDigit = columnNumber % 26
        currChar = chr( ord("A") + currDigit )
        result.append(currChar)
        columnNumber //= 26  # move to next digit
    return "".join( result[::-1] )  # reverse then join
##


def test__excel_sheet_column_title():
    tasks = [
        1,        # "A"
        28,       # "AB"
        701,      # "ZY"
    ]
    for columnNumber in tasks:
        print("==================================")
        print(f"Input: {columnNumber}")
        res = excel_sheet_column_title(columnNumber)
        print(f"Result: {res}")
##
