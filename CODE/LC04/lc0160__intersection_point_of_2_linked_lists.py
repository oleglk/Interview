# lc0160__intersection_point_of_2_linked_lists.py
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0160__intersection_point_of_2_linked_lists import *

# RELOAD:
# import importlib;    import lc0160__intersection_point_of_2_linked_lists;  importlib.reload(lc0160__intersection_point_of_2_linked_lists);  from lc0160__intersection_point_of_2_linked_lists import *


# The idea: advance longer list head by length diff, then traverse 2 lists one element at a time until common node encountered.
# See: https://www.geeksforgeeks.org/dsa/write-a-function-to-get-the-intersection-point-of-two-linked-lists/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    ##
    

def measure_list_length(head: Node|None) -> int:
    if ( head is None ):
        return 0
    lng = 1
    while ( head.next is not None ):
       lng += 1
       head = head.next
    return lng
##


def find_intersect_given_diff(longerHead: Node, shorterHead: Node, \
                              diff: int) -> Node:
    # advance longest list head 'diff' times
    for _ in range(diff):
        longerHead = longerHead.next
    # advance both heads synchronously until intersection found
    while ( longerHead is not None ):
        if ( longerHead == shorterHead ):  # intersection found
            return shorterHead
        longerHead = longerHead.next
        shorterHead = shorterHead.next
    return None  # intersection isn't found
##


def intersection_point_of_2_linked_lists(headA: Node, headB: Node) -> Node:
    lA = measure_list_length(headA)
    lB = measure_list_length(headB)
    if ( lA >= lB ):
        return find_intersect_given_diff(headA, headB, lA-lB)
    else:
        return find_intersect_given_diff(headB, headA, lB-lA)
##


def test__intersection_point_of_2_linked_lists():
    # 1 -> 2 -> 3 -> 4
    #           ^
    #      5 -> |
    n11 = Node(1); n12 = Node(2); n13 = Node(3); n14 = Node(4); n15 = Node(5)
    n11.next = n12; n12.next = n13; n13.next = n14; n15.next = n13

    tasks = [
        [n11, n15]  # n3
    ]
    for headA, headB in tasks:
        print("==============================================")
        print(f"Heads: {headA.data}, {headB.data}")
        res = intersection_point_of_2_linked_lists(headA, headB)
        print(f"Result: {res.data}")
##
