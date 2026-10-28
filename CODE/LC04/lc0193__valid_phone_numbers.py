# lc0193__valid_phone_numbers.py
# Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.
# You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
# You may also assume each line in the text file must not contain leading or trailing white spaces.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0193__valid_phone_numbers import *

# RELOAD:
# import importlib;    import lc0193__valid_phone_numbers;  importlib.reload(lc0193__valid_phone_numbers);  from lc0193__valid_phone_numbers import *

# The idea: have the input as a single string of '\n' separated records. Read the string line-by-line and match regex for the two formats.

import re

def valid_phone_numbers(recordsStr: str) -> list[str]:
    pattern1 = r"^\(\d{3}\) \d{3}-\d{4}$"
    pattern2 = r"^\d{3}-\d{3}-\d{4}$"
    validNumbers = []
    for record in recordsStr.splitlines():
        if ( re.match(pattern1, record) or re.match(pattern2, record) ):
            validNumbers.append(record)
    return validNumbers
##


def test__valid_phone_numbers():
    tasks = """
987-123-4567
123 456 7890
(123) 456-7890
"""
    print("==============================================")
    print(f"Input:\n{tasks}")
    res = valid_phone_numbers(tasks)
    print(f"Result:\n{res}")
##

