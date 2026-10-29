# lc0194__transpose_file.py
# Given a text file file.txt, transpose its content - print the output.
# You may assume that each row has the same number of columns, and each field is separated by the ' ' character.
# Example:
#  If file.txt has the following content:
#    name age
#    alice 21
#    ryan 30
#  Output the following:
#    name alice ryan
#    age 21 30

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0194__transpose_file import *

# RELOAD:
# import importlib;    import lc0194__transpose_file;  importlib.reload(lc0194__transpose_file);  from lc0194__transpose_file import *

# The idea: represent the original text as list of row-lists, then retrieve words in column order.
# See: https://algomap.io/question-bank/transpose-file


import io


def transpose_file(inpStr: str) -> None:
    # represent the original text as list of row-lists
    lineIterator = io.StringIO(inpStr)
    rowLists = [line.strip().split() for line in lineIterator]
    
    # determine max number of columns in a line
    maxColumns = max(len(row) for row in rowLists)

    # traverse the text in column order and print the words
    for colIdx in range(0, maxColumns):
        columnText = []
        for row in rowLists:
            if ( colIdx < len(row) ):  # if this row has enough columns
                columnText.append(row[colIdx])
        print(" ".join(columnText))
##


def test__transpose_file():
    inpStr = """name age
alice 21
ryan 30"""
    print("=====================================")
    print(f"Input: {inpStr}")
    print("Result:")
    transpose_file(inpStr)
##
