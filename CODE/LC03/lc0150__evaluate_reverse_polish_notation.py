# lc0150__evaluate_reverse_polish_notation.py
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
#    The valid operators are '+', '-', '*', and '/'.
#    Each operand may be an integer or another expression.
#    The division between two integers always truncates toward zero.
#    There will not be any division by zero.
#    The input represents a valid arithmetic expression in a reverse polish notation.
#    The answer and all the intermediate calculations can be represented in a 32-bit integer.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0150__evaluate_reverse_polish_notation import *

# RELOAD:
# import importlib;    import lc0150__evaluate_reverse_polish_notation;  importlib.reload(lc0150__evaluate_reverse_polish_notation);  from lc0150__evaluate_reverse_polish_notation import *

# The idea traverse expression tokens from left to right. If token is not an operator, push it into stack. If token is operator, pop right operand, pop left operand, perform the operation, push the result.
# The ultimate result is in the stack when expression is exhausted.
# See: https://www.geeksforgeeks.org/dsa/evaluate-the-value-of-an-arithmetic-expression-in-reverse-polish-notation-in-java/


def evaluate_reverse_polish_notation(exprStr: str) -> int:
    if ( not exprStr ):  return 0
    expr = exprStr.split()  # convert to list
    stack = []
    for token in expr:
        if ( token not in "+-*/" ):  # token is numeric operand
            stack.append(int(token))
            continue
        else:                        # token is operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            match token:
                case '+':
                    stack.append(operand1 + operand2)
                case '-':
                    stack.append(operand1 - operand2)
                case '*':
                    stack.append(operand1 * operand2)
                case '/':
                    # unclear whether and why abs() needed,
                    # but it's needed for some inputs and not for other inputs
                    # stack.append(operand1 // abs(operand2))
                    stack.append(operand1 // operand2)
    # now the expression is exhausted, and the final result is in the stack
    return stack.pop()
##


def test__evaluate_reverse_polish_notation():
    tasks = [
        "2 1 + 3 *",                      # 9
        "4 13 5 / +",                     # 6
        "10 6 9 3 + -11 * / * 17 + 5 +",  # 22
    ]
    for exprStr in tasks:
        print("==============================================")
        print(f"Input: {exprStr}")
        res = evaluate_reverse_polish_notation(exprStr)
        print(f"Result: {res}")
##
