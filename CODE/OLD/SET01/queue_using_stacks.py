# queue_using_stacks.py - Implement a FIFO queue using only two stacks.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from queue_using_stacks import *

# RELOAD:
# import importlib;    import queue_using_stacks;  importlib.reload(queue_using_stacks);  from queue_using_stacks import *


# The idea: 1st stack for input, 2nd for output. When pop() depletes 2nd stack, for next pop() move all elements from 1st into 2nd, then serve pop() from 2nd.
## Example:
## s1 <= 123(t)
## s2 <= 321(t)
## s2.pop(1) => 32(t)
## s2.pop(2) => 3(t)
## s2.pop(3) => (t)
## s1 <= 45(t)
## s2 <= 54(t)
## s2.pop(4) => 5(t)
## s2.pop(5) => (t)


class QueueUsingStacks:
    def __init__(self):
        self.inpStack = []
        self.outStack = []

    def enque(self, x):
        self.inpStack.append(x)

    def deque(self):
        if ( self.is_empty() ):
            raise Exception("pop(EMPTY)")
        if ( len(self.outStack) == 0 ):
            self._move_all()
        x = self.outStack.pop(-1)
        return(x)

    def first(self):
        if ( self.is_empty() ):
            raise Exception("top(EMPTY)")
        if ( len(self.outStack) == 0 ):
            self._move_all()
        x = self.outStack[-1]
        return(x)

    def is_empty(self):
        return((len(self.inpStack) == 0) and (len(self.outStack) == 0))

    def _move_all(self):
        while ( len(self.inpStack) > 0 ):
            x = self.inpStack.pop(-1)
            self.outStack.append(x)
######


def test__QueueUsingStacks():
    qu = QueueUsingStacks()
    l1 = [1,2,3]
    for x in l1:  print(f"Enque:{x}");  qu.enque(x)
    x = qu.deque();  print(f"---- Deque:{x}")
    x = qu.deque();  print(f"---- Deque:{x}")
    l2 = [4,5]
    for x in l2:  print(f"Enque:{x}");  qu.enque(x)
    while ( not qu.is_empty() ):
        x = qu.deque();  print(f"---- Deque:{x}")
