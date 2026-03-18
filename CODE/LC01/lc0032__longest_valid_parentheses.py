# lc0032__longest_valid_parentheses.py
# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0032__longest_valid_parentheses import *

# RELOAD:
# import importlib; import lc0032__longest_valid_parentheses; importlib.reload(lc0032__longest_valid_parentheses); from lc0032__longest_valid_parentheses import *

# The idea:
# Start by creating an empty stack and push -1 into it.
# Iterate over the given string.
#   - Whenever you encounter ‘(‘, push the current index in the stack.
#   - Whenever you encounter ‘)‘:
#     -- Pop the top index from the stack.
#     -- Now, if the stack is empty, push the current index in it. Otherwise, we have found a valid substring. Find its length by subtracting the current index from the top element.
#     -- Update the maximum length if required.

# See https://www.naukri.com/code360/problems/longest-valid-parentheses_1089563
# See https://www.geeksforgeeks.org/dsa/length-of-the-longest-valid-substring/

# Example 1: "(()"
# s(-1,)
# v[0]=( -> s(-1,0,)
# v[1]=( -> s(-1,0,1,)
# v[2]=) -> s(-1,0,) -> not-empty -> L=2-0=2
# Example 2: ")()()"
# s(-1,)
# v[0]=) -> s(,) -> empty -> s(0,)
# v[1]=( -> s(0,1,)
# v[2]=) -> s(0,) -> not-empty L=2-0=2
# v[3]=( -> s(0,3,)
# v[4]=) -> s(0,) -> not-empty L=4-0=4
# Example 3: "(()()"
# s(-1,)
# v[0]=( -> s(-1,0,)
# v[1]=( -> s(-1,0,1,)
# v[2]=) -> s(-1,0,) -> not-empty L=2-0=2
# v[3]=( -> s(-1,0,3)
# v[4]=) -> s(-1,0) -> not-empty L=4-0=4
# Example 4: "(()))"
# s(-1,)
# v[0]=( -> s(-1,0,)
# v[1]=( -> s(-1,0,1,)
# v[2]=) -> s(-1,0,) -> not-empty L=2-0=2
# v[3]=) -> s(-1,) -> not-empty L=3-(-1)=4
# v[4]=) -> s(,) -> empty -> s(4,)


def longest_valid_parentheses(s: str) -> int:
    stack = [-1]
    maxLength = 0
    if ( (s is None) or (s == "") ):
        return 0
    for i, c in enumerate(s):
        if ( c == '(' ):
            stack.append(i)
        else:  # c == ')'
            stack.pop()
            if ( len(stack) == 0 ):  # unmatched closing - reset expression
                stack.append(i)
            else:                    # valid substring
                l = i - stack[-1]
                maxLength = max(maxLength, l)
    return maxLength
##


def test__longest_valid_parentheses():
    tasks = [
        "((()",        # 2
        ")()()",       # 4
        "(()()",       # 4
        "(()))",       # 4
        ")()())",      # 4
    ]
    for s in tasks:
        print("========================================")
        print(f"Input: {s}")
        res = longest_valid_parentheses(s)
        print(f"Result: {res}")
##
