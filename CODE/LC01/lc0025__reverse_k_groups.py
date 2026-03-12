# lc0025__reverse_k_groups.py
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0025__reverse_k_groups import *

# RELOAD:
# import importlib; import lc0025__reverse_k_groups; importlib.reload(lc0025__reverse_k_groups); from lc0025__reverse_k_groups import *

# The idea: reverse each group by standard list reversal.
# - Build arrays of group-first- and group-last elements:
#       +     +     +    - groupFirst
# dummy>1>2>3>4>5>6>7>8>0, k=3
#     ^     ^     ^   0  - groupLast
# (reverse each group individually)
# - Loop starting from the last _complete_ group:
#        (the group is complete when groupLast[i] is not None) 
# -- groupLast[i].next = None  # null-0 terminate to enable reversal
# -- reverse group #i
# -- swap groupFirst[i] and groupLast[i]
# (reconnect the groups)
# - Loop for each i:
# -- groupLast[i].next = groupFirst[i+1]
# - if needed, treat edge cases

from UTILS.lib__linked_list import *

# The main function
def reverse_k_groups(head: Node, k: int) -> Node:
    if ( (head is None) or (head.next is None) ):
         return head
    groupFirst, groupLast = _find_groups(head, k)
    # for p in groupFirst:  print(p.data, ">")
    # for p in groupLast:  print(p.data if p is not None else "None", ">")
    groupFirstR, groupLastR = _reverse_in_groups(groupFirst, groupLast)
    # for p in groupFirstR:  print(p.data if p is not None else "None", ">")
    # for p in groupLastR:  print(p.data if p is not None else "None", ">")
    newHead = _reconnect_groups(groupFirstR, groupLastR)
    # print(LinkedList.list_to_string(newHead))
    return newHead
##


def _reverse_linked_list(head: Node) -> Node:
    if ( (head is None) or (head.next is None) ):
        return(head)
    prev = None
    curr = head
    while ( curr is not None ):
        next = curr.next
        #print(f"curr={curr.data}, next={next.data if (next is not None) else 'None'}")
        curr.next = prev
        #print(f"Set curr.next to: {curr.next.data if (curr.next is not None) else 'None'}")
        prev = curr
        curr = next
    return(prev)
##


# Returns tuple of arrays groupFirst, groupLast
# Assumes list is not empty
def _find_groups(listHead: Node, k:int) -> tuple[list[Node], list[Node]]:
#  0 1 2 3 4 5 6 7
#  +     +     +    - groupFirst
# >1>2>3>4>5>6>7>8>0, k=3
#      ^     ^   0  - groupLast
    groupFirst = [];  groupLast = []
    i = 0
    p = listHead
    while ( p is not None ):
        if ( i % k == 0 ):
            # group starts at current element
            groupFirst.append(p)
        if ( (i > 0) and ((i+1) % k == 0) ):
            # prev group ends at current element
            groupLast.append(p)
        elif ( p.next is None ):# last !incomplete! group ends at current element
            groupLast.append(None)
        p = p.next
        i += 1
    return (groupFirst, groupLast)
##


# Marks group ends with None-s, reverses each group, swaps first-last
def _reverse_in_groups(groupFirst: list[Node], groupLast: list[Node]) -> tuple[list[Node], list[Node]]:
    if ( len(groupFirst) != len(groupLast) ):
        raise Exception("Different lengths of group first/last pointers")
    for i in range(0, len(groupFirst)):
        if ( groupLast[i] is None ):
            continue  # skip incomplete (the last) group
        groupLast[i].next = None  # terminate the group for reversal
        newHead = _reverse_linked_list(groupFirst[i])
        if ( newHead != groupLast[i] ):
            raise Exception("newHead != groupLast[i]")
        # swap groupFirst[i] and groupLast[i]
        tmp = groupFirst[i]
        groupFirst[i] = groupLast[i]
        groupLast[i] = tmp
    return (groupFirst, groupLast)
##


# Connects end of each group to start of next group.
# Returns pointer to the head.
def _reconnect_groups(groupFirst: list[Node], groupLast: list[Node]) -> Node:
    for i in range(0, len(groupLast)-1):
        if ( groupLast[i] is not None  ): # any group but the last-incomplete
            groupLast[i].next = groupFirst[i+1]
    return groupFirst[0]
##


def test__reverse_k_groups():
    tasks = [
        [[1,2,3,4,5,6,7,8], 3],       # [3,2,1,6,5,4,7,8]
        [[1,2,3,4,5,6], 3],           # [3,2,1,6,5,4]
        [[], 2],                      # []
        [[1], 2],                     # [1]
        [[1,2,3], 3]                  # [3,2,1]
    ]
    for pyList, k  in tasks:
        print("=================================")
        linkedList = LinkedList.from_python_list(pyList)
        print(f"Input: {LinkedList.list_to_string(linkedList.head)}, k={k}")
        newHead = reverse_k_groups(linkedList.head, k)
        print(f"Result: {LinkedList.list_to_string(newHead)}")
##
    

# l1 = LinkedList.from_python_list([1,2,3,4,5,6,7,8])
#
# groupFirst, groupLast = _find_groups(l1.head, 3)
# for p in groupFirst:  print(p.data, ">")
# for p in groupLast:  print(p.data if p is not None else "None", ">")
#
# groupFirstR, groupLastR = _reverse_in_groups(groupFirst, groupLast)
# for p in groupFirstR:  print(p.data if p is not None else "None", ">")
# for p in groupLastR:  print(p.data if p is not None else "None", ">")
#
# newHead = _reconnect_groups(groupFirstR, groupLastR)
# print(LinkedList.list_to_string(newHead))
