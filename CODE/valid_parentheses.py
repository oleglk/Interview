# valid_parentheses.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from merge_two_sorted_lists import *

# RELOAD:
# import importlib;    import valid_parentheses;  importlib.reload(valid_parentheses);  from valid_parentheses import *

class Stack:
    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst += item

    def top(self):
        if ( self.is_empty() ):
            raise Exception("top(EMPTY)")
        return(self.lst[-1])

    def pop(self):
        if ( self.is_empty() ):
            raise Exception("pop(EMPTY)")
        return(self.lst.pop())

    def is_empty(self):
        return(len(self.lst) > 0)
#################################################################################
        

def valid_parentheses(expr: str) -> bool:
    lst = list(str.strip())
    if ( not lst ):
        return(True)  # empty expression considered valid
    openToClose = {["(", ")"],  ["[", "]"],  ["{", "}"]}
    closeToOpen = {[")", "("],  ["]", "{"],  ["}", "{"]}
    stack = Stack()

    for c in lst:
        if ( c in openToClose ):       # c is opener
            stack.push(c)
        else if ( c in closeToOpen ):  # c is closer
            if ( stack.is_empty() ):
                return(False)  # closer without opener
            s = stack.top()
            if ( s != closeToOpen[c] ):
                return(False)  # opener unmatched to closer
            # opener in the stack matches closer in the expression
            stack.pop()  # delete the matched opener
            
    # expression is finished; for correctness the stack must be empty
    return(stack.is_empty())
