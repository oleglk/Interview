# lc0020__valid_parentheses.py

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0020__valid_parentheses import *

# RELOAD:
# import importlib; import lc0020__valid_parentheses; importlib.reload(lc0020__valid_parentheses); from lc0020__valid_parentheses import *

# The idea: push openers into stack, for closers check if stack-top contains matching opener; if yes, pop it, otherwise complain. At the end of expression the stack should be empty.


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def is_empty(self):
        return (len(self.arr) == 0)

    def pop(self):
        if ( self.is_empty() ):
            raise Exception("pop() from empty stack")
        return self.arr.pop()

    def top(self):
        if ( self.is_empty() ):
            raise Exception("top() for empty stack")
        return self.arr[-1]
####


def is_opener(c: str) -> bool:
    return (c in ('(', '[', '{'))

def is_closer(c: str) -> bool:
    return (c in (')', ']', '}'))

def opener_for(c: str) -> str:
    openersFor = { ')':'(', ']':'[', '}':'{' }
    if ( c in openersFor ):
        return openersFor[c]
    else:
        return ""


def valid_parentheses(expr: str) -> bool:
    stack = Stack()
    for c in expr:
        if ( is_opener(c) ):
            stack.push(c)
            continue
        if ( not is_closer(c) ):
            continue
        # closer; the stack must have its opener
        if ( stack.is_empty() or
             (stack.top() != opener_for(c)) ):
            return False  # non-matching opener or empty stack
        stack.pop()  # pop matching opener
        
    # expression ended; stack must be empty
    return (stack.is_empty())
##


def test__valid_parentheses():
    tasks = [
        "()",           # True
        "()[]{}",       # True
        "([])",         # True
        "([]{()})",     # True
        "(]",           # False
        "([)]",         # False
        "(",            # False
        ")"             # False
    ]
    for expr in tasks:
        print("==================================")
        print(f"Input: {expr}")
        res = valid_parentheses(expr)
        print(f"Result: {res}")
