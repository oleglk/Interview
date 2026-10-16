# lc0171__excel_sheet_column_number.py
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0171__excel_sheet_column_number import *

# RELOAD:
# import importlib;    import lc0171__excel_sheet_column_number;  importlib.reload(lc0171__excel_sheet_column_number);  from lc0171__excel_sheet_column_number import *

# The idea: perform in left-to-right order res = res*26 + currentCode, where currentCode = ord(currentChar) - ord('A') + 1. +1 performed to adjust for 1-based indexing.
# See: https://algo.monster/liteproblems/171


def excel_sheet_column_number(columnTitle: str) -> int:
    result = 0
    for currentChar in columnTitle:
        currentCode = ord(currentChar) - ord('A') + 1
        result = result * 26 + currentCode
    return result
##


def test__excel_sheet_column_number():
    tasks = [
        'A',          # 1
        'AB',         # 28
        'ZY',         # 701
    ]
    for columnTitle in tasks:
        print("========================================")
        print(f"Input: {columnTitle}")
        res = excel_sheet_column_number(columnTitle)
        print(f"Result: {res}")
##
