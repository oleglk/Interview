# evaluate_rpn.py - Evaluate Reverse Polish Notation using stack. Assume all operators are binary. Use integer arithmetics.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from evaluate_rpn import *

# RELOAD:
# import importlib; import evaluate_rpn; importlib.reload(evaluate_rpn); from evaluate_rpn import *


# The idea: if operand encountered, push it; if operator encountered, pop two operands, calculate result, then push the result.


def evaluate_rpn(exprStr: str) -> int:
    stack = []
    expr = exprStr.split()  # make a list with expression
    for token in expr:
        if ( token not in ['+', '-', '*', '/'] ):  # operand - push it
            stack.append(token)
            continue
        # operator - pop operands, calc and push the result
        if ( len(stack) < 2 ):
            raise Exception(f"Insufficient stack entries: {stack} while two operands needed")
        b = int(stack.pop())
        a = int(stack.pop())
        if (   token == '+' ):
            stack.append(a + b)
        elif ( token == '-' ):
            stack.append(a - b)
        elif ( token == '*' ):
            stack.append(a * b)
        elif ( token == '/' ):
            stack.append(a / b)
    # the expression ended
    if ( len(stack) < 1 ):
        raise Exception(f"Missing result in stack")
    res = int(stack.pop())
    return res


def test__evaluate_rpn():
    tasks = ["2 3 +",  # 5
             "4 13 5 / +",  # 6
             "2 1 + 3 *" ,  # 9
             "10 6 9 3 + -11 * / * 17 + 5 +"  # 22
             ]
    for exprStr in tasks:
        print("============================")
        print(f"Input:  {exprStr}")
        res = evaluate_rpn(exprStr)
        print(f"Result: {res}")

             
