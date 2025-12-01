# zigzag_conversion.py - Convert a string to a zigzag pattern on a given number of rows and read line by line.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from zigzag_conversion import *

# RELOAD:
# import importlib; import zigzag_conversion; importlib.reload(zigzag_conversion); from zigzag_conversion import *

# The idea: create array of 'nRows' strings; at each step append one character to current row, then move to next row. Row order goes top-down-top. Return concatenation of the per-row strings.

def zigzag_conversion(s: str, nRows: int) -> str:
    n = len(s)
    if ( (nRows <= 1) or (len(s) <= nRows) ):
        return(str)
    rowLists = []  # initialize list of per-row lists
    for i in range(0, nRows):
        rowLists.append([])
    # spread characters into rows
    iChar = 0
    while ( iChar < n ):
        # traverse rows top-down
        for curRow in range(0, nRows):  # include #0, #last
            if ( iChar >= n ):
                break
            rowLists[curRow].append(s[iChar])
            print(f"@@ TD Append {s[iChar]} to #{curRow} --> '{rowLists[curRow]}'")
            iChar += 1
        # traverse rows bottom-up
        for curRow in range(nRows-2, 0, -1):  # exclude #0, #last
            if ( iChar >= n ):
                break
            rowLists[curRow].append(s[iChar])
            print(f"@@ BU Append {s[iChar]} to #{curRow} --> '{rowLists[curRow]}'")
            iChar += 1
    # concatenate per-row lists and convert to string
    flatList = []
    for rowList in rowLists:
        flatList.extend(rowList)
    resultStr = "".join(flatList)
    return(resultStr)


def test__zigzag_conversion():
    tasks = [["12345", 2],  ["PAYPALISHIRING", 3]]
    for str, nRows in tasks:
        print("===================")
        print(f"Input: '{str}', {nRows}")
        res = zigzag_conversion(str, nRows)
        print(f"Result: '{res}'")
