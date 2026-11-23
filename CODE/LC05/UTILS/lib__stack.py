# lib__stack.py

class Stack:
    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst.append(item)

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
