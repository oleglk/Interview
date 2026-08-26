# lc0147__insertion_sort_list.py
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
# The steps of the insertion sort algorithm:
#    Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
#    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
#    It repeats until no input elements remain.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0147__insertion_sort_list import *

# RELOAD:
# import importlib;    import lc0147__insertion_sort_list;  importlib.reload(lc0147__insertion_sort_list);  from lc0147__insertion_sort_list import *

# The idea: traverse the list with prevNode, currNode pair. Whenever value of currNode is smaller than that of prevNode, move currNode into its place while searching for it from the head.
# See https://algo.monster/liteproblems/147


from UTILS.lib__linked_list import *

# Class Node imported from lib__linked_list.py :
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # Pointer to the next node
####


def insertion_sort_list(head: Node) -> Node:
    if ( (head is None) or (head.next is None) ):
        return head
    dummyHead = Node(float('-inf'))
    dummyHead.next = head
    # move the pair of 'prevNode', 'currNode' over the list
    prevNode = head
    currNode = head.next
    while ( currNode is not None ):
        if ( currNode.data > prevNode.data ):  # 'currNode' already in place
            prevNode = currNode
            currNode = currNode.next
            continue  # we just moved to the next node
        # find where to insert 'currNode'
        insertPos = dummyHead  # insertion position is right after it
        while ( insertPos.next.data < currNode.data ):  # limit known to exist
            insertPos = insertPos.next
        # remove 'currNode' from its old position
        nextToProcess = currNode.next
        prevNode.next = nextToProcess
        # insert 'currNode' into its new position
        currNode.next = insertPos.next
        insertPos.next = currNode
        currNode = nextToProcess  # arrange for continuing list traversal
    return dummyHead.next
##


def print_list(node):
    if node is None:
        return
    while node is not None:
        print(f"{node.data}->", end="")
        node = node.next
##


def test__insertion_sort_list():
    tasks = [
        [4,3,2,1],   # [1,2,3,4]
        [1,5,2,4,3], # [1,2,3,4,5]
    ]
    for pyList in tasks:
        print("===============================================")
        lst = LinkedList.from_python_list(pyList)
        print("Input: ", end='')
        print_list(lst.head);        print("")
        res = insertion_sort_list(lst.head)
        print("Result: ", end='')
        print_list(res);        print("")
##
