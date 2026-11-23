# lib__double_linked_list.py - double linked list implementation 

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from UTILS.lib__double_linked_list import *

# RELOAD:
# import importlib;  import UTILS.lib__double_linked_list;  importlib.reload(UTILS.lib__double_linked_list);  from UTILS.lib__double_linked_list import *


class DoubleLinkedListNode:
    def __init__(self, elem, prev, next):
        self.elem = elem   # Value for this node
        self.prev = prev   # Pointer to previous node in list
        self.next = next   # Pointer to next node in list
####


class DoubleLinkedList:
    def __init__(self):
        self._head = None    # Pointer to list header
        self._tail = None    # Pointer to list tail
        self._listSize = 0   # Size of list


    def add_in_head(self, x):
        was_empty = self.is_empty()
        newNode = DoubleLinkedListNode(x, None, self._head)
        if ( not was_empty ):
            self._head.prev = newNode
        else:
            self._tail = newNode
        self._head = newNode
        self._listSize += 1
        return(newNode)


    def add_in_tail(self, x):
        was_empty = self.is_empty()
        newNode = DoubleLinkedListNode(x, self._tail, None)
        if ( not was_empty ):
            self._tail.next = newNode
        else:
            self._head = newNode
        self._tail = newNode
        self._listSize += 1
        return(newNode)


    def delete_by_node(self, node):
        """Deletes list member 'node'"""
        if ( node is None ):
            raise Exception("delete_by_node(None)")
        if ( node.prev is not None):  # not the first node
            node.prev.next = node.next
        else:
            self._head = node.next
        if ( node.next is not None):  # not the last node
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        self._listSize -= 1


    def delete_head(self):
        """Deletes the head node and returns its data element"""
        if ( self.is_empty() ):
            return
        oldHead = self._head
        self.delete_by_node(oldHead)
        return(oldHead.elem)


    def delete_first_by_elem(self, x):
        """Deletes 1st occurence of a node with element == 'x'
           Returns True if deletion occured"""
        node = self._head
        while ( (node is not None) and (node.elem != x) ):
            node = node.next
        if ( node is not None ):  # 'x' found
            self.delete_by_node(node)
            return(True)
        else:                     # 'x' not found
            return(False)


    def move_to_tail(self, node):
        data = node.elem
        self.delete_by_node(node)
        self.add_in_tail(data)

        
    def is_empty(self):
        return(self._head is None)

    
    def size(self):
        return self._listSize


    def content_to_string(self):
        s = ""
        node = self._head
        while ( node is not None ):
            s += " >> " + str(node.elem)
            node = node.next
        return(s)

    
    #staticmethod
    def from_python_list(pyList):
        lst = DoubleLinkedList()
        if ( not pyList ):
            return(lst)
        for x in pyList:
            lst.add_in_tail(x)
        return(lst)

######
