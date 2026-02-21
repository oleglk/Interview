# lc0006__zigzag_conversion.py
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0006__zigzag_conversion import *

# RELOAD:
# import importlib; import lc0006__zigzag_conversion; importlib.reload(lc0006__zigzag_conversion); from lc0006__zigzag_conversion import *


# The idea: place consequtive characters in array of row-strings; go downwards then upwards, each time appending a char to appropriate row.

def zigzag_conversion(inpStr: str, numRows: int) -> str:
    rows = [""]*numRows
    rowIncr = 1  # row increment is positive/negative when going down/up
    rowIdx = 0
    for ch in inpStr:
        rows[rowIdx] += ch  # append next chat to appropriate row
        if (   (rowIncr > 0) and (rowIdx < numRows-1) ):   # going down
            rowIdx += 1
        elif ( (rowIncr < 0) and (rowIdx > 0) ):           # going up
            rowIdx -= 1
        elif ( (rowIncr > 0) and (rowIdx == numRows-1) ):  # hit the bottom
            rowIdx -= 1
            rowIncr = -1
        elif ( (rowIncr < 0) and (rowIdx == 0) ):          # hit the top
            rowIdx += 1
            rowIncr = 1
        else:
            raise Exception("Should not reach here")
    # build the output string from 'rows' array
    outStr = ""
    for row in rows:
        outStr += row
    return outStr



def test__zigzag_conversion():
    tasks = [
        ["12345", 2],          # "13524"
        ["PAYPALISHIRING", 3]  # "PAHNAPLSIIGYIR"
             ]
    for str, nRows in tasks:
        print("===================")
        print(f"Input: '{str}', {nRows}")
        res = zigzag_conversion(str, nRows)
        print(f"Result: '{res}'")

135
24
