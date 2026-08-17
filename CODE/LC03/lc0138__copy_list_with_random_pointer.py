# lc0138__copy_list_with_random_pointer.py
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0138__copy_list_with_random_pointer import *

# RELOAD:
# import importlib;    import lc0138__copy_list_with_random_pointer;  importlib.reload(lc0138__copy_list_with_random_pointer);  from lc0138__copy_list_with_random_pointer import *

# The idea: in the first stage traverse the list and build all nodes' clones; store {old-node :  new-node} in nodeMap dict. In the second traversal install the pointers.
# See: https://www.geeksforgeeks.org/dsa/a-linked-list-with-next-and-arbit-pointer/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None
    ##
####


def copy_list_with_random_pointer(oldHead: Node) -> Node:
    if ( oldHead is None ):
        return None
    nodeMap = {}
    
    # clone all nodes
    curr = oldHead
    while ( curr is not None ):
        nodeMap[curr] = Node(curr.data)
        curr = curr.next

    # install the pointers
    curr = oldHead
    while ( curr is not None ):
        if ( curr.next is not None ):
            nodeMap[curr].next = nodeMap[curr.next]
        else:
            nodeMap[curr].next = None
        if ( curr.random is not None ):
            nodeMap[curr].random = nodeMap[curr.random]
        else:
            nodeMap[curr].random = None
        curr = curr.next

    return nodeMap[oldHead]
##


def printList(head):
    curr = head
    while curr is not None:
        print(f'{curr.data}(', end='')
        if curr.random:
            print(f'{curr.random.data})', end='')
        else:
            print('null)', end='')
        
        if curr.next is not None:
            print(' -> ', end='')
        curr = curr.next
    print()
##

    
def test__copy_list_with_random_pointer():
    # [[7,null],[13,0],[11,4],[10,2],[1,0]]
    l1n0 = Node(7);  l1n1 = Node(13);  l1n2 = Node(11)
    l1n3 = Node(10);  l1n4 = Node(1)
    l1n0.next = l1n1;  l1n1.next = l1n2;
    l1n2.next = l1n3;  l1n3.next = l1n4;  l1n4.next = None
    l1n0.random = None;  l1n1.random = l1n0;  l1n2.random = l1n4
    l1n3.random = l1n2;  l1n4.random = l1n0
    # [[1,1],[2,1]]
    l2n0 = Node(1);  l2n1 = Node(2)
    l2n0.next = l2n1;  l2n1.next = None
    l2n0.random = l2n1;  l2n1.random = l2n1

    tasks = [l1n0, l2n0]
    for head in tasks:
        print("=================================================")
        print("Input: ", end='')
        printList(head)
        res = copy_list_with_random_pointer(head)
        print("Result: ", end='')
        printList(res)
##
