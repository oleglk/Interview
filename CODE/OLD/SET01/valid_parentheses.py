# valid_parentheses.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from valid_parentheses import *

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
        return(len(self.lst) == 0)

    def content(self):
        return(self.lst)
#################################################################################
        

def valid_parentheses(expr: str) -> bool:
    lst = list(expr.strip())
    if ( not lst ):
        return(True)  # empty expression considered valid
    openToClose = {"(": ")",  "[": "]",  "{": "}"}
    closeToOpen = {")": "(",  "]": "[",  "}": "{"}
    stack = Stack()

    for c in lst:
        if ( c in openToClose ):       # c is opener
            stack.push(c)
            print(f"+ '{c}' considered opener")
        elif ( c in closeToOpen ):  # c is closer
            print(f"+ '{c}' considered closer")
            if ( stack.is_empty() ):
                print(f"* Stack is empty")
                return(False)  # closer without opener
            s = stack.top()
            if ( s != closeToOpen[c] ):
                print(f"* Open-closer mismatch: '{s}' <=> '{c}'; expected opener '{closeToOpen[c]}'")
                return(False)  # opener unmatched to closer
            # opener in the stack matches closer in the expression
            print(f"+ Open-closer match: '{s}' <=> '{c}'")
            stack.pop()  # delete the matched opener
        else:
            raise Exception(f"Invalid character '{c}' in '{expr}'")
            
    # expression is finished; for correctness the stack must be empty
    if ( not stack.is_empty() ):
        print(f"* Finished with non-empty stack: {''.join([str(x) for x in stack.content()])}")
    return(stack.is_empty())


def test__valid_parentheses():
    expr01 = "[{}][]"         # good
    expr02 = "[(])"           # bad
    expr03 = "["              # bad
    expr04 = "}"              # bad
    expr05 = "([[({})]]){}"   # good
    for exp in [expr01, expr02, expr03, expr04, expr05]:
        print("====================")
        res = valid_parentheses(exp)
        print(f"Expression '{exp}'\t=> {res}")
