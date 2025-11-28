# min_stack.py - Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from min_stack import *

# RELOAD:
# import importlib;    import min_stack;  importlib.reload(min_stack);  from min_stack import *

# The idea: maintain a secondary stack of the same size containing current minimum values.


class MinStack:
    def __init__(self):
        self.data = []     # primary stack
        self.minVals = []  # seconary stack

    def push(self, v):
        if self.is_empty():
            minV = v
        else:
            minV = min(v, self.minVals[-1])
        self.data.append(v)
        self.minVals.append(minV)

    def top(self):
        if ( self.is_empty() ):
            raise Exception("top(EMPTY)")
        return(self.data[-1])

    def get_min(self):
        if ( self.is_empty() ):
            raise Exception("min(EMPTY)")
        return(self.minVals[-1])
    
    def pop(self):
        if ( self.is_empty() ):
            raise Exception("pop(EMPTY)")
        v = self.data.pop(-1)
        self.minVals.pop(-1)
        return(v)

    def is_empty(self):
        return(len(self.data) == 0)

    def content(self):
        return([x for x in self.data])

    def from_list(self, lst):
        self.data = [];  self.minVals = []
        for x in lst:
            self(push(x))
####


def test__MinStack():
    st = MinStack()
    lists = [ [1,2,3], [10,1,2,20], [4,3,2,1] ]
    for lst in lists:
        print("=======================")
        for x in lst:
            st.push(x)
            print(f"After push({x}):  Content={st.content()}, min={st.get_min()}")
        while ( not st.is_empty() ):
            x = st.pop()
            minV = "NONE" if st.is_empty()  else  st.get_min()
            print(f"After pop({x}):  Content={st.content()}, min={minV}")
