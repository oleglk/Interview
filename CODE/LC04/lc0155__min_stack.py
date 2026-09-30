# lc0155__min_stack.py
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
#    MinStack() initializes the stack object.
#    void push(int value) pushes the element value onto the stack.
#    void pop() removes the element on the top of the stack.
#    int top() gets the top element of the stack.
#    int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0155__min_stack import *

# RELOAD:
# import importlib;    import lc0155__min_stack;  importlib.reload(lc0155__min_stack);  from lc0155__min_stack import *

# The idea: maintain same-size second stack with min-so-far values.
# See: https://medium.com/@saipranavmoluguri2001/why-interviewers-love-the-min-stack-problem-and-the-trick-that-solves-it-instantly-13a3de5f8f22


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    ##

    
    def push(self, val: int) -> None:
        n = len(self.stack)
        self.stack.append(val)
        if ( n > 0 ):
            self.minStack.append( min(val, self.minStack[n-1]) )
        else:
            self.minStack.append( val )
    ##


    def pop(self) -> None:
        if ( len(self.stack) == 0 ):
            raise Exception("pop() from empty stack")
        self.stack.pop()
        self.minStack.pop()
    ##


    def top(self) -> int:
        n = len(self.stack)
        if ( n == 0 ):
            raise Exception("top() from empty stack")
        return self.stack[n-1]
    ##


    def get_min(self) -> int:
        n = len(self.stack)
        if ( n == 0 ):
            raise Exception("get_min() from empty stack")
        return self.minStack[n-1]
    ##
####


def test__min_stack():
    st = MinStack()
    st.push(-2);  print("Push -2")
    st.push(0);   print("Push  0")
    st.push(-3);  print("Push -3")
    m = st.get_min();  t = st.top();  print(f"min={m}, top={t}")
    st.pop();     print("Pop")
    m = st.get_min();  t = st.top();  print(f"min={m}, top={t}")
    
